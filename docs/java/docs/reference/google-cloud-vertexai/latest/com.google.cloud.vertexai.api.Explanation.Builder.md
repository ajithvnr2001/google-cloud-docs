---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Explanation.Builder
title: Class Explanation.Builder (1.48.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:15:40.088129+00:00
---

# Class Explanation.Builder (1.48.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Explanation.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class Explanation.Builder (1.48.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.48.0 (latest)  1.47.0  1.45.0  1.43.0  1.42.0  1.40.0  1.38.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.30.0  1.28.0  1.27.0  1.24.0  1.23.0  1.22.0  1.20.1  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.8.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static final class Explanation.Builder extends GeneratedMessage.Builder<Explanation.Builder> implements ExplanationOrBuilder

Explanation of a prediction (provided in PredictResponse.predictions) produced by the Model on a given instance.

Protobuf type `google.cloud.vertexai.v1.Explanation`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > Explanation.Builder

## Implements

[ExplanationOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.ExplanationOrBuilder)

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

### addAllAttributions(Iterable<? extends Attribution> values)
    
    
    public Explanation.Builder addAllAttributions(Iterable<? extends Attribution> values)

Output only. Feature attributions grouped by predicted outputs.

For Models that predict only one output, such as regression Models that predict only one score, there is only one attibution that explains the predicted output. For Models that predict multiple outputs, such as multiclass Models that predict multiple classes, each element explains one specific item. Attribution.output_index can be used to identify which output this attribution is explaining.

By default, we provide Shapley values for the predicted class. However, you can configure the explanation request to generate Shapley values for any other classes too. For example, if a model predicts a probability of `0.4` for approving a loan application, the model's decision is to reject the application since `p(reject) = 0.6 > p(approve) = 0.4`, and the default Shapley values would be computed for rejection decision and not approval, even though the latter might be the positive class.

If users set ExplanationParameters.top_k, the attributions are sorted by instance_output_value in descending order. If ExplanationParameters.output_indices is specified, the attributions are stored by Attribution.output_index in the same order as they appear in the output_indices.

` repeated .google.cloud.vertexai.v1.Attribution attributions = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<? extends com.google.cloud.vertexai.api.Attribution>`  
  
**Returns**  
---  
**Type** | **Description**  
`[Explanation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Explanation.Builder)` |   
  
### addAllNeighbors(Iterable<? extends Neighbor> values)
    
    
    public Explanation.Builder addAllNeighbors(Iterable<? extends Neighbor> values)

Output only. List of the nearest neighbors for example-based explanations.

For models deployed with the examples explanations feature enabled, the attributions field is empty and instead the neighbors field is populated.

` repeated .google.cloud.vertexai.v1.Neighbor neighbors = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<? extends com.google.cloud.vertexai.api.Neighbor>`  
  
**Returns**  
---  
**Type** | **Description**  
`[Explanation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Explanation.Builder)` |   
  
### addAttributions(Attribution value)
    
    
    public Explanation.Builder addAttributions(Attribution value)

Output only. Feature attributions grouped by predicted outputs.

For Models that predict only one output, such as regression Models that predict only one score, there is only one attibution that explains the predicted output. For Models that predict multiple outputs, such as multiclass Models that predict multiple classes, each element explains one specific item. Attribution.output_index can be used to identify which output this attribution is explaining.

By default, we provide Shapley values for the predicted class. However, you can configure the explanation request to generate Shapley values for any other classes too. For example, if a model predicts a probability of `0.4` for approving a loan application, the model's decision is to reject the application since `p(reject) = 0.6 > p(approve) = 0.4`, and the default Shapley values would be computed for rejection decision and not approval, even though the latter might be the positive class.

If users set ExplanationParameters.top_k, the attributions are sorted by instance_output_value in descending order. If ExplanationParameters.output_indices is specified, the attributions are stored by Attribution.output_index in the same order as they appear in the output_indices.

` repeated .google.cloud.vertexai.v1.Attribution attributions = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Attribution](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Attribution)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Explanation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Explanation.Builder)` |   
  
### addAttributions(Attribution.Builder builderForValue)
    
    
    public Explanation.Builder addAttributions(Attribution.Builder builderForValue)

Output only. Feature attributions grouped by predicted outputs.

For Models that predict only one output, such as regression Models that predict only one score, there is only one attibution that explains the predicted output. For Models that predict multiple outputs, such as multiclass Models that predict multiple classes, each element explains one specific item. Attribution.output_index can be used to identify which output this attribution is explaining.

By default, we provide Shapley values for the predicted class. However, you can configure the explanation request to generate Shapley values for any other classes too. For example, if a model predicts a probability of `0.4` for approving a loan application, the model's decision is to reject the application since `p(reject) = 0.6 > p(approve) = 0.4`, and the default Shapley values would be computed for rejection decision and not approval, even though the latter might be the positive class.

If users set ExplanationParameters.top_k, the attributions are sorted by instance_output_value in descending order. If ExplanationParameters.output_indices is specified, the attributions are stored by Attribution.output_index in the same order as they appear in the output_indices.

` repeated .google.cloud.vertexai.v1.Attribution attributions = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Attribution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Attribution.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Explanation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Explanation.Builder)` |   
  
### addAttributions(int index, Attribution value)
    
    
    public Explanation.Builder addAttributions(int index, Attribution value)

Output only. Feature attributions grouped by predicted outputs.

For Models that predict only one output, such as regression Models that predict only one score, there is only one attibution that explains the predicted output. For Models that predict multiple outputs, such as multiclass Models that predict multiple classes, each element explains one specific item. Attribution.output_index can be used to identify which output this attribution is explaining.

By default, we provide Shapley values for the predicted class. However, you can configure the explanation request to generate Shapley values for any other classes too. For example, if a model predicts a probability of `0.4` for approving a loan application, the model's decision is to reject the application since `p(reject) = 0.6 > p(approve) = 0.4`, and the default Shapley values would be computed for rejection decision and not approval, even though the latter might be the positive class.

If users set ExplanationParameters.top_k, the attributions are sorted by instance_output_value in descending order. If ExplanationParameters.output_indices is specified, the attributions are stored by Attribution.output_index in the same order as they appear in the output_indices.

` repeated .google.cloud.vertexai.v1.Attribution attributions = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[Attribution](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Attribution)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Explanation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Explanation.Builder)` |   
  
### addAttributions(int index, Attribution.Builder builderForValue)
    
    
    public Explanation.Builder addAttributions(int index, Attribution.Builder builderForValue)

Output only. Feature attributions grouped by predicted outputs.

For Models that predict only one output, such as regression Models that predict only one score, there is only one attibution that explains the predicted output. For Models that predict multiple outputs, such as multiclass Models that predict multiple classes, each element explains one specific item. Attribution.output_index can be used to identify which output this attribution is explaining.

By default, we provide Shapley values for the predicted class. However, you can configure the explanation request to generate Shapley values for any other classes too. For example, if a model predicts a probability of `0.4` for approving a loan application, the model's decision is to reject the application since `p(reject) = 0.6 > p(approve) = 0.4`, and the default Shapley values would be computed for rejection decision and not approval, even though the latter might be the positive class.

If users set ExplanationParameters.top_k, the attributions are sorted by instance_output_value in descending order. If ExplanationParameters.output_indices is specified, the attributions are stored by Attribution.output_index in the same order as they appear in the output_indices.

` repeated .google.cloud.vertexai.v1.Attribution attributions = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[Attribution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Attribution.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Explanation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Explanation.Builder)` |   
  
### addAttributionsBuilder()
    
    
    public Attribution.Builder addAttributionsBuilder()

Output only. Feature attributions grouped by predicted outputs.

For Models that predict only one output, such as regression Models that predict only one score, there is only one attibution that explains the predicted output. For Models that predict multiple outputs, such as multiclass Models that predict multiple classes, each element explains one specific item. Attribution.output_index can be used to identify which output this attribution is explaining.

By default, we provide Shapley values for the predicted class. However, you can configure the explanation request to generate Shapley values for any other classes too. For example, if a model predicts a probability of `0.4` for approving a loan application, the model's decision is to reject the application since `p(reject) = 0.6 > p(approve) = 0.4`, and the default Shapley values would be computed for rejection decision and not approval, even though the latter might be the positive class.

If users set ExplanationParameters.top_k, the attributions are sorted by instance_output_value in descending order. If ExplanationParameters.output_indices is specified, the attributions are stored by Attribution.output_index in the same order as they appear in the output_indices.

` repeated .google.cloud.vertexai.v1.Attribution attributions = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Attribution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Attribution.Builder)` |   
  
### addAttributionsBuilder(int index)
    
    
    public Attribution.Builder addAttributionsBuilder(int index)

Output only. Feature attributions grouped by predicted outputs.

For Models that predict only one output, such as regression Models that predict only one score, there is only one attibution that explains the predicted output. For Models that predict multiple outputs, such as multiclass Models that predict multiple classes, each element explains one specific item. Attribution.output_index can be used to identify which output this attribution is explaining.

By default, we provide Shapley values for the predicted class. However, you can configure the explanation request to generate Shapley values for any other classes too. For example, if a model predicts a probability of `0.4` for approving a loan application, the model's decision is to reject the application since `p(reject) = 0.6 > p(approve) = 0.4`, and the default Shapley values would be computed for rejection decision and not approval, even though the latter might be the positive class.

If users set ExplanationParameters.top_k, the attributions are sorted by instance_output_value in descending order. If ExplanationParameters.output_indices is specified, the attributions are stored by Attribution.output_index in the same order as they appear in the output_indices.

` repeated .google.cloud.vertexai.v1.Attribution attributions = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Attribution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Attribution.Builder)` |   
  
### addNeighbors(Neighbor value)
    
    
    public Explanation.Builder addNeighbors(Neighbor value)

Output only. List of the nearest neighbors for example-based explanations.

For models deployed with the examples explanations feature enabled, the attributions field is empty and instead the neighbors field is populated.

` repeated .google.cloud.vertexai.v1.Neighbor neighbors = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Neighbor](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Neighbor)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Explanation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Explanation.Builder)` |   
  
### addNeighbors(Neighbor.Builder builderForValue)
    
    
    public Explanation.Builder addNeighbors(Neighbor.Builder builderForValue)

Output only. List of the nearest neighbors for example-based explanations.

For models deployed with the examples explanations feature enabled, the attributions field is empty and instead the neighbors field is populated.

` repeated .google.cloud.vertexai.v1.Neighbor neighbors = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Neighbor.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Neighbor.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Explanation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Explanation.Builder)` |   
  
### addNeighbors(int index, Neighbor value)
    
    
    public Explanation.Builder addNeighbors(int index, Neighbor value)

Output only. List of the nearest neighbors for example-based explanations.

For models deployed with the examples explanations feature enabled, the attributions field is empty and instead the neighbors field is populated.

` repeated .google.cloud.vertexai.v1.Neighbor neighbors = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[Neighbor](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Neighbor)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Explanation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Explanation.Builder)` |   
  
### addNeighbors(int index, Neighbor.Builder builderForValue)
    
    
    public Explanation.Builder addNeighbors(int index, Neighbor.Builder builderForValue)

Output only. List of the nearest neighbors for example-based explanations.

For models deployed with the examples explanations feature enabled, the attributions field is empty and instead the neighbors field is populated.

` repeated .google.cloud.vertexai.v1.Neighbor neighbors = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[Neighbor.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Neighbor.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Explanation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Explanation.Builder)` |   
  
### addNeighborsBuilder()
    
    
    public Neighbor.Builder addNeighborsBuilder()

Output only. List of the nearest neighbors for example-based explanations.

For models deployed with the examples explanations feature enabled, the attributions field is empty and instead the neighbors field is populated.

` repeated .google.cloud.vertexai.v1.Neighbor neighbors = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Neighbor.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Neighbor.Builder)` |   
  
### addNeighborsBuilder(int index)
    
    
    public Neighbor.Builder addNeighborsBuilder(int index)

Output only. List of the nearest neighbors for example-based explanations.

For models deployed with the examples explanations feature enabled, the attributions field is empty and instead the neighbors field is populated.

` repeated .google.cloud.vertexai.v1.Neighbor neighbors = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Neighbor.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Neighbor.Builder)` |   
  
### build()
    
    
    public Explanation build()

**Returns**  
---  
**Type** | **Description**  
`[Explanation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Explanation)` |   
  
### buildPartial()
    
    
    public Explanation buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[Explanation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Explanation)` |   
  
### clear()
    
    
    public Explanation.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[Explanation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Explanation.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearAttributions()
    
    
    public Explanation.Builder clearAttributions()

Output only. Feature attributions grouped by predicted outputs.

For Models that predict only one output, such as regression Models that predict only one score, there is only one attibution that explains the predicted output. For Models that predict multiple outputs, such as multiclass Models that predict multiple classes, each element explains one specific item. Attribution.output_index can be used to identify which output this attribution is explaining.

By default, we provide Shapley values for the predicted class. However, you can configure the explanation request to generate Shapley values for any other classes too. For example, if a model predicts a probability of `0.4` for approving a loan application, the model's decision is to reject the application since `p(reject) = 0.6 > p(approve) = 0.4`, and the default Shapley values would be computed for rejection decision and not approval, even though the latter might be the positive class.

If users set ExplanationParameters.top_k, the attributions are sorted by instance_output_value in descending order. If ExplanationParameters.output_indices is specified, the attributions are stored by Attribution.output_index in the same order as they appear in the output_indices.

` repeated .google.cloud.vertexai.v1.Attribution attributions = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Explanation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Explanation.Builder)` |   
  
### clearNeighbors()
    
    
    public Explanation.Builder clearNeighbors()

Output only. List of the nearest neighbors for example-based explanations.

For models deployed with the examples explanations feature enabled, the attributions field is empty and instead the neighbors field is populated.

` repeated .google.cloud.vertexai.v1.Neighbor neighbors = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Explanation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Explanation.Builder)` |   
  
### getAttributions(int index)
    
    
    public Attribution getAttributions(int index)

Output only. Feature attributions grouped by predicted outputs.

For Models that predict only one output, such as regression Models that predict only one score, there is only one attibution that explains the predicted output. For Models that predict multiple outputs, such as multiclass Models that predict multiple classes, each element explains one specific item. Attribution.output_index can be used to identify which output this attribution is explaining.

By default, we provide Shapley values for the predicted class. However, you can configure the explanation request to generate Shapley values for any other classes too. For example, if a model predicts a probability of `0.4` for approving a loan application, the model's decision is to reject the application since `p(reject) = 0.6 > p(approve) = 0.4`, and the default Shapley values would be computed for rejection decision and not approval, even though the latter might be the positive class.

If users set ExplanationParameters.top_k, the attributions are sorted by instance_output_value in descending order. If ExplanationParameters.output_indices is specified, the attributions are stored by Attribution.output_index in the same order as they appear in the output_indices.

` repeated .google.cloud.vertexai.v1.Attribution attributions = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Attribution](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Attribution)` |   
  
### getAttributionsBuilder(int index)
    
    
    public Attribution.Builder getAttributionsBuilder(int index)

Output only. Feature attributions grouped by predicted outputs.

For Models that predict only one output, such as regression Models that predict only one score, there is only one attibution that explains the predicted output. For Models that predict multiple outputs, such as multiclass Models that predict multiple classes, each element explains one specific item. Attribution.output_index can be used to identify which output this attribution is explaining.

By default, we provide Shapley values for the predicted class. However, you can configure the explanation request to generate Shapley values for any other classes too. For example, if a model predicts a probability of `0.4` for approving a loan application, the model's decision is to reject the application since `p(reject) = 0.6 > p(approve) = 0.4`, and the default Shapley values would be computed for rejection decision and not approval, even though the latter might be the positive class.

If users set ExplanationParameters.top_k, the attributions are sorted by instance_output_value in descending order. If ExplanationParameters.output_indices is specified, the attributions are stored by Attribution.output_index in the same order as they appear in the output_indices.

` repeated .google.cloud.vertexai.v1.Attribution attributions = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Attribution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Attribution.Builder)` |   
  
### getAttributionsBuilderList()
    
    
    public List<Attribution.Builder> getAttributionsBuilderList()

Output only. Feature attributions grouped by predicted outputs.

For Models that predict only one output, such as regression Models that predict only one score, there is only one attibution that explains the predicted output. For Models that predict multiple outputs, such as multiclass Models that predict multiple classes, each element explains one specific item. Attribution.output_index can be used to identify which output this attribution is explaining.

By default, we provide Shapley values for the predicted class. However, you can configure the explanation request to generate Shapley values for any other classes too. For example, if a model predicts a probability of `0.4` for approving a loan application, the model's decision is to reject the application since `p(reject) = 0.6 > p(approve) = 0.4`, and the default Shapley values would be computed for rejection decision and not approval, even though the latter might be the positive class.

If users set ExplanationParameters.top_k, the attributions are sorted by instance_output_value in descending order. If ExplanationParameters.output_indices is specified, the attributions are stored by Attribution.output_index in the same order as they appear in the output_indices.

` repeated .google.cloud.vertexai.v1.Attribution attributions = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Attribution.Builder)>` |   
  
### getAttributionsCount()
    
    
    public int getAttributionsCount()

Output only. Feature attributions grouped by predicted outputs.

For Models that predict only one output, such as regression Models that predict only one score, there is only one attibution that explains the predicted output. For Models that predict multiple outputs, such as multiclass Models that predict multiple classes, each element explains one specific item. Attribution.output_index can be used to identify which output this attribution is explaining.

By default, we provide Shapley values for the predicted class. However, you can configure the explanation request to generate Shapley values for any other classes too. For example, if a model predicts a probability of `0.4` for approving a loan application, the model's decision is to reject the application since `p(reject) = 0.6 > p(approve) = 0.4`, and the default Shapley values would be computed for rejection decision and not approval, even though the latter might be the positive class.

If users set ExplanationParameters.top_k, the attributions are sorted by instance_output_value in descending order. If ExplanationParameters.output_indices is specified, the attributions are stored by Attribution.output_index in the same order as they appear in the output_indices.

` repeated .google.cloud.vertexai.v1.Attribution attributions = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAttributionsList()
    
    
    public List<Attribution> getAttributionsList()

