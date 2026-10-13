---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingRecognitionResult.Builder
title: Class StreamingRecognitionResult.Builder (0.110.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:07:45.374697+00:00
---

# Class StreamingRecognitionResult.Builder (0.110.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingRecognitionResult.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class StreamingRecognitionResult.Builder (0.110.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.110.0 (latest)  0.106.0  0.105.0  0.104.0  0.102.0  0.99.0  0.98.0  0.96.0  0.94.0  0.93.0  0.92.0  0.91.0  0.89.0  0.87.0  0.86.0  0.85.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.75.0  0.74.0  0.73.0  0.71.0  0.70.0  0.69.0  0.68.0  0.67.0  0.66.0  0.65.0  0.64.0  0.63.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.7  0.13.1  0.12.1  0.11.5 
    
    
    public static final class StreamingRecognitionResult.Builder extends GeneratedMessage.Builder<StreamingRecognitionResult.Builder> implements StreamingRecognitionResultOrBuilder

Contains a speech recognition result corresponding to a portion of the audio that is currently being processed or an indication that this is the end of the single requested utterance.

While end-user audio is being processed, Dialogflow sends a series of results. Each result may contain a `transcript` value. A transcript represents a portion of the utterance. While the recognizer is processing audio, transcript values may be interim values or finalized values. Once a transcript is finalized, the `is_final` value is set to true and processing continues for the next transcript.

If `StreamingDetectIntentRequest.query_input.audio.config.single_utterance` was true, and the recognizer has completed processing audio, the `message_type` value is set to `END_OF_SINGLE_UTTERANCE and the following (last) result contains the last finalized transcript.`

` `

` The complete end-user utterance is determined by concatenating the finalized transcript values received for the series of results.`

`

In the following example, single utterance is enabled. In the case where single utterance is not enabled, result 7 would not occur.

`

` `````

`` ``

Num | transcript | message_type | is_final  
---|---|---|---  
1 | "tube" | TRANSCRIPT | false  
2 | "to be a" | TRANSCRIPT | false  
3 | "to be" | TRANSCRIPT | false  
4 | "to be or not to be" | TRANSCRIPT | true  
5 | "that's" | TRANSCRIPT | false  
6 | "that is | TRANSCRIPT | false  
7 | unset | END_OF_SINGLE_UTTERANCE | unset  
8 | " that is the question" | TRANSCRIPT | true  
`` ``

`` ````

` `

` Concatenating the finalized transcripts with `is_final` set to true, the complete utterance becomes "to be or not to be that is the question".

Protobuf type `google.cloud.dialogflow.cx.v3.StreamingRecognitionResult`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > StreamingRecognitionResult.Builder

## Implements

[StreamingRecognitionResultOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingRecognitionResultOrBuilder)

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

### addAllSpeechWordInfo(Iterable<? extends SpeechWordInfo> values)
    
    
    public StreamingRecognitionResult.Builder addAllSpeechWordInfo(Iterable<? extends SpeechWordInfo> values)

Word-specific information for the words recognized by Speech in transcript. Populated if and only if `message_type` = `TRANSCRIPT` and [InputAudioConfig.enable_word_info] is set.

`repeated .google.cloud.dialogflow.cx.v3.SpeechWordInfo speech_word_info = 7;`

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<? extends com.google.cloud.dialogflow.cx.v3.SpeechWordInfo>`  
  
**Returns**  
---  
**Type** | **Description**  
`[StreamingRecognitionResult.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingRecognitionResult.Builder)` |   
  
### addSpeechWordInfo(SpeechWordInfo value)
    
    
    public StreamingRecognitionResult.Builder addSpeechWordInfo(SpeechWordInfo value)

Word-specific information for the words recognized by Speech in transcript. Populated if and only if `message_type` = `TRANSCRIPT` and [InputAudioConfig.enable_word_info] is set.

`repeated .google.cloud.dialogflow.cx.v3.SpeechWordInfo speech_word_info = 7;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[SpeechWordInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SpeechWordInfo)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StreamingRecognitionResult.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingRecognitionResult.Builder)` |   
  
### addSpeechWordInfo(SpeechWordInfo.Builder builderForValue)
    
    
    public StreamingRecognitionResult.Builder addSpeechWordInfo(SpeechWordInfo.Builder builderForValue)

Word-specific information for the words recognized by Speech in transcript. Populated if and only if `message_type` = `TRANSCRIPT` and [InputAudioConfig.enable_word_info] is set.

`repeated .google.cloud.dialogflow.cx.v3.SpeechWordInfo speech_word_info = 7;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[SpeechWordInfo.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SpeechWordInfo.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StreamingRecognitionResult.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingRecognitionResult.Builder)` |   
  
### addSpeechWordInfo(int index, SpeechWordInfo value)
    
    
    public StreamingRecognitionResult.Builder addSpeechWordInfo(int index, SpeechWordInfo value)

Word-specific information for the words recognized by Speech in transcript. Populated if and only if `message_type` = `TRANSCRIPT` and [InputAudioConfig.enable_word_info] is set.

`repeated .google.cloud.dialogflow.cx.v3.SpeechWordInfo speech_word_info = 7;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[SpeechWordInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SpeechWordInfo)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StreamingRecognitionResult.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingRecognitionResult.Builder)` |   
  
### addSpeechWordInfo(int index, SpeechWordInfo.Builder builderForValue)
    
    
    public StreamingRecognitionResult.Builder addSpeechWordInfo(int index, SpeechWordInfo.Builder builderForValue)

Word-specific information for the words recognized by Speech in transcript. Populated if and only if `message_type` = `TRANSCRIPT` and [InputAudioConfig.enable_word_info] is set.

`repeated .google.cloud.dialogflow.cx.v3.SpeechWordInfo speech_word_info = 7;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[SpeechWordInfo.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SpeechWordInfo.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StreamingRecognitionResult.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingRecognitionResult.Builder)` |   
  
### addSpeechWordInfoBuilder()
    
    
    public SpeechWordInfo.Builder addSpeechWordInfoBuilder()

Word-specific information for the words recognized by Speech in transcript. Populated if and only if `message_type` = `TRANSCRIPT` and [InputAudioConfig.enable_word_info] is set.

`repeated .google.cloud.dialogflow.cx.v3.SpeechWordInfo speech_word_info = 7;`

**Returns**  
---  
**Type** | **Description**  
`[SpeechWordInfo.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SpeechWordInfo.Builder)` |   
  
### addSpeechWordInfoBuilder(int index)
    
    
    public SpeechWordInfo.Builder addSpeechWordInfoBuilder(int index)

Word-specific information for the words recognized by Speech in transcript. Populated if and only if `message_type` = `TRANSCRIPT` and [InputAudioConfig.enable_word_info] is set.

`repeated .google.cloud.dialogflow.cx.v3.SpeechWordInfo speech_word_info = 7;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SpeechWordInfo.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SpeechWordInfo.Builder)` |   
  
### build()
    
    
    public StreamingRecognitionResult build()

**Returns**  
---  
**Type** | **Description**  
`[StreamingRecognitionResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingRecognitionResult)` |   
  
### buildPartial()
    
    
    public StreamingRecognitionResult buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[StreamingRecognitionResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingRecognitionResult)` |   
  
### clear()
    
    
    public StreamingRecognitionResult.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[StreamingRecognitionResult.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingRecognitionResult.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearConfidence()
    
    
    public StreamingRecognitionResult.Builder clearConfidence()

The Speech confidence between 0.0 and 1.0 for the current portion of audio. A higher number indicates an estimated greater likelihood that the recognized words are correct. The default of 0.0 is a sentinel value indicating that confidence was not set.

This field is typically only provided if `is_final` is true and you should not rely on it being accurate or even set.

`float confidence = 4;`

**Returns**  
---  
**Type** | **Description**  
`[StreamingRecognitionResult.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingRecognitionResult.Builder)` | This builder for chaining.  
  
### clearIsFinal()
    
    
    public StreamingRecognitionResult.Builder clearIsFinal()

If `false`, the `StreamingRecognitionResult` represents an interim result that may change. If `true`, the recognizer will not return any further hypotheses about this piece of the audio. May only be populated for `message_type` = `TRANSCRIPT`.

`bool is_final = 3;`

**Returns**  
---  
**Type** | **Description**  
`[StreamingRecognitionResult.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingRecognitionResult.Builder)` | This builder for chaining.  
  
### clearLanguageCode()
    
    
    public StreamingRecognitionResult.Builder clearLanguageCode()

Detected language code for the transcript.

`string language_code = 10;`

**Returns**  
---  
**Type** | **Description**  
`[StreamingRecognitionResult.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingRecognitionResult.Builder)` | This builder for chaining.  
  
### clearMessageType()
    
    
    public StreamingRecognitionResult.Builder clearMessageType()

Type of the result message.

`.google.cloud.dialogflow.cx.v3.StreamingRecognitionResult.MessageType message_type = 1; `

**Returns**  
---  
**Type** | **Description**  
`[StreamingRecognitionResult.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingRecognitionResult.Builder)` | This builder for chaining.  
  
### clearSpeechEndOffset()
    
    
    public StreamingRecognitionResult.Builder clearSpeechEndOffset()

Time offset of the end of this Speech recognition result relative to the beginning of the audio. Only populated for `message_type` = `TRANSCRIPT`.

`.google.protobuf.Duration speech_end_offset = 8;`

**Returns**  
---  
**Type** | **Description**  
`[StreamingRecognitionResult.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingRecognitionResult.Builder)` |   
  
### clearSpeechWordInfo()
    
    
    public StreamingRecognitionResult.Builder clearSpeechWordInfo()

Word-specific information for the words recognized by Speech in transcript. Populated if and only if `message_type` = `TRANSCRIPT` and [InputAudioConfig.enable_word_info] is set.

`repeated .google.cloud.dialogflow.cx.v3.SpeechWordInfo speech_word_info = 7;`

**Returns**  
---  
**Type** | **Description**  
`[StreamingRecognitionResult.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingRecognitionResult.Builder)` |   
  
### clearStability()
    
    
    public StreamingRecognitionResult.Builder clearStability()

An estimate of the likelihood that the speech recognizer will not change its guess about this interim recognition result:

  * If the value is unspecified or 0.0, Dialogflow didn't compute the stability. In particular, Dialogflow will only provide stability for `TRANSCRIPT` results with `is_final = false`.
  * Otherwise, the value is in (0.0, 1.0] where 0.0 means completely unstable and 1.0 means completely stable.



`float stability = 6;`

**Returns**  
---  
**Type** | **Description**  
`[StreamingRecognitionResult.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingRecognitionResult.Builder)` | This builder for chaining.  
  
### clearTranscript()
    
    
    public StreamingRecognitionResult.Builder clearTranscript()

Transcript text representing the words that the user spoke. Populated if and only if `message_type` = `TRANSCRIPT`.

`string transcript = 2;`

**Returns**  
---  
**Type** | **Description**  
`[StreamingRecognitionResult.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingRecognitionResult.Builder)` | This builder for chaining.  
  
### getConfidence()
    
    
    public float getConfidence()

The Speech confidence between 0.0 and 1.0 for the current portion of audio. A higher number indicates an estimated greater likelihood that the recognized words are correct. The default of 0.0 is a sentinel value indicating that confidence was not set.

This field is typically only provided if `is_final` is true and you should not rely on it being accurate or even set.

`float confidence = 4;`

**Returns**  
---  
**Type** | **Description**  
`[float](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The confidence.  
  
### getDefaultInstanceForType()
    
    
    public StreamingRecognitionResult getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[StreamingRecognitionResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingRecognitionResult)` |   
  
### getDescriptorForType()
    
    
    public Descriptors.Descriptor getDescriptorForType()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getDescriptorForType__)

### getIsFinal()
    
    
    public boolean getIsFinal()

If `false`, the `StreamingRecognitionResult` represents an interim result that may change. If `true`, the recognizer will not return any further hypotheses about this piece of the audio. May only be populated for `message_type` = `TRANSCRIPT`.

`bool is_final = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The isFinal.  
  
### getLanguageCode()
    
    
    public String getLanguageCode()

Detected language code for the transcript.

`string language_code = 10;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The languageCode.  
  
### getLanguageCodeBytes()
    
    
    public ByteString getLanguageCodeBytes()

Detected language code for the transcript.

`string language_code = 10;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for languageCode.  
  
### getMessageType()
    
    
    public StreamingRecognitionResult.MessageType getMessageType()

Type of the result message.

`.google.cloud.dialogflow.cx.v3.StreamingRecognitionResult.MessageType message_type = 1; `

**Returns**  
---  
**Type** | **Description**  
`[StreamingRecognitionResult.MessageType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingRecognitionResult.MessageType)` | The messageType.  
  
### getMessageTypeValue()
    
    
    public int getMessageTypeValue()

Type of the result message.

`.google.cloud.dialogflow.cx.v3.StreamingRecognitionResult.MessageType message_type = 1; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for messageType.  
  
### getSpeechEndOffset()
    
    
    public Duration getSpeechEndOffset()

Time offset of the end of this Speech recognition result relative to the beginning of the audio. Only populated for `message_type` = `TRANSCRIPT`.

`.google.protobuf.Duration speech_end_offset = 8;`

**Returns**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)` | The speechEndOffset.  
  
### getSpeechEndOffsetBuilder()
    
    
    public Duration.Builder getSpeechEndOffsetBuilder()

Time offset of the end of this Speech recognition result relative to the beginning of the audio. Only populated for `message_type` = `TRANSCRIPT`.

`.google.protobuf.Duration speech_end_offset = 8;`

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.Builder.html)` |   
  
### getSpeechEndOffsetOrBuilder()
    
    
    public DurationOrBuilder getSpeechEndOffsetOrBuilder()

Time offset of the end of this Speech recognition result relative to the beginning of the audio. Only populated for `message_type` = `TRANSCRIPT`.

`.google.protobuf.Duration speech_end_offset = 8;`

**Returns**  
---  
**Type** | **Description**  
`[DurationOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DurationOrBuilder.html)` |   
  
### getSpeechWordInfo(int index)
    
    
    public SpeechWordInfo getSpeechWordInfo(int index)

Word-specific information for the words recognized by Speech in transcript. Populated if and only if `message_type` = `TRANSCRIPT` and [InputAudioConfig.enable_word_info] is set.

`repeated .google.cloud.dialogflow.cx.v3.SpeechWordInfo speech_word_info = 7;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SpeechWordInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SpeechWordInfo)` |   
  
### getSpeechWordInfoBuilder(int index)
    
    
    public SpeechWordInfo.Builder getSpeechWordInfoBuilder(int index)

Word-specific information for the words recognized by Speech in transcript. Populated if and only if `message_type` = `TRANSCRIPT` and [InputAudioConfig.enable_word_info] is set.

`repeated .google.cloud.dialogflow.cx.v3.SpeechWordInfo speech_word_info = 7;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SpeechWordInfo.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SpeechWordInfo.Builder)` |   
  
### getSpeechWordInfoBuilderList()
    
    
    public List<SpeechWordInfo.Builder> getSpeechWordInfoBuilderList()

Word-specific information for the words recognized by Speech in transcript. Populated if and only if `message_type` = `TRANSCRIPT` and [InputAudioConfig.enable_word_info] is set.

`repeated .google.cloud.dialogflow.cx.v3.SpeechWordInfo speech_word_info = 7;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SpeechWordInfo.Builder)>` |   
  
### getSpeechWordInfoCount()
    
    
    public int getSpeechWordInfoCount()

Word-specific information for the words recognized by Speech in transcript. Populated if and only if `message_type` = `TRANSCRIPT` and [InputAudioConfig.enable_word_info] is set.

`repeated .google.cloud.dialogflow.cx.v3.SpeechWordInfo speech_word_info = 7;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getSpeechWordInfoList()
    
    
    public List<SpeechWordInfo> getSpeechWordInfoList()

