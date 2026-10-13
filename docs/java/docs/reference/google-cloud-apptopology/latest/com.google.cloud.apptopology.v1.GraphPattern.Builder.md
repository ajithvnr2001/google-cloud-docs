---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-apptopology/latest/com.google.cloud.apptopology.v1.GraphPattern.Builder
title: Class GraphPattern.Builder (0.3.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:10:50.247734+00:00
---

# Class GraphPattern.Builder (0.3.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-apptopology/latest/com.google.cloud.apptopology.v1.GraphPattern.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class GraphPattern.Builder (0.3.0) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public static final class GraphPattern.Builder extends GeneratedMessage.Builder<GraphPattern.Builder> implements GraphPatternOrBuilder

Recursive graph pattern matcher to select and constrain the returned topology. AppTopology API allows cycle in the graph traversal and will return unique node and edge results in the response. SLO is guaranteed for at most 5 hops in the graph traversal.

Protobuf type `google.cloud.apptopology.v1.GraphPattern`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > GraphPattern.Builder

## Implements

[GraphPatternOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apptopology/latest/com.google.cloud.apptopology.v1.GraphPatternOrBuilder)

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

### addAllNeighbors(Iterable<? extends ConnectedNodePattern> values)
    
    
    public GraphPattern.Builder addAllNeighbors(Iterable<? extends ConnectedNodePattern> values)

Optional. Pattern matcher to match the connected subgraphs; all of these are ANDed.

` repeated .google.cloud.apptopology.v1.ConnectedNodePattern neighbors = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<? extends com.google.cloud.apptopology.v1.ConnectedNodePattern>`  
  
**Returns**  
---  
**Type** | **Description**  
`[GraphPattern.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apptopology/latest/com.google.cloud.apptopology.v1.GraphPattern.Builder)` |   
  
### addNeighbors(ConnectedNodePattern value)
    
    
    public GraphPattern.Builder addNeighbors(ConnectedNodePattern value)

Optional. Pattern matcher to match the connected subgraphs; all of these are ANDed.

` repeated .google.cloud.apptopology.v1.ConnectedNodePattern neighbors = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ConnectedNodePattern](https://docs.cloud.google.com/java/docs/reference/google-cloud-apptopology/latest/com.google.cloud.apptopology.v1.ConnectedNodePattern)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GraphPattern.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apptopology/latest/com.google.cloud.apptopology.v1.GraphPattern.Builder)` |   
  
### addNeighbors(ConnectedNodePattern.Builder builderForValue)
    
    
    public GraphPattern.Builder addNeighbors(ConnectedNodePattern.Builder builderForValue)

Optional. Pattern matcher to match the connected subgraphs; all of these are ANDed.

` repeated .google.cloud.apptopology.v1.ConnectedNodePattern neighbors = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[ConnectedNodePattern.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apptopology/latest/com.google.cloud.apptopology.v1.ConnectedNodePattern.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GraphPattern.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apptopology/latest/com.google.cloud.apptopology.v1.GraphPattern.Builder)` |   
  
### addNeighbors(int index, ConnectedNodePattern value)
    
    
    public GraphPattern.Builder addNeighbors(int index, ConnectedNodePattern value)

Optional. Pattern matcher to match the connected subgraphs; all of these are ANDed.

` repeated .google.cloud.apptopology.v1.ConnectedNodePattern neighbors = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[ConnectedNodePattern](https://docs.cloud.google.com/java/docs/reference/google-cloud-apptopology/latest/com.google.cloud.apptopology.v1.ConnectedNodePattern)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GraphPattern.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apptopology/latest/com.google.cloud.apptopology.v1.GraphPattern.Builder)` |   
  
### addNeighbors(int index, ConnectedNodePattern.Builder builderForValue)
    
    
    public GraphPattern.Builder addNeighbors(int index, ConnectedNodePattern.Builder builderForValue)

Optional. Pattern matcher to match the connected subgraphs; all of these are ANDed.

` repeated .google.cloud.apptopology.v1.ConnectedNodePattern neighbors = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[ConnectedNodePattern.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apptopology/latest/com.google.cloud.apptopology.v1.ConnectedNodePattern.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GraphPattern.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apptopology/latest/com.google.cloud.apptopology.v1.GraphPattern.Builder)` |   
  
### addNeighborsBuilder()
    
    
    public ConnectedNodePattern.Builder addNeighborsBuilder()

Optional. Pattern matcher to match the connected subgraphs; all of these are ANDed.

` repeated .google.cloud.apptopology.v1.ConnectedNodePattern neighbors = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ConnectedNodePattern.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apptopology/latest/com.google.cloud.apptopology.v1.ConnectedNodePattern.Builder)` |   
  
### addNeighborsBuilder(int index)
    
    
    public ConnectedNodePattern.Builder addNeighborsBuilder(int index)

Optional. Pattern matcher to match the connected subgraphs; all of these are ANDed.

` repeated .google.cloud.apptopology.v1.ConnectedNodePattern neighbors = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConnectedNodePattern.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apptopology/latest/com.google.cloud.apptopology.v1.ConnectedNodePattern.Builder)` |   
  
### build()
    
    
    public GraphPattern build()

**Returns**  
---  
**Type** | **Description**  
`[GraphPattern](https://docs.cloud.google.com/java/docs/reference/google-cloud-apptopology/latest/com.google.cloud.apptopology.v1.GraphPattern)` |   
  
### buildPartial()
    
    
    public GraphPattern buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[GraphPattern](https://docs.cloud.google.com/java/docs/reference/google-cloud-apptopology/latest/com.google.cloud.apptopology.v1.GraphPattern)` |   
  
### clear()
    
    
    public GraphPattern.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[GraphPattern.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apptopology/latest/com.google.cloud.apptopology.v1.GraphPattern.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearNeighbors()
    
    
    public GraphPattern.Builder clearNeighbors()

Optional. Pattern matcher to match the connected subgraphs; all of these are ANDed.

` repeated .google.cloud.apptopology.v1.ConnectedNodePattern neighbors = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[GraphPattern.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apptopology/latest/com.google.cloud.apptopology.v1.GraphPattern.Builder)` |   
  
### clearStartingNode()
    
    
    public GraphPattern.Builder clearStartingNode()

Required. Pattern matcher to select the starting nodes in the graph.

` .google.cloud.apptopology.v1.NodePattern starting_node = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[GraphPattern.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apptopology/latest/com.google.cloud.apptopology.v1.GraphPattern.Builder)` |   
  
### getDefaultInstanceForType()
    
    
    public GraphPattern getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[GraphPattern](https://docs.cloud.google.com/java/docs/reference/google-cloud-apptopology/latest/com.google.cloud.apptopology.v1.GraphPattern)` |   
  
### getDescriptorForType()
    
    
    public Descriptors.Descriptor getDescriptorForType()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getDescriptorForType__)

### getNeighbors(int index)
    
    
    public ConnectedNodePattern getNeighbors(int index)

Optional. Pattern matcher to match the connected subgraphs; all of these are ANDed.

` repeated .google.cloud.apptopology.v1.ConnectedNodePattern neighbors = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConnectedNodePattern](https://docs.cloud.google.com/java/docs/reference/google-cloud-apptopology/latest/com.google.cloud.apptopology.v1.ConnectedNodePattern)` |   
  
### getNeighborsBuilder(int index)
    
    
    public ConnectedNodePattern.Builder getNeighborsBuilder(int index)

Optional. Pattern matcher to match the connected subgraphs; all of these are ANDed.

` repeated .google.cloud.apptopology.v1.ConnectedNodePattern neighbors = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConnectedNodePattern.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apptopology/latest/com.google.cloud.apptopology.v1.ConnectedNodePattern.Builder)` |   
  
### getNeighborsBuilderList()
    
    
    public List<ConnectedNodePattern.Builder> getNeighborsBuilderList()

Optional. Pattern matcher to match the connected subgraphs; all of these are ANDed.

` repeated .google.cloud.apptopology.v1.ConnectedNodePattern neighbors = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apptopology/latest/com.google.cloud.apptopology.v1.ConnectedNodePattern.Builder)>` |   
  
### getNeighborsCount()
    
    
    public int getNeighborsCount()

Optional. Pattern matcher to match the connected subgraphs; all of these are ANDed.

` repeated .google.cloud.apptopology.v1.ConnectedNodePattern neighbors = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getNeighborsList()
    
    
    public List<ConnectedNodePattern> getNeighborsList()

Optional. Pattern matcher to match the connected subgraphs; all of these are ANDed.

` repeated .google.cloud.apptopology.v1.ConnectedNodePattern neighbors = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ConnectedNodePattern](https://docs.cloud.google.com/java/docs/reference/google-cloud-apptopology/latest/com.google.cloud.apptopology.v1.ConnectedNodePattern)>` |   
  
### getNeighborsOrBuilder(int index)
    
    
    public ConnectedNodePatternOrBuilder getNeighborsOrBuilder(int index)

Optional. Pattern matcher to match the connected subgraphs; all of these are ANDed.

` repeated .google.cloud.apptopology.v1.ConnectedNodePattern neighbors = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConnectedNodePatternOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apptopology/latest/com.google.cloud.apptopology.v1.ConnectedNodePatternOrBuilder)` |   
  
### getNeighborsOrBuilderList()
    
    
    public List<? extends ConnectedNodePatternOrBuilder> getNeighborsOrBuilderList()

Optional. Pattern matcher to match the connected subgraphs; all of these are ANDed.

` repeated .google.cloud.apptopology.v1.ConnectedNodePattern neighbors = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.apptopology.v1.ConnectedNodePatternOrBuilder>` |   
  
### getStartingNode()
    
    
    public NodePattern getStartingNode()

Required. Pattern matcher to select the starting nodes in the graph.

` .google.cloud.apptopology.v1.NodePattern starting_node = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[NodePattern](https://docs.cloud.google.com/java/docs/reference/google-cloud-apptopology/latest/com.google.cloud.apptopology.v1.NodePattern)` | The startingNode.  
  
### getStartingNodeBuilder()
    
    
    public NodePattern.Builder getStartingNodeBuilder()

Required. Pattern matcher to select the starting nodes in the graph.

` .google.cloud.apptopology.v1.NodePattern starting_node = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[NodePattern.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apptopology/latest/com.google.cloud.apptopology.v1.NodePattern.Builder)` |   
  
### getStartingNodeOrBuilder()
    
    
    public NodePatternOrBuilder getStartingNodeOrBuilder()

Required. Pattern matcher to select the starting nodes in the graph.

` .google.cloud.apptopology.v1.NodePattern starting_node = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[NodePatternOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apptopology/latest/com.google.cloud.apptopology.v1.NodePatternOrBuilder)` |   
  
### hasStartingNode()
    
    
    public boolean hasStartingNode()

Required. Pattern matcher to select the starting nodes in the graph.

` .google.cloud.apptopology.v1.NodePattern starting_node = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the startingNode field is set.  
  
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

### mergeFrom(GraphPattern other)
    
    
    public GraphPattern.Builder mergeFrom(GraphPattern other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[GraphPattern](https://docs.cloud.google.com/java/docs/reference/google-cloud-apptopology/latest/com.google.cloud.apptopology.v1.GraphPattern)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GraphPattern.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apptopology/latest/com.google.cloud.apptopology.v1.GraphPattern.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public GraphPattern.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GraphPattern.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apptopology/latest/com.google.cloud.apptopology.v1.GraphPattern.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public GraphPattern.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GraphPattern.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apptopology/latest/com.google.cloud.apptopology.v1.GraphPattern.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### mergeStartingNode(NodePattern value)
    
    
    public GraphPattern.Builder mergeStartingNode(NodePattern value)

Required. Pattern matcher to select the starting nodes in the graph.

` .google.cloud.apptopology.v1.NodePattern starting_node = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[NodePattern](https://docs.cloud.google.com/java/docs/reference/google-cloud-apptopology/latest/com.google.cloud.apptopology.v1.NodePattern)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GraphPattern.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apptopology/latest/com.google.cloud.apptopology.v1.GraphPattern.Builder)` |   
  
### removeNeighbors(int index)
    
    
    public GraphPattern.Builder removeNeighbors(int index)

Optional. Pattern matcher to match the connected subgraphs; all of these are ANDed.

` repeated .google.cloud.apptopology.v1.ConnectedNodePattern neighbors = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GraphPattern.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apptopology/latest/com.google.cloud.apptopology.v1.GraphPattern.Builder)` |   
  
### setNeighbors(int index, ConnectedNodePattern value)
    
    
    public GraphPattern.Builder setNeighbors(int index, ConnectedNodePattern value)

Optional. Pattern matcher to match the connected subgraphs; all of these are ANDed.

` repeated .google.cloud.apptopology.v1.ConnectedNodePattern neighbors = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[ConnectedNodePattern](https://docs.cloud.google.com/java/docs/reference/google-cloud-apptopology/latest/com.google.cloud.apptopology.v1.ConnectedNodePattern)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GraphPattern.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apptopology/latest/com.google.cloud.apptopology.v1.GraphPattern.Builder)` |   
  
### setNeighbors(int index, ConnectedNodePattern.Builder builderForValue)
    
    
    public GraphPattern.Builder setNeighbors(int index, ConnectedNodePattern.Builder builderForValue)

Optional. Pattern matcher to match the connected subgraphs; all of these are ANDed.

` repeated .google.cloud.apptopology.v1.ConnectedNodePattern neighbors = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[ConnectedNodePattern.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apptopology/latest/com.google.cloud.apptopology.v1.ConnectedNodePattern.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GraphPattern.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apptopology/latest/com.google.cloud.apptopology.v1.GraphPattern.Builder)` |   
  
### setStartingNode(NodePattern value)
    
    
    public GraphPattern.Builder setStartingNode(NodePattern value)

Required. Pattern matcher to select the starting nodes in the graph.

` .google.cloud.apptopology.v1.NodePattern starting_node = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[NodePattern](https://docs.cloud.google.com/java/docs/reference/google-cloud-apptopology/latest/com.google.cloud.apptopology.v1.NodePattern)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GraphPattern.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apptopology/latest/com.google.cloud.apptopology.v1.GraphPattern.Builder)` |   
  
### setStartingNode(NodePattern.Builder builderForValue)
    
    
    public GraphPattern.Builder setStartingNode(NodePattern.Builder builderForValue)

Required. Pattern matcher to select the starting nodes in the graph.

` .google.cloud.apptopology.v1.NodePattern starting_node = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[NodePattern.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apptopology/latest/com.google.cloud.apptopology.v1.NodePattern.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GraphPattern.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apptopology/latest/com.google.cloud.apptopology.v1.GraphPattern.Builder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
