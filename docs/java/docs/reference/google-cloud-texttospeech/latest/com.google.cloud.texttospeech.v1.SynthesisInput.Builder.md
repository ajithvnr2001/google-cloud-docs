---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.SynthesisInput.Builder
title: Class SynthesisInput.Builder (2.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:02:37.906379+00:00
---

# Class SynthesisInput.Builder (2.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.SynthesisInput.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class SynthesisInput.Builder (2.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.100.0 (latest)  2.96.0  2.95.0  2.94.0  2.92.0  2.89.0  2.88.0  2.86.0  2.84.0  2.83.0  2.81.0  2.79.0  2.77.0  2.76.0  2.75.0  2.74.0  2.73.0  2.71.0  2.69.0  2.68.0  2.65.0  2.64.0  2.63.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.9  2.3.0  2.2.1  2.1.5 
    
    
    public static final class SynthesisInput.Builder extends GeneratedMessage.Builder<SynthesisInput.Builder> implements SynthesisInputOrBuilder

Contains text input to be synthesized. Either `text` or `ssml` must be supplied. Supplying both or neither returns google.rpc.Code.INVALID_ARGUMENT. The input size is limited to 5000 bytes.

Protobuf type `google.cloud.texttospeech.v1.SynthesisInput`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > SynthesisInput.Builder

## Implements

[SynthesisInputOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.SynthesisInputOrBuilder)

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
    
    
    public SynthesisInput build()

**Returns**  
---  
**Type** | **Description**  
`[SynthesisInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.SynthesisInput)` |   
  
### buildPartial()
    
    
    public SynthesisInput buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[SynthesisInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.SynthesisInput)` |   
  
### clear()
    
    
    public SynthesisInput.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[SynthesisInput.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.SynthesisInput.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearCustomPronunciations()
    
    
    public SynthesisInput.Builder clearCustomPronunciations()

Optional. The pronunciation customizations are applied to the input. If this is set, the input is synthesized using the given pronunciation customizations.

The initial support is for en-us, with plans to expand to other locales in the future. Instant Clone voices aren't supported.

In order to customize the pronunciation of a phrase, there must be an exact match of the phrase in the input types. If using SSML, the phrase must not be inside a phoneme tag.

` .google.cloud.texttospeech.v1.CustomPronunciations custom_pronunciations = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[SynthesisInput.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.SynthesisInput.Builder)` |   
  
### clearInputSource()
    
    
    public SynthesisInput.Builder clearInputSource()

**Returns**  
---  
**Type** | **Description**  
`[SynthesisInput.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.SynthesisInput.Builder)` |   
  
### clearMarkup()
    
    
    public SynthesisInput.Builder clearMarkup()

Markup for Chirp 3: HD voices specifically. This field may not be used with any other voices.

`string markup = 5;`

**Returns**  
---  
**Type** | **Description**  
`[SynthesisInput.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.SynthesisInput.Builder)` | This builder for chaining.  
  
### clearMultiSpeakerMarkup()
    
    
    public SynthesisInput.Builder clearMultiSpeakerMarkup()

The multi-speaker input to be synthesized. Only applicable for multi-speaker synthesis.

`.google.cloud.texttospeech.v1.MultiSpeakerMarkup multi_speaker_markup = 4;`

**Returns**  
---  
**Type** | **Description**  
`[SynthesisInput.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.SynthesisInput.Builder)` |   
  
### clearPrompt()
    
    
    public SynthesisInput.Builder clearPrompt()

This system instruction is supported only for controllable/promptable voice models. If this system instruction is used, we pass the unedited text to Gemini-TTS. Otherwise, a default system instruction is used. AI Studio calls this system instruction, Style Instructions.

`optional string prompt = 6;`

**Returns**  
---  
**Type** | **Description**  
`[SynthesisInput.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.SynthesisInput.Builder)` | This builder for chaining.  
  
### clearSsml()
    
    
    public SynthesisInput.Builder clearSsml()

The SSML document to be synthesized. The SSML document must be valid and well-formed. Otherwise the RPC will fail and return google.rpc.Code.INVALID_ARGUMENT. For more information, see [SSML](https://cloud.google.com/text-to-speech/docs/ssml).

`string ssml = 2;`

**Returns**  
---  
**Type** | **Description**  
`[SynthesisInput.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.SynthesisInput.Builder)` | This builder for chaining.  
  
### clearText()
    
    
    public SynthesisInput.Builder clearText()

The raw text to be synthesized.

`string text = 1;`

**Returns**  
---  
**Type** | **Description**  
`[SynthesisInput.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.SynthesisInput.Builder)` | This builder for chaining.  
  
### getCustomPronunciations()
    
    
    public CustomPronunciations getCustomPronunciations()

Optional. The pronunciation customizations are applied to the input. If this is set, the input is synthesized using the given pronunciation customizations.

The initial support is for en-us, with plans to expand to other locales in the future. Instant Clone voices aren't supported.

In order to customize the pronunciation of a phrase, there must be an exact match of the phrase in the input types. If using SSML, the phrase must not be inside a phoneme tag.

` .google.cloud.texttospeech.v1.CustomPronunciations custom_pronunciations = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[CustomPronunciations](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.CustomPronunciations)` | The customPronunciations.  
  
### getCustomPronunciationsBuilder()
    
    
    public CustomPronunciations.Builder getCustomPronunciationsBuilder()

Optional. The pronunciation customizations are applied to the input. If this is set, the input is synthesized using the given pronunciation customizations.

The initial support is for en-us, with plans to expand to other locales in the future. Instant Clone voices aren't supported.

In order to customize the pronunciation of a phrase, there must be an exact match of the phrase in the input types. If using SSML, the phrase must not be inside a phoneme tag.

` .google.cloud.texttospeech.v1.CustomPronunciations custom_pronunciations = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[CustomPronunciations.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.CustomPronunciations.Builder)` |   
  
### getCustomPronunciationsOrBuilder()
    
    
    public CustomPronunciationsOrBuilder getCustomPronunciationsOrBuilder()

Optional. The pronunciation customizations are applied to the input. If this is set, the input is synthesized using the given pronunciation customizations.

The initial support is for en-us, with plans to expand to other locales in the future. Instant Clone voices aren't supported.

In order to customize the pronunciation of a phrase, there must be an exact match of the phrase in the input types. If using SSML, the phrase must not be inside a phoneme tag.

` .google.cloud.texttospeech.v1.CustomPronunciations custom_pronunciations = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[CustomPronunciationsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.CustomPronunciationsOrBuilder)` |   
  
### getDefaultInstanceForType()
    
    
    public SynthesisInput getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[SynthesisInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.SynthesisInput)` |   
  
### getDescriptorForType()
    
    
    public Descriptors.Descriptor getDescriptorForType()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getDescriptorForType__)

