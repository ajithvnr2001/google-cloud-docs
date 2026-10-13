---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.Builder
title: Class ChangeStreamRecord.PartitionEventRecord.Builder (6.124.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:38:05.621741+00:00
---

# Class ChangeStreamRecord.PartitionEventRecord.Builder (6.124.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ChangeStreamRecord.PartitionEventRecord.Builder (6.124.0) Stay organized with collections  Save and categorize content based on your preferences. 

6.124.0 (latest)  6.120.0  6.119.0  6.118.0  6.116.0  6.111.1  6.108.0  6.107.0  6.103.0  6.102.1  6.101.1  6.100.0  6.99.0  6.98.1  6.97.1  6.96.1  6.95.1  6.94.0  6.93.0  6.89.0  6.88.0  6.87.0  6.86.0  6.85.0  6.83.0  6.82.0  6.80.1  6.79.0  6.77.0  6.74.1  6.72.0  6.71.0  6.69.0  6.68.0  6.66.0  6.65.1  6.62.0  6.60.0  6.58.0  6.57.0  6.56.0  6.55.0  6.54.0  6.53.0  6.52.1  6.51.0  6.50.1  6.49.0  6.25.1  6.24.0  6.23.4  6.22.0  6.21.2  6.20.0  6.19.1  6.18.0  6.17.4  6.14.1 
    
    
    public static final class ChangeStreamRecord.PartitionEventRecord.Builder extends GeneratedMessage.Builder<ChangeStreamRecord.PartitionEventRecord.Builder> implements ChangeStreamRecord.PartitionEventRecordOrBuilder

A partition event record describes key range changes for a change stream partition. The changes to a row defined by its primary key can be captured in one change stream partition for a specific time range, and then be captured in a different change stream partition for a different time range. This movement of key ranges across change stream partitions is a reflection of activities, such as Spanner's dynamic splitting and load balancing, etc. Processing this event is needed if users want to guarantee processing of the changes for any key in timestamp order. If time ordered processing of changes for a primary key is not needed, this event can be ignored. To guarantee time ordered processing for each primary key, if the event describes move-ins, the reader of this partition needs to wait until the readers of the source partitions have processed all records with timestamps <= this PartitionEventRecord.commit_timestamp, before advancing beyond this PartitionEventRecord. If the event describes move-outs, the reader can notify the readers of the destination partitions that they can continue processing.

Protobuf type `google.spanner.v1.ChangeStreamRecord.PartitionEventRecord`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > ChangeStreamRecord.PartitionEventRecord.Builder

## Implements

[ChangeStreamRecord.PartitionEventRecordOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecordOrBuilder)

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

### addAllMoveInEvents(Iterable<? extends ChangeStreamRecord.PartitionEventRecord.MoveInEvent> values)
    
    
    public ChangeStreamRecord.PartitionEventRecord.Builder addAllMoveInEvents(Iterable<? extends ChangeStreamRecord.PartitionEventRecord.MoveInEvent> values)

Set when one or more key ranges are moved into the change stream partition identified by partition_token.

Example: Two key ranges are moved into partition (P1) from partition (P2) and partition (P3) in a single transaction at timestamp T.

The PartitionEventRecord returned in P1 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P1" move_in_events { source_partition_token: "P2" } move_in_events { source_partition_token: "P3" } }

The PartitionEventRecord returned in P2 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P2" move_out_events { destination_partition_token: "P1" } }

The PartitionEventRecord returned in P3 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P3" move_out_events { destination_partition_token: "P1" } }

` repeated .google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveInEvent move_in_events = 4; `

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<? extends com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveInEvent>`  
  
**Returns**  
---  
**Type** | **Description**  
`[ChangeStreamRecord.PartitionEventRecord.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.Builder)` |   
  
### addAllMoveOutEvents(Iterable<? extends ChangeStreamRecord.PartitionEventRecord.MoveOutEvent> values)
    
    
    public ChangeStreamRecord.PartitionEventRecord.Builder addAllMoveOutEvents(Iterable<? extends ChangeStreamRecord.PartitionEventRecord.MoveOutEvent> values)

Set when one or more key ranges are moved out of the change stream partition identified by partition_token.

Example: Two key ranges are moved out of partition (P1) to partition (P2) and partition (P3) in a single transaction at timestamp T.

The PartitionEventRecord returned in P1 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P1" move_out_events { destination_partition_token: "P2" } move_out_events { destination_partition_token: "P3" } }

The PartitionEventRecord returned in P2 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P2" move_in_events { source_partition_token: "P1" } }

The PartitionEventRecord returned in P3 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P3" move_in_events { source_partition_token: "P1" } }

` repeated .google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveOutEvent move_out_events = 5; `

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<? extends com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveOutEvent>`  
  
**Returns**  
---  
**Type** | **Description**  
`[ChangeStreamRecord.PartitionEventRecord.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.Builder)` |   
  
### addMoveInEvents(ChangeStreamRecord.PartitionEventRecord.MoveInEvent value)
    
    
    public ChangeStreamRecord.PartitionEventRecord.Builder addMoveInEvents(ChangeStreamRecord.PartitionEventRecord.MoveInEvent value)

Set when one or more key ranges are moved into the change stream partition identified by partition_token.

Example: Two key ranges are moved into partition (P1) from partition (P2) and partition (P3) in a single transaction at timestamp T.

The PartitionEventRecord returned in P1 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P1" move_in_events { source_partition_token: "P2" } move_in_events { source_partition_token: "P3" } }

The PartitionEventRecord returned in P2 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P2" move_out_events { destination_partition_token: "P1" } }

The PartitionEventRecord returned in P3 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P3" move_out_events { destination_partition_token: "P1" } }

` repeated .google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveInEvent move_in_events = 4; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ChangeStreamRecord.PartitionEventRecord.MoveInEvent](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveInEvent)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ChangeStreamRecord.PartitionEventRecord.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.Builder)` |   
  
### addMoveInEvents(ChangeStreamRecord.PartitionEventRecord.MoveInEvent.Builder builderForValue)
    
    
    public ChangeStreamRecord.PartitionEventRecord.Builder addMoveInEvents(ChangeStreamRecord.PartitionEventRecord.MoveInEvent.Builder builderForValue)

Set when one or more key ranges are moved into the change stream partition identified by partition_token.

Example: Two key ranges are moved into partition (P1) from partition (P2) and partition (P3) in a single transaction at timestamp T.

The PartitionEventRecord returned in P1 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P1" move_in_events { source_partition_token: "P2" } move_in_events { source_partition_token: "P3" } }

The PartitionEventRecord returned in P2 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P2" move_out_events { destination_partition_token: "P1" } }

The PartitionEventRecord returned in P3 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P3" move_out_events { destination_partition_token: "P1" } }

` repeated .google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveInEvent move_in_events = 4; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[ChangeStreamRecord.PartitionEventRecord.MoveInEvent.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveInEvent.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ChangeStreamRecord.PartitionEventRecord.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.Builder)` |   
  
### addMoveInEvents(int index, ChangeStreamRecord.PartitionEventRecord.MoveInEvent value)
    
    
    public ChangeStreamRecord.PartitionEventRecord.Builder addMoveInEvents(int index, ChangeStreamRecord.PartitionEventRecord.MoveInEvent value)

Set when one or more key ranges are moved into the change stream partition identified by partition_token.

Example: Two key ranges are moved into partition (P1) from partition (P2) and partition (P3) in a single transaction at timestamp T.

The PartitionEventRecord returned in P1 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P1" move_in_events { source_partition_token: "P2" } move_in_events { source_partition_token: "P3" } }

The PartitionEventRecord returned in P2 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P2" move_out_events { destination_partition_token: "P1" } }

The PartitionEventRecord returned in P3 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P3" move_out_events { destination_partition_token: "P1" } }

` repeated .google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveInEvent move_in_events = 4; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[ChangeStreamRecord.PartitionEventRecord.MoveInEvent](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveInEvent)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ChangeStreamRecord.PartitionEventRecord.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.Builder)` |   
  
### addMoveInEvents(int index, ChangeStreamRecord.PartitionEventRecord.MoveInEvent.Builder builderForValue)
    
    
    public ChangeStreamRecord.PartitionEventRecord.Builder addMoveInEvents(int index, ChangeStreamRecord.PartitionEventRecord.MoveInEvent.Builder builderForValue)

Set when one or more key ranges are moved into the change stream partition identified by partition_token.

Example: Two key ranges are moved into partition (P1) from partition (P2) and partition (P3) in a single transaction at timestamp T.

The PartitionEventRecord returned in P1 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P1" move_in_events { source_partition_token: "P2" } move_in_events { source_partition_token: "P3" } }

The PartitionEventRecord returned in P2 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P2" move_out_events { destination_partition_token: "P1" } }

The PartitionEventRecord returned in P3 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P3" move_out_events { destination_partition_token: "P1" } }

` repeated .google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveInEvent move_in_events = 4; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[ChangeStreamRecord.PartitionEventRecord.MoveInEvent.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveInEvent.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ChangeStreamRecord.PartitionEventRecord.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.Builder)` |   
  
### addMoveInEventsBuilder()
    
    
    public ChangeStreamRecord.PartitionEventRecord.MoveInEvent.Builder addMoveInEventsBuilder()

Set when one or more key ranges are moved into the change stream partition identified by partition_token.

Example: Two key ranges are moved into partition (P1) from partition (P2) and partition (P3) in a single transaction at timestamp T.

The PartitionEventRecord returned in P1 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P1" move_in_events { source_partition_token: "P2" } move_in_events { source_partition_token: "P3" } }

The PartitionEventRecord returned in P2 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P2" move_out_events { destination_partition_token: "P1" } }

The PartitionEventRecord returned in P3 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P3" move_out_events { destination_partition_token: "P1" } }

` repeated .google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveInEvent move_in_events = 4; `

**Returns**  
---  
**Type** | **Description**  
`[ChangeStreamRecord.PartitionEventRecord.MoveInEvent.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveInEvent.Builder)` |   
  
### addMoveInEventsBuilder(int index)
    
    
    public ChangeStreamRecord.PartitionEventRecord.MoveInEvent.Builder addMoveInEventsBuilder(int index)

Set when one or more key ranges are moved into the change stream partition identified by partition_token.

Example: Two key ranges are moved into partition (P1) from partition (P2) and partition (P3) in a single transaction at timestamp T.

The PartitionEventRecord returned in P1 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P1" move_in_events { source_partition_token: "P2" } move_in_events { source_partition_token: "P3" } }

The PartitionEventRecord returned in P2 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P2" move_out_events { destination_partition_token: "P1" } }

The PartitionEventRecord returned in P3 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P3" move_out_events { destination_partition_token: "P1" } }

` repeated .google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveInEvent move_in_events = 4; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ChangeStreamRecord.PartitionEventRecord.MoveInEvent.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveInEvent.Builder)` |   
  
### addMoveOutEvents(ChangeStreamRecord.PartitionEventRecord.MoveOutEvent value)
    
    
    public ChangeStreamRecord.PartitionEventRecord.Builder addMoveOutEvents(ChangeStreamRecord.PartitionEventRecord.MoveOutEvent value)

Set when one or more key ranges are moved out of the change stream partition identified by partition_token.

Example: Two key ranges are moved out of partition (P1) to partition (P2) and partition (P3) in a single transaction at timestamp T.

The PartitionEventRecord returned in P1 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P1" move_out_events { destination_partition_token: "P2" } move_out_events { destination_partition_token: "P3" } }

The PartitionEventRecord returned in P2 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P2" move_in_events { source_partition_token: "P1" } }

The PartitionEventRecord returned in P3 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P3" move_in_events { source_partition_token: "P1" } }

` repeated .google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveOutEvent move_out_events = 5; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ChangeStreamRecord.PartitionEventRecord.MoveOutEvent](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveOutEvent)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ChangeStreamRecord.PartitionEventRecord.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.Builder)` |   
  
### addMoveOutEvents(ChangeStreamRecord.PartitionEventRecord.MoveOutEvent.Builder builderForValue)
    
    
    public ChangeStreamRecord.PartitionEventRecord.Builder addMoveOutEvents(ChangeStreamRecord.PartitionEventRecord.MoveOutEvent.Builder builderForValue)

Set when one or more key ranges are moved out of the change stream partition identified by partition_token.

Example: Two key ranges are moved out of partition (P1) to partition (P2) and partition (P3) in a single transaction at timestamp T.

The PartitionEventRecord returned in P1 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P1" move_out_events { destination_partition_token: "P2" } move_out_events { destination_partition_token: "P3" } }

The PartitionEventRecord returned in P2 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P2" move_in_events { source_partition_token: "P1" } }

The PartitionEventRecord returned in P3 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P3" move_in_events { source_partition_token: "P1" } }

` repeated .google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveOutEvent move_out_events = 5; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[ChangeStreamRecord.PartitionEventRecord.MoveOutEvent.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveOutEvent.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ChangeStreamRecord.PartitionEventRecord.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.Builder)` |   
  
### addMoveOutEvents(int index, ChangeStreamRecord.PartitionEventRecord.MoveOutEvent value)
    
    
    public ChangeStreamRecord.PartitionEventRecord.Builder addMoveOutEvents(int index, ChangeStreamRecord.PartitionEventRecord.MoveOutEvent value)

Set when one or more key ranges are moved out of the change stream partition identified by partition_token.

Example: Two key ranges are moved out of partition (P1) to partition (P2) and partition (P3) in a single transaction at timestamp T.

The PartitionEventRecord returned in P1 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P1" move_out_events { destination_partition_token: "P2" } move_out_events { destination_partition_token: "P3" } }

The PartitionEventRecord returned in P2 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P2" move_in_events { source_partition_token: "P1" } }

The PartitionEventRecord returned in P3 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P3" move_in_events { source_partition_token: "P1" } }

` repeated .google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveOutEvent move_out_events = 5; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[ChangeStreamRecord.PartitionEventRecord.MoveOutEvent](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveOutEvent)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ChangeStreamRecord.PartitionEventRecord.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.Builder)` |   
  
### addMoveOutEvents(int index, ChangeStreamRecord.PartitionEventRecord.MoveOutEvent.Builder builderForValue)
    
    
    public ChangeStreamRecord.PartitionEventRecord.Builder addMoveOutEvents(int index, ChangeStreamRecord.PartitionEventRecord.MoveOutEvent.Builder builderForValue)

Set when one or more key ranges are moved out of the change stream partition identified by partition_token.

Example: Two key ranges are moved out of partition (P1) to partition (P2) and partition (P3) in a single transaction at timestamp T.

The PartitionEventRecord returned in P1 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P1" move_out_events { destination_partition_token: "P2" } move_out_events { destination_partition_token: "P3" } }

The PartitionEventRecord returned in P2 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P2" move_in_events { source_partition_token: "P1" } }

The PartitionEventRecord returned in P3 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P3" move_in_events { source_partition_token: "P1" } }

` repeated .google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveOutEvent move_out_events = 5; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[ChangeStreamRecord.PartitionEventRecord.MoveOutEvent.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveOutEvent.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ChangeStreamRecord.PartitionEventRecord.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.Builder)` |   
  
### addMoveOutEventsBuilder()
    
    
    public ChangeStreamRecord.PartitionEventRecord.MoveOutEvent.Builder addMoveOutEventsBuilder()

Set when one or more key ranges are moved out of the change stream partition identified by partition_token.

Example: Two key ranges are moved out of partition (P1) to partition (P2) and partition (P3) in a single transaction at timestamp T.

The PartitionEventRecord returned in P1 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P1" move_out_events { destination_partition_token: "P2" } move_out_events { destination_partition_token: "P3" } }

The PartitionEventRecord returned in P2 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P2" move_in_events { source_partition_token: "P1" } }

The PartitionEventRecord returned in P3 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P3" move_in_events { source_partition_token: "P1" } }

` repeated .google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveOutEvent move_out_events = 5; `

**Returns**  
---  
**Type** | **Description**  
`[ChangeStreamRecord.PartitionEventRecord.MoveOutEvent.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveOutEvent.Builder)` |   
  
### addMoveOutEventsBuilder(int index)
    
    
    public ChangeStreamRecord.PartitionEventRecord.MoveOutEvent.Builder addMoveOutEventsBuilder(int index)

Set when one or more key ranges are moved out of the change stream partition identified by partition_token.

Example: Two key ranges are moved out of partition (P1) to partition (P2) and partition (P3) in a single transaction at timestamp T.

The PartitionEventRecord returned in P1 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P1" move_out_events { destination_partition_token: "P2" } move_out_events { destination_partition_token: "P3" } }

The PartitionEventRecord returned in P2 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P2" move_in_events { source_partition_token: "P1" } }

The PartitionEventRecord returned in P3 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P3" move_in_events { source_partition_token: "P1" } }

` repeated .google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveOutEvent move_out_events = 5; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ChangeStreamRecord.PartitionEventRecord.MoveOutEvent.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveOutEvent.Builder)` |   
  
### build()
    
    
    public ChangeStreamRecord.PartitionEventRecord build()

**Returns**  
---  
**Type** | **Description**  
`[ChangeStreamRecord.PartitionEventRecord](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord)` |   
  
### buildPartial()
    
    
    public ChangeStreamRecord.PartitionEventRecord buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[ChangeStreamRecord.PartitionEventRecord](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord)` |   
  
### clear()
    
    
    public ChangeStreamRecord.PartitionEventRecord.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[ChangeStreamRecord.PartitionEventRecord.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearCommitTimestamp()
    
    
    public ChangeStreamRecord.PartitionEventRecord.Builder clearCommitTimestamp()

Indicates the commit timestamp at which the key range change occurred. DataChangeRecord.commit_timestamps, PartitionStartRecord.start_timestamps, PartitionEventRecord.commit_timestamps, and PartitionEndRecord.end_timestamps can have the same value in the same partition.

`.google.protobuf.Timestamp commit_timestamp = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ChangeStreamRecord.PartitionEventRecord.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.Builder)` |   
  
### clearMoveInEvents()
    
    
    public ChangeStreamRecord.PartitionEventRecord.Builder clearMoveInEvents()

Set when one or more key ranges are moved into the change stream partition identified by partition_token.

Example: Two key ranges are moved into partition (P1) from partition (P2) and partition (P3) in a single transaction at timestamp T.

The PartitionEventRecord returned in P1 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P1" move_in_events { source_partition_token: "P2" } move_in_events { source_partition_token: "P3" } }

The PartitionEventRecord returned in P2 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P2" move_out_events { destination_partition_token: "P1" } }

The PartitionEventRecord returned in P3 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P3" move_out_events { destination_partition_token: "P1" } }

` repeated .google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveInEvent move_in_events = 4; `

**Returns**  
---  
**Type** | **Description**  
`[ChangeStreamRecord.PartitionEventRecord.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.Builder)` |   
  
### clearMoveOutEvents()
    
    
    public ChangeStreamRecord.PartitionEventRecord.Builder clearMoveOutEvents()

Set when one or more key ranges are moved out of the change stream partition identified by partition_token.

Example: Two key ranges are moved out of partition (P1) to partition (P2) and partition (P3) in a single transaction at timestamp T.

The PartitionEventRecord returned in P1 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P1" move_out_events { destination_partition_token: "P2" } move_out_events { destination_partition_token: "P3" } }

The PartitionEventRecord returned in P2 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P2" move_in_events { source_partition_token: "P1" } }

The PartitionEventRecord returned in P3 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P3" move_in_events { source_partition_token: "P1" } }

` repeated .google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveOutEvent move_out_events = 5; `

**Returns**  
---  
**Type** | **Description**  
`[ChangeStreamRecord.PartitionEventRecord.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.Builder)` |   
  
### clearPartitionToken()
    
    
    public ChangeStreamRecord.PartitionEventRecord.Builder clearPartitionToken()

Unique partition identifier describing the partition this event occurred on. partition_token is equal to the partition token of the change stream partition currently queried to return this PartitionEventRecord.

`string partition_token = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ChangeStreamRecord.PartitionEventRecord.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.Builder)` | This builder for chaining.  
  
### clearRecordSequence()
    
    
    public ChangeStreamRecord.PartitionEventRecord.Builder clearRecordSequence()

Record sequence numbers are unique and monotonically increasing (but not necessarily contiguous) for a specific timestamp across record types in the same partition. To guarantee ordered processing, the reader should process records (of potentially different types) in record_sequence order for a specific timestamp in the same partition.

`string record_sequence = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ChangeStreamRecord.PartitionEventRecord.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.Builder)` | This builder for chaining.  
  
### getCommitTimestamp()
    
    
    public Timestamp getCommitTimestamp()

Indicates the commit timestamp at which the key range change occurred. DataChangeRecord.commit_timestamps, PartitionStartRecord.start_timestamps, PartitionEventRecord.commit_timestamps, and PartitionEndRecord.end_timestamps can have the same value in the same partition.

`.google.protobuf.Timestamp commit_timestamp = 1;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The commitTimestamp.  
  
