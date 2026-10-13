---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AutomatedBackupPolicy.WeeklySchedule.Builder
title: Class AutomatedBackupPolicy.WeeklySchedule.Builder (0.88.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:50:33.305157+00:00
---

# Class AutomatedBackupPolicy.WeeklySchedule.Builder (0.88.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AutomatedBackupPolicy.WeeklySchedule.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class AutomatedBackupPolicy.WeeklySchedule.Builder (0.88.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.88.0 (latest)  0.84.0  0.83.0  0.82.0  0.80.0  0.77.0  0.76.0  0.74.0  0.72.0  0.71.0  0.70.0  0.69.0  0.67.0  0.65.0  0.64.0  0.63.0  0.62.0  0.61.0  0.59.0  0.57.0  0.56.0  0.53.0  0.52.0  0.51.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static final class AutomatedBackupPolicy.WeeklySchedule.Builder extends GeneratedMessage.Builder<AutomatedBackupPolicy.WeeklySchedule.Builder> implements AutomatedBackupPolicy.WeeklyScheduleOrBuilder

A weekly schedule starts a backup at prescribed start times within a day, for the specified days of the week.

The weekly schedule message is flexible and can be used to create many types of schedules. For example, to have a daily backup that starts at 22:00, configure the `start_times` field to have one element "22:00" and the `days_of_week` field to have all seven days of the week.

Protobuf type `google.cloud.alloydb.v1.AutomatedBackupPolicy.WeeklySchedule`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > AutomatedBackupPolicy.WeeklySchedule.Builder

## Implements

[AutomatedBackupPolicy.WeeklyScheduleOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AutomatedBackupPolicy.WeeklyScheduleOrBuilder)

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

### addAllDaysOfWeek(Iterable<? extends DayOfWeek> values)
    
    
    public AutomatedBackupPolicy.WeeklySchedule.Builder addAllDaysOfWeek(Iterable<? extends DayOfWeek> values)

The days of the week to perform a backup.

If this field is left empty, the default of every day of the week is used.

`repeated .google.type.DayOfWeek days_of_week = 2;`

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<? extends com.google.type.DayOfWeek>`  
The daysOfWeek to add.  
**Returns**  
---  
**Type** | **Description**  
`[AutomatedBackupPolicy.WeeklySchedule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AutomatedBackupPolicy.WeeklySchedule.Builder)` | This builder for chaining.  
  
### addAllDaysOfWeekValue(Iterable<Integer> values)
    
    
    public AutomatedBackupPolicy.WeeklySchedule.Builder addAllDaysOfWeekValue(Iterable<Integer> values)

The days of the week to perform a backup.

If this field is left empty, the default of every day of the week is used.

`repeated .google.type.DayOfWeek days_of_week = 2;`

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)>`  
The enum numeric values on the wire for daysOfWeek to add.  
**Returns**  
---  
**Type** | **Description**  
`[AutomatedBackupPolicy.WeeklySchedule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AutomatedBackupPolicy.WeeklySchedule.Builder)` | This builder for chaining.  
  
### addAllStartTimes(Iterable<? extends TimeOfDay> values)
    
    
    public AutomatedBackupPolicy.WeeklySchedule.Builder addAllStartTimes(Iterable<? extends TimeOfDay> values)

The times during the day to start a backup. The start times are assumed to be in UTC and to be an exact hour (e.g., 04:00:00).

If no start times are provided, a single fixed start time is chosen arbitrarily.

`repeated .google.type.TimeOfDay start_times = 1;`

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<? extends com.google.type.TimeOfDay>`  
  
**Returns**  
---  
**Type** | **Description**  
`[AutomatedBackupPolicy.WeeklySchedule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AutomatedBackupPolicy.WeeklySchedule.Builder)` |   
  
### addDaysOfWeek(DayOfWeek value)
    
    
    public AutomatedBackupPolicy.WeeklySchedule.Builder addDaysOfWeek(DayOfWeek value)

The days of the week to perform a backup.

If this field is left empty, the default of every day of the week is used.

`repeated .google.type.DayOfWeek days_of_week = 2;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `com.google.type.DayOfWeek`  
The daysOfWeek to add.  
**Returns**  
---  
**Type** | **Description**  
`[AutomatedBackupPolicy.WeeklySchedule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AutomatedBackupPolicy.WeeklySchedule.Builder)` | This builder for chaining.  
  
### addDaysOfWeekValue(int value)
    
    
    public AutomatedBackupPolicy.WeeklySchedule.Builder addDaysOfWeekValue(int value)

The days of the week to perform a backup.

If this field is left empty, the default of every day of the week is used.

`repeated .google.type.DayOfWeek days_of_week = 2;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The enum numeric value on the wire for daysOfWeek to add.  
**Returns**  
---  
**Type** | **Description**  
`[AutomatedBackupPolicy.WeeklySchedule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AutomatedBackupPolicy.WeeklySchedule.Builder)` | This builder for chaining.  
  
### addStartTimes(TimeOfDay value)
    
    
    public AutomatedBackupPolicy.WeeklySchedule.Builder addStartTimes(TimeOfDay value)

The times during the day to start a backup. The start times are assumed to be in UTC and to be an exact hour (e.g., 04:00:00).

If no start times are provided, a single fixed start time is chosen arbitrarily.

`repeated .google.type.TimeOfDay start_times = 1;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `com.google.type.TimeOfDay`  
  
**Returns**  
---  
**Type** | **Description**  
`[AutomatedBackupPolicy.WeeklySchedule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AutomatedBackupPolicy.WeeklySchedule.Builder)` |   
  
### addStartTimes(TimeOfDay.Builder builderForValue)
    
    
    public AutomatedBackupPolicy.WeeklySchedule.Builder addStartTimes(TimeOfDay.Builder builderForValue)

The times during the day to start a backup. The start times are assumed to be in UTC and to be an exact hour (e.g., 04:00:00).

If no start times are provided, a single fixed start time is chosen arbitrarily.

`repeated .google.type.TimeOfDay start_times = 1;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `com.google.type.TimeOfDay.Builder`  
  
**Returns**  
---  
**Type** | **Description**  
`[AutomatedBackupPolicy.WeeklySchedule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AutomatedBackupPolicy.WeeklySchedule.Builder)` |   
  
### addStartTimes(int index, TimeOfDay value)
    
    
    public AutomatedBackupPolicy.WeeklySchedule.Builder addStartTimes(int index, TimeOfDay value)

The times during the day to start a backup. The start times are assumed to be in UTC and to be an exact hour (e.g., 04:00:00).

If no start times are provided, a single fixed start time is chosen arbitrarily.

`repeated .google.type.TimeOfDay start_times = 1;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `com.google.type.TimeOfDay`  
  
**Returns**  
---  
**Type** | **Description**  
`[AutomatedBackupPolicy.WeeklySchedule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AutomatedBackupPolicy.WeeklySchedule.Builder)` |   
  
### addStartTimes(int index, TimeOfDay.Builder builderForValue)
    
    
    public AutomatedBackupPolicy.WeeklySchedule.Builder addStartTimes(int index, TimeOfDay.Builder builderForValue)

The times during the day to start a backup. The start times are assumed to be in UTC and to be an exact hour (e.g., 04:00:00).

If no start times are provided, a single fixed start time is chosen arbitrarily.

`repeated .google.type.TimeOfDay start_times = 1;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `com.google.type.TimeOfDay.Builder`  
  
**Returns**  
---  
**Type** | **Description**  
`[AutomatedBackupPolicy.WeeklySchedule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AutomatedBackupPolicy.WeeklySchedule.Builder)` |   
  
### addStartTimesBuilder()
    
    
    public TimeOfDay.Builder addStartTimesBuilder()

The times during the day to start a backup. The start times are assumed to be in UTC and to be an exact hour (e.g., 04:00:00).

If no start times are provided, a single fixed start time is chosen arbitrarily.

`repeated .google.type.TimeOfDay start_times = 1;`

**Returns**  
---  
**Type** | **Description**  
`com.google.type.TimeOfDay.Builder` |   
  
### addStartTimesBuilder(int index)
    
    
    public TimeOfDay.Builder addStartTimesBuilder(int index)

The times during the day to start a backup. The start times are assumed to be in UTC and to be an exact hour (e.g., 04:00:00).

If no start times are provided, a single fixed start time is chosen arbitrarily.

`repeated .google.type.TimeOfDay start_times = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.type.TimeOfDay.Builder` |   
  
### build()
    
    
    public AutomatedBackupPolicy.WeeklySchedule build()

**Returns**  
---  
**Type** | **Description**  
`[AutomatedBackupPolicy.WeeklySchedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AutomatedBackupPolicy.WeeklySchedule)` |   
  
### buildPartial()
    
    
    public AutomatedBackupPolicy.WeeklySchedule buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[AutomatedBackupPolicy.WeeklySchedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AutomatedBackupPolicy.WeeklySchedule)` |   
  
### clear()
    
    
    public AutomatedBackupPolicy.WeeklySchedule.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[AutomatedBackupPolicy.WeeklySchedule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AutomatedBackupPolicy.WeeklySchedule.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearDaysOfWeek()
    
    
    public AutomatedBackupPolicy.WeeklySchedule.Builder clearDaysOfWeek()

The days of the week to perform a backup.

If this field is left empty, the default of every day of the week is used.

`repeated .google.type.DayOfWeek days_of_week = 2;`

**Returns**  
---  
**Type** | **Description**  
`[AutomatedBackupPolicy.WeeklySchedule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AutomatedBackupPolicy.WeeklySchedule.Builder)` | This builder for chaining.  
  
### clearStartTimes()
    
    
    public AutomatedBackupPolicy.WeeklySchedule.Builder clearStartTimes()

The times during the day to start a backup. The start times are assumed to be in UTC and to be an exact hour (e.g., 04:00:00).

If no start times are provided, a single fixed start time is chosen arbitrarily.

`repeated .google.type.TimeOfDay start_times = 1;`

**Returns**  
---  
**Type** | **Description**  
`[AutomatedBackupPolicy.WeeklySchedule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AutomatedBackupPolicy.WeeklySchedule.Builder)` |   
  
### getDaysOfWeek(int index)
    
    
    public DayOfWeek getDaysOfWeek(int index)

The days of the week to perform a backup.

If this field is left empty, the default of every day of the week is used.

`repeated .google.type.DayOfWeek days_of_week = 2;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`com.google.type.DayOfWeek` | The daysOfWeek at the given index.  
  
### getDaysOfWeekCount()
    
    
    public int getDaysOfWeekCount()

The days of the week to perform a backup.

If this field is left empty, the default of every day of the week is used.

`repeated .google.type.DayOfWeek days_of_week = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of daysOfWeek.  
  
### getDaysOfWeekList()
    
    
    public List<DayOfWeek> getDaysOfWeekList()

The days of the week to perform a backup.

If this field is left empty, the default of every day of the week is used.

`repeated .google.type.DayOfWeek days_of_week = 2;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<com.google.type.DayOfWeek>` | A list containing the daysOfWeek.  
  
### getDaysOfWeekValue(int index)
    
    
    public int getDaysOfWeekValue(int index)

The days of the week to perform a backup.

If this field is left empty, the default of every day of the week is used.

`repeated .google.type.DayOfWeek days_of_week = 2;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire of daysOfWeek at the given index.  
  
### getDaysOfWeekValueList()
    
    
    public List<Integer> getDaysOfWeekValueList()

The days of the week to perform a backup.

If this field is left empty, the default of every day of the week is used.

`repeated .google.type.DayOfWeek days_of_week = 2;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)>` | A list containing the enum numeric values on the wire for daysOfWeek.  
  
### getDefaultInstanceForType()
    
    
    public AutomatedBackupPolicy.WeeklySchedule getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[AutomatedBackupPolicy.WeeklySchedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AutomatedBackupPolicy.WeeklySchedule)` |   
  
### getDescriptorForType()
    
    
    public Descriptors.Descriptor getDescriptorForType()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getDescriptorForType__)

