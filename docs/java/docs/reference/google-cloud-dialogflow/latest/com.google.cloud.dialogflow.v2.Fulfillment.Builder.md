---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Fulfillment.Builder
title: Class Fulfillment.Builder (4.105.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:50:46.620678+00:00
---

# Class Fulfillment.Builder (4.105.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Fulfillment.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class Fulfillment.Builder (4.105.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.105.0 (latest)  4.101.0  4.100.0  4.99.0  4.97.0  4.94.0  4.93.0  4.91.0  4.89.0  4.88.0  4.87.0  4.86.0  4.84.0  4.82.0  4.81.0  4.80.0  4.79.0  4.78.0  4.76.0  4.74.0  4.73.0  4.70.0  4.69.0  4.68.0  4.66.0  4.65.0  4.64.0  4.63.0  4.62.0  4.61.0  4.60.0  4.59.0  4.58.0  4.57.0  4.55.0  4.54.0  4.53.0  4.52.0  4.51.0  4.50.0  4.49.0  4.48.0  4.47.0  4.46.0  4.45.0  4.43.0  4.42.0  4.41.0  4.40.0  4.39.0  4.38.0  4.37.0  4.36.0  4.35.0  4.34.0  4.33.0  4.30.0  4.29.0  4.28.0  4.27.0  4.26.0  4.25.0  4.24.0  4.23.0  4.22.0  4.21.0  4.20.0  4.19.0  4.18.0  4.17.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.1  4.8.6  4.7.5  4.6.0  4.5.11  4.4.0  4.3.1 
    
    
    public static final class Fulfillment.Builder extends GeneratedMessage.Builder<Fulfillment.Builder> implements FulfillmentOrBuilder

By default, your agent responds to a matched intent with a static response. As an alternative, you can provide a more dynamic response by using fulfillment. When you enable fulfillment for an intent, Dialogflow responds to that intent by calling a service that you define. For example, if an end-user wants to schedule a haircut on Friday, your service can check your database and respond to the end-user with availability information for Friday.

For more information, see the [fulfillment guide](https://cloud.google.com/dialogflow/docs/fulfillment-overview).

Protobuf type `google.cloud.dialogflow.v2.Fulfillment`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > Fulfillment.Builder

## Implements

[FulfillmentOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.FulfillmentOrBuilder)

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

### addAllFeatures(Iterable<? extends Fulfillment.Feature> values)
    
    
    public Fulfillment.Builder addAllFeatures(Iterable<? extends Fulfillment.Feature> values)

Optional. The field defines whether the fulfillment is enabled for certain features.

` repeated .google.cloud.dialogflow.v2.Fulfillment.Feature features = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<? extends com.google.cloud.dialogflow.v2.Fulfillment.Feature>`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Fulfillment.Builder)` |   
  
### addFeatures(Fulfillment.Feature value)
    
    
    public Fulfillment.Builder addFeatures(Fulfillment.Feature value)

Optional. The field defines whether the fulfillment is enabled for certain features.

` repeated .google.cloud.dialogflow.v2.Fulfillment.Feature features = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Fulfillment.Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Fulfillment.Feature)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Fulfillment.Builder)` |   
  
### addFeatures(Fulfillment.Feature.Builder builderForValue)
    
    
    public Fulfillment.Builder addFeatures(Fulfillment.Feature.Builder builderForValue)

Optional. The field defines whether the fulfillment is enabled for certain features.

` repeated .google.cloud.dialogflow.v2.Fulfillment.Feature features = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Fulfillment.Feature.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Fulfillment.Feature.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Fulfillment.Builder)` |   
  
### addFeatures(int index, Fulfillment.Feature value)
    
    
    public Fulfillment.Builder addFeatures(int index, Fulfillment.Feature value)

Optional. The field defines whether the fulfillment is enabled for certain features.

` repeated .google.cloud.dialogflow.v2.Fulfillment.Feature features = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[Fulfillment.Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Fulfillment.Feature)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Fulfillment.Builder)` |   
  
### addFeatures(int index, Fulfillment.Feature.Builder builderForValue)
    
    
    public Fulfillment.Builder addFeatures(int index, Fulfillment.Feature.Builder builderForValue)

Optional. The field defines whether the fulfillment is enabled for certain features.

` repeated .google.cloud.dialogflow.v2.Fulfillment.Feature features = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[Fulfillment.Feature.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Fulfillment.Feature.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Fulfillment.Builder)` |   
  
### addFeaturesBuilder()
    
    
    public Fulfillment.Feature.Builder addFeaturesBuilder()

Optional. The field defines whether the fulfillment is enabled for certain features.

` repeated .google.cloud.dialogflow.v2.Fulfillment.Feature features = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Feature.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Fulfillment.Feature.Builder)` |   
  
### addFeaturesBuilder(int index)
    
    
    public Fulfillment.Feature.Builder addFeaturesBuilder(int index)

Optional. The field defines whether the fulfillment is enabled for certain features.

` repeated .google.cloud.dialogflow.v2.Fulfillment.Feature features = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Feature.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Fulfillment.Feature.Builder)` |   
  
### build()
    
    
    public Fulfillment build()

**Returns**  
---  
**Type** | **Description**  
`[Fulfillment](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Fulfillment)` |   
  
### buildPartial()
    
    
    public Fulfillment buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[Fulfillment](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Fulfillment)` |   
  
