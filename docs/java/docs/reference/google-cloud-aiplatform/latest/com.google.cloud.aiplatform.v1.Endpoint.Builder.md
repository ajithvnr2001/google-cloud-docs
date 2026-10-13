---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder
title: Class Endpoint.Builder (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:47:14.785714+00:00
---

# Class Endpoint.Builder (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class Endpoint.Builder (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.82.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.0.0  2.9.8  2.8.9  2.7.4  2.5.3  2.4.0 
    
    
    public static final class Endpoint.Builder extends GeneratedMessage.Builder<Endpoint.Builder> implements EndpointOrBuilder

Models are deployed into it, and afterwards Endpoint is called to obtain predictions and explanations.

Protobuf type `google.cloud.aiplatform.v1.Endpoint`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > Endpoint.Builder

## Implements

[EndpointOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointOrBuilder)

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

### addAllDeployedModels(Iterable<? extends DeployedModel> values)
    
    
    public Endpoint.Builder addAllDeployedModels(Iterable<? extends DeployedModel> values)

Output only. The models deployed in this Endpoint. To add or remove DeployedModels use EndpointService.DeployModel and EndpointService.UndeployModel respectively.

` repeated .google.cloud.aiplatform.v1.DeployedModel deployed_models = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<? extends com.google.cloud.aiplatform.v1.DeployedModel>`  
  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` |   
  
### addDeployedModels(DeployedModel value)
    
    
    public Endpoint.Builder addDeployedModels(DeployedModel value)

Output only. The models deployed in this Endpoint. To add or remove DeployedModels use EndpointService.DeployModel and EndpointService.UndeployModel respectively.

` repeated .google.cloud.aiplatform.v1.DeployedModel deployed_models = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[DeployedModel](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployedModel)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` |   
  
### addDeployedModels(DeployedModel.Builder builderForValue)
    
    
    public Endpoint.Builder addDeployedModels(DeployedModel.Builder builderForValue)

Output only. The models deployed in this Endpoint. To add or remove DeployedModels use EndpointService.DeployModel and EndpointService.UndeployModel respectively.

` repeated .google.cloud.aiplatform.v1.DeployedModel deployed_models = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[DeployedModel.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployedModel.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` |   
  
### addDeployedModels(int index, DeployedModel value)
    
    
    public Endpoint.Builder addDeployedModels(int index, DeployedModel value)

Output only. The models deployed in this Endpoint. To add or remove DeployedModels use EndpointService.DeployModel and EndpointService.UndeployModel respectively.

` repeated .google.cloud.aiplatform.v1.DeployedModel deployed_models = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[DeployedModel](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployedModel)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` |   
  
### addDeployedModels(int index, DeployedModel.Builder builderForValue)
    
    
    public Endpoint.Builder addDeployedModels(int index, DeployedModel.Builder builderForValue)

Output only. The models deployed in this Endpoint. To add or remove DeployedModels use EndpointService.DeployModel and EndpointService.UndeployModel respectively.

` repeated .google.cloud.aiplatform.v1.DeployedModel deployed_models = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[DeployedModel.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployedModel.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` |   
  
### addDeployedModelsBuilder()
    
    
    public DeployedModel.Builder addDeployedModelsBuilder()

Output only. The models deployed in this Endpoint. To add or remove DeployedModels use EndpointService.DeployModel and EndpointService.UndeployModel respectively.

` repeated .google.cloud.aiplatform.v1.DeployedModel deployed_models = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[DeployedModel.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployedModel.Builder)` |   
  
### addDeployedModelsBuilder(int index)
    
    
    public DeployedModel.Builder addDeployedModelsBuilder(int index)

Output only. The models deployed in this Endpoint. To add or remove DeployedModels use EndpointService.DeployModel and EndpointService.UndeployModel respectively.

` repeated .google.cloud.aiplatform.v1.DeployedModel deployed_models = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DeployedModel.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployedModel.Builder)` |   
  
### build()
    
    
    public Endpoint build()

**Returns**  
---  
**Type** | **Description**  
`[Endpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint)` |   
  
### buildPartial()
    
    
    public Endpoint buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[Endpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint)` |   
  
### clear()
    
    
    public Endpoint.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearClientConnectionConfig()
    
    
    public Endpoint.Builder clearClientConnectionConfig()

Configurations that are applied to the endpoint for online prediction.

`.google.cloud.aiplatform.v1.ClientConnectionConfig client_connection_config = 23; `

**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` |   
  
### clearCreateTime()
    
    
    public Endpoint.Builder clearCreateTime()

Output only. Timestamp when this Endpoint was created.

` .google.protobuf.Timestamp create_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` |   
  
### clearDedicatedEndpointDns()
    
    
    public Endpoint.Builder clearDedicatedEndpointDns()

Output only. DNS of the dedicated endpoint. Will only be populated if dedicated_endpoint_enabled is true. Depending on the features enabled, uid might be a random number or a string. For example, if fast_tryout is enabled, uid will be fasttryout. Format: `https://{endpoint_id}.{region}-{uid}.prediction.vertexai.goog`.

`string dedicated_endpoint_dns = 25 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` | This builder for chaining.  
  
### clearDedicatedEndpointEnabled()
    
    
    public Endpoint.Builder clearDedicatedEndpointEnabled()

If true, the endpoint will be exposed through a dedicated DNS [Endpoint.dedicated_endpoint_dns]. Your request to the dedicated DNS will be isolated from other users' traffic and will have better performance and reliability. Note: Once you enabled dedicated endpoint, you won't be able to send request to the shared DNS {region}-aiplatform.googleapis.com. The limitation will be removed soon.

`bool dedicated_endpoint_enabled = 24;`

**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` | This builder for chaining.  
  
### clearDeployedModels()
    
    
    public Endpoint.Builder clearDeployedModels()

Output only. The models deployed in this Endpoint. To add or remove DeployedModels use EndpointService.DeployModel and EndpointService.UndeployModel respectively.

` repeated .google.cloud.aiplatform.v1.DeployedModel deployed_models = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` |   
  
### clearDescription()
    
    
    public Endpoint.Builder clearDescription()

The description of the Endpoint.

`string description = 3;`

**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` | This builder for chaining.  
  
### clearDisplayName()
    
    
    public Endpoint.Builder clearDisplayName()

Required. The display name of the Endpoint. The name can be up to 128 characters long and can consist of any UTF-8 characters.

`string display_name = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` | This builder for chaining.  
  
### clearEnablePrivateServiceConnect() (deprecated)
    
    
    public Endpoint.Builder clearEnablePrivateServiceConnect()

**Deprecated.** _google.cloud.aiplatform.v1.Endpoint.enable_private_service_connect is deprecated. See google/cloud/aiplatform/v1/endpoint.proto;l=128_

Deprecated: If true, expose the Endpoint via private service connect.

Only one of the fields, network or enable_private_service_connect, can be set.

`bool enable_private_service_connect = 17 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` | This builder for chaining.  
  
### clearEncryptionSpec()
    
    
    public Endpoint.Builder clearEncryptionSpec()

Customer-managed encryption key spec for an Endpoint. If set, this Endpoint and all sub-resources of this Endpoint will be secured by this key.

`.google.cloud.aiplatform.v1.EncryptionSpec encryption_spec = 10;`

**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` |   
  
### clearEtag()
    
    
    public Endpoint.Builder clearEtag()

Used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens.

`string etag = 6;`

**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` | This builder for chaining.  
  
### clearGenAiAdvancedFeaturesConfig()
    
    
    public Endpoint.Builder clearGenAiAdvancedFeaturesConfig()

Optional. Configuration for GenAiAdvancedFeatures. If the endpoint is serving GenAI models, advanced features like native RAG integration can be configured. Currently, only Model Garden models are supported.

` .google.cloud.aiplatform.v1.GenAiAdvancedFeaturesConfig gen_ai_advanced_features_config = 29 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` |   
  
### clearLabels()
    
    
    public Endpoint.Builder clearLabels()

**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` |   
  
### clearModelDeploymentMonitoringJob()
    
    
    public Endpoint.Builder clearModelDeploymentMonitoringJob()

Output only. Resource name of the Model Monitoring job associated with this Endpoint if monitoring is enabled by JobService.CreateModelDeploymentMonitoringJob. Format: `projects/{project}/locations/{location}/modelDeploymentMonitoringJobs/{model_deployment_monitoring_job}`

` string model_deployment_monitoring_job = 14 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` | This builder for chaining.  
  
### clearName()
    
    
    public Endpoint.Builder clearName()

Output only. The resource name of the Endpoint.

`string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` | This builder for chaining.  
  
### clearNetwork()
    
    
    public Endpoint.Builder clearNetwork()

Optional. The full name of the Google Compute Engine [network](https://cloud.google.com//compute/docs/networks-and-firewalls#networks) to which the Endpoint should be peered.

Private services access must already be configured for the network. If left unspecified, the Endpoint is not peered with any network.

Only one of the fields, network or enable_private_service_connect, can be set.

[Format](https://cloud.google.com/compute/docs/reference/rest/v1/networks/insert): `projects/{project}/global/networks/{network}`. Where `{project}` is a project number, as in `12345`, and `{network}` is network name.

` string network = 13 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` | This builder for chaining.  
  
### clearPredictRequestResponseLoggingConfig()
    
    
    public Endpoint.Builder clearPredictRequestResponseLoggingConfig()

Configures the request-response logging for online prediction.

` .google.cloud.aiplatform.v1.PredictRequestResponseLoggingConfig predict_request_response_logging_config = 18; `

**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` |   
  
### clearPrivateModelServerEnabled()
    
    
    public Endpoint.Builder clearPrivateModelServerEnabled()

If true, the model server will be isolated from the external internet.

`bool private_model_server_enabled = 30;`

**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` | This builder for chaining.  
  
### clearPrivateServiceConnectConfig()
    
    
    public Endpoint.Builder clearPrivateServiceConnectConfig()

Optional. Configuration for private service connect.

network and private_service_connect_config are mutually exclusive.

` .google.cloud.aiplatform.v1.PrivateServiceConnectConfig private_service_connect_config = 21 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` |   
  
### clearSatisfiesPzi()
    
    
    public Endpoint.Builder clearSatisfiesPzi()

Output only. Reserved for future use.

`bool satisfies_pzi = 28 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` | This builder for chaining.  
  
### clearSatisfiesPzs()
    
    
    public Endpoint.Builder clearSatisfiesPzs()

Output only. Reserved for future use.

`bool satisfies_pzs = 27 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` | This builder for chaining.  
  
### clearTrafficSplit()
    
    
    public Endpoint.Builder clearTrafficSplit()

**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` |   
  
### clearUpdateTime()
    
    
    public Endpoint.Builder clearUpdateTime()

Output only. Timestamp when this Endpoint was last updated.

` .google.protobuf.Timestamp update_time = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` |   
  
### containsLabels(String key)
    
    
    public boolean containsLabels(String key)

The labels with user-defined metadata to organize your Endpoints.

Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed.

See <https://goo.gl/xmQnxf> for more information and examples of labels.

`map<string, string> labels = 7;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### containsTrafficSplit(String key)
    
    
    public boolean containsTrafficSplit(String key)

A map from a DeployedModel's ID to the percentage of this Endpoint's traffic that should be forwarded to that DeployedModel.

If a DeployedModel's ID is not listed in this map, then it receives no traffic.

The traffic percentage values must add up to 100, or map must be empty if the Endpoint is to not accept any traffic at a moment.

`map<string, int32> traffic_split = 5;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getClientConnectionConfig()
    
    
    public ClientConnectionConfig getClientConnectionConfig()

Configurations that are applied to the endpoint for online prediction.

`.google.cloud.aiplatform.v1.ClientConnectionConfig client_connection_config = 23; `

**Returns**  
---  
**Type** | **Description**  
`[ClientConnectionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ClientConnectionConfig)` | The clientConnectionConfig.  
  
### getClientConnectionConfigBuilder()
    
    
    public ClientConnectionConfig.Builder getClientConnectionConfigBuilder()

Configurations that are applied to the endpoint for online prediction.

`.google.cloud.aiplatform.v1.ClientConnectionConfig client_connection_config = 23; `

**Returns**  
---  
**Type** | **Description**  
`[ClientConnectionConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ClientConnectionConfig.Builder)` |   
  
### getClientConnectionConfigOrBuilder()
    
    
    public ClientConnectionConfigOrBuilder getClientConnectionConfigOrBuilder()

Configurations that are applied to the endpoint for online prediction.

`.google.cloud.aiplatform.v1.ClientConnectionConfig client_connection_config = 23; `

**Returns**  
---  
**Type** | **Description**  
`[ClientConnectionConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ClientConnectionConfigOrBuilder)` |   
  
### getCreateTime()
    
    
    public Timestamp getCreateTime()

Output only. Timestamp when this Endpoint was created.

` .google.protobuf.Timestamp create_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeBuilder()
    
    
    public Timestamp.Builder getCreateTimeBuilder()

Output only. Timestamp when this Endpoint was created.

` .google.protobuf.Timestamp create_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)` |   
  
### getCreateTimeOrBuilder()
    
    
    public TimestampOrBuilder getCreateTimeOrBuilder()

Output only. Timestamp when this Endpoint was created.

` .google.protobuf.Timestamp create_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDedicatedEndpointDns()
    
    
    public String getDedicatedEndpointDns()

Output only. DNS of the dedicated endpoint. Will only be populated if dedicated_endpoint_enabled is true. Depending on the features enabled, uid might be a random number or a string. For example, if fast_tryout is enabled, uid will be fasttryout. Format: `https://{endpoint_id}.{region}-{uid}.prediction.vertexai.goog`.

`string dedicated_endpoint_dns = 25 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The dedicatedEndpointDns.  
  
### getDedicatedEndpointDnsBytes()
    
    
    public ByteString getDedicatedEndpointDnsBytes()

Output only. DNS of the dedicated endpoint. Will only be populated if dedicated_endpoint_enabled is true. Depending on the features enabled, uid might be a random number or a string. For example, if fast_tryout is enabled, uid will be fasttryout. Format: `https://{endpoint_id}.{region}-{uid}.prediction.vertexai.goog`.

`string dedicated_endpoint_dns = 25 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for dedicatedEndpointDns.  
  
### getDedicatedEndpointEnabled()
    
    
    public boolean getDedicatedEndpointEnabled()

If true, the endpoint will be exposed through a dedicated DNS [Endpoint.dedicated_endpoint_dns]. Your request to the dedicated DNS will be isolated from other users' traffic and will have better performance and reliability. Note: Once you enabled dedicated endpoint, you won't be able to send request to the shared DNS {region}-aiplatform.googleapis.com. The limitation will be removed soon.

`bool dedicated_endpoint_enabled = 24;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The dedicatedEndpointEnabled.  
  
### getDefaultInstanceForType()
    
    
    public Endpoint getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[Endpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint)` |   
  
### getDeployedModels(int index)
    
    
    public DeployedModel getDeployedModels(int index)

Output only. The models deployed in this Endpoint. To add or remove DeployedModels use EndpointService.DeployModel and EndpointService.UndeployModel respectively.

` repeated .google.cloud.aiplatform.v1.DeployedModel deployed_models = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DeployedModel](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployedModel)` |   
  
### getDeployedModelsBuilder(int index)
    
    
    public DeployedModel.Builder getDeployedModelsBuilder(int index)

Output only. The models deployed in this Endpoint. To add or remove DeployedModels use EndpointService.DeployModel and EndpointService.UndeployModel respectively.

` repeated .google.cloud.aiplatform.v1.DeployedModel deployed_models = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DeployedModel.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployedModel.Builder)` |   
  
### getDeployedModelsBuilderList()
    
    
    public List<DeployedModel.Builder> getDeployedModelsBuilderList()

Output only. The models deployed in this Endpoint. To add or remove DeployedModels use EndpointService.DeployModel and EndpointService.UndeployModel respectively.

` repeated .google.cloud.aiplatform.v1.DeployedModel deployed_models = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployedModel.Builder)>` |   
  
### getDeployedModelsCount()
    
    
    public int getDeployedModelsCount()

Output only. The models deployed in this Endpoint. To add or remove DeployedModels use EndpointService.DeployModel and EndpointService.UndeployModel respectively.

` repeated .google.cloud.aiplatform.v1.DeployedModel deployed_models = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getDeployedModelsList()
    
    
    public List<DeployedModel> getDeployedModelsList()