Word-specific information for the words recognized by Speech in transcript. Populated if and only if `message_type` = `TRANSCRIPT` and [InputAudioConfig.enable_word_info] is set.

`repeated .google.cloud.dialogflow.cx.v3.SpeechWordInfo speech_word_info = 7;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[SpeechWordInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SpeechWordInfo)>` |   
  
### getSpeechWordInfoOrBuilder(int index)
    
    
    public SpeechWordInfoOrBuilder getSpeechWordInfoOrBuilder(int index)

Word-specific information for the words recognized by Speech in transcript. Populated if and only if `message_type` = `TRANSCRIPT` and [InputAudioConfig.enable_word_info] is set.

`repeated .google.cloud.dialogflow.cx.v3.SpeechWordInfo speech_word_info = 7;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SpeechWordInfoOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SpeechWordInfoOrBuilder)` |   
  
### getSpeechWordInfoOrBuilderList()
    
    
    public List<? extends SpeechWordInfoOrBuilder> getSpeechWordInfoOrBuilderList()

Word-specific information for the words recognized by Speech in transcript. Populated if and only if `message_type` = `TRANSCRIPT` and [InputAudioConfig.enable_word_info] is set.

`repeated .google.cloud.dialogflow.cx.v3.SpeechWordInfo speech_word_info = 7;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.dialogflow.cx.v3.SpeechWordInfoOrBuilder>` |   
  
