---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.IrregularRhythmNotification.AlertWindow.Builder
title: Class IrregularRhythmNotification.AlertWindow.Builder (0.8.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:06:03.400095+00:00
---

# Class IrregularRhythmNotification.AlertWindow.Builder (0.8.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.IrregularRhythmNotification.AlertWindow.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class IrregularRhythmNotification.AlertWindow.Builder (0.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.8.0 (latest)  0.4.0  0.3.0  0.2.0 
    
    
    public static final class IrregularRhythmNotification.AlertWindow.Builder extends GeneratedMessage.Builder<IrregularRhythmNotification.AlertWindow.Builder> implements IrregularRhythmNotification.AlertWindowOrBuilder

An analysis window evaluated for AFib.

Note: The current version of the algorithm will only produce alerts if all windows are positive. So anything returned from the API will always have the positive bit set to true. Internally, windows can be negative, however. We never save "inconclusive" windows (they aren't produced by the algorithm).

Protobuf type ` google.devicesandservices.health.v4.IrregularRhythmNotification.AlertWindow`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > IrregularRhythmNotification.AlertWindow.Builder

## Implements

[IrregularRhythmNotification.AlertWindowOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.IrregularRhythmNotification.AlertWindowOrBuilder)

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

### addAllHeartBeats(Iterable<? extends IrregularRhythmNotification.HeartBeat> values)
    
    
    public IrregularRhythmNotification.AlertWindow.Builder addAllHeartBeats(Iterable<? extends IrregularRhythmNotification.HeartBeat> values)

Optional. All heart beats in the interval contained in this analysis window.

` repeated .google.devicesandservices.health.v4.IrregularRhythmNotification.HeartBeat heart_beats = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<? extends com.google.devicesandservices.health.v4.IrregularRhythmNotification.HeartBeat>`  
  
**Returns**  
---  
**Type** | **Description**  
`[IrregularRhythmNotification.AlertWindow.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.IrregularRhythmNotification.AlertWindow.Builder)` |   
  
### addHeartBeats(IrregularRhythmNotification.HeartBeat value)
    
    
    public IrregularRhythmNotification.AlertWindow.Builder addHeartBeats(IrregularRhythmNotification.HeartBeat value)

Optional. All heart beats in the interval contained in this analysis window.

` repeated .google.devicesandservices.health.v4.IrregularRhythmNotification.HeartBeat heart_beats = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[IrregularRhythmNotification.HeartBeat](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.IrregularRhythmNotification.HeartBeat)`  
  
**Returns**  
---  
**Type** | **Description**  
`[IrregularRhythmNotification.AlertWindow.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.IrregularRhythmNotification.AlertWindow.Builder)` |   
  
### addHeartBeats(IrregularRhythmNotification.HeartBeat.Builder builderForValue)
    
    
    public IrregularRhythmNotification.AlertWindow.Builder addHeartBeats(IrregularRhythmNotification.HeartBeat.Builder builderForValue)

Optional. All heart beats in the interval contained in this analysis window.

` repeated .google.devicesandservices.health.v4.IrregularRhythmNotification.HeartBeat heart_beats = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[IrregularRhythmNotification.HeartBeat.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.IrregularRhythmNotification.HeartBeat.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[IrregularRhythmNotification.AlertWindow.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.IrregularRhythmNotification.AlertWindow.Builder)` |   
  
### addHeartBeats(int index, IrregularRhythmNotification.HeartBeat value)
    
    
    public IrregularRhythmNotification.AlertWindow.Builder addHeartBeats(int index, IrregularRhythmNotification.HeartBeat value)

Optional. All heart beats in the interval contained in this analysis window.

` repeated .google.devicesandservices.health.v4.IrregularRhythmNotification.HeartBeat heart_beats = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[IrregularRhythmNotification.HeartBeat](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.IrregularRhythmNotification.HeartBeat)`  
  
**Returns**  
---  
**Type** | **Description**  
`[IrregularRhythmNotification.AlertWindow.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.IrregularRhythmNotification.AlertWindow.Builder)` |   
  
### addHeartBeats(int index, IrregularRhythmNotification.HeartBeat.Builder builderForValue)
    
    
    public IrregularRhythmNotification.AlertWindow.Builder addHeartBeats(int index, IrregularRhythmNotification.HeartBeat.Builder builderForValue)

Optional. All heart beats in the interval contained in this analysis window.

` repeated .google.devicesandservices.health.v4.IrregularRhythmNotification.HeartBeat heart_beats = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[IrregularRhythmNotification.HeartBeat.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.IrregularRhythmNotification.HeartBeat.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[IrregularRhythmNotification.AlertWindow.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.IrregularRhythmNotification.AlertWindow.Builder)` |   
  
### addHeartBeatsBuilder()
    
    
    public IrregularRhythmNotification.HeartBeat.Builder addHeartBeatsBuilder()

Optional. All heart beats in the interval contained in this analysis window.

` repeated .google.devicesandservices.health.v4.IrregularRhythmNotification.HeartBeat heart_beats = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[IrregularRhythmNotification.HeartBeat.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.IrregularRhythmNotification.HeartBeat.Builder)` |   
  
### addHeartBeatsBuilder(int index)
    
    
    public IrregularRhythmNotification.HeartBeat.Builder addHeartBeatsBuilder(int index)

Optional. All heart beats in the interval contained in this analysis window.

` repeated .google.devicesandservices.health.v4.IrregularRhythmNotification.HeartBeat heart_beats = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[IrregularRhythmNotification.HeartBeat.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.IrregularRhythmNotification.HeartBeat.Builder)` |   
  
### build()
    
    
    public IrregularRhythmNotification.AlertWindow build()

**Returns**  
---  
**Type** | **Description**  
`[IrregularRhythmNotification.AlertWindow](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.IrregularRhythmNotification.AlertWindow)` |   
  
### buildPartial()
    
    
    public IrregularRhythmNotification.AlertWindow buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[IrregularRhythmNotification.AlertWindow](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.IrregularRhythmNotification.AlertWindow)` |   
  
### clear()
    
    
    public IrregularRhythmNotification.AlertWindow.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[IrregularRhythmNotification.AlertWindow.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.IrregularRhythmNotification.AlertWindow.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearCivilEndTime()
    
    
    public IrregularRhythmNotification.AlertWindow.Builder clearCivilEndTime()

Output only. Observed interval end time in civil time in the timezone the subject is in at the end of the observed interval

` .google.devicesandservices.health.v4.CivilDateTime civil_end_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[IrregularRhythmNotification.AlertWindow.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.IrregularRhythmNotification.AlertWindow.Builder)` |   
  
### clearCivilStartTime()
    
    
    public IrregularRhythmNotification.AlertWindow.Builder clearCivilStartTime()

Output only. Observed interval start time in civil time in the timezone the subject is in at the start of the observed interval

` .google.devicesandservices.health.v4.CivilDateTime civil_start_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[IrregularRhythmNotification.AlertWindow.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.IrregularRhythmNotification.AlertWindow.Builder)` |   
  
### clearEndTime()
    
    
    public IrregularRhythmNotification.AlertWindow.Builder clearEndTime()

Required. The end time of the analysis window.

`.google.protobuf.Timestamp end_time = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[IrregularRhythmNotification.AlertWindow.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.IrregularRhythmNotification.AlertWindow.Builder)` |   
  
### clearEndUtcOffset()
    
    
    public IrregularRhythmNotification.AlertWindow.Builder clearEndUtcOffset()

Required. The UTC offset of the user's timezone when the analysis window ended.

` .google.protobuf.Duration end_utc_offset = 4 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[IrregularRhythmNotification.AlertWindow.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.IrregularRhythmNotification.AlertWindow.Builder)` |   
  
### clearHeartBeats()
    
    
    public IrregularRhythmNotification.AlertWindow.Builder clearHeartBeats()

Optional. All heart beats in the interval contained in this analysis window.

` repeated .google.devicesandservices.health.v4.IrregularRhythmNotification.HeartBeat heart_beats = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[IrregularRhythmNotification.AlertWindow.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.IrregularRhythmNotification.AlertWindow.Builder)` |   
  
### clearPositive()
    
    
    public IrregularRhythmNotification.AlertWindow.Builder clearPositive()

Optional. Flag indicating whether the window was positive for AFib or not. A `true` value indicates that AFib was detected in this window. A `false` value means AFib was not detected, but does not guarantee the absence of AFib.

`bool positive = 7 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[IrregularRhythmNotification.AlertWindow.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.IrregularRhythmNotification.AlertWindow.Builder)` | This builder for chaining.  
  
### clearStartTime()
    
    
    public IrregularRhythmNotification.AlertWindow.Builder clearStartTime()

Required. Observed interval. The start time of the analysis window.

`.google.protobuf.Timestamp start_time = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[IrregularRhythmNotification.AlertWindow.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.IrregularRhythmNotification.AlertWindow.Builder)` |   
  
### clearStartUtcOffset()
    
    
    public IrregularRhythmNotification.AlertWindow.Builder clearStartUtcOffset()

Required. The UTC offset of the user's timezone when the analysis window started.

` .google.protobuf.Duration start_utc_offset = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[IrregularRhythmNotification.AlertWindow.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.IrregularRhythmNotification.AlertWindow.Builder)` |   
  
### getCivilEndTime()
    
    
    public CivilDateTime getCivilEndTime()

Output only. Observed interval end time in civil time in the timezone the subject is in at the end of the observed interval

` .google.devicesandservices.health.v4.CivilDateTime civil_end_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[CivilDateTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CivilDateTime)` | The civilEndTime.  
  
### getCivilEndTimeBuilder()
    
    
    public CivilDateTime.Builder getCivilEndTimeBuilder()

Output only. Observed interval end time in civil time in the timezone the subject is in at the end of the observed interval

` .google.devicesandservices.health.v4.CivilDateTime civil_end_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[CivilDateTime.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CivilDateTime.Builder)` |   
  
### getCivilEndTimeOrBuilder()
    
    
    public CivilDateTimeOrBuilder getCivilEndTimeOrBuilder()

Output only. Observed interval end time in civil time in the timezone the subject is in at the end of the observed interval

` .google.devicesandservices.health.v4.CivilDateTime civil_end_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[CivilDateTimeOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CivilDateTimeOrBuilder)` |   
  
### getCivilStartTime()
    
    
    public CivilDateTime getCivilStartTime()

Output only. Observed interval start time in civil time in the timezone the subject is in at the start of the observed interval

` .google.devicesandservices.health.v4.CivilDateTime civil_start_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[CivilDateTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CivilDateTime)` | The civilStartTime.  
  
### getCivilStartTimeBuilder()
    
    
    public CivilDateTime.Builder getCivilStartTimeBuilder()

Output only. Observed interval start time in civil time in the timezone the subject is in at the start of the observed interval

` .google.devicesandservices.health.v4.CivilDateTime civil_start_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[CivilDateTime.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CivilDateTime.Builder)` |   
  
### getCivilStartTimeOrBuilder()
    
    
    public CivilDateTimeOrBuilder getCivilStartTimeOrBuilder()

Output only. Observed interval start time in civil time in the timezone the subject is in at the start of the observed interval

` .google.devicesandservices.health.v4.CivilDateTime civil_start_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[CivilDateTimeOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CivilDateTimeOrBuilder)` |   
  
### getDefaultInstanceForType()
    
    
    public IrregularRhythmNotification.AlertWindow getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[IrregularRhythmNotification.AlertWindow](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.IrregularRhythmNotification.AlertWindow)` |   
  
### getDescriptorForType()
    
    
    public Descriptors.Descriptor getDescriptorForType()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getDescriptorForType__)

### getEndTime()
    
    
    public Timestamp getEndTime()

Required. The end time of the analysis window.

`.google.protobuf.Timestamp end_time = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The endTime.  
  
### getEndTimeBuilder()
    
    
    public Timestamp.Builder getEndTimeBuilder()

Required. The end time of the analysis window.

`.google.protobuf.Timestamp end_time = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)` |   
  
### getEndTimeOrBuilder()
    
    
    public TimestampOrBuilder getEndTimeOrBuilder()

Required. The end time of the analysis window.

`.google.protobuf.Timestamp end_time = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getEndUtcOffset()
    
    
    public Duration getEndUtcOffset()

