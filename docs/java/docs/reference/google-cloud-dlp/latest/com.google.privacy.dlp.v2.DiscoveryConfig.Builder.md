---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder
title: Class DiscoveryConfig.Builder (3.103.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:19:01.142436+00:00
---

# Class DiscoveryConfig.Builder (3.103.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DiscoveryConfig.Builder (3.103.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.103.0 (latest)  3.99.0  3.98.0  3.97.0  3.95.0  3.92.0  3.91.0  3.89.0  3.87.0  3.86.0  3.85.0  3.84.0  3.82.0  3.80.0  3.79.0  3.78.0  3.77.0  3.76.0  3.74.0  3.72.0  3.71.0  3.68.0  3.67.0  3.66.0  3.64.0  3.63.0  3.62.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.53.0  3.52.0  3.51.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.41.0  3.40.0  3.39.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.6  3.6.7  3.5.0  3.4.0  3.3.2  3.2.1  3.1.4 
    
    
    public static final class DiscoveryConfig.Builder extends GeneratedMessage.Builder<DiscoveryConfig.Builder> implements DiscoveryConfigOrBuilder

Configuration for discovery to scan resources for profile generation. Only one discovery configuration may exist per organization, folder, or project.

The generated data profiles are retained according to the [data retention policy](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#retention).

Protobuf type `google.privacy.dlp.v2.DiscoveryConfig`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > DiscoveryConfig.Builder

## Implements

[DiscoveryConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfigOrBuilder)

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

### addActions(DataProfileAction value)
    
    
    public DiscoveryConfig.Builder addActions(DataProfileAction value)

Actions to execute at the completion of scanning.

`repeated .google.privacy.dlp.v2.DataProfileAction actions = 4;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[DataProfileAction](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DataProfileAction)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` |   
  
### addActions(DataProfileAction.Builder builderForValue)
    
    
    public DiscoveryConfig.Builder addActions(DataProfileAction.Builder builderForValue)

Actions to execute at the completion of scanning.

`repeated .google.privacy.dlp.v2.DataProfileAction actions = 4;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[DataProfileAction.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DataProfileAction.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` |   
  
### addActions(int index, DataProfileAction value)
    
    
    public DiscoveryConfig.Builder addActions(int index, DataProfileAction value)

Actions to execute at the completion of scanning.

`repeated .google.privacy.dlp.v2.DataProfileAction actions = 4;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[DataProfileAction](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DataProfileAction)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` |   
  
### addActions(int index, DataProfileAction.Builder builderForValue)
    
    
    public DiscoveryConfig.Builder addActions(int index, DataProfileAction.Builder builderForValue)

Actions to execute at the completion of scanning.

`repeated .google.privacy.dlp.v2.DataProfileAction actions = 4;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[DataProfileAction.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DataProfileAction.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` |   
  
### addActionsBuilder()
    
    
    public DataProfileAction.Builder addActionsBuilder()

Actions to execute at the completion of scanning.

`repeated .google.privacy.dlp.v2.DataProfileAction actions = 4;`

**Returns**  
---  
**Type** | **Description**  
`[DataProfileAction.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DataProfileAction.Builder)` |   
  
### addActionsBuilder(int index)
    
    
    public DataProfileAction.Builder addActionsBuilder(int index)

Actions to execute at the completion of scanning.

`repeated .google.privacy.dlp.v2.DataProfileAction actions = 4;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DataProfileAction.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DataProfileAction.Builder)` |   
  
### addAllActions(Iterable<? extends DataProfileAction> values)
    
    
    public DiscoveryConfig.Builder addAllActions(Iterable<? extends DataProfileAction> values)

Actions to execute at the completion of scanning.

`repeated .google.privacy.dlp.v2.DataProfileAction actions = 4;`

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<? extends com.google.privacy.dlp.v2.DataProfileAction>`  
  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` |   
  
### addAllErrors(Iterable<? extends Error> values)
    
    
    public DiscoveryConfig.Builder addAllErrors(Iterable<? extends Error> values)

Output only. A stream of errors encountered when the config was activated. Repeated errors may result in the config automatically being paused. Output only field. Will return the last 100 errors. Whenever the config is modified this list will be cleared.

` repeated .google.privacy.dlp.v2.Error errors = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<? extends com.google.privacy.dlp.v2.Error>`  
  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` |   
  
### addAllInspectTemplates(Iterable<String> values)
    
    
    public DiscoveryConfig.Builder addAllInspectTemplates(Iterable<String> values)

Detection logic for profile generation.

Not all template features are used by Discovery. FindingLimits, include_quote and exclude_info_types have no impact on Discovery.

Multiple templates may be provided if there is data in multiple regions. At most one template must be specified per-region (including "global"). Each region is scanned using the applicable template. If no region-specific template is specified, but a "global" template is specified, it will be copied to that region and used instead. If no global or region-specific template is provided for a region with data, that region's data will not be scanned.

For more information, see <https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#data-residency>.

`repeated string inspect_templates = 3;`

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
The inspectTemplates to add.  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` | This builder for chaining.  
  
### addAllTargets(Iterable<? extends DiscoveryTarget> values)
    
    
    public DiscoveryConfig.Builder addAllTargets(Iterable<? extends DiscoveryTarget> values)

Target to match against for determining what to scan and how frequently.

`repeated .google.privacy.dlp.v2.DiscoveryTarget targets = 5;`

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<? extends com.google.privacy.dlp.v2.DiscoveryTarget>`  
  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` |   
  
### addErrors(Error value)
    
    
    public DiscoveryConfig.Builder addErrors(Error value)

Output only. A stream of errors encountered when the config was activated. Repeated errors may result in the config automatically being paused. Output only field. Will return the last 100 errors. Whenever the config is modified this list will be cleared.

` repeated .google.privacy.dlp.v2.Error errors = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Error](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Error)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` |   
  
### addErrors(Error.Builder builderForValue)
    
    
    public DiscoveryConfig.Builder addErrors(Error.Builder builderForValue)

Output only. A stream of errors encountered when the config was activated. Repeated errors may result in the config automatically being paused. Output only field. Will return the last 100 errors. Whenever the config is modified this list will be cleared.

` repeated .google.privacy.dlp.v2.Error errors = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Error.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Error.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` |   
  
### addErrors(int index, Error value)
    
    
    public DiscoveryConfig.Builder addErrors(int index, Error value)

Output only. A stream of errors encountered when the config was activated. Repeated errors may result in the config automatically being paused. Output only field. Will return the last 100 errors. Whenever the config is modified this list will be cleared.

` repeated .google.privacy.dlp.v2.Error errors = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[Error](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Error)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` |   
  
### addErrors(int index, Error.Builder builderForValue)
    
    
    public DiscoveryConfig.Builder addErrors(int index, Error.Builder builderForValue)

Output only. A stream of errors encountered when the config was activated. Repeated errors may result in the config automatically being paused. Output only field. Will return the last 100 errors. Whenever the config is modified this list will be cleared.

` repeated .google.privacy.dlp.v2.Error errors = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[Error.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Error.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` |   
  
### addErrorsBuilder()
    
    
    public Error.Builder addErrorsBuilder()

Output only. A stream of errors encountered when the config was activated. Repeated errors may result in the config automatically being paused. Output only field. Will return the last 100 errors. Whenever the config is modified this list will be cleared.

` repeated .google.privacy.dlp.v2.Error errors = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Error.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Error.Builder)` |   
  
### addErrorsBuilder(int index)
    
    
    public Error.Builder addErrorsBuilder(int index)

Output only. A stream of errors encountered when the config was activated. Repeated errors may result in the config automatically being paused. Output only field. Will return the last 100 errors. Whenever the config is modified this list will be cleared.

` repeated .google.privacy.dlp.v2.Error errors = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Error.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Error.Builder)` |   
  
### addInspectTemplates(String value)
    
    
    public DiscoveryConfig.Builder addInspectTemplates(String value)

Detection logic for profile generation.

Not all template features are used by Discovery. FindingLimits, include_quote and exclude_info_types have no impact on Discovery.

Multiple templates may be provided if there is data in multiple regions. At most one template must be specified per-region (including "global"). Each region is scanned using the applicable template. If no region-specific template is specified, but a "global" template is specified, it will be copied to that region and used instead. If no global or region-specific template is provided for a region with data, that region's data will not be scanned.

For more information, see <https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#data-residency>.

`repeated string inspect_templates = 3;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The inspectTemplates to add.  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` | This builder for chaining.  
  
### addInspectTemplatesBytes(ByteString value)
    
    
    public DiscoveryConfig.Builder addInspectTemplatesBytes(ByteString value)

Detection logic for profile generation.

Not all template features are used by Discovery. FindingLimits, include_quote and exclude_info_types have no impact on Discovery.

Multiple templates may be provided if there is data in multiple regions. At most one template must be specified per-region (including "global"). Each region is scanned using the applicable template. If no region-specific template is specified, but a "global" template is specified, it will be copied to that region and used instead. If no global or region-specific template is provided for a region with data, that region's data will not be scanned.

For more information, see <https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#data-residency>.

`repeated string inspect_templates = 3;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes of the inspectTemplates to add.  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` | This builder for chaining.  
  
### addTargets(DiscoveryTarget value)
    
    
    public DiscoveryConfig.Builder addTargets(DiscoveryTarget value)

Target to match against for determining what to scan and how frequently.

`repeated .google.privacy.dlp.v2.DiscoveryTarget targets = 5;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[DiscoveryTarget](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryTarget)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` |   
  
### addTargets(DiscoveryTarget.Builder builderForValue)
    
    
    public DiscoveryConfig.Builder addTargets(DiscoveryTarget.Builder builderForValue)

Target to match against for determining what to scan and how frequently.

`repeated .google.privacy.dlp.v2.DiscoveryTarget targets = 5;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[DiscoveryTarget.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryTarget.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` |   
  
### addTargets(int index, DiscoveryTarget value)
    
    
    public DiscoveryConfig.Builder addTargets(int index, DiscoveryTarget value)

Target to match against for determining what to scan and how frequently.

`repeated .google.privacy.dlp.v2.DiscoveryTarget targets = 5;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[DiscoveryTarget](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryTarget)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` |   
  
### addTargets(int index, DiscoveryTarget.Builder builderForValue)
    
    
    public DiscoveryConfig.Builder addTargets(int index, DiscoveryTarget.Builder builderForValue)

Target to match against for determining what to scan and how frequently.

`repeated .google.privacy.dlp.v2.DiscoveryTarget targets = 5;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[DiscoveryTarget.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryTarget.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` |   
  
### addTargetsBuilder()
    
    
    public DiscoveryTarget.Builder addTargetsBuilder()

Target to match against for determining what to scan and how frequently.

`repeated .google.privacy.dlp.v2.DiscoveryTarget targets = 5;`

**Returns**  
---  
**Type** | **Description**  
`[DiscoveryTarget.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryTarget.Builder)` |   
  
### addTargetsBuilder(int index)
    
    
    public DiscoveryTarget.Builder addTargetsBuilder(int index)

Target to match against for determining what to scan and how frequently.

`repeated .google.privacy.dlp.v2.DiscoveryTarget targets = 5;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryTarget.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryTarget.Builder)` |   
  
### build()
    
    
    public DiscoveryConfig build()

**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig)` |   
  
### buildPartial()
    
    
    public DiscoveryConfig buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig)` |   
  
### clear()
    
    
    public DiscoveryConfig.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearActions()
    
    
    public DiscoveryConfig.Builder clearActions()

Actions to execute at the completion of scanning.

`repeated .google.privacy.dlp.v2.DataProfileAction actions = 4;`

**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` |   
  
### clearCreateTime()
    
    
    public DiscoveryConfig.Builder clearCreateTime()

Output only. The creation timestamp of a DiscoveryConfig.

` .google.protobuf.Timestamp create_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` |   
  
### clearDisplayName()
    
    
    public DiscoveryConfig.Builder clearDisplayName()

Display name (max 100 chars)

`string display_name = 11;`

**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` | This builder for chaining.  
  
### clearErrors()
    
    
    public DiscoveryConfig.Builder clearErrors()

Output only. A stream of errors encountered when the config was activated. Repeated errors may result in the config automatically being paused. Output only field. Will return the last 100 errors. Whenever the config is modified this list will be cleared.

` repeated .google.privacy.dlp.v2.Error errors = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` |   
  
### clearInspectTemplates()
    
    
    public DiscoveryConfig.Builder clearInspectTemplates()

Detection logic for profile generation.

Not all template features are used by Discovery. FindingLimits, include_quote and exclude_info_types have no impact on Discovery.

Multiple templates may be provided if there is data in multiple regions. At most one template must be specified per-region (including "global"). Each region is scanned using the applicable template. If no region-specific template is specified, but a "global" template is specified, it will be copied to that region and used instead. If no global or region-specific template is provided for a region with data, that region's data will not be scanned.

For more information, see <https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#data-residency>.

`repeated string inspect_templates = 3;`

**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` | This builder for chaining.  
  
### clearLastRunTime()
    
    
    public DiscoveryConfig.Builder clearLastRunTime()

Output only. The timestamp of the last time this config was executed.

` .google.protobuf.Timestamp last_run_time = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` |   
  
### clearName()
    
    
    public DiscoveryConfig.Builder clearName()

Output only. Unique resource name for the DiscoveryConfig, assigned by the service when the DiscoveryConfig is created, for example `projects/dlp-test-project/locations/global/discoveryConfigs/53234423`.

`string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` | This builder for chaining.  
  
### clearOrgConfig()
    
    
    public DiscoveryConfig.Builder clearOrgConfig()

Only set when the parent is an org.

`.google.privacy.dlp.v2.DiscoveryConfig.OrgConfig org_config = 2;`

**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` |   
  
### clearOtherCloudStartingLocation()
    
    
    public DiscoveryConfig.Builder clearOtherCloudStartingLocation()

Must be set only when scanning other clouds.

` .google.privacy.dlp.v2.OtherCloudDiscoveryStartingLocation other_cloud_starting_location = 12; `

**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` |   
  
### clearProcessingLocation()
    
    
    public DiscoveryConfig.Builder clearProcessingLocation()

Optional. Processing location configuration. Vertex AI dataset scanning will set processing_location.image_fallback_type to MultiRegionProcessing by default.

` .google.privacy.dlp.v2.ProcessingLocation processing_location = 13 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` |   
  
### clearStatus()
    
    
    public DiscoveryConfig.Builder clearStatus()

Required. A status for this configuration.

` .google.privacy.dlp.v2.DiscoveryConfig.Status status = 10 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` | This builder for chaining.  
  
### clearTargets()
    
    
    public DiscoveryConfig.Builder clearTargets()

Target to match against for determining what to scan and how frequently.

`repeated .google.privacy.dlp.v2.DiscoveryTarget targets = 5;`

**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` |   
  
### clearUpdateTime()
    
    
    public DiscoveryConfig.Builder clearUpdateTime()

Output only. The last update timestamp of a DiscoveryConfig.

` .google.protobuf.Timestamp update_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` |   
  
### getActions(int index)
    
    
    public DataProfileAction getActions(int index)

Actions to execute at the completion of scanning.

`repeated .google.privacy.dlp.v2.DataProfileAction actions = 4;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DataProfileAction](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DataProfileAction)` |   
  
### getActionsBuilder(int index)
    
    
    public DataProfileAction.Builder getActionsBuilder(int index)

Actions to execute at the completion of scanning.

`repeated .google.privacy.dlp.v2.DataProfileAction actions = 4;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DataProfileAction.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DataProfileAction.Builder)` |   
  
### getActionsBuilderList()
    
    
    public List<DataProfileAction.Builder> getActionsBuilderList()

Actions to execute at the completion of scanning.

`repeated .google.privacy.dlp.v2.DataProfileAction actions = 4;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DataProfileAction.Builder)>` |   
  
### getActionsCount()
    
    
    public int getActionsCount()

Actions to execute at the completion of scanning.

`repeated .google.privacy.dlp.v2.DataProfileAction actions = 4;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getActionsList()
    
    
    public List<DataProfileAction> getActionsList()

Actions to execute at the completion of scanning.

`repeated .google.privacy.dlp.v2.DataProfileAction actions = 4;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[DataProfileAction](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DataProfileAction)>` |   
  
### getActionsOrBuilder(int index)
    
    
    public DataProfileActionOrBuilder getActionsOrBuilder(int index)

Actions to execute at the completion of scanning.

`repeated .google.privacy.dlp.v2.DataProfileAction actions = 4;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DataProfileActionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DataProfileActionOrBuilder)` |   
  
### getActionsOrBuilderList()
    
    
    public List<? extends DataProfileActionOrBuilder> getActionsOrBuilderList()

Actions to execute at the completion of scanning.

`repeated .google.privacy.dlp.v2.DataProfileAction actions = 4;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.privacy.dlp.v2.DataProfileActionOrBuilder>` |   
  
### getCreateTime()
    
    
    public Timestamp getCreateTime()

Output only. The creation timestamp of a DiscoveryConfig.

` .google.protobuf.Timestamp create_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeBuilder()
    
    
    public Timestamp.Builder getCreateTimeBuilder()