### getStability()
    
    
    public float getStability()

An estimate of the likelihood that the speech recognizer will not change its guess about this interim recognition result:

  * If the value is unspecified or 0.0, Dialogflow didn't compute the stability. In particular, Dialogflow will only provide stability for `TRANSCRIPT` results with `is_final = false`.
  * Otherwise, the value is in (0.0, 1.0] where 0.0 means completely unstable and 1.0 means completely stable.



`float stability = 6;`

**Returns**  
---  
**Type** | **Description**  
`[float](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The stability.  
  
### getTranscript()
    
    
    public String getTranscript()

Transcript text representing the words that the user spoke. Populated if and only if `message_type` = `TRANSCRIPT`.

`string transcript = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The transcript.  
  
### getTranscriptBytes()
    
    
    public ByteString getTranscriptBytes()

Transcript text representing the words that the user spoke. Populated if and only if `message_type` = `TRANSCRIPT`.

`string transcript = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for transcript.  
  
### hasSpeechEndOffset()
    
    
    public boolean hasSpeechEndOffset()

Time offset of the end of this Speech recognition result relative to the beginning of the audio. Only populated for `message_type` = `TRANSCRIPT`.

`.google.protobuf.Duration speech_end_offset = 8;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the speechEndOffset field is set.  
  
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