Required. The UTC offset of the user's timezone when the analysis window ended.

` .google.protobuf.Duration end_utc_offset = 4 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)` | The endUtcOffset.  
  
### getEndUtcOffsetBuilder()
    
    
    public Duration.Builder getEndUtcOffsetBuilder()

Required. The UTC offset of the user's timezone when the analysis window ended.

` .google.protobuf.Duration end_utc_offset = 4 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.Builder.html)` |   
  
### getEndUtcOffsetOrBuilder()
    
    
    public DurationOrBuilder getEndUtcOffsetOrBuilder()

Required. The UTC offset of the user's timezone when the analysis window ended.

` .google.protobuf.Duration end_utc_offset = 4 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[DurationOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DurationOrBuilder.html)` |   
  
### getHeartBeats(int index)
    
    
    public IrregularRhythmNotification.HeartBeat getHeartBeats(int index)

Optional. All heart beats in the interval contained in this analysis window.

` repeated .google.devicesandservices.health.v4.IrregularRhythmNotification.HeartBeat heart_beats = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[IrregularRhythmNotification.HeartBeat](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.IrregularRhythmNotification.HeartBeat)` |   
  
### getHeartBeatsBuilder(int index)
    
    
    public IrregularRhythmNotification.HeartBeat.Builder getHeartBeatsBuilder(int index)