Output only. The creation timestamp of a DiscoveryConfig.

` .google.protobuf.Timestamp create_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)` |   
  
### getCreateTimeOrBuilder()
    
    
    public TimestampOrBuilder getCreateTimeOrBuilder()

Output only. The creation timestamp of a DiscoveryConfig.

` .google.protobuf.Timestamp create_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDefaultInstanceForType()
    
    
    public DiscoveryConfig getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig)` |   
  
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

Display name (max 100 chars)

`string display_name = 11;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The displayName.  
  
### getDisplayNameBytes()
    
    
    public ByteString getDisplayNameBytes()

Display name (max 100 chars)

`string display_name = 11;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for displayName.  
  
### getErrors(int index)
    
    
    public Error getErrors(int index)

Output only. A stream of errors encountered when the config was activated. Repeated errors may result in the config automatically being paused. Output only field. Will return the last 100 errors. Whenever the config is modified this list will be cleared.

` repeated .google.privacy.dlp.v2.Error errors = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Error](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Error)` |   
  
### getErrorsBuilder(int index)
    
    
    public Error.Builder getErrorsBuilder(int index)

Output only. A stream of errors encountered when the config was activated. Repeated errors may result in the config automatically being paused. Output only field. Will return the last 100 errors. Whenever the config is modified this list will be cleared.

