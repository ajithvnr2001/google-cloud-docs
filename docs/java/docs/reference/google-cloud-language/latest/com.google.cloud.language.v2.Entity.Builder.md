---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.Entity.Builder
title: Class Entity.Builder (2.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:45:53.904112+00:00
---

# Class Entity.Builder (2.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.Entity.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class Entity.Builder (2.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.100.0 (latest)  2.96.0  2.95.0  2.94.0  2.92.0  2.89.0  2.88.0  2.86.0  2.84.0  2.83.0  2.82.0  2.81.0  2.79.0  2.77.0  2.76.0  2.75.0  2.74.0  2.73.0  2.71.0  2.69.0  2.68.0  2.65.0  2.64.0  2.63.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.1  2.3.4  2.2.0  2.1.10 
    
    
    public static final class Entity.Builder extends GeneratedMessage.Builder<Entity.Builder> implements EntityOrBuilder

Represents a phrase in the text that is a known entity, such as a person, an organization, or location. The API associates information, such as probability and mentions, with entities.

Protobuf type `google.cloud.language.v2.Entity`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > Entity.Builder

## Implements

[EntityOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.EntityOrBuilder)

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

### addAllMentions(Iterable<? extends EntityMention> values)
    
    
    public Entity.Builder addAllMentions(Iterable<? extends EntityMention> values)

The mentions of this entity in the input document. The API currently supports proper noun mentions.

`repeated .google.cloud.language.v2.EntityMention mentions = 5;`

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<? extends com.google.cloud.language.v2.EntityMention>`  
  
**Returns**  
---  
**Type** | **Description**  
`[Entity.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.Entity.Builder)` |   
  
### addMentions(EntityMention value)
    
    
    public Entity.Builder addMentions(EntityMention value)

The mentions of this entity in the input document. The API currently supports proper noun mentions.

`repeated .google.cloud.language.v2.EntityMention mentions = 5;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[EntityMention](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.EntityMention)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Entity.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.Entity.Builder)` |   
  
### addMentions(EntityMention.Builder builderForValue)
    
    
    public Entity.Builder addMentions(EntityMention.Builder builderForValue)

The mentions of this entity in the input document. The API currently supports proper noun mentions.

`repeated .google.cloud.language.v2.EntityMention mentions = 5;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[EntityMention.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.EntityMention.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Entity.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.Entity.Builder)` |   
  
### addMentions(int index, EntityMention value)
    
    
    public Entity.Builder addMentions(int index, EntityMention value)

The mentions of this entity in the input document. The API currently supports proper noun mentions.

`repeated .google.cloud.language.v2.EntityMention mentions = 5;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[EntityMention](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.EntityMention)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Entity.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.Entity.Builder)` |   
  
### addMentions(int index, EntityMention.Builder builderForValue)
    
    
    public Entity.Builder addMentions(int index, EntityMention.Builder builderForValue)

The mentions of this entity in the input document. The API currently supports proper noun mentions.

`repeated .google.cloud.language.v2.EntityMention mentions = 5;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[EntityMention.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.EntityMention.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Entity.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.Entity.Builder)` |   
  
### addMentionsBuilder()
    
    
    public EntityMention.Builder addMentionsBuilder()

The mentions of this entity in the input document. The API currently supports proper noun mentions.

`repeated .google.cloud.language.v2.EntityMention mentions = 5;`

**Returns**  
---  
**Type** | **Description**  
`[EntityMention.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.EntityMention.Builder)` |   
  
### addMentionsBuilder(int index)
    
    
    public EntityMention.Builder addMentionsBuilder(int index)

The mentions of this entity in the input document. The API currently supports proper noun mentions.

`repeated .google.cloud.language.v2.EntityMention mentions = 5;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[EntityMention.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.EntityMention.Builder)` |   
  
### build()
    
    
    public Entity build()

**Returns**  
---  
**Type** | **Description**  
`[Entity](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.Entity)` |   
  
### buildPartial()
    
    
    public Entity buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[Entity](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.Entity)` |   
  