### clear()
    
    
    public Fulfillment.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Fulfillment.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearDisplayName()
    
    
    public Fulfillment.Builder clearDisplayName()

Optional. The human-readable name of the fulfillment, unique within the agent.

This field is not used for Fulfillment in an Environment.

`string display_name = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Fulfillment.Builder)` | This builder for chaining.  
  
### clearEnabled()
    
    
    public Fulfillment.Builder clearEnabled()

Optional. Whether fulfillment is enabled.

`bool enabled = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Fulfillment.Builder)` | This builder for chaining.  
  
### clearFeatures()
    
    
    public Fulfillment.Builder clearFeatures()

Optional. The field defines whether the fulfillment is enabled for certain features.

` repeated .google.cloud.dialogflow.v2.Fulfillment.Feature features = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Fulfillment.Builder)` |   
  
### clearFulfillment()
    
    
    public Fulfillment.Builder clearFulfillment()

**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Fulfillment.Builder)` |   
  
### clearGenericWebService()
    
    
    public Fulfillment.Builder clearGenericWebService()

Configuration for a generic web service.

`.google.cloud.dialogflow.v2.Fulfillment.GenericWebService generic_web_service = 3; `

**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Fulfillment.Builder)` |   
  
### clearName()
    
    
    public Fulfillment.Builder clearName()

Required. The unique identifier of the fulfillment. Supported formats:

  * `projects/<Project ID>/agent/fulfillment`
  * `projects/<Project ID>/locations/<Location ID>/agent/fulfillment`

This field is not used for Fulfillment in an Environment.




`string name = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Fulfillment.Builder)` | This builder for chaining.  
  
### getDefaultInstanceForType()
    
    
    public Fulfillment getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[Fulfillment](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Fulfillment)` |   
  
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

Optional. The human-readable name of the fulfillment, unique within the agent.

This field is not used for Fulfillment in an Environment.

`string display_name = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The displayName.  
  
### getDisplayNameBytes()
    
    
    public ByteString getDisplayNameBytes()

Optional. The human-readable name of the fulfillment, unique within the agent.

This field is not used for Fulfillment in an Environment.

`string display_name = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for displayName.  
  
### getEnabled()
    
    
    public boolean getEnabled()

Optional. Whether fulfillment is enabled.

`bool enabled = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enabled.  
  
### getFeatures(int index)
    
    
    public Fulfillment.Feature getFeatures(int index)

Optional. The field defines whether the fulfillment is enabled for certain features.

` repeated .google.cloud.dialogflow.v2.Fulfillment.Feature features = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Fulfillment.Feature)` |   
  
### getFeaturesBuilder(int index)
    
    
    public Fulfillment.Feature.Builder getFeaturesBuilder(int index)

Optional. The field defines whether the fulfillment is enabled for certain features.

` repeated .google.cloud.dialogflow.v2.Fulfillment.Feature features = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Feature.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Fulfillment.Feature.Builder)` |   
  