` repeated .google.privacy.dlp.v2.Error errors = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Error.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Error.Builder)` |   
  
### getErrorsBuilderList()
    
    
    public List<Error.Builder> getErrorsBuilderList()

Output only. A stream of errors encountered when the config was activated. Repeated errors may result in the config automatically being paused. Output only field. Will return the last 100 errors. Whenever the config is modified this list will be cleared.

` repeated .google.privacy.dlp.v2.Error errors = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Error.Builder)>` |   
  
### getErrorsCount()
    
    
    public int getErrorsCount()

Output only. A stream of errors encountered when the config was activated. Repeated errors may result in the config automatically being paused. Output only field. Will return the last 100 errors. Whenever the config is modified this list will be cleared.

` repeated .google.privacy.dlp.v2.Error errors = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getErrorsList()
    
    
    public List<Error> getErrorsList()

Output only. A stream of errors encountered when the config was activated. Repeated errors may result in the config automatically being paused. Output only field. Will return the last 100 errors. Whenever the config is modified this list will be cleared.

` repeated .google.privacy.dlp.v2.Error errors = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Error](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Error)>` |   
  
### getErrorsOrBuilder(int index)
    
    
    public ErrorOrBuilder getErrorsOrBuilder(int index)

Output only. A stream of errors encountered when the config was activated. Repeated errors may result in the config automatically being paused. Output only field. Will return the last 100 errors. Whenever the config is modified this list will be cleared.

` repeated .google.privacy.dlp.v2.Error errors = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ErrorOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ErrorOrBuilder)` |   
  
### getErrorsOrBuilderList()
    
    
    public List<? extends ErrorOrBuilder> getErrorsOrBuilderList()

Output only. A stream of errors encountered when the config was activated. Repeated errors may result in the config automatically being paused. Output only field. Will return the last 100 errors. Whenever the config is modified this list will be cleared.

` repeated .google.privacy.dlp.v2.Error errors = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.privacy.dlp.v2.ErrorOrBuilder>` |   
  
### getInspectTemplates(int index)
    
    
    public String getInspectTemplates(int index)

Detection logic for profile generation.

Not all template features are used by Discovery. FindingLimits, include_quote and exclude_info_types have no impact on Discovery.

Multiple templates may be provided if there is data in multiple regions. At most one template must be specified per-region (including "global"). Each region is scanned using the applicable template. If no region-specific template is specified, but a "global" template is specified, it will be copied to that region and used instead. If no global or region-specific template is provided for a region with data, that region's data will not be scanned.

For more information, see <https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#data-residency>.

`repeated string inspect_templates = 3;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The inspectTemplates at the given index.  
  