### getCommitTimestampBuilder()
    
    
    public Timestamp.Builder getCommitTimestampBuilder()

Indicates the commit timestamp at which the key range change occurred. DataChangeRecord.commit_timestamps, PartitionStartRecord.start_timestamps, PartitionEventRecord.commit_timestamps, and PartitionEndRecord.end_timestamps can have the same value in the same partition.

`.google.protobuf.Timestamp commit_timestamp = 1;`

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)` |   
  
### getCommitTimestampOrBuilder()
    
    
    public TimestampOrBuilder getCommitTimestampOrBuilder()

Indicates the commit timestamp at which the key range change occurred. DataChangeRecord.commit_timestamps, PartitionStartRecord.start_timestamps, PartitionEventRecord.commit_timestamps, and PartitionEndRecord.end_timestamps can have the same value in the same partition.

`.google.protobuf.Timestamp commit_timestamp = 1;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDefaultInstanceForType()
    
    
    public ChangeStreamRecord.PartitionEventRecord getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[ChangeStreamRecord.PartitionEventRecord](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord)` |   
  
### getDescriptorForType()
    
    
    public Descriptors.Descriptor getDescriptorForType()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getDescriptorForType__)

### getMoveInEvents(int index)
    
    
    public ChangeStreamRecord.PartitionEventRecord.MoveInEvent getMoveInEvents(int index)

Set when one or more key ranges are moved into the change stream partition identified by partition_token.

Example: Two key ranges are moved into partition (P1) from partition (P2) and partition (P3) in a single transaction at timestamp T.

The PartitionEventRecord returned in P1 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P1" move_in_events { source_partition_token: "P2" } move_in_events { source_partition_token: "P3" } }

The PartitionEventRecord returned in P2 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P2" move_out_events { destination_partition_token: "P1" } }

The PartitionEventRecord returned in P3 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P3" move_out_events { destination_partition_token: "P1" } }

` repeated .google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveInEvent move_in_events = 4; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ChangeStreamRecord.PartitionEventRecord.MoveInEvent](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveInEvent)` |   
  
### getMoveInEventsBuilder(int index)
    
    
    public ChangeStreamRecord.PartitionEventRecord.MoveInEvent.Builder getMoveInEventsBuilder(int index)

Set when one or more key ranges are moved into the change stream partition identified by partition_token.

Example: Two key ranges are moved into partition (P1) from partition (P2) and partition (P3) in a single transaction at timestamp T.

The PartitionEventRecord returned in P1 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P1" move_in_events { source_partition_token: "P2" } move_in_events { source_partition_token: "P3" } }

The PartitionEventRecord returned in P2 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P2" move_out_events { destination_partition_token: "P1" } }

The PartitionEventRecord returned in P3 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P3" move_out_events { destination_partition_token: "P1" } }

` repeated .google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveInEvent move_in_events = 4; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ChangeStreamRecord.PartitionEventRecord.MoveInEvent.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveInEvent.Builder)` |   
  
### getMoveInEventsBuilderList()
    
    
    public List<ChangeStreamRecord.PartitionEventRecord.MoveInEvent.Builder> getMoveInEventsBuilderList()

Set when one or more key ranges are moved into the change stream partition identified by partition_token.

Example: Two key ranges are moved into partition (P1) from partition (P2) and partition (P3) in a single transaction at timestamp T.

The PartitionEventRecord returned in P1 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P1" move_in_events { source_partition_token: "P2" } move_in_events { source_partition_token: "P3" } }

The PartitionEventRecord returned in P2 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P2" move_out_events { destination_partition_token: "P1" } }

The PartitionEventRecord returned in P3 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P3" move_out_events { destination_partition_token: "P1" } }

` repeated .google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveInEvent move_in_events = 4; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveInEvent.Builder)>` |   
  
### getMoveInEventsCount()
    
    
    public int getMoveInEventsCount()

Set when one or more key ranges are moved into the change stream partition identified by partition_token.

Example: Two key ranges are moved into partition (P1) from partition (P2) and partition (P3) in a single transaction at timestamp T.

The PartitionEventRecord returned in P1 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P1" move_in_events { source_partition_token: "P2" } move_in_events { source_partition_token: "P3" } }

The PartitionEventRecord returned in P2 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P2" move_out_events { destination_partition_token: "P1" } }

The PartitionEventRecord returned in P3 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P3" move_out_events { destination_partition_token: "P1" } }

` repeated .google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveInEvent move_in_events = 4; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getMoveInEventsList()
    
    
    public List<ChangeStreamRecord.PartitionEventRecord.MoveInEvent> getMoveInEventsList()