### getStartTimes(int index)
    
    
    public TimeOfDay getStartTimes(int index)

The times during the day to start a backup. The start times are assumed to be in UTC and to be an exact hour (e.g., 04:00:00).

If no start times are provided, a single fixed start time is chosen arbitrarily.

`repeated .google.type.TimeOfDay start_times = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.type.TimeOfDay` |   
  
### getStartTimesBuilder(int index)
    
    
    public TimeOfDay.Builder getStartTimesBuilder(int index)

The times during the day to start a backup. The start times are assumed to be in UTC and to be an exact hour (e.g., 04:00:00).

If no start times are provided, a single fixed start time is chosen arbitrarily.

`repeated .google.type.TimeOfDay start_times = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.type.TimeOfDay.Builder` |   
  
### getStartTimesBuilderList()
    
    
    public List<TimeOfDay.Builder> getStartTimesBuilderList()

The times during the day to start a backup. The start times are assumed to be in UTC and to be an exact hour (e.g., 04:00:00).

If no start times are provided, a single fixed start time is chosen arbitrarily.

`repeated .google.type.TimeOfDay start_times = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<com.google.type.TimeOfDay.Builder>` |   
  
### getStartTimesCount()
    
    
    public int getStartTimesCount()

The times during the day to start a backup. The start times are assumed to be in UTC and to be an exact hour (e.g., 04:00:00).

