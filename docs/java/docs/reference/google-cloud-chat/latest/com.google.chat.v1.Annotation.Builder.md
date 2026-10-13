---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Annotation.Builder
title: Class Annotation.Builder (0.63.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:13:20.776052+00:00
---

# Class Annotation.Builder (0.63.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Annotation.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class Annotation.Builder (0.63.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.63.0 (latest)  0.59.0  0.58.0  0.57.0  0.55.0  0.52.0  0.51.0  0.49.0  0.47.0  0.46.0  0.45.0  0.44.0  0.42.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.34.0  0.32.0  0.31.0  0.28.0  0.27.0  0.26.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.1.0 
    
    
    public static final class Annotation.Builder extends GeneratedMessage.Builder<Annotation.Builder> implements AnnotationOrBuilder

Annotations can be associated with the plain-text body of the message or with chips that link to Google Workspace resources like Google Docs or Sheets with `start_index` and `length` of 0. To add basic formatting to a text message, see [Format text messages](https://developers.google.com/workspace/chat/format-messages).

Example plain-text message body: ``` Hello @FooBot how are you!" ````

` `

` The corresponding annotations metadata: ``` "annotations":[{ "type":"USER_MENTION", "startIndex":6, "length":7, "userMention": { "user": { "name":"users/{user}", "displayName":"FooBot", "avatarUrl":"<https://goo.gl/aeDtrS>", "type":"BOT" }, "type":"MENTION" } }] ```

Protobuf type `google.chat.v1.Annotation`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > Annotation.Builder

## Implements

[AnnotationOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.AnnotationOrBuilder)

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
    
    
    public Annotation build()

**Returns**  
---  
**Type** | **Description**  
`[Annotation](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Annotation)` |   
  
### buildPartial()
    
    
    public Annotation buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[Annotation](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Annotation)` |   
  
### clear()
    
    
    public Annotation.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[Annotation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Annotation.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearCustomEmojiMetadata()
    
    
    public Annotation.Builder clearCustomEmojiMetadata()

The metadata for a custom emoji.

`.google.chat.v1.CustomEmojiMetadata custom_emoji_metadata = 7;`

**Returns**  
---  
**Type** | **Description**  
`[Annotation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Annotation.Builder)` |   
  
### clearLength()
    
    
    public Annotation.Builder clearLength()

Length of the substring in the plain-text message body this annotation corresponds to. If not present, indicates a length of 0.

`int32 length = 3;`

**Returns**  
---  
**Type** | **Description**  
`[Annotation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Annotation.Builder)` | This builder for chaining.  
  
### clearMetadata()
    
    
    public Annotation.Builder clearMetadata()

**Returns**  
---  
**Type** | **Description**  
`[Annotation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Annotation.Builder)` |   
  
### clearRichLinkMetadata()
    
    
    public Annotation.Builder clearRichLinkMetadata()

The metadata for a rich link.

`.google.chat.v1.RichLinkMetadata rich_link_metadata = 6;`

**Returns**  
---  
**Type** | **Description**  
`[Annotation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Annotation.Builder)` |   
  
### clearSlashCommand()
    
    
    public Annotation.Builder clearSlashCommand()

The metadata for a slash command.

`.google.chat.v1.SlashCommandMetadata slash_command = 5;`

**Returns**  
---  
**Type** | **Description**  
`[Annotation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Annotation.Builder)` |   
  
### clearStartIndex()
    
    
    public Annotation.Builder clearStartIndex()

Start index (0-based, inclusive) in the plain-text message body this annotation corresponds to.

`optional int32 start_index = 2;`

**Returns**  
---  
**Type** | **Description**  
`[Annotation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Annotation.Builder)` | This builder for chaining.  
  
### clearType()
    
    
    public Annotation.Builder clearType()

The type of this annotation.

`.google.chat.v1.AnnotationType type = 1;`

**Returns**  
---  
**Type** | **Description**  
`[Annotation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Annotation.Builder)` | This builder for chaining.  
  
### clearUserMention()
    
    
    public Annotation.Builder clearUserMention()

The metadata of user mention.

`.google.chat.v1.UserMentionMetadata user_mention = 4;`

**Returns**  
---  
**Type** | **Description**  
`[Annotation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Annotation.Builder)` |   
  
### getCustomEmojiMetadata()
    
    
    public CustomEmojiMetadata getCustomEmojiMetadata()

The metadata for a custom emoji.

`.google.chat.v1.CustomEmojiMetadata custom_emoji_metadata = 7;`

**Returns**  
---  
**Type** | **Description**  
`[CustomEmojiMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CustomEmojiMetadata)` | The customEmojiMetadata.  
  
### getCustomEmojiMetadataBuilder()
    
    
    public CustomEmojiMetadata.Builder getCustomEmojiMetadataBuilder()

The metadata for a custom emoji.

`.google.chat.v1.CustomEmojiMetadata custom_emoji_metadata = 7;`

**Returns**  
---  
**Type** | **Description**  
`[CustomEmojiMetadata.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CustomEmojiMetadata.Builder)` |   
  
### getCustomEmojiMetadataOrBuilder()
    
    
    public CustomEmojiMetadataOrBuilder getCustomEmojiMetadataOrBuilder()

The metadata for a custom emoji.

`.google.chat.v1.CustomEmojiMetadata custom_emoji_metadata = 7;`

**Returns**  
---  
**Type** | **Description**  
`[CustomEmojiMetadataOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CustomEmojiMetadataOrBuilder)` |   
  
### getDefaultInstanceForType()
    
    
    public Annotation getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[Annotation](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Annotation)` |   
  
### getDescriptorForType()
    
    
    public Descriptors.Descriptor getDescriptorForType()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getDescriptorForType__)

### getLength()
    
    
    public int getLength()

Length of the substring in the plain-text message body this annotation corresponds to. If not present, indicates a length of 0.

`int32 length = 3;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The length.  
  
### getMetadataCase()
    
    
    public Annotation.MetadataCase getMetadataCase()

**Returns**  
---  
**Type** | **Description**  
`[Annotation.MetadataCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Annotation.MetadataCase)` |   
  
### getRichLinkMetadata()
    
    
    public RichLinkMetadata getRichLinkMetadata()

The metadata for a rich link.

`.google.chat.v1.RichLinkMetadata rich_link_metadata = 6;`

**Returns**  
---  
**Type** | **Description**  
`[RichLinkMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.RichLinkMetadata)` | The richLinkMetadata.  
  
### getRichLinkMetadataBuilder()
    
    
    public RichLinkMetadata.Builder getRichLinkMetadataBuilder()

The metadata for a rich link.

`.google.chat.v1.RichLinkMetadata rich_link_metadata = 6;`

**Returns**  
---  
**Type** | **Description**  
`[RichLinkMetadata.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.RichLinkMetadata.Builder)` |   
  
### getRichLinkMetadataOrBuilder()
    
    
    public RichLinkMetadataOrBuilder getRichLinkMetadataOrBuilder()

The metadata for a rich link.

`.google.chat.v1.RichLinkMetadata rich_link_metadata = 6;`

**Returns**  
---  
**Type** | **Description**  
`[RichLinkMetadataOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.RichLinkMetadataOrBuilder)` |   
  
### getSlashCommand()
    
    
    public SlashCommandMetadata getSlashCommand()

The metadata for a slash command.

`.google.chat.v1.SlashCommandMetadata slash_command = 5;`

**Returns**  
---  
**Type** | **Description**  
`[SlashCommandMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SlashCommandMetadata)` | The slashCommand.  
  
### getSlashCommandBuilder()
    
    
    public SlashCommandMetadata.Builder getSlashCommandBuilder()

The metadata for a slash command.

`.google.chat.v1.SlashCommandMetadata slash_command = 5;`

**Returns**  
---  
**Type** | **Description**  
`[SlashCommandMetadata.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SlashCommandMetadata.Builder)` |   
  
### getSlashCommandOrBuilder()
    
    
    public SlashCommandMetadataOrBuilder getSlashCommandOrBuilder()

The metadata for a slash command.

`.google.chat.v1.SlashCommandMetadata slash_command = 5;`

**Returns**  
---  
**Type** | **Description**  
`[SlashCommandMetadataOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SlashCommandMetadataOrBuilder)` |   
  
### getStartIndex()
    
    
    public int getStartIndex()

Start index (0-based, inclusive) in the plain-text message body this annotation corresponds to.

`optional int32 start_index = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The startIndex.  
  
### getType()
    
    
    public AnnotationType getType()

The type of this annotation.

`.google.chat.v1.AnnotationType type = 1;`

**Returns**  
---  
**Type** | **Description**  
`[AnnotationType](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.AnnotationType)` | The type.  
  
### getTypeValue()
    
    
    public int getTypeValue()

The type of this annotation.

`.google.chat.v1.AnnotationType type = 1;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for type.  
  
### getUserMention()
    
    
    public UserMentionMetadata getUserMention()

The metadata of user mention.

`.google.chat.v1.UserMentionMetadata user_mention = 4;`

**Returns**  
---  
**Type** | **Description**  
`[UserMentionMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UserMentionMetadata)` | The userMention.  
  
### getUserMentionBuilder()
    
    
    public UserMentionMetadata.Builder getUserMentionBuilder()

The metadata of user mention.

`.google.chat.v1.UserMentionMetadata user_mention = 4;`

**Returns**  
---  
**Type** | **Description**  
`[UserMentionMetadata.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UserMentionMetadata.Builder)` |   
  
### getUserMentionOrBuilder()
    
    
    public UserMentionMetadataOrBuilder getUserMentionOrBuilder()

The metadata of user mention.

`.google.chat.v1.UserMentionMetadata user_mention = 4;`

**Returns**  
---  
**Type** | **Description**  
`[UserMentionMetadataOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UserMentionMetadataOrBuilder)` |   
  
### hasCustomEmojiMetadata()
    
    
    public boolean hasCustomEmojiMetadata()

The metadata for a custom emoji.

`.google.chat.v1.CustomEmojiMetadata custom_emoji_metadata = 7;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the customEmojiMetadata field is set.  
  
### hasRichLinkMetadata()
    
    
    public boolean hasRichLinkMetadata()

The metadata for a rich link.

`.google.chat.v1.RichLinkMetadata rich_link_metadata = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the richLinkMetadata field is set.  
  
### hasSlashCommand()
    
    
    public boolean hasSlashCommand()

The metadata for a slash command.

`.google.chat.v1.SlashCommandMetadata slash_command = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the slashCommand field is set.  
  
### hasStartIndex()
    
    
    public boolean hasStartIndex()

Start index (0-based, inclusive) in the plain-text message body this annotation corresponds to.

`optional int32 start_index = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the startIndex field is set.  
  
### hasUserMention()
    
    
    public boolean hasUserMention()

The metadata of user mention.

`.google.chat.v1.UserMentionMetadata user_mention = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the userMention field is set.  
  
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

### mergeCustomEmojiMetadata(CustomEmojiMetadata value)
    
    
    public Annotation.Builder mergeCustomEmojiMetadata(CustomEmojiMetadata value)

The metadata for a custom emoji.

`.google.chat.v1.CustomEmojiMetadata custom_emoji_metadata = 7;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[CustomEmojiMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CustomEmojiMetadata)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Annotation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Annotation.Builder)` |   
  
### mergeFrom(Annotation other)
    
    
    public Annotation.Builder mergeFrom(Annotation other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Annotation](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Annotation)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Annotation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Annotation.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public Annotation.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Annotation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Annotation.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public Annotation.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Annotation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Annotation.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### mergeRichLinkMetadata(RichLinkMetadata value)
    
    
    public Annotation.Builder mergeRichLinkMetadata(RichLinkMetadata value)

The metadata for a rich link.

`.google.chat.v1.RichLinkMetadata rich_link_metadata = 6;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[RichLinkMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.RichLinkMetadata)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Annotation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Annotation.Builder)` |   
  
### mergeSlashCommand(SlashCommandMetadata value)
    
    
    public Annotation.Builder mergeSlashCommand(SlashCommandMetadata value)

The metadata for a slash command.

`.google.chat.v1.SlashCommandMetadata slash_command = 5;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[SlashCommandMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SlashCommandMetadata)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Annotation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Annotation.Builder)` |   
  
### mergeUserMention(UserMentionMetadata value)
    
    
    public Annotation.Builder mergeUserMention(UserMentionMetadata value)

The metadata of user mention.

`.google.chat.v1.UserMentionMetadata user_mention = 4;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[UserMentionMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UserMentionMetadata)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Annotation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Annotation.Builder)` |   
  
### setCustomEmojiMetadata(CustomEmojiMetadata value)
    
    
    public Annotation.Builder setCustomEmojiMetadata(CustomEmojiMetadata value)

The metadata for a custom emoji.

`.google.chat.v1.CustomEmojiMetadata custom_emoji_metadata = 7;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[CustomEmojiMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CustomEmojiMetadata)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Annotation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Annotation.Builder)` |   
  
### setCustomEmojiMetadata(CustomEmojiMetadata.Builder builderForValue)
    
    
    public Annotation.Builder setCustomEmojiMetadata(CustomEmojiMetadata.Builder builderForValue)

The metadata for a custom emoji.

`.google.chat.v1.CustomEmojiMetadata custom_emoji_metadata = 7;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[CustomEmojiMetadata.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CustomEmojiMetadata.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Annotation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Annotation.Builder)` |   
  
### setLength(int value)
    
    
    public Annotation.Builder setLength(int value)

Length of the substring in the plain-text message body this annotation corresponds to. If not present, indicates a length of 0.

`int32 length = 3;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The length to set.  
**Returns**  
---  
**Type** | **Description**  
`[Annotation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Annotation.Builder)` | This builder for chaining.  
  
### setRichLinkMetadata(RichLinkMetadata value)
    
    
    public Annotation.Builder setRichLinkMetadata(RichLinkMetadata value)

The metadata for a rich link.

`.google.chat.v1.RichLinkMetadata rich_link_metadata = 6;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[RichLinkMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.RichLinkMetadata)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Annotation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Annotation.Builder)` |   
  
### setRichLinkMetadata(RichLinkMetadata.Builder builderForValue)
    
    
    public Annotation.Builder setRichLinkMetadata(RichLinkMetadata.Builder builderForValue)

The metadata for a rich link.

`.google.chat.v1.RichLinkMetadata rich_link_metadata = 6;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[RichLinkMetadata.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.RichLinkMetadata.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Annotation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Annotation.Builder)` |   
  
### setSlashCommand(SlashCommandMetadata value)
    
    
    public Annotation.Builder setSlashCommand(SlashCommandMetadata value)

The metadata for a slash command.

`.google.chat.v1.SlashCommandMetadata slash_command = 5;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[SlashCommandMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SlashCommandMetadata)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Annotation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Annotation.Builder)` |   
  
### setSlashCommand(SlashCommandMetadata.Builder builderForValue)
    
    
    public Annotation.Builder setSlashCommand(SlashCommandMetadata.Builder builderForValue)

The metadata for a slash command.

`.google.chat.v1.SlashCommandMetadata slash_command = 5;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[SlashCommandMetadata.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SlashCommandMetadata.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Annotation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Annotation.Builder)` |   
  
### setStartIndex(int value)
    
    
    public Annotation.Builder setStartIndex(int value)

Start index (0-based, inclusive) in the plain-text message body this annotation corresponds to.

`optional int32 start_index = 2;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The startIndex to set.  
**Returns**  
---  
**Type** | **Description**  
`[Annotation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Annotation.Builder)` | This builder for chaining.  
  
