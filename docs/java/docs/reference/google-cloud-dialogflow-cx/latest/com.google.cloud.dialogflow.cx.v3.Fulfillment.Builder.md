---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.Builder
title: Class Fulfillment.Builder (0.110.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:21:26.528203+00:00
---

# Class Fulfillment.Builder (0.110.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class Fulfillment.Builder (0.110.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.110.0 (latest)  0.106.0  0.105.0  0.104.0  0.102.0  0.99.0  0.98.0  0.96.0  0.94.0  0.93.0  0.92.0  0.91.0  0.89.0  0.87.0  0.86.0  0.85.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.75.0  0.74.0  0.73.0  0.71.0  0.70.0  0.69.0  0.68.0  0.67.0  0.66.0  0.65.0  0.64.0  0.63.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.7  0.13.1  0.12.1  0.11.5 
    
    
    public static final class Fulfillment.Builder extends GeneratedMessage.Builder<Fulfillment.Builder> implements FulfillmentOrBuilder

A fulfillment can do one or more of the following actions at the same time:

  * Generate rich message responses.
  * Set parameter values.
  * Call the webhook.

Fulfillments can be called at various stages in the Page or Form lifecycle. For example, when a DetectIntentRequest drives a session to enter a new page, the page's entry fulfillment can add a static response to the QueryResult in the returning DetectIntentResponse, call the webhook (for example, to load user data from a database), or both.




Protobuf type `google.cloud.dialogflow.cx.v3.Fulfillment`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > Fulfillment.Builder

## Implements

[FulfillmentOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.FulfillmentOrBuilder)

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

### addAllConditionalCases(Iterable<? extends Fulfillment.ConditionalCases> values)
    
    
    public Fulfillment.Builder addAllConditionalCases(Iterable<? extends Fulfillment.ConditionalCases> values)

Conditional cases for this fulfillment.

` repeated .google.cloud.dialogflow.cx.v3.Fulfillment.ConditionalCases conditional_cases = 5; `

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<? extends com.google.cloud.dialogflow.cx.v3.Fulfillment.ConditionalCases>`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.Builder)` |   
  
### addAllGenerators(Iterable<? extends Fulfillment.GeneratorSettings> values)
    
    
    public Fulfillment.Builder addAllGenerators(Iterable<? extends Fulfillment.GeneratorSettings> values)

A list of Generators to be called during this fulfillment.

`repeated .google.cloud.dialogflow.cx.v3.Fulfillment.GeneratorSettings generators = 13; `

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<? extends com.google.cloud.dialogflow.cx.v3.Fulfillment.GeneratorSettings>`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.Builder)` |   
  
### addAllMessages(Iterable<? extends ResponseMessage> values)
    
    
    public Fulfillment.Builder addAllMessages(Iterable<? extends ResponseMessage> values)

The list of rich message responses to present to the user.

`repeated .google.cloud.dialogflow.cx.v3.ResponseMessage messages = 1;`

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<? extends com.google.cloud.dialogflow.cx.v3.ResponseMessage>`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.Builder)` |   
  
### addAllSetParameterActions(Iterable<? extends Fulfillment.SetParameterAction> values)
    
    
    public Fulfillment.Builder addAllSetParameterActions(Iterable<? extends Fulfillment.SetParameterAction> values)

Set parameter values before executing the webhook.

` repeated .google.cloud.dialogflow.cx.v3.Fulfillment.SetParameterAction set_parameter_actions = 4; `

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<? extends com.google.cloud.dialogflow.cx.v3.Fulfillment.SetParameterAction>`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.Builder)` |   
  
### addConditionalCases(Fulfillment.ConditionalCases value)
    
    
    public Fulfillment.Builder addConditionalCases(Fulfillment.ConditionalCases value)

Conditional cases for this fulfillment.

` repeated .google.cloud.dialogflow.cx.v3.Fulfillment.ConditionalCases conditional_cases = 5; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Fulfillment.ConditionalCases](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.ConditionalCases)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.Builder)` |   
  
### addConditionalCases(Fulfillment.ConditionalCases.Builder builderForValue)
    
    
    public Fulfillment.Builder addConditionalCases(Fulfillment.ConditionalCases.Builder builderForValue)

Conditional cases for this fulfillment.

` repeated .google.cloud.dialogflow.cx.v3.Fulfillment.ConditionalCases conditional_cases = 5; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Fulfillment.ConditionalCases.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.ConditionalCases.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.Builder)` |   
  
### addConditionalCases(int index, Fulfillment.ConditionalCases value)
    
    
    public Fulfillment.Builder addConditionalCases(int index, Fulfillment.ConditionalCases value)

Conditional cases for this fulfillment.

` repeated .google.cloud.dialogflow.cx.v3.Fulfillment.ConditionalCases conditional_cases = 5; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[Fulfillment.ConditionalCases](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.ConditionalCases)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.Builder)` |   
  
### addConditionalCases(int index, Fulfillment.ConditionalCases.Builder builderForValue)
    
    
    public Fulfillment.Builder addConditionalCases(int index, Fulfillment.ConditionalCases.Builder builderForValue)

Conditional cases for this fulfillment.

` repeated .google.cloud.dialogflow.cx.v3.Fulfillment.ConditionalCases conditional_cases = 5; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[Fulfillment.ConditionalCases.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.ConditionalCases.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.Builder)` |   
  
### addConditionalCasesBuilder()
    
    
    public Fulfillment.ConditionalCases.Builder addConditionalCasesBuilder()

Conditional cases for this fulfillment.

` repeated .google.cloud.dialogflow.cx.v3.Fulfillment.ConditionalCases conditional_cases = 5; `

**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.ConditionalCases.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.ConditionalCases.Builder)` |   
  
### addConditionalCasesBuilder(int index)
    
    
    public Fulfillment.ConditionalCases.Builder addConditionalCasesBuilder(int index)

Conditional cases for this fulfillment.

` repeated .google.cloud.dialogflow.cx.v3.Fulfillment.ConditionalCases conditional_cases = 5; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.ConditionalCases.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.ConditionalCases.Builder)` |   
  
### addGenerators(Fulfillment.GeneratorSettings value)
    
    
    public Fulfillment.Builder addGenerators(Fulfillment.GeneratorSettings value)

A list of Generators to be called during this fulfillment.

`repeated .google.cloud.dialogflow.cx.v3.Fulfillment.GeneratorSettings generators = 13; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Fulfillment.GeneratorSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.GeneratorSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.Builder)` |   
  
### addGenerators(Fulfillment.GeneratorSettings.Builder builderForValue)
    
    
    public Fulfillment.Builder addGenerators(Fulfillment.GeneratorSettings.Builder builderForValue)

A list of Generators to be called during this fulfillment.

`repeated .google.cloud.dialogflow.cx.v3.Fulfillment.GeneratorSettings generators = 13; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Fulfillment.GeneratorSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.GeneratorSettings.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.Builder)` |   
  
### addGenerators(int index, Fulfillment.GeneratorSettings value)
    
    
    public Fulfillment.Builder addGenerators(int index, Fulfillment.GeneratorSettings value)

A list of Generators to be called during this fulfillment.

`repeated .google.cloud.dialogflow.cx.v3.Fulfillment.GeneratorSettings generators = 13; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[Fulfillment.GeneratorSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.GeneratorSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.Builder)` |   
  
### addGenerators(int index, Fulfillment.GeneratorSettings.Builder builderForValue)
    
    
    public Fulfillment.Builder addGenerators(int index, Fulfillment.GeneratorSettings.Builder builderForValue)

A list of Generators to be called during this fulfillment.

`repeated .google.cloud.dialogflow.cx.v3.Fulfillment.GeneratorSettings generators = 13; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[Fulfillment.GeneratorSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.GeneratorSettings.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.Builder)` |   
  
### addGeneratorsBuilder()
    
    
    public Fulfillment.GeneratorSettings.Builder addGeneratorsBuilder()

A list of Generators to be called during this fulfillment.

`repeated .google.cloud.dialogflow.cx.v3.Fulfillment.GeneratorSettings generators = 13; `

**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.GeneratorSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.GeneratorSettings.Builder)` |   
  
