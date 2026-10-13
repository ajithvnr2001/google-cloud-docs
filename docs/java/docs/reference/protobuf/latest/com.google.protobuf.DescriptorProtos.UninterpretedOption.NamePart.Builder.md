---
url: https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DescriptorProtos.UninterpretedOption.NamePart.Builder
title: Class DescriptorProtos.UninterpretedOption.NamePart.Builder (3.19.4) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:31:28.124411+00:00
---

# Class DescriptorProtos.UninterpretedOption.NamePart.Builder (3.19.4)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DescriptorProtos.UninterpretedOption.NamePart.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DescriptorProtos.UninterpretedOption.NamePart.Builder (3.19.4) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public static final class DescriptorProtos.UninterpretedOption.NamePart.Builder extends GeneratedMessageV3.Builder<DescriptorProtos.UninterpretedOption.NamePart.Builder> implements DescriptorProtos.UninterpretedOption.NamePartOrBuilder

The name of the uninterpreted option. Each string represents a segment in a dot-separated name. is_extension is true iff a segment represents an extension (denoted with parentheses in options specs in .proto files). E.g.,{ ["foo", false], ["bar.baz", true], ["qux", false] } represents "foo.(bar.baz).qux".

Protobuf type `google.protobuf.UninterpretedOption.NamePart`

## Inheritance

[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder) > [AbstractMessage.Builder<BuilderType>](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder) > [GeneratedMessageV3.Builder](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder) > DescriptorProtos.UninterpretedOption.NamePart.Builder

## Implements

[DescriptorProtos.UninterpretedOption.NamePartOrBuilder](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DescriptorProtos.UninterpretedOption.NamePartOrBuilder)

## Inherited Members

