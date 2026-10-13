---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.PermissionSettings
title: Class Space.PermissionSettings (0.63.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:12:59.216176+00:00
---

# Class Space.PermissionSettings (0.63.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.PermissionSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class Space.PermissionSettings (0.63.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.63.0 (latest)  0.59.0  0.58.0  0.57.0  0.55.0  0.52.0  0.51.0  0.49.0  0.47.0  0.46.0  0.45.0  0.44.0  0.42.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.34.0  0.32.0  0.31.0  0.28.0  0.27.0  0.26.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.1.0 
    
    
    public static final class Space.PermissionSettings extends GeneratedMessage implements Space.PermissionSettingsOrBuilder

[Permission settings](https://support.google.com/chat/answer/13340792) that you can specify when updating an existing named space.

To set permission settings when creating a space, specify the `PredefinedPermissionSettings` field in your request.

Protobuf type `google.chat.v1.Space.PermissionSettings`

## Inheritance

[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.html) > [AbstractMessage](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.html) > [GeneratedMessage](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html) > Space.PermissionSettings

## Implements

[Space.PermissionSettingsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.PermissionSettingsOrBuilder)

## Inherited Members

[AbstractMessage.equals(Object)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.html#com_google_protobuf_AbstractMessage_equals_java_lang_Object_)

[AbstractMessage.findInitializationErrors()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.html#com_google_protobuf_AbstractMessage_findInitializationErrors__)

[AbstractMessage.getInitializationErrorString()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.html#com_google_protobuf_AbstractMessage_getInitializationErrorString__)

[AbstractMessage.hashCode()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.html#com_google_protobuf_AbstractMessage_hashCode__)

[AbstractMessage.hashFields(int,Map<Descriptors.FieldDescriptor,Object>)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.html#com_google_protobuf_AbstractMessage_hashFields_int_java_util_Map_com_google_protobuf_Descriptors_FieldDescriptor_java_lang_Object__)

[AbstractMessage.newBuilderForType(AbstractMessage.BuilderParent)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.html#com_google_protobuf_AbstractMessage_newBuilderForType_com_google_protobuf_AbstractMessage_BuilderParent_)

[AbstractMessage.toString()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.html#com_google_protobuf_AbstractMessage_toString__)

[AbstractMessageLite.<T>addAll(Iterable<T>,List<? super T>)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.html#com_google_protobuf_AbstractMessageLite__T_addAll_java_lang_Iterable_T__java_util_List___super_T__)

[AbstractMessageLite.checkByteStringIsUtf8(ByteString)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.html#com_google_protobuf_AbstractMessageLite_checkByteStringIsUtf8_com_google_protobuf_ByteString_)

[AbstractMessageLite.toByteArray()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.html#com_google_protobuf_AbstractMessageLite_toByteArray__)

[AbstractMessageLite.toByteString()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.html#com_google_protobuf_AbstractMessageLite_toByteString__)

[AbstractMessageLite.writeDelimitedTo(OutputStream)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.html#com_google_protobuf_AbstractMessageLite_writeDelimitedTo_java_io_OutputStream_)

[AbstractMessageLite.writeTo(OutputStream)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.html#com_google_protobuf_AbstractMessageLite_writeTo_java_io_OutputStream_)

com.google.protobuf.GeneratedMessage.<ContainingT,T>newFileScopedGeneratedExtension(java.lang.Class<?>,com.google.protobuf.Message)

com.google.protobuf.GeneratedMessage.<ContainingT,T>newMessageScopedGeneratedExtension(com.google.protobuf.Message,int,java.lang.Class<?>,com.google.protobuf.Message)

com.google.protobuf.GeneratedMessage.<ListT>makeMutableCopy(ListT)

com.google.protobuf.GeneratedMessage.<ListT>makeMutableCopy(ListT,int)

[GeneratedMessage.<M>parseDelimitedWithIOException(Parser<M>,InputStream)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage__M_parseDelimitedWithIOException_com_google_protobuf_Parser_M__java_io_InputStream_)

[GeneratedMessage.<M>parseDelimitedWithIOException(Parser<M>,InputStream,ExtensionRegistryLite)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage__M_parseDelimitedWithIOException_com_google_protobuf_Parser_M__java_io_InputStream_com_google_protobuf_ExtensionRegistryLite_)

[GeneratedMessage.<M>parseWithIOException(Parser<M>,CodedInputStream)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage__M_parseWithIOException_com_google_protobuf_Parser_M__com_google_protobuf_CodedInputStream_)

[GeneratedMessage.<M>parseWithIOException(Parser<M>,CodedInputStream,ExtensionRegistryLite)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage__M_parseWithIOException_com_google_protobuf_Parser_M__com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

[GeneratedMessage.<M>parseWithIOException(Parser<M>,InputStream)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage__M_parseWithIOException_com_google_protobuf_Parser_M__java_io_InputStream_)

[GeneratedMessage.<M>parseWithIOException(Parser<M>,InputStream,ExtensionRegistryLite)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage__M_parseWithIOException_com_google_protobuf_Parser_M__java_io_InputStream_com_google_protobuf_ExtensionRegistryLite_)

com.google.protobuf.GeneratedMessage.<T>emptyList(java.lang.Class<T>)

com.google.protobuf.GeneratedMessage.<V>serializeBooleanMapTo(com.google.protobuf.CodedOutputStream,com.google.protobuf.MapField<java.lang.Boolean,V>,com.google.protobuf.MapEntry<java.lang.Boolean,V>,int)

com.google.protobuf.GeneratedMessage.<V>serializeIntegerMapTo(com.google.protobuf.CodedOutputStream,com.google.protobuf.MapField<java.lang.Integer,V>,com.google.protobuf.MapEntry<java.lang.Integer,V>,int)

com.google.protobuf.GeneratedMessage.<V>serializeLongMapTo(com.google.protobuf.CodedOutputStream,com.google.protobuf.MapField<java.lang.Long,V>,com.google.protobuf.MapEntry<java.lang.Long,V>,int)

com.google.protobuf.GeneratedMessage.<V>serializeStringMapTo(com.google.protobuf.CodedOutputStream,com.google.protobuf.MapField<java.lang.String,V>,com.google.protobuf.MapEntry<java.lang.String,V>,int)

com.google.protobuf.GeneratedMessage.canUseUnsafe()

[GeneratedMessage.computeStringSize(int,Object)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_computeStringSize_int_java_lang_Object_)

[GeneratedMessage.computeStringSizeNoTag(Object)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_computeStringSizeNoTag_java_lang_Object_)

com.google.protobuf.GeneratedMessage.emptyBooleanList()

com.google.protobuf.GeneratedMessage.emptyDoubleList()

com.google.protobuf.GeneratedMessage.emptyFloatList()

com.google.protobuf.GeneratedMessage.emptyIntList()

com.google.protobuf.GeneratedMessage.emptyLongList()

[GeneratedMessage.getAllFields()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_getAllFields__)

[GeneratedMessage.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_getDescriptorForType__)

[GeneratedMessage.getField(Descriptors.FieldDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_getField_com_google_protobuf_Descriptors_FieldDescriptor_)

[GeneratedMessage.getOneofFieldDescriptor(Descriptors.OneofDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_getOneofFieldDescriptor_com_google_protobuf_Descriptors_OneofDescriptor_)

[GeneratedMessage.getParserForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_getParserForType__)

[GeneratedMessage.getRepeatedField(Descriptors.FieldDescriptor,int)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_getRepeatedField_com_google_protobuf_Descriptors_FieldDescriptor_int_)

[GeneratedMessage.getRepeatedFieldCount(Descriptors.FieldDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_getRepeatedFieldCount_com_google_protobuf_Descriptors_FieldDescriptor_)

[GeneratedMessage.getSerializedSize()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_getSerializedSize__)

[GeneratedMessage.getUnknownFields()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_getUnknownFields__)

[GeneratedMessage.hasField(Descriptors.FieldDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_hasField_com_google_protobuf_Descriptors_FieldDescriptor_)

[GeneratedMessage.hasOneof(Descriptors.OneofDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_hasOneof_com_google_protobuf_Descriptors_OneofDescriptor_)

[GeneratedMessage.internalGetFieldAccessorTable()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_internalGetFieldAccessorTable__)

[GeneratedMessage.internalGetMapField(int)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_internalGetMapField_int_)

com.google.protobuf.GeneratedMessage.internalGetMapFieldReflection(int)

[GeneratedMessage.isInitialized()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_isInitialized__)

com.google.protobuf.GeneratedMessage.isStringEmpty(java.lang.Object)

[GeneratedMessage.makeExtensionsImmutable()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_makeExtensionsImmutable__)

com.google.protobuf.GeneratedMessage.mergeFromAndMakeImmutableInternal(com.google.protobuf.CodedInputStream,com.google.protobuf.ExtensionRegistryLite)

com.google.protobuf.GeneratedMessage.newInstance(com.google.protobuf.GeneratedMessage.UnusedPrivateParameter)

[GeneratedMessage.parseUnknownField(CodedInputStream,UnknownFieldSet.Builder,ExtensionRegistryLite,int)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_parseUnknownField_com_google_protobuf_CodedInputStream_com_google_protobuf_UnknownFieldSet_Builder_com_google_protobuf_ExtensionRegistryLite_int_)

com.google.protobuf.GeneratedMessage.parseUnknownFieldProto3(com.google.protobuf.CodedInputStream,com.google.protobuf.UnknownFieldSet.Builder,com.google.protobuf.ExtensionRegistryLite,int)

[GeneratedMessage.writeReplace()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_writeReplace__)

[GeneratedMessage.writeString(CodedOutputStream,int,Object)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_writeString_com_google_protobuf_CodedOutputStream_int_java_lang_Object_)

[GeneratedMessage.writeStringNoTag(CodedOutputStream,Object)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_writeStringNoTag_com_google_protobuf_CodedOutputStream_java_lang_Object_)

[GeneratedMessage.writeTo(CodedOutputStream)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_writeTo_com_google_protobuf_CodedOutputStream_)

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Static Fields 

### MANAGE_APPS_FIELD_NUMBER
    
    
    public static final int MANAGE_APPS_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### MANAGE_MEMBERS_AND_GROUPS_FIELD_NUMBER
    
    
    public static final int MANAGE_MEMBERS_AND_GROUPS_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### MANAGE_WEBHOOKS_FIELD_NUMBER
    
    
    public static final int MANAGE_WEBHOOKS_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### MODIFY_SPACE_DETAILS_FIELD_NUMBER
    
    
    public static final int MODIFY_SPACE_DETAILS_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### POST_MESSAGES_FIELD_NUMBER
    
    
    public static final int POST_MESSAGES_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### REPLY_MESSAGES_FIELD_NUMBER
    
    
    public static final int REPLY_MESSAGES_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### TOGGLE_HISTORY_FIELD_NUMBER
    
    
    public static final int TOGGLE_HISTORY_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### USE_AT_MENTION_ALL_FIELD_NUMBER
    
    
    public static final int USE_AT_MENTION_ALL_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### VIEW_SPACE_MEMBERSHIP_FIELD_NUMBER
    
    
    public static final int VIEW_SPACE_MEMBERSHIP_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
## Static Methods 

### getDefaultInstance()
    
    
    public static Space.PermissionSettings getDefaultInstance()

**Returns**  
---  
**Type** | **Description**  
`[Space.PermissionSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.PermissionSettings)` |   
  
### getDescriptor()
    
    
    public static final Descriptors.Descriptor getDescriptor()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
  
### newBuilder()
    
    
    public static Space.PermissionSettings.Builder newBuilder()

**Returns**  
---  
**Type** | **Description**  
`[Space.PermissionSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.PermissionSettings.Builder)` |   
  
### newBuilder(Space.PermissionSettings prototype)
    
    
    public static Space.PermissionSettings.Builder newBuilder(Space.PermissionSettings prototype)

**Parameter**  
---  
**Name** | **Description**  
`prototype` | `[Space.PermissionSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.PermissionSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Space.PermissionSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.PermissionSettings.Builder)` |   
  
### parseDelimitedFrom(InputStream input)
    
    
    public static Space.PermissionSettings parseDelimitedFrom(InputStream input)

**Parameter**  
---  
**Name** | **Description**  
`input` | `[InputStream](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Space.PermissionSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.PermissionSettings)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseDelimitedFrom(InputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public static Space.PermissionSettings parseDelimitedFrom(InputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[InputStream](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Space.PermissionSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.PermissionSettings)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseFrom(byte[] data)
    
    
    public static Space.PermissionSettings parseFrom(byte[] data)

**Parameter**  
---  
**Name** | **Description**  
`data` | `byte[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[Space.PermissionSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.PermissionSettings)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parseFrom(byte[] data, ExtensionRegistryLite extensionRegistry)
    
    
    public static Space.PermissionSettings parseFrom(byte[] data, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`data` | `byte[]`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Space.PermissionSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.PermissionSettings)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parseFrom(ByteString data)
    
    
    public static Space.PermissionSettings parseFrom(ByteString data)

**Parameter**  
---  
**Name** | **Description**  
`data` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Space.PermissionSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.PermissionSettings)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parseFrom(ByteString data, ExtensionRegistryLite extensionRegistry)
    
    
    public static Space.PermissionSettings parseFrom(ByteString data, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`data` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Space.PermissionSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.PermissionSettings)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parseFrom(CodedInputStream input)
    
    
    public static Space.PermissionSettings parseFrom(CodedInputStream input)

**Parameter**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Space.PermissionSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.PermissionSettings)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public static Space.PermissionSettings parseFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Space.PermissionSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.PermissionSettings)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseFrom(InputStream input)
    
    
    public static Space.PermissionSettings parseFrom(InputStream input)

**Parameter**  
---  
**Name** | **Description**  
`input` | `[InputStream](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Space.PermissionSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.PermissionSettings)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseFrom(InputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public static Space.PermissionSettings parseFrom(InputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[InputStream](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Space.PermissionSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.PermissionSettings)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseFrom(ByteBuffer data)
    
    
    public static Space.PermissionSettings parseFrom(ByteBuffer data)

**Parameter**  
---  
**Name** | **Description**  
`data` | `[ByteBuffer](https://docs.oracle.com/javase/8/docs/api/java/nio/ByteBuffer.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Space.PermissionSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.PermissionSettings)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parseFrom(ByteBuffer data, ExtensionRegistryLite extensionRegistry)
    
    
    public static Space.PermissionSettings parseFrom(ByteBuffer data, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`data` | `[ByteBuffer](https://docs.oracle.com/javase/8/docs/api/java/nio/ByteBuffer.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Space.PermissionSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.PermissionSettings)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parser()
    
    
    public static Parser<Space.PermissionSettings> parser()

**Returns**  
---  
**Type** | **Description**  
`[Parser](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Parser.html)<[PermissionSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.PermissionSettings)>` |   
  
## Methods 

### equals(Object obj)
    
    
    public boolean equals(Object obj)

**Parameter**  
---  
**Name** | **Description**  
`obj` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[AbstractMessage.equals(Object other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.html#com_google_protobuf_AbstractMessage_equals_java_lang_Object_)

### getDefaultInstanceForType()
    
    
    public Space.PermissionSettings getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[Space.PermissionSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.PermissionSettings)` |   
  
### getManageApps()
    
    
    public Space.PermissionSetting getManageApps()

Optional. Setting for managing apps in a space.

` optional .google.chat.v1.Space.PermissionSetting manage_apps = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Space.PermissionSetting](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.PermissionSetting)` | The manageApps.  
  
### getManageAppsOrBuilder()
    
    
    public Space.PermissionSettingOrBuilder getManageAppsOrBuilder()

Optional. Setting for managing apps in a space.

` optional .google.chat.v1.Space.PermissionSetting manage_apps = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Space.PermissionSettingOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.PermissionSettingOrBuilder)` |   
  
### getManageMembersAndGroups()
    
    
    public Space.PermissionSetting getManageMembersAndGroups()

Optional. Setting for managing members and groups in a space.

` optional .google.chat.v1.Space.PermissionSetting manage_members_and_groups = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Space.PermissionSetting](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.PermissionSetting)` | The manageMembersAndGroups.  
  
### getManageMembersAndGroupsOrBuilder()
    
    
    public Space.PermissionSettingOrBuilder getManageMembersAndGroupsOrBuilder()

Optional. Setting for managing members and groups in a space.

` optional .google.chat.v1.Space.PermissionSetting manage_members_and_groups = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Space.PermissionSettingOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.PermissionSettingOrBuilder)` |   
  
### getManageWebhooks()
    
    
    public Space.PermissionSetting getManageWebhooks()

Optional. Setting for managing webhooks in a space.

` optional .google.chat.v1.Space.PermissionSetting manage_webhooks = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Space.PermissionSetting](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.PermissionSetting)` | The manageWebhooks.  
  
### getManageWebhooksOrBuilder()
    
    
    public Space.PermissionSettingOrBuilder getManageWebhooksOrBuilder()

Optional. Setting for managing webhooks in a space.

` optional .google.chat.v1.Space.PermissionSetting manage_webhooks = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Space.PermissionSettingOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.PermissionSettingOrBuilder)` |   
  
### getModifySpaceDetails()
    
    
    public Space.PermissionSetting getModifySpaceDetails()

Optional. Setting for updating space name, avatar, description and guidelines.

` optional .google.chat.v1.Space.PermissionSetting modify_space_details = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Space.PermissionSetting](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.PermissionSetting)` | The modifySpaceDetails.  
  
### getModifySpaceDetailsOrBuilder()
    
    
    public Space.PermissionSettingOrBuilder getModifySpaceDetailsOrBuilder()

Optional. Setting for updating space name, avatar, description and guidelines.

` optional .google.chat.v1.Space.PermissionSetting modify_space_details = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Space.PermissionSettingOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.PermissionSettingOrBuilder)` |   
  
### getParserForType()
    
    
    public Parser<Space.PermissionSettings> getParserForType()

**Returns**  
---  
**Type** | **Description**  
`[Parser](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Parser.html)<[PermissionSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.PermissionSettings)>` |   
**Overrides**

[GeneratedMessage.getParserForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_getParserForType__)

### getPostMessages()
    
    
    public Space.PermissionSetting getPostMessages()

Output only. Setting for posting messages in a space.

` optional .google.chat.v1.Space.PermissionSetting post_messages = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Space.PermissionSetting](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.PermissionSetting)` | The postMessages.  
  
### getPostMessagesOrBuilder()
    
    
    public Space.PermissionSettingOrBuilder getPostMessagesOrBuilder()

Output only. Setting for posting messages in a space.

` optional .google.chat.v1.Space.PermissionSetting post_messages = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Space.PermissionSettingOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.PermissionSettingOrBuilder)` |   
  
### getReplyMessages()
    
    
    public Space.PermissionSetting getReplyMessages()

Optional. Setting for replying to messages in a space.

` optional .google.chat.v1.Space.PermissionSetting reply_messages = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Space.PermissionSetting](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.PermissionSetting)` | The replyMessages.  
  
### getReplyMessagesOrBuilder()
    
    
    public Space.PermissionSettingOrBuilder getReplyMessagesOrBuilder()

Optional. Setting for replying to messages in a space.

` optional .google.chat.v1.Space.PermissionSetting reply_messages = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Space.PermissionSettingOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.PermissionSettingOrBuilder)` |   
  
### getSerializedSize()
    
    
    public int getSerializedSize()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[GeneratedMessage.getSerializedSize()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_getSerializedSize__)

### getToggleHistory()
    
    
    public Space.PermissionSetting getToggleHistory()

Optional. Setting for toggling space history on and off.

` optional .google.chat.v1.Space.PermissionSetting toggle_history = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Space.PermissionSetting](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.PermissionSetting)` | The toggleHistory.  
  
### getToggleHistoryOrBuilder()
    
    
    public Space.PermissionSettingOrBuilder getToggleHistoryOrBuilder()

Optional. Setting for toggling space history on and off.

` optional .google.chat.v1.Space.PermissionSetting toggle_history = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Space.PermissionSettingOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.PermissionSettingOrBuilder)` |   
  
### getUseAtMentionAll()
    
    
    public Space.PermissionSetting getUseAtMentionAll()

Optional. Setting for using @all in a space.

` optional .google.chat.v1.Space.PermissionSetting use_at_mention_all = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Space.PermissionSetting](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.PermissionSetting)` | The useAtMentionAll.  
  
### getUseAtMentionAllOrBuilder()
    
    
    public Space.PermissionSettingOrBuilder getUseAtMentionAllOrBuilder()

Optional. Setting for using @all in a space.

` optional .google.chat.v1.Space.PermissionSetting use_at_mention_all = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Space.PermissionSettingOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.PermissionSettingOrBuilder)` |   
  
### getViewSpaceMembership()
    
    
    public Space.PermissionSetting getViewSpaceMembership()

Optional. Setting for viewing space membership. Must be specified together with `AccessPermissionSettings.view_space_membership_setting` in the update mask and request body when updating who can view space membership. When restricting view access to specific roles (for example, space managers or assistant managers only), specify the desired role permissions here and provide an empty `AccessPermissionSettings.view_space_membership_setting` in the same request. If a target audience is configured in `AccessPermissionSettings.view_space_membership_setting`, this setting must be granted to all members.

` optional .google.chat.v1.Space.PermissionSetting view_space_membership = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Space.PermissionSetting](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.PermissionSetting)` | The viewSpaceMembership.  
  
### getViewSpaceMembershipOrBuilder()
    
    
    public Space.PermissionSettingOrBuilder getViewSpaceMembershipOrBuilder()

Optional. Setting for viewing space membership. Must be specified together with `AccessPermissionSettings.view_space_membership_setting` in the update mask and request body when updating who can view space membership. When restricting view access to specific roles (for example, space managers or assistant managers only), specify the desired role permissions here and provide an empty `AccessPermissionSettings.view_space_membership_setting` in the same request. If a target audience is configured in `AccessPermissionSettings.view_space_membership_setting`, this setting must be granted to all members.

` optional .google.chat.v1.Space.PermissionSetting view_space_membership = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Space.PermissionSettingOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.PermissionSettingOrBuilder)` |   
  
### hasManageApps()
    
    
    public boolean hasManageApps()

Optional. Setting for managing apps in a space.

` optional .google.chat.v1.Space.PermissionSetting manage_apps = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the manageApps field is set.  
  
### hasManageMembersAndGroups()
    
    
    public boolean hasManageMembersAndGroups()

Optional. Setting for managing members and groups in a space.

` optional .google.chat.v1.Space.PermissionSetting manage_members_and_groups = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the manageMembersAndGroups field is set.  
  
### hasManageWebhooks()
    
    
    public boolean hasManageWebhooks()

Optional. Setting for managing webhooks in a space.

` optional .google.chat.v1.Space.PermissionSetting manage_webhooks = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the manageWebhooks field is set.  
  
### hasModifySpaceDetails()
    
    
    public boolean hasModifySpaceDetails()

Optional. Setting for updating space name, avatar, description and guidelines.

` optional .google.chat.v1.Space.PermissionSetting modify_space_details = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the modifySpaceDetails field is set.  
  
### hasPostMessages()
    
    
    public boolean hasPostMessages()

Output only. Setting for posting messages in a space.

` optional .google.chat.v1.Space.PermissionSetting post_messages = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the postMessages field is set.  
  
### hasReplyMessages()
    
    
    public boolean hasReplyMessages()

Optional. Setting for replying to messages in a space.

` optional .google.chat.v1.Space.PermissionSetting reply_messages = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the replyMessages field is set.  
  
### hasToggleHistory()
    
    
    public boolean hasToggleHistory()

Optional. Setting for toggling space history on and off.

` optional .google.chat.v1.Space.PermissionSetting toggle_history = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the toggleHistory field is set.  
  
### hasUseAtMentionAll()
    
    
    public boolean hasUseAtMentionAll()

Optional. Setting for using @all in a space.

` optional .google.chat.v1.Space.PermissionSetting use_at_mention_all = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the useAtMentionAll field is set.  
  
### hasViewSpaceMembership()
    
    
    public boolean hasViewSpaceMembership()

Optional. Setting for viewing space membership. Must be specified together with `AccessPermissionSettings.view_space_membership_setting` in the update mask and request body when updating who can view space membership. When restricting view access to specific roles (for example, space managers or assistant managers only), specify the desired role permissions here and provide an empty `AccessPermissionSettings.view_space_membership_setting` in the same request. If a target audience is configured in `AccessPermissionSettings.view_space_membership_setting`, this setting must be granted to all members.

` optional .google.chat.v1.Space.PermissionSetting view_space_membership = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the viewSpaceMembership field is set.  
  
### hashCode()
    
    
    public int hashCode()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[AbstractMessage.hashCode()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.html#com_google_protobuf_AbstractMessage_hashCode__)

### internalGetFieldAccessorTable()
    
    
    protected GeneratedMessage.FieldAccessorTable internalGetFieldAccessorTable()

**Returns**  
---  
**Type** | **Description**  
`[FieldAccessorTable](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.FieldAccessorTable.html)` |   
**Overrides**

[GeneratedMessage.internalGetFieldAccessorTable()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_internalGetFieldAccessorTable__)

### isInitialized()
    
    
    public final boolean isInitialized()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[GeneratedMessage.isInitialized()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_isInitialized__)

### newBuilderForType()
    
    
    public Space.PermissionSettings.Builder newBuilderForType()

**Returns**  
---  
**Type** | **Description**  
`[Space.PermissionSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.PermissionSettings.Builder)` |   
  
### newBuilderForType(AbstractMessage.BuilderParent parent)
    
    
    protected Space.PermissionSettings.Builder newBuilderForType(AbstractMessage.BuilderParent parent)

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[BuilderParent](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.BuilderParent.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Space.PermissionSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.PermissionSettings.Builder)` |   
**Overrides**

[AbstractMessage.newBuilderForType(AbstractMessage.BuilderParent parent)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.html#com_google_protobuf_AbstractMessage_newBuilderForType_com_google_protobuf_AbstractMessage_BuilderParent_)

### toBuilder()
    
    
    public Space.PermissionSettings.Builder toBuilder()

**Returns**  
---  
**Type** | **Description**  
`[Space.PermissionSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space.PermissionSettings.Builder)` |   
  
### writeTo(CodedOutputStream output)
    
    
    public void writeTo(CodedOutputStream output)

**Parameter**  
---  
**Name** | **Description**  
`output` | `[CodedOutputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedOutputStream.html)`  
  
**Overrides**

[GeneratedMessage.writeTo(CodedOutputStream output)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_writeTo_com_google_protobuf_CodedOutputStream_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