### addGeneratorsBuilder(int index)
    
    
    public Fulfillment.GeneratorSettings.Builder addGeneratorsBuilder(int index)

A list of Generators to be called during this fulfillment.

`repeated .google.cloud.dialogflow.cx.v3.Fulfillment.GeneratorSettings generators = 13; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.GeneratorSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.GeneratorSettings.Builder)` |   
  
### addMessages(ResponseMessage value)
    
    
    public Fulfillment.Builder addMessages(ResponseMessage value)

The list of rich message responses to present to the user.

`repeated .google.cloud.dialogflow.cx.v3.ResponseMessage messages = 1;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ResponseMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ResponseMessage)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.Builder)` |   
  
### addMessages(ResponseMessage.Builder builderForValue)
    
    
    public Fulfillment.Builder addMessages(ResponseMessage.Builder builderForValue)

The list of rich message responses to present to the user.

`repeated .google.cloud.dialogflow.cx.v3.ResponseMessage messages = 1;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[ResponseMessage.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ResponseMessage.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.Builder)` |   
  
### addMessages(int index, ResponseMessage value)
    
    
    public Fulfillment.Builder addMessages(int index, ResponseMessage value)

The list of rich message responses to present to the user.

`repeated .google.cloud.dialogflow.cx.v3.ResponseMessage messages = 1;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[ResponseMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ResponseMessage)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.Builder)` |   
  
