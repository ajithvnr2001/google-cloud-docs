---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.StandardSchedule.Builder
title: Class StandardSchedule.Builder (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:46:39.660624+00:00
---

# Class StandardSchedule.Builder (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.StandardSchedule.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class StandardSchedule.Builder (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static final class StandardSchedule.Builder extends GeneratedMessage.Builder<StandardSchedule.Builder> implements StandardScheduleOrBuilder

`StandardSchedule` defines a schedule that run within the confines of a defined window of days. We can define recurrence type for schedule as HOURLY, DAILY, WEEKLY, MONTHLY or YEARLY.

Protobuf type `google.cloud.backupdr.v1beta.StandardSchedule`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > StandardSchedule.Builder

## Implements

[StandardScheduleOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.StandardScheduleOrBuilder)

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

### addAllDaysOfMonth(Iterable<? extends Integer> values)
    
    
    public StandardSchedule.Builder addAllDaysOfMonth(Iterable<? extends Integer> values)

Optional. Specifies days of months like 1, 5, or 14 on which jobs will run.

Values for `days_of_month` are only applicable for `recurrence_type`, `MONTHLY` and `YEARLY`. A validation error will occur if other values are supplied.

`repeated int32 days_of_month = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<? extends java.lang.Integer>`  
The daysOfMonth to add.  
**Returns**  
---  
**Type** | **Description**  
`[StandardSchedule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.StandardSchedule.Builder)` | This builder for chaining.  
  
### addAllDaysOfWeek(Iterable<? extends DayOfWeek> values)
    
    
    public StandardSchedule.Builder addAllDaysOfWeek(Iterable<? extends DayOfWeek> values)

Optional. Specifies days of week like, MONDAY or TUESDAY, on which jobs will run.

This is required for `recurrence_type`, `WEEKLY` and is not applicable otherwise. A validation error will occur if a value is supplied and `recurrence_type` is not `WEEKLY`.

` repeated .google.type.DayOfWeek days_of_week = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<? extends com.google.type.DayOfWeek>`  
The daysOfWeek to add.  
**Returns**  
---  
**Type** | **Description**  
`[StandardSchedule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.StandardSchedule.Builder)` | This builder for chaining.  
  
### addAllDaysOfWeekValue(Iterable<Integer> values)
    
    
    public StandardSchedule.Builder addAllDaysOfWeekValue(Iterable<Integer> values)

Optional. Specifies days of week like, MONDAY or TUESDAY, on which jobs will run.

This is required for `recurrence_type`, `WEEKLY` and is not applicable otherwise. A validation error will occur if a value is supplied and `recurrence_type` is not `WEEKLY`.

` repeated .google.type.DayOfWeek days_of_week = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)>`  
The enum numeric values on the wire for daysOfWeek to add.  
**Returns**  
---  
**Type** | **Description**  
`[StandardSchedule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.StandardSchedule.Builder)` | This builder for chaining.  
  
### addAllMonths(Iterable<? extends Month> values)
    
    
    public StandardSchedule.Builder addAllMonths(Iterable<? extends Month> values)

Optional. Specifies the months of year, like `FEBRUARY` and/or `MAY`, on which jobs will run.

This field is only applicable when `recurrence_type` is `YEARLY`. A validation error will occur if other values are supplied.

`repeated .google.type.Month months = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<? extends com.google.type.Month>`  
The months to add.  
**Returns**  
---  
**Type** | **Description**  
`[StandardSchedule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.StandardSchedule.Builder)` | This builder for chaining.  
  
### addAllMonthsValue(Iterable<Integer> values)
    
    
    public StandardSchedule.Builder addAllMonthsValue(Iterable<Integer> values)

Optional. Specifies the months of year, like `FEBRUARY` and/or `MAY`, on which jobs will run.

This field is only applicable when `recurrence_type` is `YEARLY`. A validation error will occur if other values are supplied.

`repeated .google.type.Month months = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)>`  
The enum numeric values on the wire for months to add.  
**Returns**  
---  
**Type** | **Description**  
`[StandardSchedule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.StandardSchedule.Builder)` | This builder for chaining.  
  
### addDaysOfMonth(int value)
    
    
    public StandardSchedule.Builder addDaysOfMonth(int value)

Optional. Specifies days of months like 1, 5, or 14 on which jobs will run.

Values for `days_of_month` are only applicable for `recurrence_type`, `MONTHLY` and `YEARLY`. A validation error will occur if other values are supplied.

`repeated int32 days_of_month = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The daysOfMonth to add.  
**Returns**  
---  
**Type** | **Description**  
`[StandardSchedule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.StandardSchedule.Builder)` | This builder for chaining.  
  
### addDaysOfWeek(DayOfWeek value)
    
    
    public StandardSchedule.Builder addDaysOfWeek(DayOfWeek value)

Optional. Specifies days of week like, MONDAY or TUESDAY, on which jobs will run.

This is required for `recurrence_type`, `WEEKLY` and is not applicable otherwise. A validation error will occur if a value is supplied and `recurrence_type` is not `WEEKLY`.

` repeated .google.type.DayOfWeek days_of_week = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `com.google.type.DayOfWeek`  
The daysOfWeek to add.  
**Returns**  
---  
**Type** | **Description**  
`[StandardSchedule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.StandardSchedule.Builder)` | This builder for chaining.  
  
### addDaysOfWeekValue(int value)
    
    
    public StandardSchedule.Builder addDaysOfWeekValue(int value)

Optional. Specifies days of week like, MONDAY or TUESDAY, on which jobs will run.

This is required for `recurrence_type`, `WEEKLY` and is not applicable otherwise. A validation error will occur if a value is supplied and `recurrence_type` is not `WEEKLY`.

` repeated .google.type.DayOfWeek days_of_week = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The enum numeric value on the wire for daysOfWeek to add.  
**Returns**  
---  
**Type** | **Description**  
`[StandardSchedule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.StandardSchedule.Builder)` | This builder for chaining.  
  
### addMonths(Month value)
    
    
    public StandardSchedule.Builder addMonths(Month value)

Optional. Specifies the months of year, like `FEBRUARY` and/or `MAY`, on which jobs will run.

This field is only applicable when `recurrence_type` is `YEARLY`. A validation error will occur if other values are supplied.

`repeated .google.type.Month months = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `com.google.type.Month`  
The months to add.  
**Returns**  
---  
**Type** | **Description**  
`[StandardSchedule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.StandardSchedule.Builder)` | This builder for chaining.  
  
### addMonthsValue(int value)
    
    
    public StandardSchedule.Builder addMonthsValue(int value)

Optional. Specifies the months of year, like `FEBRUARY` and/or `MAY`, on which jobs will run.

This field is only applicable when `recurrence_type` is `YEARLY`. A validation error will occur if other values are supplied.

`repeated .google.type.Month months = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The enum numeric value on the wire for months to add.  
**Returns**  
---  
**Type** | **Description**  
`[StandardSchedule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.StandardSchedule.Builder)` | This builder for chaining.  
  
### build()
    
    
    public StandardSchedule build()

**Returns**  
---  
**Type** | **Description**  
`[StandardSchedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.StandardSchedule)` |   
  
### buildPartial()
    
    
    public StandardSchedule buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[StandardSchedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.StandardSchedule)` |   
  
### clear()
    
    
    public StandardSchedule.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[StandardSchedule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.StandardSchedule.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearBackupWindow()
    
    
    public StandardSchedule.Builder clearBackupWindow()

Required. A BackupWindow defines the window of day during which backup jobs will run. Jobs are queued at the beginning of the window and will be marked as `NOT_RUN` if they do not start by the end of the window.

Note: running jobs will not be cancelled at the end of the window.

` .google.cloud.backupdr.v1beta.BackupWindow backup_window = 7 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[StandardSchedule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.StandardSchedule.Builder)` |   
  
### clearDaysOfMonth()
    
    
    public StandardSchedule.Builder clearDaysOfMonth()

Optional. Specifies days of months like 1, 5, or 14 on which jobs will run.

Values for `days_of_month` are only applicable for `recurrence_type`, `MONTHLY` and `YEARLY`. A validation error will occur if other values are supplied.

`repeated int32 days_of_month = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[StandardSchedule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.StandardSchedule.Builder)` | This builder for chaining.  
  
### clearDaysOfWeek()
    
    
    public StandardSchedule.Builder clearDaysOfWeek()

Optional. Specifies days of week like, MONDAY or TUESDAY, on which jobs will run.

This is required for `recurrence_type`, `WEEKLY` and is not applicable otherwise. A validation error will occur if a value is supplied and `recurrence_type` is not `WEEKLY`.

` repeated .google.type.DayOfWeek days_of_week = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[StandardSchedule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.StandardSchedule.Builder)` | This builder for chaining.  
  
### clearHourlyFrequency()
    
    
    public StandardSchedule.Builder clearHourlyFrequency()

Optional. Specifies frequency for hourly backups. A hourly frequency of 2 means jobs will run every 2 hours from start time till end time defined.

This is required for `recurrence_type`, `HOURLY` and is not applicable otherwise. A validation error will occur if a value is supplied and `recurrence_type` is not `HOURLY`.

The supported values for each resource type are as follows:

  * `compute.googleapis.com/Instance`: 1-23
  * `compute.googleapis.com/Disk`: 1-23
  * `sqladmin.googleapis.com/Instance`: 6-23
  * `alloydb.googleapis.com/Cluster`: 1-23
  * `file.googleapis.com/Instance`: 1-23

Refer to link <https://cloud.google.com/backup-disaster-recovery/docs/concepts/cloud_best_practices> for more details.




`int32 hourly_frequency = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[StandardSchedule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.StandardSchedule.Builder)` | This builder for chaining.  
  
### clearMonths()
    
    
    public StandardSchedule.Builder clearMonths()

Optional. Specifies the months of year, like `FEBRUARY` and/or `MAY`, on which jobs will run.

This field is only applicable when `recurrence_type` is `YEARLY`. A validation error will occur if other values are supplied.

`repeated .google.type.Month months = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[StandardSchedule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.StandardSchedule.Builder)` | This builder for chaining.  
  
### clearRecurrenceType()
    
    
    public StandardSchedule.Builder clearRecurrenceType()

Required. Specifies the `RecurrenceType` for the schedule.

` .google.cloud.backupdr.v1beta.StandardSchedule.RecurrenceType recurrence_type = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[StandardSchedule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.StandardSchedule.Builder)` | This builder for chaining.  
  
### clearTimeZone()
    
    
    public StandardSchedule.Builder clearTimeZone()

Required. The time zone to be used when interpreting the schedule. The value of this field must be a time zone name from the IANA tz database. See <https://en.wikipedia.org/wiki/List_of_tz_database_time_zones> for the list of valid timezone names. For e.g., Europe/Paris.

`string time_zone = 8 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[StandardSchedule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.StandardSchedule.Builder)` | This builder for chaining.  
  
### clearWeekDayOfMonth()
    
    
    public StandardSchedule.Builder clearWeekDayOfMonth()

Optional. Specifies a week day of the month like, FIRST SUNDAY or LAST MONDAY, on which jobs will run. This will be specified by two fields in `WeekDayOfMonth`, one for the day, e.g. `MONDAY`, and one for the week, e.g. `LAST`.

This field is only applicable for `recurrence_type`, `MONTHLY` and `YEARLY`. A validation error will occur if other values are supplied.

` .google.cloud.backupdr.v1beta.WeekDayOfMonth week_day_of_month = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[StandardSchedule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.StandardSchedule.Builder)` |   
  
### getBackupWindow()
    
    
    public BackupWindow getBackupWindow()

Required. A BackupWindow defines the window of day during which backup jobs will run. Jobs are queued at the beginning of the window and will be marked as `NOT_RUN` if they do not start by the end of the window.

Note: running jobs will not be cancelled at the end of the window.

` .google.cloud.backupdr.v1beta.BackupWindow backup_window = 7 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[BackupWindow](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.BackupWindow)` | The backupWindow.  
  
### getBackupWindowBuilder()
    
    
    public BackupWindow.Builder getBackupWindowBuilder()

Required. A BackupWindow defines the window of day during which backup jobs will run. Jobs are queued at the beginning of the window and will be marked as `NOT_RUN` if they do not start by the end of the window.

Note: running jobs will not be cancelled at the end of the window.

` .google.cloud.backupdr.v1beta.BackupWindow backup_window = 7 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[BackupWindow.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.BackupWindow.Builder)` |   
  
### getBackupWindowOrBuilder()
    
    
    public BackupWindowOrBuilder getBackupWindowOrBuilder()

Required. A BackupWindow defines the window of day during which backup jobs will run. Jobs are queued at the beginning of the window and will be marked as `NOT_RUN` if they do not start by the end of the window.

Note: running jobs will not be cancelled at the end of the window.

` .google.cloud.backupdr.v1beta.BackupWindow backup_window = 7 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[BackupWindowOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.BackupWindowOrBuilder)` |   
  
### getDaysOfMonth(int index)
    
    
    public int getDaysOfMonth(int index)

Optional. Specifies days of months like 1, 5, or 14 on which jobs will run.

Values for `days_of_month` are only applicable for `recurrence_type`, `MONTHLY` and `YEARLY`. A validation error will occur if other values are supplied.

`repeated int32 days_of_month = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The daysOfMonth at the given index.  
  
### getDaysOfMonthCount()
    
    
    public int getDaysOfMonthCount()

Optional. Specifies days of months like 1, 5, or 14 on which jobs will run.

Values for `days_of_month` are only applicable for `recurrence_type`, `MONTHLY` and `YEARLY`. A validation error will occur if other values are supplied.

`repeated int32 days_of_month = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of daysOfMonth.  
  
### getDaysOfMonthList()
    
    
    public List<Integer> getDaysOfMonthList()

Optional. Specifies days of months like 1, 5, or 14 on which jobs will run.

Values for `days_of_month` are only applicable for `recurrence_type`, `MONTHLY` and `YEARLY`. A validation error will occur if other values are supplied.

`repeated int32 days_of_month = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)>` | A list containing the daysOfMonth.  
  
### getDaysOfWeek(int index)
    
    
    public DayOfWeek getDaysOfWeek(int index)

Optional. Specifies days of week like, MONDAY or TUESDAY, on which jobs will run.

This is required for `recurrence_type`, `WEEKLY` and is not applicable otherwise. A validation error will occur if a value is supplied and `recurrence_type` is not `WEEKLY`.

` repeated .google.type.DayOfWeek days_of_week = 3 [(.google.api.field_behavior) = OPTIONAL]; `

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

Optional. Specifies days of week like, MONDAY or TUESDAY, on which jobs will run.

This is required for `recurrence_type`, `WEEKLY` and is not applicable otherwise. A validation error will occur if a value is supplied and `recurrence_type` is not `WEEKLY`.

` repeated .google.type.DayOfWeek days_of_week = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of daysOfWeek.  
  
### getDaysOfWeekList()
    
    
    public List<DayOfWeek> getDaysOfWeekList()

Optional. Specifies days of week like, MONDAY or TUESDAY, on which jobs will run.

This is required for `recurrence_type`, `WEEKLY` and is not applicable otherwise. A validation error will occur if a value is supplied and `recurrence_type` is not `WEEKLY`.

` repeated .google.type.DayOfWeek days_of_week = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<com.google.type.DayOfWeek>` | A list containing the daysOfWeek.  
  
### getDaysOfWeekValue(int index)
    
    
    public int getDaysOfWeekValue(int index)

Optional. Specifies days of week like, MONDAY or TUESDAY, on which jobs will run.

This is required for `recurrence_type`, `WEEKLY` and is not applicable otherwise. A validation error will occur if a value is supplied and `recurrence_type` is not `WEEKLY`.

` repeated .google.type.DayOfWeek days_of_week = 3 [(.google.api.field_behavior) = OPTIONAL]; `

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

Optional. Specifies days of week like, MONDAY or TUESDAY, on which jobs will run.

This is required for `recurrence_type`, `WEEKLY` and is not applicable otherwise. A validation error will occur if a value is supplied and `recurrence_type` is not `WEEKLY`.

` repeated .google.type.DayOfWeek days_of_week = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)>` | A list containing the enum numeric values on the wire for daysOfWeek.  
  
### getDefaultInstanceForType()
    
    
    public StandardSchedule getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[StandardSchedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.StandardSchedule)` |   
  
### getDescriptorForType()
    
    
    public Descriptors.Descriptor getDescriptorForType()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getDescriptorForType__)