### clear()
    
    
    public Entity.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[Entity.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.Entity.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearMentions()
    
    
    public Entity.Builder clearMentions()

The mentions of this entity in the input document. The API currently supports proper noun mentions.

`repeated .google.cloud.language.v2.EntityMention mentions = 5;`

**Returns**  
---  
**Type** | **Description**  
`[Entity.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.Entity.Builder)` |   
  
### clearMetadata()
    
    
    public Entity.Builder clearMetadata()

**Returns**  
---  
**Type** | **Description**  
`[Entity.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.Entity.Builder)` |   
  
### clearName()
    
    
    public Entity.Builder clearName()

The representative name for the entity.

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[Entity.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.Entity.Builder)` | This builder for chaining.  
  
### clearSentiment()
    
    
    public Entity.Builder clearSentiment()

For calls to [AnalyzeEntitySentiment][] or if AnnotateTextRequest.Features.extract_entity_sentiment is set to true, this field will contain the aggregate sentiment expressed for this entity in the provided document.

`.google.cloud.language.v2.Sentiment sentiment = 6;`

**Returns**  
---  
**Type** | **Description**  
`[Entity.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.Entity.Builder)` |   
  
### clearType()
    
    
    public Entity.Builder clearType()

The entity type.

`.google.cloud.language.v2.Entity.Type type = 2;`

**Returns**  
---  
**Type** | **Description**  
`[Entity.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.Entity.Builder)` | This builder for chaining.  
  
### containsMetadata(String key)
    
    
    public boolean containsMetadata(String key)

Metadata associated with the entity.

For the metadata associated with other entity types, see the Type table below.

`map<string, string> metadata = 3;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getDefaultInstanceForType()
    
    
    public Entity getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[Entity](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.Entity)` |   
  
### getDescriptorForType()
    
    
    public Descriptors.Descriptor getDescriptorForType()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getDescriptorForType__)

### getMentions(int index)
    
    
    public EntityMention getMentions(int index)

The mentions of this entity in the input document. The API currently supports proper noun mentions.

`repeated .google.cloud.language.v2.EntityMention mentions = 5;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[EntityMention](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.EntityMention)` |   
  
### getMentionsBuilder(int index)
    
    
    public EntityMention.Builder getMentionsBuilder(int index)

The mentions of this entity in the input document. The API currently supports proper noun mentions.

`repeated .google.cloud.language.v2.EntityMention mentions = 5;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[EntityMention.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.EntityMention.Builder)` |   
  
### getMentionsBuilderList()
    
    
    public List<EntityMention.Builder> getMentionsBuilderList()

The mentions of this entity in the input document. The API currently supports proper noun mentions.

`repeated .google.cloud.language.v2.EntityMention mentions = 5;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.EntityMention.Builder)>` |   
  
### getMentionsCount()
    
    
    public int getMentionsCount()

The mentions of this entity in the input document. The API currently supports proper noun mentions.

`repeated .google.cloud.language.v2.EntityMention mentions = 5;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getMentionsList()
    
    
    public List<EntityMention> getMentionsList()

The mentions of this entity in the input document. The API currently supports proper noun mentions.

`repeated .google.cloud.language.v2.EntityMention mentions = 5;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[EntityMention](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.EntityMention)>` |   
  
### getMentionsOrBuilder(int index)
    
    
    public EntityMentionOrBuilder getMentionsOrBuilder(int index)

The mentions of this entity in the input document. The API currently supports proper noun mentions.

`repeated .google.cloud.language.v2.EntityMention mentions = 5;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[EntityMentionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.EntityMentionOrBuilder)` |   
  
### getMentionsOrBuilderList()
    
    
    public List<? extends EntityMentionOrBuilder> getMentionsOrBuilderList()

The mentions of this entity in the input document. The API currently supports proper noun mentions.

`repeated .google.cloud.language.v2.EntityMention mentions = 5;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.language.v2.EntityMentionOrBuilder>` |   
  
### getMetadata() (deprecated)
    
    
    public Map<String,String> getMetadata()