Optional. All heart beats in the interval contained in this analysis window.

` repeated .google.devicesandservices.health.v4.IrregularRhythmNotification.HeartBeat heart_beats = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[IrregularRhythmNotification.HeartBeat.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.IrregularRhythmNotification.HeartBeat.Builder)` |   
  
### getHeartBeatsBuilderList()
    
    
    public List<IrregularRhythmNotification.HeartBeat.Builder> getHeartBeatsBuilderList()

Optional. All heart beats in the interval contained in this analysis window.

` repeated .google.devicesandservices.health.v4.IrregularRhythmNotification.HeartBeat heart_beats = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.IrregularRhythmNotification.HeartBeat.Builder)>` |   
  
### getHeartBeatsCount()
    
    
    public int getHeartBeatsCount()

Optional. All heart beats in the interval contained in this analysis window.

` repeated .google.devicesandservices.health.v4.IrregularRhythmNotification.HeartBeat heart_beats = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getHeartBeatsList()
    
    
    public List<IrregularRhythmNotification.HeartBeat> getHeartBeatsList()

Optional. All heart beats in the interval contained in this analysis window.

` repeated .google.devicesandservices.health.v4.IrregularRhythmNotification.HeartBeat heart_beats = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[HeartBeat](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.IrregularRhythmNotification.HeartBeat)>` |   
  
### getHeartBeatsOrBuilder(int index)
    
    
    public IrregularRhythmNotification.HeartBeatOrBuilder getHeartBeatsOrBuilder(int index)

Optional. All heart beats in the interval contained in this analysis window.

` repeated .google.devicesandservices.health.v4.IrregularRhythmNotification.HeartBeat heart_beats = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[IrregularRhythmNotification.HeartBeatOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.IrregularRhythmNotification.HeartBeatOrBuilder)` |   
  
### getHeartBeatsOrBuilderList()
    
    
    public List<? extends IrregularRhythmNotification.HeartBeatOrBuilder> getHeartBeatsOrBuilderList()

Optional. All heart beats in the interval contained in this analysis window.

` repeated .google.devicesandservices.health.v4.IrregularRhythmNotification.HeartBeat heart_beats = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.devicesandservices.health.v4.IrregularRhythmNotification.HeartBeatOrBuilder>` |   
  
### getPositive()
    
    
    public boolean getPositive()

Optional. Flag indicating whether the window was positive for AFib or not. A `true` value indicates that AFib was detected in this window. A `false` value means AFib was not detected, but does not guarantee the absence of AFib.

`bool positive = 7 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The positive.  
  
