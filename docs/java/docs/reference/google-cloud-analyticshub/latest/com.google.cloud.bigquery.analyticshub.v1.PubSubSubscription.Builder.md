---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder
title: Class PubSubSubscription.Builder (0.96.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:38:00.946514+00:00
---

# Class PubSubSubscription.Builder (0.96.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class PubSubSubscription.Builder (0.96.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.96.0 (latest)  0.92.0  0.91.0  0.90.0  0.88.0  0.85.0  0.84.0  0.82.0  0.80.0  0.79.0  0.78.0  0.77.0  0.75.0  0.73.0  0.72.0  0.71.0  0.70.0  0.69.0  0.67.0  0.65.0  0.64.0  0.61.0  0.60.0  0.59.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static final class PubSubSubscription.Builder extends GeneratedMessage.Builder<PubSubSubscription.Builder> implements PubSubSubscriptionOrBuilder

Defines the destination Pub/Sub subscription. If none of `push_config`, `bigquery_config`, `cloud_storage_config`, `pubsub_export_config`, or `pubsublite_export_config` is set, then the subscriber will pull and ack messages using API methods. At most one of these fields may be set.

Protobuf type `google.cloud.bigquery.analyticshub.v1.PubSubSubscription`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > PubSubSubscription.Builder

## Implements

[PubSubSubscriptionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscriptionOrBuilder)

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

### addAllMessageTransforms(Iterable<? extends MessageTransform> values)
    
    
    public PubSubSubscription.Builder addAllMessageTransforms(Iterable<? extends MessageTransform> values)

Optional. Transforms to be applied to messages before they are delivered to subscribers. Transforms are applied in the order specified.

` repeated .google.cloud.bigquery.analyticshub.v1.MessageTransform message_transforms = 25 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<? extends com.google.cloud.bigquery.analyticshub.v1.MessageTransform>`  
  
**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` |   
  
### addMessageTransforms(MessageTransform value)
    
    
    public PubSubSubscription.Builder addMessageTransforms(MessageTransform value)

Optional. Transforms to be applied to messages before they are delivered to subscribers. Transforms are applied in the order specified.

` repeated .google.cloud.bigquery.analyticshub.v1.MessageTransform message_transforms = 25 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[MessageTransform](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.MessageTransform)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` |   
  
### addMessageTransforms(MessageTransform.Builder builderForValue)
    
    
    public PubSubSubscription.Builder addMessageTransforms(MessageTransform.Builder builderForValue)

Optional. Transforms to be applied to messages before they are delivered to subscribers. Transforms are applied in the order specified.

` repeated .google.cloud.bigquery.analyticshub.v1.MessageTransform message_transforms = 25 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[MessageTransform.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.MessageTransform.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` |   
  
### addMessageTransforms(int index, MessageTransform value)
    
    
    public PubSubSubscription.Builder addMessageTransforms(int index, MessageTransform value)

Optional. Transforms to be applied to messages before they are delivered to subscribers. Transforms are applied in the order specified.

` repeated .google.cloud.bigquery.analyticshub.v1.MessageTransform message_transforms = 25 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[MessageTransform](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.MessageTransform)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` |   
  
### addMessageTransforms(int index, MessageTransform.Builder builderForValue)
    
    
    public PubSubSubscription.Builder addMessageTransforms(int index, MessageTransform.Builder builderForValue)

Optional. Transforms to be applied to messages before they are delivered to subscribers. Transforms are applied in the order specified.

` repeated .google.cloud.bigquery.analyticshub.v1.MessageTransform message_transforms = 25 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[MessageTransform.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.MessageTransform.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` |   
  
### addMessageTransformsBuilder()
    
    
    public MessageTransform.Builder addMessageTransformsBuilder()

Optional. Transforms to be applied to messages before they are delivered to subscribers. Transforms are applied in the order specified.

` repeated .google.cloud.bigquery.analyticshub.v1.MessageTransform message_transforms = 25 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[MessageTransform.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.MessageTransform.Builder)` |   
  
### addMessageTransformsBuilder(int index)
    
    
    public MessageTransform.Builder addMessageTransformsBuilder(int index)

Optional. Transforms to be applied to messages before they are delivered to subscribers. Transforms are applied in the order specified.

` repeated .google.cloud.bigquery.analyticshub.v1.MessageTransform message_transforms = 25 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MessageTransform.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.MessageTransform.Builder)` |   
  
### build()
    
    
    public PubSubSubscription build()

**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription)` |   
  
### buildPartial()
    
    
    public PubSubSubscription buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription)` |   
  
### clear()
    
    
    public PubSubSubscription.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearAckDeadlineSeconds()
    
    
    public PubSubSubscription.Builder clearAckDeadlineSeconds()

Optional. The approximate amount of time (on a best-effort basis) Pub/Sub waits for the subscriber to acknowledge receipt before resending the message. In the interval after the message is delivered and before it is acknowledged, it is considered to be _outstanding_. During that time period, the message will not be redelivered (on a best-effort basis).

For pull subscriptions, this value is used as the initial value for the ack deadline. To override this value for a given message, call `ModifyAckDeadline` with the corresponding `ack_id` if using non-streaming pull or send the `ack_id` in a `StreamingModifyAckDeadlineRequest` if using streaming pull. The minimum custom deadline you can specify is 10 seconds. The maximum custom deadline you can specify is 600 seconds (10 minutes). If this parameter is 0, a default value of 10 seconds is used.

For push delivery, this value is also used to set the request timeout for the call to the push endpoint.

If the subscriber never acknowledges the message, the Pub/Sub system will eventually redeliver the message.

`int32 ack_deadline_seconds = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` | This builder for chaining.  
  
### clearBigqueryConfig()
    
    
    public PubSubSubscription.Builder clearBigqueryConfig()

Optional. If delivery to BigQuery is used with this subscription, this field is used to configure it.

` .google.cloud.bigquery.analyticshub.v1.BigQueryConfig bigquery_config = 18 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` |   
  
### clearCloudStorageConfig()
    
    
    public PubSubSubscription.Builder clearCloudStorageConfig()

Optional. If delivery to Google Cloud Storage is used with this subscription, this field is used to configure it.

` .google.cloud.bigquery.analyticshub.v1.CloudStorageConfig cloud_storage_config = 22 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` |   
  
### clearDeadLetterPolicy()
    
    
    public PubSubSubscription.Builder clearDeadLetterPolicy()

Optional. A policy that specifies the conditions for dead lettering messages in this subscription. If dead_letter_policy is not set, dead lettering is disabled.

The Pub/Sub service account associated with this subscriptions's parent project (i.e., service-{project_number}@gcp-sa-pubsub.iam.gserviceaccount.com) must have permission to Acknowledge() messages on this subscription.

` .google.cloud.bigquery.analyticshub.v1.DeadLetterPolicy dead_letter_policy = 13 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` |   
  
### clearDetached()
    
    
    public PubSubSubscription.Builder clearDetached()

Optional. Indicates whether the subscription is detached from its topic. Detached subscriptions don't receive messages from their topic and don't retain any backlog. `Pull` and `StreamingPull` requests will return FAILED_PRECONDITION. If the subscription is a push subscription, pushes to the endpoint will not be made.

`bool detached = 15 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` | This builder for chaining.  
  
### clearEnableExactlyOnceDelivery()
    
    
    public PubSubSubscription.Builder clearEnableExactlyOnceDelivery()

Optional. If true, Pub/Sub provides the following guarantees for the delivery of a message with a given value of `message_id` on this subscription:

  * The message sent to a subscriber is guaranteed not to be resent before the message's acknowledgement deadline expires.
  * An acknowledged message will not be resent to a subscriber.

Note that subscribers may still receive multiple copies of a message when `enable_exactly_once_delivery` is true if the message was published multiple times by a publisher client. These copies are considered distinct by Pub/Sub and have distinct `message_id` values.




`bool enable_exactly_once_delivery = 16 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` | This builder for chaining.  
  
### clearEnableMessageOrdering()
    
    
    public PubSubSubscription.Builder clearEnableMessageOrdering()

Optional. If true, messages published with the same `ordering_key` in `PubsubMessage` will be delivered to the subscribers in the order in which they are received by the Pub/Sub system. Otherwise, they may be delivered in any order.

`bool enable_message_ordering = 10 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` | This builder for chaining.  
  
### clearExpirationPolicy()
    
    
    public PubSubSubscription.Builder clearExpirationPolicy()

Optional. A policy that specifies the conditions for this subscription's expiration. A subscription is considered active as long as any connected subscriber is successfully consuming messages from the subscription or is issuing operations on the subscription. If `expiration_policy` is not set, a _default policy_ with `ttl` of 31 days will be used. The minimum allowed value for `expiration_policy.ttl` is 1 day. If `expiration_policy` is set, but `expiration_policy.ttl` is not set, the subscription never expires.

` .google.cloud.bigquery.analyticshub.v1.ExpirationPolicy expiration_policy = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` |   
  
### clearFilter()
    
    
    public PubSubSubscription.Builder clearFilter()

Optional. An expression written in the Pub/Sub [filter language](https://cloud.google.com/pubsub/docs/filtering). If non-empty, then only `PubsubMessage`s whose `attributes` field matches the filter are delivered on this subscription. If empty, then no messages are filtered out.

`string filter = 12 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` | This builder for chaining.  
  
### clearLabels()
    
    
    public PubSubSubscription.Builder clearLabels()

**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` |   
  
### clearMessageRetentionDuration()
    
    
    public PubSubSubscription.Builder clearMessageRetentionDuration()

Optional. How long to retain unacknowledged messages in the subscription's backlog, from the moment a message is published. If `retain_acked_messages` is true, then this also configures the retention of acknowledged messages, and thus configures how far back in time a `Seek` can be done. Defaults to 7 days. Cannot be more than 31 days or less than 10 minutes.

` .google.protobuf.Duration message_retention_duration = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` |   
  
### clearMessageTransforms()
    
    
    public PubSubSubscription.Builder clearMessageTransforms()

Optional. Transforms to be applied to messages before they are delivered to subscribers. Transforms are applied in the order specified.

` repeated .google.cloud.bigquery.analyticshub.v1.MessageTransform message_transforms = 25 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` |   
  
### clearName()
    
    
    public PubSubSubscription.Builder clearName()

Required. Name of the subscription. Format is `projects/{project}/subscriptions/{sub}`.

`string name = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` | This builder for chaining.  
  
### clearPushConfig()
    
    
    public PubSubSubscription.Builder clearPushConfig()

Optional. If push delivery is used with this subscription, this field is used to configure it.

` .google.cloud.bigquery.analyticshub.v1.PushConfig push_config = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` |   
  
### clearRetainAckedMessages()
    
    
    public PubSubSubscription.Builder clearRetainAckedMessages()

Optional. Indicates whether to retain acknowledged messages. If true, then messages are not expunged from the subscription's backlog, even if they are acknowledged, until they fall out of the `message_retention_duration` window. This must be true if you would like to [`Seek` to a timestamp](https://cloud.google.com/pubsub/docs/replay-overview#seek_to_a_time) in the past to replay previously-acknowledged messages.

`bool retain_acked_messages = 7 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` | This builder for chaining.  
  
### clearRetryPolicy()
    
    
    public PubSubSubscription.Builder clearRetryPolicy()

Optional. A policy that specifies how Pub/Sub retries message delivery for this subscription.

If not set, the default retry policy is applied. This generally implies that messages will be retried as soon as possible for healthy subscribers. RetryPolicy will be triggered on NACKs or acknowledgement deadline exceeded events for a given message.

` .google.cloud.bigquery.analyticshub.v1.RetryPolicy retry_policy = 14 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` |   
  
### clearTags()
    
    
    public PubSubSubscription.Builder clearTags()

**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` |   
  
### containsLabels(String key)
    
    
    public boolean containsLabels(String key)

Optional. See [Creating and managing labels](https://cloud.google.com/pubsub/docs/labels).

`map<string, string> labels = 9 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### containsTags(String key)
    
    
    public boolean containsTags(String key)

Optional. Input only. Immutable. Tag keys/values directly bound to this resource. For example: "123/environment": "production", "123/costCenter": "marketing"

` map<string, string> tags = 26 [(.google.api.field_behavior) = INPUT_ONLY, (.google.api.field_behavior) = IMMUTABLE, (.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAckDeadlineSeconds()
    
    
    public int getAckDeadlineSeconds()

Optional. The approximate amount of time (on a best-effort basis) Pub/Sub waits for the subscriber to acknowledge receipt before resending the message. In the interval after the message is delivered and before it is acknowledged, it is considered to be _outstanding_. During that time period, the message will not be redelivered (on a best-effort basis).

For pull subscriptions, this value is used as the initial value for the ack deadline. To override this value for a given message, call `ModifyAckDeadline` with the corresponding `ack_id` if using non-streaming pull or send the `ack_id` in a `StreamingModifyAckDeadlineRequest` if using streaming pull. The minimum custom deadline you can specify is 10 seconds. The maximum custom deadline you can specify is 600 seconds (10 minutes). If this parameter is 0, a default value of 10 seconds is used.

For push delivery, this value is also used to set the request timeout for the call to the push endpoint.

If the subscriber never acknowledges the message, the Pub/Sub system will eventually redeliver the message.

`int32 ack_deadline_seconds = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The ackDeadlineSeconds.  
  
### getBigqueryConfig()
    
    
    public BigQueryConfig getBigqueryConfig()

Optional. If delivery to BigQuery is used with this subscription, this field is used to configure it.

` .google.cloud.bigquery.analyticshub.v1.BigQueryConfig bigquery_config = 18 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[BigQueryConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.BigQueryConfig)` | The bigqueryConfig.  
  
### getBigqueryConfigBuilder()
    
    
    public BigQueryConfig.Builder getBigqueryConfigBuilder()

Optional. If delivery to BigQuery is used with this subscription, this field is used to configure it.

` .google.cloud.bigquery.analyticshub.v1.BigQueryConfig bigquery_config = 18 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[BigQueryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.BigQueryConfig.Builder)` |   
  
### getBigqueryConfigOrBuilder()
    
    
    public BigQueryConfigOrBuilder getBigqueryConfigOrBuilder()

Optional. If delivery to BigQuery is used with this subscription, this field is used to configure it.

` .google.cloud.bigquery.analyticshub.v1.BigQueryConfig bigquery_config = 18 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[BigQueryConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.BigQueryConfigOrBuilder)` |   
  
### getCloudStorageConfig()
    
    
    public CloudStorageConfig getCloudStorageConfig()

Optional. If delivery to Google Cloud Storage is used with this subscription, this field is used to configure it.

` .google.cloud.bigquery.analyticshub.v1.CloudStorageConfig cloud_storage_config = 22 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[CloudStorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.CloudStorageConfig)` | The cloudStorageConfig.  
  
### getCloudStorageConfigBuilder()
    
    
    public CloudStorageConfig.Builder getCloudStorageConfigBuilder()

Optional. If delivery to Google Cloud Storage is used with this subscription, this field is used to configure it.

` .google.cloud.bigquery.analyticshub.v1.CloudStorageConfig cloud_storage_config = 22 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[CloudStorageConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.CloudStorageConfig.Builder)` |   
  
### getCloudStorageConfigOrBuilder()
    
    
    public CloudStorageConfigOrBuilder getCloudStorageConfigOrBuilder()

Optional. If delivery to Google Cloud Storage is used with this subscription, this field is used to configure it.

` .google.cloud.bigquery.analyticshub.v1.CloudStorageConfig cloud_storage_config = 22 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[CloudStorageConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.CloudStorageConfigOrBuilder)` |   
  
### getDeadLetterPolicy()
    
    
    public DeadLetterPolicy getDeadLetterPolicy()

Optional. A policy that specifies the conditions for dead lettering messages in this subscription. If dead_letter_policy is not set, dead lettering is disabled.

The Pub/Sub service account associated with this subscriptions's parent project (i.e., service-{project_number}@gcp-sa-pubsub.iam.gserviceaccount.com) must have permission to Acknowledge() messages on this subscription.

` .google.cloud.bigquery.analyticshub.v1.DeadLetterPolicy dead_letter_policy = 13 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[DeadLetterPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.DeadLetterPolicy)` | The deadLetterPolicy.  
  
### getDeadLetterPolicyBuilder()
    
    
    public DeadLetterPolicy.Builder getDeadLetterPolicyBuilder()

Optional. A policy that specifies the conditions for dead lettering messages in this subscription. If dead_letter_policy is not set, dead lettering is disabled.

The Pub/Sub service account associated with this subscriptions's parent project (i.e., service-{project_number}@gcp-sa-pubsub.iam.gserviceaccount.com) must have permission to Acknowledge() messages on this subscription.

` .google.cloud.bigquery.analyticshub.v1.DeadLetterPolicy dead_letter_policy = 13 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[DeadLetterPolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.DeadLetterPolicy.Builder)` |   
  
### getDeadLetterPolicyOrBuilder()
    
    
    public DeadLetterPolicyOrBuilder getDeadLetterPolicyOrBuilder()

Optional. A policy that specifies the conditions for dead lettering messages in this subscription. If dead_letter_policy is not set, dead lettering is disabled.

The Pub/Sub service account associated with this subscriptions's parent project (i.e., service-{project_number}@gcp-sa-pubsub.iam.gserviceaccount.com) must have permission to Acknowledge() messages on this subscription.

` .google.cloud.bigquery.analyticshub.v1.DeadLetterPolicy dead_letter_policy = 13 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[DeadLetterPolicyOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.DeadLetterPolicyOrBuilder)` |   
  
### getDefaultInstanceForType()
    
    
    public PubSubSubscription getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription)` |   
  
### getDescriptorForType()
    
    
    public Descriptors.Descriptor getDescriptorForType()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getDescriptorForType__)

### getDetached()
    
    
    public boolean getDetached()

Optional. Indicates whether the subscription is detached from its topic. Detached subscriptions don't receive messages from their topic and don't retain any backlog. `Pull` and `StreamingPull` requests will return FAILED_PRECONDITION. If the subscription is a push subscription, pushes to the endpoint will not be made.

`bool detached = 15 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The detached.  
  