Output only. The models deployed in this Endpoint. To add or remove DeployedModels use EndpointService.DeployModel and EndpointService.UndeployModel respectively.

` repeated .google.cloud.aiplatform.v1.DeployedModel deployed_models = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[DeployedModel](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployedModel)>` |   
  
### getDeployedModelsOrBuilder(int index)
    
    
    public DeployedModelOrBuilder getDeployedModelsOrBuilder(int index)

Output only. The models deployed in this Endpoint. To add or remove DeployedModels use EndpointService.DeployModel and EndpointService.UndeployModel respectively.

` repeated .google.cloud.aiplatform.v1.DeployedModel deployed_models = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DeployedModelOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployedModelOrBuilder)` |   
  
### getDeployedModelsOrBuilderList()
    
    
    public List<? extends DeployedModelOrBuilder> getDeployedModelsOrBuilderList()

Output only. The models deployed in this Endpoint. To add or remove DeployedModels use EndpointService.DeployModel and EndpointService.UndeployModel respectively.

` repeated .google.cloud.aiplatform.v1.DeployedModel deployed_models = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.aiplatform.v1.DeployedModelOrBuilder>` |   
  
### getDescription()
    
    
    public String getDescription()

The description of the Endpoint.

`string description = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The description.  
  
### getDescriptionBytes()
    
    
    public ByteString getDescriptionBytes()

The description of the Endpoint.

`string description = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for description.  
  