[AbstractMessage.Builder.findInitializationErrors()](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder#com_google_protobuf_AbstractMessage_Builder_findInitializationErrors__)

[AbstractMessage.Builder.getInitializationErrorString()](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder#com_google_protobuf_AbstractMessage_Builder_getInitializationErrorString__)

[AbstractMessage.Builder.internalMergeFrom(AbstractMessageLite)](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder#com_google_protobuf_AbstractMessage_Builder_internalMergeFrom_com_google_protobuf_AbstractMessageLite_)

[AbstractMessage.Builder.mergeDelimitedFrom(InputStream)](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder#com_google_protobuf_AbstractMessage_Builder_mergeDelimitedFrom_java_io_InputStream_)

[AbstractMessage.Builder.mergeDelimitedFrom(InputStream,ExtensionRegistryLite)](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder#com_google_protobuf_AbstractMessage_Builder_mergeDelimitedFrom_java_io_InputStream_com_google_protobuf_ExtensionRegistryLite_)

[AbstractMessage.Builder.mergeFrom(byte[])](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder#com_google_protobuf_AbstractMessage_Builder_mergeFrom_byte___)

[AbstractMessage.Builder.mergeFrom(byte[],ExtensionRegistryLite)](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder#com_google_protobuf_AbstractMessage_Builder_mergeFrom_byte___com_google_protobuf_ExtensionRegistryLite_)

[AbstractMessage.Builder.mergeFrom(byte[],int,int)](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder#com_google_protobuf_AbstractMessage_Builder_mergeFrom_byte___int_int_)

[AbstractMessage.Builder.mergeFrom(byte[],int,int,ExtensionRegistryLite)](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder#com_google_protobuf_AbstractMessage_Builder_mergeFrom_byte___int_int_com_google_protobuf_ExtensionRegistryLite_)

[AbstractMessage.Builder.mergeFrom(ByteString)](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_ByteString_)

[AbstractMessage.Builder.mergeFrom(ByteString,ExtensionRegistryLite)](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_ByteString_com_google_protobuf_ExtensionRegistryLite_)

[AbstractMessage.Builder.mergeFrom(CodedInputStream)](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_)

[AbstractMessage.Builder.mergeFrom(CodedInputStream,ExtensionRegistryLite)](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

[AbstractMessage.Builder.mergeFrom(Message)](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

[AbstractMessage.Builder.mergeFrom(InputStream)](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder#com_google_protobuf_AbstractMessage_Builder_mergeFrom_java_io_InputStream_)

[AbstractMessage.Builder.mergeFrom(InputStream,ExtensionRegistryLite)](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder#com_google_protobuf_AbstractMessage_Builder_mergeFrom_java_io_InputStream_com_google_protobuf_ExtensionRegistryLite_)

[AbstractMessage.Builder.newUninitializedMessageException(Message)](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder#com_google_protobuf_AbstractMessage_Builder_newUninitializedMessageException_com_google_protobuf_Message_)

[AbstractMessage.Builder.toString()](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder#com_google_protobuf_AbstractMessage_Builder_toString__)

[AbstractMessageLite.Builder.<T>addAll(Iterable<T>,Collection<? super T>)](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder#com_google_protobuf_AbstractMessageLite_Builder__T_addAll_java_lang_Iterable_T__java_util_Collection___super_T__)

[AbstractMessageLite.Builder.<T>addAll(Iterable<T>,List<? super T>)](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder#com_google_protobuf_AbstractMessageLite_Builder__T_addAll_java_lang_Iterable_T__java_util_List___super_T__)

[AbstractMessageLite.Builder.internalMergeFrom(MessageType)](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder#com_google_protobuf_AbstractMessageLite_Builder_internalMergeFrom_MessageType_)

[AbstractMessageLite.Builder.mergeFrom(MessageLite)](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder#com_google_protobuf_AbstractMessageLite_Builder_mergeFrom_com_google_protobuf_MessageLite_)

[AbstractMessageLite.Builder.newUninitializedMessageException(MessageLite)](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder#com_google_protobuf_AbstractMessageLite_Builder_newUninitializedMessageException_com_google_protobuf_MessageLite_)

[GeneratedMessageV3.Builder.addRepeatedField(Descriptors.FieldDescriptor,Object)](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder#com_google_protobuf_GeneratedMessageV3_Builder_addRepeatedField_com_google_protobuf_Descriptors_FieldDescriptor_java_lang_Object_)

[GeneratedMessageV3.Builder.clear()](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder#com_google_protobuf_GeneratedMessageV3_Builder_clear__)

[GeneratedMessageV3.Builder.clearField(Descriptors.FieldDescriptor)](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder#com_google_protobuf_GeneratedMessageV3_Builder_clearField_com_google_protobuf_Descriptors_FieldDescriptor_)

[GeneratedMessageV3.Builder.clearOneof(Descriptors.OneofDescriptor)](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder#com_google_protobuf_GeneratedMessageV3_Builder_clearOneof_com_google_protobuf_Descriptors_OneofDescriptor_)

[GeneratedMessageV3.Builder.clone()](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder#com_google_protobuf_GeneratedMessageV3_Builder_clone__)

[GeneratedMessageV3.Builder.getAllFields()](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder#com_google_protobuf_GeneratedMessageV3_Builder_getAllFields__)

[GeneratedMessageV3.Builder.getDescriptorForType()](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder#com_google_protobuf_GeneratedMessageV3_Builder_getDescriptorForType__)

[GeneratedMessageV3.Builder.getField(Descriptors.FieldDescriptor)](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder#com_google_protobuf_GeneratedMessageV3_Builder_getField_com_google_protobuf_Descriptors_FieldDescriptor_)

[GeneratedMessageV3.Builder.getFieldBuilder(Descriptors.FieldDescriptor)](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder#com_google_protobuf_GeneratedMessageV3_Builder_getFieldBuilder_com_google_protobuf_Descriptors_FieldDescriptor_)

[GeneratedMessageV3.Builder.getOneofFieldDescriptor(Descriptors.OneofDescriptor)](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder#com_google_protobuf_GeneratedMessageV3_Builder_getOneofFieldDescriptor_com_google_protobuf_Descriptors_OneofDescriptor_)

[GeneratedMessageV3.Builder.getParentForChildren()](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder#com_google_protobuf_GeneratedMessageV3_Builder_getParentForChildren__)

[GeneratedMessageV3.Builder.getRepeatedField(Descriptors.FieldDescriptor,int)](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder#com_google_protobuf_GeneratedMessageV3_Builder_getRepeatedField_com_google_protobuf_Descriptors_FieldDescriptor_int_)

[GeneratedMessageV3.Builder.getRepeatedFieldBuilder(Descriptors.FieldDescriptor,int)](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder#com_google_protobuf_GeneratedMessageV3_Builder_getRepeatedFieldBuilder_com_google_protobuf_Descriptors_FieldDescriptor_int_)

[GeneratedMessageV3.Builder.getRepeatedFieldCount(Descriptors.FieldDescriptor)](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder#com_google_protobuf_GeneratedMessageV3_Builder_getRepeatedFieldCount_com_google_protobuf_Descriptors_FieldDescriptor_)

[GeneratedMessageV3.Builder.getUnknownFields()](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder#com_google_protobuf_GeneratedMessageV3_Builder_getUnknownFields__)

[GeneratedMessageV3.Builder.hasField(Descriptors.FieldDescriptor)](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder#com_google_protobuf_GeneratedMessageV3_Builder_hasField_com_google_protobuf_Descriptors_FieldDescriptor_)

[GeneratedMessageV3.Builder.hasOneof(Descriptors.OneofDescriptor)](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder#com_google_protobuf_GeneratedMessageV3_Builder_hasOneof_com_google_protobuf_Descriptors_OneofDescriptor_)

[GeneratedMessageV3.Builder.internalGetFieldAccessorTable()](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder#com_google_protobuf_GeneratedMessageV3_Builder_internalGetFieldAccessorTable__)

[GeneratedMessageV3.Builder.internalGetMapField(int)](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder#com_google_protobuf_GeneratedMessageV3_Builder_internalGetMapField_int_)

[GeneratedMessageV3.Builder.internalGetMutableMapField(int)](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder#com_google_protobuf_GeneratedMessageV3_Builder_internalGetMutableMapField_int_)

[GeneratedMessageV3.Builder.isClean()](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder#com_google_protobuf_GeneratedMessageV3_Builder_isClean__)

[GeneratedMessageV3.Builder.isInitialized()](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder#com_google_protobuf_GeneratedMessageV3_Builder_isInitialized__)

[GeneratedMessageV3.Builder.markClean()](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder#com_google_protobuf_GeneratedMessageV3_Builder_markClean__)

[GeneratedMessageV3.Builder.mergeUnknownFields(UnknownFieldSet)](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder#com_google_protobuf_GeneratedMessageV3_Builder_mergeUnknownFields_com_google_protobuf_UnknownFieldSet_)

[GeneratedMessageV3.Builder.newBuilderForField(Descriptors.FieldDescriptor)](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder#com_google_protobuf_GeneratedMessageV3_Builder_newBuilderForField_com_google_protobuf_Descriptors_FieldDescriptor_)

[GeneratedMessageV3.Builder.onBuilt()](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder#com_google_protobuf_GeneratedMessageV3_Builder_onBuilt__)

[GeneratedMessageV3.Builder.onChanged()](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder#com_google_protobuf_GeneratedMessageV3_Builder_onChanged__)

[GeneratedMessageV3.Builder.setField(Descriptors.FieldDescriptor,Object)](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder#com_google_protobuf_GeneratedMessageV3_Builder_setField_com_google_protobuf_Descriptors_FieldDescriptor_java_lang_Object_)

[GeneratedMessageV3.Builder.setRepeatedField(Descriptors.FieldDescriptor,int,Object)](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder#com_google_protobuf_GeneratedMessageV3_Builder_setRepeatedField_com_google_protobuf_Descriptors_FieldDescriptor_int_java_lang_Object_)

[GeneratedMessageV3.Builder.setUnknownFields(UnknownFieldSet)](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder#com_google_protobuf_GeneratedMessageV3_Builder_setUnknownFields_com_google_protobuf_UnknownFieldSet_)

[GeneratedMessageV3.Builder.setUnknownFieldsProto3(UnknownFieldSet)](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder#com_google_protobuf_GeneratedMessageV3_Builder_setUnknownFieldsProto3_com_google_protobuf_UnknownFieldSet_)

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
`[Descriptors.Descriptor](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor)` |   
  
## Methods 

### addRepeatedField(Descriptors.FieldDescriptor field, Object value)
    
    
    public DescriptorProtos.UninterpretedOption.NamePart.Builder addRepeatedField(Descriptors.FieldDescriptor field, Object value)

**Parameters**  
---  
**Name** | **Description**  
`field` | `[Descriptors.FieldDescriptor](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.FieldDescriptor)`  
  
`value` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DescriptorProtos.UninterpretedOption.NamePart.Builder](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DescriptorProtos.UninterpretedOption.NamePart.Builder)` |   
**Overrides**

[GeneratedMessageV3.Builder<BuilderType>.addRepeatedField(Descriptors.FieldDescriptor field, Object value)](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder#com_google_protobuf_GeneratedMessageV3_Builder_addRepeatedField_com_google_protobuf_Descriptors_FieldDescriptor_java_lang_Object_)

### build()
    
    
    public DescriptorProtos.UninterpretedOption.NamePart build()

**Returns**  
---  
**Type** | **Description**  
`[DescriptorProtos.UninterpretedOption.NamePart](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DescriptorProtos.UninterpretedOption.NamePart)` |   
  
### buildPartial()
    
    
    public DescriptorProtos.UninterpretedOption.NamePart buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[DescriptorProtos.UninterpretedOption.NamePart](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DescriptorProtos.UninterpretedOption.NamePart)` |   
  
### clear()
    
    
    public DescriptorProtos.UninterpretedOption.NamePart.Builder clear()

Called by the initialization and clear code paths to allow subclasses to reset any of their builtin fields back to the initial values.

**Returns**  
---  
**Type** | **Description**  
`[DescriptorProtos.UninterpretedOption.NamePart.Builder](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DescriptorProtos.UninterpretedOption.NamePart.Builder)` |   
**Overrides**

[GeneratedMessageV3.Builder<BuilderType>.clear()](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder#com_google_protobuf_GeneratedMessageV3_Builder_clear__)

### clearField(Descriptors.FieldDescriptor field)
    
    
    public DescriptorProtos.UninterpretedOption.NamePart.Builder clearField(Descriptors.FieldDescriptor field)

**Parameter**  
---  
**Name** | **Description**  
`field` | `[Descriptors.FieldDescriptor](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.FieldDescriptor)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DescriptorProtos.UninterpretedOption.NamePart.Builder](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DescriptorProtos.UninterpretedOption.NamePart.Builder)` |   
**Overrides**

[GeneratedMessageV3.Builder<BuilderType>.clearField(Descriptors.FieldDescriptor field)](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder#com_google_protobuf_GeneratedMessageV3_Builder_clearField_com_google_protobuf_Descriptors_FieldDescriptor_)

### clearIsExtension()
    
    
    public DescriptorProtos.UninterpretedOption.NamePart.Builder clearIsExtension()

`required bool is_extension = 2;`

**Returns**  
---  
**Type** | **Description**  
`[DescriptorProtos.UninterpretedOption.NamePart.Builder](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DescriptorProtos.UninterpretedOption.NamePart.Builder)` | This builder for chaining.  
  
### clearNamePart()
    
    
    public DescriptorProtos.UninterpretedOption.NamePart.Builder clearNamePart()

`required string name_part = 1;`

**Returns**  
---  
**Type** | **Description**  
`[DescriptorProtos.UninterpretedOption.NamePart.Builder](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DescriptorProtos.UninterpretedOption.NamePart.Builder)` | This builder for chaining.  
  
### clearOneof(Descriptors.OneofDescriptor oneof)
    
    
    public DescriptorProtos.UninterpretedOption.NamePart.Builder clearOneof(Descriptors.OneofDescriptor oneof)

TODO(jieluo): Clear it when all subclasses have implemented this method.

**Parameter**  
---  
**Name** | **Description**  
`oneof` | `[Descriptors.OneofDescriptor](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.OneofDescriptor)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DescriptorProtos.UninterpretedOption.NamePart.Builder](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DescriptorProtos.UninterpretedOption.NamePart.Builder)` |   
**Overrides**

[GeneratedMessageV3.Builder<BuilderType>.clearOneof(Descriptors.OneofDescriptor oneof)](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder#com_google_protobuf_GeneratedMessageV3_Builder_clearOneof_com_google_protobuf_Descriptors_OneofDescriptor_)

### clone()
    
    
    public DescriptorProtos.UninterpretedOption.NamePart.Builder clone()

Clones the Builder.

**Returns**  
---  
**Type** | **Description**  
`[DescriptorProtos.UninterpretedOption.NamePart.Builder](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DescriptorProtos.UninterpretedOption.NamePart.Builder)` |   
**Overrides**

[GeneratedMessageV3.Builder<BuilderType>.clone()](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder#com_google_protobuf_GeneratedMessageV3_Builder_clone__)

### getDefaultInstanceForType()
    
    
    public DescriptorProtos.UninterpretedOption.NamePart getDefaultInstanceForType()

Get an instance of the type with no fields set. Because no fields are set, all getters for singular fields will return default values and repeated fields will appear empty. This may or may not be a singleton. This differs from the `getDefaultInstance()` method of generated message classes in that this method is an abstract method of the `MessageLite` interface whereas `getDefaultInstance()` is a static method of a specific class. They return the same thing.

**Returns**  
---  
**Type** | **Description**  
`[DescriptorProtos.UninterpretedOption.NamePart](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DescriptorProtos.UninterpretedOption.NamePart)` |   
  
### getDescriptorForType()
    
    
    public Descriptors.Descriptor getDescriptorForType()

Get the message's type's descriptor. This differs from the `getDescriptor()` method of generated message classes in that this method is an abstract method of the `Message` interface whereas `getDescriptor()` is a static method of a specific class. They return the same thing.

**Returns**  
---  
**Type** | **Description**  
`[Descriptors.Descriptor](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor)` |   
**Overrides**

[GeneratedMessageV3.Builder<BuilderType>.getDescriptorForType()](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder#com_google_protobuf_GeneratedMessageV3_Builder_getDescriptorForType__)

### getIsExtension()
    
    
    public boolean getIsExtension()

`required bool is_extension = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The isExtension.  
  
### getNamePart()
    
    
    public String getNamePart()

`required string name_part = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The namePart.  
  
### getNamePartBytes()
    
    
    public ByteString getNamePartBytes()

`required string name_part = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString)` | The bytes for namePart.  
  
### hasIsExtension()
    
    
    public boolean hasIsExtension()

`required bool is_extension = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the isExtension field is set.  
  
### hasNamePart()
    
    
    public boolean hasNamePart()

`required string name_part = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the namePart field is set.  
  
### internalGetFieldAccessorTable()
    
    
    protected GeneratedMessageV3.FieldAccessorTable internalGetFieldAccessorTable()

Get the FieldAccessorTable for this type. We can't have the message class pass this in to the constructor because of bootstrapping trouble with DescriptorProtos.

**Returns**  
---  
**Type** | **Description**  
`[GeneratedMessageV3.FieldAccessorTable](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.FieldAccessorTable)` |   
**Overrides**

[GeneratedMessageV3.Builder<BuilderType>.internalGetFieldAccessorTable()](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder#com_google_protobuf_GeneratedMessageV3_Builder_internalGetFieldAccessorTable__)

### isInitialized()
    
    
    public final boolean isInitialized()

Returns true if all required fields in the message and all embedded messages are set, false otherwise.

See also: [MessageOrBuilder#getInitializationErrorString()](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder#com_google_protobuf_MessageOrBuilder_getInitializationErrorString__)

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[GeneratedMessageV3.Builder<BuilderType>.isInitialized()](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder#com_google_protobuf_GeneratedMessageV3_Builder_isInitialized__)

### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public DescriptorProtos.UninterpretedOption.NamePart.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

Like Builder#mergeFrom(CodedInputStream), but also parses extensions. The extensions that you want to be able to parse must be registered in `extensionRegistry`. Extensions not in the registry will be treated as unknown fields.

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DescriptorProtos.UninterpretedOption.NamePart.Builder](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DescriptorProtos.UninterpretedOption.NamePart.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(DescriptorProtos.UninterpretedOption.NamePart other)
    
    
    public DescriptorProtos.UninterpretedOption.NamePart.Builder mergeFrom(DescriptorProtos.UninterpretedOption.NamePart other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[DescriptorProtos.UninterpretedOption.NamePart](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DescriptorProtos.UninterpretedOption.NamePart)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DescriptorProtos.UninterpretedOption.NamePart.Builder](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DescriptorProtos.UninterpretedOption.NamePart.Builder)` |   
  
### mergeFrom(Message other)
    
    
    public DescriptorProtos.UninterpretedOption.NamePart.Builder mergeFrom(Message other)

Merge `other` into the message being built. `other` must have the exact same type as `this` (i.e. `getDescriptorForType() == other.getDescriptorForType()`).

Merging occurs as follows. For each field:  


  * For singular primitive fields, if the field is set in `other`, then `other`'s value overwrites the value in this message.  

  * For singular message fields, if the field is set in `other`, it is merged into the corresponding sub-message of this message using the same merging rules.  

  * For repeated fields, the elements in `other` are concatenated with the elements in this message.  

  * For oneof groups, if the other message has one of the fields set, the group of this message is cleared and replaced by the field of the other message, so that the oneof constraint is preserved.

This is equivalent to the `Message::MergeFrom` method in C++.




**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DescriptorProtos.UninterpretedOption.NamePart.Builder](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DescriptorProtos.UninterpretedOption.NamePart.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### mergeUnknownFields(UnknownFieldSet unknownFields)
    
    
    public final DescriptorProtos.UninterpretedOption.NamePart.Builder mergeUnknownFields(UnknownFieldSet unknownFields)

Merge some unknown fields into the [UnknownFieldSet](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.UnknownFieldSet) for this message.

**Parameter**  
---  
**Name** | **Description**  
`unknownFields` | `[UnknownFieldSet](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.UnknownFieldSet)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DescriptorProtos.UninterpretedOption.NamePart.Builder](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DescriptorProtos.UninterpretedOption.NamePart.Builder)` |   
**Overrides**

[GeneratedMessageV3.Builder<BuilderType>.mergeUnknownFields(UnknownFieldSet unknownFields)](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder#com_google_protobuf_GeneratedMessageV3_Builder_mergeUnknownFields_com_google_protobuf_UnknownFieldSet_)

### setField(Descriptors.FieldDescriptor field, Object value)
    
    
    public DescriptorProtos.UninterpretedOption.NamePart.Builder setField(Descriptors.FieldDescriptor field, Object value)

**Parameters**  
---  
**Name** | **Description**  
`field` | `[Descriptors.FieldDescriptor](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.FieldDescriptor)`  
  
`value` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DescriptorProtos.UninterpretedOption.NamePart.Builder](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DescriptorProtos.UninterpretedOption.NamePart.Builder)` |   
**Overrides**

[GeneratedMessageV3.Builder<BuilderType>.setField(Descriptors.FieldDescriptor field, Object value)](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder#com_google_protobuf_GeneratedMessageV3_Builder_setField_com_google_protobuf_Descriptors_FieldDescriptor_java_lang_Object_)

### setIsExtension(boolean value)
    
    
    public DescriptorProtos.UninterpretedOption.NamePart.Builder setIsExtension(boolean value)

`required bool is_extension = 2;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The isExtension to set.  
**Returns**  
---  
**Type** | **Description**  
`[DescriptorProtos.UninterpretedOption.NamePart.Builder](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DescriptorProtos.UninterpretedOption.NamePart.Builder)` | This builder for chaining.  
  
### setNamePart(String value)
    
    
    public DescriptorProtos.UninterpretedOption.NamePart.Builder setNamePart(String value)

`required string name_part = 1;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The namePart to set.  
**Returns**  
---  
**Type** | **Description**  
`[DescriptorProtos.UninterpretedOption.NamePart.Builder](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DescriptorProtos.UninterpretedOption.NamePart.Builder)` | This builder for chaining.  
  
### setNamePartBytes(ByteString value)
    
    
    public DescriptorProtos.UninterpretedOption.NamePart.Builder setNamePartBytes(ByteString value)

`required string name_part = 1;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString)`  
The bytes for namePart to set.  
**Returns**  
---  
**Type** | **Description**  
`[DescriptorProtos.UninterpretedOption.NamePart.Builder](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DescriptorProtos.UninterpretedOption.NamePart.Builder)` | This builder for chaining.  
  
### setRepeatedField(Descriptors.FieldDescriptor field, int index, Object value)
    
    
    public DescriptorProtos.UninterpretedOption.NamePart.Builder setRepeatedField(Descriptors.FieldDescriptor field, int index, Object value)

**Parameters**  
---  
**Name** | **Description**  
`field` | `[Descriptors.FieldDescriptor](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.FieldDescriptor)`  
  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DescriptorProtos.UninterpretedOption.NamePart.Builder](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DescriptorProtos.UninterpretedOption.NamePart.Builder)` |   
**Overrides**

[GeneratedMessageV3.Builder<BuilderType>.setRepeatedField(Descriptors.FieldDescriptor field, int index, Object value)](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder#com_google_protobuf_GeneratedMessageV3_Builder_setRepeatedField_com_google_protobuf_Descriptors_FieldDescriptor_int_java_lang_Object_)

### setUnknownFields(UnknownFieldSet unknownFields)
    
    
    public final DescriptorProtos.UninterpretedOption.NamePart.Builder setUnknownFields(UnknownFieldSet unknownFields)

**Parameter**  
---  
**Name** | **Description**  
`unknownFields` | `[UnknownFieldSet](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.UnknownFieldSet)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DescriptorProtos.UninterpretedOption.NamePart.Builder](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DescriptorProtos.UninterpretedOption.NamePart.Builder)` |   
**Overrides**

[GeneratedMessageV3.Builder<BuilderType>.setUnknownFields(UnknownFieldSet unknownFields)](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder#com_google_protobuf_GeneratedMessageV3_Builder_setUnknownFields_com_google_protobuf_UnknownFieldSet_)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-30 UTC."],[],[]] 