### getEnableExactlyOnceDelivery()
    
    
    public boolean getEnableExactlyOnceDelivery()

Optional. If true, Pub/Sub provides the following guarantees for the delivery of a message with a given value of `message_id` on this subscription:

  * The message sent to a subscriber is guaranteed not to be resent before the message's acknowledgement deadline expires.
  * An acknowledged message will not be resent to a subscriber.

Note that subscribers may still receive multiple copies of a message when `enable_exactly_once_delivery` is true if the message was published multiple times by a publisher client. These copies are considered distinct by Pub/Sub and have distinct `message_id` values.




`bool enable_exactly_once_delivery = 16 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enableExactlyOnceDelivery.  
  
### getEnableMessageOrdering()
    
    
    public boolean getEnableMessageOrdering()

Optional. If true, messages published with the same `ordering_key` in `PubsubMessage` will be delivered to the subscribers in the order in which they are received by the Pub/Sub system. Otherwise, they may be delivered in any order.

`bool enable_message_ordering = 10 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enableMessageOrdering.  
  
### getExpirationPolicy()
    
    
    public ExpirationPolicy getExpirationPolicy()

Optional. A policy that specifies the conditions for this subscription's expiration. A subscription is considered active as long as any connected subscriber is successfully consuming messages from the subscription or is issuing operations on the subscription. If `expiration_policy` is not set, a _default policy_ with `ttl` of 31 days will be used. The minimum allowed value for `expiration_policy.ttl` is 1 day. If `expiration_policy` is set, but `expiration_policy.ttl` is not set, the subscription never expires.