### getDescriptorForType()
    
    
    public Descriptors.Descriptor getDescriptorForType()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getDescriptorForType__)

### getDisplayName()
    
    
    public String getDisplayName()

Required. The display name of the Endpoint. The name can be up to 128 characters long and can consist of any UTF-8 characters.

`string display_name = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The displayName.  
  
### getDisplayNameBytes()
    
    
    public ByteString getDisplayNameBytes()

Required. The display name of the Endpoint. The name can be up to 128 characters long and can consist of any UTF-8 characters.

`string display_name = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for displayName.  
  
### getEnablePrivateServiceConnect() (deprecated)
    
    
    public boolean getEnablePrivateServiceConnect()

**Deprecated.** _google.cloud.aiplatform.v1.Endpoint.enable_private_service_connect is deprecated. See google/cloud/aiplatform/v1/endpoint.proto;l=128_

Deprecated: If true, expose the Endpoint via private service connect.

Only one of the fields, network or enable_private_service_connect, can be set.

`bool enable_private_service_connect = 17 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enablePrivateServiceConnect.  
  
### getEncryptionSpec()
    
    
    public EncryptionSpec getEncryptionSpec()

Customer-managed encryption key spec for an Endpoint. If set, this Endpoint and all sub-resources of this Endpoint will be secured by this key.

`.google.cloud.aiplatform.v1.EncryptionSpec encryption_spec = 10;`

**Returns**  
---  
**Type** | **Description**  
`[EncryptionSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EncryptionSpec)` | The encryptionSpec.  
  
### getEncryptionSpecBuilder()
    
    
    public EncryptionSpec.Builder getEncryptionSpecBuilder()

Customer-managed encryption key spec for an Endpoint. If set, this Endpoint and all sub-resources of this Endpoint will be secured by this key.

`.google.cloud.aiplatform.v1.EncryptionSpec encryption_spec = 10;`

**Returns**  
---  
**Type** | **Description**  
`[EncryptionSpec.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EncryptionSpec.Builder)` |   
  
### getEncryptionSpecOrBuilder()
    
    
    public EncryptionSpecOrBuilder getEncryptionSpecOrBuilder()

Customer-managed encryption key spec for an Endpoint. If set, this Endpoint and all sub-resources of this Endpoint will be secured by this key.

`.google.cloud.aiplatform.v1.EncryptionSpec encryption_spec = 10;`

**Returns**  
---  
**Type** | **Description**  
`[EncryptionSpecOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EncryptionSpecOrBuilder)` |   
  
### getEtag()
    
    
    public String getEtag()

Used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens.

`string etag = 6;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The etag.  
  