### getHourlyFrequency()
    
    
    public int getHourlyFrequency()

Optional. Specifies frequency for hourly backups. A hourly frequency of 2 means jobs will run every 2 hours from start time till end time defined.

This is required for `recurrence_type`, `HOURLY` and is not applicable otherwise. A validation error will occur if a value is supplied and `recurrence_type` is not `HOURLY`.

The supported values for each resource type are as follows:

  * `compute.googleapis.com/Instance`: 1-23
  * `compute.googleapis.com/Disk`: 1-23
  * `sqladmin.googleapis.com/Instance`: 6-23
  * `alloydb.googleapis.com/Cluster`: 1-23
  * `file.googleapis.com/Instance`: 1-23

Refer to link <https://cloud.google.com/backup-disaster-recovery/docs/concepts/cloud_best_practices> for more details.




`int32 hourly_frequency = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The hourlyFrequency.  
  
### getMonths(int index)
    
    
    public Month getMonths(int index)

Optional. Specifies the months of year, like `FEBRUARY` and/or `MAY`, on which jobs will run.

This field is only applicable when `recurrence_type` is `YEARLY`. A validation error will occur if other values are supplied.

`repeated .google.type.Month months = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`com.google.type.Month` | The months at the given index.  
  
### getMonthsCount()
    
    
    public int getMonthsCount()