` .google.cloud.bigquery.analyticshub.v1.ExpirationPolicy expiration_policy = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ExpirationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.ExpirationPolicy)` | The expirationPolicy.  
  
### getExpirationPolicyBuilder()
    
    
    public ExpirationPolicy.Builder getExpirationPolicyBuilder()

Optional. A policy that specifies the conditions for this subscription's expiration. A subscription is considered active as long as any connected subscriber is successfully consuming messages from the subscription or is issuing operations on the subscription. If `expiration_policy` is not set, a _default policy_ with `ttl` of 31 days will be used. The minimum allowed value for `expiration_policy.ttl` is 1 day. If `expiration_policy` is set, but `expiration_policy.ttl` is not set, the subscription never expires.

` .google.cloud.bigquery.analyticshub.v1.ExpirationPolicy expiration_policy = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ExpirationPolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.ExpirationPolicy.Builder)` |   
  
### getExpirationPolicyOrBuilder()
    
    
    public ExpirationPolicyOrBuilder getExpirationPolicyOrBuilder()

Optional. A policy that specifies the conditions for this subscription's expiration. A subscription is considered active as long as any connected subscriber is successfully consuming messages from the subscription or is issuing operations on the subscription. If `expiration_policy` is not set, a _default policy_ with `ttl` of 31 days will be used. The minimum allowed value for `expiration_policy.ttl` is 1 day. If `expiration_policy` is set, but `expiration_policy.ttl` is not set, the subscription never expires.