If no start times are provided, a single fixed start time is chosen arbitrarily.

`repeated .google.type.TimeOfDay start_times = 1;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getStartTimesList()
    
    
    public List<TimeOfDay> getStartTimesList()

The times during the day to start a backup. The start times are assumed to be in UTC and to be an exact hour (e.g., 04:00:00).

If no start times are provided, a single fixed start time is chosen arbitrarily.

`repeated .google.type.TimeOfDay start_times = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<com.google.type.TimeOfDay>` |   
  
### getStartTimesOrBuilder(int index)
    
    
    public TimeOfDayOrBuilder getStartTimesOrBuilder(int index)

The times during the day to start a backup. The start times are assumed to be in UTC and to be an exact hour (e.g., 04:00:00).

If no start times are provided, a single fixed start time is chosen arbitrarily.

`repeated .google.type.TimeOfDay start_times = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.type.TimeOfDayOrBuilder` |   
  
### getStartTimesOrBuilderList()
    
    
    public List<? extends TimeOfDayOrBuilder> getStartTimesOrBuilderList()

The times during the day to start a backup. The start times are assumed to be in UTC and to be an exact hour (e.g., 04:00:00).

If no start times are provided, a single fixed start time is chosen arbitrarily.

`repeated .google.type.TimeOfDay start_times = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.type.TimeOfDayOrBuilder>` |   
  
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

### mergeFrom(AutomatedBackupPolicy.WeeklySchedule other)
    
    
    public AutomatedBackupPolicy.WeeklySchedule.Builder mergeFrom(AutomatedBackupPolicy.WeeklySchedule other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AutomatedBackupPolicy.WeeklySchedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AutomatedBackupPolicy.WeeklySchedule)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AutomatedBackupPolicy.WeeklySchedule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AutomatedBackupPolicy.WeeklySchedule.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public AutomatedBackupPolicy.WeeklySchedule.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AutomatedBackupPolicy.WeeklySchedule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AutomatedBackupPolicy.WeeklySchedule.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public AutomatedBackupPolicy.WeeklySchedule.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AutomatedBackupPolicy.WeeklySchedule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AutomatedBackupPolicy.WeeklySchedule.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### removeStartTimes(int index)
    
    
    public AutomatedBackupPolicy.WeeklySchedule.Builder removeStartTimes(int index)

The times during the day to start a backup. The start times are assumed to be in UTC and to be an exact hour (e.g., 04:00:00).

If no start times are provided, a single fixed start time is chosen arbitrarily.

`repeated .google.type.TimeOfDay start_times = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AutomatedBackupPolicy.WeeklySchedule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AutomatedBackupPolicy.WeeklySchedule.Builder)` |   
  
### setDaysOfWeek(int index, DayOfWeek value)
    
    
    public AutomatedBackupPolicy.WeeklySchedule.Builder setDaysOfWeek(int index, DayOfWeek value)

The days of the week to perform a backup.

If this field is left empty, the default of every day of the week is used.

`repeated .google.type.DayOfWeek days_of_week = 2;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index to set the value at.  
`value` | `com.google.type.DayOfWeek`  
The daysOfWeek to set.  
**Returns**  
---  
**Type** | **Description**  
`[AutomatedBackupPolicy.WeeklySchedule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AutomatedBackupPolicy.WeeklySchedule.Builder)` | This builder for chaining.  
  