Output only. Feature attributions grouped by predicted outputs.

For Models that predict only one output, such as regression Models that predict only one score, there is only one attibution that explains the predicted output. For Models that predict multiple outputs, such as multiclass Models that predict multiple classes, each element explains one specific item. Attribution.output_index can be used to identify which output this attribution is explaining.

By default, we provide Shapley values for the predicted class. However, you can configure the explanation request to generate Shapley values for any other classes too. For example, if a model predicts a probability of `0.4` for approving a loan application, the model's decision is to reject the application since `p(reject) = 0.6 > p(approve) = 0.4`, and the default Shapley values would be computed for rejection decision and not approval, even though the latter might be the positive class.

If users set ExplanationParameters.top_k, the attributions are sorted by instance_output_value in descending order. If ExplanationParameters.output_indices is specified, the attributions are stored by Attribution.output_index in the same order as they appear in the output_indices.

` repeated .google.cloud.vertexai.v1.Attribution attributions = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Attribution](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Attribution)>` |   
  
### getAttributionsOrBuilder(int index)
    
    
    public AttributionOrBuilder getAttributionsOrBuilder(int index)

Output only. Feature attributions grouped by predicted outputs.

For Models that predict only one output, such as regression Models that predict only one score, there is only one attibution that explains the predicted output. For Models that predict multiple outputs, such as multiclass Models that predict multiple classes, each element explains one specific item. Attribution.output_index can be used to identify which output this attribution is explaining.