Use [#getMetadataMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.Entity.Builder#com_google_cloud_language_v2_Entity_Builder_getMetadataMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getMetadataCount()
    
    
    public int getMetadataCount()

Metadata associated with the entity.

For the metadata associated with other entity types, see the Type table below.

`map<string, string> metadata = 3;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getMetadataMap()
    
    
    public Map<String,String> getMetadataMap()

Metadata associated with the entity.

For the metadata associated with other entity types, see the Type table below.

`map<string, string> metadata = 3;`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getMetadataOrDefault(String key, String defaultValue)
    
    
    public String getMetadataOrDefault(String key, String defaultValue)

Metadata associated with the entity.

For the metadata associated with other entity types, see the Type table below.

`map<string, string> metadata = 3;`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getMetadataOrThrow(String key)
    
    
    public String getMetadataOrThrow(String key)

Metadata associated with the entity.

For the metadata associated with other entity types, see the Type table below.

`map<string, string> metadata = 3;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getMutableMetadata() (deprecated)
    
    
    public Map<String,String> getMutableMetadata()

Use alternate mutation accessors instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getName()
    
    
    public String getName()

The representative name for the entity.

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public ByteString getNameBytes()

The representative name for the entity.

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getSentiment()
    
    
    public Sentiment getSentiment()

For calls to [AnalyzeEntitySentiment][] or if AnnotateTextRequest.Features.extract_entity_sentiment is set to true, this field will contain the aggregate sentiment expressed for this entity in the provided document.

`.google.cloud.language.v2.Sentiment sentiment = 6;`

**Returns**  
---  
**Type** | **Description**  
`[Sentiment](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.Sentiment)` | The sentiment.  
  
### getSentimentBuilder()
    
    
    public Sentiment.Builder getSentimentBuilder()

For calls to [AnalyzeEntitySentiment][] or if AnnotateTextRequest.Features.extract_entity_sentiment is set to true, this field will contain the aggregate sentiment expressed for this entity in the provided document.

`.google.cloud.language.v2.Sentiment sentiment = 6;`

**Returns**  
---  
**Type** | **Description**  
`[Sentiment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.Sentiment.Builder)` |   
  
### getSentimentOrBuilder()
    
    
    public SentimentOrBuilder getSentimentOrBuilder()

For calls to [AnalyzeEntitySentiment][] or if AnnotateTextRequest.Features.extract_entity_sentiment is set to true, this field will contain the aggregate sentiment expressed for this entity in the provided document.

`.google.cloud.language.v2.Sentiment sentiment = 6;`

**Returns**  
---  
**Type** | **Description**  
`[SentimentOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.SentimentOrBuilder)` |   
  
### getType()
    
    
    public Entity.Type getType()

The entity type.

`.google.cloud.language.v2.Entity.Type type = 2;`

**Returns**  
---  
**Type** | **Description**  
`[Entity.Type](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.Entity.Type)` | The type.  
  
### getTypeValue()
    
    
    public int getTypeValue()

The entity type.

`.google.cloud.language.v2.Entity.Type type = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for type.  
  
### hasSentiment()
    
    
    public boolean hasSentiment()

For calls to [AnalyzeEntitySentiment][] or if AnnotateTextRequest.Features.extract_entity_sentiment is set to true, this field will contain the aggregate sentiment expressed for this entity in the provided document.

`.google.cloud.language.v2.Sentiment sentiment = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the sentiment field is set.  
  
### internalGetFieldAccessorTable()
    
    
    protected GeneratedMessage.FieldAccessorTable internalGetFieldAccessorTable()

**Returns**  
---  
**Type** | **Description**  
`[FieldAccessorTable](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.FieldAccessorTable.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.internalGetFieldAccessorTable()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_internalGetFieldAccessorTable__)

### internalGetMapFieldReflection(int number)
    
    
    protected MapFieldReflectionAccessor internalGetMapFieldReflection(int number)

**Parameter**  
---  
**Name** | **Description**  
`number` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.protobuf.MapFieldReflectionAccessor` |   
**Overrides**

com.google.protobuf.GeneratedMessage.Builder.internalGetMapFieldReflection(int)

### internalGetMutableMapFieldReflection(int number)
    
    
    protected MapFieldReflectionAccessor internalGetMutableMapFieldReflection(int number)

**Parameter**  
---  
**Name** | **Description**  
`number` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.protobuf.MapFieldReflectionAccessor` |   
**Overrides**

com.google.protobuf.GeneratedMessage.Builder.internalGetMutableMapFieldReflection(int)

### isInitialized()
    
    
    public final boolean isInitialized()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.isInitialized()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_isInitialized__)

### mergeFrom(Entity other)
    
    
    public Entity.Builder mergeFrom(Entity other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Entity](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.Entity)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Entity.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.Entity.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public Entity.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Entity.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.Entity.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public Entity.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Entity.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.Entity.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### mergeSentiment(Sentiment value)
    
    
    public Entity.Builder mergeSentiment(Sentiment value)

For calls to [AnalyzeEntitySentiment][] or if AnnotateTextRequest.Features.extract_entity_sentiment is set to true, this field will contain the aggregate sentiment expressed for this entity in the provided document.

`.google.cloud.language.v2.Sentiment sentiment = 6;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Sentiment](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.Sentiment)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Entity.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.Entity.Builder)` |   
  
### putAllMetadata(Map<String,String> values)
    
    
    public Entity.Builder putAllMetadata(Map<String,String> values)

Metadata associated with the entity.

For the metadata associated with other entity types, see the Type table below.

`map<string, string> metadata = 3;`

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[Entity.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.Entity.Builder)` |   
  