Set when one or more key ranges are moved into the change stream partition identified by partition_token.

Example: Two key ranges are moved into partition (P1) from partition (P2) and partition (P3) in a single transaction at timestamp T.

The PartitionEventRecord returned in P1 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P1" move_in_events { source_partition_token: "P2" } move_in_events { source_partition_token: "P3" } }

The PartitionEventRecord returned in P2 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P2" move_out_events { destination_partition_token: "P1" } }

The PartitionEventRecord returned in P3 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P3" move_out_events { destination_partition_token: "P1" } }

` repeated .google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveInEvent move_in_events = 4; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[MoveInEvent](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveInEvent)>` |   
  
### getMoveInEventsOrBuilder(int index)
    
    
    public ChangeStreamRecord.PartitionEventRecord.MoveInEventOrBuilder getMoveInEventsOrBuilder(int index)

Set when one or more key ranges are moved into the change stream partition identified by partition_token.

Example: Two key ranges are moved into partition (P1) from partition (P2) and partition (P3) in a single transaction at timestamp T.

The PartitionEventRecord returned in P1 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P1" move_in_events { source_partition_token: "P2" } move_in_events { source_partition_token: "P3" } }

The PartitionEventRecord returned in P2 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P2" move_out_events { destination_partition_token: "P1" } }