By default, we provide Shapley values for the predicted class. However, you can configure the explanation request to generate Shapley values for any other classes too. For example, if a model predicts a probability of `0.4` for approving a loan application, the model's decision is to reject the application since `p(reject) = 0.6 > p(approve) = 0.4`, and the default Shapley values would be computed for rejection decision and not approval, even though the latter might be the positive class.

If users set ExplanationParameters.top_k, the attributions are sorted by instance_output_value in descending order. If ExplanationParameters.output_indices is specified, the attributions are stored by Attribution.output_index in the same order as they appear in the output_indices.

` repeated .google.cloud.vertexai.v1.Attribution attributions = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AttributionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.AttributionOrBuilder)` |   
  
### getAttributionsOrBuilderList()
    
    
    public List<? extends AttributionOrBuilder> getAttributionsOrBuilderList()

Output only. Feature attributions grouped by predicted outputs.

For Models that predict only one output, such as regression Models that predict only one score, there is only one attibution that explains the predicted output. For Models that predict multiple outputs, such as multiclass Models that predict multiple classes, each element explains one specific item. Attribution.output_index can be used to identify which output this attribution is explaining.

By default, we provide Shapley values for the predicted class. However, you can configure the explanation request to generate Shapley values for any other classes too. For example, if a model predicts a probability of `0.4` for approving a loan application, the model's decision is to reject the application since `p(reject) = 0.6 > p(approve) = 0.4`, and the default Shapley values would be computed for rejection decision and not approval, even though the latter might be the positive class.