### addMessages(int index, ResponseMessage.Builder builderForValue)
    
    
    public Fulfillment.Builder addMessages(int index, ResponseMessage.Builder builderForValue)

The list of rich message responses to present to the user.

`repeated .google.cloud.dialogflow.cx.v3.ResponseMessage messages = 1;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[ResponseMessage.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ResponseMessage.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.Builder)` |   
  
### addMessagesBuilder()
    
    
    public ResponseMessage.Builder addMessagesBuilder()

The list of rich message responses to present to the user.

`repeated .google.cloud.dialogflow.cx.v3.ResponseMessage messages = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ResponseMessage.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ResponseMessage.Builder)` |   
  
### addMessagesBuilder(int index)
    
    
    public ResponseMessage.Builder addMessagesBuilder(int index)

The list of rich message responses to present to the user.

`repeated .google.cloud.dialogflow.cx.v3.ResponseMessage messages = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ResponseMessage.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ResponseMessage.Builder)` |   
  
### addSetParameterActions(Fulfillment.SetParameterAction value)
    
    
    public Fulfillment.Builder addSetParameterActions(Fulfillment.SetParameterAction value)

Set parameter values before executing the webhook.

` repeated .google.cloud.dialogflow.cx.v3.Fulfillment.SetParameterAction set_parameter_actions = 4; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Fulfillment.SetParameterAction](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.SetParameterAction)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.Builder)` |   
  
### addSetParameterActions(Fulfillment.SetParameterAction.Builder builderForValue)
    
    
    public Fulfillment.Builder addSetParameterActions(Fulfillment.SetParameterAction.Builder builderForValue)

Set parameter values before executing the webhook.

` repeated .google.cloud.dialogflow.cx.v3.Fulfillment.SetParameterAction set_parameter_actions = 4; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Fulfillment.SetParameterAction.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.SetParameterAction.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.Builder)` |   
  
### addSetParameterActions(int index, Fulfillment.SetParameterAction value)
    
    
    public Fulfillment.Builder addSetParameterActions(int index, Fulfillment.SetParameterAction value)

Set parameter values before executing the webhook.

` repeated .google.cloud.dialogflow.cx.v3.Fulfillment.SetParameterAction set_parameter_actions = 4; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[Fulfillment.SetParameterAction](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.SetParameterAction)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.Builder)` |   
  
### addSetParameterActions(int index, Fulfillment.SetParameterAction.Builder builderForValue)
    
    
    public Fulfillment.Builder addSetParameterActions(int index, Fulfillment.SetParameterAction.Builder builderForValue)

Set parameter values before executing the webhook.

` repeated .google.cloud.dialogflow.cx.v3.Fulfillment.SetParameterAction set_parameter_actions = 4; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[Fulfillment.SetParameterAction.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.SetParameterAction.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.Builder)` |   
  
### addSetParameterActionsBuilder()
    
    
    public Fulfillment.SetParameterAction.Builder addSetParameterActionsBuilder()

Set parameter values before executing the webhook.

` repeated .google.cloud.dialogflow.cx.v3.Fulfillment.SetParameterAction set_parameter_actions = 4; `

**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.SetParameterAction.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.SetParameterAction.Builder)` |   
  
### addSetParameterActionsBuilder(int index)
    
    
    public Fulfillment.SetParameterAction.Builder addSetParameterActionsBuilder(int index)

Set parameter values before executing the webhook.

` repeated .google.cloud.dialogflow.cx.v3.Fulfillment.SetParameterAction set_parameter_actions = 4; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.SetParameterAction.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.SetParameterAction.Builder)` |   
  
### build()
    
    
    public Fulfillment build()

**Returns**  
---  
**Type** | **Description**  
`[Fulfillment](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment)` |   
  
### buildPartial()
    
    
    public Fulfillment buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[Fulfillment](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment)` |   
  
### clear()
    
    
    public Fulfillment.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearAdvancedSettings()
    
    
    public Fulfillment.Builder clearAdvancedSettings()

Hierarchical advanced settings for this fulfillment. The settings exposed at the lower level overrides the settings exposed at the higher level.

`.google.cloud.dialogflow.cx.v3.AdvancedSettings advanced_settings = 7;`

**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.Builder)` |   
  
### clearConditionalCases()
    
    
    public Fulfillment.Builder clearConditionalCases()

Conditional cases for this fulfillment.

` repeated .google.cloud.dialogflow.cx.v3.Fulfillment.ConditionalCases conditional_cases = 5; `

**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.Builder)` |   
  
### clearEnableGenerativeFallback()
    
    
    public Fulfillment.Builder clearEnableGenerativeFallback()

If the flag is true, the agent will utilize LLM to generate a text response. If LLM generation fails, the defined responses in the fulfillment will be respected. This flag is only useful for fulfillments associated with no-match event handlers.

`bool enable_generative_fallback = 12;`