Optional. Specifies the months of year, like `FEBRUARY` and/or `MAY`, on which jobs will run.

This field is only applicable when `recurrence_type` is `YEARLY`. A validation error will occur if other values are supplied.

`repeated .google.type.Month months = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of months.  
  
### getMonthsList()
    
    
    public List<Month> getMonthsList()

Optional. Specifies the months of year, like `FEBRUARY` and/or `MAY`, on which jobs will run.

This field is only applicable when `recurrence_type` is `YEARLY`. A validation error will occur if other values are supplied.

`repeated .google.type.Month months = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<com.google.type.Month>` | A list containing the months.  
  
### getMonthsValue(int index)
    
    
    public int getMonthsValue(int index)

Optional. Specifies the months of year, like `FEBRUARY` and/or `MAY`, on which jobs will run.

This field is only applicable when `recurrence_type` is `YEARLY`. A validation error will occur if other values are supplied.

`repeated .google.type.Month months = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire of months at the given index.  
  
### getMonthsValueList()
    
    
    public List<Integer> getMonthsValueList()

Optional. Specifies the months of year, like `FEBRUARY` and/or `MAY`, on which jobs will run.

This field is only applicable when `recurrence_type` is `YEARLY`. A validation error will occur if other values are supplied.

`repeated .google.type.Month months = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)>` | A list containing the enum numeric values on the wire for months.  
  