` .google.cloud.bigquery.analyticshub.v1.ExpirationPolicy expiration_policy = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ExpirationPolicyOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.ExpirationPolicyOrBuilder)` |   
  
### getFilter()
    
    
    public String getFilter()

Optional. An expression written in the Pub/Sub [filter language](https://cloud.google.com/pubsub/docs/filtering). If non-empty, then only `PubsubMessage`s whose `attributes` field matches the filter are delivered on this subscription. If empty, then no messages are filtered out.

`string filter = 12 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The filter.  
  
### getFilterBytes()
    
    
    public ByteString getFilterBytes()

Optional. An expression written in the Pub/Sub [filter language](https://cloud.google.com/pubsub/docs/filtering). If non-empty, then only `PubsubMessage`s whose `attributes` field matches the filter are delivered on this subscription. If empty, then no messages are filtered out.

`string filter = 12 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for filter.  
  
### getLabels() (deprecated)
    
    
    public Map<String,String> getLabels()

Use [#getLabelsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder#com_google_cloud_bigquery_analyticshub_v1_PubSubSubscription_Builder_getLabelsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsCount()
    
    
    public int getLabelsCount()

Optional. See [Creating and managing labels](https://cloud.google.com/pubsub/docs/labels).

`map<string, string> labels = 9 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getLabelsMap()
    
    
    public Map<String,String> getLabelsMap()

Optional. See [Creating and managing labels](https://cloud.google.com/pubsub/docs/labels).

`map<string, string> labels = 9 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsOrDefault(String key, String defaultValue)
    
    
    public String getLabelsOrDefault(String key, String defaultValue)

Optional. See [Creating and managing labels](https://cloud.google.com/pubsub/docs/labels).

`map<string, string> labels = 9 [(.google.api.field_behavior) = OPTIONAL];`

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

Optional. See [Creating and managing labels](https://cloud.google.com/pubsub/docs/labels).

`map<string, string> labels = 9 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getMessageRetentionDuration()
    
    
    public Duration getMessageRetentionDuration()

Optional. How long to retain unacknowledged messages in the subscription's backlog, from the moment a message is published. If `retain_acked_messages` is true, then this also configures the retention of acknowledged messages, and thus configures how far back in time a `Seek` can be done. Defaults to 7 days. Cannot be more than 31 days or less than 10 minutes.

` .google.protobuf.Duration message_retention_duration = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)` | The messageRetentionDuration.  
  
### getMessageRetentionDurationBuilder()
    
    
    public Duration.Builder getMessageRetentionDurationBuilder()

Optional. How long to retain unacknowledged messages in the subscription's backlog, from the moment a message is published. If `retain_acked_messages` is true, then this also configures the retention of acknowledged messages, and thus configures how far back in time a `Seek` can be done. Defaults to 7 days. Cannot be more than 31 days or less than 10 minutes.

` .google.protobuf.Duration message_retention_duration = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.Builder.html)` |   
  
### getMessageRetentionDurationOrBuilder()
    
    
    public DurationOrBuilder getMessageRetentionDurationOrBuilder()

Optional. How long to retain unacknowledged messages in the subscription's backlog, from the moment a message is published. If `retain_acked_messages` is true, then this also configures the retention of acknowledged messages, and thus configures how far back in time a `Seek` can be done. Defaults to 7 days. Cannot be more than 31 days or less than 10 minutes.

` .google.protobuf.Duration message_retention_duration = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[DurationOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DurationOrBuilder.html)` |   
  
### getMessageTransforms(int index)
    
    
    public MessageTransform getMessageTransforms(int index)

Optional. Transforms to be applied to messages before they are delivered to subscribers. Transforms are applied in the order specified.

` repeated .google.cloud.bigquery.analyticshub.v1.MessageTransform message_transforms = 25 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MessageTransform](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.MessageTransform)` |   
  
### getMessageTransformsBuilder(int index)
    
    
    public MessageTransform.Builder getMessageTransformsBuilder(int index)

Optional. Transforms to be applied to messages before they are delivered to subscribers. Transforms are applied in the order specified.

` repeated .google.cloud.bigquery.analyticshub.v1.MessageTransform message_transforms = 25 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MessageTransform.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.MessageTransform.Builder)` |   
  
### getMessageTransformsBuilderList()
    
    
    public List<MessageTransform.Builder> getMessageTransformsBuilderList()

Optional. Transforms to be applied to messages before they are delivered to subscribers. Transforms are applied in the order specified.

` repeated .google.cloud.bigquery.analyticshub.v1.MessageTransform message_transforms = 25 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.MessageTransform.Builder)>` |   
  
### getMessageTransformsCount()
    
    
    public int getMessageTransformsCount()

Optional. Transforms to be applied to messages before they are delivered to subscribers. Transforms are applied in the order specified.

` repeated .google.cloud.bigquery.analyticshub.v1.MessageTransform message_transforms = 25 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getMessageTransformsList()
    
    
    public List<MessageTransform> getMessageTransformsList()

Optional. Transforms to be applied to messages before they are delivered to subscribers. Transforms are applied in the order specified.

` repeated .google.cloud.bigquery.analyticshub.v1.MessageTransform message_transforms = 25 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[MessageTransform](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.MessageTransform)>` |   
  
### getMessageTransformsOrBuilder(int index)
    
    
    public MessageTransformOrBuilder getMessageTransformsOrBuilder(int index)

Optional. Transforms to be applied to messages before they are delivered to subscribers. Transforms are applied in the order specified.

` repeated .google.cloud.bigquery.analyticshub.v1.MessageTransform message_transforms = 25 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MessageTransformOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.MessageTransformOrBuilder)` |   
  
### getMessageTransformsOrBuilderList()
    
    
    public List<? extends MessageTransformOrBuilder> getMessageTransformsOrBuilderList()

Optional. Transforms to be applied to messages before they are delivered to subscribers. Transforms are applied in the order specified.

` repeated .google.cloud.bigquery.analyticshub.v1.MessageTransform message_transforms = 25 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.bigquery.analyticshub.v1.MessageTransformOrBuilder>` |   
  
### getMutableLabels() (deprecated)
    
    
    public Map<String,String> getMutableLabels()

Use alternate mutation accessors instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getMutableTags() (deprecated)
    
    
    public Map<String,String> getMutableTags()

Use alternate mutation accessors instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getName()
    
    
    public String getName()