### setType(AnnotationType value)
    
    
    public Annotation.Builder setType(AnnotationType value)

The type of this annotation.

`.google.chat.v1.AnnotationType type = 1;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[AnnotationType](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.AnnotationType)`  
The type to set.  
**Returns**  
---  
**Type** | **Description**  
`[Annotation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Annotation.Builder)` | This builder for chaining.  
  
### setTypeValue(int value)
    
    
    public Annotation.Builder setTypeValue(int value)

The type of this annotation.

`.google.chat.v1.AnnotationType type = 1;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The enum numeric value on the wire for type to set.  
**Returns**  
---  
**Type** | **Description**  
`[Annotation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Annotation.Builder)` | This builder for chaining.  
  
### setUserMention(UserMentionMetadata value)
    
    
    public Annotation.Builder setUserMention(UserMentionMetadata value)

The metadata of user mention.

`.google.chat.v1.UserMentionMetadata user_mention = 4;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[UserMentionMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UserMentionMetadata)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Annotation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Annotation.Builder)` |   
  
### setUserMention(UserMentionMetadata.Builder builderForValue)
    
    
    public Annotation.Builder setUserMention(UserMentionMetadata.Builder builderForValue)

The metadata of user mention.

`.google.chat.v1.UserMentionMetadata user_mention = 4;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[UserMentionMetadata.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UserMentionMetadata.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Annotation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Annotation.Builder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