### getRecurrenceType()
    
    
    public StandardSchedule.RecurrenceType getRecurrenceType()

Required. Specifies the `RecurrenceType` for the schedule.

` .google.cloud.backupdr.v1beta.StandardSchedule.RecurrenceType recurrence_type = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[StandardSchedule.RecurrenceType](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.StandardSchedule.RecurrenceType)` | The recurrenceType.  
  
### getRecurrenceTypeValue()
    
    
    public int getRecurrenceTypeValue()

Required. Specifies the `RecurrenceType` for the schedule.

` .google.cloud.backupdr.v1beta.StandardSchedule.RecurrenceType recurrence_type = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for recurrenceType.  
  
### getTimeZone()
    
    
    public String getTimeZone()

Required. The time zone to be used when interpreting the schedule. The value of this field must be a time zone name from the IANA tz database. See <https://en.wikipedia.org/wiki/List_of_tz_database_time_zones> for the list of valid timezone names. For e.g., Europe/Paris.

`string time_zone = 8 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The timeZone.  
  
### getTimeZoneBytes()
    
    
    public ByteString getTimeZoneBytes()

Required. The time zone to be used when interpreting the schedule. The value of this field must be a time zone name from the IANA tz database. See <https://en.wikipedia.org/wiki/List_of_tz_database_time_zones> for the list of valid timezone names. For e.g., Europe/Paris.