Required. Name of the subscription. Format is `projects/{project}/subscriptions/{sub}`.

`string name = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public ByteString getNameBytes()

Required. Name of the subscription. Format is `projects/{project}/subscriptions/{sub}`.

`string name = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getPushConfig()
    
    
    public PushConfig getPushConfig()

Optional. If push delivery is used with this subscription, this field is used to configure it.

` .google.cloud.bigquery.analyticshub.v1.PushConfig push_config = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[PushConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PushConfig)` | The pushConfig.  
  
### getPushConfigBuilder()
    
    
    public PushConfig.Builder getPushConfigBuilder()

Optional. If push delivery is used with this subscription, this field is used to configure it.

` .google.cloud.bigquery.analyticshub.v1.PushConfig push_config = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[PushConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PushConfig.Builder)` |   
  
### getPushConfigOrBuilder()
    
    
    public PushConfigOrBuilder getPushConfigOrBuilder()

Optional. If push delivery is used with this subscription, this field is used to configure it.

` .google.cloud.bigquery.analyticshub.v1.PushConfig push_config = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[PushConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PushConfigOrBuilder)` |   
  
### getRetainAckedMessages()
    
    
    public boolean getRetainAckedMessages()

Optional. Indicates whether to retain acknowledged messages. If true, then messages are not expunged from the subscription's backlog, even if they are acknowledged, until they fall out of the `message_retention_duration` window. This must be true if you would like to [`Seek` to a timestamp](https://cloud.google.com/pubsub/docs/replay-overview#seek_to_a_time) in the past to replay previously-acknowledged messages.