### setDaysOfWeekValue(int index, int value)
    
    
    public AutomatedBackupPolicy.WeeklySchedule.Builder setDaysOfWeekValue(int index, int value)

The days of the week to perform a backup.

If this field is left empty, the default of every day of the week is used.

`repeated .google.type.DayOfWeek days_of_week = 2;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index to set the value at.  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The enum numeric value on the wire for daysOfWeek to set.  
**Returns**  
---  
**Type** | **Description**  
`[AutomatedBackupPolicy.WeeklySchedule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AutomatedBackupPolicy.WeeklySchedule.Builder)` | This builder for chaining.  
  
### setStartTimes(int index, TimeOfDay value)
    
    
    public AutomatedBackupPolicy.WeeklySchedule.Builder setStartTimes(int index, TimeOfDay value)

The times during the day to start a backup. The start times are assumed to be in UTC and to be an exact hour (e.g., 04:00:00).

If no start times are provided, a single fixed start time is chosen arbitrarily.

`repeated .google.type.TimeOfDay start_times = 1;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `com.google.type.TimeOfDay`  
  
**Returns**  
---  
**Type** | **Description**  
`[AutomatedBackupPolicy.WeeklySchedule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AutomatedBackupPolicy.WeeklySchedule.Builder)` |   
  
### setStartTimes(int index, TimeOfDay.Builder builderForValue)
    
    
    public AutomatedBackupPolicy.WeeklySchedule.Builder setStartTimes(int index, TimeOfDay.Builder builderForValue)

The times during the day to start a backup. The start times are assumed to be in UTC and to be an exact hour (e.g., 04:00:00).

If no start times are provided, a single fixed start time is chosen arbitrarily.

`repeated .google.type.TimeOfDay start_times = 1;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `com.google.type.TimeOfDay.Builder`  
  
**Returns**  
---  
**Type** | **Description**  
`[AutomatedBackupPolicy.WeeklySchedule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AutomatedBackupPolicy.WeeklySchedule.Builder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