The PartitionEventRecord returned in P3 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P3" move_out_events { destination_partition_token: "P1" } }

` repeated .google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveInEvent move_in_events = 4; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ChangeStreamRecord.PartitionEventRecord.MoveInEventOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveInEventOrBuilder)` |   
  
### getMoveInEventsOrBuilderList()
    
    
    public List<? extends ChangeStreamRecord.PartitionEventRecord.MoveInEventOrBuilder> getMoveInEventsOrBuilderList()

Set when one or more key ranges are moved into the change stream partition identified by partition_token.

Example: Two key ranges are moved into partition (P1) from partition (P2) and partition (P3) in a single transaction at timestamp T.

The PartitionEventRecord returned in P1 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P1" move_in_events { source_partition_token: "P2" } move_in_events { source_partition_token: "P3" } }

The PartitionEventRecord returned in P2 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P2" move_out_events { destination_partition_token: "P1" } }

The PartitionEventRecord returned in P3 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P3" move_out_events { destination_partition_token: "P1" } }

` repeated .google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveInEvent move_in_events = 4; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveInEventOrBuilder>` |   
  
### getMoveOutEvents(int index)
    
    
    public ChangeStreamRecord.PartitionEventRecord.MoveOutEvent getMoveOutEvents(int index)

Set when one or more key ranges are moved out of the change stream partition identified by partition_token.