### getEtagBytes()
    
    
    public ByteString getEtagBytes()

Used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens.

`string etag = 6;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for etag.  
  
### getGenAiAdvancedFeaturesConfig()
    
    
    public GenAiAdvancedFeaturesConfig getGenAiAdvancedFeaturesConfig()

Optional. Configuration for GenAiAdvancedFeatures. If the endpoint is serving GenAI models, advanced features like native RAG integration can be configured. Currently, only Model Garden models are supported.

` .google.cloud.aiplatform.v1.GenAiAdvancedFeaturesConfig gen_ai_advanced_features_config = 29 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[GenAiAdvancedFeaturesConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GenAiAdvancedFeaturesConfig)` | The genAiAdvancedFeaturesConfig.  
  
### getGenAiAdvancedFeaturesConfigBuilder()
    
    
    public GenAiAdvancedFeaturesConfig.Builder getGenAiAdvancedFeaturesConfigBuilder()

Optional. Configuration for GenAiAdvancedFeatures. If the endpoint is serving GenAI models, advanced features like native RAG integration can be configured. Currently, only Model Garden models are supported.

` .google.cloud.aiplatform.v1.GenAiAdvancedFeaturesConfig gen_ai_advanced_features_config = 29 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[GenAiAdvancedFeaturesConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GenAiAdvancedFeaturesConfig.Builder)` |   
  
### getGenAiAdvancedFeaturesConfigOrBuilder()
    
    
    public GenAiAdvancedFeaturesConfigOrBuilder getGenAiAdvancedFeaturesConfigOrBuilder()

Optional. Configuration for GenAiAdvancedFeatures. If the endpoint is serving GenAI models, advanced features like native RAG integration can be configured. Currently, only Model Garden models are supported.

` .google.cloud.aiplatform.v1.GenAiAdvancedFeaturesConfig gen_ai_advanced_features_config = 29 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[GenAiAdvancedFeaturesConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GenAiAdvancedFeaturesConfigOrBuilder)` |   
  
### getLabels() (deprecated)
    
    
    public Map<String,String> getLabels()

Use [#getLabelsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder#com_google_cloud_aiplatform_v1_Endpoint_Builder_getLabelsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsCount()
    
    
    public int getLabelsCount()

The labels with user-defined metadata to organize your Endpoints.

Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed.

See <https://goo.gl/xmQnxf> for more information and examples of labels.

`map<string, string> labels = 7;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getLabelsMap()
    
    
    public Map<String,String> getLabelsMap()

The labels with user-defined metadata to organize your Endpoints.

Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed.

See <https://goo.gl/xmQnxf> for more information and examples of labels.

`map<string, string> labels = 7;`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsOrDefault(String key, String defaultValue)
    
    
    public String getLabelsOrDefault(String key, String defaultValue)

The labels with user-defined metadata to organize your Endpoints.

Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed.

See <https://goo.gl/xmQnxf> for more information and examples of labels.

`map<string, string> labels = 7;`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getLabelsOrThrow(String key)
    
    
    public String getLabelsOrThrow(String key)

The labels with user-defined metadata to organize your Endpoints.

Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed.

See <https://goo.gl/xmQnxf> for more information and examples of labels.

`map<string, string> labels = 7;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getModelDeploymentMonitoringJob()
    
    
    public String getModelDeploymentMonitoringJob()

Output only. Resource name of the Model Monitoring job associated with this Endpoint if monitoring is enabled by JobService.CreateModelDeploymentMonitoringJob. Format: `projects/{project}/locations/{location}/modelDeploymentMonitoringJobs/{model_deployment_monitoring_job}`

` string model_deployment_monitoring_job = 14 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The modelDeploymentMonitoringJob.  
  
### getModelDeploymentMonitoringJobBytes()
    
    
    public ByteString getModelDeploymentMonitoringJobBytes()

Output only. Resource name of the Model Monitoring job associated with this Endpoint if monitoring is enabled by JobService.CreateModelDeploymentMonitoringJob. Format: `projects/{project}/locations/{location}/modelDeploymentMonitoringJobs/{model_deployment_monitoring_job}`

` string model_deployment_monitoring_job = 14 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for modelDeploymentMonitoringJob.  
  
### getMutableLabels() (deprecated)
    
    
    public Map<String,String> getMutableLabels()

Use alternate mutation accessors instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getMutableTrafficSplit() (deprecated)
    
    
    public Map<String,Integer> getMutableTrafficSplit()

Use alternate mutation accessors instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)>` |   
  
### getName()
    
    
    public String getName()

Output only. The resource name of the Endpoint.

`string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public ByteString getNameBytes()

Output only. The resource name of the Endpoint.

`string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getNetwork()
    
    
    public String getNetwork()