### mergeFrom(StreamingRecognitionResult other)
    
    
    public StreamingRecognitionResult.Builder mergeFrom(StreamingRecognitionResult other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[StreamingRecognitionResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingRecognitionResult)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StreamingRecognitionResult.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingRecognitionResult.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public StreamingRecognitionResult.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StreamingRecognitionResult.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingRecognitionResult.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public StreamingRecognitionResult.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StreamingRecognitionResult.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingRecognitionResult.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### mergeSpeechEndOffset(Duration value)
    
    
    public StreamingRecognitionResult.Builder mergeSpeechEndOffset(Duration value)

Time offset of the end of this Speech recognition result relative to the beginning of the audio. Only populated for `message_type` = `TRANSCRIPT`.

`.google.protobuf.Duration speech_end_offset = 8;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StreamingRecognitionResult.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingRecognitionResult.Builder)` |   
  
### removeSpeechWordInfo(int index)
    
    
    public StreamingRecognitionResult.Builder removeSpeechWordInfo(int index)

Word-specific information for the words recognized by Speech in transcript. Populated if and only if `message_type` = `TRANSCRIPT` and [InputAudioConfig.enable_word_info] is set.

`repeated .google.cloud.dialogflow.cx.v3.SpeechWordInfo speech_word_info = 7;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StreamingRecognitionResult.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingRecognitionResult.Builder)` |   
  
### setConfidence(float value)
    
    
    public StreamingRecognitionResult.Builder setConfidence(float value)

The Speech confidence between 0.0 and 1.0 for the current portion of audio. A higher number indicates an estimated greater likelihood that the recognized words are correct. The default of 0.0 is a sentinel value indicating that confidence was not set.

This field is typically only provided if `is_final` is true and you should not rely on it being accurate or even set.

`float confidence = 4;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[float](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The confidence to set.  
**Returns**  
---  
**Type** | **Description**  
`[StreamingRecognitionResult.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingRecognitionResult.Builder)` | This builder for chaining.  
  
### setIsFinal(boolean value)
    
    
    public StreamingRecognitionResult.Builder setIsFinal(boolean value)

If `false`, the `StreamingRecognitionResult` represents an interim result that may change. If `true`, the recognizer will not return any further hypotheses about this piece of the audio. May only be populated for `message_type` = `TRANSCRIPT`.

`bool is_final = 3;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The isFinal to set.  
**Returns**  
---  
**Type** | **Description**  
`[StreamingRecognitionResult.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingRecognitionResult.Builder)` | This builder for chaining.  
  
### setLanguageCode(String value)
    
    
    public StreamingRecognitionResult.Builder setLanguageCode(String value)

Detected language code for the transcript.

`string language_code = 10;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The languageCode to set.  
**Returns**  
---  
**Type** | **Description**  
`[StreamingRecognitionResult.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingRecognitionResult.Builder)` | This builder for chaining.  
  
### setLanguageCodeBytes(ByteString value)
    
    
    public StreamingRecognitionResult.Builder setLanguageCodeBytes(ByteString value)

Detected language code for the transcript.

`string language_code = 10;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for languageCode to set.  
**Returns**  
---  
**Type** | **Description**  
`[StreamingRecognitionResult.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingRecognitionResult.Builder)` | This builder for chaining.  
  
### setMessageType(StreamingRecognitionResult.MessageType value)
    
    
    public StreamingRecognitionResult.Builder setMessageType(StreamingRecognitionResult.MessageType value)

Type of the result message.

`.google.cloud.dialogflow.cx.v3.StreamingRecognitionResult.MessageType message_type = 1; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[StreamingRecognitionResult.MessageType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingRecognitionResult.MessageType)`  
The messageType to set.  
**Returns**  
---  
**Type** | **Description**  
`[StreamingRecognitionResult.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingRecognitionResult.Builder)` | This builder for chaining.  
  
### setMessageTypeValue(int value)
    
    
    public StreamingRecognitionResult.Builder setMessageTypeValue(int value)

Type of the result message.

`.google.cloud.dialogflow.cx.v3.StreamingRecognitionResult.MessageType message_type = 1; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The enum numeric value on the wire for messageType to set.  
**Returns**  
---  
**Type** | **Description**  
`[StreamingRecognitionResult.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingRecognitionResult.Builder)` | This builder for chaining.  
  
### setSpeechEndOffset(Duration value)
    
    
    public StreamingRecognitionResult.Builder setSpeechEndOffset(Duration value)

Time offset of the end of this Speech recognition result relative to the beginning of the audio. Only populated for `message_type` = `TRANSCRIPT`.

`.google.protobuf.Duration speech_end_offset = 8;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StreamingRecognitionResult.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingRecognitionResult.Builder)` |   
  
### setSpeechEndOffset(Duration.Builder builderForValue)
    
    
    public StreamingRecognitionResult.Builder setSpeechEndOffset(Duration.Builder builderForValue)

Time offset of the end of this Speech recognition result relative to the beginning of the audio. Only populated for `message_type` = `TRANSCRIPT`.

`.google.protobuf.Duration speech_end_offset = 8;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StreamingRecognitionResult.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingRecognitionResult.Builder)` |   
  
### setSpeechWordInfo(int index, SpeechWordInfo value)
    
    
    public StreamingRecognitionResult.Builder setSpeechWordInfo(int index, SpeechWordInfo value)

Word-specific information for the words recognized by Speech in transcript. Populated if and only if `message_type` = `TRANSCRIPT` and [InputAudioConfig.enable_word_info] is set.

`repeated .google.cloud.dialogflow.cx.v3.SpeechWordInfo speech_word_info = 7;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[SpeechWordInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SpeechWordInfo)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StreamingRecognitionResult.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingRecognitionResult.Builder)` |   
  
### setSpeechWordInfo(int index, SpeechWordInfo.Builder builderForValue)
    
    
    public StreamingRecognitionResult.Builder setSpeechWordInfo(int index, SpeechWordInfo.Builder builderForValue)

Word-specific information for the words recognized by Speech in transcript. Populated if and only if `message_type` = `TRANSCRIPT` and [InputAudioConfig.enable_word_info] is set.

`repeated .google.cloud.dialogflow.cx.v3.SpeechWordInfo speech_word_info = 7;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[SpeechWordInfo.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SpeechWordInfo.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StreamingRecognitionResult.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingRecognitionResult.Builder)` |   
  
### setStability(float value)
    
    
    public StreamingRecognitionResult.Builder setStability(float value)

An estimate of the likelihood that the speech recognizer will not change its guess about this interim recognition result:

  * If the value is unspecified or 0.0, Dialogflow didn't compute the stability. In particular, Dialogflow will only provide stability for `TRANSCRIPT` results with `is_final = false`.
  * Otherwise, the value is in (0.0, 1.0] where 0.0 means completely unstable and 1.0 means completely stable.



`float stability = 6;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[float](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The stability to set.  
**Returns**  
---  
**Type** | **Description**  
`[StreamingRecognitionResult.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingRecognitionResult.Builder)` | This builder for chaining.  
  
### setTranscript(String value)
    
    
    public StreamingRecognitionResult.Builder setTranscript(String value)

Transcript text representing the words that the user spoke. Populated if and only if `message_type` = `TRANSCRIPT`.

`string transcript = 2;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The transcript to set.  
**Returns**  
---  
**Type** | **Description**  
`[StreamingRecognitionResult.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingRecognitionResult.Builder)` | This builder for chaining.  
  
### setTranscriptBytes(ByteString value)
    
    
    public StreamingRecognitionResult.Builder setTranscriptBytes(ByteString value)

Transcript text representing the words that the user spoke. Populated if and only if `message_type` = `TRANSCRIPT`.

`string transcript = 2;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for transcript to set.  
**Returns**  
---  
**Type** | **Description**  
`[StreamingRecognitionResult.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingRecognitionResult.Builder)` | This builder for chaining.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