**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.Builder)` | This builder for chaining.  
  
### clearGenerators()
    
    
    public Fulfillment.Builder clearGenerators()

A list of Generators to be called during this fulfillment.

`repeated .google.cloud.dialogflow.cx.v3.Fulfillment.GeneratorSettings generators = 13; `

**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.Builder)` |   
  
### clearMessages()
    
    
    public Fulfillment.Builder clearMessages()

The list of rich message responses to present to the user.

`repeated .google.cloud.dialogflow.cx.v3.ResponseMessage messages = 1;`

**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.Builder)` |   
  
### clearReturnPartialResponses()
    
    
    public Fulfillment.Builder clearReturnPartialResponses()

Whether Dialogflow should return currently queued fulfillment response messages in streaming APIs. If a webhook is specified, it happens before Dialogflow invokes webhook. Warning: 1) This flag only affects streaming API. Responses are still queued and returned once in non-streaming API. 2) The flag can be enabled in any fulfillment but only the first 3 partial responses will be returned. You may only want to apply it to fulfillments that have slow webhooks.

`bool return_partial_responses = 8;`

**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.Builder)` | This builder for chaining.  
  
### clearSetParameterActions()
    
    
    public Fulfillment.Builder clearSetParameterActions()

Set parameter values before executing the webhook.

` repeated .google.cloud.dialogflow.cx.v3.Fulfillment.SetParameterAction set_parameter_actions = 4; `

**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.Builder)` |   
  
### clearTag()
    
    
    public Fulfillment.Builder clearTag()

The value of this field will be populated in the WebhookRequest `fulfillmentInfo.tag` field by Dialogflow when the associated webhook is called. The tag is typically used by the webhook service to identify which fulfillment is being called, but it could be used for other purposes. This field is required if `webhook` is specified.

`string tag = 3;`

**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.Builder)` | This builder for chaining.  
  
### clearWebhook()
    
    
    public Fulfillment.Builder clearWebhook()

The webhook to call. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/webhooks/<WebhookID>`.

`string webhook = 2 [(.google.api.resource_reference) = { ... }`

**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.Builder)` | This builder for chaining.  
  
### getAdvancedSettings()
    
    
    public AdvancedSettings getAdvancedSettings()

Hierarchical advanced settings for this fulfillment. The settings exposed at the lower level overrides the settings exposed at the higher level.

`.google.cloud.dialogflow.cx.v3.AdvancedSettings advanced_settings = 7;`

**Returns**  
---  
**Type** | **Description**  
`[AdvancedSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AdvancedSettings)` | The advancedSettings.  
  
### getAdvancedSettingsBuilder()
    
    
    public AdvancedSettings.Builder getAdvancedSettingsBuilder()

Hierarchical advanced settings for this fulfillment. The settings exposed at the lower level overrides the settings exposed at the higher level.

`.google.cloud.dialogflow.cx.v3.AdvancedSettings advanced_settings = 7;`

**Returns**  
---  
**Type** | **Description**  
`[AdvancedSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AdvancedSettings.Builder)` |   
  
### getAdvancedSettingsOrBuilder()
    
    
    public AdvancedSettingsOrBuilder getAdvancedSettingsOrBuilder()

Hierarchical advanced settings for this fulfillment. The settings exposed at the lower level overrides the settings exposed at the higher level.

`.google.cloud.dialogflow.cx.v3.AdvancedSettings advanced_settings = 7;`

**Returns**  
---  
**Type** | **Description**  
`[AdvancedSettingsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AdvancedSettingsOrBuilder)` |   
  
### getConditionalCases(int index)
    
    
    public Fulfillment.ConditionalCases getConditionalCases(int index)

Conditional cases for this fulfillment.

` repeated .google.cloud.dialogflow.cx.v3.Fulfillment.ConditionalCases conditional_cases = 5; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.ConditionalCases](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.ConditionalCases)` |   
  
### getConditionalCasesBuilder(int index)
    
    
    public Fulfillment.ConditionalCases.Builder getConditionalCasesBuilder(int index)

Conditional cases for this fulfillment.

` repeated .google.cloud.dialogflow.cx.v3.Fulfillment.ConditionalCases conditional_cases = 5; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.ConditionalCases.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.ConditionalCases.Builder)` |   
  
### getConditionalCasesBuilderList()
    
    
    public List<Fulfillment.ConditionalCases.Builder> getConditionalCasesBuilderList()

Conditional cases for this fulfillment.

` repeated .google.cloud.dialogflow.cx.v3.Fulfillment.ConditionalCases conditional_cases = 5; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.ConditionalCases.Builder)>` |   
  
### getConditionalCasesCount()
    
    
    public int getConditionalCasesCount()

Conditional cases for this fulfillment.

` repeated .google.cloud.dialogflow.cx.v3.Fulfillment.ConditionalCases conditional_cases = 5; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getConditionalCasesList()
    
    
    public List<Fulfillment.ConditionalCases> getConditionalCasesList()

Conditional cases for this fulfillment.

` repeated .google.cloud.dialogflow.cx.v3.Fulfillment.ConditionalCases conditional_cases = 5; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ConditionalCases](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.ConditionalCases)>` |   
  
### getConditionalCasesOrBuilder(int index)
    
    
    public Fulfillment.ConditionalCasesOrBuilder getConditionalCasesOrBuilder(int index)

Conditional cases for this fulfillment.

` repeated .google.cloud.dialogflow.cx.v3.Fulfillment.ConditionalCases conditional_cases = 5; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.ConditionalCasesOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.ConditionalCasesOrBuilder)` |   
  
### getConditionalCasesOrBuilderList()
    
    
    public List<? extends Fulfillment.ConditionalCasesOrBuilder> getConditionalCasesOrBuilderList()

Conditional cases for this fulfillment.

` repeated .google.cloud.dialogflow.cx.v3.Fulfillment.ConditionalCases conditional_cases = 5; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.dialogflow.cx.v3.Fulfillment.ConditionalCasesOrBuilder>` |   
  
### getDefaultInstanceForType()
    
    
    public Fulfillment getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[Fulfillment](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment)` |   
  
