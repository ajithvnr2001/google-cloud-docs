---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder
title: Class WorkstationConfig.Builder (0.87.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:21:56.194092+00:00
---

# Class WorkstationConfig.Builder (0.87.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class WorkstationConfig.Builder (0.87.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.87.0 (latest)  0.83.0  0.82.0  0.81.0  0.79.0  0.76.0  0.75.0  0.73.0  0.71.0  0.70.0  0.68.0  0.66.0  0.64.0  0.63.0  0.62.0  0.61.0  0.60.0  0.58.0  0.56.0  0.55.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static final class WorkstationConfig.Builder extends GeneratedMessage.Builder<WorkstationConfig.Builder> implements WorkstationConfigOrBuilder

A workstation configuration resource in the Cloud Workstations API.

Workstation configurations act as templates for workstations. The workstation configuration defines details such as the workstation virtual machine (VM) instance type, persistent storage, container image defining environment, which IDE or Code Editor to use, and more. Administrators and platform teams can also use [Identity and Access Management (IAM)](https://cloud.google.com/iam/docs/overview) rules to grant access to teams or to individual developers.

Protobuf type `google.cloud.workstations.v1.WorkstationConfig`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > WorkstationConfig.Builder

## Implements

[WorkstationConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfigOrBuilder)

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

### addAllAllowedPorts(Iterable<? extends WorkstationConfig.PortRange> values)
    
    
    public WorkstationConfig.Builder addAllAllowedPorts(Iterable<? extends WorkstationConfig.PortRange> values)

Optional. A list of PortRanges specifying single ports or ranges of ports that are externally accessible in the workstation. Allowed ports must be one of 22, 80, or within range 1024-65535. If not specified defaults to ports 22, 80, and ports 1024-65535.

` repeated .google.cloud.workstations.v1.WorkstationConfig.PortRange allowed_ports = 25 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<? extends com.google.cloud.workstations.v1.WorkstationConfig.PortRange>`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### addAllConditions(Iterable<? extends Status> values)
    
    
    public WorkstationConfig.Builder addAllConditions(Iterable<? extends Status> values)

Output only. Status conditions describing the workstation configuration's current state.

` repeated .google.rpc.Status conditions = 16 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<? extends com.google.rpc.Status>`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### addAllEphemeralDirectories(Iterable<? extends WorkstationConfig.EphemeralDirectory> values)
    
    
    public WorkstationConfig.Builder addAllEphemeralDirectories(Iterable<? extends WorkstationConfig.EphemeralDirectory> values)

Optional. Ephemeral directories which won't persist across workstation sessions.

` repeated .google.cloud.workstations.v1.WorkstationConfig.EphemeralDirectory ephemeral_directories = 22 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<? extends com.google.cloud.workstations.v1.WorkstationConfig.EphemeralDirectory>`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### addAllPersistentDirectories(Iterable<? extends WorkstationConfig.PersistentDirectory> values)
    
    
    public WorkstationConfig.Builder addAllPersistentDirectories(Iterable<? extends WorkstationConfig.PersistentDirectory> values)

Optional. Directories to persist across workstation sessions.

` repeated .google.cloud.workstations.v1.WorkstationConfig.PersistentDirectory persistent_directories = 13 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<? extends com.google.cloud.workstations.v1.WorkstationConfig.PersistentDirectory>`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### addAllReadinessChecks(Iterable<? extends WorkstationConfig.ReadinessCheck> values)
    
    
    public WorkstationConfig.Builder addAllReadinessChecks(Iterable<? extends WorkstationConfig.ReadinessCheck> values)

Optional. Readiness checks to perform when starting a workstation using this workstation configuration. Mark a workstation as running only after all specified readiness checks return 200 status codes.

` repeated .google.cloud.workstations.v1.WorkstationConfig.ReadinessCheck readiness_checks = 19 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<? extends com.google.cloud.workstations.v1.WorkstationConfig.ReadinessCheck>`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### addAllReplicaZones(Iterable<String> values)
    
    
    public WorkstationConfig.Builder addAllReplicaZones(Iterable<String> values)

Optional. Immutable. Specifies the zones used to replicate the VM and disk resources within the region. If set, exactly two zones within the workstation cluster's region must be specified—for example, `['us-central1-a', 'us-central1-f']`. If this field is empty, two default zones within the region are used.

Immutable after the workstation configuration is created.

` repeated string replica_zones = 23 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = IMMUTABLE]; `

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
The replicaZones to add.  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` | This builder for chaining.  
  
### addAllowedPorts(WorkstationConfig.PortRange value)
    
    
    public WorkstationConfig.Builder addAllowedPorts(WorkstationConfig.PortRange value)

Optional. A list of PortRanges specifying single ports or ranges of ports that are externally accessible in the workstation. Allowed ports must be one of 22, 80, or within range 1024-65535. If not specified defaults to ports 22, 80, and ports 1024-65535.

` repeated .google.cloud.workstations.v1.WorkstationConfig.PortRange allowed_ports = 25 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[WorkstationConfig.PortRange](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.PortRange)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### addAllowedPorts(WorkstationConfig.PortRange.Builder builderForValue)
    
    
    public WorkstationConfig.Builder addAllowedPorts(WorkstationConfig.PortRange.Builder builderForValue)

Optional. A list of PortRanges specifying single ports or ranges of ports that are externally accessible in the workstation. Allowed ports must be one of 22, 80, or within range 1024-65535. If not specified defaults to ports 22, 80, and ports 1024-65535.

` repeated .google.cloud.workstations.v1.WorkstationConfig.PortRange allowed_ports = 25 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[WorkstationConfig.PortRange.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.PortRange.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### addAllowedPorts(int index, WorkstationConfig.PortRange value)
    
    
    public WorkstationConfig.Builder addAllowedPorts(int index, WorkstationConfig.PortRange value)

Optional. A list of PortRanges specifying single ports or ranges of ports that are externally accessible in the workstation. Allowed ports must be one of 22, 80, or within range 1024-65535. If not specified defaults to ports 22, 80, and ports 1024-65535.

` repeated .google.cloud.workstations.v1.WorkstationConfig.PortRange allowed_ports = 25 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[WorkstationConfig.PortRange](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.PortRange)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### addAllowedPorts(int index, WorkstationConfig.PortRange.Builder builderForValue)
    
    
    public WorkstationConfig.Builder addAllowedPorts(int index, WorkstationConfig.PortRange.Builder builderForValue)

Optional. A list of PortRanges specifying single ports or ranges of ports that are externally accessible in the workstation. Allowed ports must be one of 22, 80, or within range 1024-65535. If not specified defaults to ports 22, 80, and ports 1024-65535.

` repeated .google.cloud.workstations.v1.WorkstationConfig.PortRange allowed_ports = 25 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[WorkstationConfig.PortRange.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.PortRange.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### addAllowedPortsBuilder()
    
    
    public WorkstationConfig.PortRange.Builder addAllowedPortsBuilder()

Optional. A list of PortRanges specifying single ports or ranges of ports that are externally accessible in the workstation. Allowed ports must be one of 22, 80, or within range 1024-65535. If not specified defaults to ports 22, 80, and ports 1024-65535.

` repeated .google.cloud.workstations.v1.WorkstationConfig.PortRange allowed_ports = 25 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.PortRange.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.PortRange.Builder)` |   
  
### addAllowedPortsBuilder(int index)
    
    
    public WorkstationConfig.PortRange.Builder addAllowedPortsBuilder(int index)

Optional. A list of PortRanges specifying single ports or ranges of ports that are externally accessible in the workstation. Allowed ports must be one of 22, 80, or within range 1024-65535. If not specified defaults to ports 22, 80, and ports 1024-65535.

` repeated .google.cloud.workstations.v1.WorkstationConfig.PortRange allowed_ports = 25 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.PortRange.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.PortRange.Builder)` |   
  
### addConditions(Status value)
    
    
    public WorkstationConfig.Builder addConditions(Status value)

Output only. Status conditions describing the workstation configuration's current state.

` repeated .google.rpc.Status conditions = 16 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `com.google.rpc.Status`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### addConditions(Status.Builder builderForValue)
    
    
    public WorkstationConfig.Builder addConditions(Status.Builder builderForValue)

Output only. Status conditions describing the workstation configuration's current state.

` repeated .google.rpc.Status conditions = 16 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `com.google.rpc.Status.Builder`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### addConditions(int index, Status value)
    
    
    public WorkstationConfig.Builder addConditions(int index, Status value)

Output only. Status conditions describing the workstation configuration's current state.

` repeated .google.rpc.Status conditions = 16 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `com.google.rpc.Status`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### addConditions(int index, Status.Builder builderForValue)
    
    
    public WorkstationConfig.Builder addConditions(int index, Status.Builder builderForValue)

Output only. Status conditions describing the workstation configuration's current state.

` repeated .google.rpc.Status conditions = 16 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `com.google.rpc.Status.Builder`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### addConditionsBuilder()
    
    
    public Status.Builder addConditionsBuilder()

Output only. Status conditions describing the workstation configuration's current state.

` repeated .google.rpc.Status conditions = 16 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`com.google.rpc.Status.Builder` |   
  
### addConditionsBuilder(int index)
    
    
    public Status.Builder addConditionsBuilder(int index)

Output only. Status conditions describing the workstation configuration's current state.

` repeated .google.rpc.Status conditions = 16 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.rpc.Status.Builder` |   
  
### addEphemeralDirectories(WorkstationConfig.EphemeralDirectory value)
    
    
    public WorkstationConfig.Builder addEphemeralDirectories(WorkstationConfig.EphemeralDirectory value)

Optional. Ephemeral directories which won't persist across workstation sessions.