### getStartTime()
    
    
    public Timestamp getStartTime()

Required. Observed interval. The start time of the analysis window.

`.google.protobuf.Timestamp start_time = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The startTime.  
  
### getStartTimeBuilder()
    
    
    public Timestamp.Builder getStartTimeBuilder()

Required. Observed interval. The start time of the analysis window.

`.google.protobuf.Timestamp start_time = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)` |   
  
### getStartTimeOrBuilder()
    
    
    public TimestampOrBuilder getStartTimeOrBuilder()

Required. Observed interval. The start time of the analysis window.

`.google.protobuf.Timestamp start_time = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getStartUtcOffset()
    
    
    public Duration getStartUtcOffset()

Required. The UTC offset of the user's timezone when the analysis window started.

` .google.protobuf.Duration start_utc_offset = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)` | The startUtcOffset.  
  
### getStartUtcOffsetBuilder()
    
    
    public Duration.Builder getStartUtcOffsetBuilder()

Required. The UTC offset of the user's timezone when the analysis window started.

` .google.protobuf.Duration start_utc_offset = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.Builder.html)` |   
  
### getStartUtcOffsetOrBuilder()
    
    
    public DurationOrBuilder getStartUtcOffsetOrBuilder()

Required. The UTC offset of the user's timezone when the analysis window started.