If users set ExplanationParameters.top_k, the attributions are sorted by instance_output_value in descending order. If ExplanationParameters.output_indices is specified, the attributions are stored by Attribution.output_index in the same order as they appear in the output_indices.

` repeated .google.cloud.vertexai.v1.Attribution attributions = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.vertexai.api.AttributionOrBuilder>` |   
  
### getDefaultInstanceForType()
    
    
    public Explanation getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[Explanation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Explanation)` |   
  
### getDescriptorForType()
    
    
    public Descriptors.Descriptor getDescriptorForType()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getDescriptorForType__)

### getNeighbors(int index)
    
    
    public Neighbor getNeighbors(int index)

Output only. List of the nearest neighbors for example-based explanations.

For models deployed with the examples explanations feature enabled, the attributions field is empty and instead the neighbors field is populated.

` repeated .google.cloud.vertexai.v1.Neighbor neighbors = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Neighbor](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Neighbor)` |   
  
### getNeighborsBuilder(int index)
    
    
    public Neighbor.Builder getNeighborsBuilder(int index)

Output only. List of the nearest neighbors for example-based explanations.

For models deployed with the examples explanations feature enabled, the attributions field is empty and instead the neighbors field is populated.

` repeated .google.cloud.vertexai.v1.Neighbor neighbors = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Neighbor.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Neighbor.Builder)` |   
  
### getNeighborsBuilderList()
    
    
    public List<Neighbor.Builder> getNeighborsBuilderList()

Output only. List of the nearest neighbors for example-based explanations.

For models deployed with the examples explanations feature enabled, the attributions field is empty and instead the neighbors field is populated.

` repeated .google.cloud.vertexai.v1.Neighbor neighbors = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Neighbor.Builder)>` |   
  
### getNeighborsCount()
    
    
    public int getNeighborsCount()

Output only. List of the nearest neighbors for example-based explanations.

For models deployed with the examples explanations feature enabled, the attributions field is empty and instead the neighbors field is populated.

` repeated .google.cloud.vertexai.v1.Neighbor neighbors = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getNeighborsList()
    
    
    public List<Neighbor> getNeighborsList()