`string time_zone = 8 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for timeZone.  
  
### getWeekDayOfMonth()
    
    
    public WeekDayOfMonth getWeekDayOfMonth()

Optional. Specifies a week day of the month like, FIRST SUNDAY or LAST MONDAY, on which jobs will run. This will be specified by two fields in `WeekDayOfMonth`, one for the day, e.g. `MONDAY`, and one for the week, e.g. `LAST`.

This field is only applicable for `recurrence_type`, `MONTHLY` and `YEARLY`. A validation error will occur if other values are supplied.

` .google.cloud.backupdr.v1beta.WeekDayOfMonth week_day_of_month = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[WeekDayOfMonth](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.WeekDayOfMonth)` | The weekDayOfMonth.  
  
### getWeekDayOfMonthBuilder()
    
    
    public WeekDayOfMonth.Builder getWeekDayOfMonthBuilder()

Optional. Specifies a week day of the month like, FIRST SUNDAY or LAST MONDAY, on which jobs will run. This will be specified by two fields in `WeekDayOfMonth`, one for the day, e.g. `MONDAY`, and one for the week, e.g. `LAST`.

This field is only applicable for `recurrence_type`, `MONTHLY` and `YEARLY`. A validation error will occur if other values are supplied.

` .google.cloud.backupdr.v1beta.WeekDayOfMonth week_day_of_month = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[WeekDayOfMonth.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.WeekDayOfMonth.Builder)` |   
  
### getWeekDayOfMonthOrBuilder()
    
    
    public WeekDayOfMonthOrBuilder getWeekDayOfMonthOrBuilder()

Optional. Specifies a week day of the month like, FIRST SUNDAY or LAST MONDAY, on which jobs will run. This will be specified by two fields in `WeekDayOfMonth`, one for the day, e.g. `MONDAY`, and one for the week, e.g. `LAST`.

This field is only applicable for `recurrence_type`, `MONTHLY` and `YEARLY`. A validation error will occur if other values are supplied.

` .google.cloud.backupdr.v1beta.WeekDayOfMonth week_day_of_month = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[WeekDayOfMonthOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.WeekDayOfMonthOrBuilder)` |   
  
### hasBackupWindow()
    
    
    public boolean hasBackupWindow()

Required. A BackupWindow defines the window of day during which backup jobs will run. Jobs are queued at the beginning of the window and will be marked as `NOT_RUN` if they do not start by the end of the window.

Note: running jobs will not be cancelled at the end of the window.

` .google.cloud.backupdr.v1beta.BackupWindow backup_window = 7 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the backupWindow field is set.  
  