### getDescriptorForType()
    
    
    public Descriptors.Descriptor getDescriptorForType()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getDescriptorForType__)

### getEnableGenerativeFallback()
    
    
    public boolean getEnableGenerativeFallback()

If the flag is true, the agent will utilize LLM to generate a text response. If LLM generation fails, the defined responses in the fulfillment will be respected. This flag is only useful for fulfillments associated with no-match event handlers.

`bool enable_generative_fallback = 12;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enableGenerativeFallback.  
  
### getGenerators(int index)
    
    
    public Fulfillment.GeneratorSettings getGenerators(int index)

A list of Generators to be called during this fulfillment.

`repeated .google.cloud.dialogflow.cx.v3.Fulfillment.GeneratorSettings generators = 13; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.GeneratorSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.GeneratorSettings)` |   
  
### getGeneratorsBuilder(int index)
    
    
    public Fulfillment.GeneratorSettings.Builder getGeneratorsBuilder(int index)

A list of Generators to be called during this fulfillment.

`repeated .google.cloud.dialogflow.cx.v3.Fulfillment.GeneratorSettings generators = 13; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.GeneratorSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.GeneratorSettings.Builder)` |   
  
### getGeneratorsBuilderList()
    
    
    public List<Fulfillment.GeneratorSettings.Builder> getGeneratorsBuilderList()

A list of Generators to be called during this fulfillment.

`repeated .google.cloud.dialogflow.cx.v3.Fulfillment.GeneratorSettings generators = 13; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.GeneratorSettings.Builder)>` |   
  
### getGeneratorsCount()
    
    
    public int getGeneratorsCount()

A list of Generators to be called during this fulfillment.

`repeated .google.cloud.dialogflow.cx.v3.Fulfillment.GeneratorSettings generators = 13; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getGeneratorsList()
    
    
    public List<Fulfillment.GeneratorSettings> getGeneratorsList()

A list of Generators to be called during this fulfillment.

`repeated .google.cloud.dialogflow.cx.v3.Fulfillment.GeneratorSettings generators = 13; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[GeneratorSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.GeneratorSettings)>` |   
  
### getGeneratorsOrBuilder(int index)
    
    
    public Fulfillment.GeneratorSettingsOrBuilder getGeneratorsOrBuilder(int index)

A list of Generators to be called during this fulfillment.

`repeated .google.cloud.dialogflow.cx.v3.Fulfillment.GeneratorSettings generators = 13; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.GeneratorSettingsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.GeneratorSettingsOrBuilder)` |   
  
### getGeneratorsOrBuilderList()
    
    
    public List<? extends Fulfillment.GeneratorSettingsOrBuilder> getGeneratorsOrBuilderList()

A list of Generators to be called during this fulfillment.

`repeated .google.cloud.dialogflow.cx.v3.Fulfillment.GeneratorSettings generators = 13; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.dialogflow.cx.v3.Fulfillment.GeneratorSettingsOrBuilder>` |   
  
### getMessages(int index)
    
    
    public ResponseMessage getMessages(int index)

The list of rich message responses to present to the user.

`repeated .google.cloud.dialogflow.cx.v3.ResponseMessage messages = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ResponseMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ResponseMessage)` |   
  
### getMessagesBuilder(int index)
    
    
    public ResponseMessage.Builder getMessagesBuilder(int index)

The list of rich message responses to present to the user.

`repeated .google.cloud.dialogflow.cx.v3.ResponseMessage messages = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ResponseMessage.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ResponseMessage.Builder)` |   
  
### getMessagesBuilderList()
    
    
    public List<ResponseMessage.Builder> getMessagesBuilderList()