### getInspectTemplatesBytes(int index)
    
    
    public ByteString getInspectTemplatesBytes(int index)

Detection logic for profile generation.

Not all template features are used by Discovery. FindingLimits, include_quote and exclude_info_types have no impact on Discovery.

Multiple templates may be provided if there is data in multiple regions. At most one template must be specified per-region (including "global"). Each region is scanned using the applicable template. If no region-specific template is specified, but a "global" template is specified, it will be copied to that region and used instead. If no global or region-specific template is provided for a region with data, that region's data will not be scanned.

For more information, see <https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#data-residency>.

`repeated string inspect_templates = 3;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the inspectTemplates at the given index.  
  
### getInspectTemplatesCount()
    
    
    public int getInspectTemplatesCount()

Detection logic for profile generation.

Not all template features are used by Discovery. FindingLimits, include_quote and exclude_info_types have no impact on Discovery.

Multiple templates may be provided if there is data in multiple regions. At most one template must be specified per-region (including "global"). Each region is scanned using the applicable template. If no region-specific template is specified, but a "global" template is specified, it will be copied to that region and used instead. If no global or region-specific template is provided for a region with data, that region's data will not be scanned.

For more information, see <https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#data-residency>.

`repeated string inspect_templates = 3;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of inspectTemplates.  
  