` .google.protobuf.Duration start_utc_offset = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[DurationOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DurationOrBuilder.html)` |   
  
### hasCivilEndTime()
    
    
    public boolean hasCivilEndTime()

Output only. Observed interval end time in civil time in the timezone the subject is in at the end of the observed interval

` .google.devicesandservices.health.v4.CivilDateTime civil_end_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the civilEndTime field is set.  
  
### hasCivilStartTime()
    
    
    public boolean hasCivilStartTime()

Output only. Observed interval start time in civil time in the timezone the subject is in at the start of the observed interval

` .google.devicesandservices.health.v4.CivilDateTime civil_start_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the civilStartTime field is set.  
  
### hasEndTime()
    
    
    public boolean hasEndTime()

Required. The end time of the analysis window.

`.google.protobuf.Timestamp end_time = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the endTime field is set.  
  
### hasEndUtcOffset()
    
    
    public boolean hasEndUtcOffset()

Required. The UTC offset of the user's timezone when the analysis window ended.

` .google.protobuf.Duration end_utc_offset = 4 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the endUtcOffset field is set.  
  
### hasStartTime()
    
    
    public boolean hasStartTime()

Required. Observed interval. The start time of the analysis window.

`.google.protobuf.Timestamp start_time = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the startTime field is set.  
  
### hasStartUtcOffset()
    
    
    public boolean hasStartUtcOffset()

Required. The UTC offset of the user's timezone when the analysis window started.

` .google.protobuf.Duration start_utc_offset = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the startUtcOffset field is set.  
  
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

### mergeCivilEndTime(CivilDateTime value)
    
    
    public IrregularRhythmNotification.AlertWindow.Builder mergeCivilEndTime(CivilDateTime value)

Output only. Observed interval end time in civil time in the timezone the subject is in at the end of the observed interval

` .google.devicesandservices.health.v4.CivilDateTime civil_end_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[CivilDateTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CivilDateTime)`  
  
**Returns**  
---  
**Type** | **Description**  
`[IrregularRhythmNotification.AlertWindow.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.IrregularRhythmNotification.AlertWindow.Builder)` |   
  
### mergeCivilStartTime(CivilDateTime value)
    
    
    public IrregularRhythmNotification.AlertWindow.Builder mergeCivilStartTime(CivilDateTime value)

Output only. Observed interval start time in civil time in the timezone the subject is in at the start of the observed interval

` .google.devicesandservices.health.v4.CivilDateTime civil_start_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[CivilDateTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CivilDateTime)`  
  
**Returns**  
---  
**Type** | **Description**  
`[IrregularRhythmNotification.AlertWindow.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.IrregularRhythmNotification.AlertWindow.Builder)` |   
  
### mergeEndTime(Timestamp value)
    
    
    public IrregularRhythmNotification.AlertWindow.Builder mergeEndTime(Timestamp value)

Required. The end time of the analysis window.

`.google.protobuf.Timestamp end_time = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[IrregularRhythmNotification.AlertWindow.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.IrregularRhythmNotification.AlertWindow.Builder)` |   
  
### mergeEndUtcOffset(Duration value)
    
    
    public IrregularRhythmNotification.AlertWindow.Builder mergeEndUtcOffset(Duration value)

Required. The UTC offset of the user's timezone when the analysis window ended.

` .google.protobuf.Duration end_utc_offset = 4 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[IrregularRhythmNotification.AlertWindow.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.IrregularRhythmNotification.AlertWindow.Builder)` |   
  