Output only. List of the nearest neighbors for example-based explanations.

For models deployed with the examples explanations feature enabled, the attributions field is empty and instead the neighbors field is populated.

` repeated .google.cloud.vertexai.v1.Neighbor neighbors = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Neighbor](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Neighbor)>` |   
  
### getNeighborsOrBuilder(int index)
    
    
    public NeighborOrBuilder getNeighborsOrBuilder(int index)

Output only. List of the nearest neighbors for example-based explanations.

For models deployed with the examples explanations feature enabled, the attributions field is empty and instead the neighbors field is populated.

` repeated .google.cloud.vertexai.v1.Neighbor neighbors = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[NeighborOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.NeighborOrBuilder)` |   
  
### getNeighborsOrBuilderList()
    
    
    public List<? extends NeighborOrBuilder> getNeighborsOrBuilderList()

Output only. List of the nearest neighbors for example-based explanations.

For models deployed with the examples explanations feature enabled, the attributions field is empty and instead the neighbors field is populated.

` repeated .google.cloud.vertexai.v1.Neighbor neighbors = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.vertexai.api.NeighborOrBuilder>` |   
  
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

### mergeFrom(Explanation other)
    
    
    public Explanation.Builder mergeFrom(Explanation other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Explanation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Explanation)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Explanation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Explanation.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public Explanation.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Explanation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Explanation.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public Explanation.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Explanation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Explanation.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### removeAttributions(int index)
    
    
    public Explanation.Builder removeAttributions(int index)