The list of rich message responses to present to the user.

`repeated .google.cloud.dialogflow.cx.v3.ResponseMessage messages = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ResponseMessage.Builder)>` |   
  
### getMessagesCount()
    
    
    public int getMessagesCount()

The list of rich message responses to present to the user.

`repeated .google.cloud.dialogflow.cx.v3.ResponseMessage messages = 1;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getMessagesList()
    
    
    public List<ResponseMessage> getMessagesList()

The list of rich message responses to present to the user.

`repeated .google.cloud.dialogflow.cx.v3.ResponseMessage messages = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ResponseMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ResponseMessage)>` |   
  
### getMessagesOrBuilder(int index)
    
    
    public ResponseMessageOrBuilder getMessagesOrBuilder(int index)

The list of rich message responses to present to the user.

`repeated .google.cloud.dialogflow.cx.v3.ResponseMessage messages = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ResponseMessageOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ResponseMessageOrBuilder)` |   
  
### getMessagesOrBuilderList()
    
    
    public List<? extends ResponseMessageOrBuilder> getMessagesOrBuilderList()

The list of rich message responses to present to the user.

`repeated .google.cloud.dialogflow.cx.v3.ResponseMessage messages = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.dialogflow.cx.v3.ResponseMessageOrBuilder>` |   
  
### getReturnPartialResponses()
    
    
    public boolean getReturnPartialResponses()

Whether Dialogflow should return currently queued fulfillment response messages in streaming APIs. If a webhook is specified, it happens before Dialogflow invokes webhook. Warning: 1) This flag only affects streaming API. Responses are still queued and returned once in non-streaming API. 2) The flag can be enabled in any fulfillment but only the first 3 partial responses will be returned. You may only want to apply it to fulfillments that have slow webhooks.

`bool return_partial_responses = 8;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The returnPartialResponses.  
  
### getSetParameterActions(int index)
    
    
    public Fulfillment.SetParameterAction getSetParameterActions(int index)

Set parameter values before executing the webhook.

` repeated .google.cloud.dialogflow.cx.v3.Fulfillment.SetParameterAction set_parameter_actions = 4; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.SetParameterAction](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.SetParameterAction)` |   
  
### getSetParameterActionsBuilder(int index)
    
    
    public Fulfillment.SetParameterAction.Builder getSetParameterActionsBuilder(int index)

Set parameter values before executing the webhook.

` repeated .google.cloud.dialogflow.cx.v3.Fulfillment.SetParameterAction set_parameter_actions = 4; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.SetParameterAction.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.SetParameterAction.Builder)` |   
  
### getSetParameterActionsBuilderList()
    
    
    public List<Fulfillment.SetParameterAction.Builder> getSetParameterActionsBuilderList()

Set parameter values before executing the webhook.

` repeated .google.cloud.dialogflow.cx.v3.Fulfillment.SetParameterAction set_parameter_actions = 4; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.SetParameterAction.Builder)>` |   
  
### getSetParameterActionsCount()
    
    
    public int getSetParameterActionsCount()

Set parameter values before executing the webhook.

` repeated .google.cloud.dialogflow.cx.v3.Fulfillment.SetParameterAction set_parameter_actions = 4; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getSetParameterActionsList()
    
    
    public List<Fulfillment.SetParameterAction> getSetParameterActionsList()

Set parameter values before executing the webhook.

` repeated .google.cloud.dialogflow.cx.v3.Fulfillment.SetParameterAction set_parameter_actions = 4; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[SetParameterAction](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.SetParameterAction)>` |   
  
### getSetParameterActionsOrBuilder(int index)
    
    
    public Fulfillment.SetParameterActionOrBuilder getSetParameterActionsOrBuilder(int index)

Set parameter values before executing the webhook.

` repeated .google.cloud.dialogflow.cx.v3.Fulfillment.SetParameterAction set_parameter_actions = 4; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.SetParameterActionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.SetParameterActionOrBuilder)` |   
  
### getSetParameterActionsOrBuilderList()
    
    
    public List<? extends Fulfillment.SetParameterActionOrBuilder> getSetParameterActionsOrBuilderList()

Set parameter values before executing the webhook.

` repeated .google.cloud.dialogflow.cx.v3.Fulfillment.SetParameterAction set_parameter_actions = 4; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.dialogflow.cx.v3.Fulfillment.SetParameterActionOrBuilder>` |   
  
### getTag()
    
    
    public String getTag()

The value of this field will be populated in the WebhookRequest `fulfillmentInfo.tag` field by Dialogflow when the associated webhook is called. The tag is typically used by the webhook service to identify which fulfillment is being called, but it could be used for other purposes. This field is required if `webhook` is specified.

`string tag = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The tag.  
  
### getTagBytes()
    
    
    public ByteString getTagBytes()

