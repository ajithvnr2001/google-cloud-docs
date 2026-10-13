---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroup.Builder
title: Class InstanceGroup.Builder (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:56:20.572388+00:00
---

# Class InstanceGroup.Builder (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroup.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class InstanceGroup.Builder (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 
    
    
    public static final class InstanceGroup.Builder extends GeneratedMessage.Builder<InstanceGroup.Builder> implements InstanceGroupOrBuilder

Represents an Instance Group resource.

Instance Groups can be used to configure a target forload balancing.

Instance groups can either be managed or unmanaged.

To create managed instance groups, use the instanceGroupManager orregionInstanceGroupManager resource instead.

Use zonal unmanaged instance groups if you need to applyload balancing to groups of heterogeneous instances or if you need to manage the instances yourself. You cannot create regional unmanaged instance groups.

For more information, readInstance groups.

Protobuf type `google.cloud.compute.v1.InstanceGroup`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > InstanceGroup.Builder

## Implements

[InstanceGroupOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupOrBuilder)

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

### addAllNamedPorts(Iterable<? extends NamedPort> values)
    
    
    public InstanceGroup.Builder addAllNamedPorts(Iterable<? extends NamedPort> values)

Optional. Assigns a name to a port number. For example:{name: "http", port: 80}

This allows the system to reference ports by the assigned name instead of a port number. Named ports can also contain multiple ports. For example:[{name: "app1", port: 8080}, {name: "app1", port: 8081}, {name: "app2", port: 8082}]

Named ports apply to all instances in this instance group.

`repeated .google.cloud.compute.v1.NamedPort named_ports = 427598732;`

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<? extends com.google.cloud.compute.v1.NamedPort>`  
  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroup.Builder)` |   
  
### addNamedPorts(NamedPort value)
    
    
    public InstanceGroup.Builder addNamedPorts(NamedPort value)

Optional. Assigns a name to a port number. For example:{name: "http", port: 80}

This allows the system to reference ports by the assigned name instead of a port number. Named ports can also contain multiple ports. For example:[{name: "app1", port: 8080}, {name: "app1", port: 8081}, {name: "app2", port: 8082}]

Named ports apply to all instances in this instance group.

`repeated .google.cloud.compute.v1.NamedPort named_ports = 427598732;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[NamedPort](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NamedPort)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroup.Builder)` |   
  
### addNamedPorts(NamedPort.Builder builderForValue)
    
    
    public InstanceGroup.Builder addNamedPorts(NamedPort.Builder builderForValue)

Optional. Assigns a name to a port number. For example:{name: "http", port: 80}

This allows the system to reference ports by the assigned name instead of a port number. Named ports can also contain multiple ports. For example:[{name: "app1", port: 8080}, {name: "app1", port: 8081}, {name: "app2", port: 8082}]

Named ports apply to all instances in this instance group.

`repeated .google.cloud.compute.v1.NamedPort named_ports = 427598732;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[NamedPort.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NamedPort.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroup.Builder)` |   
  
### addNamedPorts(int index, NamedPort value)
    
    
    public InstanceGroup.Builder addNamedPorts(int index, NamedPort value)

Optional. Assigns a name to a port number. For example:{name: "http", port: 80}

This allows the system to reference ports by the assigned name instead of a port number. Named ports can also contain multiple ports. For example:[{name: "app1", port: 8080}, {name: "app1", port: 8081}, {name: "app2", port: 8082}]

Named ports apply to all instances in this instance group.

`repeated .google.cloud.compute.v1.NamedPort named_ports = 427598732;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[NamedPort](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NamedPort)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroup.Builder)` |   
  
### addNamedPorts(int index, NamedPort.Builder builderForValue)
    
    
    public InstanceGroup.Builder addNamedPorts(int index, NamedPort.Builder builderForValue)

Optional. Assigns a name to a port number. For example:{name: "http", port: 80}

This allows the system to reference ports by the assigned name instead of a port number. Named ports can also contain multiple ports. For example:[{name: "app1", port: 8080}, {name: "app1", port: 8081}, {name: "app2", port: 8082}]

Named ports apply to all instances in this instance group.

`repeated .google.cloud.compute.v1.NamedPort named_ports = 427598732;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[NamedPort.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NamedPort.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroup.Builder)` |   
  
### addNamedPortsBuilder()
    
    
    public NamedPort.Builder addNamedPortsBuilder()

Optional. Assigns a name to a port number. For example:{name: "http", port: 80}

This allows the system to reference ports by the assigned name instead of a port number. Named ports can also contain multiple ports. For example:[{name: "app1", port: 8080}, {name: "app1", port: 8081}, {name: "app2", port: 8082}]

Named ports apply to all instances in this instance group.

`repeated .google.cloud.compute.v1.NamedPort named_ports = 427598732;`

**Returns**  
---  
**Type** | **Description**  
`[NamedPort.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NamedPort.Builder)` |   
  
### addNamedPortsBuilder(int index)
    
    
    public NamedPort.Builder addNamedPortsBuilder(int index)

Optional. Assigns a name to a port number. For example:{name: "http", port: 80}

This allows the system to reference ports by the assigned name instead of a port number. Named ports can also contain multiple ports. For example:[{name: "app1", port: 8080}, {name: "app1", port: 8081}, {name: "app2", port: 8082}]

Named ports apply to all instances in this instance group.

`repeated .google.cloud.compute.v1.NamedPort named_ports = 427598732;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[NamedPort.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NamedPort.Builder)` |   
  
### build()
    
    
    public InstanceGroup build()

**Returns**  
---  
**Type** | **Description**  
`[InstanceGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroup)` |   
  
### buildPartial()
    
    
    public InstanceGroup buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[InstanceGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroup)` |   
  
### clear()
    
    
    public InstanceGroup.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[InstanceGroup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroup.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearCreationTimestamp()
    
    
    public InstanceGroup.Builder clearCreationTimestamp()

Output only. [Output Only] The creation timestamp for this instance group inRFC3339 text format.

`optional string creation_timestamp = 30525366;`

**Returns**  
---  
**Type** | **Description**  
`[InstanceGroup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroup.Builder)` | This builder for chaining.  
  
### clearDescription()
    
    
    public InstanceGroup.Builder clearDescription()

An optional description of this resource. Provide this property when you create the resource.

`optional string description = 422937596;`

**Returns**  
---  
**Type** | **Description**  
`[InstanceGroup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroup.Builder)` | This builder for chaining.  
  
### clearFingerprint()
    
    
    public InstanceGroup.Builder clearFingerprint()

Output only. [Output Only] The fingerprint of the named ports. The system uses this fingerprint to detect conflicts when multiple users change the named ports concurrently.

`optional string fingerprint = 234678500;`

**Returns**  
---  
**Type** | **Description**  
`[InstanceGroup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroup.Builder)` | This builder for chaining.  
  
### clearId()
    
    
    public InstanceGroup.Builder clearId()

Output only. [Output Only] A unique identifier for this instance group, generated by the server.

`optional uint64 id = 3355;`

**Returns**  
---  
**Type** | **Description**  
`[InstanceGroup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroup.Builder)` | This builder for chaining.  
  
### clearKind()
    
    
    public InstanceGroup.Builder clearKind()

Output only. [Output Only] The resource type, which is alwayscompute#instanceGroup for instance groups.

`optional string kind = 3292052;`

**Returns**  
---  
**Type** | **Description**  
`[InstanceGroup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroup.Builder)` | This builder for chaining.  
  
### clearName()
    
    
    public InstanceGroup.Builder clearName()

The name of the instance group. The name must be 1-63 characters long, and comply withRFC1035.

`optional string name = 3373707;`

**Returns**  
---  
**Type** | **Description**  
`[InstanceGroup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroup.Builder)` | This builder for chaining.  
  
### clearNamedPorts()
    
    
    public InstanceGroup.Builder clearNamedPorts()

Optional. Assigns a name to a port number. For example:{name: "http", port: 80}

This allows the system to reference ports by the assigned name instead of a port number. Named ports can also contain multiple ports. For example:[{name: "app1", port: 8080}, {name: "app1", port: 8081}, {name: "app2", port: 8082}]

Named ports apply to all instances in this instance group.

`repeated .google.cloud.compute.v1.NamedPort named_ports = 427598732;`

**Returns**  
---  
**Type** | **Description**  
`[InstanceGroup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroup.Builder)` |   
  
### clearNetwork()
    
    
    public InstanceGroup.Builder clearNetwork()

[Output Only] The URL of the network to which all instances in the instance group belong. If your instance has multiple network interfaces, then the network and subnetwork fields only refer to the network and subnet used by your primary interface (nic0).

`optional string network = 232872494;`

**Returns**  
---  
**Type** | **Description**  
`[InstanceGroup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroup.Builder)` | This builder for chaining.  
  
### clearRegion()
    
    
    public InstanceGroup.Builder clearRegion()

Output only. [Output Only] The URL of theregion where the instance group is located (for regional resources).

`optional string region = 138946292;`

**Returns**  
---  
**Type** | **Description**  
`[InstanceGroup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroup.Builder)` | This builder for chaining.  
  
### clearSelfLink()
    
    
    public InstanceGroup.Builder clearSelfLink()

Output only. [Output Only] The URL for this instance group. The server generates this URL.

`optional string self_link = 456214797;`

**Returns**  
---  
**Type** | **Description**  
`[InstanceGroup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroup.Builder)` | This builder for chaining.  
  
### clearSize()
    
    
    public InstanceGroup.Builder clearSize()

Output only. [Output Only] The total number of instances in the instance group.

`optional int32 size = 3530753;`

**Returns**  
---  
**Type** | **Description**  
`[InstanceGroup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroup.Builder)` | This builder for chaining.  
  
### clearSubnetwork()
    
    
    public InstanceGroup.Builder clearSubnetwork()

Output only. [Output Only] The URL of the subnetwork to which all instances in the instance group belong. If your instance has multiple network interfaces, then the network and subnetwork fields only refer to the network and subnet used by your primary interface (nic0).

`optional string subnetwork = 307827694;`

**Returns**  
---  
**Type** | **Description**  
`[InstanceGroup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroup.Builder)` | This builder for chaining.  
  
### clearZone()
    
    
    public InstanceGroup.Builder clearZone()

Output only. [Output Only] The URL of thezone where the instance group is located (for zonal resources).

`optional string zone = 3744684;`

**Returns**  
---  
**Type** | **Description**  
`[InstanceGroup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroup.Builder)` | This builder for chaining.  
  
### getCreationTimestamp()
    
    
    public String getCreationTimestamp()

Output only. [Output Only] The creation timestamp for this instance group inRFC3339 text format.

`optional string creation_timestamp = 30525366;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The creationTimestamp.  
  
### getCreationTimestampBytes()
    
    
    public ByteString getCreationTimestampBytes()

Output only. [Output Only] The creation timestamp for this instance group inRFC3339 text format.

`optional string creation_timestamp = 30525366;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for creationTimestamp.  
  
### getDefaultInstanceForType()
    
    
    public InstanceGroup getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[InstanceGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroup)` |   
  
### getDescription()
    
    
    public String getDescription()

An optional description of this resource. Provide this property when you create the resource.

`optional string description = 422937596;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The description.  
  
### getDescriptionBytes()
    
    
    public ByteString getDescriptionBytes()

An optional description of this resource. Provide this property when you create the resource.

`optional string description = 422937596;`

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

### getFingerprint()
    
    
    public String getFingerprint()

Output only. [Output Only] The fingerprint of the named ports. The system uses this fingerprint to detect conflicts when multiple users change the named ports concurrently.

`optional string fingerprint = 234678500;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The fingerprint.  
  
### getFingerprintBytes()
    
    
    public ByteString getFingerprintBytes()

Output only. [Output Only] The fingerprint of the named ports. The system uses this fingerprint to detect conflicts when multiple users change the named ports concurrently.

`optional string fingerprint = 234678500;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for fingerprint.  
  
### getId()
    
    
    public long getId()

Output only. [Output Only] A unique identifier for this instance group, generated by the server.

`optional uint64 id = 3355;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The id.  
  
### getKind()
    
    
    public String getKind()

Output only. [Output Only] The resource type, which is alwayscompute#instanceGroup for instance groups.

`optional string kind = 3292052;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The kind.  
  
### getKindBytes()
    
    
    public ByteString getKindBytes()

Output only. [Output Only] The resource type, which is alwayscompute#instanceGroup for instance groups.

`optional string kind = 3292052;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for kind.  
  
### getName()
    
    
    public String getName()

The name of the instance group. The name must be 1-63 characters long, and comply withRFC1035.

`optional string name = 3373707;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public ByteString getNameBytes()

The name of the instance group. The name must be 1-63 characters long, and comply withRFC1035.

`optional string name = 3373707;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getNamedPorts(int index)
    
    
    public NamedPort getNamedPorts(int index)

Optional. Assigns a name to a port number. For example:{name: "http", port: 80}

This allows the system to reference ports by the assigned name instead of a port number. Named ports can also contain multiple ports. For example:[{name: "app1", port: 8080}, {name: "app1", port: 8081}, {name: "app2", port: 8082}]

Named ports apply to all instances in this instance group.

`repeated .google.cloud.compute.v1.NamedPort named_ports = 427598732;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[NamedPort](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NamedPort)` |   
  
### getNamedPortsBuilder(int index)
    
    
    public NamedPort.Builder getNamedPortsBuilder(int index)

Optional. Assigns a name to a port number. For example:{name: "http", port: 80}

This allows the system to reference ports by the assigned name instead of a port number. Named ports can also contain multiple ports. For example:[{name: "app1", port: 8080}, {name: "app1", port: 8081}, {name: "app2", port: 8082}]

Named ports apply to all instances in this instance group.

`repeated .google.cloud.compute.v1.NamedPort named_ports = 427598732;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[NamedPort.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NamedPort.Builder)` |   
  
### getNamedPortsBuilderList()
    
    
    public List<NamedPort.Builder> getNamedPortsBuilderList()

Optional. Assigns a name to a port number. For example:{name: "http", port: 80}

This allows the system to reference ports by the assigned name instead of a port number. Named ports can also contain multiple ports. For example:[{name: "app1", port: 8080}, {name: "app1", port: 8081}, {name: "app2", port: 8082}]

Named ports apply to all instances in this instance group.

`repeated .google.cloud.compute.v1.NamedPort named_ports = 427598732;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NamedPort.Builder)>` |   
  
### getNamedPortsCount()
    
    
    public int getNamedPortsCount()

Optional. Assigns a name to a port number. For example:{name: "http", port: 80}

This allows the system to reference ports by the assigned name instead of a port number. Named ports can also contain multiple ports. For example:[{name: "app1", port: 8080}, {name: "app1", port: 8081}, {name: "app2", port: 8082}]

Named ports apply to all instances in this instance group.

`repeated .google.cloud.compute.v1.NamedPort named_ports = 427598732;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getNamedPortsList()
    
    
    public List<NamedPort> getNamedPortsList()

Optional. Assigns a name to a port number. For example:{name: "http", port: 80}

This allows the system to reference ports by the assigned name instead of a port number. Named ports can also contain multiple ports. For example:[{name: "app1", port: 8080}, {name: "app1", port: 8081}, {name: "app2", port: 8082}]

Named ports apply to all instances in this instance group.

`repeated .google.cloud.compute.v1.NamedPort named_ports = 427598732;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[NamedPort](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NamedPort)>` |   
  
### getNamedPortsOrBuilder(int index)
    
    
    public NamedPortOrBuilder getNamedPortsOrBuilder(int index)

Optional. Assigns a name to a port number. For example:{name: "http", port: 80}

This allows the system to reference ports by the assigned name instead of a port number. Named ports can also contain multiple ports. For example:[{name: "app1", port: 8080}, {name: "app1", port: 8081}, {name: "app2", port: 8082}]

Named ports apply to all instances in this instance group.

`repeated .google.cloud.compute.v1.NamedPort named_ports = 427598732;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[NamedPortOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NamedPortOrBuilder)` |   
  
### getNamedPortsOrBuilderList()
    
    
    public List<? extends NamedPortOrBuilder> getNamedPortsOrBuilderList()

Optional. Assigns a name to a port number. For example:{name: "http", port: 80}

This allows the system to reference ports by the assigned name instead of a port number. Named ports can also contain multiple ports. For example:[{name: "app1", port: 8080}, {name: "app1", port: 8081}, {name: "app2", port: 8082}]

Named ports apply to all instances in this instance group.

`repeated .google.cloud.compute.v1.NamedPort named_ports = 427598732;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.compute.v1.NamedPortOrBuilder>` |   
  
### getNetwork()
    
    
    public String getNetwork()

[Output Only] The URL of the network to which all instances in the instance group belong. If your instance has multiple network interfaces, then the network and subnetwork fields only refer to the network and subnet used by your primary interface (nic0).

`optional string network = 232872494;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The network.  
  
### getNetworkBytes()
    
    
    public ByteString getNetworkBytes()

[Output Only] The URL of the network to which all instances in the instance group belong. If your instance has multiple network interfaces, then the network and subnetwork fields only refer to the network and subnet used by your primary interface (nic0).

`optional string network = 232872494;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for network.  
  
### getRegion()
    
    
    public String getRegion()

Output only. [Output Only] The URL of theregion where the instance group is located (for regional resources).

`optional string region = 138946292;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The region.  
  
### getRegionBytes()
    
    
    public ByteString getRegionBytes()

Output only. [Output Only] The URL of theregion where the instance group is located (for regional resources).

`optional string region = 138946292;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for region.  
  
### getSelfLink()
    
    
    public String getSelfLink()

Output only. [Output Only] The URL for this instance group. The server generates this URL.

`optional string self_link = 456214797;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The selfLink.  
  
### getSelfLinkBytes()
    
    
    public ByteString getSelfLinkBytes()

Output only. [Output Only] The URL for this instance group. The server generates this URL.

`optional string self_link = 456214797;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for selfLink.  
  
### getSize()
    
    
    public int getSize()

Output only. [Output Only] The total number of instances in the instance group.

`optional int32 size = 3530753;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The size.  
  
### getSubnetwork()
    
    
    public String getSubnetwork()

Output only. [Output Only] The URL of the subnetwork to which all instances in the instance group belong. If your instance has multiple network interfaces, then the network and subnetwork fields only refer to the network and subnet used by your primary interface (nic0).

`optional string subnetwork = 307827694;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The subnetwork.  
  
### getSubnetworkBytes()
    
    
    public ByteString getSubnetworkBytes()

Output only. [Output Only] The URL of the subnetwork to which all instances in the instance group belong. If your instance has multiple network interfaces, then the network and subnetwork fields only refer to the network and subnet used by your primary interface (nic0).

`optional string subnetwork = 307827694;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for subnetwork.  
  
### getZone()
    
    
    public String getZone()

Output only. [Output Only] The URL of thezone where the instance group is located (for zonal resources).

`optional string zone = 3744684;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The zone.  
  
### getZoneBytes()
    
    
    public ByteString getZoneBytes()

Output only. [Output Only] The URL of thezone where the instance group is located (for zonal resources).

`optional string zone = 3744684;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for zone.  
  
### hasCreationTimestamp()
    
    
    public boolean hasCreationTimestamp()

Output only. [Output Only] The creation timestamp for this instance group inRFC3339 text format.

`optional string creation_timestamp = 30525366;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the creationTimestamp field is set.  
  
### hasDescription()
    
    
    public boolean hasDescription()

An optional description of this resource. Provide this property when you create the resource.

`optional string description = 422937596;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the description field is set.  
  
### hasFingerprint()
    
    
    public boolean hasFingerprint()

Output only. [Output Only] The fingerprint of the named ports. The system uses this fingerprint to detect conflicts when multiple users change the named ports concurrently.

`optional string fingerprint = 234678500;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the fingerprint field is set.  
  
### hasId()
    
    
    public boolean hasId()

Output only. [Output Only] A unique identifier for this instance group, generated by the server.

`optional uint64 id = 3355;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the id field is set.  
  
### hasKind()
    
    
    public boolean hasKind()

Output only. [Output Only] The resource type, which is alwayscompute#instanceGroup for instance groups.

`optional string kind = 3292052;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the kind field is set.  
  
### hasName()
    
    
    public boolean hasName()

The name of the instance group. The name must be 1-63 characters long, and comply withRFC1035.

`optional string name = 3373707;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the name field is set.  
  
### hasNetwork()
    
    
    public boolean hasNetwork()

[Output Only] The URL of the network to which all instances in the instance group belong. If your instance has multiple network interfaces, then the network and subnetwork fields only refer to the network and subnet used by your primary interface (nic0).

`optional string network = 232872494;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the network field is set.  
  
### hasRegion()
    
    
    public boolean hasRegion()

Output only. [Output Only] The URL of theregion where the instance group is located (for regional resources).

`optional string region = 138946292;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the region field is set.  
  
### hasSelfLink()
    
    
    public boolean hasSelfLink()

Output only. [Output Only] The URL for this instance group. The server generates this URL.

`optional string self_link = 456214797;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the selfLink field is set.  
  
### hasSize()
    
    
    public boolean hasSize()

Output only. [Output Only] The total number of instances in the instance group.

`optional int32 size = 3530753;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the size field is set.  
  
### hasSubnetwork()
    
    
    public boolean hasSubnetwork()

Output only. [Output Only] The URL of the subnetwork to which all instances in the instance group belong. If your instance has multiple network interfaces, then the network and subnetwork fields only refer to the network and subnet used by your primary interface (nic0).

`optional string subnetwork = 307827694;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the subnetwork field is set.  
  
### hasZone()
    
    
    public boolean hasZone()

Output only. [Output Only] The URL of thezone where the instance group is located (for zonal resources).

`optional string zone = 3744684;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the zone field is set.  
  
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

### mergeFrom(InstanceGroup other)
    
    
    public InstanceGroup.Builder mergeFrom(InstanceGroup other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[InstanceGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroup)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroup.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public InstanceGroup.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroup.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public InstanceGroup.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroup.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### removeNamedPorts(int index)
    
    
    public InstanceGroup.Builder removeNamedPorts(int index)

Optional. Assigns a name to a port number. For example:{name: "http", port: 80}

This allows the system to reference ports by the assigned name instead of a port number. Named ports can also contain multiple ports. For example:[{name: "app1", port: 8080}, {name: "app1", port: 8081}, {name: "app2", port: 8082}]

Named ports apply to all instances in this instance group.

`repeated .google.cloud.compute.v1.NamedPort named_ports = 427598732;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroup.Builder)` |   
  
### setCreationTimestamp(String value)
    
    
    public InstanceGroup.Builder setCreationTimestamp(String value)

Output only. [Output Only] The creation timestamp for this instance group inRFC3339 text format.

`optional string creation_timestamp = 30525366;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The creationTimestamp to set.  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroup.Builder)` | This builder for chaining.  
  
### setCreationTimestampBytes(ByteString value)
    
    
    public InstanceGroup.Builder setCreationTimestampBytes(ByteString value)

Output only. [Output Only] The creation timestamp for this instance group inRFC3339 text format.

`optional string creation_timestamp = 30525366;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for creationTimestamp to set.  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroup.Builder)` | This builder for chaining.  
  
### setDescription(String value)
    
    
    public InstanceGroup.Builder setDescription(String value)

An optional description of this resource. Provide this property when you create the resource.

`optional string description = 422937596;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The description to set.  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroup.Builder)` | This builder for chaining.  
  
### setDescriptionBytes(ByteString value)
    
    
    public InstanceGroup.Builder setDescriptionBytes(ByteString value)

An optional description of this resource. Provide this property when you create the resource.

`optional string description = 422937596;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for description to set.  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroup.Builder)` | This builder for chaining.  
  
### setFingerprint(String value)
    
    
    public InstanceGroup.Builder setFingerprint(String value)

Output only. [Output Only] The fingerprint of the named ports. The system uses this fingerprint to detect conflicts when multiple users change the named ports concurrently.

`optional string fingerprint = 234678500;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The fingerprint to set.  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroup.Builder)` | This builder for chaining.  
  
### setFingerprintBytes(ByteString value)
    
    
    public InstanceGroup.Builder setFingerprintBytes(ByteString value)

Output only. [Output Only] The fingerprint of the named ports. The system uses this fingerprint to detect conflicts when multiple users change the named ports concurrently.

`optional string fingerprint = 234678500;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for fingerprint to set.  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroup.Builder)` | This builder for chaining.  
  
### setId(long value)
    
    
    public InstanceGroup.Builder setId(long value)

Output only. [Output Only] A unique identifier for this instance group, generated by the server.

`optional uint64 id = 3355;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The id to set.  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroup.Builder)` | This builder for chaining.  
  
### setKind(String value)
    
    
    public InstanceGroup.Builder setKind(String value)

Output only. [Output Only] The resource type, which is alwayscompute#instanceGroup for instance groups.

`optional string kind = 3292052;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The kind to set.  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroup.Builder)` | This builder for chaining.  
  
### setKindBytes(ByteString value)
    
    
    public InstanceGroup.Builder setKindBytes(ByteString value)

Output only. [Output Only] The resource type, which is alwayscompute#instanceGroup for instance groups.

`optional string kind = 3292052;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for kind to set.  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroup.Builder)` | This builder for chaining.  
  
### setName(String value)
    
    
    public InstanceGroup.Builder setName(String value)

The name of the instance group. The name must be 1-63 characters long, and comply withRFC1035.

`optional string name = 3373707;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name to set.  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroup.Builder)` | This builder for chaining.  
  
### setNameBytes(ByteString value)
    
    
    public InstanceGroup.Builder setNameBytes(ByteString value)

The name of the instance group. The name must be 1-63 characters long, and comply withRFC1035.

`optional string name = 3373707;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for name to set.  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroup.Builder)` | This builder for chaining.  
  
### setNamedPorts(int index, NamedPort value)
    
    
    public InstanceGroup.Builder setNamedPorts(int index, NamedPort value)

Optional. Assigns a name to a port number. For example:{name: "http", port: 80}

This allows the system to reference ports by the assigned name instead of a port number. Named ports can also contain multiple ports. For example:[{name: "app1", port: 8080}, {name: "app1", port: 8081}, {name: "app2", port: 8082}]

Named ports apply to all instances in this instance group.

`repeated .google.cloud.compute.v1.NamedPort named_ports = 427598732;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[NamedPort](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NamedPort)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroup.Builder)` |   
  
### setNamedPorts(int index, NamedPort.Builder builderForValue)
    
    
    public InstanceGroup.Builder setNamedPorts(int index, NamedPort.Builder builderForValue)

Optional. Assigns a name to a port number. For example:{name: "http", port: 80}

This allows the system to reference ports by the assigned name instead of a port number. Named ports can also contain multiple ports. For example:[{name: "app1", port: 8080}, {name: "app1", port: 8081}, {name: "app2", port: 8082}]

Named ports apply to all instances in this instance group.

`repeated .google.cloud.compute.v1.NamedPort named_ports = 427598732;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[NamedPort.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NamedPort.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroup.Builder)` |   
  
### setNetwork(String value)
    
    
    public InstanceGroup.Builder setNetwork(String value)

[Output Only] The URL of the network to which all instances in the instance group belong. If your instance has multiple network interfaces, then the network and subnetwork fields only refer to the network and subnet used by your primary interface (nic0).

`optional string network = 232872494;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The network to set.  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroup.Builder)` | This builder for chaining.  
  
### setNetworkBytes(ByteString value)
    
    
    public InstanceGroup.Builder setNetworkBytes(ByteString value)

[Output Only] The URL of the network to which all instances in the instance group belong. If your instance has multiple network interfaces, then the network and subnetwork fields only refer to the network and subnet used by your primary interface (nic0).

`optional string network = 232872494;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for network to set.  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroup.Builder)` | This builder for chaining.  
  
### setRegion(String value)
    
    
    public InstanceGroup.Builder setRegion(String value)

Output only. [Output Only] The URL of theregion where the instance group is located (for regional resources).

`optional string region = 138946292;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The region to set.  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroup.Builder)` | This builder for chaining.  
  
### setRegionBytes(ByteString value)
    
    
    public InstanceGroup.Builder setRegionBytes(ByteString value)

Output only. [Output Only] The URL of theregion where the instance group is located (for regional resources).

`optional string region = 138946292;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for region to set.  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroup.Builder)` | This builder for chaining.  
  
### setSelfLink(String value)
    
    
    public InstanceGroup.Builder setSelfLink(String value)

Output only. [Output Only] The URL for this instance group. The server generates this URL.

`optional string self_link = 456214797;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The selfLink to set.  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroup.Builder)` | This builder for chaining.  
  
### setSelfLinkBytes(ByteString value)
    
    
    public InstanceGroup.Builder setSelfLinkBytes(ByteString value)

Output only. [Output Only] The URL for this instance group. The server generates this URL.

`optional string self_link = 456214797;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for selfLink to set.  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroup.Builder)` | This builder for chaining.  
  
### setSize(int value)
    
    
    public InstanceGroup.Builder setSize(int value)

Output only. [Output Only] The total number of instances in the instance group.

`optional int32 size = 3530753;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The size to set.  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroup.Builder)` | This builder for chaining.  
  
### setSubnetwork(String value)
    
    
    public InstanceGroup.Builder setSubnetwork(String value)

Output only. [Output Only] The URL of the subnetwork to which all instances in the instance group belong. If your instance has multiple network interfaces, then the network and subnetwork fields only refer to the network and subnet used by your primary interface (nic0).

`optional string subnetwork = 307827694;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The subnetwork to set.  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroup.Builder)` | This builder for chaining.  
  
### setSubnetworkBytes(ByteString value)
    
    
    public InstanceGroup.Builder setSubnetworkBytes(ByteString value)

Output only. [Output Only] The URL of the subnetwork to which all instances in the instance group belong. If your instance has multiple network interfaces, then the network and subnetwork fields only refer to the network and subnet used by your primary interface (nic0).

`optional string subnetwork = 307827694;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for subnetwork to set.  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroup.Builder)` | This builder for chaining.  
  
### setZone(String value)
    
    
    public InstanceGroup.Builder setZone(String value)

Output only. [Output Only] The URL of thezone where the instance group is located (for zonal resources).

`optional string zone = 3744684;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The zone to set.  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroup.Builder)` | This builder for chaining.  
  
### setZoneBytes(ByteString value)
    
    
    public InstanceGroup.Builder setZoneBytes(ByteString value)

Output only. [Output Only] The URL of thezone where the instance group is located (for zonal resources).

`optional string zone = 3744684;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for zone to set.  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroup.Builder)` | This builder for chaining.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