Example: Two key ranges are moved out of partition (P1) to partition (P2) and partition (P3) in a single transaction at timestamp T.

The PartitionEventRecord returned in P1 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P1" move_out_events { destination_partition_token: "P2" } move_out_events { destination_partition_token: "P3" } }

The PartitionEventRecord returned in P2 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P2" move_in_events { source_partition_token: "P1" } }

The PartitionEventRecord returned in P3 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P3" move_in_events { source_partition_token: "P1" } }

` repeated .google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveOutEvent move_out_events = 5; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ChangeStreamRecord.PartitionEventRecord.MoveOutEvent](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveOutEvent)` |   
  
### getMoveOutEventsBuilder(int index)
    
    
    public ChangeStreamRecord.PartitionEventRecord.MoveOutEvent.Builder getMoveOutEventsBuilder(int index)

Set when one or more key ranges are moved out of the change stream partition identified by partition_token.

Example: Two key ranges are moved out of partition (P1) to partition (P2) and partition (P3) in a single transaction at timestamp T.

The PartitionEventRecord returned in P1 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P1" move_out_events { destination_partition_token: "P2" } move_out_events { destination_partition_token: "P3" } }

The PartitionEventRecord returned in P2 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P2" move_in_events { source_partition_token: "P1" } }

The PartitionEventRecord returned in P3 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P3" move_in_events { source_partition_token: "P1" } }