### getInputSourceCase()
    
    
    public SynthesisInput.InputSourceCase getInputSourceCase()

**Returns**  
---  
**Type** | **Description**  
`[SynthesisInput.InputSourceCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.SynthesisInput.InputSourceCase)` |   
  
### getMarkup()
    
    
    public String getMarkup()

Markup for Chirp 3: HD voices specifically. This field may not be used with any other voices.

`string markup = 5;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The markup.  
  
### getMarkupBytes()
    
    
    public ByteString getMarkupBytes()

Markup for Chirp 3: HD voices specifically. This field may not be used with any other voices.

`string markup = 5;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for markup.  
  
### getMultiSpeakerMarkup()
    
    
    public MultiSpeakerMarkup getMultiSpeakerMarkup()

The multi-speaker input to be synthesized. Only applicable for multi-speaker synthesis.

`.google.cloud.texttospeech.v1.MultiSpeakerMarkup multi_speaker_markup = 4;`

**Returns**  
---  
**Type** | **Description**  
`[MultiSpeakerMarkup](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.MultiSpeakerMarkup)` | The multiSpeakerMarkup.  
  
### getMultiSpeakerMarkupBuilder()
    
    
    public MultiSpeakerMarkup.Builder getMultiSpeakerMarkupBuilder()

The multi-speaker input to be synthesized. Only applicable for multi-speaker synthesis.

