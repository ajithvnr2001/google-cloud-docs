---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingDetectIntentRequest.Builder
title: Class StreamingDetectIntentRequest.Builder (0.110.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:45:01.962518+00:00
---

# Class StreamingDetectIntentRequest.Builder (0.110.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingDetectIntentRequest.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class StreamingDetectIntentRequest.Builder (0.110.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.110.0 (latest)  0.106.0  0.105.0  0.104.0  0.102.0  0.99.0  0.98.0  0.96.0  0.94.0  0.93.0  0.92.0  0.91.0  0.89.0  0.87.0  0.86.0  0.85.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.75.0  0.74.0  0.73.0  0.71.0  0.70.0  0.69.0  0.68.0  0.67.0  0.66.0  0.65.0  0.64.0  0.63.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.7  0.13.1  0.12.1  0.11.5 
    
    
    public static final class StreamingDetectIntentRequest.Builder extends GeneratedMessage.Builder<StreamingDetectIntentRequest.Builder> implements StreamingDetectIntentRequestOrBuilder

The top-level message sent by the client to the Sessions.StreamingDetectIntent method.

Multiple request messages should be sent in order:

  1. The first message must contain session, query_input plus optionally query_params. If the client wants to receive an audio response, it should also contain output_audio_config.

  2. If query_input was set to query_input.audio.config, all subsequent messages must contain query_input.audio.audio to continue with Speech recognition. If you decide to rather detect an intent from text input after you already started Speech recognition, please send a message with query_input.text.

However, note that:

  3. Dialogflow will bill you for the audio duration so far.

  4. Dialogflow discards all Speech recognition results in favor of the input text.
  5. Dialogflow will use the language code from the first message.

After you sent all input, you must half-close or abort the request stream.




Protobuf type `google.cloud.dialogflow.cx.v3.StreamingDetectIntentRequest`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > StreamingDetectIntentRequest.Builder

## Implements

[StreamingDetectIntentRequestOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingDetectIntentRequestOrBuilder)

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
    
    
    public StreamingDetectIntentRequest build()

**Returns**  
---  
**Type** | **Description**  
`[StreamingDetectIntentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingDetectIntentRequest)` |   
  
### buildPartial()
    
    
    public StreamingDetectIntentRequest buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[StreamingDetectIntentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingDetectIntentRequest)` |   
  
### clear()
    
    
    public StreamingDetectIntentRequest.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[StreamingDetectIntentRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingDetectIntentRequest.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearEnableDebuggingInfo()
    
    
    public StreamingDetectIntentRequest.Builder clearEnableDebuggingInfo()

If true, `StreamingDetectIntentResponse.debugging_info` will get populated.

`bool enable_debugging_info = 8;`

**Returns**  
---  
**Type** | **Description**  
`[StreamingDetectIntentRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingDetectIntentRequest.Builder)` | This builder for chaining.  
  
### clearEnablePartialResponse()
    
    
    public StreamingDetectIntentRequest.Builder clearEnablePartialResponse()

Enable partial detect intent response. If this flag is not enabled, response stream still contains only one final `DetectIntentResponse` even if some `Fulfillment`s in the agent have been configured to return partial responses.

`bool enable_partial_response = 5;`

**Returns**  
---  
**Type** | **Description**  
`[StreamingDetectIntentRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingDetectIntentRequest.Builder)` | This builder for chaining.  
  
### clearOutputAudioConfig()
    
    
    public StreamingDetectIntentRequest.Builder clearOutputAudioConfig()

Instructs the speech synthesizer how to generate the output audio.

`.google.cloud.dialogflow.cx.v3.OutputAudioConfig output_audio_config = 4;`

**Returns**  
---  
**Type** | **Description**  
`[StreamingDetectIntentRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingDetectIntentRequest.Builder)` |   
  
### clearQueryInput()
    
    
    public StreamingDetectIntentRequest.Builder clearQueryInput()

Required. The input specification.

` .google.cloud.dialogflow.cx.v3.QueryInput query_input = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[StreamingDetectIntentRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingDetectIntentRequest.Builder)` |   
  
### clearQueryParams()
    
    
    public StreamingDetectIntentRequest.Builder clearQueryParams()

The parameters of this query.

`.google.cloud.dialogflow.cx.v3.QueryParameters query_params = 2;`

**Returns**  
---  
**Type** | **Description**  
`[StreamingDetectIntentRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingDetectIntentRequest.Builder)` |   
  
### clearResponseView()
    
    
    public StreamingDetectIntentRequest.Builder clearResponseView()

Optional. Specifies which fields in the QueryResult to return. If not set, the default is DETECT_INTENT_RESPONSE_VIEW_FULL.

` .google.cloud.dialogflow.cx.v3.DetectIntentResponseView response_view = 16 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[StreamingDetectIntentRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingDetectIntentRequest.Builder)` | This builder for chaining.  
  
### clearSession()
    
    
    public StreamingDetectIntentRequest.Builder clearSession()

The name of the session this query is sent to. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/sessions/<SessionID>` or `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/environments/<EnvironmentID>/sessions/<SessionID>`. If `Environment ID` is not specified, we assume default 'draft' environment. It's up to the API caller to choose an appropriate `Session ID`. It can be a random number or some type of session identifiers (preferably hashed). The length of the `Session ID` must not exceed 36 characters. Note: session must be set in the first request.

For more information, see the [sessions guide](https://cloud.google.com/dialogflow/cx/docs/concept/session).

Note: Always use agent versions for production traffic. See [Versions and environments](https://cloud.google.com/dialogflow/cx/docs/concept/version).

`string session = 1 [(.google.api.resource_reference) = { ... }`

**Returns**  
---  
**Type** | **Description**  
`[StreamingDetectIntentRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingDetectIntentRequest.Builder)` | This builder for chaining.  
  
### getDefaultInstanceForType()
    
    
    public StreamingDetectIntentRequest getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[StreamingDetectIntentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingDetectIntentRequest)` |   
  
### getDescriptorForType()
    
    
    public Descriptors.Descriptor getDescriptorForType()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getDescriptorForType__)

### getEnableDebuggingInfo()
    
    
    public boolean getEnableDebuggingInfo()

If true, `StreamingDetectIntentResponse.debugging_info` will get populated.

`bool enable_debugging_info = 8;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enableDebuggingInfo.  
  
### getEnablePartialResponse()
    
    
    public boolean getEnablePartialResponse()

Enable partial detect intent response. If this flag is not enabled, response stream still contains only one final `DetectIntentResponse` even if some `Fulfillment`s in the agent have been configured to return partial responses.

`bool enable_partial_response = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enablePartialResponse.  
  
### getOutputAudioConfig()
    
    
    public OutputAudioConfig getOutputAudioConfig()

Instructs the speech synthesizer how to generate the output audio.

`.google.cloud.dialogflow.cx.v3.OutputAudioConfig output_audio_config = 4;`

**Returns**  
---  
**Type** | **Description**  
`[OutputAudioConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.OutputAudioConfig)` | The outputAudioConfig.  
  
### getOutputAudioConfigBuilder()
    
    
    public OutputAudioConfig.Builder getOutputAudioConfigBuilder()

Instructs the speech synthesizer how to generate the output audio.

`.google.cloud.dialogflow.cx.v3.OutputAudioConfig output_audio_config = 4;`

**Returns**  
---  
**Type** | **Description**  
`[OutputAudioConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.OutputAudioConfig.Builder)` |   
  
### getOutputAudioConfigOrBuilder()
    
    
    public OutputAudioConfigOrBuilder getOutputAudioConfigOrBuilder()

Instructs the speech synthesizer how to generate the output audio.

`.google.cloud.dialogflow.cx.v3.OutputAudioConfig output_audio_config = 4;`

**Returns**  
---  
**Type** | **Description**  
`[OutputAudioConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.OutputAudioConfigOrBuilder)` |   
  
### getQueryInput()
    
    
    public QueryInput getQueryInput()

Required. The input specification.

` .google.cloud.dialogflow.cx.v3.QueryInput query_input = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[QueryInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.QueryInput)` | The queryInput.  
  
### getQueryInputBuilder()
    
    
    public QueryInput.Builder getQueryInputBuilder()

Required. The input specification.

` .google.cloud.dialogflow.cx.v3.QueryInput query_input = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[QueryInput.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.QueryInput.Builder)` |   
  
### getQueryInputOrBuilder()
    
    
    public QueryInputOrBuilder getQueryInputOrBuilder()

Required. The input specification.

` .google.cloud.dialogflow.cx.v3.QueryInput query_input = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[QueryInputOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.QueryInputOrBuilder)` |   
  
### getQueryParams()
    
    
    public QueryParameters getQueryParams()

The parameters of this query.

`.google.cloud.dialogflow.cx.v3.QueryParameters query_params = 2;`

**Returns**  
---  
**Type** | **Description**  
`[QueryParameters](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.QueryParameters)` | The queryParams.  
  
### getQueryParamsBuilder()
    
    
    public QueryParameters.Builder getQueryParamsBuilder()

The parameters of this query.

`.google.cloud.dialogflow.cx.v3.QueryParameters query_params = 2;`

**Returns**  
---  
**Type** | **Description**  
`[QueryParameters.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.QueryParameters.Builder)` |   
  
### getQueryParamsOrBuilder()
    
    
    public QueryParametersOrBuilder getQueryParamsOrBuilder()

The parameters of this query.

`.google.cloud.dialogflow.cx.v3.QueryParameters query_params = 2;`

**Returns**  
---  
**Type** | **Description**  
`[QueryParametersOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.QueryParametersOrBuilder)` |   
  
### getResponseView()
    
    
    public DetectIntentResponseView getResponseView()

Optional. Specifies which fields in the QueryResult to return. If not set, the default is DETECT_INTENT_RESPONSE_VIEW_FULL.

` .google.cloud.dialogflow.cx.v3.DetectIntentResponseView response_view = 16 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[DetectIntentResponseView](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DetectIntentResponseView)` | The responseView.  
  
### getResponseViewValue()
    
    
    public int getResponseViewValue()

Optional. Specifies which fields in the QueryResult to return. If not set, the default is DETECT_INTENT_RESPONSE_VIEW_FULL.

` .google.cloud.dialogflow.cx.v3.DetectIntentResponseView response_view = 16 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for responseView.  
  
### getSession()
    
    
    public String getSession()

The name of the session this query is sent to. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/sessions/<SessionID>` or `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/environments/<EnvironmentID>/sessions/<SessionID>`. If `Environment ID` is not specified, we assume default 'draft' environment. It's up to the API caller to choose an appropriate `Session ID`. It can be a random number or some type of session identifiers (preferably hashed). The length of the `Session ID` must not exceed 36 characters. Note: session must be set in the first request.

For more information, see the [sessions guide](https://cloud.google.com/dialogflow/cx/docs/concept/session).

Note: Always use agent versions for production traffic. See [Versions and environments](https://cloud.google.com/dialogflow/cx/docs/concept/version).

`string session = 1 [(.google.api.resource_reference) = { ... }`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The session.  
  
### getSessionBytes()
    
    
    public ByteString getSessionBytes()

The name of the session this query is sent to. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/sessions/<SessionID>` or `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/environments/<EnvironmentID>/sessions/<SessionID>`. If `Environment ID` is not specified, we assume default 'draft' environment. It's up to the API caller to choose an appropriate `Session ID`. It can be a random number or some type of session identifiers (preferably hashed). The length of the `Session ID` must not exceed 36 characters. Note: session must be set in the first request.

For more information, see the [sessions guide](https://cloud.google.com/dialogflow/cx/docs/concept/session).

Note: Always use agent versions for production traffic. See [Versions and environments](https://cloud.google.com/dialogflow/cx/docs/concept/version).

`string session = 1 [(.google.api.resource_reference) = { ... }`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for session.  
  
### hasOutputAudioConfig()
    
    
    public boolean hasOutputAudioConfig()

Instructs the speech synthesizer how to generate the output audio.

`.google.cloud.dialogflow.cx.v3.OutputAudioConfig output_audio_config = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the outputAudioConfig field is set.  
  
### hasQueryInput()
    
    
    public boolean hasQueryInput()

Required. The input specification.

` .google.cloud.dialogflow.cx.v3.QueryInput query_input = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the queryInput field is set.  
  
### hasQueryParams()
    
    
    public boolean hasQueryParams()

The parameters of this query.

`.google.cloud.dialogflow.cx.v3.QueryParameters query_params = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the queryParams field is set.  
  
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

### mergeFrom(StreamingDetectIntentRequest other)
    
    
    public StreamingDetectIntentRequest.Builder mergeFrom(StreamingDetectIntentRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[StreamingDetectIntentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingDetectIntentRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StreamingDetectIntentRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingDetectIntentRequest.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public StreamingDetectIntentRequest.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StreamingDetectIntentRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingDetectIntentRequest.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public StreamingDetectIntentRequest.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StreamingDetectIntentRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingDetectIntentRequest.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### mergeOutputAudioConfig(OutputAudioConfig value)
    
    
    public StreamingDetectIntentRequest.Builder mergeOutputAudioConfig(OutputAudioConfig value)

Instructs the speech synthesizer how to generate the output audio.

`.google.cloud.dialogflow.cx.v3.OutputAudioConfig output_audio_config = 4;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[OutputAudioConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.OutputAudioConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StreamingDetectIntentRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingDetectIntentRequest.Builder)` |   
  
### mergeQueryInput(QueryInput value)
    
    
    public StreamingDetectIntentRequest.Builder mergeQueryInput(QueryInput value)

Required. The input specification.

` .google.cloud.dialogflow.cx.v3.QueryInput query_input = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[QueryInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.QueryInput)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StreamingDetectIntentRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingDetectIntentRequest.Builder)` |   
  
### mergeQueryParams(QueryParameters value)
    
    
    public StreamingDetectIntentRequest.Builder mergeQueryParams(QueryParameters value)

The parameters of this query.

`.google.cloud.dialogflow.cx.v3.QueryParameters query_params = 2;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[QueryParameters](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.QueryParameters)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StreamingDetectIntentRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingDetectIntentRequest.Builder)` |   
  
### setEnableDebuggingInfo(boolean value)
    
    
    public StreamingDetectIntentRequest.Builder setEnableDebuggingInfo(boolean value)

If true, `StreamingDetectIntentResponse.debugging_info` will get populated.

`bool enable_debugging_info = 8;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The enableDebuggingInfo to set.  
**Returns**  
---  
**Type** | **Description**  
`[StreamingDetectIntentRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingDetectIntentRequest.Builder)` | This builder for chaining.  
  
### setEnablePartialResponse(boolean value)
    
    
    public StreamingDetectIntentRequest.Builder setEnablePartialResponse(boolean value)

Enable partial detect intent response. If this flag is not enabled, response stream still contains only one final `DetectIntentResponse` even if some `Fulfillment`s in the agent have been configured to return partial responses.

`bool enable_partial_response = 5;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The enablePartialResponse to set.  
**Returns**  
---  
**Type** | **Description**  
`[StreamingDetectIntentRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingDetectIntentRequest.Builder)` | This builder for chaining.  
  
### setOutputAudioConfig(OutputAudioConfig value)
    
    
    public StreamingDetectIntentRequest.Builder setOutputAudioConfig(OutputAudioConfig value)

Instructs the speech synthesizer how to generate the output audio.

`.google.cloud.dialogflow.cx.v3.OutputAudioConfig output_audio_config = 4;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[OutputAudioConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.OutputAudioConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StreamingDetectIntentRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingDetectIntentRequest.Builder)` |   
  
### setOutputAudioConfig(OutputAudioConfig.Builder builderForValue)
    
    
    public StreamingDetectIntentRequest.Builder setOutputAudioConfig(OutputAudioConfig.Builder builderForValue)

Instructs the speech synthesizer how to generate the output audio.

`.google.cloud.dialogflow.cx.v3.OutputAudioConfig output_audio_config = 4;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[OutputAudioConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.OutputAudioConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StreamingDetectIntentRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingDetectIntentRequest.Builder)` |   
  
### setQueryInput(QueryInput value)
    
    
    public StreamingDetectIntentRequest.Builder setQueryInput(QueryInput value)

Required. The input specification.

` .google.cloud.dialogflow.cx.v3.QueryInput query_input = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[QueryInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.QueryInput)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StreamingDetectIntentRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingDetectIntentRequest.Builder)` |   
  
### setQueryInput(QueryInput.Builder builderForValue)
    
    
    public StreamingDetectIntentRequest.Builder setQueryInput(QueryInput.Builder builderForValue)

Required. The input specification.

` .google.cloud.dialogflow.cx.v3.QueryInput query_input = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[QueryInput.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.QueryInput.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StreamingDetectIntentRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingDetectIntentRequest.Builder)` |   
  
### setQueryParams(QueryParameters value)
    
    
    public StreamingDetectIntentRequest.Builder setQueryParams(QueryParameters value)

The parameters of this query.

`.google.cloud.dialogflow.cx.v3.QueryParameters query_params = 2;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[QueryParameters](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.QueryParameters)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StreamingDetectIntentRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingDetectIntentRequest.Builder)` |   
  
### setQueryParams(QueryParameters.Builder builderForValue)
    
    
    public StreamingDetectIntentRequest.Builder setQueryParams(QueryParameters.Builder builderForValue)

The parameters of this query.

`.google.cloud.dialogflow.cx.v3.QueryParameters query_params = 2;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[QueryParameters.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.QueryParameters.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StreamingDetectIntentRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingDetectIntentRequest.Builder)` |   
  
### setResponseView(DetectIntentResponseView value)
    
    
    public StreamingDetectIntentRequest.Builder setResponseView(DetectIntentResponseView value)

Optional. Specifies which fields in the QueryResult to return. If not set, the default is DETECT_INTENT_RESPONSE_VIEW_FULL.

` .google.cloud.dialogflow.cx.v3.DetectIntentResponseView response_view = 16 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[DetectIntentResponseView](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DetectIntentResponseView)`  
The responseView to set.  
**Returns**  
---  
**Type** | **Description**  
`[StreamingDetectIntentRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingDetectIntentRequest.Builder)` | This builder for chaining.  
  
### setResponseViewValue(int value)
    
    
    public StreamingDetectIntentRequest.Builder setResponseViewValue(int value)

Optional. Specifies which fields in the QueryResult to return. If not set, the default is DETECT_INTENT_RESPONSE_VIEW_FULL.

` .google.cloud.dialogflow.cx.v3.DetectIntentResponseView response_view = 16 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The enum numeric value on the wire for responseView to set.  
**Returns**  
---  
**Type** | **Description**  
`[StreamingDetectIntentRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingDetectIntentRequest.Builder)` | This builder for chaining.  
  
### setSession(String value)
    
    
    public StreamingDetectIntentRequest.Builder setSession(String value)

The name of the session this query is sent to. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/sessions/<SessionID>` or `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/environments/<EnvironmentID>/sessions/<SessionID>`. If `Environment ID` is not specified, we assume default 'draft' environment. It's up to the API caller to choose an appropriate `Session ID`. It can be a random number or some type of session identifiers (preferably hashed). The length of the `Session ID` must not exceed 36 characters. Note: session must be set in the first request.

For more information, see the [sessions guide](https://cloud.google.com/dialogflow/cx/docs/concept/session).

Note: Always use agent versions for production traffic. See [Versions and environments](https://cloud.google.com/dialogflow/cx/docs/concept/version).

`string session = 1 [(.google.api.resource_reference) = { ... }`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The session to set.  
**Returns**  
---  
**Type** | **Description**  
`[StreamingDetectIntentRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingDetectIntentRequest.Builder)` | This builder for chaining.  
  
### setSessionBytes(ByteString value)
    
    
    public StreamingDetectIntentRequest.Builder setSessionBytes(ByteString value)

The name of the session this query is sent to. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/sessions/<SessionID>` or `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/environments/<EnvironmentID>/sessions/<SessionID>`. If `Environment ID` is not specified, we assume default 'draft' environment. It's up to the API caller to choose an appropriate `Session ID`. It can be a random number or some type of session identifiers (preferably hashed). The length of the `Session ID` must not exceed 36 characters. Note: session must be set in the first request.

For more information, see the [sessions guide](https://cloud.google.com/dialogflow/cx/docs/concept/session).

Note: Always use agent versions for production traffic. See [Versions and environments](https://cloud.google.com/dialogflow/cx/docs/concept/version).

`string session = 1 [(.google.api.resource_reference) = { ... }`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for session to set.  
**Returns**  
---  
**Type** | **Description**  
`[StreamingDetectIntentRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingDetectIntentRequest.Builder)` | This builder for chaining.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