` repeated .google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveOutEvent move_out_events = 5; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ChangeStreamRecord.PartitionEventRecord.MoveOutEvent.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveOutEvent.Builder)` |   
  
### getMoveOutEventsBuilderList()
    
    
    public List<ChangeStreamRecord.PartitionEventRecord.MoveOutEvent.Builder> getMoveOutEventsBuilderList()

Set when one or more key ranges are moved out of the change stream partition identified by partition_token.

Example: Two key ranges are moved out of partition (P1) to partition (P2) and partition (P3) in a single transaction at timestamp T.

The PartitionEventRecord returned in P1 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P1" move_out_events { destination_partition_token: "P2" } move_out_events { destination_partition_token: "P3" } }

The PartitionEventRecord returned in P2 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P2" move_in_events { source_partition_token: "P1" } }

The PartitionEventRecord returned in P3 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P3" move_in_events { source_partition_token: "P1" } }

` repeated .google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveOutEvent move_out_events = 5; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveOutEvent.Builder)>` |   
  
### getMoveOutEventsCount()
    
    
    public int getMoveOutEventsCount()

Set when one or more key ranges are moved out of the change stream partition identified by partition_token.

Example: Two key ranges are moved out of partition (P1) to partition (P2) and partition (P3) in a single transaction at timestamp T.

The PartitionEventRecord returned in P1 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P1" move_out_events { destination_partition_token: "P2" } move_out_events { destination_partition_token: "P3" } }

The PartitionEventRecord returned in P2 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P2" move_in_events { source_partition_token: "P1" } }

The PartitionEventRecord returned in P3 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P3" move_in_events { source_partition_token: "P1" } }

` repeated .google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveOutEvent move_out_events = 5; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getMoveOutEventsList()
    
    
    public List<ChangeStreamRecord.PartitionEventRecord.MoveOutEvent> getMoveOutEventsList()

Set when one or more key ranges are moved out of the change stream partition identified by partition_token.

Example: Two key ranges are moved out of partition (P1) to partition (P2) and partition (P3) in a single transaction at timestamp T.

The PartitionEventRecord returned in P1 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P1" move_out_events { destination_partition_token: "P2" } move_out_events { destination_partition_token: "P3" } }

The PartitionEventRecord returned in P2 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P2" move_in_events { source_partition_token: "P1" } }

The PartitionEventRecord returned in P3 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P3" move_in_events { source_partition_token: "P1" } }

` repeated .google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveOutEvent move_out_events = 5; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[MoveOutEvent](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveOutEvent)>` |   
  
### getMoveOutEventsOrBuilder(int index)
    
    
    public ChangeStreamRecord.PartitionEventRecord.MoveOutEventOrBuilder getMoveOutEventsOrBuilder(int index)

Set when one or more key ranges are moved out of the change stream partition identified by partition_token.

Example: Two key ranges are moved out of partition (P1) to partition (P2) and partition (P3) in a single transaction at timestamp T.

The PartitionEventRecord returned in P1 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P1" move_out_events { destination_partition_token: "P2" } move_out_events { destination_partition_token: "P3" } }

The PartitionEventRecord returned in P2 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P2" move_in_events { source_partition_token: "P1" } }

The PartitionEventRecord returned in P3 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P3" move_in_events { source_partition_token: "P1" } }

` repeated .google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveOutEvent move_out_events = 5; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ChangeStreamRecord.PartitionEventRecord.MoveOutEventOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveOutEventOrBuilder)` |   
  
### getMoveOutEventsOrBuilderList()
    
    
    public List<? extends ChangeStreamRecord.PartitionEventRecord.MoveOutEventOrBuilder> getMoveOutEventsOrBuilderList()

Set when one or more key ranges are moved out of the change stream partition identified by partition_token.

Example: Two key ranges are moved out of partition (P1) to partition (P2) and partition (P3) in a single transaction at timestamp T.

The PartitionEventRecord returned in P1 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P1" move_out_events { destination_partition_token: "P2" } move_out_events { destination_partition_token: "P3" } }

The PartitionEventRecord returned in P2 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P2" move_in_events { source_partition_token: "P1" } }

The PartitionEventRecord returned in P3 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P3" move_in_events { source_partition_token: "P1" } }

` repeated .google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveOutEvent move_out_events = 5; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveOutEventOrBuilder>` |   
  
### getPartitionToken()
    
    
    public String getPartitionToken()

Unique partition identifier describing the partition this event occurred on. partition_token is equal to the partition token of the change stream partition currently queried to return this PartitionEventRecord.

`string partition_token = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The partitionToken.  
  
### getPartitionTokenBytes()
    
    
    public ByteString getPartitionTokenBytes()

Unique partition identifier describing the partition this event occurred on. partition_token is equal to the partition token of the change stream partition currently queried to return this PartitionEventRecord.

`string partition_token = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for partitionToken.  
  
### getRecordSequence()
    
    
    public String getRecordSequence()

Record sequence numbers are unique and monotonically increasing (but not necessarily contiguous) for a specific timestamp across record types in the same partition. To guarantee ordered processing, the reader should process records (of potentially different types) in record_sequence order for a specific timestamp in the same partition.

`string record_sequence = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The recordSequence.  
  