`.google.cloud.texttospeech.v1.MultiSpeakerMarkup multi_speaker_markup = 4;`

**Returns**  
---  
**Type** | **Description**  
`[MultiSpeakerMarkup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.MultiSpeakerMarkup.Builder)` |   
  
### getMultiSpeakerMarkupOrBuilder()
    
    
    public MultiSpeakerMarkupOrBuilder getMultiSpeakerMarkupOrBuilder()

The multi-speaker input to be synthesized. Only applicable for multi-speaker synthesis.

`.google.cloud.texttospeech.v1.MultiSpeakerMarkup multi_speaker_markup = 4;`

**Returns**  
---  
**Type** | **Description**  
`[MultiSpeakerMarkupOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.MultiSpeakerMarkupOrBuilder)` |   
  
### getPrompt()
    
    
    public String getPrompt()

This system instruction is supported only for controllable/promptable voice models. If this system instruction is used, we pass the unedited text to Gemini-TTS. Otherwise, a default system instruction is used. AI Studio calls this system instruction, Style Instructions.

`optional string prompt = 6;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The prompt.  
  
### getPromptBytes()
    
    
    public ByteString getPromptBytes()

This system instruction is supported only for controllable/promptable voice models. If this system instruction is used, we pass the unedited text to Gemini-TTS. Otherwise, a default system instruction is used. AI Studio calls this system instruction, Style Instructions.

`optional string prompt = 6;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for prompt.  
  
### getSsml()
    
    
    public String getSsml()