### getFeaturesBuilderList()
    
    
    public List<Fulfillment.Feature.Builder> getFeaturesBuilderList()

Optional. The field defines whether the fulfillment is enabled for certain features.

` repeated .google.cloud.dialogflow.v2.Fulfillment.Feature features = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Fulfillment.Feature.Builder)>` |   
  
### getFeaturesCount()
    
    
    public int getFeaturesCount()

Optional. The field defines whether the fulfillment is enabled for certain features.

` repeated .google.cloud.dialogflow.v2.Fulfillment.Feature features = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getFeaturesList()
    
    
    public List<Fulfillment.Feature> getFeaturesList()

Optional. The field defines whether the fulfillment is enabled for certain features.

` repeated .google.cloud.dialogflow.v2.Fulfillment.Feature features = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Fulfillment.Feature)>` |   
  
### getFeaturesOrBuilder(int index)
    
    
    public Fulfillment.FeatureOrBuilder getFeaturesOrBuilder(int index)

Optional. The field defines whether the fulfillment is enabled for certain features.

` repeated .google.cloud.dialogflow.v2.Fulfillment.Feature features = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.FeatureOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Fulfillment.FeatureOrBuilder)` |   
  
### getFeaturesOrBuilderList()
    
    
    public List<? extends Fulfillment.FeatureOrBuilder> getFeaturesOrBuilderList()

Optional. The field defines whether the fulfillment is enabled for certain features.

` repeated .google.cloud.dialogflow.v2.Fulfillment.Feature features = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.dialogflow.v2.Fulfillment.FeatureOrBuilder>` |   
  
### getFulfillmentCase()
    
    
    public Fulfillment.FulfillmentCase getFulfillmentCase()

**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.FulfillmentCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Fulfillment.FulfillmentCase)` |   
  
### getGenericWebService()
    
    
    public Fulfillment.GenericWebService getGenericWebService()

Configuration for a generic web service.

`.google.cloud.dialogflow.v2.Fulfillment.GenericWebService generic_web_service = 3; `

**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.GenericWebService](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Fulfillment.GenericWebService)` | The genericWebService.  
  
### getGenericWebServiceBuilder()
    
    
    public Fulfillment.GenericWebService.Builder getGenericWebServiceBuilder()

Configuration for a generic web service.

`.google.cloud.dialogflow.v2.Fulfillment.GenericWebService generic_web_service = 3; `

**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.GenericWebService.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Fulfillment.GenericWebService.Builder)` |   
  
### getGenericWebServiceOrBuilder()
    
    
    public Fulfillment.GenericWebServiceOrBuilder getGenericWebServiceOrBuilder()

Configuration for a generic web service.

`.google.cloud.dialogflow.v2.Fulfillment.GenericWebService generic_web_service = 3; `

**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.GenericWebServiceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Fulfillment.GenericWebServiceOrBuilder)` |   
  
### getName()
    
    
    public String getName()

Required. The unique identifier of the fulfillment. Supported formats:

  * `projects/<Project ID>/agent/fulfillment`
  * `projects/<Project ID>/locations/<Location ID>/agent/fulfillment`

This field is not used for Fulfillment in an Environment.




`string name = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public ByteString getNameBytes()

Required. The unique identifier of the fulfillment. Supported formats:

  * `projects/<Project ID>/agent/fulfillment`
  * `projects/<Project ID>/locations/<Location ID>/agent/fulfillment`

This field is not used for Fulfillment in an Environment.




`string name = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### hasGenericWebService()
    
    
    public boolean hasGenericWebService()

Configuration for a generic web service.

`.google.cloud.dialogflow.v2.Fulfillment.GenericWebService generic_web_service = 3; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the genericWebService field is set.  
  
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

### mergeFrom(Fulfillment other)
    
    
    public Fulfillment.Builder mergeFrom(Fulfillment other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Fulfillment](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Fulfillment)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Fulfillment.Builder)` |   
  
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
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Fulfillment.Builder)` |   
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
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Fulfillment.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### mergeGenericWebService(Fulfillment.GenericWebService value)
    
    
    public Fulfillment.Builder mergeGenericWebService(Fulfillment.GenericWebService value)

Configuration for a generic web service.