### getRecordSequenceBytes()
    
    
    public ByteString getRecordSequenceBytes()

Record sequence numbers are unique and monotonically increasing (but not necessarily contiguous) for a specific timestamp across record types in the same partition. To guarantee ordered processing, the reader should process records (of potentially different types) in record_sequence order for a specific timestamp in the same partition.

`string record_sequence = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for recordSequence.  
  
### hasCommitTimestamp()
    
    
    public boolean hasCommitTimestamp()

Indicates the commit timestamp at which the key range change occurred. DataChangeRecord.commit_timestamps, PartitionStartRecord.start_timestamps, PartitionEventRecord.commit_timestamps, and PartitionEndRecord.end_timestamps can have the same value in the same partition.

`.google.protobuf.Timestamp commit_timestamp = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the commitTimestamp field is set.  
  
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

### mergeCommitTimestamp(Timestamp value)
    
    
    public ChangeStreamRecord.PartitionEventRecord.Builder mergeCommitTimestamp(Timestamp value)

Indicates the commit timestamp at which the key range change occurred. DataChangeRecord.commit_timestamps, PartitionStartRecord.start_timestamps, PartitionEventRecord.commit_timestamps, and PartitionEndRecord.end_timestamps can have the same value in the same partition.

`.google.protobuf.Timestamp commit_timestamp = 1;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ChangeStreamRecord.PartitionEventRecord.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public ChangeStreamRecord.PartitionEventRecord.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ChangeStreamRecord.PartitionEventRecord.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public ChangeStreamRecord.PartitionEventRecord.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ChangeStreamRecord.PartitionEventRecord.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### mergeFrom(ChangeStreamRecord.PartitionEventRecord other)
    
    
    public ChangeStreamRecord.PartitionEventRecord.Builder mergeFrom(ChangeStreamRecord.PartitionEventRecord other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ChangeStreamRecord.PartitionEventRecord](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ChangeStreamRecord.PartitionEventRecord.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.Builder)` |   
  
### removeMoveInEvents(int index)
    
    
    public ChangeStreamRecord.PartitionEventRecord.Builder removeMoveInEvents(int index)

Set when one or more key ranges are moved into the change stream partition identified by partition_token.

Example: Two key ranges are moved into partition (P1) from partition (P2) and partition (P3) in a single transaction at timestamp T.

The PartitionEventRecord returned in P1 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P1" move_in_events { source_partition_token: "P2" } move_in_events { source_partition_token: "P3" } }

The PartitionEventRecord returned in P2 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P2" move_out_events { destination_partition_token: "P1" } }

The PartitionEventRecord returned in P3 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P3" move_out_events { destination_partition_token: "P1" } }

` repeated .google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveInEvent move_in_events = 4; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ChangeStreamRecord.PartitionEventRecord.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.Builder)` |   
  
### removeMoveOutEvents(int index)
    
    
    public ChangeStreamRecord.PartitionEventRecord.Builder removeMoveOutEvents(int index)

Set when one or more key ranges are moved out of the change stream partition identified by partition_token.

Example: Two key ranges are moved out of partition (P1) to partition (P2) and partition (P3) in a single transaction at timestamp T.

The PartitionEventRecord returned in P1 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P1" move_out_events { destination_partition_token: "P2" } move_out_events { destination_partition_token: "P3" } }

The PartitionEventRecord returned in P2 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P2" move_in_events { source_partition_token: "P1" } }

The PartitionEventRecord returned in P3 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P3" move_in_events { source_partition_token: "P1" } }

` repeated .google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveOutEvent move_out_events = 5; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ChangeStreamRecord.PartitionEventRecord.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.Builder)` |   
  
### setCommitTimestamp(Timestamp value)
    
    
    public ChangeStreamRecord.PartitionEventRecord.Builder setCommitTimestamp(Timestamp value)

Indicates the commit timestamp at which the key range change occurred. DataChangeRecord.commit_timestamps, PartitionStartRecord.start_timestamps, PartitionEventRecord.commit_timestamps, and PartitionEndRecord.end_timestamps can have the same value in the same partition.

`.google.protobuf.Timestamp commit_timestamp = 1;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ChangeStreamRecord.PartitionEventRecord.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.Builder)` |   
  
### setCommitTimestamp(Timestamp.Builder builderForValue)
    
    
    public ChangeStreamRecord.PartitionEventRecord.Builder setCommitTimestamp(Timestamp.Builder builderForValue)

Indicates the commit timestamp at which the key range change occurred. DataChangeRecord.commit_timestamps, PartitionStartRecord.start_timestamps, PartitionEventRecord.commit_timestamps, and PartitionEndRecord.end_timestamps can have the same value in the same partition.

`.google.protobuf.Timestamp commit_timestamp = 1;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ChangeStreamRecord.PartitionEventRecord.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.Builder)` |   
  
### setMoveInEvents(int index, ChangeStreamRecord.PartitionEventRecord.MoveInEvent value)
    
    
    public ChangeStreamRecord.PartitionEventRecord.Builder setMoveInEvents(int index, ChangeStreamRecord.PartitionEventRecord.MoveInEvent value)

Set when one or more key ranges are moved into the change stream partition identified by partition_token.

Example: Two key ranges are moved into partition (P1) from partition (P2) and partition (P3) in a single transaction at timestamp T.

The PartitionEventRecord returned in P1 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P1" move_in_events { source_partition_token: "P2" } move_in_events { source_partition_token: "P3" } }

The PartitionEventRecord returned in P2 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P2" move_out_events { destination_partition_token: "P1" } }

The PartitionEventRecord returned in P3 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P3" move_out_events { destination_partition_token: "P1" } }