### hasWeekDayOfMonth()
    
    
    public boolean hasWeekDayOfMonth()

Optional. Specifies a week day of the month like, FIRST SUNDAY or LAST MONDAY, on which jobs will run. This will be specified by two fields in `WeekDayOfMonth`, one for the day, e.g. `MONDAY`, and one for the week, e.g. `LAST`.

This field is only applicable for `recurrence_type`, `MONTHLY` and `YEARLY`. A validation error will occur if other values are supplied.

` .google.cloud.backupdr.v1beta.WeekDayOfMonth week_day_of_month = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the weekDayOfMonth field is set.  
  
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

### mergeBackupWindow(BackupWindow value)
    
    
    public StandardSchedule.Builder mergeBackupWindow(BackupWindow value)

Required. A BackupWindow defines the window of day during which backup jobs will run. Jobs are queued at the beginning of the window and will be marked as `NOT_RUN` if they do not start by the end of the window.

Note: running jobs will not be cancelled at the end of the window.

` .google.cloud.backupdr.v1beta.BackupWindow backup_window = 7 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[BackupWindow](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.BackupWindow)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StandardSchedule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.StandardSchedule.Builder)` |   
  
### mergeFrom(StandardSchedule other)
    
    
    public StandardSchedule.Builder mergeFrom(StandardSchedule other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[StandardSchedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.StandardSchedule)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StandardSchedule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.StandardSchedule.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public StandardSchedule.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StandardSchedule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.StandardSchedule.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public StandardSchedule.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StandardSchedule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.StandardSchedule.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### mergeWeekDayOfMonth(WeekDayOfMonth value)
    
    
    public StandardSchedule.Builder mergeWeekDayOfMonth(WeekDayOfMonth value)

Optional. Specifies a week day of the month like, FIRST SUNDAY or LAST MONDAY, on which jobs will run. This will be specified by two fields in `WeekDayOfMonth`, one for the day, e.g. `MONDAY`, and one for the week, e.g. `LAST`.

This field is only applicable for `recurrence_type`, `MONTHLY` and `YEARLY`. A validation error will occur if other values are supplied.

` .google.cloud.backupdr.v1beta.WeekDayOfMonth week_day_of_month = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[WeekDayOfMonth](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.WeekDayOfMonth)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StandardSchedule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.StandardSchedule.Builder)` |   
  
### setBackupWindow(BackupWindow value)
    
    
    public StandardSchedule.Builder setBackupWindow(BackupWindow value)

Required. A BackupWindow defines the window of day during which backup jobs will run. Jobs are queued at the beginning of the window and will be marked as `NOT_RUN` if they do not start by the end of the window.

Note: running jobs will not be cancelled at the end of the window.

` .google.cloud.backupdr.v1beta.BackupWindow backup_window = 7 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[BackupWindow](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.BackupWindow)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StandardSchedule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.StandardSchedule.Builder)` |   
  
### setBackupWindow(BackupWindow.Builder builderForValue)
    
    
    public StandardSchedule.Builder setBackupWindow(BackupWindow.Builder builderForValue)

Required. A BackupWindow defines the window of day during which backup jobs will run. Jobs are queued at the beginning of the window and will be marked as `NOT_RUN` if they do not start by the end of the window.

Note: running jobs will not be cancelled at the end of the window.

` .google.cloud.backupdr.v1beta.BackupWindow backup_window = 7 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[BackupWindow.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.BackupWindow.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StandardSchedule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.StandardSchedule.Builder)` |   
  
### setDaysOfMonth(int index, int value)
    
    
    public StandardSchedule.Builder setDaysOfMonth(int index, int value)

Optional. Specifies days of months like 1, 5, or 14 on which jobs will run.

Values for `days_of_month` are only applicable for `recurrence_type`, `MONTHLY` and `YEARLY`. A validation error will occur if other values are supplied.

`repeated int32 days_of_month = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index to set the value at.  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The daysOfMonth to set.  
**Returns**  
---  
**Type** | **Description**  
`[StandardSchedule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.StandardSchedule.Builder)` | This builder for chaining.  
  