The value of this field will be populated in the WebhookRequest `fulfillmentInfo.tag` field by Dialogflow when the associated webhook is called. The tag is typically used by the webhook service to identify which fulfillment is being called, but it could be used for other purposes. This field is required if `webhook` is specified.

`string tag = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for tag.  
  
### getWebhook()
    
    
    public String getWebhook()

The webhook to call. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/webhooks/<WebhookID>`.

`string webhook = 2 [(.google.api.resource_reference) = { ... }`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The webhook.  
  
### getWebhookBytes()
    
    
    public ByteString getWebhookBytes()

The webhook to call. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/webhooks/<WebhookID>`.

`string webhook = 2 [(.google.api.resource_reference) = { ... }`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for webhook.  
  
### hasAdvancedSettings()
    
    
    public boolean hasAdvancedSettings()

Hierarchical advanced settings for this fulfillment. The settings exposed at the lower level overrides the settings exposed at the higher level.

`.google.cloud.dialogflow.cx.v3.AdvancedSettings advanced_settings = 7;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the advancedSettings field is set.  
  
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

### mergeAdvancedSettings(AdvancedSettings value)
    
    
    public Fulfillment.Builder mergeAdvancedSettings(AdvancedSettings value)

Hierarchical advanced settings for this fulfillment. The settings exposed at the lower level overrides the settings exposed at the higher level.

`.google.cloud.dialogflow.cx.v3.AdvancedSettings advanced_settings = 7;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[AdvancedSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AdvancedSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.Builder)` |   
  
### mergeFrom(Fulfillment other)
    
    
    public Fulfillment.Builder mergeFrom(Fulfillment other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Fulfillment](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public Fulfillment.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public Fulfillment.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### removeConditionalCases(int index)
    
    
    public Fulfillment.Builder removeConditionalCases(int index)

Conditional cases for this fulfillment.

` repeated .google.cloud.dialogflow.cx.v3.Fulfillment.ConditionalCases conditional_cases = 5; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.Builder)` |   
  
### removeGenerators(int index)
    
    
    public Fulfillment.Builder removeGenerators(int index)

A list of Generators to be called during this fulfillment.

`repeated .google.cloud.dialogflow.cx.v3.Fulfillment.GeneratorSettings generators = 13; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.Builder)` |   
  
### removeMessages(int index)
    
    
    public Fulfillment.Builder removeMessages(int index)

The list of rich message responses to present to the user.

`repeated .google.cloud.dialogflow.cx.v3.ResponseMessage messages = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.Builder)` |   
  
### removeSetParameterActions(int index)
    
    
    public Fulfillment.Builder removeSetParameterActions(int index)

Set parameter values before executing the webhook.

` repeated .google.cloud.dialogflow.cx.v3.Fulfillment.SetParameterAction set_parameter_actions = 4; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.Builder)` |   
  
### setAdvancedSettings(AdvancedSettings value)
    
    
    public Fulfillment.Builder setAdvancedSettings(AdvancedSettings value)

Hierarchical advanced settings for this fulfillment. The settings exposed at the lower level overrides the settings exposed at the higher level.

`.google.cloud.dialogflow.cx.v3.AdvancedSettings advanced_settings = 7;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[AdvancedSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AdvancedSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.Builder)` |   
  
### setAdvancedSettings(AdvancedSettings.Builder builderForValue)
    
    
    public Fulfillment.Builder setAdvancedSettings(AdvancedSettings.Builder builderForValue)

Hierarchical advanced settings for this fulfillment. The settings exposed at the lower level overrides the settings exposed at the higher level.

`.google.cloud.dialogflow.cx.v3.AdvancedSettings advanced_settings = 7;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[AdvancedSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AdvancedSettings.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.Builder)` |   
  
### setConditionalCases(int index, Fulfillment.ConditionalCases value)
    
    
    public Fulfillment.Builder setConditionalCases(int index, Fulfillment.ConditionalCases value)

Conditional cases for this fulfillment.

` repeated .google.cloud.dialogflow.cx.v3.Fulfillment.ConditionalCases conditional_cases = 5; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[Fulfillment.ConditionalCases](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.ConditionalCases)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.Builder)` |   
  
### setConditionalCases(int index, Fulfillment.ConditionalCases.Builder builderForValue)
    
    
    public Fulfillment.Builder setConditionalCases(int index, Fulfillment.ConditionalCases.Builder builderForValue)

Conditional cases for this fulfillment.

` repeated .google.cloud.dialogflow.cx.v3.Fulfillment.ConditionalCases conditional_cases = 5; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[Fulfillment.ConditionalCases.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.ConditionalCases.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.Builder)` |   
  
### setEnableGenerativeFallback(boolean value)
    
    
    public Fulfillment.Builder setEnableGenerativeFallback(boolean value)

If the flag is true, the agent will utilize LLM to generate a text response. If LLM generation fails, the defined responses in the fulfillment will be respected. This flag is only useful for fulfillments associated with no-match event handlers.

`bool enable_generative_fallback = 12;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The enableGenerativeFallback to set.  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.Builder)` | This builder for chaining.  
  
### setGenerators(int index, Fulfillment.GeneratorSettings value)
    
    
    public Fulfillment.Builder setGenerators(int index, Fulfillment.GeneratorSettings value)

A list of Generators to be called during this fulfillment.

`repeated .google.cloud.dialogflow.cx.v3.Fulfillment.GeneratorSettings generators = 13; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[Fulfillment.GeneratorSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.GeneratorSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.Builder)` |   
  
### setGenerators(int index, Fulfillment.GeneratorSettings.Builder builderForValue)
    
    
    public Fulfillment.Builder setGenerators(int index, Fulfillment.GeneratorSettings.Builder builderForValue)

A list of Generators to be called during this fulfillment.

`repeated .google.cloud.dialogflow.cx.v3.Fulfillment.GeneratorSettings generators = 13; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[Fulfillment.GeneratorSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.GeneratorSettings.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.Builder)` |   
  
### setMessages(int index, ResponseMessage value)
    
    
    public Fulfillment.Builder setMessages(int index, ResponseMessage value)

The list of rich message responses to present to the user.

`repeated .google.cloud.dialogflow.cx.v3.ResponseMessage messages = 1;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[ResponseMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ResponseMessage)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.Builder)` |   
  
### setMessages(int index, ResponseMessage.Builder builderForValue)
    
    
    public Fulfillment.Builder setMessages(int index, ResponseMessage.Builder builderForValue)

The list of rich message responses to present to the user.

`repeated .google.cloud.dialogflow.cx.v3.ResponseMessage messages = 1;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[ResponseMessage.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ResponseMessage.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.Builder)` |   
  
### setReturnPartialResponses(boolean value)
    
    
    public Fulfillment.Builder setReturnPartialResponses(boolean value)

Whether Dialogflow should return currently queued fulfillment response messages in streaming APIs. If a webhook is specified, it happens before Dialogflow invokes webhook. Warning: 1) This flag only affects streaming API. Responses are still queued and returned once in non-streaming API. 2) The flag can be enabled in any fulfillment but only the first 3 partial responses will be returned. You may only want to apply it to fulfillments that have slow webhooks.