`.google.cloud.dialogflow.v2.Fulfillment.GenericWebService generic_web_service = 3; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Fulfillment.GenericWebService](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Fulfillment.GenericWebService)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Fulfillment.Builder)` |   
  
### removeFeatures(int index)
    
    
    public Fulfillment.Builder removeFeatures(int index)

Optional. The field defines whether the fulfillment is enabled for certain features.

` repeated .google.cloud.dialogflow.v2.Fulfillment.Feature features = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Fulfillment.Builder)` |   
  
### setDisplayName(String value)
    
    
    public Fulfillment.Builder setDisplayName(String value)

Optional. The human-readable name of the fulfillment, unique within the agent.

This field is not used for Fulfillment in an Environment.

`string display_name = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The displayName to set.  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Fulfillment.Builder)` | This builder for chaining.  
  
### setDisplayNameBytes(ByteString value)
    
    
    public Fulfillment.Builder setDisplayNameBytes(ByteString value)

Optional. The human-readable name of the fulfillment, unique within the agent.

This field is not used for Fulfillment in an Environment.

`string display_name = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for displayName to set.  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Fulfillment.Builder)` | This builder for chaining.  
  
### setEnabled(boolean value)
    
    
    public Fulfillment.Builder setEnabled(boolean value)

Optional. Whether fulfillment is enabled.

`bool enabled = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The enabled to set.  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Fulfillment.Builder)` | This builder for chaining.  
  
### setFeatures(int index, Fulfillment.Feature value)
    
    
    public Fulfillment.Builder setFeatures(int index, Fulfillment.Feature value)

Optional. The field defines whether the fulfillment is enabled for certain features.

` repeated .google.cloud.dialogflow.v2.Fulfillment.Feature features = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[Fulfillment.Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Fulfillment.Feature)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Fulfillment.Builder)` |   
  
### setFeatures(int index, Fulfillment.Feature.Builder builderForValue)
    
    
    public Fulfillment.Builder setFeatures(int index, Fulfillment.Feature.Builder builderForValue)

Optional. The field defines whether the fulfillment is enabled for certain features.

` repeated .google.cloud.dialogflow.v2.Fulfillment.Feature features = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[Fulfillment.Feature.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Fulfillment.Feature.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Fulfillment.Builder)` |   
  
### setGenericWebService(Fulfillment.GenericWebService value)
    
    
    public Fulfillment.Builder setGenericWebService(Fulfillment.GenericWebService value)

Configuration for a generic web service.

`.google.cloud.dialogflow.v2.Fulfillment.GenericWebService generic_web_service = 3; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Fulfillment.GenericWebService](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Fulfillment.GenericWebService)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Fulfillment.Builder)` |   
  
### setGenericWebService(Fulfillment.GenericWebService.Builder builderForValue)
    
    
    public Fulfillment.Builder setGenericWebService(Fulfillment.GenericWebService.Builder builderForValue)

Configuration for a generic web service.

`.google.cloud.dialogflow.v2.Fulfillment.GenericWebService generic_web_service = 3; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Fulfillment.GenericWebService.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Fulfillment.GenericWebService.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Fulfillment.Builder)` |   
  
### setName(String value)
    
    
    public Fulfillment.Builder setName(String value)

Required. The unique identifier of the fulfillment. Supported formats:

  * `projects/<Project ID>/agent/fulfillment`
  * `projects/<Project ID>/locations/<Location ID>/agent/fulfillment`

This field is not used for Fulfillment in an Environment.




`string name = 1 [(.google.api.field_behavior) = REQUIRED];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name to set.  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Fulfillment.Builder)` | This builder for chaining.  
  
### setNameBytes(ByteString value)
    
    
    public Fulfillment.Builder setNameBytes(ByteString value)

Required. The unique identifier of the fulfillment. Supported formats:

  * `projects/<Project ID>/agent/fulfillment`
  * `projects/<Project ID>/locations/<Location ID>/agent/fulfillment`

This field is not used for Fulfillment in an Environment.




`string name = 1 [(.google.api.field_behavior) = REQUIRED];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for name to set.  
**Returns**  
---  
**Type** | **Description**  
`[Fulfillment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Fulfillment.Builder)` | This builder for chaining.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