### setDaysOfWeek(int index, DayOfWeek value)
    
    
    public StandardSchedule.Builder setDaysOfWeek(int index, DayOfWeek value)

Optional. Specifies days of week like, MONDAY or TUESDAY, on which jobs will run.

This is required for `recurrence_type`, `WEEKLY` and is not applicable otherwise. A validation error will occur if a value is supplied and `recurrence_type` is not `WEEKLY`.

` repeated .google.type.DayOfWeek days_of_week = 3 [(.google.api.field_behavior) = OPTIONAL]; `

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
`[StandardSchedule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.StandardSchedule.Builder)` | This builder for chaining.  
  
### setDaysOfWeekValue(int index, int value)
    
    
    public StandardSchedule.Builder setDaysOfWeekValue(int index, int value)

Optional. Specifies days of week like, MONDAY or TUESDAY, on which jobs will run.

This is required for `recurrence_type`, `WEEKLY` and is not applicable otherwise. A validation error will occur if a value is supplied and `recurrence_type` is not `WEEKLY`.

` repeated .google.type.DayOfWeek days_of_week = 3 [(.google.api.field_behavior) = OPTIONAL]; `

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
`[StandardSchedule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.StandardSchedule.Builder)` | This builder for chaining.  
  
### setHourlyFrequency(int value)
    
    
    public StandardSchedule.Builder setHourlyFrequency(int value)

Optional. Specifies frequency for hourly backups. A hourly frequency of 2 means jobs will run every 2 hours from start time till end time defined.

This is required for `recurrence_type`, `HOURLY` and is not applicable otherwise. A validation error will occur if a value is supplied and `recurrence_type` is not `HOURLY`.

The supported values for each resource type are as follows:

  * `compute.googleapis.com/Instance`: 1-23
  * `compute.googleapis.com/Disk`: 1-23
  * `sqladmin.googleapis.com/Instance`: 6-23
  * `alloydb.googleapis.com/Cluster`: 1-23
  * `file.googleapis.com/Instance`: 1-23

Refer to link <https://cloud.google.com/backup-disaster-recovery/docs/concepts/cloud_best_practices> for more details.




`int32 hourly_frequency = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The hourlyFrequency to set.  
**Returns**  
---  
**Type** | **Description**  
`[StandardSchedule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.StandardSchedule.Builder)` | This builder for chaining.  
  
### setMonths(int index, Month value)
    
    
    public StandardSchedule.Builder setMonths(int index, Month value)

Optional. Specifies the months of year, like `FEBRUARY` and/or `MAY`, on which jobs will run.

This field is only applicable when `recurrence_type` is `YEARLY`. A validation error will occur if other values are supplied.

`repeated .google.type.Month months = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index to set the value at.  
`value` | `com.google.type.Month`  
The months to set.  
**Returns**  
---  
**Type** | **Description**  
`[StandardSchedule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.StandardSchedule.Builder)` | This builder for chaining.  
  
### setMonthsValue(int index, int value)
    
    
    public StandardSchedule.Builder setMonthsValue(int index, int value)