`bool return_partial_responses = 8;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The returnPartialResponses to set.  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.Builder)` | This builder for chaining.  
  
### setSetParameterActions(int index, Fulfillment.SetParameterAction value)
    
    
    public Fulfillment.Builder setSetParameterActions(int index, Fulfillment.SetParameterAction value)

Set parameter values before executing the webhook.

` repeated .google.cloud.dialogflow.cx.v3.Fulfillment.SetParameterAction set_parameter_actions = 4; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[Fulfillment.SetParameterAction](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.SetParameterAction)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.Builder)` |   
  
### setSetParameterActions(int index, Fulfillment.SetParameterAction.Builder builderForValue)
    
    
    public Fulfillment.Builder setSetParameterActions(int index, Fulfillment.SetParameterAction.Builder builderForValue)

Set parameter values before executing the webhook.

` repeated .google.cloud.dialogflow.cx.v3.Fulfillment.SetParameterAction set_parameter_actions = 4; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[Fulfillment.SetParameterAction.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.SetParameterAction.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.Builder)` |   
  
### setTag(String value)
    
    
    public Fulfillment.Builder setTag(String value)

The value of this field will be populated in the WebhookRequest `fulfillmentInfo.tag` field by Dialogflow when the associated webhook is called. The tag is typically used by the webhook service to identify which fulfillment is being called, but it could be used for other purposes. This field is required if `webhook` is specified.

`string tag = 3;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The tag to set.  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.Builder)` | This builder for chaining.  
  
### setTagBytes(ByteString value)
    
    
    public Fulfillment.Builder setTagBytes(ByteString value)

The value of this field will be populated in the WebhookRequest `fulfillmentInfo.tag` field by Dialogflow when the associated webhook is called. The tag is typically used by the webhook service to identify which fulfillment is being called, but it could be used for other purposes. This field is required if `webhook` is specified.

`string tag = 3;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for tag to set.  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.Builder)` | This builder for chaining.  
  
### setWebhook(String value)
    
    
    public Fulfillment.Builder setWebhook(String value)

The webhook to call. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/webhooks/<WebhookID>`.

`string webhook = 2 [(.google.api.resource_reference) = { ... }`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The webhook to set.  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.Builder)` | This builder for chaining.  
  
### setWebhookBytes(ByteString value)
    
    
    public Fulfillment.Builder setWebhookBytes(ByteString value)

The webhook to call. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/webhooks/<WebhookID>`.

`string webhook = 2 [(.google.api.resource_reference) = { ... }`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for webhook to set.  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment.Builder)` | This builder for chaining.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