` repeated .google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveInEvent move_in_events = 4; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[ChangeStreamRecord.PartitionEventRecord.MoveInEvent](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveInEvent)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ChangeStreamRecord.PartitionEventRecord.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.Builder)` |   
  
### setMoveInEvents(int index, ChangeStreamRecord.PartitionEventRecord.MoveInEvent.Builder builderForValue)
    
    
    public ChangeStreamRecord.PartitionEventRecord.Builder setMoveInEvents(int index, ChangeStreamRecord.PartitionEventRecord.MoveInEvent.Builder builderForValue)

Set when one or more key ranges are moved into the change stream partition identified by partition_token.

Example: Two key ranges are moved into partition (P1) from partition (P2) and partition (P3) in a single transaction at timestamp T.

The PartitionEventRecord returned in P1 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P1" move_in_events { source_partition_token: "P2" } move_in_events { source_partition_token: "P3" } }

The PartitionEventRecord returned in P2 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P2" move_out_events { destination_partition_token: "P1" } }

The PartitionEventRecord returned in P3 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P3" move_out_events { destination_partition_token: "P1" } }

` repeated .google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveInEvent move_in_events = 4; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[ChangeStreamRecord.PartitionEventRecord.MoveInEvent.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveInEvent.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ChangeStreamRecord.PartitionEventRecord.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.Builder)` |   
  
### setMoveOutEvents(int index, ChangeStreamRecord.PartitionEventRecord.MoveOutEvent value)
    
    
    public ChangeStreamRecord.PartitionEventRecord.Builder setMoveOutEvents(int index, ChangeStreamRecord.PartitionEventRecord.MoveOutEvent value)

Set when one or more key ranges are moved out of the change stream partition identified by partition_token.

Example: Two key ranges are moved out of partition (P1) to partition (P2) and partition (P3) in a single transaction at timestamp T.

The PartitionEventRecord returned in P1 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P1" move_out_events { destination_partition_token: "P2" } move_out_events { destination_partition_token: "P3" } }

The PartitionEventRecord returned in P2 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P2" move_in_events { source_partition_token: "P1" } }

The PartitionEventRecord returned in P3 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P3" move_in_events { source_partition_token: "P1" } }

` repeated .google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveOutEvent move_out_events = 5; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[ChangeStreamRecord.PartitionEventRecord.MoveOutEvent](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveOutEvent)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ChangeStreamRecord.PartitionEventRecord.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.Builder)` |   
  
### setMoveOutEvents(int index, ChangeStreamRecord.PartitionEventRecord.MoveOutEvent.Builder builderForValue)
    
    
    public ChangeStreamRecord.PartitionEventRecord.Builder setMoveOutEvents(int index, ChangeStreamRecord.PartitionEventRecord.MoveOutEvent.Builder builderForValue)

Set when one or more key ranges are moved out of the change stream partition identified by partition_token.

Example: Two key ranges are moved out of partition (P1) to partition (P2) and partition (P3) in a single transaction at timestamp T.

The PartitionEventRecord returned in P1 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P1" move_out_events { destination_partition_token: "P2" } move_out_events { destination_partition_token: "P3" } }

The PartitionEventRecord returned in P2 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P2" move_in_events { source_partition_token: "P1" } }

The PartitionEventRecord returned in P3 will reflect the move as:

PartitionEventRecord { commit_timestamp: T partition_token: "P3" move_in_events { source_partition_token: "P1" } }

` repeated .google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveOutEvent move_out_events = 5; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[ChangeStreamRecord.PartitionEventRecord.MoveOutEvent.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveOutEvent.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ChangeStreamRecord.PartitionEventRecord.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.Builder)` |   
  
### setPartitionToken(String value)
    
    
    public ChangeStreamRecord.PartitionEventRecord.Builder setPartitionToken(String value)

Unique partition identifier describing the partition this event occurred on. partition_token is equal to the partition token of the change stream partition currently queried to return this PartitionEventRecord.

`string partition_token = 3;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The partitionToken to set.  
**Returns**  
---  
**Type** | **Description**  
`[ChangeStreamRecord.PartitionEventRecord.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.Builder)` | This builder for chaining.  
  
### setPartitionTokenBytes(ByteString value)
    
    
    public ChangeStreamRecord.PartitionEventRecord.Builder setPartitionTokenBytes(ByteString value)

Unique partition identifier describing the partition this event occurred on. partition_token is equal to the partition token of the change stream partition currently queried to return this PartitionEventRecord.

`string partition_token = 3;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for partitionToken to set.  
**Returns**  
---  
**Type** | **Description**  
`[ChangeStreamRecord.PartitionEventRecord.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.Builder)` | This builder for chaining.  
  
### setRecordSequence(String value)
    
    
    public ChangeStreamRecord.PartitionEventRecord.Builder setRecordSequence(String value)

Record sequence numbers are unique and monotonically increasing (but not necessarily contiguous) for a specific timestamp across record types in the same partition. To guarantee ordered processing, the reader should process records (of potentially different types) in record_sequence order for a specific timestamp in the same partition.

`string record_sequence = 2;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The recordSequence to set.  
**Returns**  
---  
**Type** | **Description**  
`[ChangeStreamRecord.PartitionEventRecord.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.Builder)` | This builder for chaining.  
  
### setRecordSequenceBytes(ByteString value)
    
    
    public ChangeStreamRecord.PartitionEventRecord.Builder setRecordSequenceBytes(ByteString value)

Record sequence numbers are unique and monotonically increasing (but not necessarily contiguous) for a specific timestamp across record types in the same partition. To guarantee ordered processing, the reader should process records (of potentially different types) in record_sequence order for a specific timestamp in the same partition.

`string record_sequence = 2;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for recordSequence to set.  
**Returns**  
---  
**Type** | **Description**  
`[ChangeStreamRecord.PartitionEventRecord.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.Builder)` | This builder for chaining.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