### getInspectTemplatesList()
    
    
    public ProtocolStringList getInspectTemplatesList()

Detection logic for profile generation.

Not all template features are used by Discovery. FindingLimits, include_quote and exclude_info_types have no impact on Discovery.

Multiple templates may be provided if there is data in multiple regions. At most one template must be specified per-region (including "global"). Each region is scanned using the applicable template. If no region-specific template is specified, but a "global" template is specified, it will be copied to that region and used instead. If no global or region-specific template is provided for a region with data, that region's data will not be scanned.

For more information, see <https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#data-residency>.

`repeated string inspect_templates = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ProtocolStringList](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ProtocolStringList.html)` | A list containing the inspectTemplates.  
  
### getLastRunTime()
    
    
    public Timestamp getLastRunTime()

Output only. The timestamp of the last time this config was executed.

` .google.protobuf.Timestamp last_run_time = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The lastRunTime.  
  
### getLastRunTimeBuilder()
    
    
    public Timestamp.Builder getLastRunTimeBuilder()

Output only. The timestamp of the last time this config was executed.

` .google.protobuf.Timestamp last_run_time = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)` |   
  
### getLastRunTimeOrBuilder()
    
    
    public TimestampOrBuilder getLastRunTimeOrBuilder()

Output only. The timestamp of the last time this config was executed.

` .google.protobuf.Timestamp last_run_time = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getName()
    
    
    public String getName()

Output only. Unique resource name for the DiscoveryConfig, assigned by the service when the DiscoveryConfig is created, for example `projects/dlp-test-project/locations/global/discoveryConfigs/53234423`.

`string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public ByteString getNameBytes()

Output only. Unique resource name for the DiscoveryConfig, assigned by the service when the DiscoveryConfig is created, for example `projects/dlp-test-project/locations/global/discoveryConfigs/53234423`.

`string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getOrgConfig()
    
    
    public DiscoveryConfig.OrgConfig getOrgConfig()

Only set when the parent is an org.

`.google.privacy.dlp.v2.DiscoveryConfig.OrgConfig org_config = 2;`

**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.OrgConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.OrgConfig)` | The orgConfig.  
  
### getOrgConfigBuilder()
    
    
    public DiscoveryConfig.OrgConfig.Builder getOrgConfigBuilder()

Only set when the parent is an org.

`.google.privacy.dlp.v2.DiscoveryConfig.OrgConfig org_config = 2;`

**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.OrgConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.OrgConfig.Builder)` |   
  
### getOrgConfigOrBuilder()
    
    
    public DiscoveryConfig.OrgConfigOrBuilder getOrgConfigOrBuilder()

Only set when the parent is an org.

`.google.privacy.dlp.v2.DiscoveryConfig.OrgConfig org_config = 2;`

**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.OrgConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.OrgConfigOrBuilder)` |   
  
### getOtherCloudStartingLocation()
    
    
    public OtherCloudDiscoveryStartingLocation getOtherCloudStartingLocation()

Must be set only when scanning other clouds.

` .google.privacy.dlp.v2.OtherCloudDiscoveryStartingLocation other_cloud_starting_location = 12; `

**Returns**  
---  
**Type** | **Description**  
`[OtherCloudDiscoveryStartingLocation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.OtherCloudDiscoveryStartingLocation)` | The otherCloudStartingLocation.  
  
### getOtherCloudStartingLocationBuilder()
    
    
    public OtherCloudDiscoveryStartingLocation.Builder getOtherCloudStartingLocationBuilder()

Must be set only when scanning other clouds.

` .google.privacy.dlp.v2.OtherCloudDiscoveryStartingLocation other_cloud_starting_location = 12; `

**Returns**  
---  
**Type** | **Description**  
`[OtherCloudDiscoveryStartingLocation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.OtherCloudDiscoveryStartingLocation.Builder)` |   
  
### getOtherCloudStartingLocationOrBuilder()
    
    
    public OtherCloudDiscoveryStartingLocationOrBuilder getOtherCloudStartingLocationOrBuilder()

Must be set only when scanning other clouds.

` .google.privacy.dlp.v2.OtherCloudDiscoveryStartingLocation other_cloud_starting_location = 12; `

**Returns**  
---  
**Type** | **Description**  
`[OtherCloudDiscoveryStartingLocationOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.OtherCloudDiscoveryStartingLocationOrBuilder)` |   
  
### getProcessingLocation()
    
    
    public ProcessingLocation getProcessingLocation()

Optional. Processing location configuration. Vertex AI dataset scanning will set processing_location.image_fallback_type to MultiRegionProcessing by default.

` .google.privacy.dlp.v2.ProcessingLocation processing_location = 13 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ProcessingLocation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ProcessingLocation)` | The processingLocation.  
  
### getProcessingLocationBuilder()
    
    
    public ProcessingLocation.Builder getProcessingLocationBuilder()

Optional. Processing location configuration. Vertex AI dataset scanning will set processing_location.image_fallback_type to MultiRegionProcessing by default.

` .google.privacy.dlp.v2.ProcessingLocation processing_location = 13 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ProcessingLocation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ProcessingLocation.Builder)` |   
  
### getProcessingLocationOrBuilder()
    
    
    public ProcessingLocationOrBuilder getProcessingLocationOrBuilder()

Optional. Processing location configuration. Vertex AI dataset scanning will set processing_location.image_fallback_type to MultiRegionProcessing by default.

` .google.privacy.dlp.v2.ProcessingLocation processing_location = 13 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ProcessingLocationOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ProcessingLocationOrBuilder)` |   
  
### getStatus()
    
    
    public DiscoveryConfig.Status getStatus()

Required. A status for this configuration.

` .google.privacy.dlp.v2.DiscoveryConfig.Status status = 10 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Status](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Status)` | The status.  
  
### getStatusValue()
    
    
    public int getStatusValue()

Required. A status for this configuration.

` .google.privacy.dlp.v2.DiscoveryConfig.Status status = 10 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for status.  
  