Output only. Feature attributions grouped by predicted outputs.

For Models that predict only one output, such as regression Models that predict only one score, there is only one attibution that explains the predicted output. For Models that predict multiple outputs, such as multiclass Models that predict multiple classes, each element explains one specific item. Attribution.output_index can be used to identify which output this attribution is explaining.

By default, we provide Shapley values for the predicted class. However, you can configure the explanation request to generate Shapley values for any other classes too. For example, if a model predicts a probability of `0.4` for approving a loan application, the model's decision is to reject the application since `p(reject) = 0.6 > p(approve) = 0.4`, and the default Shapley values would be computed for rejection decision and not approval, even though the latter might be the positive class.

If users set ExplanationParameters.top_k, the attributions are sorted by instance_output_value in descending order. If ExplanationParameters.output_indices is specified, the attributions are stored by Attribution.output_index in the same order as they appear in the output_indices.

` repeated .google.cloud.vertexai.v1.Attribution attributions = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Explanation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Explanation.Builder)` |   
  
### removeNeighbors(int index)
    
    
    public Explanation.Builder removeNeighbors(int index)

Output only. List of the nearest neighbors for example-based explanations.

For models deployed with the examples explanations feature enabled, the attributions field is empty and instead the neighbors field is populated.

` repeated .google.cloud.vertexai.v1.Neighbor neighbors = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Explanation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Explanation.Builder)` |   
  