### putMetadata(String key, String value)
    
    
    public Entity.Builder putMetadata(String key, String value)

Metadata associated with the entity.

For the metadata associated with other entity types, see the Type table below.

`map<string, string> metadata = 3;`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Entity.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.Entity.Builder)` |   
  
### removeMentions(int index)
    
    
    public Entity.Builder removeMentions(int index)

The mentions of this entity in the input document. The API currently supports proper noun mentions.

`repeated .google.cloud.language.v2.EntityMention mentions = 5;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Entity.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.Entity.Builder)` |   
  
### removeMetadata(String key)
    
    
    public Entity.Builder removeMetadata(String key)

Metadata associated with the entity.

For the metadata associated with other entity types, see the Type table below.

`map<string, string> metadata = 3;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Entity.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.Entity.Builder)` |   
  
### setMentions(int index, EntityMention value)
    
    
    public Entity.Builder setMentions(int index, EntityMention value)

The mentions of this entity in the input document. The API currently supports proper noun mentions.

`repeated .google.cloud.language.v2.EntityMention mentions = 5;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[EntityMention](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.EntityMention)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Entity.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.Entity.Builder)` |   
  
### setMentions(int index, EntityMention.Builder builderForValue)
    
    
    public Entity.Builder setMentions(int index, EntityMention.Builder builderForValue)

The mentions of this entity in the input document. The API currently supports proper noun mentions.

`repeated .google.cloud.language.v2.EntityMention mentions = 5;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[EntityMention.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.EntityMention.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Entity.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.Entity.Builder)` |   
  
### setName(String value)
    
    
    public Entity.Builder setName(String value)

The representative name for the entity.

`string name = 1;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name to set.  
**Returns**  
---  
**Type** | **Description**  
`[Entity.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.Entity.Builder)` | This builder for chaining.  
  
### setNameBytes(ByteString value)
    
    
    public Entity.Builder setNameBytes(ByteString value)

The representative name for the entity.

`string name = 1;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for name to set.  
**Returns**  
---  
**Type** | **Description**  
`[Entity.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.Entity.Builder)` | This builder for chaining.  
  
### setSentiment(Sentiment value)
    
    
    public Entity.Builder setSentiment(Sentiment value)

For calls to [AnalyzeEntitySentiment][] or if AnnotateTextRequest.Features.extract_entity_sentiment is set to true, this field will contain the aggregate sentiment expressed for this entity in the provided document.

`.google.cloud.language.v2.Sentiment sentiment = 6;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Sentiment](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.Sentiment)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Entity.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.Entity.Builder)` |   
  
### setSentiment(Sentiment.Builder builderForValue)
    
    
    public Entity.Builder setSentiment(Sentiment.Builder builderForValue)

For calls to [AnalyzeEntitySentiment][] or if AnnotateTextRequest.Features.extract_entity_sentiment is set to true, this field will contain the aggregate sentiment expressed for this entity in the provided document.

`.google.cloud.language.v2.Sentiment sentiment = 6;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Sentiment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.Sentiment.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Entity.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.Entity.Builder)` |   
  
### setType(Entity.Type value)
    
    
    public Entity.Builder setType(Entity.Type value)

The entity type.

`.google.cloud.language.v2.Entity.Type type = 2;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Entity.Type](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.Entity.Type)`  
The type to set.  
**Returns**  
---  
**Type** | **Description**  
`[Entity.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.Entity.Builder)` | This builder for chaining.  
  
### setTypeValue(int value)
    
    
    public Entity.Builder setTypeValue(int value)

The entity type.

`.google.cloud.language.v2.Entity.Type type = 2;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The enum numeric value on the wire for type to set.  
**Returns**  
---  
**Type** | **Description**  
`[Entity.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.Entity.Builder)` | This builder for chaining.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