### mergeFrom(IrregularRhythmNotification.AlertWindow other)
    
    
    public IrregularRhythmNotification.AlertWindow.Builder mergeFrom(IrregularRhythmNotification.AlertWindow other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[IrregularRhythmNotification.AlertWindow](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.IrregularRhythmNotification.AlertWindow)`  
  
**Returns**  
---  
**Type** | **Description**  
`[IrregularRhythmNotification.AlertWindow.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.IrregularRhythmNotification.AlertWindow.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public IrregularRhythmNotification.AlertWindow.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[IrregularRhythmNotification.AlertWindow.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.IrregularRhythmNotification.AlertWindow.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public IrregularRhythmNotification.AlertWindow.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[IrregularRhythmNotification.AlertWindow.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.IrregularRhythmNotification.AlertWindow.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### mergeStartTime(Timestamp value)
    
    
    public IrregularRhythmNotification.AlertWindow.Builder mergeStartTime(Timestamp value)

Required. Observed interval. The start time of the analysis window.

`.google.protobuf.Timestamp start_time = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[IrregularRhythmNotification.AlertWindow.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.IrregularRhythmNotification.AlertWindow.Builder)` |   
  
### mergeStartUtcOffset(Duration value)
    
    
    public IrregularRhythmNotification.AlertWindow.Builder mergeStartUtcOffset(Duration value)

Required. The UTC offset of the user's timezone when the analysis window started.

` .google.protobuf.Duration start_utc_offset = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[IrregularRhythmNotification.AlertWindow.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.IrregularRhythmNotification.AlertWindow.Builder)` |   
  
### removeHeartBeats(int index)
    
    
    public IrregularRhythmNotification.AlertWindow.Builder removeHeartBeats(int index)

Optional. All heart beats in the interval contained in this analysis window.

` repeated .google.devicesandservices.health.v4.IrregularRhythmNotification.HeartBeat heart_beats = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[IrregularRhythmNotification.AlertWindow.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.IrregularRhythmNotification.AlertWindow.Builder)` |   
  
### setCivilEndTime(CivilDateTime value)
    
    
    public IrregularRhythmNotification.AlertWindow.Builder setCivilEndTime(CivilDateTime value)

Output only. Observed interval end time in civil time in the timezone the subject is in at the end of the observed interval

` .google.devicesandservices.health.v4.CivilDateTime civil_end_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[CivilDateTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CivilDateTime)`  
  
**Returns**  
---  
**Type** | **Description**  
`[IrregularRhythmNotification.AlertWindow.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.IrregularRhythmNotification.AlertWindow.Builder)` |   
  
### setCivilEndTime(CivilDateTime.Builder builderForValue)
    
    
    public IrregularRhythmNotification.AlertWindow.Builder setCivilEndTime(CivilDateTime.Builder builderForValue)

Output only. Observed interval end time in civil time in the timezone the subject is in at the end of the observed interval

` .google.devicesandservices.health.v4.CivilDateTime civil_end_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[CivilDateTime.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CivilDateTime.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[IrregularRhythmNotification.AlertWindow.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.IrregularRhythmNotification.AlertWindow.Builder)` |   
  
### setCivilStartTime(CivilDateTime value)
    
    
    public IrregularRhythmNotification.AlertWindow.Builder setCivilStartTime(CivilDateTime value)

Output only. Observed interval start time in civil time in the timezone the subject is in at the start of the observed interval

` .google.devicesandservices.health.v4.CivilDateTime civil_start_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[CivilDateTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CivilDateTime)`  
  
**Returns**  
---  
**Type** | **Description**  
`[IrregularRhythmNotification.AlertWindow.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.IrregularRhythmNotification.AlertWindow.Builder)` |   
  
### setCivilStartTime(CivilDateTime.Builder builderForValue)
    
    
    public IrregularRhythmNotification.AlertWindow.Builder setCivilStartTime(CivilDateTime.Builder builderForValue)

Output only. Observed interval start time in civil time in the timezone the subject is in at the start of the observed interval

` .google.devicesandservices.health.v4.CivilDateTime civil_start_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[CivilDateTime.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CivilDateTime.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[IrregularRhythmNotification.AlertWindow.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.IrregularRhythmNotification.AlertWindow.Builder)` |   
  
### setEndTime(Timestamp value)
    
    
    public IrregularRhythmNotification.AlertWindow.Builder setEndTime(Timestamp value)

Required. The end time of the analysis window.

`.google.protobuf.Timestamp end_time = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[IrregularRhythmNotification.AlertWindow.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.IrregularRhythmNotification.AlertWindow.Builder)` |   
  
### setEndTime(Timestamp.Builder builderForValue)
    
    
    public IrregularRhythmNotification.AlertWindow.Builder setEndTime(Timestamp.Builder builderForValue)

Required. The end time of the analysis window.

`.google.protobuf.Timestamp end_time = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[IrregularRhythmNotification.AlertWindow.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.IrregularRhythmNotification.AlertWindow.Builder)` |   
  
### setEndUtcOffset(Duration value)
    
    
    public IrregularRhythmNotification.AlertWindow.Builder setEndUtcOffset(Duration value)

Required. The UTC offset of the user's timezone when the analysis window ended.

` .google.protobuf.Duration end_utc_offset = 4 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[IrregularRhythmNotification.AlertWindow.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.IrregularRhythmNotification.AlertWindow.Builder)` |   
  
### setEndUtcOffset(Duration.Builder builderForValue)
    
    
    public IrregularRhythmNotification.AlertWindow.Builder setEndUtcOffset(Duration.Builder builderForValue)

Required. The UTC offset of the user's timezone when the analysis window ended.

` .google.protobuf.Duration end_utc_offset = 4 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[IrregularRhythmNotification.AlertWindow.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.IrregularRhythmNotification.AlertWindow.Builder)` |   
  
### setHeartBeats(int index, IrregularRhythmNotification.HeartBeat value)
    
    
    public IrregularRhythmNotification.AlertWindow.Builder setHeartBeats(int index, IrregularRhythmNotification.HeartBeat value)

Optional. All heart beats in the interval contained in this analysis window.

` repeated .google.devicesandservices.health.v4.IrregularRhythmNotification.HeartBeat heart_beats = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[IrregularRhythmNotification.HeartBeat](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.IrregularRhythmNotification.HeartBeat)`  
  
**Returns**  
---  
**Type** | **Description**  
`[IrregularRhythmNotification.AlertWindow.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.IrregularRhythmNotification.AlertWindow.Builder)` |   
  
### setHeartBeats(int index, IrregularRhythmNotification.HeartBeat.Builder builderForValue)
    
    
    public IrregularRhythmNotification.AlertWindow.Builder setHeartBeats(int index, IrregularRhythmNotification.HeartBeat.Builder builderForValue)

Optional. All heart beats in the interval contained in this analysis window.

` repeated .google.devicesandservices.health.v4.IrregularRhythmNotification.HeartBeat heart_beats = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[IrregularRhythmNotification.HeartBeat.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.IrregularRhythmNotification.HeartBeat.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[IrregularRhythmNotification.AlertWindow.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.IrregularRhythmNotification.AlertWindow.Builder)` |   
  
### setPositive(boolean value)
    
    
    public IrregularRhythmNotification.AlertWindow.Builder setPositive(boolean value)

Optional. Flag indicating whether the window was positive for AFib or not. A `true` value indicates that AFib was detected in this window. A `false` value means AFib was not detected, but does not guarantee the absence of AFib.

`bool positive = 7 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The positive to set.  
**Returns**  
---  
**Type** | **Description**  
`[IrregularRhythmNotification.AlertWindow.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.IrregularRhythmNotification.AlertWindow.Builder)` | This builder for chaining.  
  
### setStartTime(Timestamp value)
    
    
    public IrregularRhythmNotification.AlertWindow.Builder setStartTime(Timestamp value)

Required. Observed interval. The start time of the analysis window.

`.google.protobuf.Timestamp start_time = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[IrregularRhythmNotification.AlertWindow.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.IrregularRhythmNotification.AlertWindow.Builder)` |   
  
### setStartTime(Timestamp.Builder builderForValue)
    
    
    public IrregularRhythmNotification.AlertWindow.Builder setStartTime(Timestamp.Builder builderForValue)

Required. Observed interval. The start time of the analysis window.

`.google.protobuf.Timestamp start_time = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[IrregularRhythmNotification.AlertWindow.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.IrregularRhythmNotification.AlertWindow.Builder)` |   
  
### setStartUtcOffset(Duration value)
    
    
    public IrregularRhythmNotification.AlertWindow.Builder setStartUtcOffset(Duration value)

Required. The UTC offset of the user's timezone when the analysis window started.

` .google.protobuf.Duration start_utc_offset = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[IrregularRhythmNotification.AlertWindow.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.IrregularRhythmNotification.AlertWindow.Builder)` |   
  
### setStartUtcOffset(Duration.Builder builderForValue)
    
    
    public IrregularRhythmNotification.AlertWindow.Builder setStartUtcOffset(Duration.Builder builderForValue)

Required. The UTC offset of the user's timezone when the analysis window started.

` .google.protobuf.Duration start_utc_offset = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[IrregularRhythmNotification.AlertWindow.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.IrregularRhythmNotification.AlertWindow.Builder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