Optional. The full name of the Google Compute Engine [network](https://cloud.google.com//compute/docs/networks-and-firewalls#networks) to which the Endpoint should be peered.

Private services access must already be configured for the network. If left unspecified, the Endpoint is not peered with any network.

Only one of the fields, network or enable_private_service_connect, can be set.

[Format](https://cloud.google.com/compute/docs/reference/rest/v1/networks/insert): `projects/{project}/global/networks/{network}`. Where `{project}` is a project number, as in `12345`, and `{network}` is network name.

` string network = 13 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The network.  
  
### getNetworkBytes()
    
    
    public ByteString getNetworkBytes()

Optional. The full name of the Google Compute Engine [network](https://cloud.google.com//compute/docs/networks-and-firewalls#networks) to which the Endpoint should be peered.

Private services access must already be configured for the network. If left unspecified, the Endpoint is not peered with any network.

Only one of the fields, network or enable_private_service_connect, can be set.

[Format](https://cloud.google.com/compute/docs/reference/rest/v1/networks/insert): `projects/{project}/global/networks/{network}`. Where `{project}` is a project number, as in `12345`, and `{network}` is network name.

` string network = 13 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for network.  
  
### getPredictRequestResponseLoggingConfig()
    
    
    public PredictRequestResponseLoggingConfig getPredictRequestResponseLoggingConfig()

Configures the request-response logging for online prediction.

` .google.cloud.aiplatform.v1.PredictRequestResponseLoggingConfig predict_request_response_logging_config = 18; `

**Returns**  
---  
**Type** | **Description**  
`[PredictRequestResponseLoggingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictRequestResponseLoggingConfig)` | The predictRequestResponseLoggingConfig.  
  
### getPredictRequestResponseLoggingConfigBuilder()
    
    
    public PredictRequestResponseLoggingConfig.Builder getPredictRequestResponseLoggingConfigBuilder()

Configures the request-response logging for online prediction.

` .google.cloud.aiplatform.v1.PredictRequestResponseLoggingConfig predict_request_response_logging_config = 18; `

**Returns**  
---  
**Type** | **Description**  
`[PredictRequestResponseLoggingConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictRequestResponseLoggingConfig.Builder)` |   
  
### getPredictRequestResponseLoggingConfigOrBuilder()
    
    
    public PredictRequestResponseLoggingConfigOrBuilder getPredictRequestResponseLoggingConfigOrBuilder()

Configures the request-response logging for online prediction.

` .google.cloud.aiplatform.v1.PredictRequestResponseLoggingConfig predict_request_response_logging_config = 18; `

**Returns**  
---  
**Type** | **Description**  
`[PredictRequestResponseLoggingConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictRequestResponseLoggingConfigOrBuilder)` |   
  
### getPrivateModelServerEnabled()
    
    
    public boolean getPrivateModelServerEnabled()

If true, the model server will be isolated from the external internet.

`bool private_model_server_enabled = 30;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The privateModelServerEnabled.  
  
### getPrivateServiceConnectConfig()
    
    
    public PrivateServiceConnectConfig getPrivateServiceConnectConfig()

Optional. Configuration for private service connect.

network and private_service_connect_config are mutually exclusive.

` .google.cloud.aiplatform.v1.PrivateServiceConnectConfig private_service_connect_config = 21 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[PrivateServiceConnectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PrivateServiceConnectConfig)` | The privateServiceConnectConfig.  
  
### getPrivateServiceConnectConfigBuilder()
    
    
    public PrivateServiceConnectConfig.Builder getPrivateServiceConnectConfigBuilder()

Optional. Configuration for private service connect.

network and private_service_connect_config are mutually exclusive.

` .google.cloud.aiplatform.v1.PrivateServiceConnectConfig private_service_connect_config = 21 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[PrivateServiceConnectConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PrivateServiceConnectConfig.Builder)` |   
  
### getPrivateServiceConnectConfigOrBuilder()
    
    
    public PrivateServiceConnectConfigOrBuilder getPrivateServiceConnectConfigOrBuilder()

Optional. Configuration for private service connect.

network and private_service_connect_config are mutually exclusive.

` .google.cloud.aiplatform.v1.PrivateServiceConnectConfig private_service_connect_config = 21 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[PrivateServiceConnectConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PrivateServiceConnectConfigOrBuilder)` |   
  
### getSatisfiesPzi()
    
    
    public boolean getSatisfiesPzi()

Output only. Reserved for future use.

`bool satisfies_pzi = 28 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The satisfiesPzi.  
  
### getSatisfiesPzs()
    
    
    public boolean getSatisfiesPzs()

Output only. Reserved for future use.

`bool satisfies_pzs = 27 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The satisfiesPzs.  
  
### getTrafficSplit() (deprecated)
    
    
    public Map<String,Integer> getTrafficSplit()

Use [#getTrafficSplitMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder#com_google_cloud_aiplatform_v1_Endpoint_Builder_getTrafficSplitMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)>` |   
  
### getTrafficSplitCount()
    
    
    public int getTrafficSplitCount()

A map from a DeployedModel's ID to the percentage of this Endpoint's traffic that should be forwarded to that DeployedModel.

If a DeployedModel's ID is not listed in this map, then it receives no traffic.

The traffic percentage values must add up to 100, or map must be empty if the Endpoint is to not accept any traffic at a moment.

`map<string, int32> traffic_split = 5;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getTrafficSplitMap()
    
    
    public Map<String,Integer> getTrafficSplitMap()

A map from a DeployedModel's ID to the percentage of this Endpoint's traffic that should be forwarded to that DeployedModel.

If a DeployedModel's ID is not listed in this map, then it receives no traffic.

The traffic percentage values must add up to 100, or map must be empty if the Endpoint is to not accept any traffic at a moment.

`map<string, int32> traffic_split = 5;`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)>` |   
  
### getTrafficSplitOrDefault(String key, int defaultValue)
    
    
    public int getTrafficSplitOrDefault(String key, int defaultValue)

A map from a DeployedModel's ID to the percentage of this Endpoint's traffic that should be forwarded to that DeployedModel.

If a DeployedModel's ID is not listed in this map, then it receives no traffic.

The traffic percentage values must add up to 100, or map must be empty if the Endpoint is to not accept any traffic at a moment.

`map<string, int32> traffic_split = 5;`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getTrafficSplitOrThrow(String key)
    
    
    public int getTrafficSplitOrThrow(String key)

A map from a DeployedModel's ID to the percentage of this Endpoint's traffic that should be forwarded to that DeployedModel.

If a DeployedModel's ID is not listed in this map, then it receives no traffic.

The traffic percentage values must add up to 100, or map must be empty if the Endpoint is to not accept any traffic at a moment.

`map<string, int32> traffic_split = 5;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getUpdateTime()
    
    
    public Timestamp getUpdateTime()

Output only. Timestamp when this Endpoint was last updated.

` .google.protobuf.Timestamp update_time = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The updateTime.  
  
### getUpdateTimeBuilder()
    
    
    public Timestamp.Builder getUpdateTimeBuilder()

Output only. Timestamp when this Endpoint was last updated.

` .google.protobuf.Timestamp update_time = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)` |   
  
### getUpdateTimeOrBuilder()
    
    
    public TimestampOrBuilder getUpdateTimeOrBuilder()

Output only. Timestamp when this Endpoint was last updated.

` .google.protobuf.Timestamp update_time = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### hasClientConnectionConfig()
    
    
    public boolean hasClientConnectionConfig()

Configurations that are applied to the endpoint for online prediction.

`.google.cloud.aiplatform.v1.ClientConnectionConfig client_connection_config = 23; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the clientConnectionConfig field is set.  
  
### hasCreateTime()
    
    
    public boolean hasCreateTime()

Output only. Timestamp when this Endpoint was created.

` .google.protobuf.Timestamp create_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasEncryptionSpec()
    
    
    public boolean hasEncryptionSpec()

Customer-managed encryption key spec for an Endpoint. If set, this Endpoint and all sub-resources of this Endpoint will be secured by this key.

`.google.cloud.aiplatform.v1.EncryptionSpec encryption_spec = 10;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the encryptionSpec field is set.  
  
### hasGenAiAdvancedFeaturesConfig()
    
    
    public boolean hasGenAiAdvancedFeaturesConfig()

Optional. Configuration for GenAiAdvancedFeatures. If the endpoint is serving GenAI models, advanced features like native RAG integration can be configured. Currently, only Model Garden models are supported.

` .google.cloud.aiplatform.v1.GenAiAdvancedFeaturesConfig gen_ai_advanced_features_config = 29 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the genAiAdvancedFeaturesConfig field is set.  
  
### hasPredictRequestResponseLoggingConfig()
    
    
    public boolean hasPredictRequestResponseLoggingConfig()

Configures the request-response logging for online prediction.

` .google.cloud.aiplatform.v1.PredictRequestResponseLoggingConfig predict_request_response_logging_config = 18; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the predictRequestResponseLoggingConfig field is set.  
  
### hasPrivateServiceConnectConfig()
    
    
    public boolean hasPrivateServiceConnectConfig()

Optional. Configuration for private service connect.

network and private_service_connect_config are mutually exclusive.

` .google.cloud.aiplatform.v1.PrivateServiceConnectConfig private_service_connect_config = 21 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the privateServiceConnectConfig field is set.  
  
### hasUpdateTime()
    
    
    public boolean hasUpdateTime()

Output only. Timestamp when this Endpoint was last updated.

` .google.protobuf.Timestamp update_time = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the updateTime field is set.  
  
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

### mergeClientConnectionConfig(ClientConnectionConfig value)
    
    
    public Endpoint.Builder mergeClientConnectionConfig(ClientConnectionConfig value)

Configurations that are applied to the endpoint for online prediction.

`.google.cloud.aiplatform.v1.ClientConnectionConfig client_connection_config = 23; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ClientConnectionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ClientConnectionConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` |   
  
### mergeCreateTime(Timestamp value)
    
    
    public Endpoint.Builder mergeCreateTime(Timestamp value)

Output only. Timestamp when this Endpoint was created.

` .google.protobuf.Timestamp create_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` |   
  
### mergeEncryptionSpec(EncryptionSpec value)
    
    
    public Endpoint.Builder mergeEncryptionSpec(EncryptionSpec value)

Customer-managed encryption key spec for an Endpoint. If set, this Endpoint and all sub-resources of this Endpoint will be secured by this key.

`.google.cloud.aiplatform.v1.EncryptionSpec encryption_spec = 10;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[EncryptionSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EncryptionSpec)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` |   
  
### mergeFrom(Endpoint other)
    
    
    public Endpoint.Builder mergeFrom(Endpoint other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Endpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public Endpoint.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public Endpoint.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### mergeGenAiAdvancedFeaturesConfig(GenAiAdvancedFeaturesConfig value)
    
    
    public Endpoint.Builder mergeGenAiAdvancedFeaturesConfig(GenAiAdvancedFeaturesConfig value)

Optional. Configuration for GenAiAdvancedFeatures. If the endpoint is serving GenAI models, advanced features like native RAG integration can be configured. Currently, only Model Garden models are supported.

` .google.cloud.aiplatform.v1.GenAiAdvancedFeaturesConfig gen_ai_advanced_features_config = 29 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[GenAiAdvancedFeaturesConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GenAiAdvancedFeaturesConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` |   
  
### mergePredictRequestResponseLoggingConfig(PredictRequestResponseLoggingConfig value)
    
    
    public Endpoint.Builder mergePredictRequestResponseLoggingConfig(PredictRequestResponseLoggingConfig value)

Configures the request-response logging for online prediction.

` .google.cloud.aiplatform.v1.PredictRequestResponseLoggingConfig predict_request_response_logging_config = 18; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[PredictRequestResponseLoggingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictRequestResponseLoggingConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` |   
  
### mergePrivateServiceConnectConfig(PrivateServiceConnectConfig value)
    
    
    public Endpoint.Builder mergePrivateServiceConnectConfig(PrivateServiceConnectConfig value)

Optional. Configuration for private service connect.

network and private_service_connect_config are mutually exclusive.

` .google.cloud.aiplatform.v1.PrivateServiceConnectConfig private_service_connect_config = 21 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[PrivateServiceConnectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PrivateServiceConnectConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` |   
  
### mergeUpdateTime(Timestamp value)
    
    
    public Endpoint.Builder mergeUpdateTime(Timestamp value)

Output only. Timestamp when this Endpoint was last updated.

` .google.protobuf.Timestamp update_time = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` |   
  
### putAllLabels(Map<String,String> values)
    
    
    public Endpoint.Builder putAllLabels(Map<String,String> values)

The labels with user-defined metadata to organize your Endpoints.

Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed.

See <https://goo.gl/xmQnxf> for more information and examples of labels.

`map<string, string> labels = 7;`

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` |   
  
### putAllTrafficSplit(Map<String,Integer> values)
    
    
    public Endpoint.Builder putAllTrafficSplit(Map<String,Integer> values)

A map from a DeployedModel's ID to the percentage of this Endpoint's traffic that should be forwarded to that DeployedModel.

If a DeployedModel's ID is not listed in this map, then it receives no traffic.

The traffic percentage values must add up to 100, or map must be empty if the Endpoint is to not accept any traffic at a moment.

`map<string, int32> traffic_split = 5;`

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` |   
  
### putLabels(String key, String value)
    
    
    public Endpoint.Builder putLabels(String key, String value)

The labels with user-defined metadata to organize your Endpoints.

Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed.

See <https://goo.gl/xmQnxf> for more information and examples of labels.

`map<string, string> labels = 7;`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` |   
  
### putTrafficSplit(String key, int value)
    
    
    public Endpoint.Builder putTrafficSplit(String key, int value)

A map from a DeployedModel's ID to the percentage of this Endpoint's traffic that should be forwarded to that DeployedModel.

If a DeployedModel's ID is not listed in this map, then it receives no traffic.

The traffic percentage values must add up to 100, or map must be empty if the Endpoint is to not accept any traffic at a moment.

`map<string, int32> traffic_split = 5;`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` |   
  
### removeDeployedModels(int index)
    
    
    public Endpoint.Builder removeDeployedModels(int index)

Output only. The models deployed in this Endpoint. To add or remove DeployedModels use EndpointService.DeployModel and EndpointService.UndeployModel respectively.

` repeated .google.cloud.aiplatform.v1.DeployedModel deployed_models = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` |   
  
### removeLabels(String key)
    
    
    public Endpoint.Builder removeLabels(String key)

The labels with user-defined metadata to organize your Endpoints.

Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed.

See <https://goo.gl/xmQnxf> for more information and examples of labels.

`map<string, string> labels = 7;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` |   
  
### removeTrafficSplit(String key)
    
    
    public Endpoint.Builder removeTrafficSplit(String key)

A map from a DeployedModel's ID to the percentage of this Endpoint's traffic that should be forwarded to that DeployedModel.

If a DeployedModel's ID is not listed in this map, then it receives no traffic.

The traffic percentage values must add up to 100, or map must be empty if the Endpoint is to not accept any traffic at a moment.

`map<string, int32> traffic_split = 5;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` |   
  
### setClientConnectionConfig(ClientConnectionConfig value)
    
    
    public Endpoint.Builder setClientConnectionConfig(ClientConnectionConfig value)

Configurations that are applied to the endpoint for online prediction.

`.google.cloud.aiplatform.v1.ClientConnectionConfig client_connection_config = 23; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ClientConnectionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ClientConnectionConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` |   
  
### setClientConnectionConfig(ClientConnectionConfig.Builder builderForValue)
    
    
    public Endpoint.Builder setClientConnectionConfig(ClientConnectionConfig.Builder builderForValue)

Configurations that are applied to the endpoint for online prediction.

`.google.cloud.aiplatform.v1.ClientConnectionConfig client_connection_config = 23; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[ClientConnectionConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ClientConnectionConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` |   
  
### setCreateTime(Timestamp value)
    
    
    public Endpoint.Builder setCreateTime(Timestamp value)

Output only. Timestamp when this Endpoint was created.

` .google.protobuf.Timestamp create_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` |   
  
### setCreateTime(Timestamp.Builder builderForValue)
    
    
    public Endpoint.Builder setCreateTime(Timestamp.Builder builderForValue)

Output only. Timestamp when this Endpoint was created.

` .google.protobuf.Timestamp create_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` |   
  
### setDedicatedEndpointDns(String value)
    
    
    public Endpoint.Builder setDedicatedEndpointDns(String value)

Output only. DNS of the dedicated endpoint. Will only be populated if dedicated_endpoint_enabled is true. Depending on the features enabled, uid might be a random number or a string. For example, if fast_tryout is enabled, uid will be fasttryout. Format: `https://{endpoint_id}.{region}-{uid}.prediction.vertexai.goog`.

`string dedicated_endpoint_dns = 25 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The dedicatedEndpointDns to set.  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` | This builder for chaining.  
  
### setDedicatedEndpointDnsBytes(ByteString value)
    
    
    public Endpoint.Builder setDedicatedEndpointDnsBytes(ByteString value)

Output only. DNS of the dedicated endpoint. Will only be populated if dedicated_endpoint_enabled is true. Depending on the features enabled, uid might be a random number or a string. For example, if fast_tryout is enabled, uid will be fasttryout. Format: `https://{endpoint_id}.{region}-{uid}.prediction.vertexai.goog`.

`string dedicated_endpoint_dns = 25 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for dedicatedEndpointDns to set.  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` | This builder for chaining.  
  
### setDedicatedEndpointEnabled(boolean value)
    
    
    public Endpoint.Builder setDedicatedEndpointEnabled(boolean value)

If true, the endpoint will be exposed through a dedicated DNS [Endpoint.dedicated_endpoint_dns]. Your request to the dedicated DNS will be isolated from other users' traffic and will have better performance and reliability. Note: Once you enabled dedicated endpoint, you won't be able to send request to the shared DNS {region}-aiplatform.googleapis.com. The limitation will be removed soon.

`bool dedicated_endpoint_enabled = 24;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The dedicatedEndpointEnabled to set.  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` | This builder for chaining.  
  
### setDeployedModels(int index, DeployedModel value)
    
    
    public Endpoint.Builder setDeployedModels(int index, DeployedModel value)

Output only. The models deployed in this Endpoint. To add or remove DeployedModels use EndpointService.DeployModel and EndpointService.UndeployModel respectively.

` repeated .google.cloud.aiplatform.v1.DeployedModel deployed_models = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[DeployedModel](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployedModel)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` |   
  
### setDeployedModels(int index, DeployedModel.Builder builderForValue)
    
    
    public Endpoint.Builder setDeployedModels(int index, DeployedModel.Builder builderForValue)

Output only. The models deployed in this Endpoint. To add or remove DeployedModels use EndpointService.DeployModel and EndpointService.UndeployModel respectively.

` repeated .google.cloud.aiplatform.v1.DeployedModel deployed_models = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[DeployedModel.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployedModel.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` |   
  
### setDescription(String value)
    
    
    public Endpoint.Builder setDescription(String value)

The description of the Endpoint.

`string description = 3;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The description to set.  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` | This builder for chaining.  
  
### setDescriptionBytes(ByteString value)
    
    
    public Endpoint.Builder setDescriptionBytes(ByteString value)

The description of the Endpoint.

`string description = 3;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for description to set.  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` | This builder for chaining.  
  
### setDisplayName(String value)
    
    
    public Endpoint.Builder setDisplayName(String value)

Required. The display name of the Endpoint. The name can be up to 128 characters long and can consist of any UTF-8 characters.

`string display_name = 2 [(.google.api.field_behavior) = REQUIRED];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The displayName to set.  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` | This builder for chaining.  
  
### setDisplayNameBytes(ByteString value)
    
    
    public Endpoint.Builder setDisplayNameBytes(ByteString value)

Required. The display name of the Endpoint. The name can be up to 128 characters long and can consist of any UTF-8 characters.

`string display_name = 2 [(.google.api.field_behavior) = REQUIRED];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for displayName to set.  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` | This builder for chaining.  
  
### setEnablePrivateServiceConnect(boolean value) (deprecated)
    
    
    public Endpoint.Builder setEnablePrivateServiceConnect(boolean value)

**Deprecated.** _google.cloud.aiplatform.v1.Endpoint.enable_private_service_connect is deprecated. See google/cloud/aiplatform/v1/endpoint.proto;l=128_

Deprecated: If true, expose the Endpoint via private service connect.

Only one of the fields, network or enable_private_service_connect, can be set.

`bool enable_private_service_connect = 17 [deprecated = true];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The enablePrivateServiceConnect to set.  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` | This builder for chaining.  
  
### setEncryptionSpec(EncryptionSpec value)
    
    
    public Endpoint.Builder setEncryptionSpec(EncryptionSpec value)

Customer-managed encryption key spec for an Endpoint. If set, this Endpoint and all sub-resources of this Endpoint will be secured by this key.

`.google.cloud.aiplatform.v1.EncryptionSpec encryption_spec = 10;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[EncryptionSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EncryptionSpec)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` |   
  
### setEncryptionSpec(EncryptionSpec.Builder builderForValue)
    
    
    public Endpoint.Builder setEncryptionSpec(EncryptionSpec.Builder builderForValue)

Customer-managed encryption key spec for an Endpoint. If set, this Endpoint and all sub-resources of this Endpoint will be secured by this key.

`.google.cloud.aiplatform.v1.EncryptionSpec encryption_spec = 10;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[EncryptionSpec.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EncryptionSpec.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` |   
  
### setEtag(String value)
    
    
    public Endpoint.Builder setEtag(String value)

Used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens.

`string etag = 6;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The etag to set.  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` | This builder for chaining.  
  
### setEtagBytes(ByteString value)
    
    
    public Endpoint.Builder setEtagBytes(ByteString value)

Used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens.

`string etag = 6;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for etag to set.  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` | This builder for chaining.  
  
### setGenAiAdvancedFeaturesConfig(GenAiAdvancedFeaturesConfig value)
    
    
    public Endpoint.Builder setGenAiAdvancedFeaturesConfig(GenAiAdvancedFeaturesConfig value)

Optional. Configuration for GenAiAdvancedFeatures. If the endpoint is serving GenAI models, advanced features like native RAG integration can be configured. Currently, only Model Garden models are supported.

` .google.cloud.aiplatform.v1.GenAiAdvancedFeaturesConfig gen_ai_advanced_features_config = 29 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[GenAiAdvancedFeaturesConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GenAiAdvancedFeaturesConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` |   
  
### setGenAiAdvancedFeaturesConfig(GenAiAdvancedFeaturesConfig.Builder builderForValue)
    
    
    public Endpoint.Builder setGenAiAdvancedFeaturesConfig(GenAiAdvancedFeaturesConfig.Builder builderForValue)

Optional. Configuration for GenAiAdvancedFeatures. If the endpoint is serving GenAI models, advanced features like native RAG integration can be configured. Currently, only Model Garden models are supported.

` .google.cloud.aiplatform.v1.GenAiAdvancedFeaturesConfig gen_ai_advanced_features_config = 29 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[GenAiAdvancedFeaturesConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GenAiAdvancedFeaturesConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` |   
  
### setModelDeploymentMonitoringJob(String value)
    
    
    public Endpoint.Builder setModelDeploymentMonitoringJob(String value)

Output only. Resource name of the Model Monitoring job associated with this Endpoint if monitoring is enabled by JobService.CreateModelDeploymentMonitoringJob. Format: `projects/{project}/locations/{location}/modelDeploymentMonitoringJobs/{model_deployment_monitoring_job}`

` string model_deployment_monitoring_job = 14 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The modelDeploymentMonitoringJob to set.  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` | This builder for chaining.  
  
### setModelDeploymentMonitoringJobBytes(ByteString value)
    
    
    public Endpoint.Builder setModelDeploymentMonitoringJobBytes(ByteString value)

Output only. Resource name of the Model Monitoring job associated with this Endpoint if monitoring is enabled by JobService.CreateModelDeploymentMonitoringJob. Format: `projects/{project}/locations/{location}/modelDeploymentMonitoringJobs/{model_deployment_monitoring_job}`

` string model_deployment_monitoring_job = 14 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for modelDeploymentMonitoringJob to set.  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` | This builder for chaining.  
  
### setName(String value)
    
    
    public Endpoint.Builder setName(String value)

Output only. The resource name of the Endpoint.

`string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name to set.  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` | This builder for chaining.  
  
### setNameBytes(ByteString value)
    
    
    public Endpoint.Builder setNameBytes(ByteString value)

Output only. The resource name of the Endpoint.

`string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for name to set.  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` | This builder for chaining.  
  
### setNetwork(String value)
    
    
    public Endpoint.Builder setNetwork(String value)

Optional. The full name of the Google Compute Engine [network](https://cloud.google.com//compute/docs/networks-and-firewalls#networks) to which the Endpoint should be peered.

Private services access must already be configured for the network. If left unspecified, the Endpoint is not peered with any network.

Only one of the fields, network or enable_private_service_connect, can be set.

[Format](https://cloud.google.com/compute/docs/reference/rest/v1/networks/insert): `projects/{project}/global/networks/{network}`. Where `{project}` is a project number, as in `12345`, and `{network}` is network name.

` string network = 13 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The network to set.  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` | This builder for chaining.  
  
### setNetworkBytes(ByteString value)
    
    
    public Endpoint.Builder setNetworkBytes(ByteString value)

Optional. The full name of the Google Compute Engine [network](https://cloud.google.com//compute/docs/networks-and-firewalls#networks) to which the Endpoint should be peered.

Private services access must already be configured for the network. If left unspecified, the Endpoint is not peered with any network.

Only one of the fields, network or enable_private_service_connect, can be set.

[Format](https://cloud.google.com/compute/docs/reference/rest/v1/networks/insert): `projects/{project}/global/networks/{network}`. Where `{project}` is a project number, as in `12345`, and `{network}` is network name.

` string network = 13 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for network to set.  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` | This builder for chaining.  
  
### setPredictRequestResponseLoggingConfig(PredictRequestResponseLoggingConfig value)
    
    
    public Endpoint.Builder setPredictRequestResponseLoggingConfig(PredictRequestResponseLoggingConfig value)

Configures the request-response logging for online prediction.

` .google.cloud.aiplatform.v1.PredictRequestResponseLoggingConfig predict_request_response_logging_config = 18; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[PredictRequestResponseLoggingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictRequestResponseLoggingConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` |   
  
### setPredictRequestResponseLoggingConfig(PredictRequestResponseLoggingConfig.Builder builderForValue)
    
    
    public Endpoint.Builder setPredictRequestResponseLoggingConfig(PredictRequestResponseLoggingConfig.Builder builderForValue)

Configures the request-response logging for online prediction.

` .google.cloud.aiplatform.v1.PredictRequestResponseLoggingConfig predict_request_response_logging_config = 18; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[PredictRequestResponseLoggingConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictRequestResponseLoggingConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` |   
  
### setPrivateModelServerEnabled(boolean value)
    
    
    public Endpoint.Builder setPrivateModelServerEnabled(boolean value)

If true, the model server will be isolated from the external internet.

`bool private_model_server_enabled = 30;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The privateModelServerEnabled to set.  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` | This builder for chaining.  
  
### setPrivateServiceConnectConfig(PrivateServiceConnectConfig value)
    
    
    public Endpoint.Builder setPrivateServiceConnectConfig(PrivateServiceConnectConfig value)

Optional. Configuration for private service connect.

network and private_service_connect_config are mutually exclusive.

` .google.cloud.aiplatform.v1.PrivateServiceConnectConfig private_service_connect_config = 21 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[PrivateServiceConnectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PrivateServiceConnectConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` |   
  
### setPrivateServiceConnectConfig(PrivateServiceConnectConfig.Builder builderForValue)
    
    
    public Endpoint.Builder setPrivateServiceConnectConfig(PrivateServiceConnectConfig.Builder builderForValue)

Optional. Configuration for private service connect.

network and private_service_connect_config are mutually exclusive.

` .google.cloud.aiplatform.v1.PrivateServiceConnectConfig private_service_connect_config = 21 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[PrivateServiceConnectConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PrivateServiceConnectConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` |   
  
### setSatisfiesPzi(boolean value)
    
    
    public Endpoint.Builder setSatisfiesPzi(boolean value)

Output only. Reserved for future use.

`bool satisfies_pzi = 28 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The satisfiesPzi to set.  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` | This builder for chaining.  
  
### setSatisfiesPzs(boolean value)
    
    
    public Endpoint.Builder setSatisfiesPzs(boolean value)

Output only. Reserved for future use.

`bool satisfies_pzs = 27 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The satisfiesPzs to set.  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` | This builder for chaining.  
  
### setUpdateTime(Timestamp value)
    
    
    public Endpoint.Builder setUpdateTime(Timestamp value)

Output only. Timestamp when this Endpoint was last updated.

` .google.protobuf.Timestamp update_time = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` |   
  
### setUpdateTime(Timestamp.Builder builderForValue)
    
    
    public Endpoint.Builder setUpdateTime(Timestamp.Builder builderForValue)

Output only. Timestamp when this Endpoint was last updated.

` .google.protobuf.Timestamp update_time = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint.Builder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