`bool retain_acked_messages = 7 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The retainAckedMessages.  
  
### getRetryPolicy()
    
    
    public RetryPolicy getRetryPolicy()

Optional. A policy that specifies how Pub/Sub retries message delivery for this subscription.

If not set, the default retry policy is applied. This generally implies that messages will be retried as soon as possible for healthy subscribers. RetryPolicy will be triggered on NACKs or acknowledgement deadline exceeded events for a given message.

` .google.cloud.bigquery.analyticshub.v1.RetryPolicy retry_policy = 14 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[RetryPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.RetryPolicy)` | The retryPolicy.  
  
### getRetryPolicyBuilder()
    
    
    public RetryPolicy.Builder getRetryPolicyBuilder()

Optional. A policy that specifies how Pub/Sub retries message delivery for this subscription.

If not set, the default retry policy is applied. This generally implies that messages will be retried as soon as possible for healthy subscribers. RetryPolicy will be triggered on NACKs or acknowledgement deadline exceeded events for a given message.

` .google.cloud.bigquery.analyticshub.v1.RetryPolicy retry_policy = 14 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[RetryPolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.RetryPolicy.Builder)` |   
  
### getRetryPolicyOrBuilder()
    
    
    public RetryPolicyOrBuilder getRetryPolicyOrBuilder()

Optional. A policy that specifies how Pub/Sub retries message delivery for this subscription.

If not set, the default retry policy is applied. This generally implies that messages will be retried as soon as possible for healthy subscribers. RetryPolicy will be triggered on NACKs or acknowledgement deadline exceeded events for a given message.

` .google.cloud.bigquery.analyticshub.v1.RetryPolicy retry_policy = 14 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[RetryPolicyOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.RetryPolicyOrBuilder)` |   
  
### getTags() (deprecated)
    
    
    public Map<String,String> getTags()

Use [#getTagsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder#com_google_cloud_bigquery_analyticshub_v1_PubSubSubscription_Builder_getTagsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getTagsCount()
    
    
    public int getTagsCount()

Optional. Input only. Immutable. Tag keys/values directly bound to this resource. For example: "123/environment": "production", "123/costCenter": "marketing"

` map<string, string> tags = 26 [(.google.api.field_behavior) = INPUT_ONLY, (.google.api.field_behavior) = IMMUTABLE, (.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getTagsMap()
    
    
    public Map<String,String> getTagsMap()

Optional. Input only. Immutable. Tag keys/values directly bound to this resource. For example: "123/environment": "production", "123/costCenter": "marketing"

` map<string, string> tags = 26 [(.google.api.field_behavior) = INPUT_ONLY, (.google.api.field_behavior) = IMMUTABLE, (.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getTagsOrDefault(String key, String defaultValue)
    
    
    public String getTagsOrDefault(String key, String defaultValue)

Optional. Input only. Immutable. Tag keys/values directly bound to this resource. For example: "123/environment": "production", "123/costCenter": "marketing"

` map<string, string> tags = 26 [(.google.api.field_behavior) = INPUT_ONLY, (.google.api.field_behavior) = IMMUTABLE, (.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getTagsOrThrow(String key)
    
    
    public String getTagsOrThrow(String key)

Optional. Input only. Immutable. Tag keys/values directly bound to this resource. For example: "123/environment": "production", "123/costCenter": "marketing"

` map<string, string> tags = 26 [(.google.api.field_behavior) = INPUT_ONLY, (.google.api.field_behavior) = IMMUTABLE, (.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### hasBigqueryConfig()
    
    
    public boolean hasBigqueryConfig()

Optional. If delivery to BigQuery is used with this subscription, this field is used to configure it.

` .google.cloud.bigquery.analyticshub.v1.BigQueryConfig bigquery_config = 18 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the bigqueryConfig field is set.  
  
### hasCloudStorageConfig()
    
    
    public boolean hasCloudStorageConfig()

Optional. If delivery to Google Cloud Storage is used with this subscription, this field is used to configure it.

` .google.cloud.bigquery.analyticshub.v1.CloudStorageConfig cloud_storage_config = 22 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the cloudStorageConfig field is set.  
  
### hasDeadLetterPolicy()
    
    
    public boolean hasDeadLetterPolicy()

Optional. A policy that specifies the conditions for dead lettering messages in this subscription. If dead_letter_policy is not set, dead lettering is disabled.

The Pub/Sub service account associated with this subscriptions's parent project (i.e., service-{project_number}@gcp-sa-pubsub.iam.gserviceaccount.com) must have permission to Acknowledge() messages on this subscription.

` .google.cloud.bigquery.analyticshub.v1.DeadLetterPolicy dead_letter_policy = 13 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the deadLetterPolicy field is set.  
  
### hasExpirationPolicy()
    
    
    public boolean hasExpirationPolicy()

Optional. A policy that specifies the conditions for this subscription's expiration. A subscription is considered active as long as any connected subscriber is successfully consuming messages from the subscription or is issuing operations on the subscription. If `expiration_policy` is not set, a _default policy_ with `ttl` of 31 days will be used. The minimum allowed value for `expiration_policy.ttl` is 1 day. If `expiration_policy` is set, but `expiration_policy.ttl` is not set, the subscription never expires.

` .google.cloud.bigquery.analyticshub.v1.ExpirationPolicy expiration_policy = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the expirationPolicy field is set.  
  
### hasMessageRetentionDuration()
    
    
    public boolean hasMessageRetentionDuration()

Optional. How long to retain unacknowledged messages in the subscription's backlog, from the moment a message is published. If `retain_acked_messages` is true, then this also configures the retention of acknowledged messages, and thus configures how far back in time a `Seek` can be done. Defaults to 7 days. Cannot be more than 31 days or less than 10 minutes.

` .google.protobuf.Duration message_retention_duration = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the messageRetentionDuration field is set.  
  
### hasPushConfig()
    
    
    public boolean hasPushConfig()

Optional. If push delivery is used with this subscription, this field is used to configure it.

` .google.cloud.bigquery.analyticshub.v1.PushConfig push_config = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the pushConfig field is set.  
  
### hasRetryPolicy()
    
    
    public boolean hasRetryPolicy()

Optional. A policy that specifies how Pub/Sub retries message delivery for this subscription.

If not set, the default retry policy is applied. This generally implies that messages will be retried as soon as possible for healthy subscribers. RetryPolicy will be triggered on NACKs or acknowledgement deadline exceeded events for a given message.

` .google.cloud.bigquery.analyticshub.v1.RetryPolicy retry_policy = 14 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the retryPolicy field is set.  
  
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

### mergeBigqueryConfig(BigQueryConfig value)
    
    
    public PubSubSubscription.Builder mergeBigqueryConfig(BigQueryConfig value)

Optional. If delivery to BigQuery is used with this subscription, this field is used to configure it.

` .google.cloud.bigquery.analyticshub.v1.BigQueryConfig bigquery_config = 18 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[BigQueryConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.BigQueryConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` |   
  
### mergeCloudStorageConfig(CloudStorageConfig value)
    
    
    public PubSubSubscription.Builder mergeCloudStorageConfig(CloudStorageConfig value)

Optional. If delivery to Google Cloud Storage is used with this subscription, this field is used to configure it.

` .google.cloud.bigquery.analyticshub.v1.CloudStorageConfig cloud_storage_config = 22 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[CloudStorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.CloudStorageConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` |   
  
### mergeDeadLetterPolicy(DeadLetterPolicy value)
    
    
    public PubSubSubscription.Builder mergeDeadLetterPolicy(DeadLetterPolicy value)

Optional. A policy that specifies the conditions for dead lettering messages in this subscription. If dead_letter_policy is not set, dead lettering is disabled.

The Pub/Sub service account associated with this subscriptions's parent project (i.e., service-{project_number}@gcp-sa-pubsub.iam.gserviceaccount.com) must have permission to Acknowledge() messages on this subscription.

` .google.cloud.bigquery.analyticshub.v1.DeadLetterPolicy dead_letter_policy = 13 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[DeadLetterPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.DeadLetterPolicy)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` |   
  
### mergeExpirationPolicy(ExpirationPolicy value)
    
    
    public PubSubSubscription.Builder mergeExpirationPolicy(ExpirationPolicy value)

Optional. A policy that specifies the conditions for this subscription's expiration. A subscription is considered active as long as any connected subscriber is successfully consuming messages from the subscription or is issuing operations on the subscription. If `expiration_policy` is not set, a _default policy_ with `ttl` of 31 days will be used. The minimum allowed value for `expiration_policy.ttl` is 1 day. If `expiration_policy` is set, but `expiration_policy.ttl` is not set, the subscription never expires.

` .google.cloud.bigquery.analyticshub.v1.ExpirationPolicy expiration_policy = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ExpirationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.ExpirationPolicy)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` |   
  
### mergeFrom(PubSubSubscription other)
    
    
    public PubSubSubscription.Builder mergeFrom(PubSubSubscription other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[PubSubSubscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public PubSubSubscription.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public PubSubSubscription.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### mergeMessageRetentionDuration(Duration value)
    
    
    public PubSubSubscription.Builder mergeMessageRetentionDuration(Duration value)

Optional. How long to retain unacknowledged messages in the subscription's backlog, from the moment a message is published. If `retain_acked_messages` is true, then this also configures the retention of acknowledged messages, and thus configures how far back in time a `Seek` can be done. Defaults to 7 days. Cannot be more than 31 days or less than 10 minutes.

` .google.protobuf.Duration message_retention_duration = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` |   
  
### mergePushConfig(PushConfig value)
    
    
    public PubSubSubscription.Builder mergePushConfig(PushConfig value)

Optional. If push delivery is used with this subscription, this field is used to configure it.

` .google.cloud.bigquery.analyticshub.v1.PushConfig push_config = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[PushConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PushConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` |   
  
### mergeRetryPolicy(RetryPolicy value)
    
    
    public PubSubSubscription.Builder mergeRetryPolicy(RetryPolicy value)

Optional. A policy that specifies how Pub/Sub retries message delivery for this subscription.

If not set, the default retry policy is applied. This generally implies that messages will be retried as soon as possible for healthy subscribers. RetryPolicy will be triggered on NACKs or acknowledgement deadline exceeded events for a given message.

` .google.cloud.bigquery.analyticshub.v1.RetryPolicy retry_policy = 14 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[RetryPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.RetryPolicy)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` |   
  
### putAllLabels(Map<String,String> values)
    
    
    public PubSubSubscription.Builder putAllLabels(Map<String,String> values)

Optional. See [Creating and managing labels](https://cloud.google.com/pubsub/docs/labels).

`map<string, string> labels = 9 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` |   
  
### putAllTags(Map<String,String> values)
    
    
    public PubSubSubscription.Builder putAllTags(Map<String,String> values)

Optional. Input only. Immutable. Tag keys/values directly bound to this resource. For example: "123/environment": "production", "123/costCenter": "marketing"

` map<string, string> tags = 26 [(.google.api.field_behavior) = INPUT_ONLY, (.google.api.field_behavior) = IMMUTABLE, (.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` |   
  
### putLabels(String key, String value)
    
    
    public PubSubSubscription.Builder putLabels(String key, String value)

Optional. See [Creating and managing labels](https://cloud.google.com/pubsub/docs/labels).

`map<string, string> labels = 9 [(.google.api.field_behavior) = OPTIONAL];`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` |   
  
### putTags(String key, String value)
    
    
    public PubSubSubscription.Builder putTags(String key, String value)

Optional. Input only. Immutable. Tag keys/values directly bound to this resource. For example: "123/environment": "production", "123/costCenter": "marketing"

` map<string, string> tags = 26 [(.google.api.field_behavior) = INPUT_ONLY, (.google.api.field_behavior) = IMMUTABLE, (.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` |   
  
### removeLabels(String key)
    
    
    public PubSubSubscription.Builder removeLabels(String key)

Optional. See [Creating and managing labels](https://cloud.google.com/pubsub/docs/labels).

`map<string, string> labels = 9 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` |   
  
### removeMessageTransforms(int index)
    
    
    public PubSubSubscription.Builder removeMessageTransforms(int index)

Optional. Transforms to be applied to messages before they are delivered to subscribers. Transforms are applied in the order specified.

` repeated .google.cloud.bigquery.analyticshub.v1.MessageTransform message_transforms = 25 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` |   
  
### removeTags(String key)
    
    
    public PubSubSubscription.Builder removeTags(String key)

Optional. Input only. Immutable. Tag keys/values directly bound to this resource. For example: "123/environment": "production", "123/costCenter": "marketing"

` map<string, string> tags = 26 [(.google.api.field_behavior) = INPUT_ONLY, (.google.api.field_behavior) = IMMUTABLE, (.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` |   
  
### setAckDeadlineSeconds(int value)
    
    
    public PubSubSubscription.Builder setAckDeadlineSeconds(int value)

Optional. The approximate amount of time (on a best-effort basis) Pub/Sub waits for the subscriber to acknowledge receipt before resending the message. In the interval after the message is delivered and before it is acknowledged, it is considered to be _outstanding_. During that time period, the message will not be redelivered (on a best-effort basis).

For pull subscriptions, this value is used as the initial value for the ack deadline. To override this value for a given message, call `ModifyAckDeadline` with the corresponding `ack_id` if using non-streaming pull or send the `ack_id` in a `StreamingModifyAckDeadlineRequest` if using streaming pull. The minimum custom deadline you can specify is 10 seconds. The maximum custom deadline you can specify is 600 seconds (10 minutes). If this parameter is 0, a default value of 10 seconds is used.

For push delivery, this value is also used to set the request timeout for the call to the push endpoint.

If the subscriber never acknowledges the message, the Pub/Sub system will eventually redeliver the message.

`int32 ack_deadline_seconds = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The ackDeadlineSeconds to set.  
**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` | This builder for chaining.  
  
### setBigqueryConfig(BigQueryConfig value)
    
    
    public PubSubSubscription.Builder setBigqueryConfig(BigQueryConfig value)

Optional. If delivery to BigQuery is used with this subscription, this field is used to configure it.

` .google.cloud.bigquery.analyticshub.v1.BigQueryConfig bigquery_config = 18 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[BigQueryConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.BigQueryConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` |   
  
### setBigqueryConfig(BigQueryConfig.Builder builderForValue)
    
    
    public PubSubSubscription.Builder setBigqueryConfig(BigQueryConfig.Builder builderForValue)

Optional. If delivery to BigQuery is used with this subscription, this field is used to configure it.

` .google.cloud.bigquery.analyticshub.v1.BigQueryConfig bigquery_config = 18 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[BigQueryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.BigQueryConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` |   
  
### setCloudStorageConfig(CloudStorageConfig value)
    
    
    public PubSubSubscription.Builder setCloudStorageConfig(CloudStorageConfig value)

Optional. If delivery to Google Cloud Storage is used with this subscription, this field is used to configure it.

` .google.cloud.bigquery.analyticshub.v1.CloudStorageConfig cloud_storage_config = 22 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[CloudStorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.CloudStorageConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` |   
  
### setCloudStorageConfig(CloudStorageConfig.Builder builderForValue)
    
    
    public PubSubSubscription.Builder setCloudStorageConfig(CloudStorageConfig.Builder builderForValue)

Optional. If delivery to Google Cloud Storage is used with this subscription, this field is used to configure it.

` .google.cloud.bigquery.analyticshub.v1.CloudStorageConfig cloud_storage_config = 22 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[CloudStorageConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.CloudStorageConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` |   
  
### setDeadLetterPolicy(DeadLetterPolicy value)
    
    
    public PubSubSubscription.Builder setDeadLetterPolicy(DeadLetterPolicy value)

Optional. A policy that specifies the conditions for dead lettering messages in this subscription. If dead_letter_policy is not set, dead lettering is disabled.

The Pub/Sub service account associated with this subscriptions's parent project (i.e., service-{project_number}@gcp-sa-pubsub.iam.gserviceaccount.com) must have permission to Acknowledge() messages on this subscription.

` .google.cloud.bigquery.analyticshub.v1.DeadLetterPolicy dead_letter_policy = 13 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[DeadLetterPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.DeadLetterPolicy)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` |   
  
### setDeadLetterPolicy(DeadLetterPolicy.Builder builderForValue)
    
    
    public PubSubSubscription.Builder setDeadLetterPolicy(DeadLetterPolicy.Builder builderForValue)

Optional. A policy that specifies the conditions for dead lettering messages in this subscription. If dead_letter_policy is not set, dead lettering is disabled.

The Pub/Sub service account associated with this subscriptions's parent project (i.e., service-{project_number}@gcp-sa-pubsub.iam.gserviceaccount.com) must have permission to Acknowledge() messages on this subscription.

` .google.cloud.bigquery.analyticshub.v1.DeadLetterPolicy dead_letter_policy = 13 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[DeadLetterPolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.DeadLetterPolicy.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` |   
  
### setDetached(boolean value)
    
    
    public PubSubSubscription.Builder setDetached(boolean value)

Optional. Indicates whether the subscription is detached from its topic. Detached subscriptions don't receive messages from their topic and don't retain any backlog. `Pull` and `StreamingPull` requests will return FAILED_PRECONDITION. If the subscription is a push subscription, pushes to the endpoint will not be made.

`bool detached = 15 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The detached to set.  
**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` | This builder for chaining.  
  
### setEnableExactlyOnceDelivery(boolean value)
    
    
    public PubSubSubscription.Builder setEnableExactlyOnceDelivery(boolean value)

Optional. If true, Pub/Sub provides the following guarantees for the delivery of a message with a given value of `message_id` on this subscription:

  * The message sent to a subscriber is guaranteed not to be resent before the message's acknowledgement deadline expires.
  * An acknowledged message will not be resent to a subscriber.

Note that subscribers may still receive multiple copies of a message when `enable_exactly_once_delivery` is true if the message was published multiple times by a publisher client. These copies are considered distinct by Pub/Sub and have distinct `message_id` values.




`bool enable_exactly_once_delivery = 16 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The enableExactlyOnceDelivery to set.  
**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` | This builder for chaining.  
  
### setEnableMessageOrdering(boolean value)
    
    
    public PubSubSubscription.Builder setEnableMessageOrdering(boolean value)

Optional. If true, messages published with the same `ordering_key` in `PubsubMessage` will be delivered to the subscribers in the order in which they are received by the Pub/Sub system. Otherwise, they may be delivered in any order.

`bool enable_message_ordering = 10 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The enableMessageOrdering to set.  
**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` | This builder for chaining.  
  
### setExpirationPolicy(ExpirationPolicy value)
    
    
    public PubSubSubscription.Builder setExpirationPolicy(ExpirationPolicy value)

Optional. A policy that specifies the conditions for this subscription's expiration. A subscription is considered active as long as any connected subscriber is successfully consuming messages from the subscription or is issuing operations on the subscription. If `expiration_policy` is not set, a _default policy_ with `ttl` of 31 days will be used. The minimum allowed value for `expiration_policy.ttl` is 1 day. If `expiration_policy` is set, but `expiration_policy.ttl` is not set, the subscription never expires.

` .google.cloud.bigquery.analyticshub.v1.ExpirationPolicy expiration_policy = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ExpirationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.ExpirationPolicy)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` |   
  
### setExpirationPolicy(ExpirationPolicy.Builder builderForValue)
    
    
    public PubSubSubscription.Builder setExpirationPolicy(ExpirationPolicy.Builder builderForValue)

Optional. A policy that specifies the conditions for this subscription's expiration. A subscription is considered active as long as any connected subscriber is successfully consuming messages from the subscription or is issuing operations on the subscription. If `expiration_policy` is not set, a _default policy_ with `ttl` of 31 days will be used. The minimum allowed value for `expiration_policy.ttl` is 1 day. If `expiration_policy` is set, but `expiration_policy.ttl` is not set, the subscription never expires.

` .google.cloud.bigquery.analyticshub.v1.ExpirationPolicy expiration_policy = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[ExpirationPolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.ExpirationPolicy.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` |   
  
### setFilter(String value)
    
    
    public PubSubSubscription.Builder setFilter(String value)

Optional. An expression written in the Pub/Sub [filter language](https://cloud.google.com/pubsub/docs/filtering). If non-empty, then only `PubsubMessage`s whose `attributes` field matches the filter are delivered on this subscription. If empty, then no messages are filtered out.

`string filter = 12 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The filter to set.  
**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` | This builder for chaining.  
  
### setFilterBytes(ByteString value)
    
    
    public PubSubSubscription.Builder setFilterBytes(ByteString value)

Optional. An expression written in the Pub/Sub [filter language](https://cloud.google.com/pubsub/docs/filtering). If non-empty, then only `PubsubMessage`s whose `attributes` field matches the filter are delivered on this subscription. If empty, then no messages are filtered out.

`string filter = 12 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for filter to set.  
**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` | This builder for chaining.  
  
### setMessageRetentionDuration(Duration value)
    
    
    public PubSubSubscription.Builder setMessageRetentionDuration(Duration value)

Optional. How long to retain unacknowledged messages in the subscription's backlog, from the moment a message is published. If `retain_acked_messages` is true, then this also configures the retention of acknowledged messages, and thus configures how far back in time a `Seek` can be done. Defaults to 7 days. Cannot be more than 31 days or less than 10 minutes.

` .google.protobuf.Duration message_retention_duration = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` |   
  
### setMessageRetentionDuration(Duration.Builder builderForValue)
    
    
    public PubSubSubscription.Builder setMessageRetentionDuration(Duration.Builder builderForValue)

Optional. How long to retain unacknowledged messages in the subscription's backlog, from the moment a message is published. If `retain_acked_messages` is true, then this also configures the retention of acknowledged messages, and thus configures how far back in time a `Seek` can be done. Defaults to 7 days. Cannot be more than 31 days or less than 10 minutes.

` .google.protobuf.Duration message_retention_duration = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` |   
  
### setMessageTransforms(int index, MessageTransform value)
    
    
    public PubSubSubscription.Builder setMessageTransforms(int index, MessageTransform value)

Optional. Transforms to be applied to messages before they are delivered to subscribers. Transforms are applied in the order specified.

` repeated .google.cloud.bigquery.analyticshub.v1.MessageTransform message_transforms = 25 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[MessageTransform](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.MessageTransform)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` |   
  
### setMessageTransforms(int index, MessageTransform.Builder builderForValue)
    
    
    public PubSubSubscription.Builder setMessageTransforms(int index, MessageTransform.Builder builderForValue)

Optional. Transforms to be applied to messages before they are delivered to subscribers. Transforms are applied in the order specified.

` repeated .google.cloud.bigquery.analyticshub.v1.MessageTransform message_transforms = 25 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[MessageTransform.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.MessageTransform.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` |   
  
### setName(String value)
    
    
    public PubSubSubscription.Builder setName(String value)

Required. Name of the subscription. Format is `projects/{project}/subscriptions/{sub}`.

`string name = 1 [(.google.api.field_behavior) = REQUIRED];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name to set.  
**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` | This builder for chaining.  
  
### setNameBytes(ByteString value)
    
    
    public PubSubSubscription.Builder setNameBytes(ByteString value)

Required. Name of the subscription. Format is `projects/{project}/subscriptions/{sub}`.

`string name = 1 [(.google.api.field_behavior) = REQUIRED];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for name to set.  
**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` | This builder for chaining.  
  
### setPushConfig(PushConfig value)
    
    
    public PubSubSubscription.Builder setPushConfig(PushConfig value)

Optional. If push delivery is used with this subscription, this field is used to configure it.

` .google.cloud.bigquery.analyticshub.v1.PushConfig push_config = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[PushConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PushConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` |   
  
### setPushConfig(PushConfig.Builder builderForValue)
    
    
    public PubSubSubscription.Builder setPushConfig(PushConfig.Builder builderForValue)

Optional. If push delivery is used with this subscription, this field is used to configure it.

` .google.cloud.bigquery.analyticshub.v1.PushConfig push_config = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[PushConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PushConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` |   
  
### setRetainAckedMessages(boolean value)
    
    
    public PubSubSubscription.Builder setRetainAckedMessages(boolean value)

Optional. Indicates whether to retain acknowledged messages. If true, then messages are not expunged from the subscription's backlog, even if they are acknowledged, until they fall out of the `message_retention_duration` window. This must be true if you would like to [`Seek` to a timestamp](https://cloud.google.com/pubsub/docs/replay-overview#seek_to_a_time) in the past to replay previously-acknowledged messages.

`bool retain_acked_messages = 7 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The retainAckedMessages to set.  
**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` | This builder for chaining.  
  
### setRetryPolicy(RetryPolicy value)
    
    
    public PubSubSubscription.Builder setRetryPolicy(RetryPolicy value)

Optional. A policy that specifies how Pub/Sub retries message delivery for this subscription.

If not set, the default retry policy is applied. This generally implies that messages will be retried as soon as possible for healthy subscribers. RetryPolicy will be triggered on NACKs or acknowledgement deadline exceeded events for a given message.

` .google.cloud.bigquery.analyticshub.v1.RetryPolicy retry_policy = 14 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[RetryPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.RetryPolicy)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` |   
  
### setRetryPolicy(RetryPolicy.Builder builderForValue)
    
    
    public PubSubSubscription.Builder setRetryPolicy(RetryPolicy.Builder builderForValue)

Optional. A policy that specifies how Pub/Sub retries message delivery for this subscription.

If not set, the default retry policy is applied. This generally implies that messages will be retried as soon as possible for healthy subscribers. RetryPolicy will be triggered on NACKs or acknowledgement deadline exceeded events for a given message.

` .google.cloud.bigquery.analyticshub.v1.RetryPolicy retry_policy = 14 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[RetryPolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.RetryPolicy.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.PubSubSubscription.Builder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