### setAttributions(int index, Attribution value)
    
    
    public Explanation.Builder setAttributions(int index, Attribution value)

Output only. Feature attributions grouped by predicted outputs.

For Models that predict only one output, such as regression Models that predict only one score, there is only one attibution that explains the predicted output. For Models that predict multiple outputs, such as multiclass Models that predict multiple classes, each element explains one specific item. Attribution.output_index can be used to identify which output this attribution is explaining.

By default, we provide Shapley values for the predicted class. However, you can configure the explanation request to generate Shapley values for any other classes too. For example, if a model predicts a probability of `0.4` for approving a loan application, the model's decision is to reject the application since `p(reject) = 0.6 > p(approve) = 0.4`, and the default Shapley values would be computed for rejection decision and not approval, even though the latter might be the positive class.

If users set ExplanationParameters.top_k, the attributions are sorted by instance_output_value in descending order. If ExplanationParameters.output_indices is specified, the attributions are stored by Attribution.output_index in the same order as they appear in the output_indices.

` repeated .google.cloud.vertexai.v1.Attribution attributions = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[Attribution](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Attribution)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Explanation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Explanation.Builder)` |   
  
### setAttributions(int index, Attribution.Builder builderForValue)
    
    
    public Explanation.Builder setAttributions(int index, Attribution.Builder builderForValue)

Output only. Feature attributions grouped by predicted outputs.

For Models that predict only one output, such as regression Models that predict only one score, there is only one attibution that explains the predicted output. For Models that predict multiple outputs, such as multiclass Models that predict multiple classes, each element explains one specific item. Attribution.output_index can be used to identify which output this attribution is explaining.

By default, we provide Shapley values for the predicted class. However, you can configure the explanation request to generate Shapley values for any other classes too. For example, if a model predicts a probability of `0.4` for approving a loan application, the model's decision is to reject the application since `p(reject) = 0.6 > p(approve) = 0.4`, and the default Shapley values would be computed for rejection decision and not approval, even though the latter might be the positive class.

If users set ExplanationParameters.top_k, the attributions are sorted by instance_output_value in descending order. If ExplanationParameters.output_indices is specified, the attributions are stored by Attribution.output_index in the same order as they appear in the output_indices.

` repeated .google.cloud.vertexai.v1.Attribution attributions = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[Attribution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Attribution.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Explanation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Explanation.Builder)` |   
  
### setNeighbors(int index, Neighbor value)
    
    
    public Explanation.Builder setNeighbors(int index, Neighbor value)

Output only. List of the nearest neighbors for example-based explanations.

For models deployed with the examples explanations feature enabled, the attributions field is empty and instead the neighbors field is populated.

` repeated .google.cloud.vertexai.v1.Neighbor neighbors = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[Neighbor](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Neighbor)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Explanation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Explanation.Builder)` |   
  
### setNeighbors(int index, Neighbor.Builder builderForValue)
    
    
    public Explanation.Builder setNeighbors(int index, Neighbor.Builder builderForValue)

Output only. List of the nearest neighbors for example-based explanations.

For models deployed with the examples explanations feature enabled, the attributions field is empty and instead the neighbors field is populated.

` repeated .google.cloud.vertexai.v1.Neighbor neighbors = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[Neighbor.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Neighbor.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Explanation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Explanation.Builder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-30 UTC."],[],[]] 