The SSML document to be synthesized. The SSML document must be valid and well-formed. Otherwise the RPC will fail and return google.rpc.Code.INVALID_ARGUMENT. For more information, see [SSML](https://cloud.google.com/text-to-speech/docs/ssml).

`string ssml = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The ssml.  
  
### getSsmlBytes()
    
    
    public ByteString getSsmlBytes()

The SSML document to be synthesized. The SSML document must be valid and well-formed. Otherwise the RPC will fail and return google.rpc.Code.INVALID_ARGUMENT. For more information, see [SSML](https://cloud.google.com/text-to-speech/docs/ssml).

`string ssml = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for ssml.  
  
### getText()
    
    
    public String getText()

The raw text to be synthesized.

`string text = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The text.  
  
### getTextBytes()
    
    
    public ByteString getTextBytes()

The raw text to be synthesized.

`string text = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for text.  
  
### hasCustomPronunciations()
    
    
    public boolean hasCustomPronunciations()

Optional. The pronunciation customizations are applied to the input. If this is set, the input is synthesized using the given pronunciation customizations.

The initial support is for en-us, with plans to expand to other locales in the future. Instant Clone voices aren't supported.

In order to customize the pronunciation of a phrase, there must be an exact match of the phrase in the input types. If using SSML, the phrase must not be inside a phoneme tag.

` .google.cloud.texttospeech.v1.CustomPronunciations custom_pronunciations = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the customPronunciations field is set.  
  
### hasMarkup()
    
    
    public boolean hasMarkup()

Markup for Chirp 3: HD voices specifically. This field may not be used with any other voices.

`string markup = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the markup field is set.  
  
### hasMultiSpeakerMarkup()
    
    
    public boolean hasMultiSpeakerMarkup()

The multi-speaker input to be synthesized. Only applicable for multi-speaker synthesis.

`.google.cloud.texttospeech.v1.MultiSpeakerMarkup multi_speaker_markup = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the multiSpeakerMarkup field is set.  
  
### hasPrompt()
    
    
    public boolean hasPrompt()

This system instruction is supported only for controllable/promptable voice models. If this system instruction is used, we pass the unedited text to Gemini-TTS. Otherwise, a default system instruction is used. AI Studio calls this system instruction, Style Instructions.

`optional string prompt = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the prompt field is set.  
  
### hasSsml()
    
    
    public boolean hasSsml()

The SSML document to be synthesized. The SSML document must be valid and well-formed. Otherwise the RPC will fail and return google.rpc.Code.INVALID_ARGUMENT. For more information, see [SSML](https://cloud.google.com/text-to-speech/docs/ssml).

`string ssml = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the ssml field is set.  
  
### hasText()
    
    
    public boolean hasText()

The raw text to be synthesized.

`string text = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the text field is set.  
  
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

### mergeCustomPronunciations(CustomPronunciations value)
    
    
    public SynthesisInput.Builder mergeCustomPronunciations(CustomPronunciations value)

Optional. The pronunciation customizations are applied to the input. If this is set, the input is synthesized using the given pronunciation customizations.

The initial support is for en-us, with plans to expand to other locales in the future. Instant Clone voices aren't supported.

In order to customize the pronunciation of a phrase, there must be an exact match of the phrase in the input types. If using SSML, the phrase must not be inside a phoneme tag.

` .google.cloud.texttospeech.v1.CustomPronunciations custom_pronunciations = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[CustomPronunciations](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.CustomPronunciations)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SynthesisInput.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.SynthesisInput.Builder)` |   
  
### mergeFrom(SynthesisInput other)
    
    
    public SynthesisInput.Builder mergeFrom(SynthesisInput other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[SynthesisInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.SynthesisInput)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SynthesisInput.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.SynthesisInput.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public SynthesisInput.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SynthesisInput.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.SynthesisInput.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public SynthesisInput.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SynthesisInput.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.SynthesisInput.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### mergeMultiSpeakerMarkup(MultiSpeakerMarkup value)
    
    
    public SynthesisInput.Builder mergeMultiSpeakerMarkup(MultiSpeakerMarkup value)

The multi-speaker input to be synthesized. Only applicable for multi-speaker synthesis.

`.google.cloud.texttospeech.v1.MultiSpeakerMarkup multi_speaker_markup = 4;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[MultiSpeakerMarkup](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.MultiSpeakerMarkup)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SynthesisInput.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.SynthesisInput.Builder)` |   
  
### setCustomPronunciations(CustomPronunciations value)
    
    
    public SynthesisInput.Builder setCustomPronunciations(CustomPronunciations value)

Optional. The pronunciation customizations are applied to the input. If this is set, the input is synthesized using the given pronunciation customizations.

The initial support is for en-us, with plans to expand to other locales in the future. Instant Clone voices aren't supported.

In order to customize the pronunciation of a phrase, there must be an exact match of the phrase in the input types. If using SSML, the phrase must not be inside a phoneme tag.

` .google.cloud.texttospeech.v1.CustomPronunciations custom_pronunciations = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[CustomPronunciations](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.CustomPronunciations)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SynthesisInput.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.SynthesisInput.Builder)` |   
  
### setCustomPronunciations(CustomPronunciations.Builder builderForValue)
    
    
    public SynthesisInput.Builder setCustomPronunciations(CustomPronunciations.Builder builderForValue)

Optional. The pronunciation customizations are applied to the input. If this is set, the input is synthesized using the given pronunciation customizations.

The initial support is for en-us, with plans to expand to other locales in the future. Instant Clone voices aren't supported.

In order to customize the pronunciation of a phrase, there must be an exact match of the phrase in the input types. If using SSML, the phrase must not be inside a phoneme tag.

` .google.cloud.texttospeech.v1.CustomPronunciations custom_pronunciations = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[CustomPronunciations.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.CustomPronunciations.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SynthesisInput.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.SynthesisInput.Builder)` |   
  
### setMarkup(String value)
    
    
    public SynthesisInput.Builder setMarkup(String value)

Markup for Chirp 3: HD voices specifically. This field may not be used with any other voices.

`string markup = 5;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The markup to set.  
**Returns**  
---  
**Type** | **Description**  
`[SynthesisInput.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.SynthesisInput.Builder)` | This builder for chaining.  
  
### setMarkupBytes(ByteString value)
    
    
    public SynthesisInput.Builder setMarkupBytes(ByteString value)

Markup for Chirp 3: HD voices specifically. This field may not be used with any other voices.

`string markup = 5;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for markup to set.  
**Returns**  
---  
**Type** | **Description**  
`[SynthesisInput.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.SynthesisInput.Builder)` | This builder for chaining.  
  
### setMultiSpeakerMarkup(MultiSpeakerMarkup value)
    
    
    public SynthesisInput.Builder setMultiSpeakerMarkup(MultiSpeakerMarkup value)

The multi-speaker input to be synthesized. Only applicable for multi-speaker synthesis.

`.google.cloud.texttospeech.v1.MultiSpeakerMarkup multi_speaker_markup = 4;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[MultiSpeakerMarkup](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.MultiSpeakerMarkup)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SynthesisInput.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.SynthesisInput.Builder)` |   
  
### setMultiSpeakerMarkup(MultiSpeakerMarkup.Builder builderForValue)
    
    
    public SynthesisInput.Builder setMultiSpeakerMarkup(MultiSpeakerMarkup.Builder builderForValue)

The multi-speaker input to be synthesized. Only applicable for multi-speaker synthesis.

`.google.cloud.texttospeech.v1.MultiSpeakerMarkup multi_speaker_markup = 4;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[MultiSpeakerMarkup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.MultiSpeakerMarkup.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SynthesisInput.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.SynthesisInput.Builder)` |   
  
### setPrompt(String value)
    
    
    public SynthesisInput.Builder setPrompt(String value)

This system instruction is supported only for controllable/promptable voice models. If this system instruction is used, we pass the unedited text to Gemini-TTS. Otherwise, a default system instruction is used. AI Studio calls this system instruction, Style Instructions.

`optional string prompt = 6;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The prompt to set.  
**Returns**  
---  
**Type** | **Description**  
`[SynthesisInput.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.SynthesisInput.Builder)` | This builder for chaining.  
  
### setPromptBytes(ByteString value)
    
    
    public SynthesisInput.Builder setPromptBytes(ByteString value)

This system instruction is supported only for controllable/promptable voice models. If this system instruction is used, we pass the unedited text to Gemini-TTS. Otherwise, a default system instruction is used. AI Studio calls this system instruction, Style Instructions.

`optional string prompt = 6;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for prompt to set.  
**Returns**  
---  
**Type** | **Description**  
`[SynthesisInput.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.SynthesisInput.Builder)` | This builder for chaining.  
  
### setSsml(String value)
    
    
    public SynthesisInput.Builder setSsml(String value)

The SSML document to be synthesized. The SSML document must be valid and well-formed. Otherwise the RPC will fail and return google.rpc.Code.INVALID_ARGUMENT. For more information, see [SSML](https://cloud.google.com/text-to-speech/docs/ssml).

`string ssml = 2;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The ssml to set.  
**Returns**  
---  
**Type** | **Description**  
`[SynthesisInput.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.SynthesisInput.Builder)` | This builder for chaining.  
  
### setSsmlBytes(ByteString value)
    
    
    public SynthesisInput.Builder setSsmlBytes(ByteString value)

The SSML document to be synthesized. The SSML document must be valid and well-formed. Otherwise the RPC will fail and return google.rpc.Code.INVALID_ARGUMENT. For more information, see [SSML](https://cloud.google.com/text-to-speech/docs/ssml).

`string ssml = 2;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for ssml to set.  
**Returns**  
---  
**Type** | **Description**  
`[SynthesisInput.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.SynthesisInput.Builder)` | This builder for chaining.  
  
### setText(String value)
    
    
    public SynthesisInput.Builder setText(String value)

The raw text to be synthesized.

`string text = 1;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The text to set.  
**Returns**  
---  
**Type** | **Description**  
`[SynthesisInput.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.SynthesisInput.Builder)` | This builder for chaining.  
  
### setTextBytes(ByteString value)
    
    
    public SynthesisInput.Builder setTextBytes(ByteString value)

The raw text to be synthesized.

`string text = 1;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for text to set.  
**Returns**  
---  
**Type** | **Description**  
`[SynthesisInput.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-texttospeech/latest/com.google.cloud.texttospeech.v1.SynthesisInput.Builder)` | This builder for chaining.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