### getTargets(int index)
    
    
    public DiscoveryTarget getTargets(int index)

Target to match against for determining what to scan and how frequently.

`repeated .google.privacy.dlp.v2.DiscoveryTarget targets = 5;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryTarget](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryTarget)` |   
  
### getTargetsBuilder(int index)
    
    
    public DiscoveryTarget.Builder getTargetsBuilder(int index)

Target to match against for determining what to scan and how frequently.

`repeated .google.privacy.dlp.v2.DiscoveryTarget targets = 5;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryTarget.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryTarget.Builder)` |   
  
### getTargetsBuilderList()
    
    
    public List<DiscoveryTarget.Builder> getTargetsBuilderList()

Target to match against for determining what to scan and how frequently.

`repeated .google.privacy.dlp.v2.DiscoveryTarget targets = 5;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryTarget.Builder)>` |   
  
### getTargetsCount()
    
    
    public int getTargetsCount()

Target to match against for determining what to scan and how frequently.

`repeated .google.privacy.dlp.v2.DiscoveryTarget targets = 5;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getTargetsList()
    
    
    public List<DiscoveryTarget> getTargetsList()

Target to match against for determining what to scan and how frequently.

`repeated .google.privacy.dlp.v2.DiscoveryTarget targets = 5;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[DiscoveryTarget](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryTarget)>` |   
  
### getTargetsOrBuilder(int index)
    
    
    public DiscoveryTargetOrBuilder getTargetsOrBuilder(int index)

Target to match against for determining what to scan and how frequently.

`repeated .google.privacy.dlp.v2.DiscoveryTarget targets = 5;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryTargetOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryTargetOrBuilder)` |   
  
### getTargetsOrBuilderList()
    
    
    public List<? extends DiscoveryTargetOrBuilder> getTargetsOrBuilderList()

Target to match against for determining what to scan and how frequently.

`repeated .google.privacy.dlp.v2.DiscoveryTarget targets = 5;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.privacy.dlp.v2.DiscoveryTargetOrBuilder>` |   
  
### getUpdateTime()
    
    
    public Timestamp getUpdateTime()

Output only. The last update timestamp of a DiscoveryConfig.

` .google.protobuf.Timestamp update_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The updateTime.  
  
### getUpdateTimeBuilder()
    
    
    public Timestamp.Builder getUpdateTimeBuilder()

Output only. The last update timestamp of a DiscoveryConfig.

` .google.protobuf.Timestamp update_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)` |   
  
### getUpdateTimeOrBuilder()
    
    
    public TimestampOrBuilder getUpdateTimeOrBuilder()

Output only. The last update timestamp of a DiscoveryConfig.

` .google.protobuf.Timestamp update_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### hasCreateTime()
    
    
    public boolean hasCreateTime()

Output only. The creation timestamp of a DiscoveryConfig.

` .google.protobuf.Timestamp create_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasLastRunTime()
    
    
    public boolean hasLastRunTime()

Output only. The timestamp of the last time this config was executed.

` .google.protobuf.Timestamp last_run_time = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the lastRunTime field is set.  
  
### hasOrgConfig()
    
    
    public boolean hasOrgConfig()

Only set when the parent is an org.

`.google.privacy.dlp.v2.DiscoveryConfig.OrgConfig org_config = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the orgConfig field is set.  
  
### hasOtherCloudStartingLocation()
    
    
    public boolean hasOtherCloudStartingLocation()

Must be set only when scanning other clouds.

` .google.privacy.dlp.v2.OtherCloudDiscoveryStartingLocation other_cloud_starting_location = 12; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the otherCloudStartingLocation field is set.  
  
### hasProcessingLocation()
    
    
    public boolean hasProcessingLocation()

Optional. Processing location configuration. Vertex AI dataset scanning will set processing_location.image_fallback_type to MultiRegionProcessing by default.

` .google.privacy.dlp.v2.ProcessingLocation processing_location = 13 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the processingLocation field is set.  
  
### hasUpdateTime()
    
    
    public boolean hasUpdateTime()

Output only. The last update timestamp of a DiscoveryConfig.