Optional. Specifies the months of year, like `FEBRUARY` and/or `MAY`, on which jobs will run.

This field is only applicable when `recurrence_type` is `YEARLY`. A validation error will occur if other values are supplied.

`repeated .google.type.Month months = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index to set the value at.  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The enum numeric value on the wire for months to set.  
**Returns**  
---  
**Type** | **Description**  
`[StandardSchedule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.StandardSchedule.Builder)` | This builder for chaining.  
  
### setRecurrenceType(StandardSchedule.RecurrenceType value)
    
    
    public StandardSchedule.Builder setRecurrenceType(StandardSchedule.RecurrenceType value)

Required. Specifies the `RecurrenceType` for the schedule.

` .google.cloud.backupdr.v1beta.StandardSchedule.RecurrenceType recurrence_type = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[StandardSchedule.RecurrenceType](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.StandardSchedule.RecurrenceType)`  
The recurrenceType to set.  
**Returns**  
---  
**Type** | **Description**  
`[StandardSchedule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.StandardSchedule.Builder)` | This builder for chaining.  
  
### setRecurrenceTypeValue(int value)
    
    
    public StandardSchedule.Builder setRecurrenceTypeValue(int value)

Required. Specifies the `RecurrenceType` for the schedule.

` .google.cloud.backupdr.v1beta.StandardSchedule.RecurrenceType recurrence_type = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The enum numeric value on the wire for recurrenceType to set.  
**Returns**  
---  
**Type** | **Description**  
`[StandardSchedule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.StandardSchedule.Builder)` | This builder for chaining.  
  
### setTimeZone(String value)
    
    
    public StandardSchedule.Builder setTimeZone(String value)

Required. The time zone to be used when interpreting the schedule. The value of this field must be a time zone name from the IANA tz database. See <https://en.wikipedia.org/wiki/List_of_tz_database_time_zones> for the list of valid timezone names. For e.g., Europe/Paris.

`string time_zone = 8 [(.google.api.field_behavior) = REQUIRED];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The timeZone to set.  
**Returns**  
---  
**Type** | **Description**  
`[StandardSchedule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.StandardSchedule.Builder)` | This builder for chaining.  
  
### setTimeZoneBytes(ByteString value)
    
    
    public StandardSchedule.Builder setTimeZoneBytes(ByteString value)

Required. The time zone to be used when interpreting the schedule. The value of this field must be a time zone name from the IANA tz database. See <https://en.wikipedia.org/wiki/List_of_tz_database_time_zones> for the list of valid timezone names. For e.g., Europe/Paris.

`string time_zone = 8 [(.google.api.field_behavior) = REQUIRED];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for timeZone to set.  
**Returns**  
---  
**Type** | **Description**  
`[StandardSchedule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.StandardSchedule.Builder)` | This builder for chaining.  
  
### setWeekDayOfMonth(WeekDayOfMonth value)
    
    
    public StandardSchedule.Builder setWeekDayOfMonth(WeekDayOfMonth value)

Optional. Specifies a week day of the month like, FIRST SUNDAY or LAST MONDAY, on which jobs will run. This will be specified by two fields in `WeekDayOfMonth`, one for the day, e.g. `MONDAY`, and one for the week, e.g. `LAST`.

This field is only applicable for `recurrence_type`, `MONTHLY` and `YEARLY`. A validation error will occur if other values are supplied.

` .google.cloud.backupdr.v1beta.WeekDayOfMonth week_day_of_month = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[WeekDayOfMonth](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.WeekDayOfMonth)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StandardSchedule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.StandardSchedule.Builder)` |   
  
### setWeekDayOfMonth(WeekDayOfMonth.Builder builderForValue)
    
    
    public StandardSchedule.Builder setWeekDayOfMonth(WeekDayOfMonth.Builder builderForValue)

Optional. Specifies a week day of the month like, FIRST SUNDAY or LAST MONDAY, on which jobs will run. This will be specified by two fields in `WeekDayOfMonth`, one for the day, e.g. `MONDAY`, and one for the week, e.g. `LAST`.

This field is only applicable for `recurrence_type`, `MONTHLY` and `YEARLY`. A validation error will occur if other values are supplied.

` .google.cloud.backupdr.v1beta.WeekDayOfMonth week_day_of_month = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[WeekDayOfMonth.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.WeekDayOfMonth.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StandardSchedule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.StandardSchedule.Builder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