` repeated .google.cloud.workstations.v1.WorkstationConfig.EphemeralDirectory ephemeral_directories = 22 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[WorkstationConfig.EphemeralDirectory](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.EphemeralDirectory)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### addEphemeralDirectories(WorkstationConfig.EphemeralDirectory.Builder builderForValue)
    
    
    public WorkstationConfig.Builder addEphemeralDirectories(WorkstationConfig.EphemeralDirectory.Builder builderForValue)

Optional. Ephemeral directories which won't persist across workstation sessions.

` repeated .google.cloud.workstations.v1.WorkstationConfig.EphemeralDirectory ephemeral_directories = 22 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[WorkstationConfig.EphemeralDirectory.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.EphemeralDirectory.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### addEphemeralDirectories(int index, WorkstationConfig.EphemeralDirectory value)
    
    
    public WorkstationConfig.Builder addEphemeralDirectories(int index, WorkstationConfig.EphemeralDirectory value)

Optional. Ephemeral directories which won't persist across workstation sessions.

` repeated .google.cloud.workstations.v1.WorkstationConfig.EphemeralDirectory ephemeral_directories = 22 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[WorkstationConfig.EphemeralDirectory](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.EphemeralDirectory)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### addEphemeralDirectories(int index, WorkstationConfig.EphemeralDirectory.Builder builderForValue)
    
    
    public WorkstationConfig.Builder addEphemeralDirectories(int index, WorkstationConfig.EphemeralDirectory.Builder builderForValue)

Optional. Ephemeral directories which won't persist across workstation sessions.

` repeated .google.cloud.workstations.v1.WorkstationConfig.EphemeralDirectory ephemeral_directories = 22 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[WorkstationConfig.EphemeralDirectory.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.EphemeralDirectory.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### addEphemeralDirectoriesBuilder()
    
    
    public WorkstationConfig.EphemeralDirectory.Builder addEphemeralDirectoriesBuilder()

Optional. Ephemeral directories which won't persist across workstation sessions.

` repeated .google.cloud.workstations.v1.WorkstationConfig.EphemeralDirectory ephemeral_directories = 22 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.EphemeralDirectory.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.EphemeralDirectory.Builder)` |   
  
### addEphemeralDirectoriesBuilder(int index)
    
    
    public WorkstationConfig.EphemeralDirectory.Builder addEphemeralDirectoriesBuilder(int index)

Optional. Ephemeral directories which won't persist across workstation sessions.

` repeated .google.cloud.workstations.v1.WorkstationConfig.EphemeralDirectory ephemeral_directories = 22 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.EphemeralDirectory.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.EphemeralDirectory.Builder)` |   
  
### addPersistentDirectories(WorkstationConfig.PersistentDirectory value)
    
    
    public WorkstationConfig.Builder addPersistentDirectories(WorkstationConfig.PersistentDirectory value)

Optional. Directories to persist across workstation sessions.

` repeated .google.cloud.workstations.v1.WorkstationConfig.PersistentDirectory persistent_directories = 13 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[WorkstationConfig.PersistentDirectory](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.PersistentDirectory)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### addPersistentDirectories(WorkstationConfig.PersistentDirectory.Builder builderForValue)
    
    
    public WorkstationConfig.Builder addPersistentDirectories(WorkstationConfig.PersistentDirectory.Builder builderForValue)

Optional. Directories to persist across workstation sessions.

` repeated .google.cloud.workstations.v1.WorkstationConfig.PersistentDirectory persistent_directories = 13 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[WorkstationConfig.PersistentDirectory.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.PersistentDirectory.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### addPersistentDirectories(int index, WorkstationConfig.PersistentDirectory value)
    
    
    public WorkstationConfig.Builder addPersistentDirectories(int index, WorkstationConfig.PersistentDirectory value)

Optional. Directories to persist across workstation sessions.

` repeated .google.cloud.workstations.v1.WorkstationConfig.PersistentDirectory persistent_directories = 13 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[WorkstationConfig.PersistentDirectory](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.PersistentDirectory)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### addPersistentDirectories(int index, WorkstationConfig.PersistentDirectory.Builder builderForValue)
    
    
    public WorkstationConfig.Builder addPersistentDirectories(int index, WorkstationConfig.PersistentDirectory.Builder builderForValue)

Optional. Directories to persist across workstation sessions.

` repeated .google.cloud.workstations.v1.WorkstationConfig.PersistentDirectory persistent_directories = 13 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[WorkstationConfig.PersistentDirectory.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.PersistentDirectory.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### addPersistentDirectoriesBuilder()
    
    
    public WorkstationConfig.PersistentDirectory.Builder addPersistentDirectoriesBuilder()

Optional. Directories to persist across workstation sessions.

` repeated .google.cloud.workstations.v1.WorkstationConfig.PersistentDirectory persistent_directories = 13 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.PersistentDirectory.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.PersistentDirectory.Builder)` |   
  
### addPersistentDirectoriesBuilder(int index)
    
    
    public WorkstationConfig.PersistentDirectory.Builder addPersistentDirectoriesBuilder(int index)

Optional. Directories to persist across workstation sessions.

` repeated .google.cloud.workstations.v1.WorkstationConfig.PersistentDirectory persistent_directories = 13 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.PersistentDirectory.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.PersistentDirectory.Builder)` |   
  
### addReadinessChecks(WorkstationConfig.ReadinessCheck value)
    
    
    public WorkstationConfig.Builder addReadinessChecks(WorkstationConfig.ReadinessCheck value)

Optional. Readiness checks to perform when starting a workstation using this workstation configuration. Mark a workstation as running only after all specified readiness checks return 200 status codes.

` repeated .google.cloud.workstations.v1.WorkstationConfig.ReadinessCheck readiness_checks = 19 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[WorkstationConfig.ReadinessCheck](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.ReadinessCheck)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### addReadinessChecks(WorkstationConfig.ReadinessCheck.Builder builderForValue)
    
    
    public WorkstationConfig.Builder addReadinessChecks(WorkstationConfig.ReadinessCheck.Builder builderForValue)

Optional. Readiness checks to perform when starting a workstation using this workstation configuration. Mark a workstation as running only after all specified readiness checks return 200 status codes.

` repeated .google.cloud.workstations.v1.WorkstationConfig.ReadinessCheck readiness_checks = 19 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[WorkstationConfig.ReadinessCheck.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.ReadinessCheck.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### addReadinessChecks(int index, WorkstationConfig.ReadinessCheck value)
    
    
    public WorkstationConfig.Builder addReadinessChecks(int index, WorkstationConfig.ReadinessCheck value)

Optional. Readiness checks to perform when starting a workstation using this workstation configuration. Mark a workstation as running only after all specified readiness checks return 200 status codes.

` repeated .google.cloud.workstations.v1.WorkstationConfig.ReadinessCheck readiness_checks = 19 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[WorkstationConfig.ReadinessCheck](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.ReadinessCheck)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### addReadinessChecks(int index, WorkstationConfig.ReadinessCheck.Builder builderForValue)
    
    
    public WorkstationConfig.Builder addReadinessChecks(int index, WorkstationConfig.ReadinessCheck.Builder builderForValue)

Optional. Readiness checks to perform when starting a workstation using this workstation configuration. Mark a workstation as running only after all specified readiness checks return 200 status codes.

` repeated .google.cloud.workstations.v1.WorkstationConfig.ReadinessCheck readiness_checks = 19 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[WorkstationConfig.ReadinessCheck.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.ReadinessCheck.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### addReadinessChecksBuilder()
    
    
    public WorkstationConfig.ReadinessCheck.Builder addReadinessChecksBuilder()

Optional. Readiness checks to perform when starting a workstation using this workstation configuration. Mark a workstation as running only after all specified readiness checks return 200 status codes.

` repeated .google.cloud.workstations.v1.WorkstationConfig.ReadinessCheck readiness_checks = 19 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.ReadinessCheck.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.ReadinessCheck.Builder)` |   
  
### addReadinessChecksBuilder(int index)
    
    
    public WorkstationConfig.ReadinessCheck.Builder addReadinessChecksBuilder(int index)

Optional. Readiness checks to perform when starting a workstation using this workstation configuration. Mark a workstation as running only after all specified readiness checks return 200 status codes.

` repeated .google.cloud.workstations.v1.WorkstationConfig.ReadinessCheck readiness_checks = 19 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.ReadinessCheck.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.ReadinessCheck.Builder)` |   
  
### addReplicaZones(String value)
    
    
    public WorkstationConfig.Builder addReplicaZones(String value)

Optional. Immutable. Specifies the zones used to replicate the VM and disk resources within the region. If set, exactly two zones within the workstation cluster's region must be specified—for example, `['us-central1-a', 'us-central1-f']`. If this field is empty, two default zones within the region are used.

Immutable after the workstation configuration is created.

` repeated string replica_zones = 23 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = IMMUTABLE]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The replicaZones to add.  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` | This builder for chaining.  
  
### addReplicaZonesBytes(ByteString value)
    
    
    public WorkstationConfig.Builder addReplicaZonesBytes(ByteString value)

Optional. Immutable. Specifies the zones used to replicate the VM and disk resources within the region. If set, exactly two zones within the workstation cluster's region must be specified—for example, `['us-central1-a', 'us-central1-f']`. If this field is empty, two default zones within the region are used.

Immutable after the workstation configuration is created.

` repeated string replica_zones = 23 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = IMMUTABLE]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes of the replicaZones to add.  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` | This builder for chaining.  
  
### build()
    
    
    public WorkstationConfig build()

**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig)` |   
  
### buildPartial()
    
    
    public WorkstationConfig buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig)` |   
  
### clear()
    
    
    public WorkstationConfig.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearAllowedPorts()
    
    
    public WorkstationConfig.Builder clearAllowedPorts()

Optional. A list of PortRanges specifying single ports or ranges of ports that are externally accessible in the workstation. Allowed ports must be one of 22, 80, or within range 1024-65535. If not specified defaults to ports 22, 80, and ports 1024-65535.

` repeated .google.cloud.workstations.v1.WorkstationConfig.PortRange allowed_ports = 25 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### clearAnnotations()
    
    
    public WorkstationConfig.Builder clearAnnotations()

**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### clearConditions()
    
    
    public WorkstationConfig.Builder clearConditions()

Output only. Status conditions describing the workstation configuration's current state.

` repeated .google.rpc.Status conditions = 16 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### clearContainer()
    
    
    public WorkstationConfig.Builder clearContainer()

Optional. Container that runs upon startup for each workstation using this workstation configuration.

` .google.cloud.workstations.v1.WorkstationConfig.Container container = 14 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### clearCreateTime()
    
    
    public WorkstationConfig.Builder clearCreateTime()

Output only. Time when this workstation configuration was created.

` .google.protobuf.Timestamp create_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### clearDegraded()
    
    
    public WorkstationConfig.Builder clearDegraded()

Output only. Whether this workstation configuration is in degraded mode, in which case it may require user action to restore full functionality. The conditions field contains detailed information about the status of the configuration.

`bool degraded = 15 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` | This builder for chaining.  
  
### clearDeleteTime()
    
    
    public WorkstationConfig.Builder clearDeleteTime()

Output only. Time when this workstation configuration was soft-deleted.

` .google.protobuf.Timestamp delete_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### clearDisableTcpConnections()
    
    
    public WorkstationConfig.Builder clearDisableTcpConnections()

Optional. Disables support for plain TCP connections in the workstation. By default the service supports TCP connections through a websocket relay. Setting this option to true disables that relay, which prevents the usage of services that require plain TCP connections, such as SSH. When enabled, all communication must occur over HTTPS or WSS.

`bool disable_tcp_connections = 24 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` | This builder for chaining.  
  
### clearDisplayName()
    
    
    public WorkstationConfig.Builder clearDisplayName()

Optional. Human-readable name for this workstation configuration.

`string display_name = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` | This builder for chaining.  
  
### clearEnableAuditAgent()
    
    
    public WorkstationConfig.Builder clearEnableAuditAgent()

Optional. Whether to enable Linux `auditd` logging on the workstation. When enabled, a service_account must also be specified that has `roles/logging.logWriter` and `roles/monitoring.metricWriter` on the project. Operating system audit logging is distinct from [Cloud Audit Logs](https://cloud.google.com/workstations/docs/audit-logging) and [Container output logging](https://cloud.google.com/workstations/docs/container-output-logging#overview). Operating system audit logs are available in the [Cloud Logging](https://cloud.google.com/logging/docs) console by querying:

resource.type="gce_instance" log_name:"/logs/linux-auditd"

`bool enable_audit_agent = 20 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` | This builder for chaining.  
  
### clearEncryptionKey()
    
    
    public WorkstationConfig.Builder clearEncryptionKey()

Immutable. Encrypts resources of this workstation configuration using a customer-managed encryption key (CMEK).

If specified, the boot disk of the Compute Engine instance and the persistent disk are encrypted using this encryption key. If this field is not set, the disks are encrypted using a generated key. Customer-managed encryption keys do not protect disk metadata.

If the customer-managed encryption key is rotated, when the workstation instance is stopped, the system attempts to recreate the persistent disk with the new version of the key. Be sure to keep older versions of the key until the persistent disk is recreated. Otherwise, data on the persistent disk might be lost.

If the encryption key is revoked, the workstation session automatically stops within 7 hours.

Immutable after the workstation configuration is created.

` .google.cloud.workstations.v1.WorkstationConfig.CustomerEncryptionKey encryption_key = 17 [(.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### clearEphemeralDirectories()
    
    
    public WorkstationConfig.Builder clearEphemeralDirectories()

Optional. Ephemeral directories which won't persist across workstation sessions.

` repeated .google.cloud.workstations.v1.WorkstationConfig.EphemeralDirectory ephemeral_directories = 22 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### clearEtag()
    
    
    public WorkstationConfig.Builder clearEtag()

Optional. Checksum computed by the server. May be sent on update and delete requests to make sure that the client has an up-to-date value before proceeding.

`string etag = 9 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` | This builder for chaining.  
  
### clearGrantWorkstationAdminRoleOnCreate()
    
    
    public WorkstationConfig.Builder clearGrantWorkstationAdminRoleOnCreate()

Optional. Grant creator of a workstation `roles/workstations.policyAdmin` role along with `roles/workstations.user` role on the workstation created by them. This allows workstation users to share access to either their entire workstation, or individual ports. Defaults to false.

` bool grant_workstation_admin_role_on_create = 29 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` | This builder for chaining.  
  
### clearHost()
    
    
    public WorkstationConfig.Builder clearHost()

Optional. Runtime host for the workstation.

` .google.cloud.workstations.v1.WorkstationConfig.Host host = 12 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### clearIdleTimeout()
    
    
    public WorkstationConfig.Builder clearIdleTimeout()

Optional. Number of seconds to wait before automatically stopping a workstation after it last received user traffic.

A value of `"0s"` indicates that Cloud Workstations VMs created with this configuration should never time out due to idleness. Provide [duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#duration) terminated by `s` for seconds—for example, `"7200s"` (2 hours). The default is `"1200s"` (20 minutes).

`.google.protobuf.Duration idle_timeout = 10 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### clearLabels()
    
    
    public WorkstationConfig.Builder clearLabels()

**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### clearMaxUsableWorkstations()
    
    
    public WorkstationConfig.Builder clearMaxUsableWorkstations()

Optional. Maximum number of workstations under this configuration a user can have `workstations.workstation.use` permission on.

Only enforced on CreateWorkstation API calls on the user issuing the API request. Can be overridden by:

  * granting a user workstations.workstationConfigs.exemptMaxUsableWorkstationLimit permission, or
  * having a user with that permission create a workstation and granting another user `workstations.workstation.use` permission on that workstation.

If not specified, defaults to `0`, which indicates unlimited.




`int32 max_usable_workstations = 28 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` | This builder for chaining.  
  
### clearName()
    
    
    public WorkstationConfig.Builder clearName()

Identifier. Full name of this workstation configuration.

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` | This builder for chaining.  
  
### clearPersistentDirectories()
    
    
    public WorkstationConfig.Builder clearPersistentDirectories()

Optional. Directories to persist across workstation sessions.

` repeated .google.cloud.workstations.v1.WorkstationConfig.PersistentDirectory persistent_directories = 13 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### clearReadinessChecks()
    
    
    public WorkstationConfig.Builder clearReadinessChecks()

Optional. Readiness checks to perform when starting a workstation using this workstation configuration. Mark a workstation as running only after all specified readiness checks return 200 status codes.

` repeated .google.cloud.workstations.v1.WorkstationConfig.ReadinessCheck readiness_checks = 19 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### clearReconciling()
    
    
    public WorkstationConfig.Builder clearReconciling()

Output only. Indicates whether this workstation configuration is currently being updated to match its intended state.

`bool reconciling = 4 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` | This builder for chaining.  
  
### clearReplicaZones()
    
    
    public WorkstationConfig.Builder clearReplicaZones()

Optional. Immutable. Specifies the zones used to replicate the VM and disk resources within the region. If set, exactly two zones within the workstation cluster's region must be specified—for example, `['us-central1-a', 'us-central1-f']`. If this field is empty, two default zones within the region are used.

Immutable after the workstation configuration is created.

` repeated string replica_zones = 23 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` | This builder for chaining.  
  
### clearRunningTimeout()
    
    
    public WorkstationConfig.Builder clearRunningTimeout()

Optional. Number of seconds that a workstation can run until it is automatically shut down. We recommend that workstations be shut down daily to reduce costs and so that security updates can be applied upon restart. The idle_timeout and running_timeout fields are independent of each other. Note that the running_timeout field shuts down VMs after the specified time, regardless of whether or not the VMs are idle.

Provide duration terminated by `s` for seconds—for example, `"54000s"` (15 hours). Defaults to `"43200s"` (12 hours). A value of `"0s"` indicates that workstations using this configuration should never time out. If encryption_key is set, it must be greater than `"0s"` and less than `"86400s"` (24 hours).

Warning: A value of `"0s"` indicates that Cloud Workstations VMs created with this configuration have no maximum running time. This is strongly discouraged because you incur costs and will not pick up security updates.

` .google.protobuf.Duration running_timeout = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### clearUid()
    
    
    public WorkstationConfig.Builder clearUid()

Output only. A system-assigned unique identifier for this workstation configuration.

` string uid = 3 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.field_info) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` | This builder for chaining.  
  
### clearUpdateTime()
    
    
    public WorkstationConfig.Builder clearUpdateTime()

Output only. Time when this workstation configuration was most recently updated.

` .google.protobuf.Timestamp update_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### containsAnnotations(String key)
    
    
    public boolean containsAnnotations(String key)

Optional. Client-specified annotations.

`map<string, string> annotations = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### containsLabels(String key)
    
    
    public boolean containsLabels(String key)

Optional. [Labels](https://cloud.google.com/workstations/docs/label-resources) that are applied to the workstation configuration and that are also propagated to the underlying Compute Engine resources.

`map<string, string> labels = 18 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAllowedPorts(int index)
    
    
    public WorkstationConfig.PortRange getAllowedPorts(int index)

Optional. A list of PortRanges specifying single ports or ranges of ports that are externally accessible in the workstation. Allowed ports must be one of 22, 80, or within range 1024-65535. If not specified defaults to ports 22, 80, and ports 1024-65535.

` repeated .google.cloud.workstations.v1.WorkstationConfig.PortRange allowed_ports = 25 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.PortRange](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.PortRange)` |   
  
### getAllowedPortsBuilder(int index)
    
    
    public WorkstationConfig.PortRange.Builder getAllowedPortsBuilder(int index)

Optional. A list of PortRanges specifying single ports or ranges of ports that are externally accessible in the workstation. Allowed ports must be one of 22, 80, or within range 1024-65535. If not specified defaults to ports 22, 80, and ports 1024-65535.

` repeated .google.cloud.workstations.v1.WorkstationConfig.PortRange allowed_ports = 25 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.PortRange.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.PortRange.Builder)` |   
  
### getAllowedPortsBuilderList()
    
    
    public List<WorkstationConfig.PortRange.Builder> getAllowedPortsBuilderList()

Optional. A list of PortRanges specifying single ports or ranges of ports that are externally accessible in the workstation. Allowed ports must be one of 22, 80, or within range 1024-65535. If not specified defaults to ports 22, 80, and ports 1024-65535.

` repeated .google.cloud.workstations.v1.WorkstationConfig.PortRange allowed_ports = 25 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.PortRange.Builder)>` |   
  
### getAllowedPortsCount()
    
    
    public int getAllowedPortsCount()

Optional. A list of PortRanges specifying single ports or ranges of ports that are externally accessible in the workstation. Allowed ports must be one of 22, 80, or within range 1024-65535. If not specified defaults to ports 22, 80, and ports 1024-65535.

` repeated .google.cloud.workstations.v1.WorkstationConfig.PortRange allowed_ports = 25 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAllowedPortsList()
    
    
    public List<WorkstationConfig.PortRange> getAllowedPortsList()

Optional. A list of PortRanges specifying single ports or ranges of ports that are externally accessible in the workstation. Allowed ports must be one of 22, 80, or within range 1024-65535. If not specified defaults to ports 22, 80, and ports 1024-65535.

` repeated .google.cloud.workstations.v1.WorkstationConfig.PortRange allowed_ports = 25 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[PortRange](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.PortRange)>` |   
  
### getAllowedPortsOrBuilder(int index)
    
    
    public WorkstationConfig.PortRangeOrBuilder getAllowedPortsOrBuilder(int index)

Optional. A list of PortRanges specifying single ports or ranges of ports that are externally accessible in the workstation. Allowed ports must be one of 22, 80, or within range 1024-65535. If not specified defaults to ports 22, 80, and ports 1024-65535.

` repeated .google.cloud.workstations.v1.WorkstationConfig.PortRange allowed_ports = 25 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.PortRangeOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.PortRangeOrBuilder)` |   
  
### getAllowedPortsOrBuilderList()
    
    
    public List<? extends WorkstationConfig.PortRangeOrBuilder> getAllowedPortsOrBuilderList()

Optional. A list of PortRanges specifying single ports or ranges of ports that are externally accessible in the workstation. Allowed ports must be one of 22, 80, or within range 1024-65535. If not specified defaults to ports 22, 80, and ports 1024-65535.

` repeated .google.cloud.workstations.v1.WorkstationConfig.PortRange allowed_ports = 25 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.workstations.v1.WorkstationConfig.PortRangeOrBuilder>` |   
  
### getAnnotations() (deprecated)
    
    
    public Map<String,String> getAnnotations()

Use [#getAnnotationsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder#com_google_cloud_workstations_v1_WorkstationConfig_Builder_getAnnotationsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getAnnotationsCount()
    
    
    public int getAnnotationsCount()

Optional. Client-specified annotations.

`map<string, string> annotations = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAnnotationsMap()
    
    
    public Map<String,String> getAnnotationsMap()

Optional. Client-specified annotations.

`map<string, string> annotations = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getAnnotationsOrDefault(String key, String defaultValue)
    
    
    public String getAnnotationsOrDefault(String key, String defaultValue)

Optional. Client-specified annotations.

`map<string, string> annotations = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getAnnotationsOrThrow(String key)
    
    
    public String getAnnotationsOrThrow(String key)

Optional. Client-specified annotations.

`map<string, string> annotations = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getConditions(int index)
    
    
    public Status getConditions(int index)

Output only. Status conditions describing the workstation configuration's current state.

` repeated .google.rpc.Status conditions = 16 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.rpc.Status` |   
  
### getConditionsBuilder(int index)
    
    
    public Status.Builder getConditionsBuilder(int index)

Output only. Status conditions describing the workstation configuration's current state.

` repeated .google.rpc.Status conditions = 16 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.rpc.Status.Builder` |   
  
### getConditionsBuilderList()
    
    
    public List<Status.Builder> getConditionsBuilderList()

Output only. Status conditions describing the workstation configuration's current state.

` repeated .google.rpc.Status conditions = 16 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<com.google.rpc.Status.Builder>` |   
  
### getConditionsCount()
    
    
    public int getConditionsCount()

Output only. Status conditions describing the workstation configuration's current state.

` repeated .google.rpc.Status conditions = 16 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getConditionsList()
    
    
    public List<Status> getConditionsList()

Output only. Status conditions describing the workstation configuration's current state.

` repeated .google.rpc.Status conditions = 16 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<com.google.rpc.Status>` |   
  
### getConditionsOrBuilder(int index)
    
    
    public StatusOrBuilder getConditionsOrBuilder(int index)

Output only. Status conditions describing the workstation configuration's current state.

` repeated .google.rpc.Status conditions = 16 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.rpc.StatusOrBuilder` |   
  
### getConditionsOrBuilderList()
    
    
    public List<? extends StatusOrBuilder> getConditionsOrBuilderList()

Output only. Status conditions describing the workstation configuration's current state.

` repeated .google.rpc.Status conditions = 16 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.rpc.StatusOrBuilder>` |   
  
### getContainer()
    
    
    public WorkstationConfig.Container getContainer()

Optional. Container that runs upon startup for each workstation using this workstation configuration.

` .google.cloud.workstations.v1.WorkstationConfig.Container container = 14 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Container](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Container)` | The container.  
  
### getContainerBuilder()
    
    
    public WorkstationConfig.Container.Builder getContainerBuilder()

Optional. Container that runs upon startup for each workstation using this workstation configuration.

` .google.cloud.workstations.v1.WorkstationConfig.Container container = 14 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Container.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Container.Builder)` |   
  
### getContainerOrBuilder()
    
    
    public WorkstationConfig.ContainerOrBuilder getContainerOrBuilder()

Optional. Container that runs upon startup for each workstation using this workstation configuration.

` .google.cloud.workstations.v1.WorkstationConfig.Container container = 14 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.ContainerOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.ContainerOrBuilder)` |   
  
### getCreateTime()
    
    
    public Timestamp getCreateTime()

Output only. Time when this workstation configuration was created.

` .google.protobuf.Timestamp create_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeBuilder()
    
    
    public Timestamp.Builder getCreateTimeBuilder()

Output only. Time when this workstation configuration was created.

` .google.protobuf.Timestamp create_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)` |   
  
### getCreateTimeOrBuilder()
    
    
    public TimestampOrBuilder getCreateTimeOrBuilder()

Output only. Time when this workstation configuration was created.

` .google.protobuf.Timestamp create_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDefaultInstanceForType()
    
    
    public WorkstationConfig getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig)` |   
  
### getDegraded()
    
    
    public boolean getDegraded()

Output only. Whether this workstation configuration is in degraded mode, in which case it may require user action to restore full functionality. The conditions field contains detailed information about the status of the configuration.

`bool degraded = 15 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The degraded.  
  
### getDeleteTime()
    
    
    public Timestamp getDeleteTime()

Output only. Time when this workstation configuration was soft-deleted.

` .google.protobuf.Timestamp delete_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The deleteTime.  
  
### getDeleteTimeBuilder()
    
    
    public Timestamp.Builder getDeleteTimeBuilder()

Output only. Time when this workstation configuration was soft-deleted.

` .google.protobuf.Timestamp delete_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)` |   
  
### getDeleteTimeOrBuilder()
    
    
    public TimestampOrBuilder getDeleteTimeOrBuilder()

Output only. Time when this workstation configuration was soft-deleted.

` .google.protobuf.Timestamp delete_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDescriptorForType()
    
    
    public Descriptors.Descriptor getDescriptorForType()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getDescriptorForType__)

### getDisableTcpConnections()
    
    
    public boolean getDisableTcpConnections()

Optional. Disables support for plain TCP connections in the workstation. By default the service supports TCP connections through a websocket relay. Setting this option to true disables that relay, which prevents the usage of services that require plain TCP connections, such as SSH. When enabled, all communication must occur over HTTPS or WSS.

`bool disable_tcp_connections = 24 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The disableTcpConnections.  
  
### getDisplayName()
    
    
    public String getDisplayName()

Optional. Human-readable name for this workstation configuration.

`string display_name = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The displayName.  
  
### getDisplayNameBytes()
    
    
    public ByteString getDisplayNameBytes()

Optional. Human-readable name for this workstation configuration.

`string display_name = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for displayName.  
  
### getEnableAuditAgent()
    
    
    public boolean getEnableAuditAgent()

Optional. Whether to enable Linux `auditd` logging on the workstation. When enabled, a service_account must also be specified that has `roles/logging.logWriter` and `roles/monitoring.metricWriter` on the project. Operating system audit logging is distinct from [Cloud Audit Logs](https://cloud.google.com/workstations/docs/audit-logging) and [Container output logging](https://cloud.google.com/workstations/docs/container-output-logging#overview). Operating system audit logs are available in the [Cloud Logging](https://cloud.google.com/logging/docs) console by querying:

resource.type="gce_instance" log_name:"/logs/linux-auditd"

`bool enable_audit_agent = 20 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enableAuditAgent.  
  
### getEncryptionKey()
    
    
    public WorkstationConfig.CustomerEncryptionKey getEncryptionKey()

Immutable. Encrypts resources of this workstation configuration using a customer-managed encryption key (CMEK).

If specified, the boot disk of the Compute Engine instance and the persistent disk are encrypted using this encryption key. If this field is not set, the disks are encrypted using a generated key. Customer-managed encryption keys do not protect disk metadata.

If the customer-managed encryption key is rotated, when the workstation instance is stopped, the system attempts to recreate the persistent disk with the new version of the key. Be sure to keep older versions of the key until the persistent disk is recreated. Otherwise, data on the persistent disk might be lost.

If the encryption key is revoked, the workstation session automatically stops within 7 hours.

Immutable after the workstation configuration is created.

` .google.cloud.workstations.v1.WorkstationConfig.CustomerEncryptionKey encryption_key = 17 [(.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.CustomerEncryptionKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.CustomerEncryptionKey)` | The encryptionKey.  
  
### getEncryptionKeyBuilder()
    
    
    public WorkstationConfig.CustomerEncryptionKey.Builder getEncryptionKeyBuilder()

Immutable. Encrypts resources of this workstation configuration using a customer-managed encryption key (CMEK).

If specified, the boot disk of the Compute Engine instance and the persistent disk are encrypted using this encryption key. If this field is not set, the disks are encrypted using a generated key. Customer-managed encryption keys do not protect disk metadata.

If the customer-managed encryption key is rotated, when the workstation instance is stopped, the system attempts to recreate the persistent disk with the new version of the key. Be sure to keep older versions of the key until the persistent disk is recreated. Otherwise, data on the persistent disk might be lost.

If the encryption key is revoked, the workstation session automatically stops within 7 hours.

Immutable after the workstation configuration is created.

` .google.cloud.workstations.v1.WorkstationConfig.CustomerEncryptionKey encryption_key = 17 [(.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.CustomerEncryptionKey.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.CustomerEncryptionKey.Builder)` |   
  
### getEncryptionKeyOrBuilder()
    
    
    public WorkstationConfig.CustomerEncryptionKeyOrBuilder getEncryptionKeyOrBuilder()

Immutable. Encrypts resources of this workstation configuration using a customer-managed encryption key (CMEK).

If specified, the boot disk of the Compute Engine instance and the persistent disk are encrypted using this encryption key. If this field is not set, the disks are encrypted using a generated key. Customer-managed encryption keys do not protect disk metadata.

If the customer-managed encryption key is rotated, when the workstation instance is stopped, the system attempts to recreate the persistent disk with the new version of the key. Be sure to keep older versions of the key until the persistent disk is recreated. Otherwise, data on the persistent disk might be lost.

If the encryption key is revoked, the workstation session automatically stops within 7 hours.

Immutable after the workstation configuration is created.

` .google.cloud.workstations.v1.WorkstationConfig.CustomerEncryptionKey encryption_key = 17 [(.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.CustomerEncryptionKeyOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.CustomerEncryptionKeyOrBuilder)` |   
  
### getEphemeralDirectories(int index)
    
    
    public WorkstationConfig.EphemeralDirectory getEphemeralDirectories(int index)

Optional. Ephemeral directories which won't persist across workstation sessions.

` repeated .google.cloud.workstations.v1.WorkstationConfig.EphemeralDirectory ephemeral_directories = 22 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.EphemeralDirectory](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.EphemeralDirectory)` |   
  
### getEphemeralDirectoriesBuilder(int index)
    
    
    public WorkstationConfig.EphemeralDirectory.Builder getEphemeralDirectoriesBuilder(int index)

Optional. Ephemeral directories which won't persist across workstation sessions.

` repeated .google.cloud.workstations.v1.WorkstationConfig.EphemeralDirectory ephemeral_directories = 22 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.EphemeralDirectory.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.EphemeralDirectory.Builder)` |   
  
### getEphemeralDirectoriesBuilderList()
    
    
    public List<WorkstationConfig.EphemeralDirectory.Builder> getEphemeralDirectoriesBuilderList()

Optional. Ephemeral directories which won't persist across workstation sessions.

` repeated .google.cloud.workstations.v1.WorkstationConfig.EphemeralDirectory ephemeral_directories = 22 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.EphemeralDirectory.Builder)>` |   
  
### getEphemeralDirectoriesCount()
    
    
    public int getEphemeralDirectoriesCount()

Optional. Ephemeral directories which won't persist across workstation sessions.

` repeated .google.cloud.workstations.v1.WorkstationConfig.EphemeralDirectory ephemeral_directories = 22 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getEphemeralDirectoriesList()
    
    
    public List<WorkstationConfig.EphemeralDirectory> getEphemeralDirectoriesList()

Optional. Ephemeral directories which won't persist across workstation sessions.

` repeated .google.cloud.workstations.v1.WorkstationConfig.EphemeralDirectory ephemeral_directories = 22 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[EphemeralDirectory](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.EphemeralDirectory)>` |   
  
### getEphemeralDirectoriesOrBuilder(int index)
    
    
    public WorkstationConfig.EphemeralDirectoryOrBuilder getEphemeralDirectoriesOrBuilder(int index)

Optional. Ephemeral directories which won't persist across workstation sessions.

` repeated .google.cloud.workstations.v1.WorkstationConfig.EphemeralDirectory ephemeral_directories = 22 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.EphemeralDirectoryOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.EphemeralDirectoryOrBuilder)` |   
  
### getEphemeralDirectoriesOrBuilderList()
    
    
    public List<? extends WorkstationConfig.EphemeralDirectoryOrBuilder> getEphemeralDirectoriesOrBuilderList()

Optional. Ephemeral directories which won't persist across workstation sessions.

` repeated .google.cloud.workstations.v1.WorkstationConfig.EphemeralDirectory ephemeral_directories = 22 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.workstations.v1.WorkstationConfig.EphemeralDirectoryOrBuilder>` |   
  
### getEtag()
    
    
    public String getEtag()

Optional. Checksum computed by the server. May be sent on update and delete requests to make sure that the client has an up-to-date value before proceeding.

`string etag = 9 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The etag.  
  
### getEtagBytes()
    
    
    public ByteString getEtagBytes()

Optional. Checksum computed by the server. May be sent on update and delete requests to make sure that the client has an up-to-date value before proceeding.

`string etag = 9 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for etag.  
  
### getGrantWorkstationAdminRoleOnCreate()
    
    
    public boolean getGrantWorkstationAdminRoleOnCreate()

Optional. Grant creator of a workstation `roles/workstations.policyAdmin` role along with `roles/workstations.user` role on the workstation created by them. This allows workstation users to share access to either their entire workstation, or individual ports. Defaults to false.

` bool grant_workstation_admin_role_on_create = 29 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The grantWorkstationAdminRoleOnCreate.  
  
### getHost()
    
    
    public WorkstationConfig.Host getHost()

Optional. Runtime host for the workstation.

` .google.cloud.workstations.v1.WorkstationConfig.Host host = 12 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Host](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Host)` | The host.  
  
### getHostBuilder()
    
    
    public WorkstationConfig.Host.Builder getHostBuilder()

Optional. Runtime host for the workstation.

` .google.cloud.workstations.v1.WorkstationConfig.Host host = 12 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Host.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Host.Builder)` |   
  
### getHostOrBuilder()
    
    
    public WorkstationConfig.HostOrBuilder getHostOrBuilder()

Optional. Runtime host for the workstation.

` .google.cloud.workstations.v1.WorkstationConfig.Host host = 12 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.HostOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.HostOrBuilder)` |   
  
### getIdleTimeout()
    
    
    public Duration getIdleTimeout()

Optional. Number of seconds to wait before automatically stopping a workstation after it last received user traffic.

A value of `"0s"` indicates that Cloud Workstations VMs created with this configuration should never time out due to idleness. Provide [duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#duration) terminated by `s` for seconds—for example, `"7200s"` (2 hours). The default is `"1200s"` (20 minutes).

`.google.protobuf.Duration idle_timeout = 10 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)` | The idleTimeout.  
  
### getIdleTimeoutBuilder()
    
    
    public Duration.Builder getIdleTimeoutBuilder()

Optional. Number of seconds to wait before automatically stopping a workstation after it last received user traffic.

A value of `"0s"` indicates that Cloud Workstations VMs created with this configuration should never time out due to idleness. Provide [duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#duration) terminated by `s` for seconds—for example, `"7200s"` (2 hours). The default is `"1200s"` (20 minutes).

`.google.protobuf.Duration idle_timeout = 10 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.Builder.html)` |   
  
### getIdleTimeoutOrBuilder()
    
    
    public DurationOrBuilder getIdleTimeoutOrBuilder()

Optional. Number of seconds to wait before automatically stopping a workstation after it last received user traffic.

A value of `"0s"` indicates that Cloud Workstations VMs created with this configuration should never time out due to idleness. Provide [duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#duration) terminated by `s` for seconds—for example, `"7200s"` (2 hours). The default is `"1200s"` (20 minutes).

`.google.protobuf.Duration idle_timeout = 10 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[DurationOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DurationOrBuilder.html)` |   
  
### getLabels() (deprecated)
    
    
    public Map<String,String> getLabels()

Use [#getLabelsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder#com_google_cloud_workstations_v1_WorkstationConfig_Builder_getLabelsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsCount()
    
    
    public int getLabelsCount()

Optional. [Labels](https://cloud.google.com/workstations/docs/label-resources) that are applied to the workstation configuration and that are also propagated to the underlying Compute Engine resources.

`map<string, string> labels = 18 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getLabelsMap()
    
    
    public Map<String,String> getLabelsMap()

Optional. [Labels](https://cloud.google.com/workstations/docs/label-resources) that are applied to the workstation configuration and that are also propagated to the underlying Compute Engine resources.

`map<string, string> labels = 18 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsOrDefault(String key, String defaultValue)
    
    
    public String getLabelsOrDefault(String key, String defaultValue)

Optional. [Labels](https://cloud.google.com/workstations/docs/label-resources) that are applied to the workstation configuration and that are also propagated to the underlying Compute Engine resources.

`map<string, string> labels = 18 [(.google.api.field_behavior) = OPTIONAL];`

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

Optional. [Labels](https://cloud.google.com/workstations/docs/label-resources) that are applied to the workstation configuration and that are also propagated to the underlying Compute Engine resources.

`map<string, string> labels = 18 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getMaxUsableWorkstations()
    
    
    public int getMaxUsableWorkstations()

Optional. Maximum number of workstations under this configuration a user can have `workstations.workstation.use` permission on.

Only enforced on CreateWorkstation API calls on the user issuing the API request. Can be overridden by:

  * granting a user workstations.workstationConfigs.exemptMaxUsableWorkstationLimit permission, or
  * having a user with that permission create a workstation and granting another user `workstations.workstation.use` permission on that workstation.

If not specified, defaults to `0`, which indicates unlimited.




`int32 max_usable_workstations = 28 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The maxUsableWorkstations.  
  
### getMutableAnnotations() (deprecated)
    
    
    public Map<String,String> getMutableAnnotations()

Use alternate mutation accessors instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getMutableLabels() (deprecated)
    
    
    public Map<String,String> getMutableLabels()

Use alternate mutation accessors instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getName()
    
    
    public String getName()

Identifier. Full name of this workstation configuration.

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public ByteString getNameBytes()

Identifier. Full name of this workstation configuration.

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getPersistentDirectories(int index)
    
    
    public WorkstationConfig.PersistentDirectory getPersistentDirectories(int index)

Optional. Directories to persist across workstation sessions.

` repeated .google.cloud.workstations.v1.WorkstationConfig.PersistentDirectory persistent_directories = 13 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.PersistentDirectory](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.PersistentDirectory)` |   
  
### getPersistentDirectoriesBuilder(int index)
    
    
    public WorkstationConfig.PersistentDirectory.Builder getPersistentDirectoriesBuilder(int index)

Optional. Directories to persist across workstation sessions.

` repeated .google.cloud.workstations.v1.WorkstationConfig.PersistentDirectory persistent_directories = 13 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.PersistentDirectory.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.PersistentDirectory.Builder)` |   
  
### getPersistentDirectoriesBuilderList()
    
    
    public List<WorkstationConfig.PersistentDirectory.Builder> getPersistentDirectoriesBuilderList()

Optional. Directories to persist across workstation sessions.

` repeated .google.cloud.workstations.v1.WorkstationConfig.PersistentDirectory persistent_directories = 13 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.PersistentDirectory.Builder)>` |   
  
### getPersistentDirectoriesCount()
    
    
    public int getPersistentDirectoriesCount()

Optional. Directories to persist across workstation sessions.

` repeated .google.cloud.workstations.v1.WorkstationConfig.PersistentDirectory persistent_directories = 13 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getPersistentDirectoriesList()
    
    
    public List<WorkstationConfig.PersistentDirectory> getPersistentDirectoriesList()

Optional. Directories to persist across workstation sessions.

` repeated .google.cloud.workstations.v1.WorkstationConfig.PersistentDirectory persistent_directories = 13 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[PersistentDirectory](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.PersistentDirectory)>` |   
  
### getPersistentDirectoriesOrBuilder(int index)
    
    
    public WorkstationConfig.PersistentDirectoryOrBuilder getPersistentDirectoriesOrBuilder(int index)

Optional. Directories to persist across workstation sessions.

` repeated .google.cloud.workstations.v1.WorkstationConfig.PersistentDirectory persistent_directories = 13 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.PersistentDirectoryOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.PersistentDirectoryOrBuilder)` |   
  
### getPersistentDirectoriesOrBuilderList()
    
    
    public List<? extends WorkstationConfig.PersistentDirectoryOrBuilder> getPersistentDirectoriesOrBuilderList()

Optional. Directories to persist across workstation sessions.

` repeated .google.cloud.workstations.v1.WorkstationConfig.PersistentDirectory persistent_directories = 13 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.workstations.v1.WorkstationConfig.PersistentDirectoryOrBuilder>` |   
  
### getReadinessChecks(int index)
    
    
    public WorkstationConfig.ReadinessCheck getReadinessChecks(int index)

Optional. Readiness checks to perform when starting a workstation using this workstation configuration. Mark a workstation as running only after all specified readiness checks return 200 status codes.

` repeated .google.cloud.workstations.v1.WorkstationConfig.ReadinessCheck readiness_checks = 19 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.ReadinessCheck](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.ReadinessCheck)` |   
  
### getReadinessChecksBuilder(int index)
    
    
    public WorkstationConfig.ReadinessCheck.Builder getReadinessChecksBuilder(int index)

Optional. Readiness checks to perform when starting a workstation using this workstation configuration. Mark a workstation as running only after all specified readiness checks return 200 status codes.

` repeated .google.cloud.workstations.v1.WorkstationConfig.ReadinessCheck readiness_checks = 19 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.ReadinessCheck.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.ReadinessCheck.Builder)` |   
  
### getReadinessChecksBuilderList()
    
    
    public List<WorkstationConfig.ReadinessCheck.Builder> getReadinessChecksBuilderList()

Optional. Readiness checks to perform when starting a workstation using this workstation configuration. Mark a workstation as running only after all specified readiness checks return 200 status codes.

` repeated .google.cloud.workstations.v1.WorkstationConfig.ReadinessCheck readiness_checks = 19 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.ReadinessCheck.Builder)>` |   
  
### getReadinessChecksCount()
    
    
    public int getReadinessChecksCount()

Optional. Readiness checks to perform when starting a workstation using this workstation configuration. Mark a workstation as running only after all specified readiness checks return 200 status codes.

` repeated .google.cloud.workstations.v1.WorkstationConfig.ReadinessCheck readiness_checks = 19 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getReadinessChecksList()
    
    
    public List<WorkstationConfig.ReadinessCheck> getReadinessChecksList()

Optional. Readiness checks to perform when starting a workstation using this workstation configuration. Mark a workstation as running only after all specified readiness checks return 200 status codes.

` repeated .google.cloud.workstations.v1.WorkstationConfig.ReadinessCheck readiness_checks = 19 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ReadinessCheck](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.ReadinessCheck)>` |   
  
### getReadinessChecksOrBuilder(int index)
    
    
    public WorkstationConfig.ReadinessCheckOrBuilder getReadinessChecksOrBuilder(int index)

Optional. Readiness checks to perform when starting a workstation using this workstation configuration. Mark a workstation as running only after all specified readiness checks return 200 status codes.

` repeated .google.cloud.workstations.v1.WorkstationConfig.ReadinessCheck readiness_checks = 19 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.ReadinessCheckOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.ReadinessCheckOrBuilder)` |   
  
### getReadinessChecksOrBuilderList()
    
    
    public List<? extends WorkstationConfig.ReadinessCheckOrBuilder> getReadinessChecksOrBuilderList()

Optional. Readiness checks to perform when starting a workstation using this workstation configuration. Mark a workstation as running only after all specified readiness checks return 200 status codes.

` repeated .google.cloud.workstations.v1.WorkstationConfig.ReadinessCheck readiness_checks = 19 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.workstations.v1.WorkstationConfig.ReadinessCheckOrBuilder>` |   
  
### getReconciling()
    
    
    public boolean getReconciling()

Output only. Indicates whether this workstation configuration is currently being updated to match its intended state.

`bool reconciling = 4 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The reconciling.  
  
### getReplicaZones(int index)
    
    
    public String getReplicaZones(int index)

Optional. Immutable. Specifies the zones used to replicate the VM and disk resources within the region. If set, exactly two zones within the workstation cluster's region must be specified—for example, `['us-central1-a', 'us-central1-f']`. If this field is empty, two default zones within the region are used.

Immutable after the workstation configuration is created.

` repeated string replica_zones = 23 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = IMMUTABLE]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The replicaZones at the given index.  
  
### getReplicaZonesBytes(int index)
    
    
    public ByteString getReplicaZonesBytes(int index)

Optional. Immutable. Specifies the zones used to replicate the VM and disk resources within the region. If set, exactly two zones within the workstation cluster's region must be specified—for example, `['us-central1-a', 'us-central1-f']`. If this field is empty, two default zones within the region are used.

Immutable after the workstation configuration is created.

` repeated string replica_zones = 23 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = IMMUTABLE]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the replicaZones at the given index.  
  
### getReplicaZonesCount()
    
    
    public int getReplicaZonesCount()

Optional. Immutable. Specifies the zones used to replicate the VM and disk resources within the region. If set, exactly two zones within the workstation cluster's region must be specified—for example, `['us-central1-a', 'us-central1-f']`. If this field is empty, two default zones within the region are used.

Immutable after the workstation configuration is created.

` repeated string replica_zones = 23 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of replicaZones.  
  
### getReplicaZonesList()
    
    
    public ProtocolStringList getReplicaZonesList()

Optional. Immutable. Specifies the zones used to replicate the VM and disk resources within the region. If set, exactly two zones within the workstation cluster's region must be specified—for example, `['us-central1-a', 'us-central1-f']`. If this field is empty, two default zones within the region are used.

Immutable after the workstation configuration is created.

` repeated string replica_zones = 23 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[ProtocolStringList](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ProtocolStringList.html)` | A list containing the replicaZones.  
  
### getRunningTimeout()
    
    
    public Duration getRunningTimeout()

Optional. Number of seconds that a workstation can run until it is automatically shut down. We recommend that workstations be shut down daily to reduce costs and so that security updates can be applied upon restart. The idle_timeout and running_timeout fields are independent of each other. Note that the running_timeout field shuts down VMs after the specified time, regardless of whether or not the VMs are idle.

Provide duration terminated by `s` for seconds—for example, `"54000s"` (15 hours). Defaults to `"43200s"` (12 hours). A value of `"0s"` indicates that workstations using this configuration should never time out. If encryption_key is set, it must be greater than `"0s"` and less than `"86400s"` (24 hours).

Warning: A value of `"0s"` indicates that Cloud Workstations VMs created with this configuration have no maximum running time. This is strongly discouraged because you incur costs and will not pick up security updates.

` .google.protobuf.Duration running_timeout = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)` | The runningTimeout.  
  
### getRunningTimeoutBuilder()
    
    
    public Duration.Builder getRunningTimeoutBuilder()

Optional. Number of seconds that a workstation can run until it is automatically shut down. We recommend that workstations be shut down daily to reduce costs and so that security updates can be applied upon restart. The idle_timeout and running_timeout fields are independent of each other. Note that the running_timeout field shuts down VMs after the specified time, regardless of whether or not the VMs are idle.

Provide duration terminated by `s` for seconds—for example, `"54000s"` (15 hours). Defaults to `"43200s"` (12 hours). A value of `"0s"` indicates that workstations using this configuration should never time out. If encryption_key is set, it must be greater than `"0s"` and less than `"86400s"` (24 hours).

Warning: A value of `"0s"` indicates that Cloud Workstations VMs created with this configuration have no maximum running time. This is strongly discouraged because you incur costs and will not pick up security updates.

` .google.protobuf.Duration running_timeout = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.Builder.html)` |   
  
### getRunningTimeoutOrBuilder()
    
    
    public DurationOrBuilder getRunningTimeoutOrBuilder()

Optional. Number of seconds that a workstation can run until it is automatically shut down. We recommend that workstations be shut down daily to reduce costs and so that security updates can be applied upon restart. The idle_timeout and running_timeout fields are independent of each other. Note that the running_timeout field shuts down VMs after the specified time, regardless of whether or not the VMs are idle.

Provide duration terminated by `s` for seconds—for example, `"54000s"` (15 hours). Defaults to `"43200s"` (12 hours). A value of `"0s"` indicates that workstations using this configuration should never time out. If encryption_key is set, it must be greater than `"0s"` and less than `"86400s"` (24 hours).

Warning: A value of `"0s"` indicates that Cloud Workstations VMs created with this configuration have no maximum running time. This is strongly discouraged because you incur costs and will not pick up security updates.

` .google.protobuf.Duration running_timeout = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[DurationOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DurationOrBuilder.html)` |   
  
### getUid()
    
    
    public String getUid()

Output only. A system-assigned unique identifier for this workstation configuration.

` string uid = 3 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.field_info) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The uid.  
  
### getUidBytes()
    
    
    public ByteString getUidBytes()

Output only. A system-assigned unique identifier for this workstation configuration.

` string uid = 3 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.field_info) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for uid.  
  
### getUpdateTime()
    
    
    public Timestamp getUpdateTime()

Output only. Time when this workstation configuration was most recently updated.

` .google.protobuf.Timestamp update_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The updateTime.  
  
### getUpdateTimeBuilder()
    
    
    public Timestamp.Builder getUpdateTimeBuilder()

Output only. Time when this workstation configuration was most recently updated.

` .google.protobuf.Timestamp update_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)` |   
  
### getUpdateTimeOrBuilder()
    
    
    public TimestampOrBuilder getUpdateTimeOrBuilder()

Output only. Time when this workstation configuration was most recently updated.

` .google.protobuf.Timestamp update_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### hasContainer()
    
    
    public boolean hasContainer()

Optional. Container that runs upon startup for each workstation using this workstation configuration.

` .google.cloud.workstations.v1.WorkstationConfig.Container container = 14 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the container field is set.  
  
### hasCreateTime()
    
    
    public boolean hasCreateTime()

Output only. Time when this workstation configuration was created.

` .google.protobuf.Timestamp create_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasDeleteTime()
    
    
    public boolean hasDeleteTime()

Output only. Time when this workstation configuration was soft-deleted.

` .google.protobuf.Timestamp delete_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the deleteTime field is set.  
  
### hasEncryptionKey()
    
    
    public boolean hasEncryptionKey()

Immutable. Encrypts resources of this workstation configuration using a customer-managed encryption key (CMEK).

If specified, the boot disk of the Compute Engine instance and the persistent disk are encrypted using this encryption key. If this field is not set, the disks are encrypted using a generated key. Customer-managed encryption keys do not protect disk metadata.

If the customer-managed encryption key is rotated, when the workstation instance is stopped, the system attempts to recreate the persistent disk with the new version of the key. Be sure to keep older versions of the key until the persistent disk is recreated. Otherwise, data on the persistent disk might be lost.

If the encryption key is revoked, the workstation session automatically stops within 7 hours.

Immutable after the workstation configuration is created.

` .google.cloud.workstations.v1.WorkstationConfig.CustomerEncryptionKey encryption_key = 17 [(.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the encryptionKey field is set.  
  
### hasHost()
    
    
    public boolean hasHost()

Optional. Runtime host for the workstation.

` .google.cloud.workstations.v1.WorkstationConfig.Host host = 12 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the host field is set.  
  
### hasIdleTimeout()
    
    
    public boolean hasIdleTimeout()

Optional. Number of seconds to wait before automatically stopping a workstation after it last received user traffic.

A value of `"0s"` indicates that Cloud Workstations VMs created with this configuration should never time out due to idleness. Provide [duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#duration) terminated by `s` for seconds—for example, `"7200s"` (2 hours). The default is `"1200s"` (20 minutes).

`.google.protobuf.Duration idle_timeout = 10 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the idleTimeout field is set.  
  
### hasRunningTimeout()
    
    
    public boolean hasRunningTimeout()

Optional. Number of seconds that a workstation can run until it is automatically shut down. We recommend that workstations be shut down daily to reduce costs and so that security updates can be applied upon restart. The idle_timeout and running_timeout fields are independent of each other. Note that the running_timeout field shuts down VMs after the specified time, regardless of whether or not the VMs are idle.

Provide duration terminated by `s` for seconds—for example, `"54000s"` (15 hours). Defaults to `"43200s"` (12 hours). A value of `"0s"` indicates that workstations using this configuration should never time out. If encryption_key is set, it must be greater than `"0s"` and less than `"86400s"` (24 hours).

Warning: A value of `"0s"` indicates that Cloud Workstations VMs created with this configuration have no maximum running time. This is strongly discouraged because you incur costs and will not pick up security updates.

` .google.protobuf.Duration running_timeout = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the runningTimeout field is set.  
  
### hasUpdateTime()
    
    
    public boolean hasUpdateTime()

Output only. Time when this workstation configuration was most recently updated.

` .google.protobuf.Timestamp update_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

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

### mergeContainer(WorkstationConfig.Container value)
    
    
    public WorkstationConfig.Builder mergeContainer(WorkstationConfig.Container value)

Optional. Container that runs upon startup for each workstation using this workstation configuration.

` .google.cloud.workstations.v1.WorkstationConfig.Container container = 14 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[WorkstationConfig.Container](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Container)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### mergeCreateTime(Timestamp value)
    
    
    public WorkstationConfig.Builder mergeCreateTime(Timestamp value)

Output only. Time when this workstation configuration was created.

` .google.protobuf.Timestamp create_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### mergeDeleteTime(Timestamp value)
    
    
    public WorkstationConfig.Builder mergeDeleteTime(Timestamp value)

Output only. Time when this workstation configuration was soft-deleted.

` .google.protobuf.Timestamp delete_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### mergeEncryptionKey(WorkstationConfig.CustomerEncryptionKey value)
    
    
    public WorkstationConfig.Builder mergeEncryptionKey(WorkstationConfig.CustomerEncryptionKey value)

Immutable. Encrypts resources of this workstation configuration using a customer-managed encryption key (CMEK).

If specified, the boot disk of the Compute Engine instance and the persistent disk are encrypted using this encryption key. If this field is not set, the disks are encrypted using a generated key. Customer-managed encryption keys do not protect disk metadata.

If the customer-managed encryption key is rotated, when the workstation instance is stopped, the system attempts to recreate the persistent disk with the new version of the key. Be sure to keep older versions of the key until the persistent disk is recreated. Otherwise, data on the persistent disk might be lost.

If the encryption key is revoked, the workstation session automatically stops within 7 hours.

Immutable after the workstation configuration is created.

` .google.cloud.workstations.v1.WorkstationConfig.CustomerEncryptionKey encryption_key = 17 [(.google.api.field_behavior) = IMMUTABLE]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[WorkstationConfig.CustomerEncryptionKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.CustomerEncryptionKey)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### mergeFrom(WorkstationConfig other)
    
    
    public WorkstationConfig.Builder mergeFrom(WorkstationConfig other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[WorkstationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public WorkstationConfig.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public WorkstationConfig.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### mergeHost(WorkstationConfig.Host value)
    
    
    public WorkstationConfig.Builder mergeHost(WorkstationConfig.Host value)

Optional. Runtime host for the workstation.

` .google.cloud.workstations.v1.WorkstationConfig.Host host = 12 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[WorkstationConfig.Host](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Host)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### mergeIdleTimeout(Duration value)
    
    
    public WorkstationConfig.Builder mergeIdleTimeout(Duration value)

Optional. Number of seconds to wait before automatically stopping a workstation after it last received user traffic.

A value of `"0s"` indicates that Cloud Workstations VMs created with this configuration should never time out due to idleness. Provide [duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#duration) terminated by `s` for seconds—for example, `"7200s"` (2 hours). The default is `"1200s"` (20 minutes).

`.google.protobuf.Duration idle_timeout = 10 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### mergeRunningTimeout(Duration value)
    
    
    public WorkstationConfig.Builder mergeRunningTimeout(Duration value)

Optional. Number of seconds that a workstation can run until it is automatically shut down. We recommend that workstations be shut down daily to reduce costs and so that security updates can be applied upon restart. The idle_timeout and running_timeout fields are independent of each other. Note that the running_timeout field shuts down VMs after the specified time, regardless of whether or not the VMs are idle.

Provide duration terminated by `s` for seconds—for example, `"54000s"` (15 hours). Defaults to `"43200s"` (12 hours). A value of `"0s"` indicates that workstations using this configuration should never time out. If encryption_key is set, it must be greater than `"0s"` and less than `"86400s"` (24 hours).

Warning: A value of `"0s"` indicates that Cloud Workstations VMs created with this configuration have no maximum running time. This is strongly discouraged because you incur costs and will not pick up security updates.

` .google.protobuf.Duration running_timeout = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### mergeUpdateTime(Timestamp value)
    
    
    public WorkstationConfig.Builder mergeUpdateTime(Timestamp value)

Output only. Time when this workstation configuration was most recently updated.

` .google.protobuf.Timestamp update_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### putAllAnnotations(Map<String,String> values)
    
    
    public WorkstationConfig.Builder putAllAnnotations(Map<String,String> values)

Optional. Client-specified annotations.

`map<string, string> annotations = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### putAllLabels(Map<String,String> values)
    
    
    public WorkstationConfig.Builder putAllLabels(Map<String,String> values)

Optional. [Labels](https://cloud.google.com/workstations/docs/label-resources) that are applied to the workstation configuration and that are also propagated to the underlying Compute Engine resources.

`map<string, string> labels = 18 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### putAnnotations(String key, String value)
    
    
    public WorkstationConfig.Builder putAnnotations(String key, String value)

Optional. Client-specified annotations.

`map<string, string> annotations = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### putLabels(String key, String value)
    
    
    public WorkstationConfig.Builder putLabels(String key, String value)

Optional. [Labels](https://cloud.google.com/workstations/docs/label-resources) that are applied to the workstation configuration and that are also propagated to the underlying Compute Engine resources.

`map<string, string> labels = 18 [(.google.api.field_behavior) = OPTIONAL];`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### removeAllowedPorts(int index)
    
    
    public WorkstationConfig.Builder removeAllowedPorts(int index)

Optional. A list of PortRanges specifying single ports or ranges of ports that are externally accessible in the workstation. Allowed ports must be one of 22, 80, or within range 1024-65535. If not specified defaults to ports 22, 80, and ports 1024-65535.

` repeated .google.cloud.workstations.v1.WorkstationConfig.PortRange allowed_ports = 25 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### removeAnnotations(String key)
    
    
    public WorkstationConfig.Builder removeAnnotations(String key)

Optional. Client-specified annotations.

`map<string, string> annotations = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### removeConditions(int index)
    
    
    public WorkstationConfig.Builder removeConditions(int index)

Output only. Status conditions describing the workstation configuration's current state.

` repeated .google.rpc.Status conditions = 16 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### removeEphemeralDirectories(int index)
    
    
    public WorkstationConfig.Builder removeEphemeralDirectories(int index)

Optional. Ephemeral directories which won't persist across workstation sessions.

` repeated .google.cloud.workstations.v1.WorkstationConfig.EphemeralDirectory ephemeral_directories = 22 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### removeLabels(String key)
    
    
    public WorkstationConfig.Builder removeLabels(String key)

Optional. [Labels](https://cloud.google.com/workstations/docs/label-resources) that are applied to the workstation configuration and that are also propagated to the underlying Compute Engine resources.

`map<string, string> labels = 18 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### removePersistentDirectories(int index)
    
    
    public WorkstationConfig.Builder removePersistentDirectories(int index)

Optional. Directories to persist across workstation sessions.

` repeated .google.cloud.workstations.v1.WorkstationConfig.PersistentDirectory persistent_directories = 13 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### removeReadinessChecks(int index)
    
    
    public WorkstationConfig.Builder removeReadinessChecks(int index)

Optional. Readiness checks to perform when starting a workstation using this workstation configuration. Mark a workstation as running only after all specified readiness checks return 200 status codes.

` repeated .google.cloud.workstations.v1.WorkstationConfig.ReadinessCheck readiness_checks = 19 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### setAllowedPorts(int index, WorkstationConfig.PortRange value)
    
    
    public WorkstationConfig.Builder setAllowedPorts(int index, WorkstationConfig.PortRange value)

Optional. A list of PortRanges specifying single ports or ranges of ports that are externally accessible in the workstation. Allowed ports must be one of 22, 80, or within range 1024-65535. If not specified defaults to ports 22, 80, and ports 1024-65535.

` repeated .google.cloud.workstations.v1.WorkstationConfig.PortRange allowed_ports = 25 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[WorkstationConfig.PortRange](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.PortRange)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### setAllowedPorts(int index, WorkstationConfig.PortRange.Builder builderForValue)
    
    
    public WorkstationConfig.Builder setAllowedPorts(int index, WorkstationConfig.PortRange.Builder builderForValue)

Optional. A list of PortRanges specifying single ports or ranges of ports that are externally accessible in the workstation. Allowed ports must be one of 22, 80, or within range 1024-65535. If not specified defaults to ports 22, 80, and ports 1024-65535.

` repeated .google.cloud.workstations.v1.WorkstationConfig.PortRange allowed_ports = 25 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[WorkstationConfig.PortRange.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.PortRange.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### setConditions(int index, Status value)
    
    
    public WorkstationConfig.Builder setConditions(int index, Status value)

Output only. Status conditions describing the workstation configuration's current state.

` repeated .google.rpc.Status conditions = 16 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `com.google.rpc.Status`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### setConditions(int index, Status.Builder builderForValue)
    
    
    public WorkstationConfig.Builder setConditions(int index, Status.Builder builderForValue)

Output only. Status conditions describing the workstation configuration's current state.

` repeated .google.rpc.Status conditions = 16 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `com.google.rpc.Status.Builder`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### setContainer(WorkstationConfig.Container value)
    
    
    public WorkstationConfig.Builder setContainer(WorkstationConfig.Container value)

Optional. Container that runs upon startup for each workstation using this workstation configuration.

` .google.cloud.workstations.v1.WorkstationConfig.Container container = 14 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[WorkstationConfig.Container](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Container)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### setContainer(WorkstationConfig.Container.Builder builderForValue)
    
    
    public WorkstationConfig.Builder setContainer(WorkstationConfig.Container.Builder builderForValue)

Optional. Container that runs upon startup for each workstation using this workstation configuration.

` .google.cloud.workstations.v1.WorkstationConfig.Container container = 14 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[WorkstationConfig.Container.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Container.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### setCreateTime(Timestamp value)
    
    
    public WorkstationConfig.Builder setCreateTime(Timestamp value)

Output only. Time when this workstation configuration was created.

` .google.protobuf.Timestamp create_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### setCreateTime(Timestamp.Builder builderForValue)
    
    
    public WorkstationConfig.Builder setCreateTime(Timestamp.Builder builderForValue)

Output only. Time when this workstation configuration was created.

` .google.protobuf.Timestamp create_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### setDegraded(boolean value)
    
    
    public WorkstationConfig.Builder setDegraded(boolean value)

Output only. Whether this workstation configuration is in degraded mode, in which case it may require user action to restore full functionality. The conditions field contains detailed information about the status of the configuration.

`bool degraded = 15 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The degraded to set.  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` | This builder for chaining.  
  
### setDeleteTime(Timestamp value)
    
    
    public WorkstationConfig.Builder setDeleteTime(Timestamp value)

Output only. Time when this workstation configuration was soft-deleted.

` .google.protobuf.Timestamp delete_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### setDeleteTime(Timestamp.Builder builderForValue)
    
    
    public WorkstationConfig.Builder setDeleteTime(Timestamp.Builder builderForValue)

Output only. Time when this workstation configuration was soft-deleted.

` .google.protobuf.Timestamp delete_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### setDisableTcpConnections(boolean value)
    
    
    public WorkstationConfig.Builder setDisableTcpConnections(boolean value)

Optional. Disables support for plain TCP connections in the workstation. By default the service supports TCP connections through a websocket relay. Setting this option to true disables that relay, which prevents the usage of services that require plain TCP connections, such as SSH. When enabled, all communication must occur over HTTPS or WSS.

`bool disable_tcp_connections = 24 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The disableTcpConnections to set.  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` | This builder for chaining.  
  
### setDisplayName(String value)
    
    
    public WorkstationConfig.Builder setDisplayName(String value)

Optional. Human-readable name for this workstation configuration.

`string display_name = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The displayName to set.  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` | This builder for chaining.  
  
### setDisplayNameBytes(ByteString value)
    
    
    public WorkstationConfig.Builder setDisplayNameBytes(ByteString value)

Optional. Human-readable name for this workstation configuration.

`string display_name = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for displayName to set.  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` | This builder for chaining.  
  
### setEnableAuditAgent(boolean value)
    
    
    public WorkstationConfig.Builder setEnableAuditAgent(boolean value)

Optional. Whether to enable Linux `auditd` logging on the workstation. When enabled, a service_account must also be specified that has `roles/logging.logWriter` and `roles/monitoring.metricWriter` on the project. Operating system audit logging is distinct from [Cloud Audit Logs](https://cloud.google.com/workstations/docs/audit-logging) and [Container output logging](https://cloud.google.com/workstations/docs/container-output-logging#overview). Operating system audit logs are available in the [Cloud Logging](https://cloud.google.com/logging/docs) console by querying:

resource.type="gce_instance" log_name:"/logs/linux-auditd"

`bool enable_audit_agent = 20 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The enableAuditAgent to set.  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` | This builder for chaining.  
  
### setEncryptionKey(WorkstationConfig.CustomerEncryptionKey value)
    
    
    public WorkstationConfig.Builder setEncryptionKey(WorkstationConfig.CustomerEncryptionKey value)

Immutable. Encrypts resources of this workstation configuration using a customer-managed encryption key (CMEK).

If specified, the boot disk of the Compute Engine instance and the persistent disk are encrypted using this encryption key. If this field is not set, the disks are encrypted using a generated key. Customer-managed encryption keys do not protect disk metadata.

If the customer-managed encryption key is rotated, when the workstation instance is stopped, the system attempts to recreate the persistent disk with the new version of the key. Be sure to keep older versions of the key until the persistent disk is recreated. Otherwise, data on the persistent disk might be lost.

If the encryption key is revoked, the workstation session automatically stops within 7 hours.

Immutable after the workstation configuration is created.

` .google.cloud.workstations.v1.WorkstationConfig.CustomerEncryptionKey encryption_key = 17 [(.google.api.field_behavior) = IMMUTABLE]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[WorkstationConfig.CustomerEncryptionKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.CustomerEncryptionKey)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### setEncryptionKey(WorkstationConfig.CustomerEncryptionKey.Builder builderForValue)
    
    
    public WorkstationConfig.Builder setEncryptionKey(WorkstationConfig.CustomerEncryptionKey.Builder builderForValue)

Immutable. Encrypts resources of this workstation configuration using a customer-managed encryption key (CMEK).

If specified, the boot disk of the Compute Engine instance and the persistent disk are encrypted using this encryption key. If this field is not set, the disks are encrypted using a generated key. Customer-managed encryption keys do not protect disk metadata.

If the customer-managed encryption key is rotated, when the workstation instance is stopped, the system attempts to recreate the persistent disk with the new version of the key. Be sure to keep older versions of the key until the persistent disk is recreated. Otherwise, data on the persistent disk might be lost.

If the encryption key is revoked, the workstation session automatically stops within 7 hours.

Immutable after the workstation configuration is created.

` .google.cloud.workstations.v1.WorkstationConfig.CustomerEncryptionKey encryption_key = 17 [(.google.api.field_behavior) = IMMUTABLE]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[WorkstationConfig.CustomerEncryptionKey.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.CustomerEncryptionKey.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### setEphemeralDirectories(int index, WorkstationConfig.EphemeralDirectory value)
    
    
    public WorkstationConfig.Builder setEphemeralDirectories(int index, WorkstationConfig.EphemeralDirectory value)

Optional. Ephemeral directories which won't persist across workstation sessions.

` repeated .google.cloud.workstations.v1.WorkstationConfig.EphemeralDirectory ephemeral_directories = 22 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[WorkstationConfig.EphemeralDirectory](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.EphemeralDirectory)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### setEphemeralDirectories(int index, WorkstationConfig.EphemeralDirectory.Builder builderForValue)
    
    
    public WorkstationConfig.Builder setEphemeralDirectories(int index, WorkstationConfig.EphemeralDirectory.Builder builderForValue)

Optional. Ephemeral directories which won't persist across workstation sessions.

` repeated .google.cloud.workstations.v1.WorkstationConfig.EphemeralDirectory ephemeral_directories = 22 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[WorkstationConfig.EphemeralDirectory.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.EphemeralDirectory.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### setEtag(String value)
    
    
    public WorkstationConfig.Builder setEtag(String value)

Optional. Checksum computed by the server. May be sent on update and delete requests to make sure that the client has an up-to-date value before proceeding.

`string etag = 9 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The etag to set.  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` | This builder for chaining.  
  
### setEtagBytes(ByteString value)
    
    
    public WorkstationConfig.Builder setEtagBytes(ByteString value)

Optional. Checksum computed by the server. May be sent on update and delete requests to make sure that the client has an up-to-date value before proceeding.

`string etag = 9 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for etag to set.  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` | This builder for chaining.  
  
### setGrantWorkstationAdminRoleOnCreate(boolean value)
    
    
    public WorkstationConfig.Builder setGrantWorkstationAdminRoleOnCreate(boolean value)

Optional. Grant creator of a workstation `roles/workstations.policyAdmin` role along with `roles/workstations.user` role on the workstation created by them. This allows workstation users to share access to either their entire workstation, or individual ports. Defaults to false.

` bool grant_workstation_admin_role_on_create = 29 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The grantWorkstationAdminRoleOnCreate to set.  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` | This builder for chaining.  
  
### setHost(WorkstationConfig.Host value)
    
    
    public WorkstationConfig.Builder setHost(WorkstationConfig.Host value)

Optional. Runtime host for the workstation.

` .google.cloud.workstations.v1.WorkstationConfig.Host host = 12 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[WorkstationConfig.Host](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Host)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### setHost(WorkstationConfig.Host.Builder builderForValue)
    
    
    public WorkstationConfig.Builder setHost(WorkstationConfig.Host.Builder builderForValue)

Optional. Runtime host for the workstation.

` .google.cloud.workstations.v1.WorkstationConfig.Host host = 12 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[WorkstationConfig.Host.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Host.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### setIdleTimeout(Duration value)
    
    
    public WorkstationConfig.Builder setIdleTimeout(Duration value)

Optional. Number of seconds to wait before automatically stopping a workstation after it last received user traffic.

A value of `"0s"` indicates that Cloud Workstations VMs created with this configuration should never time out due to idleness. Provide [duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#duration) terminated by `s` for seconds—for example, `"7200s"` (2 hours). The default is `"1200s"` (20 minutes).

`.google.protobuf.Duration idle_timeout = 10 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### setIdleTimeout(Duration.Builder builderForValue)
    
    
    public WorkstationConfig.Builder setIdleTimeout(Duration.Builder builderForValue)

Optional. Number of seconds to wait before automatically stopping a workstation after it last received user traffic.

A value of `"0s"` indicates that Cloud Workstations VMs created with this configuration should never time out due to idleness. Provide [duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#duration) terminated by `s` for seconds—for example, `"7200s"` (2 hours). The default is `"1200s"` (20 minutes).

`.google.protobuf.Duration idle_timeout = 10 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### setMaxUsableWorkstations(int value)
    
    
    public WorkstationConfig.Builder setMaxUsableWorkstations(int value)

Optional. Maximum number of workstations under this configuration a user can have `workstations.workstation.use` permission on.

Only enforced on CreateWorkstation API calls on the user issuing the API request. Can be overridden by:

  * granting a user workstations.workstationConfigs.exemptMaxUsableWorkstationLimit permission, or
  * having a user with that permission create a workstation and granting another user `workstations.workstation.use` permission on that workstation.

If not specified, defaults to `0`, which indicates unlimited.




`int32 max_usable_workstations = 28 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The maxUsableWorkstations to set.  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` | This builder for chaining.  
  
### setName(String value)
    
    
    public WorkstationConfig.Builder setName(String value)

Identifier. Full name of this workstation configuration.

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name to set.  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` | This builder for chaining.  
  
### setNameBytes(ByteString value)
    
    
    public WorkstationConfig.Builder setNameBytes(ByteString value)

Identifier. Full name of this workstation configuration.

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for name to set.  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` | This builder for chaining.  
  
### setPersistentDirectories(int index, WorkstationConfig.PersistentDirectory value)
    
    
    public WorkstationConfig.Builder setPersistentDirectories(int index, WorkstationConfig.PersistentDirectory value)

Optional. Directories to persist across workstation sessions.

` repeated .google.cloud.workstations.v1.WorkstationConfig.PersistentDirectory persistent_directories = 13 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[WorkstationConfig.PersistentDirectory](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.PersistentDirectory)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### setPersistentDirectories(int index, WorkstationConfig.PersistentDirectory.Builder builderForValue)
    
    
    public WorkstationConfig.Builder setPersistentDirectories(int index, WorkstationConfig.PersistentDirectory.Builder builderForValue)

Optional. Directories to persist across workstation sessions.

` repeated .google.cloud.workstations.v1.WorkstationConfig.PersistentDirectory persistent_directories = 13 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[WorkstationConfig.PersistentDirectory.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.PersistentDirectory.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### setReadinessChecks(int index, WorkstationConfig.ReadinessCheck value)
    
    
    public WorkstationConfig.Builder setReadinessChecks(int index, WorkstationConfig.ReadinessCheck value)

Optional. Readiness checks to perform when starting a workstation using this workstation configuration. Mark a workstation as running only after all specified readiness checks return 200 status codes.

` repeated .google.cloud.workstations.v1.WorkstationConfig.ReadinessCheck readiness_checks = 19 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[WorkstationConfig.ReadinessCheck](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.ReadinessCheck)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### setReadinessChecks(int index, WorkstationConfig.ReadinessCheck.Builder builderForValue)
    
    
    public WorkstationConfig.Builder setReadinessChecks(int index, WorkstationConfig.ReadinessCheck.Builder builderForValue)

Optional. Readiness checks to perform when starting a workstation using this workstation configuration. Mark a workstation as running only after all specified readiness checks return 200 status codes.

` repeated .google.cloud.workstations.v1.WorkstationConfig.ReadinessCheck readiness_checks = 19 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[WorkstationConfig.ReadinessCheck.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.ReadinessCheck.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### setReconciling(boolean value)
    
    
    public WorkstationConfig.Builder setReconciling(boolean value)

Output only. Indicates whether this workstation configuration is currently being updated to match its intended state.

`bool reconciling = 4 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The reconciling to set.  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` | This builder for chaining.  
  
### setReplicaZones(int index, String value)
    
    
    public WorkstationConfig.Builder setReplicaZones(int index, String value)

Optional. Immutable. Specifies the zones used to replicate the VM and disk resources within the region. If set, exactly two zones within the workstation cluster's region must be specified—for example, `['us-central1-a', 'us-central1-f']`. If this field is empty, two default zones within the region are used.

Immutable after the workstation configuration is created.

` repeated string replica_zones = 23 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = IMMUTABLE]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index to set the value at.  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The replicaZones to set.  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` | This builder for chaining.  
  
### setRunningTimeout(Duration value)
    
    
    public WorkstationConfig.Builder setRunningTimeout(Duration value)

Optional. Number of seconds that a workstation can run until it is automatically shut down. We recommend that workstations be shut down daily to reduce costs and so that security updates can be applied upon restart. The idle_timeout and running_timeout fields are independent of each other. Note that the running_timeout field shuts down VMs after the specified time, regardless of whether or not the VMs are idle.

Provide duration terminated by `s` for seconds—for example, `"54000s"` (15 hours). Defaults to `"43200s"` (12 hours). A value of `"0s"` indicates that workstations using this configuration should never time out. If encryption_key is set, it must be greater than `"0s"` and less than `"86400s"` (24 hours).

Warning: A value of `"0s"` indicates that Cloud Workstations VMs created with this configuration have no maximum running time. This is strongly discouraged because you incur costs and will not pick up security updates.

` .google.protobuf.Duration running_timeout = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### setRunningTimeout(Duration.Builder builderForValue)
    
    
    public WorkstationConfig.Builder setRunningTimeout(Duration.Builder builderForValue)

Optional. Number of seconds that a workstation can run until it is automatically shut down. We recommend that workstations be shut down daily to reduce costs and so that security updates can be applied upon restart. The idle_timeout and running_timeout fields are independent of each other. Note that the running_timeout field shuts down VMs after the specified time, regardless of whether or not the VMs are idle.

Provide duration terminated by `s` for seconds—for example, `"54000s"` (15 hours). Defaults to `"43200s"` (12 hours). A value of `"0s"` indicates that workstations using this configuration should never time out. If encryption_key is set, it must be greater than `"0s"` and less than `"86400s"` (24 hours).

Warning: A value of `"0s"` indicates that Cloud Workstations VMs created with this configuration have no maximum running time. This is strongly discouraged because you incur costs and will not pick up security updates.

` .google.protobuf.Duration running_timeout = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### setUid(String value)
    
    
    public WorkstationConfig.Builder setUid(String value)

Output only. A system-assigned unique identifier for this workstation configuration.

` string uid = 3 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.field_info) = { ... } `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The uid to set.  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` | This builder for chaining.  
  
### setUidBytes(ByteString value)
    
    
    public WorkstationConfig.Builder setUidBytes(ByteString value)

Output only. A system-assigned unique identifier for this workstation configuration.

` string uid = 3 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.field_info) = { ... } `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for uid to set.  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` | This builder for chaining.  
  
### setUpdateTime(Timestamp value)
    
    
    public WorkstationConfig.Builder setUpdateTime(Timestamp value)

Output only. Time when this workstation configuration was most recently updated.

` .google.protobuf.Timestamp update_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
### setUpdateTime(Timestamp.Builder builderForValue)
    
    
    public WorkstationConfig.Builder setUpdateTime(Timestamp.Builder builderForValue)

Output only. Time when this workstation configuration was most recently updated.

` .google.protobuf.Timestamp update_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig.Builder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