` .google.protobuf.Timestamp update_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

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

### isInitialized()
    
    
    public final boolean isInitialized()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.isInitialized()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_isInitialized__)

### mergeCreateTime(Timestamp value)
    
    
    public DiscoveryConfig.Builder mergeCreateTime(Timestamp value)

Output only. The creation timestamp of a DiscoveryConfig.

` .google.protobuf.Timestamp create_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` |   
  
### mergeFrom(DiscoveryConfig other)
    
    
    public DiscoveryConfig.Builder mergeFrom(DiscoveryConfig other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[DiscoveryConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public DiscoveryConfig.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public DiscoveryConfig.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### mergeLastRunTime(Timestamp value)
    
    
    public DiscoveryConfig.Builder mergeLastRunTime(Timestamp value)

Output only. The timestamp of the last time this config was executed.

` .google.protobuf.Timestamp last_run_time = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` |   
  
### mergeOrgConfig(DiscoveryConfig.OrgConfig value)
    
    
    public DiscoveryConfig.Builder mergeOrgConfig(DiscoveryConfig.OrgConfig value)

Only set when the parent is an org.

`.google.privacy.dlp.v2.DiscoveryConfig.OrgConfig org_config = 2;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[DiscoveryConfig.OrgConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.OrgConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` |   
  
### mergeOtherCloudStartingLocation(OtherCloudDiscoveryStartingLocation value)
    
    
    public DiscoveryConfig.Builder mergeOtherCloudStartingLocation(OtherCloudDiscoveryStartingLocation value)

Must be set only when scanning other clouds.

` .google.privacy.dlp.v2.OtherCloudDiscoveryStartingLocation other_cloud_starting_location = 12; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[OtherCloudDiscoveryStartingLocation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.OtherCloudDiscoveryStartingLocation)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` |   
  
### mergeProcessingLocation(ProcessingLocation value)
    
    
    public DiscoveryConfig.Builder mergeProcessingLocation(ProcessingLocation value)

Optional. Processing location configuration. Vertex AI dataset scanning will set processing_location.image_fallback_type to MultiRegionProcessing by default.

` .google.privacy.dlp.v2.ProcessingLocation processing_location = 13 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ProcessingLocation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ProcessingLocation)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` |   
  
### mergeUpdateTime(Timestamp value)
    
    
    public DiscoveryConfig.Builder mergeUpdateTime(Timestamp value)

Output only. The last update timestamp of a DiscoveryConfig.

` .google.protobuf.Timestamp update_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` |   
  
### removeActions(int index)
    
    
    public DiscoveryConfig.Builder removeActions(int index)

Actions to execute at the completion of scanning.

`repeated .google.privacy.dlp.v2.DataProfileAction actions = 4;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` |   
  
### removeErrors(int index)
    
    
    public DiscoveryConfig.Builder removeErrors(int index)

Output only. A stream of errors encountered when the config was activated. Repeated errors may result in the config automatically being paused. Output only field. Will return the last 100 errors. Whenever the config is modified this list will be cleared.

` repeated .google.privacy.dlp.v2.Error errors = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` |   
  
### removeTargets(int index)
    
    
    public DiscoveryConfig.Builder removeTargets(int index)

Target to match against for determining what to scan and how frequently.

`repeated .google.privacy.dlp.v2.DiscoveryTarget targets = 5;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` |   
  
### setActions(int index, DataProfileAction value)
    
    
    public DiscoveryConfig.Builder setActions(int index, DataProfileAction value)

Actions to execute at the completion of scanning.

`repeated .google.privacy.dlp.v2.DataProfileAction actions = 4;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[DataProfileAction](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DataProfileAction)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` |   
  
### setActions(int index, DataProfileAction.Builder builderForValue)
    
    
    public DiscoveryConfig.Builder setActions(int index, DataProfileAction.Builder builderForValue)

Actions to execute at the completion of scanning.

`repeated .google.privacy.dlp.v2.DataProfileAction actions = 4;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[DataProfileAction.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DataProfileAction.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` |   
  
### setCreateTime(Timestamp value)
    
    
    public DiscoveryConfig.Builder setCreateTime(Timestamp value)

Output only. The creation timestamp of a DiscoveryConfig.

` .google.protobuf.Timestamp create_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` |   
  
### setCreateTime(Timestamp.Builder builderForValue)
    
    
    public DiscoveryConfig.Builder setCreateTime(Timestamp.Builder builderForValue)

Output only. The creation timestamp of a DiscoveryConfig.

` .google.protobuf.Timestamp create_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` |   
  
### setDisplayName(String value)
    
    
    public DiscoveryConfig.Builder setDisplayName(String value)

Display name (max 100 chars)

`string display_name = 11;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The displayName to set.  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` | This builder for chaining.  
  
### setDisplayNameBytes(ByteString value)
    
    
    public DiscoveryConfig.Builder setDisplayNameBytes(ByteString value)

Display name (max 100 chars)

`string display_name = 11;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for displayName to set.  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` | This builder for chaining.  
  
### setErrors(int index, Error value)
    
    
    public DiscoveryConfig.Builder setErrors(int index, Error value)

Output only. A stream of errors encountered when the config was activated. Repeated errors may result in the config automatically being paused. Output only field. Will return the last 100 errors. Whenever the config is modified this list will be cleared.

` repeated .google.privacy.dlp.v2.Error errors = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[Error](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Error)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` |   
  
### setErrors(int index, Error.Builder builderForValue)
    
    
    public DiscoveryConfig.Builder setErrors(int index, Error.Builder builderForValue)

Output only. A stream of errors encountered when the config was activated. Repeated errors may result in the config automatically being paused. Output only field. Will return the last 100 errors. Whenever the config is modified this list will be cleared.

` repeated .google.privacy.dlp.v2.Error errors = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[Error.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Error.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` |   
  
### setInspectTemplates(int index, String value)
    
    
    public DiscoveryConfig.Builder setInspectTemplates(int index, String value)

Detection logic for profile generation.

Not all template features are used by Discovery. FindingLimits, include_quote and exclude_info_types have no impact on Discovery.

Multiple templates may be provided if there is data in multiple regions. At most one template must be specified per-region (including "global"). Each region is scanned using the applicable template. If no region-specific template is specified, but a "global" template is specified, it will be copied to that region and used instead. If no global or region-specific template is provided for a region with data, that region's data will not be scanned.

For more information, see <https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#data-residency>.

`repeated string inspect_templates = 3;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index to set the value at.  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The inspectTemplates to set.  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` | This builder for chaining.  
  
### setLastRunTime(Timestamp value)
    
    
    public DiscoveryConfig.Builder setLastRunTime(Timestamp value)

Output only. The timestamp of the last time this config was executed.

` .google.protobuf.Timestamp last_run_time = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` |   
  
### setLastRunTime(Timestamp.Builder builderForValue)
    
    
    public DiscoveryConfig.Builder setLastRunTime(Timestamp.Builder builderForValue)

Output only. The timestamp of the last time this config was executed.

` .google.protobuf.Timestamp last_run_time = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` |   
  
### setName(String value)
    
    
    public DiscoveryConfig.Builder setName(String value)

Output only. Unique resource name for the DiscoveryConfig, assigned by the service when the DiscoveryConfig is created, for example `projects/dlp-test-project/locations/global/discoveryConfigs/53234423`.

`string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name to set.  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` | This builder for chaining.  
  
### setNameBytes(ByteString value)
    
    
    public DiscoveryConfig.Builder setNameBytes(ByteString value)

Output only. Unique resource name for the DiscoveryConfig, assigned by the service when the DiscoveryConfig is created, for example `projects/dlp-test-project/locations/global/discoveryConfigs/53234423`.

`string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for name to set.  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` | This builder for chaining.  
  
### setOrgConfig(DiscoveryConfig.OrgConfig value)
    
    
    public DiscoveryConfig.Builder setOrgConfig(DiscoveryConfig.OrgConfig value)

Only set when the parent is an org.

`.google.privacy.dlp.v2.DiscoveryConfig.OrgConfig org_config = 2;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[DiscoveryConfig.OrgConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.OrgConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` |   
  
### setOrgConfig(DiscoveryConfig.OrgConfig.Builder builderForValue)
    
    
    public DiscoveryConfig.Builder setOrgConfig(DiscoveryConfig.OrgConfig.Builder builderForValue)

Only set when the parent is an org.

`.google.privacy.dlp.v2.DiscoveryConfig.OrgConfig org_config = 2;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[DiscoveryConfig.OrgConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.OrgConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` |   
  
### setOtherCloudStartingLocation(OtherCloudDiscoveryStartingLocation value)
    
    
    public DiscoveryConfig.Builder setOtherCloudStartingLocation(OtherCloudDiscoveryStartingLocation value)

Must be set only when scanning other clouds.

` .google.privacy.dlp.v2.OtherCloudDiscoveryStartingLocation other_cloud_starting_location = 12; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[OtherCloudDiscoveryStartingLocation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.OtherCloudDiscoveryStartingLocation)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` |   
  
### setOtherCloudStartingLocation(OtherCloudDiscoveryStartingLocation.Builder builderForValue)
    
    
    public DiscoveryConfig.Builder setOtherCloudStartingLocation(OtherCloudDiscoveryStartingLocation.Builder builderForValue)

Must be set only when scanning other clouds.

` .google.privacy.dlp.v2.OtherCloudDiscoveryStartingLocation other_cloud_starting_location = 12; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[OtherCloudDiscoveryStartingLocation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.OtherCloudDiscoveryStartingLocation.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` |   
  
### setProcessingLocation(ProcessingLocation value)
    
    
    public DiscoveryConfig.Builder setProcessingLocation(ProcessingLocation value)

Optional. Processing location configuration. Vertex AI dataset scanning will set processing_location.image_fallback_type to MultiRegionProcessing by default.

` .google.privacy.dlp.v2.ProcessingLocation processing_location = 13 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ProcessingLocation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ProcessingLocation)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` |   
  
### setProcessingLocation(ProcessingLocation.Builder builderForValue)
    
    
    public DiscoveryConfig.Builder setProcessingLocation(ProcessingLocation.Builder builderForValue)

Optional. Processing location configuration. Vertex AI dataset scanning will set processing_location.image_fallback_type to MultiRegionProcessing by default.

` .google.privacy.dlp.v2.ProcessingLocation processing_location = 13 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[ProcessingLocation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ProcessingLocation.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` |   
  
### setStatus(DiscoveryConfig.Status value)
    
    
    public DiscoveryConfig.Builder setStatus(DiscoveryConfig.Status value)

Required. A status for this configuration.

` .google.privacy.dlp.v2.DiscoveryConfig.Status status = 10 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[DiscoveryConfig.Status](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Status)`  
The status to set.  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` | This builder for chaining.  
  
### setStatusValue(int value)
    
    
    public DiscoveryConfig.Builder setStatusValue(int value)

Required. A status for this configuration.

` .google.privacy.dlp.v2.DiscoveryConfig.Status status = 10 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The enum numeric value on the wire for status to set.  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` | This builder for chaining.  
  
### setTargets(int index, DiscoveryTarget value)
    
    
    public DiscoveryConfig.Builder setTargets(int index, DiscoveryTarget value)

Target to match against for determining what to scan and how frequently.

`repeated .google.privacy.dlp.v2.DiscoveryTarget targets = 5;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[DiscoveryTarget](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryTarget)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` |   
  
### setTargets(int index, DiscoveryTarget.Builder builderForValue)
    
    
    public DiscoveryConfig.Builder setTargets(int index, DiscoveryTarget.Builder builderForValue)

Target to match against for determining what to scan and how frequently.

`repeated .google.privacy.dlp.v2.DiscoveryTarget targets = 5;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[DiscoveryTarget.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryTarget.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` |   
  
### setUpdateTime(Timestamp value)
    
    
    public DiscoveryConfig.Builder setUpdateTime(Timestamp value)

Output only. The last update timestamp of a DiscoveryConfig.

` .google.protobuf.Timestamp update_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` |   
  
### setUpdateTime(Timestamp.Builder builderForValue)
    
    
    public DiscoveryConfig.Builder setUpdateTime(Timestamp.Builder builderForValue)

Output only. The last update timestamp of a DiscoveryConfig.

` .google.protobuf.Timestamp update_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DiscoveryConfig.Builder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
