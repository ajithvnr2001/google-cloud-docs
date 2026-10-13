---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder
title: Class DailyRollupDataPoint.Builder (0.8.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:20:23.468120+00:00
---

# Class DailyRollupDataPoint.Builder (0.8.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DailyRollupDataPoint.Builder (0.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.8.0 (latest)  0.4.0  0.3.0  0.2.0 
    
    
    public static final class DailyRollupDataPoint.Builder extends GeneratedMessage.Builder<DailyRollupDataPoint.Builder> implements DailyRollupDataPointOrBuilder

Value of a daily rollup for a single civil time interval (aggregation window) of reconciled data points from all data sources, excluding those data points that are identified as recorded by wearables in intervals when they were not actually worn.

Protobuf type `google.devicesandservices.health.v4.DailyRollupDataPoint`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > DailyRollupDataPoint.Builder

## Implements

[DailyRollupDataPointOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPointOrBuilder)

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

### build()
    
    
    public DailyRollupDataPoint build()

**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint)` |   
  
### buildPartial()
    
    
    public DailyRollupDataPoint buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint)` |   
  
### clear()
    
    
    public DailyRollupDataPoint.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearActiveEnergyBurned()
    
    
    public DailyRollupDataPoint.Builder clearActiveEnergyBurned()

Returned by default when rolling up data points from the `active-energy-burned` data type.

` .google.devicesandservices.health.v4.ActiveEnergyBurnedRollupValue active_energy_burned = 27; `

**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### clearActiveMinutes()
    
    
    public DailyRollupDataPoint.Builder clearActiveMinutes()

Returned by default when rolling up data points from the `active-minutes` data type, or when requested explicitly using the `active-minutes` rollup type identifier.

`.google.devicesandservices.health.v4.ActiveMinutesRollupValue active_minutes = 24; `

**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### clearActiveZoneMinutes()
    
    
    public DailyRollupDataPoint.Builder clearActiveZoneMinutes()

Returned by default when rolling up data points from the `active-zone-minutes` data type, or when requested explicitly using the `active-zone-minutes` rollup type identifier.

` .google.devicesandservices.health.v4.ActiveZoneMinutesRollupValue active_zone_minutes = 15; `

**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### clearActivityLevel()
    
    
    public DailyRollupDataPoint.Builder clearActivityLevel()

Returned by default when rolling up data points from the `activity-level` data type, or when requested explicitly using the `activity-level` rollup type identifier.

`.google.devicesandservices.health.v4.ActivityLevelRollupValue activity_level = 20; `

**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### clearAltitude()
    
    
    public DailyRollupDataPoint.Builder clearAltitude()

Returned by default when rolling up data points from the `altitude` data type, or when requested explicitly using the `altitude` rollup type identifier.

`.google.devicesandservices.health.v4.AltitudeRollupValue altitude = 11;`

**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### clearBloodGlucose()
    
    
    public DailyRollupDataPoint.Builder clearBloodGlucose()

Returned by default when rolling up data points from the `blood-glucose` data type.

`.google.devicesandservices.health.v4.BloodGlucoseRollupValue blood_glucose = 28;`

**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### clearBodyFat()
    
    
    public DailyRollupDataPoint.Builder clearBodyFat()

Returned by default when rolling up data points from the `body-fat` data type, or when requested explicitly using the `body-fat` rollup type identifier.

`.google.devicesandservices.health.v4.BodyFatRollupValue body_fat = 13;`

**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### clearCaloriesInHeartRateZone()
    
    
    public DailyRollupDataPoint.Builder clearCaloriesInHeartRateZone()

Returned by default when rolling up data points from the `calories-in-heart-rate-zone` data type, or when requested explicitly using the `calories-in-heart-rate-zone` rollup type identifier.

` .google.devicesandservices.health.v4.CaloriesInHeartRateZoneRollupValue calories_in_heart_rate_zone = 19; `

**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### clearCivilEndTime()
    
    
    public DailyRollupDataPoint.Builder clearCivilEndTime()

End time of the window this value aggregates over

`.google.devicesandservices.health.v4.CivilDateTime civil_end_time = 2;`

**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### clearCivilStartTime()
    
    
    public DailyRollupDataPoint.Builder clearCivilStartTime()

Start time of the window this value aggregates over

`.google.devicesandservices.health.v4.CivilDateTime civil_start_time = 1;`

**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### clearCoreBodyTemperature()
    
    
    public DailyRollupDataPoint.Builder clearCoreBodyTemperature()

Returned by default when rolling up data points from the `core-body-temperature` data type, or when requested explicitly using the `core-body-temperature` rollup type identifier.

` .google.devicesandservices.health.v4.CoreBodyTemperatureRollupValue core_body_temperature = 26; `

**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### clearDistance()
    
    
    public DailyRollupDataPoint.Builder clearDistance()

Returned by default when rolling up data points from the `distance` data type, or when requested explicitly using the `distance` rollup type identifier.

`.google.devicesandservices.health.v4.DistanceRollupValue distance = 12;`

**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### clearFloors()
    
    
    public DailyRollupDataPoint.Builder clearFloors()

Returned by default when rolling up data points from the `floors` data type, or when requested explicitly using the `floors` rollup type identifier.

`.google.devicesandservices.health.v4.FloorsRollupValue floors = 6;`

**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### clearHeartRate()
    
    
    public DailyRollupDataPoint.Builder clearHeartRate()

Returned by default when rolling up data points from the `heart-rate` data type, or when requested explicitly using the `heart-rate` rollup type identifier.

`.google.devicesandservices.health.v4.HeartRateRollupValue heart_rate = 7;`

**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### clearHeartRateVariabilityPersonalRange()
    
    
    public DailyRollupDataPoint.Builder clearHeartRateVariabilityPersonalRange()

Returned by default when rolling up data points from the `daily-heart-rate-variability` data type, or when requested explicitly using the `heart-rate-variability-personal-range` rollup type identifier.

` .google.devicesandservices.health.v4.HeartRateVariabilityPersonalRangeRollupValue heart_rate_variability_personal_range = 9; `

**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### clearHydrationLog()
    
    
    public DailyRollupDataPoint.Builder clearHydrationLog()

Returned by default when rolling up data points from the `hydration-log` data type, or when requested explicitly using the `hydration-log` rollup type identifier.

`.google.devicesandservices.health.v4.HydrationLogRollupValue hydration_log = 22;`

**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### clearNutritionLog()
    
    
    public DailyRollupDataPoint.Builder clearNutritionLog()

Returned by default when rolling up data points from the `nutrition-log` data type, or when requested explicitly using the `nutrition-log` rollup type identifier.

`.google.devicesandservices.health.v4.NutritionLogRollupValue nutrition_log = 21;`

**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### clearRestingHeartRatePersonalRange()
    
    
    public DailyRollupDataPoint.Builder clearRestingHeartRatePersonalRange()

Returned by default when rolling up data points from the `daily-resting-heart-rate` data type, or when requested explicitly using the `resting-heart-rate-personal-range` rollup type identifier.

` .google.devicesandservices.health.v4.RestingHeartRatePersonalRangeRollupValue resting_heart_rate_personal_range = 8; `

**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### clearRunVo2Max()
    
    
    public DailyRollupDataPoint.Builder clearRunVo2Max()

Returned by default when rolling up data points from the `run-vo2-max` data type, or when requested explicitly using the `run-vo2-max` rollup type identifier.

`.google.devicesandservices.health.v4.RunVO2MaxRollupValue run_vo2_max = 18;`

**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### clearSedentaryPeriod()
    
    
    public DailyRollupDataPoint.Builder clearSedentaryPeriod()

Returned by default when rolling up data points from the `sedentary-period` data type, or when requested explicitly using the `sedentary-period` rollup type identifier.

`.google.devicesandservices.health.v4.SedentaryPeriodRollupValue sedentary_period = 17; `

**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### clearSteps()
    
    
    public DailyRollupDataPoint.Builder clearSteps()

Returned by default when rolling up data points from the `steps` data type, or when requested explicitly using the `steps` rollup type identifier.

`.google.devicesandservices.health.v4.StepsRollupValue steps = 5;`

**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### clearSwimLengthsData()
    
    
    public DailyRollupDataPoint.Builder clearSwimLengthsData()

Returned by default when rolling up data points from the `swim-lengths-data` data type, or when requested explicitly using the `swim-lengths-data` rollup type identifier.

`.google.devicesandservices.health.v4.SwimLengthsDataRollupValue swim_lengths_data = 25; `

**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### clearTimeInHeartRateZone()
    
    
    public DailyRollupDataPoint.Builder clearTimeInHeartRateZone()

Returned by default when rolling up data points from the `time-in-heart-rate-zone` data type, or when requested explicitly using the `time-in-heart-rate-zone` rollup type identifier.

` .google.devicesandservices.health.v4.TimeInHeartRateZoneRollupValue time_in_heart_rate_zone = 23; `

**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### clearTotalCalories()
    
    
    public DailyRollupDataPoint.Builder clearTotalCalories()

Returned by default when rolling up data points from the `total-calories` data type, or when requested explicitly using the `total-calories` rollup type identifier.

`.google.devicesandservices.health.v4.TotalCaloriesRollupValue total_calories = 14; `

**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### clearValue()
    
    
    public DailyRollupDataPoint.Builder clearValue()

**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### clearWeight()
    
    
    public DailyRollupDataPoint.Builder clearWeight()

Returned by default when rolling up data points from the `weight` data type, or when requested explicitly using the `weight` rollup type identifier.

`.google.devicesandservices.health.v4.WeightRollupValue weight = 10;`

**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### getActiveEnergyBurned()
    
    
    public ActiveEnergyBurnedRollupValue getActiveEnergyBurned()

Returned by default when rolling up data points from the `active-energy-burned` data type.

` .google.devicesandservices.health.v4.ActiveEnergyBurnedRollupValue active_energy_burned = 27; `

**Returns**  
---  
**Type** | **Description**  
`[ActiveEnergyBurnedRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ActiveEnergyBurnedRollupValue)` | The activeEnergyBurned.  
  
### getActiveEnergyBurnedBuilder()
    
    
    public ActiveEnergyBurnedRollupValue.Builder getActiveEnergyBurnedBuilder()

Returned by default when rolling up data points from the `active-energy-burned` data type.

` .google.devicesandservices.health.v4.ActiveEnergyBurnedRollupValue active_energy_burned = 27; `

**Returns**  
---  
**Type** | **Description**  
`[ActiveEnergyBurnedRollupValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ActiveEnergyBurnedRollupValue.Builder)` |   
  
### getActiveEnergyBurnedOrBuilder()
    
    
    public ActiveEnergyBurnedRollupValueOrBuilder getActiveEnergyBurnedOrBuilder()

Returned by default when rolling up data points from the `active-energy-burned` data type.

` .google.devicesandservices.health.v4.ActiveEnergyBurnedRollupValue active_energy_burned = 27; `

**Returns**  
---  
**Type** | **Description**  
`[ActiveEnergyBurnedRollupValueOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ActiveEnergyBurnedRollupValueOrBuilder)` |   
  
### getActiveMinutes()
    
    
    public ActiveMinutesRollupValue getActiveMinutes()

Returned by default when rolling up data points from the `active-minutes` data type, or when requested explicitly using the `active-minutes` rollup type identifier.

`.google.devicesandservices.health.v4.ActiveMinutesRollupValue active_minutes = 24; `

**Returns**  
---  
**Type** | **Description**  
`[ActiveMinutesRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ActiveMinutesRollupValue)` | The activeMinutes.  
  
### getActiveMinutesBuilder()
    
    
    public ActiveMinutesRollupValue.Builder getActiveMinutesBuilder()

Returned by default when rolling up data points from the `active-minutes` data type, or when requested explicitly using the `active-minutes` rollup type identifier.

`.google.devicesandservices.health.v4.ActiveMinutesRollupValue active_minutes = 24; `

**Returns**  
---  
**Type** | **Description**  
`[ActiveMinutesRollupValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ActiveMinutesRollupValue.Builder)` |   
  
### getActiveMinutesOrBuilder()
    
    
    public ActiveMinutesRollupValueOrBuilder getActiveMinutesOrBuilder()

Returned by default when rolling up data points from the `active-minutes` data type, or when requested explicitly using the `active-minutes` rollup type identifier.

`.google.devicesandservices.health.v4.ActiveMinutesRollupValue active_minutes = 24; `

**Returns**  
---  
**Type** | **Description**  
`[ActiveMinutesRollupValueOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ActiveMinutesRollupValueOrBuilder)` |   
  
### getActiveZoneMinutes()
    
    
    public ActiveZoneMinutesRollupValue getActiveZoneMinutes()

Returned by default when rolling up data points from the `active-zone-minutes` data type, or when requested explicitly using the `active-zone-minutes` rollup type identifier.

` .google.devicesandservices.health.v4.ActiveZoneMinutesRollupValue active_zone_minutes = 15; `

**Returns**  
---  
**Type** | **Description**  
`[ActiveZoneMinutesRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ActiveZoneMinutesRollupValue)` | The activeZoneMinutes.  
  
### getActiveZoneMinutesBuilder()
    
    
    public ActiveZoneMinutesRollupValue.Builder getActiveZoneMinutesBuilder()

Returned by default when rolling up data points from the `active-zone-minutes` data type, or when requested explicitly using the `active-zone-minutes` rollup type identifier.

` .google.devicesandservices.health.v4.ActiveZoneMinutesRollupValue active_zone_minutes = 15; `

**Returns**  
---  
**Type** | **Description**  
`[ActiveZoneMinutesRollupValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ActiveZoneMinutesRollupValue.Builder)` |   
  
### getActiveZoneMinutesOrBuilder()
    
    
    public ActiveZoneMinutesRollupValueOrBuilder getActiveZoneMinutesOrBuilder()

Returned by default when rolling up data points from the `active-zone-minutes` data type, or when requested explicitly using the `active-zone-minutes` rollup type identifier.

` .google.devicesandservices.health.v4.ActiveZoneMinutesRollupValue active_zone_minutes = 15; `

**Returns**  
---  
**Type** | **Description**  
`[ActiveZoneMinutesRollupValueOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ActiveZoneMinutesRollupValueOrBuilder)` |   
  
### getActivityLevel()
    
    
    public ActivityLevelRollupValue getActivityLevel()

Returned by default when rolling up data points from the `activity-level` data type, or when requested explicitly using the `activity-level` rollup type identifier.

`.google.devicesandservices.health.v4.ActivityLevelRollupValue activity_level = 20; `

**Returns**  
---  
**Type** | **Description**  
`[ActivityLevelRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ActivityLevelRollupValue)` | The activityLevel.  
  
### getActivityLevelBuilder()
    
    
    public ActivityLevelRollupValue.Builder getActivityLevelBuilder()

Returned by default when rolling up data points from the `activity-level` data type, or when requested explicitly using the `activity-level` rollup type identifier.

`.google.devicesandservices.health.v4.ActivityLevelRollupValue activity_level = 20; `

**Returns**  
---  
**Type** | **Description**  
`[ActivityLevelRollupValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ActivityLevelRollupValue.Builder)` |   
  
### getActivityLevelOrBuilder()
    
    
    public ActivityLevelRollupValueOrBuilder getActivityLevelOrBuilder()

Returned by default when rolling up data points from the `activity-level` data type, or when requested explicitly using the `activity-level` rollup type identifier.

`.google.devicesandservices.health.v4.ActivityLevelRollupValue activity_level = 20; `

**Returns**  
---  
**Type** | **Description**  
`[ActivityLevelRollupValueOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ActivityLevelRollupValueOrBuilder)` |   
  
### getAltitude()
    
    
    public AltitudeRollupValue getAltitude()

Returned by default when rolling up data points from the `altitude` data type, or when requested explicitly using the `altitude` rollup type identifier.

`.google.devicesandservices.health.v4.AltitudeRollupValue altitude = 11;`

**Returns**  
---  
**Type** | **Description**  
`[AltitudeRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.AltitudeRollupValue)` | The altitude.  
  
### getAltitudeBuilder()
    
    
    public AltitudeRollupValue.Builder getAltitudeBuilder()

Returned by default when rolling up data points from the `altitude` data type, or when requested explicitly using the `altitude` rollup type identifier.

`.google.devicesandservices.health.v4.AltitudeRollupValue altitude = 11;`

**Returns**  
---  
**Type** | **Description**  
`[AltitudeRollupValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.AltitudeRollupValue.Builder)` |   
  
### getAltitudeOrBuilder()
    
    
    public AltitudeRollupValueOrBuilder getAltitudeOrBuilder()

Returned by default when rolling up data points from the `altitude` data type, or when requested explicitly using the `altitude` rollup type identifier.

`.google.devicesandservices.health.v4.AltitudeRollupValue altitude = 11;`

**Returns**  
---  
**Type** | **Description**  
`[AltitudeRollupValueOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.AltitudeRollupValueOrBuilder)` |   
  
### getBloodGlucose()
    
    
    public BloodGlucoseRollupValue getBloodGlucose()

Returned by default when rolling up data points from the `blood-glucose` data type.

`.google.devicesandservices.health.v4.BloodGlucoseRollupValue blood_glucose = 28;`

**Returns**  
---  
**Type** | **Description**  
`[BloodGlucoseRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.BloodGlucoseRollupValue)` | The bloodGlucose.  
  
### getBloodGlucoseBuilder()
    
    
    public BloodGlucoseRollupValue.Builder getBloodGlucoseBuilder()

Returned by default when rolling up data points from the `blood-glucose` data type.

`.google.devicesandservices.health.v4.BloodGlucoseRollupValue blood_glucose = 28;`

**Returns**  
---  
**Type** | **Description**  
`[BloodGlucoseRollupValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.BloodGlucoseRollupValue.Builder)` |   
  
### getBloodGlucoseOrBuilder()
    
    
    public BloodGlucoseRollupValueOrBuilder getBloodGlucoseOrBuilder()

Returned by default when rolling up data points from the `blood-glucose` data type.

`.google.devicesandservices.health.v4.BloodGlucoseRollupValue blood_glucose = 28;`

**Returns**  
---  
**Type** | **Description**  
`[BloodGlucoseRollupValueOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.BloodGlucoseRollupValueOrBuilder)` |   
  
### getBodyFat()
    
    
    public BodyFatRollupValue getBodyFat()

Returned by default when rolling up data points from the `body-fat` data type, or when requested explicitly using the `body-fat` rollup type identifier.

`.google.devicesandservices.health.v4.BodyFatRollupValue body_fat = 13;`

**Returns**  
---  
**Type** | **Description**  
`[BodyFatRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.BodyFatRollupValue)` | The bodyFat.  
  
### getBodyFatBuilder()
    
    
    public BodyFatRollupValue.Builder getBodyFatBuilder()

Returned by default when rolling up data points from the `body-fat` data type, or when requested explicitly using the `body-fat` rollup type identifier.

`.google.devicesandservices.health.v4.BodyFatRollupValue body_fat = 13;`

**Returns**  
---  
**Type** | **Description**  
`[BodyFatRollupValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.BodyFatRollupValue.Builder)` |   
  
### getBodyFatOrBuilder()
    
    
    public BodyFatRollupValueOrBuilder getBodyFatOrBuilder()

Returned by default when rolling up data points from the `body-fat` data type, or when requested explicitly using the `body-fat` rollup type identifier.

`.google.devicesandservices.health.v4.BodyFatRollupValue body_fat = 13;`

**Returns**  
---  
**Type** | **Description**  
`[BodyFatRollupValueOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.BodyFatRollupValueOrBuilder)` |   
  
### getCaloriesInHeartRateZone()
    
    
    public CaloriesInHeartRateZoneRollupValue getCaloriesInHeartRateZone()

Returned by default when rolling up data points from the `calories-in-heart-rate-zone` data type, or when requested explicitly using the `calories-in-heart-rate-zone` rollup type identifier.

` .google.devicesandservices.health.v4.CaloriesInHeartRateZoneRollupValue calories_in_heart_rate_zone = 19; `

**Returns**  
---  
**Type** | **Description**  
`[CaloriesInHeartRateZoneRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CaloriesInHeartRateZoneRollupValue)` | The caloriesInHeartRateZone.  
  
### getCaloriesInHeartRateZoneBuilder()
    
    
    public CaloriesInHeartRateZoneRollupValue.Builder getCaloriesInHeartRateZoneBuilder()

Returned by default when rolling up data points from the `calories-in-heart-rate-zone` data type, or when requested explicitly using the `calories-in-heart-rate-zone` rollup type identifier.

` .google.devicesandservices.health.v4.CaloriesInHeartRateZoneRollupValue calories_in_heart_rate_zone = 19; `

**Returns**  
---  
**Type** | **Description**  
`[CaloriesInHeartRateZoneRollupValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CaloriesInHeartRateZoneRollupValue.Builder)` |   
  
### getCaloriesInHeartRateZoneOrBuilder()
    
    
    public CaloriesInHeartRateZoneRollupValueOrBuilder getCaloriesInHeartRateZoneOrBuilder()

Returned by default when rolling up data points from the `calories-in-heart-rate-zone` data type, or when requested explicitly using the `calories-in-heart-rate-zone` rollup type identifier.

` .google.devicesandservices.health.v4.CaloriesInHeartRateZoneRollupValue calories_in_heart_rate_zone = 19; `

**Returns**  
---  
**Type** | **Description**  
`[CaloriesInHeartRateZoneRollupValueOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CaloriesInHeartRateZoneRollupValueOrBuilder)` |   
  
### getCivilEndTime()
    
    
    public CivilDateTime getCivilEndTime()

End time of the window this value aggregates over

`.google.devicesandservices.health.v4.CivilDateTime civil_end_time = 2;`

**Returns**  
---  
**Type** | **Description**  
`[CivilDateTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CivilDateTime)` | The civilEndTime.  
  
### getCivilEndTimeBuilder()
    
    
    public CivilDateTime.Builder getCivilEndTimeBuilder()

End time of the window this value aggregates over

`.google.devicesandservices.health.v4.CivilDateTime civil_end_time = 2;`

**Returns**  
---  
**Type** | **Description**  
`[CivilDateTime.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CivilDateTime.Builder)` |   
  
### getCivilEndTimeOrBuilder()
    
    
    public CivilDateTimeOrBuilder getCivilEndTimeOrBuilder()

End time of the window this value aggregates over

`.google.devicesandservices.health.v4.CivilDateTime civil_end_time = 2;`

**Returns**  
---  
**Type** | **Description**  
`[CivilDateTimeOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CivilDateTimeOrBuilder)` |   
  
### getCivilStartTime()
    
    
    public CivilDateTime getCivilStartTime()

Start time of the window this value aggregates over

`.google.devicesandservices.health.v4.CivilDateTime civil_start_time = 1;`

**Returns**  
---  
**Type** | **Description**  
`[CivilDateTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CivilDateTime)` | The civilStartTime.  
  
### getCivilStartTimeBuilder()
    
    
    public CivilDateTime.Builder getCivilStartTimeBuilder()

Start time of the window this value aggregates over

`.google.devicesandservices.health.v4.CivilDateTime civil_start_time = 1;`

**Returns**  
---  
**Type** | **Description**  
`[CivilDateTime.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CivilDateTime.Builder)` |   
  
### getCivilStartTimeOrBuilder()
    
    
    public CivilDateTimeOrBuilder getCivilStartTimeOrBuilder()

Start time of the window this value aggregates over

`.google.devicesandservices.health.v4.CivilDateTime civil_start_time = 1;`

**Returns**  
---  
**Type** | **Description**  
`[CivilDateTimeOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CivilDateTimeOrBuilder)` |   
  
### getCoreBodyTemperature()
    
    
    public CoreBodyTemperatureRollupValue getCoreBodyTemperature()

Returned by default when rolling up data points from the `core-body-temperature` data type, or when requested explicitly using the `core-body-temperature` rollup type identifier.

` .google.devicesandservices.health.v4.CoreBodyTemperatureRollupValue core_body_temperature = 26; `

**Returns**  
---  
**Type** | **Description**  
`[CoreBodyTemperatureRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CoreBodyTemperatureRollupValue)` | The coreBodyTemperature.  
  
### getCoreBodyTemperatureBuilder()
    
    
    public CoreBodyTemperatureRollupValue.Builder getCoreBodyTemperatureBuilder()

Returned by default when rolling up data points from the `core-body-temperature` data type, or when requested explicitly using the `core-body-temperature` rollup type identifier.

` .google.devicesandservices.health.v4.CoreBodyTemperatureRollupValue core_body_temperature = 26; `

**Returns**  
---  
**Type** | **Description**  
`[CoreBodyTemperatureRollupValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CoreBodyTemperatureRollupValue.Builder)` |   
  
### getCoreBodyTemperatureOrBuilder()
    
    
    public CoreBodyTemperatureRollupValueOrBuilder getCoreBodyTemperatureOrBuilder()

Returned by default when rolling up data points from the `core-body-temperature` data type, or when requested explicitly using the `core-body-temperature` rollup type identifier.

` .google.devicesandservices.health.v4.CoreBodyTemperatureRollupValue core_body_temperature = 26; `

**Returns**  
---  
**Type** | **Description**  
`[CoreBodyTemperatureRollupValueOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CoreBodyTemperatureRollupValueOrBuilder)` |   
  
### getDefaultInstanceForType()
    
    
    public DailyRollupDataPoint getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint)` |   
  
### getDescriptorForType()
    
    
    public Descriptors.Descriptor getDescriptorForType()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getDescriptorForType__)

### getDistance()
    
    
    public DistanceRollupValue getDistance()

Returned by default when rolling up data points from the `distance` data type, or when requested explicitly using the `distance` rollup type identifier.

`.google.devicesandservices.health.v4.DistanceRollupValue distance = 12;`

**Returns**  
---  
**Type** | **Description**  
`[DistanceRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DistanceRollupValue)` | The distance.  
  
### getDistanceBuilder()
    
    
    public DistanceRollupValue.Builder getDistanceBuilder()

Returned by default when rolling up data points from the `distance` data type, or when requested explicitly using the `distance` rollup type identifier.

`.google.devicesandservices.health.v4.DistanceRollupValue distance = 12;`

**Returns**  
---  
**Type** | **Description**  
`[DistanceRollupValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DistanceRollupValue.Builder)` |   
  
### getDistanceOrBuilder()
    
    
    public DistanceRollupValueOrBuilder getDistanceOrBuilder()

Returned by default when rolling up data points from the `distance` data type, or when requested explicitly using the `distance` rollup type identifier.

`.google.devicesandservices.health.v4.DistanceRollupValue distance = 12;`

**Returns**  
---  
**Type** | **Description**  
`[DistanceRollupValueOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DistanceRollupValueOrBuilder)` |   
  
### getFloors()
    
    
    public FloorsRollupValue getFloors()

Returned by default when rolling up data points from the `floors` data type, or when requested explicitly using the `floors` rollup type identifier.

`.google.devicesandservices.health.v4.FloorsRollupValue floors = 6;`

**Returns**  
---  
**Type** | **Description**  
`[FloorsRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.FloorsRollupValue)` | The floors.  
  
### getFloorsBuilder()
    
    
    public FloorsRollupValue.Builder getFloorsBuilder()

Returned by default when rolling up data points from the `floors` data type, or when requested explicitly using the `floors` rollup type identifier.

`.google.devicesandservices.health.v4.FloorsRollupValue floors = 6;`

**Returns**  
---  
**Type** | **Description**  
`[FloorsRollupValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.FloorsRollupValue.Builder)` |   
  
### getFloorsOrBuilder()
    
    
    public FloorsRollupValueOrBuilder getFloorsOrBuilder()

Returned by default when rolling up data points from the `floors` data type, or when requested explicitly using the `floors` rollup type identifier.

`.google.devicesandservices.health.v4.FloorsRollupValue floors = 6;`

**Returns**  
---  
**Type** | **Description**  
`[FloorsRollupValueOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.FloorsRollupValueOrBuilder)` |   
  
### getHeartRate()
    
    
    public HeartRateRollupValue getHeartRate()

Returned by default when rolling up data points from the `heart-rate` data type, or when requested explicitly using the `heart-rate` rollup type identifier.

`.google.devicesandservices.health.v4.HeartRateRollupValue heart_rate = 7;`

**Returns**  
---  
**Type** | **Description**  
`[HeartRateRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.HeartRateRollupValue)` | The heartRate.  
  
### getHeartRateBuilder()
    
    
    public HeartRateRollupValue.Builder getHeartRateBuilder()

Returned by default when rolling up data points from the `heart-rate` data type, or when requested explicitly using the `heart-rate` rollup type identifier.

`.google.devicesandservices.health.v4.HeartRateRollupValue heart_rate = 7;`

**Returns**  
---  
**Type** | **Description**  
`[HeartRateRollupValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.HeartRateRollupValue.Builder)` |   
  
### getHeartRateOrBuilder()
    
    
    public HeartRateRollupValueOrBuilder getHeartRateOrBuilder()

Returned by default when rolling up data points from the `heart-rate` data type, or when requested explicitly using the `heart-rate` rollup type identifier.

`.google.devicesandservices.health.v4.HeartRateRollupValue heart_rate = 7;`

**Returns**  
---  
**Type** | **Description**  
`[HeartRateRollupValueOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.HeartRateRollupValueOrBuilder)` |   
  
### getHeartRateVariabilityPersonalRange()
    
    
    public HeartRateVariabilityPersonalRangeRollupValue getHeartRateVariabilityPersonalRange()

Returned by default when rolling up data points from the `daily-heart-rate-variability` data type, or when requested explicitly using the `heart-rate-variability-personal-range` rollup type identifier.

` .google.devicesandservices.health.v4.HeartRateVariabilityPersonalRangeRollupValue heart_rate_variability_personal_range = 9; `

**Returns**  
---  
**Type** | **Description**  
`[HeartRateVariabilityPersonalRangeRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.HeartRateVariabilityPersonalRangeRollupValue)` | The heartRateVariabilityPersonalRange.  
  
### getHeartRateVariabilityPersonalRangeBuilder()
    
    
    public HeartRateVariabilityPersonalRangeRollupValue.Builder getHeartRateVariabilityPersonalRangeBuilder()

Returned by default when rolling up data points from the `daily-heart-rate-variability` data type, or when requested explicitly using the `heart-rate-variability-personal-range` rollup type identifier.

` .google.devicesandservices.health.v4.HeartRateVariabilityPersonalRangeRollupValue heart_rate_variability_personal_range = 9; `

**Returns**  
---  
**Type** | **Description**  
`[HeartRateVariabilityPersonalRangeRollupValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.HeartRateVariabilityPersonalRangeRollupValue.Builder)` |   
  
### getHeartRateVariabilityPersonalRangeOrBuilder()
    
    
    public HeartRateVariabilityPersonalRangeRollupValueOrBuilder getHeartRateVariabilityPersonalRangeOrBuilder()

Returned by default when rolling up data points from the `daily-heart-rate-variability` data type, or when requested explicitly using the `heart-rate-variability-personal-range` rollup type identifier.

` .google.devicesandservices.health.v4.HeartRateVariabilityPersonalRangeRollupValue heart_rate_variability_personal_range = 9; `

**Returns**  
---  
**Type** | **Description**  
`[HeartRateVariabilityPersonalRangeRollupValueOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.HeartRateVariabilityPersonalRangeRollupValueOrBuilder)` |   
  
### getHydrationLog()
    
    
    public HydrationLogRollupValue getHydrationLog()

Returned by default when rolling up data points from the `hydration-log` data type, or when requested explicitly using the `hydration-log` rollup type identifier.

`.google.devicesandservices.health.v4.HydrationLogRollupValue hydration_log = 22;`

**Returns**  
---  
**Type** | **Description**  
`[HydrationLogRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.HydrationLogRollupValue)` | The hydrationLog.  
  
### getHydrationLogBuilder()
    
    
    public HydrationLogRollupValue.Builder getHydrationLogBuilder()

Returned by default when rolling up data points from the `hydration-log` data type, or when requested explicitly using the `hydration-log` rollup type identifier.

`.google.devicesandservices.health.v4.HydrationLogRollupValue hydration_log = 22;`

**Returns**  
---  
**Type** | **Description**  
`[HydrationLogRollupValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.HydrationLogRollupValue.Builder)` |   
  
### getHydrationLogOrBuilder()
    
    
    public HydrationLogRollupValueOrBuilder getHydrationLogOrBuilder()

Returned by default when rolling up data points from the `hydration-log` data type, or when requested explicitly using the `hydration-log` rollup type identifier.

`.google.devicesandservices.health.v4.HydrationLogRollupValue hydration_log = 22;`

**Returns**  
---  
**Type** | **Description**  
`[HydrationLogRollupValueOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.HydrationLogRollupValueOrBuilder)` |   
  
### getNutritionLog()
    
    
    public NutritionLogRollupValue getNutritionLog()

Returned by default when rolling up data points from the `nutrition-log` data type, or when requested explicitly using the `nutrition-log` rollup type identifier.

`.google.devicesandservices.health.v4.NutritionLogRollupValue nutrition_log = 21;`

**Returns**  
---  
**Type** | **Description**  
`[NutritionLogRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.NutritionLogRollupValue)` | The nutritionLog.  
  
### getNutritionLogBuilder()
    
    
    public NutritionLogRollupValue.Builder getNutritionLogBuilder()

Returned by default when rolling up data points from the `nutrition-log` data type, or when requested explicitly using the `nutrition-log` rollup type identifier.

`.google.devicesandservices.health.v4.NutritionLogRollupValue nutrition_log = 21;`

**Returns**  
---  
**Type** | **Description**  
`[NutritionLogRollupValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.NutritionLogRollupValue.Builder)` |   
  
### getNutritionLogOrBuilder()
    
    
    public NutritionLogRollupValueOrBuilder getNutritionLogOrBuilder()

Returned by default when rolling up data points from the `nutrition-log` data type, or when requested explicitly using the `nutrition-log` rollup type identifier.

`.google.devicesandservices.health.v4.NutritionLogRollupValue nutrition_log = 21;`

**Returns**  
---  
**Type** | **Description**  
`[NutritionLogRollupValueOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.NutritionLogRollupValueOrBuilder)` |   
  
### getRestingHeartRatePersonalRange()
    
    
    public RestingHeartRatePersonalRangeRollupValue getRestingHeartRatePersonalRange()

Returned by default when rolling up data points from the `daily-resting-heart-rate` data type, or when requested explicitly using the `resting-heart-rate-personal-range` rollup type identifier.

` .google.devicesandservices.health.v4.RestingHeartRatePersonalRangeRollupValue resting_heart_rate_personal_range = 8; `

**Returns**  
---  
**Type** | **Description**  
`[RestingHeartRatePersonalRangeRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.RestingHeartRatePersonalRangeRollupValue)` | The restingHeartRatePersonalRange.  
  
### getRestingHeartRatePersonalRangeBuilder()
    
    
    public RestingHeartRatePersonalRangeRollupValue.Builder getRestingHeartRatePersonalRangeBuilder()

Returned by default when rolling up data points from the `daily-resting-heart-rate` data type, or when requested explicitly using the `resting-heart-rate-personal-range` rollup type identifier.

` .google.devicesandservices.health.v4.RestingHeartRatePersonalRangeRollupValue resting_heart_rate_personal_range = 8; `

**Returns**  
---  
**Type** | **Description**  
`[RestingHeartRatePersonalRangeRollupValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.RestingHeartRatePersonalRangeRollupValue.Builder)` |   
  
### getRestingHeartRatePersonalRangeOrBuilder()
    
    
    public RestingHeartRatePersonalRangeRollupValueOrBuilder getRestingHeartRatePersonalRangeOrBuilder()

Returned by default when rolling up data points from the `daily-resting-heart-rate` data type, or when requested explicitly using the `resting-heart-rate-personal-range` rollup type identifier.

` .google.devicesandservices.health.v4.RestingHeartRatePersonalRangeRollupValue resting_heart_rate_personal_range = 8; `

**Returns**  
---  
**Type** | **Description**  
`[RestingHeartRatePersonalRangeRollupValueOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.RestingHeartRatePersonalRangeRollupValueOrBuilder)` |   
  
### getRunVo2Max()
    
    
    public RunVO2MaxRollupValue getRunVo2Max()

Returned by default when rolling up data points from the `run-vo2-max` data type, or when requested explicitly using the `run-vo2-max` rollup type identifier.

`.google.devicesandservices.health.v4.RunVO2MaxRollupValue run_vo2_max = 18;`

**Returns**  
---  
**Type** | **Description**  
`[RunVO2MaxRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.RunVO2MaxRollupValue)` | The runVo2Max.  
  
### getRunVo2MaxBuilder()
    
    
    public RunVO2MaxRollupValue.Builder getRunVo2MaxBuilder()

Returned by default when rolling up data points from the `run-vo2-max` data type, or when requested explicitly using the `run-vo2-max` rollup type identifier.

`.google.devicesandservices.health.v4.RunVO2MaxRollupValue run_vo2_max = 18;`

**Returns**  
---  
**Type** | **Description**  
`[RunVO2MaxRollupValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.RunVO2MaxRollupValue.Builder)` |   
  
### getRunVo2MaxOrBuilder()
    
    
    public RunVO2MaxRollupValueOrBuilder getRunVo2MaxOrBuilder()

Returned by default when rolling up data points from the `run-vo2-max` data type, or when requested explicitly using the `run-vo2-max` rollup type identifier.

`.google.devicesandservices.health.v4.RunVO2MaxRollupValue run_vo2_max = 18;`

**Returns**  
---  
**Type** | **Description**  
`[RunVO2MaxRollupValueOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.RunVO2MaxRollupValueOrBuilder)` |   
  
### getSedentaryPeriod()
    
    
    public SedentaryPeriodRollupValue getSedentaryPeriod()

Returned by default when rolling up data points from the `sedentary-period` data type, or when requested explicitly using the `sedentary-period` rollup type identifier.

`.google.devicesandservices.health.v4.SedentaryPeriodRollupValue sedentary_period = 17; `

**Returns**  
---  
**Type** | **Description**  
`[SedentaryPeriodRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.SedentaryPeriodRollupValue)` | The sedentaryPeriod.  
  
### getSedentaryPeriodBuilder()
    
    
    public SedentaryPeriodRollupValue.Builder getSedentaryPeriodBuilder()

Returned by default when rolling up data points from the `sedentary-period` data type, or when requested explicitly using the `sedentary-period` rollup type identifier.

`.google.devicesandservices.health.v4.SedentaryPeriodRollupValue sedentary_period = 17; `

**Returns**  
---  
**Type** | **Description**  
`[SedentaryPeriodRollupValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.SedentaryPeriodRollupValue.Builder)` |   
  
### getSedentaryPeriodOrBuilder()
    
    
    public SedentaryPeriodRollupValueOrBuilder getSedentaryPeriodOrBuilder()

Returned by default when rolling up data points from the `sedentary-period` data type, or when requested explicitly using the `sedentary-period` rollup type identifier.

`.google.devicesandservices.health.v4.SedentaryPeriodRollupValue sedentary_period = 17; `

**Returns**  
---  
**Type** | **Description**  
`[SedentaryPeriodRollupValueOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.SedentaryPeriodRollupValueOrBuilder)` |   
  
### getSteps()
    
    
    public StepsRollupValue getSteps()

Returned by default when rolling up data points from the `steps` data type, or when requested explicitly using the `steps` rollup type identifier.

`.google.devicesandservices.health.v4.StepsRollupValue steps = 5;`

**Returns**  
---  
**Type** | **Description**  
`[StepsRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.StepsRollupValue)` | The steps.  
  
### getStepsBuilder()
    
    
    public StepsRollupValue.Builder getStepsBuilder()

Returned by default when rolling up data points from the `steps` data type, or when requested explicitly using the `steps` rollup type identifier.

`.google.devicesandservices.health.v4.StepsRollupValue steps = 5;`

**Returns**  
---  
**Type** | **Description**  
`[StepsRollupValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.StepsRollupValue.Builder)` |   
  
### getStepsOrBuilder()
    
    
    public StepsRollupValueOrBuilder getStepsOrBuilder()

Returned by default when rolling up data points from the `steps` data type, or when requested explicitly using the `steps` rollup type identifier.

`.google.devicesandservices.health.v4.StepsRollupValue steps = 5;`

**Returns**  
---  
**Type** | **Description**  
`[StepsRollupValueOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.StepsRollupValueOrBuilder)` |   
  
### getSwimLengthsData()
    
    
    public SwimLengthsDataRollupValue getSwimLengthsData()

Returned by default when rolling up data points from the `swim-lengths-data` data type, or when requested explicitly using the `swim-lengths-data` rollup type identifier.

`.google.devicesandservices.health.v4.SwimLengthsDataRollupValue swim_lengths_data = 25; `

**Returns**  
---  
**Type** | **Description**  
`[SwimLengthsDataRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.SwimLengthsDataRollupValue)` | The swimLengthsData.  
  
### getSwimLengthsDataBuilder()
    
    
    public SwimLengthsDataRollupValue.Builder getSwimLengthsDataBuilder()

Returned by default when rolling up data points from the `swim-lengths-data` data type, or when requested explicitly using the `swim-lengths-data` rollup type identifier.

`.google.devicesandservices.health.v4.SwimLengthsDataRollupValue swim_lengths_data = 25; `

**Returns**  
---  
**Type** | **Description**  
`[SwimLengthsDataRollupValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.SwimLengthsDataRollupValue.Builder)` |   
  
### getSwimLengthsDataOrBuilder()
    
    
    public SwimLengthsDataRollupValueOrBuilder getSwimLengthsDataOrBuilder()

Returned by default when rolling up data points from the `swim-lengths-data` data type, or when requested explicitly using the `swim-lengths-data` rollup type identifier.

`.google.devicesandservices.health.v4.SwimLengthsDataRollupValue swim_lengths_data = 25; `

**Returns**  
---  
**Type** | **Description**  
`[SwimLengthsDataRollupValueOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.SwimLengthsDataRollupValueOrBuilder)` |   
  
### getTimeInHeartRateZone()
    
    
    public TimeInHeartRateZoneRollupValue getTimeInHeartRateZone()

Returned by default when rolling up data points from the `time-in-heart-rate-zone` data type, or when requested explicitly using the `time-in-heart-rate-zone` rollup type identifier.

` .google.devicesandservices.health.v4.TimeInHeartRateZoneRollupValue time_in_heart_rate_zone = 23; `

**Returns**  
---  
**Type** | **Description**  
`[TimeInHeartRateZoneRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.TimeInHeartRateZoneRollupValue)` | The timeInHeartRateZone.  
  
### getTimeInHeartRateZoneBuilder()
    
    
    public TimeInHeartRateZoneRollupValue.Builder getTimeInHeartRateZoneBuilder()

Returned by default when rolling up data points from the `time-in-heart-rate-zone` data type, or when requested explicitly using the `time-in-heart-rate-zone` rollup type identifier.

` .google.devicesandservices.health.v4.TimeInHeartRateZoneRollupValue time_in_heart_rate_zone = 23; `

**Returns**  
---  
**Type** | **Description**  
`[TimeInHeartRateZoneRollupValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.TimeInHeartRateZoneRollupValue.Builder)` |   
  
### getTimeInHeartRateZoneOrBuilder()
    
    
    public TimeInHeartRateZoneRollupValueOrBuilder getTimeInHeartRateZoneOrBuilder()

Returned by default when rolling up data points from the `time-in-heart-rate-zone` data type, or when requested explicitly using the `time-in-heart-rate-zone` rollup type identifier.

` .google.devicesandservices.health.v4.TimeInHeartRateZoneRollupValue time_in_heart_rate_zone = 23; `

**Returns**  
---  
**Type** | **Description**  
`[TimeInHeartRateZoneRollupValueOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.TimeInHeartRateZoneRollupValueOrBuilder)` |   
  
### getTotalCalories()
    
    
    public TotalCaloriesRollupValue getTotalCalories()

Returned by default when rolling up data points from the `total-calories` data type, or when requested explicitly using the `total-calories` rollup type identifier.

`.google.devicesandservices.health.v4.TotalCaloriesRollupValue total_calories = 14; `

**Returns**  
---  
**Type** | **Description**  
`[TotalCaloriesRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.TotalCaloriesRollupValue)` | The totalCalories.  
  
### getTotalCaloriesBuilder()
    
    
    public TotalCaloriesRollupValue.Builder getTotalCaloriesBuilder()

Returned by default when rolling up data points from the `total-calories` data type, or when requested explicitly using the `total-calories` rollup type identifier.

`.google.devicesandservices.health.v4.TotalCaloriesRollupValue total_calories = 14; `

**Returns**  
---  
**Type** | **Description**  
`[TotalCaloriesRollupValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.TotalCaloriesRollupValue.Builder)` |   
  
### getTotalCaloriesOrBuilder()
    
    
    public TotalCaloriesRollupValueOrBuilder getTotalCaloriesOrBuilder()

Returned by default when rolling up data points from the `total-calories` data type, or when requested explicitly using the `total-calories` rollup type identifier.

`.google.devicesandservices.health.v4.TotalCaloriesRollupValue total_calories = 14; `

**Returns**  
---  
**Type** | **Description**  
`[TotalCaloriesRollupValueOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.TotalCaloriesRollupValueOrBuilder)` |   
  
### getValueCase()
    
    
    public DailyRollupDataPoint.ValueCase getValueCase()

**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.ValueCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.ValueCase)` |   
  
### getWeight()
    
    
    public WeightRollupValue getWeight()

Returned by default when rolling up data points from the `weight` data type, or when requested explicitly using the `weight` rollup type identifier.

`.google.devicesandservices.health.v4.WeightRollupValue weight = 10;`

**Returns**  
---  
**Type** | **Description**  
`[WeightRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.WeightRollupValue)` | The weight.  
  
### getWeightBuilder()
    
    
    public WeightRollupValue.Builder getWeightBuilder()

Returned by default when rolling up data points from the `weight` data type, or when requested explicitly using the `weight` rollup type identifier.

`.google.devicesandservices.health.v4.WeightRollupValue weight = 10;`

**Returns**  
---  
**Type** | **Description**  
`[WeightRollupValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.WeightRollupValue.Builder)` |   
  
### getWeightOrBuilder()
    
    
    public WeightRollupValueOrBuilder getWeightOrBuilder()

Returned by default when rolling up data points from the `weight` data type, or when requested explicitly using the `weight` rollup type identifier.

`.google.devicesandservices.health.v4.WeightRollupValue weight = 10;`

**Returns**  
---  
**Type** | **Description**  
`[WeightRollupValueOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.WeightRollupValueOrBuilder)` |   
  
### hasActiveEnergyBurned()
    
    
    public boolean hasActiveEnergyBurned()

Returned by default when rolling up data points from the `active-energy-burned` data type.

` .google.devicesandservices.health.v4.ActiveEnergyBurnedRollupValue active_energy_burned = 27; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the activeEnergyBurned field is set.  
  
### hasActiveMinutes()
    
    
    public boolean hasActiveMinutes()

Returned by default when rolling up data points from the `active-minutes` data type, or when requested explicitly using the `active-minutes` rollup type identifier.

`.google.devicesandservices.health.v4.ActiveMinutesRollupValue active_minutes = 24; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the activeMinutes field is set.  
  
### hasActiveZoneMinutes()
    
    
    public boolean hasActiveZoneMinutes()

Returned by default when rolling up data points from the `active-zone-minutes` data type, or when requested explicitly using the `active-zone-minutes` rollup type identifier.

` .google.devicesandservices.health.v4.ActiveZoneMinutesRollupValue active_zone_minutes = 15; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the activeZoneMinutes field is set.  
  
### hasActivityLevel()
    
    
    public boolean hasActivityLevel()

Returned by default when rolling up data points from the `activity-level` data type, or when requested explicitly using the `activity-level` rollup type identifier.

`.google.devicesandservices.health.v4.ActivityLevelRollupValue activity_level = 20; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the activityLevel field is set.  
  
### hasAltitude()
    
    
    public boolean hasAltitude()

Returned by default when rolling up data points from the `altitude` data type, or when requested explicitly using the `altitude` rollup type identifier.

`.google.devicesandservices.health.v4.AltitudeRollupValue altitude = 11;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the altitude field is set.  
  
### hasBloodGlucose()
    
    
    public boolean hasBloodGlucose()

Returned by default when rolling up data points from the `blood-glucose` data type.

`.google.devicesandservices.health.v4.BloodGlucoseRollupValue blood_glucose = 28;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the bloodGlucose field is set.  
  
### hasBodyFat()
    
    
    public boolean hasBodyFat()

Returned by default when rolling up data points from the `body-fat` data type, or when requested explicitly using the `body-fat` rollup type identifier.

`.google.devicesandservices.health.v4.BodyFatRollupValue body_fat = 13;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the bodyFat field is set.  
  
### hasCaloriesInHeartRateZone()
    
    
    public boolean hasCaloriesInHeartRateZone()

Returned by default when rolling up data points from the `calories-in-heart-rate-zone` data type, or when requested explicitly using the `calories-in-heart-rate-zone` rollup type identifier.

` .google.devicesandservices.health.v4.CaloriesInHeartRateZoneRollupValue calories_in_heart_rate_zone = 19; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the caloriesInHeartRateZone field is set.  
  
### hasCivilEndTime()
    
    
    public boolean hasCivilEndTime()

End time of the window this value aggregates over

`.google.devicesandservices.health.v4.CivilDateTime civil_end_time = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the civilEndTime field is set.  
  
### hasCivilStartTime()
    
    
    public boolean hasCivilStartTime()

Start time of the window this value aggregates over

`.google.devicesandservices.health.v4.CivilDateTime civil_start_time = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the civilStartTime field is set.  
  
### hasCoreBodyTemperature()
    
    
    public boolean hasCoreBodyTemperature()

Returned by default when rolling up data points from the `core-body-temperature` data type, or when requested explicitly using the `core-body-temperature` rollup type identifier.

` .google.devicesandservices.health.v4.CoreBodyTemperatureRollupValue core_body_temperature = 26; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the coreBodyTemperature field is set.  
  
### hasDistance()
    
    
    public boolean hasDistance()

Returned by default when rolling up data points from the `distance` data type, or when requested explicitly using the `distance` rollup type identifier.

`.google.devicesandservices.health.v4.DistanceRollupValue distance = 12;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the distance field is set.  
  
### hasFloors()
    
    
    public boolean hasFloors()

Returned by default when rolling up data points from the `floors` data type, or when requested explicitly using the `floors` rollup type identifier.

`.google.devicesandservices.health.v4.FloorsRollupValue floors = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the floors field is set.  
  
### hasHeartRate()
    
    
    public boolean hasHeartRate()

Returned by default when rolling up data points from the `heart-rate` data type, or when requested explicitly using the `heart-rate` rollup type identifier.

`.google.devicesandservices.health.v4.HeartRateRollupValue heart_rate = 7;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the heartRate field is set.  
  
### hasHeartRateVariabilityPersonalRange()
    
    
    public boolean hasHeartRateVariabilityPersonalRange()

Returned by default when rolling up data points from the `daily-heart-rate-variability` data type, or when requested explicitly using the `heart-rate-variability-personal-range` rollup type identifier.

` .google.devicesandservices.health.v4.HeartRateVariabilityPersonalRangeRollupValue heart_rate_variability_personal_range = 9; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the heartRateVariabilityPersonalRange field is set.  
  
### hasHydrationLog()
    
    
    public boolean hasHydrationLog()

Returned by default when rolling up data points from the `hydration-log` data type, or when requested explicitly using the `hydration-log` rollup type identifier.

`.google.devicesandservices.health.v4.HydrationLogRollupValue hydration_log = 22;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the hydrationLog field is set.  
  
### hasNutritionLog()
    
    
    public boolean hasNutritionLog()

Returned by default when rolling up data points from the `nutrition-log` data type, or when requested explicitly using the `nutrition-log` rollup type identifier.

`.google.devicesandservices.health.v4.NutritionLogRollupValue nutrition_log = 21;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the nutritionLog field is set.  
  
### hasRestingHeartRatePersonalRange()
    
    
    public boolean hasRestingHeartRatePersonalRange()

Returned by default when rolling up data points from the `daily-resting-heart-rate` data type, or when requested explicitly using the `resting-heart-rate-personal-range` rollup type identifier.

` .google.devicesandservices.health.v4.RestingHeartRatePersonalRangeRollupValue resting_heart_rate_personal_range = 8; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the restingHeartRatePersonalRange field is set.  
  
### hasRunVo2Max()
    
    
    public boolean hasRunVo2Max()

Returned by default when rolling up data points from the `run-vo2-max` data type, or when requested explicitly using the `run-vo2-max` rollup type identifier.

`.google.devicesandservices.health.v4.RunVO2MaxRollupValue run_vo2_max = 18;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the runVo2Max field is set.  
  
### hasSedentaryPeriod()
    
    
    public boolean hasSedentaryPeriod()

Returned by default when rolling up data points from the `sedentary-period` data type, or when requested explicitly using the `sedentary-period` rollup type identifier.

`.google.devicesandservices.health.v4.SedentaryPeriodRollupValue sedentary_period = 17; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the sedentaryPeriod field is set.  
  
### hasSteps()
    
    
    public boolean hasSteps()

Returned by default when rolling up data points from the `steps` data type, or when requested explicitly using the `steps` rollup type identifier.

`.google.devicesandservices.health.v4.StepsRollupValue steps = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the steps field is set.  
  
### hasSwimLengthsData()
    
    
    public boolean hasSwimLengthsData()

Returned by default when rolling up data points from the `swim-lengths-data` data type, or when requested explicitly using the `swim-lengths-data` rollup type identifier.

`.google.devicesandservices.health.v4.SwimLengthsDataRollupValue swim_lengths_data = 25; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the swimLengthsData field is set.  
  
### hasTimeInHeartRateZone()
    
    
    public boolean hasTimeInHeartRateZone()

Returned by default when rolling up data points from the `time-in-heart-rate-zone` data type, or when requested explicitly using the `time-in-heart-rate-zone` rollup type identifier.

` .google.devicesandservices.health.v4.TimeInHeartRateZoneRollupValue time_in_heart_rate_zone = 23; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the timeInHeartRateZone field is set.  
  
### hasTotalCalories()
    
    
    public boolean hasTotalCalories()

Returned by default when rolling up data points from the `total-calories` data type, or when requested explicitly using the `total-calories` rollup type identifier.

`.google.devicesandservices.health.v4.TotalCaloriesRollupValue total_calories = 14; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the totalCalories field is set.  
  
### hasWeight()
    
    
    public boolean hasWeight()

Returned by default when rolling up data points from the `weight` data type, or when requested explicitly using the `weight` rollup type identifier.

`.google.devicesandservices.health.v4.WeightRollupValue weight = 10;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the weight field is set.  
  
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

### mergeActiveEnergyBurned(ActiveEnergyBurnedRollupValue value)
    
    
    public DailyRollupDataPoint.Builder mergeActiveEnergyBurned(ActiveEnergyBurnedRollupValue value)

Returned by default when rolling up data points from the `active-energy-burned` data type.

` .google.devicesandservices.health.v4.ActiveEnergyBurnedRollupValue active_energy_burned = 27; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ActiveEnergyBurnedRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ActiveEnergyBurnedRollupValue)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### mergeActiveMinutes(ActiveMinutesRollupValue value)
    
    
    public DailyRollupDataPoint.Builder mergeActiveMinutes(ActiveMinutesRollupValue value)

Returned by default when rolling up data points from the `active-minutes` data type, or when requested explicitly using the `active-minutes` rollup type identifier.

`.google.devicesandservices.health.v4.ActiveMinutesRollupValue active_minutes = 24; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ActiveMinutesRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ActiveMinutesRollupValue)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### mergeActiveZoneMinutes(ActiveZoneMinutesRollupValue value)
    
    
    public DailyRollupDataPoint.Builder mergeActiveZoneMinutes(ActiveZoneMinutesRollupValue value)

Returned by default when rolling up data points from the `active-zone-minutes` data type, or when requested explicitly using the `active-zone-minutes` rollup type identifier.

` .google.devicesandservices.health.v4.ActiveZoneMinutesRollupValue active_zone_minutes = 15; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ActiveZoneMinutesRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ActiveZoneMinutesRollupValue)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### mergeActivityLevel(ActivityLevelRollupValue value)
    
    
    public DailyRollupDataPoint.Builder mergeActivityLevel(ActivityLevelRollupValue value)

Returned by default when rolling up data points from the `activity-level` data type, or when requested explicitly using the `activity-level` rollup type identifier.

`.google.devicesandservices.health.v4.ActivityLevelRollupValue activity_level = 20; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ActivityLevelRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ActivityLevelRollupValue)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### mergeAltitude(AltitudeRollupValue value)
    
    
    public DailyRollupDataPoint.Builder mergeAltitude(AltitudeRollupValue value)

Returned by default when rolling up data points from the `altitude` data type, or when requested explicitly using the `altitude` rollup type identifier.

`.google.devicesandservices.health.v4.AltitudeRollupValue altitude = 11;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[AltitudeRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.AltitudeRollupValue)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### mergeBloodGlucose(BloodGlucoseRollupValue value)
    
    
    public DailyRollupDataPoint.Builder mergeBloodGlucose(BloodGlucoseRollupValue value)

Returned by default when rolling up data points from the `blood-glucose` data type.

`.google.devicesandservices.health.v4.BloodGlucoseRollupValue blood_glucose = 28;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[BloodGlucoseRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.BloodGlucoseRollupValue)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### mergeBodyFat(BodyFatRollupValue value)
    
    
    public DailyRollupDataPoint.Builder mergeBodyFat(BodyFatRollupValue value)

Returned by default when rolling up data points from the `body-fat` data type, or when requested explicitly using the `body-fat` rollup type identifier.

`.google.devicesandservices.health.v4.BodyFatRollupValue body_fat = 13;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[BodyFatRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.BodyFatRollupValue)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### mergeCaloriesInHeartRateZone(CaloriesInHeartRateZoneRollupValue value)
    
    
    public DailyRollupDataPoint.Builder mergeCaloriesInHeartRateZone(CaloriesInHeartRateZoneRollupValue value)

Returned by default when rolling up data points from the `calories-in-heart-rate-zone` data type, or when requested explicitly using the `calories-in-heart-rate-zone` rollup type identifier.

` .google.devicesandservices.health.v4.CaloriesInHeartRateZoneRollupValue calories_in_heart_rate_zone = 19; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[CaloriesInHeartRateZoneRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CaloriesInHeartRateZoneRollupValue)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### mergeCivilEndTime(CivilDateTime value)
    
    
    public DailyRollupDataPoint.Builder mergeCivilEndTime(CivilDateTime value)

End time of the window this value aggregates over

`.google.devicesandservices.health.v4.CivilDateTime civil_end_time = 2;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[CivilDateTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CivilDateTime)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### mergeCivilStartTime(CivilDateTime value)
    
    
    public DailyRollupDataPoint.Builder mergeCivilStartTime(CivilDateTime value)

Start time of the window this value aggregates over

`.google.devicesandservices.health.v4.CivilDateTime civil_start_time = 1;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[CivilDateTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CivilDateTime)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### mergeCoreBodyTemperature(CoreBodyTemperatureRollupValue value)
    
    
    public DailyRollupDataPoint.Builder mergeCoreBodyTemperature(CoreBodyTemperatureRollupValue value)

Returned by default when rolling up data points from the `core-body-temperature` data type, or when requested explicitly using the `core-body-temperature` rollup type identifier.

` .google.devicesandservices.health.v4.CoreBodyTemperatureRollupValue core_body_temperature = 26; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[CoreBodyTemperatureRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CoreBodyTemperatureRollupValue)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### mergeDistance(DistanceRollupValue value)
    
    
    public DailyRollupDataPoint.Builder mergeDistance(DistanceRollupValue value)

Returned by default when rolling up data points from the `distance` data type, or when requested explicitly using the `distance` rollup type identifier.

`.google.devicesandservices.health.v4.DistanceRollupValue distance = 12;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[DistanceRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DistanceRollupValue)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### mergeFloors(FloorsRollupValue value)
    
    
    public DailyRollupDataPoint.Builder mergeFloors(FloorsRollupValue value)

Returned by default when rolling up data points from the `floors` data type, or when requested explicitly using the `floors` rollup type identifier.

`.google.devicesandservices.health.v4.FloorsRollupValue floors = 6;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[FloorsRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.FloorsRollupValue)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### mergeFrom(DailyRollupDataPoint other)
    
    
    public DailyRollupDataPoint.Builder mergeFrom(DailyRollupDataPoint other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[DailyRollupDataPoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public DailyRollupDataPoint.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public DailyRollupDataPoint.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### mergeHeartRate(HeartRateRollupValue value)
    
    
    public DailyRollupDataPoint.Builder mergeHeartRate(HeartRateRollupValue value)

Returned by default when rolling up data points from the `heart-rate` data type, or when requested explicitly using the `heart-rate` rollup type identifier.

`.google.devicesandservices.health.v4.HeartRateRollupValue heart_rate = 7;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[HeartRateRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.HeartRateRollupValue)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### mergeHeartRateVariabilityPersonalRange(HeartRateVariabilityPersonalRangeRollupValue value)
    
    
    public DailyRollupDataPoint.Builder mergeHeartRateVariabilityPersonalRange(HeartRateVariabilityPersonalRangeRollupValue value)

Returned by default when rolling up data points from the `daily-heart-rate-variability` data type, or when requested explicitly using the `heart-rate-variability-personal-range` rollup type identifier.

` .google.devicesandservices.health.v4.HeartRateVariabilityPersonalRangeRollupValue heart_rate_variability_personal_range = 9; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[HeartRateVariabilityPersonalRangeRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.HeartRateVariabilityPersonalRangeRollupValue)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### mergeHydrationLog(HydrationLogRollupValue value)
    
    
    public DailyRollupDataPoint.Builder mergeHydrationLog(HydrationLogRollupValue value)

Returned by default when rolling up data points from the `hydration-log` data type, or when requested explicitly using the `hydration-log` rollup type identifier.

`.google.devicesandservices.health.v4.HydrationLogRollupValue hydration_log = 22;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[HydrationLogRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.HydrationLogRollupValue)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### mergeNutritionLog(NutritionLogRollupValue value)
    
    
    public DailyRollupDataPoint.Builder mergeNutritionLog(NutritionLogRollupValue value)

Returned by default when rolling up data points from the `nutrition-log` data type, or when requested explicitly using the `nutrition-log` rollup type identifier.

`.google.devicesandservices.health.v4.NutritionLogRollupValue nutrition_log = 21;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[NutritionLogRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.NutritionLogRollupValue)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### mergeRestingHeartRatePersonalRange(RestingHeartRatePersonalRangeRollupValue value)
    
    
    public DailyRollupDataPoint.Builder mergeRestingHeartRatePersonalRange(RestingHeartRatePersonalRangeRollupValue value)

Returned by default when rolling up data points from the `daily-resting-heart-rate` data type, or when requested explicitly using the `resting-heart-rate-personal-range` rollup type identifier.

` .google.devicesandservices.health.v4.RestingHeartRatePersonalRangeRollupValue resting_heart_rate_personal_range = 8; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[RestingHeartRatePersonalRangeRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.RestingHeartRatePersonalRangeRollupValue)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### mergeRunVo2Max(RunVO2MaxRollupValue value)
    
    
    public DailyRollupDataPoint.Builder mergeRunVo2Max(RunVO2MaxRollupValue value)

Returned by default when rolling up data points from the `run-vo2-max` data type, or when requested explicitly using the `run-vo2-max` rollup type identifier.

`.google.devicesandservices.health.v4.RunVO2MaxRollupValue run_vo2_max = 18;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[RunVO2MaxRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.RunVO2MaxRollupValue)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### mergeSedentaryPeriod(SedentaryPeriodRollupValue value)
    
    
    public DailyRollupDataPoint.Builder mergeSedentaryPeriod(SedentaryPeriodRollupValue value)

Returned by default when rolling up data points from the `sedentary-period` data type, or when requested explicitly using the `sedentary-period` rollup type identifier.

`.google.devicesandservices.health.v4.SedentaryPeriodRollupValue sedentary_period = 17; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[SedentaryPeriodRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.SedentaryPeriodRollupValue)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### mergeSteps(StepsRollupValue value)
    
    
    public DailyRollupDataPoint.Builder mergeSteps(StepsRollupValue value)

Returned by default when rolling up data points from the `steps` data type, or when requested explicitly using the `steps` rollup type identifier.

`.google.devicesandservices.health.v4.StepsRollupValue steps = 5;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[StepsRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.StepsRollupValue)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### mergeSwimLengthsData(SwimLengthsDataRollupValue value)
    
    
    public DailyRollupDataPoint.Builder mergeSwimLengthsData(SwimLengthsDataRollupValue value)

Returned by default when rolling up data points from the `swim-lengths-data` data type, or when requested explicitly using the `swim-lengths-data` rollup type identifier.

`.google.devicesandservices.health.v4.SwimLengthsDataRollupValue swim_lengths_data = 25; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[SwimLengthsDataRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.SwimLengthsDataRollupValue)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### mergeTimeInHeartRateZone(TimeInHeartRateZoneRollupValue value)
    
    
    public DailyRollupDataPoint.Builder mergeTimeInHeartRateZone(TimeInHeartRateZoneRollupValue value)

Returned by default when rolling up data points from the `time-in-heart-rate-zone` data type, or when requested explicitly using the `time-in-heart-rate-zone` rollup type identifier.

` .google.devicesandservices.health.v4.TimeInHeartRateZoneRollupValue time_in_heart_rate_zone = 23; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[TimeInHeartRateZoneRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.TimeInHeartRateZoneRollupValue)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### mergeTotalCalories(TotalCaloriesRollupValue value)
    
    
    public DailyRollupDataPoint.Builder mergeTotalCalories(TotalCaloriesRollupValue value)

Returned by default when rolling up data points from the `total-calories` data type, or when requested explicitly using the `total-calories` rollup type identifier.

`.google.devicesandservices.health.v4.TotalCaloriesRollupValue total_calories = 14; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[TotalCaloriesRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.TotalCaloriesRollupValue)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### mergeWeight(WeightRollupValue value)
    
    
    public DailyRollupDataPoint.Builder mergeWeight(WeightRollupValue value)

Returned by default when rolling up data points from the `weight` data type, or when requested explicitly using the `weight` rollup type identifier.

`.google.devicesandservices.health.v4.WeightRollupValue weight = 10;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[WeightRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.WeightRollupValue)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### setActiveEnergyBurned(ActiveEnergyBurnedRollupValue value)
    
    
    public DailyRollupDataPoint.Builder setActiveEnergyBurned(ActiveEnergyBurnedRollupValue value)

Returned by default when rolling up data points from the `active-energy-burned` data type.

` .google.devicesandservices.health.v4.ActiveEnergyBurnedRollupValue active_energy_burned = 27; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ActiveEnergyBurnedRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ActiveEnergyBurnedRollupValue)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### setActiveEnergyBurned(ActiveEnergyBurnedRollupValue.Builder builderForValue)
    
    
    public DailyRollupDataPoint.Builder setActiveEnergyBurned(ActiveEnergyBurnedRollupValue.Builder builderForValue)

Returned by default when rolling up data points from the `active-energy-burned` data type.

` .google.devicesandservices.health.v4.ActiveEnergyBurnedRollupValue active_energy_burned = 27; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[ActiveEnergyBurnedRollupValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ActiveEnergyBurnedRollupValue.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### setActiveMinutes(ActiveMinutesRollupValue value)
    
    
    public DailyRollupDataPoint.Builder setActiveMinutes(ActiveMinutesRollupValue value)

Returned by default when rolling up data points from the `active-minutes` data type, or when requested explicitly using the `active-minutes` rollup type identifier.

`.google.devicesandservices.health.v4.ActiveMinutesRollupValue active_minutes = 24; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ActiveMinutesRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ActiveMinutesRollupValue)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### setActiveMinutes(ActiveMinutesRollupValue.Builder builderForValue)
    
    
    public DailyRollupDataPoint.Builder setActiveMinutes(ActiveMinutesRollupValue.Builder builderForValue)

Returned by default when rolling up data points from the `active-minutes` data type, or when requested explicitly using the `active-minutes` rollup type identifier.

`.google.devicesandservices.health.v4.ActiveMinutesRollupValue active_minutes = 24; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[ActiveMinutesRollupValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ActiveMinutesRollupValue.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### setActiveZoneMinutes(ActiveZoneMinutesRollupValue value)
    
    
    public DailyRollupDataPoint.Builder setActiveZoneMinutes(ActiveZoneMinutesRollupValue value)

Returned by default when rolling up data points from the `active-zone-minutes` data type, or when requested explicitly using the `active-zone-minutes` rollup type identifier.

` .google.devicesandservices.health.v4.ActiveZoneMinutesRollupValue active_zone_minutes = 15; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ActiveZoneMinutesRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ActiveZoneMinutesRollupValue)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### setActiveZoneMinutes(ActiveZoneMinutesRollupValue.Builder builderForValue)
    
    
    public DailyRollupDataPoint.Builder setActiveZoneMinutes(ActiveZoneMinutesRollupValue.Builder builderForValue)

Returned by default when rolling up data points from the `active-zone-minutes` data type, or when requested explicitly using the `active-zone-minutes` rollup type identifier.

` .google.devicesandservices.health.v4.ActiveZoneMinutesRollupValue active_zone_minutes = 15; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[ActiveZoneMinutesRollupValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ActiveZoneMinutesRollupValue.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### setActivityLevel(ActivityLevelRollupValue value)
    
    
    public DailyRollupDataPoint.Builder setActivityLevel(ActivityLevelRollupValue value)

Returned by default when rolling up data points from the `activity-level` data type, or when requested explicitly using the `activity-level` rollup type identifier.

`.google.devicesandservices.health.v4.ActivityLevelRollupValue activity_level = 20; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ActivityLevelRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ActivityLevelRollupValue)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### setActivityLevel(ActivityLevelRollupValue.Builder builderForValue)
    
    
    public DailyRollupDataPoint.Builder setActivityLevel(ActivityLevelRollupValue.Builder builderForValue)

Returned by default when rolling up data points from the `activity-level` data type, or when requested explicitly using the `activity-level` rollup type identifier.

`.google.devicesandservices.health.v4.ActivityLevelRollupValue activity_level = 20; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[ActivityLevelRollupValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ActivityLevelRollupValue.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### setAltitude(AltitudeRollupValue value)
    
    
    public DailyRollupDataPoint.Builder setAltitude(AltitudeRollupValue value)

Returned by default when rolling up data points from the `altitude` data type, or when requested explicitly using the `altitude` rollup type identifier.

`.google.devicesandservices.health.v4.AltitudeRollupValue altitude = 11;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[AltitudeRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.AltitudeRollupValue)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### setAltitude(AltitudeRollupValue.Builder builderForValue)
    
    
    public DailyRollupDataPoint.Builder setAltitude(AltitudeRollupValue.Builder builderForValue)

Returned by default when rolling up data points from the `altitude` data type, or when requested explicitly using the `altitude` rollup type identifier.

`.google.devicesandservices.health.v4.AltitudeRollupValue altitude = 11;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[AltitudeRollupValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.AltitudeRollupValue.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### setBloodGlucose(BloodGlucoseRollupValue value)
    
    
    public DailyRollupDataPoint.Builder setBloodGlucose(BloodGlucoseRollupValue value)

Returned by default when rolling up data points from the `blood-glucose` data type.

`.google.devicesandservices.health.v4.BloodGlucoseRollupValue blood_glucose = 28;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[BloodGlucoseRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.BloodGlucoseRollupValue)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### setBloodGlucose(BloodGlucoseRollupValue.Builder builderForValue)
    
    
    public DailyRollupDataPoint.Builder setBloodGlucose(BloodGlucoseRollupValue.Builder builderForValue)

Returned by default when rolling up data points from the `blood-glucose` data type.

`.google.devicesandservices.health.v4.BloodGlucoseRollupValue blood_glucose = 28;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[BloodGlucoseRollupValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.BloodGlucoseRollupValue.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### setBodyFat(BodyFatRollupValue value)
    
    
    public DailyRollupDataPoint.Builder setBodyFat(BodyFatRollupValue value)

Returned by default when rolling up data points from the `body-fat` data type, or when requested explicitly using the `body-fat` rollup type identifier.

`.google.devicesandservices.health.v4.BodyFatRollupValue body_fat = 13;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[BodyFatRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.BodyFatRollupValue)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### setBodyFat(BodyFatRollupValue.Builder builderForValue)
    
    
    public DailyRollupDataPoint.Builder setBodyFat(BodyFatRollupValue.Builder builderForValue)

Returned by default when rolling up data points from the `body-fat` data type, or when requested explicitly using the `body-fat` rollup type identifier.

`.google.devicesandservices.health.v4.BodyFatRollupValue body_fat = 13;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[BodyFatRollupValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.BodyFatRollupValue.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### setCaloriesInHeartRateZone(CaloriesInHeartRateZoneRollupValue value)
    
    
    public DailyRollupDataPoint.Builder setCaloriesInHeartRateZone(CaloriesInHeartRateZoneRollupValue value)

Returned by default when rolling up data points from the `calories-in-heart-rate-zone` data type, or when requested explicitly using the `calories-in-heart-rate-zone` rollup type identifier.

` .google.devicesandservices.health.v4.CaloriesInHeartRateZoneRollupValue calories_in_heart_rate_zone = 19; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[CaloriesInHeartRateZoneRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CaloriesInHeartRateZoneRollupValue)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### setCaloriesInHeartRateZone(CaloriesInHeartRateZoneRollupValue.Builder builderForValue)
    
    
    public DailyRollupDataPoint.Builder setCaloriesInHeartRateZone(CaloriesInHeartRateZoneRollupValue.Builder builderForValue)

Returned by default when rolling up data points from the `calories-in-heart-rate-zone` data type, or when requested explicitly using the `calories-in-heart-rate-zone` rollup type identifier.

` .google.devicesandservices.health.v4.CaloriesInHeartRateZoneRollupValue calories_in_heart_rate_zone = 19; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[CaloriesInHeartRateZoneRollupValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CaloriesInHeartRateZoneRollupValue.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### setCivilEndTime(CivilDateTime value)
    
    
    public DailyRollupDataPoint.Builder setCivilEndTime(CivilDateTime value)

End time of the window this value aggregates over

`.google.devicesandservices.health.v4.CivilDateTime civil_end_time = 2;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[CivilDateTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CivilDateTime)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### setCivilEndTime(CivilDateTime.Builder builderForValue)
    
    
    public DailyRollupDataPoint.Builder setCivilEndTime(CivilDateTime.Builder builderForValue)

End time of the window this value aggregates over

`.google.devicesandservices.health.v4.CivilDateTime civil_end_time = 2;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[CivilDateTime.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CivilDateTime.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### setCivilStartTime(CivilDateTime value)
    
    
    public DailyRollupDataPoint.Builder setCivilStartTime(CivilDateTime value)

Start time of the window this value aggregates over

`.google.devicesandservices.health.v4.CivilDateTime civil_start_time = 1;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[CivilDateTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CivilDateTime)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### setCivilStartTime(CivilDateTime.Builder builderForValue)
    
    
    public DailyRollupDataPoint.Builder setCivilStartTime(CivilDateTime.Builder builderForValue)

Start time of the window this value aggregates over

`.google.devicesandservices.health.v4.CivilDateTime civil_start_time = 1;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[CivilDateTime.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CivilDateTime.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### setCoreBodyTemperature(CoreBodyTemperatureRollupValue value)
    
    
    public DailyRollupDataPoint.Builder setCoreBodyTemperature(CoreBodyTemperatureRollupValue value)

Returned by default when rolling up data points from the `core-body-temperature` data type, or when requested explicitly using the `core-body-temperature` rollup type identifier.

` .google.devicesandservices.health.v4.CoreBodyTemperatureRollupValue core_body_temperature = 26; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[CoreBodyTemperatureRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CoreBodyTemperatureRollupValue)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### setCoreBodyTemperature(CoreBodyTemperatureRollupValue.Builder builderForValue)
    
    
    public DailyRollupDataPoint.Builder setCoreBodyTemperature(CoreBodyTemperatureRollupValue.Builder builderForValue)

Returned by default when rolling up data points from the `core-body-temperature` data type, or when requested explicitly using the `core-body-temperature` rollup type identifier.

` .google.devicesandservices.health.v4.CoreBodyTemperatureRollupValue core_body_temperature = 26; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[CoreBodyTemperatureRollupValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CoreBodyTemperatureRollupValue.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### setDistance(DistanceRollupValue value)
    
    
    public DailyRollupDataPoint.Builder setDistance(DistanceRollupValue value)

Returned by default when rolling up data points from the `distance` data type, or when requested explicitly using the `distance` rollup type identifier.

`.google.devicesandservices.health.v4.DistanceRollupValue distance = 12;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[DistanceRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DistanceRollupValue)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### setDistance(DistanceRollupValue.Builder builderForValue)
    
    
    public DailyRollupDataPoint.Builder setDistance(DistanceRollupValue.Builder builderForValue)

Returned by default when rolling up data points from the `distance` data type, or when requested explicitly using the `distance` rollup type identifier.

`.google.devicesandservices.health.v4.DistanceRollupValue distance = 12;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[DistanceRollupValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DistanceRollupValue.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### setFloors(FloorsRollupValue value)
    
    
    public DailyRollupDataPoint.Builder setFloors(FloorsRollupValue value)

Returned by default when rolling up data points from the `floors` data type, or when requested explicitly using the `floors` rollup type identifier.

`.google.devicesandservices.health.v4.FloorsRollupValue floors = 6;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[FloorsRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.FloorsRollupValue)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### setFloors(FloorsRollupValue.Builder builderForValue)
    
    
    public DailyRollupDataPoint.Builder setFloors(FloorsRollupValue.Builder builderForValue)

Returned by default when rolling up data points from the `floors` data type, or when requested explicitly using the `floors` rollup type identifier.

`.google.devicesandservices.health.v4.FloorsRollupValue floors = 6;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[FloorsRollupValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.FloorsRollupValue.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### setHeartRate(HeartRateRollupValue value)
    
    
    public DailyRollupDataPoint.Builder setHeartRate(HeartRateRollupValue value)

Returned by default when rolling up data points from the `heart-rate` data type, or when requested explicitly using the `heart-rate` rollup type identifier.

`.google.devicesandservices.health.v4.HeartRateRollupValue heart_rate = 7;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[HeartRateRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.HeartRateRollupValue)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### setHeartRate(HeartRateRollupValue.Builder builderForValue)
    
    
    public DailyRollupDataPoint.Builder setHeartRate(HeartRateRollupValue.Builder builderForValue)

Returned by default when rolling up data points from the `heart-rate` data type, or when requested explicitly using the `heart-rate` rollup type identifier.

`.google.devicesandservices.health.v4.HeartRateRollupValue heart_rate = 7;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[HeartRateRollupValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.HeartRateRollupValue.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### setHeartRateVariabilityPersonalRange(HeartRateVariabilityPersonalRangeRollupValue value)
    
    
    public DailyRollupDataPoint.Builder setHeartRateVariabilityPersonalRange(HeartRateVariabilityPersonalRangeRollupValue value)

Returned by default when rolling up data points from the `daily-heart-rate-variability` data type, or when requested explicitly using the `heart-rate-variability-personal-range` rollup type identifier.

` .google.devicesandservices.health.v4.HeartRateVariabilityPersonalRangeRollupValue heart_rate_variability_personal_range = 9; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[HeartRateVariabilityPersonalRangeRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.HeartRateVariabilityPersonalRangeRollupValue)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### setHeartRateVariabilityPersonalRange(HeartRateVariabilityPersonalRangeRollupValue.Builder builderForValue)
    
    
    public DailyRollupDataPoint.Builder setHeartRateVariabilityPersonalRange(HeartRateVariabilityPersonalRangeRollupValue.Builder builderForValue)

Returned by default when rolling up data points from the `daily-heart-rate-variability` data type, or when requested explicitly using the `heart-rate-variability-personal-range` rollup type identifier.

` .google.devicesandservices.health.v4.HeartRateVariabilityPersonalRangeRollupValue heart_rate_variability_personal_range = 9; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[HeartRateVariabilityPersonalRangeRollupValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.HeartRateVariabilityPersonalRangeRollupValue.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### setHydrationLog(HydrationLogRollupValue value)
    
    
    public DailyRollupDataPoint.Builder setHydrationLog(HydrationLogRollupValue value)

Returned by default when rolling up data points from the `hydration-log` data type, or when requested explicitly using the `hydration-log` rollup type identifier.

`.google.devicesandservices.health.v4.HydrationLogRollupValue hydration_log = 22;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[HydrationLogRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.HydrationLogRollupValue)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### setHydrationLog(HydrationLogRollupValue.Builder builderForValue)
    
    
    public DailyRollupDataPoint.Builder setHydrationLog(HydrationLogRollupValue.Builder builderForValue)

Returned by default when rolling up data points from the `hydration-log` data type, or when requested explicitly using the `hydration-log` rollup type identifier.

`.google.devicesandservices.health.v4.HydrationLogRollupValue hydration_log = 22;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[HydrationLogRollupValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.HydrationLogRollupValue.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### setNutritionLog(NutritionLogRollupValue value)
    
    
    public DailyRollupDataPoint.Builder setNutritionLog(NutritionLogRollupValue value)

Returned by default when rolling up data points from the `nutrition-log` data type, or when requested explicitly using the `nutrition-log` rollup type identifier.

`.google.devicesandservices.health.v4.NutritionLogRollupValue nutrition_log = 21;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[NutritionLogRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.NutritionLogRollupValue)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### setNutritionLog(NutritionLogRollupValue.Builder builderForValue)
    
    
    public DailyRollupDataPoint.Builder setNutritionLog(NutritionLogRollupValue.Builder builderForValue)

Returned by default when rolling up data points from the `nutrition-log` data type, or when requested explicitly using the `nutrition-log` rollup type identifier.

`.google.devicesandservices.health.v4.NutritionLogRollupValue nutrition_log = 21;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[NutritionLogRollupValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.NutritionLogRollupValue.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### setRestingHeartRatePersonalRange(RestingHeartRatePersonalRangeRollupValue value)
    
    
    public DailyRollupDataPoint.Builder setRestingHeartRatePersonalRange(RestingHeartRatePersonalRangeRollupValue value)

Returned by default when rolling up data points from the `daily-resting-heart-rate` data type, or when requested explicitly using the `resting-heart-rate-personal-range` rollup type identifier.

` .google.devicesandservices.health.v4.RestingHeartRatePersonalRangeRollupValue resting_heart_rate_personal_range = 8; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[RestingHeartRatePersonalRangeRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.RestingHeartRatePersonalRangeRollupValue)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### setRestingHeartRatePersonalRange(RestingHeartRatePersonalRangeRollupValue.Builder builderForValue)
    
    
    public DailyRollupDataPoint.Builder setRestingHeartRatePersonalRange(RestingHeartRatePersonalRangeRollupValue.Builder builderForValue)

Returned by default when rolling up data points from the `daily-resting-heart-rate` data type, or when requested explicitly using the `resting-heart-rate-personal-range` rollup type identifier.

` .google.devicesandservices.health.v4.RestingHeartRatePersonalRangeRollupValue resting_heart_rate_personal_range = 8; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[RestingHeartRatePersonalRangeRollupValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.RestingHeartRatePersonalRangeRollupValue.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### setRunVo2Max(RunVO2MaxRollupValue value)
    
    
    public DailyRollupDataPoint.Builder setRunVo2Max(RunVO2MaxRollupValue value)

Returned by default when rolling up data points from the `run-vo2-max` data type, or when requested explicitly using the `run-vo2-max` rollup type identifier.

`.google.devicesandservices.health.v4.RunVO2MaxRollupValue run_vo2_max = 18;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[RunVO2MaxRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.RunVO2MaxRollupValue)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### setRunVo2Max(RunVO2MaxRollupValue.Builder builderForValue)
    
    
    public DailyRollupDataPoint.Builder setRunVo2Max(RunVO2MaxRollupValue.Builder builderForValue)

Returned by default when rolling up data points from the `run-vo2-max` data type, or when requested explicitly using the `run-vo2-max` rollup type identifier.

`.google.devicesandservices.health.v4.RunVO2MaxRollupValue run_vo2_max = 18;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[RunVO2MaxRollupValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.RunVO2MaxRollupValue.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### setSedentaryPeriod(SedentaryPeriodRollupValue value)
    
    
    public DailyRollupDataPoint.Builder setSedentaryPeriod(SedentaryPeriodRollupValue value)

Returned by default when rolling up data points from the `sedentary-period` data type, or when requested explicitly using the `sedentary-period` rollup type identifier.

`.google.devicesandservices.health.v4.SedentaryPeriodRollupValue sedentary_period = 17; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[SedentaryPeriodRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.SedentaryPeriodRollupValue)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### setSedentaryPeriod(SedentaryPeriodRollupValue.Builder builderForValue)
    
    
    public DailyRollupDataPoint.Builder setSedentaryPeriod(SedentaryPeriodRollupValue.Builder builderForValue)

Returned by default when rolling up data points from the `sedentary-period` data type, or when requested explicitly using the `sedentary-period` rollup type identifier.

`.google.devicesandservices.health.v4.SedentaryPeriodRollupValue sedentary_period = 17; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[SedentaryPeriodRollupValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.SedentaryPeriodRollupValue.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### setSteps(StepsRollupValue value)
    
    
    public DailyRollupDataPoint.Builder setSteps(StepsRollupValue value)

Returned by default when rolling up data points from the `steps` data type, or when requested explicitly using the `steps` rollup type identifier.

`.google.devicesandservices.health.v4.StepsRollupValue steps = 5;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[StepsRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.StepsRollupValue)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### setSteps(StepsRollupValue.Builder builderForValue)
    
    
    public DailyRollupDataPoint.Builder setSteps(StepsRollupValue.Builder builderForValue)

Returned by default when rolling up data points from the `steps` data type, or when requested explicitly using the `steps` rollup type identifier.

`.google.devicesandservices.health.v4.StepsRollupValue steps = 5;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[StepsRollupValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.StepsRollupValue.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### setSwimLengthsData(SwimLengthsDataRollupValue value)
    
    
    public DailyRollupDataPoint.Builder setSwimLengthsData(SwimLengthsDataRollupValue value)

Returned by default when rolling up data points from the `swim-lengths-data` data type, or when requested explicitly using the `swim-lengths-data` rollup type identifier.

`.google.devicesandservices.health.v4.SwimLengthsDataRollupValue swim_lengths_data = 25; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[SwimLengthsDataRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.SwimLengthsDataRollupValue)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### setSwimLengthsData(SwimLengthsDataRollupValue.Builder builderForValue)
    
    
    public DailyRollupDataPoint.Builder setSwimLengthsData(SwimLengthsDataRollupValue.Builder builderForValue)

Returned by default when rolling up data points from the `swim-lengths-data` data type, or when requested explicitly using the `swim-lengths-data` rollup type identifier.

`.google.devicesandservices.health.v4.SwimLengthsDataRollupValue swim_lengths_data = 25; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[SwimLengthsDataRollupValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.SwimLengthsDataRollupValue.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### setTimeInHeartRateZone(TimeInHeartRateZoneRollupValue value)
    
    
    public DailyRollupDataPoint.Builder setTimeInHeartRateZone(TimeInHeartRateZoneRollupValue value)

Returned by default when rolling up data points from the `time-in-heart-rate-zone` data type, or when requested explicitly using the `time-in-heart-rate-zone` rollup type identifier.

` .google.devicesandservices.health.v4.TimeInHeartRateZoneRollupValue time_in_heart_rate_zone = 23; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[TimeInHeartRateZoneRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.TimeInHeartRateZoneRollupValue)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### setTimeInHeartRateZone(TimeInHeartRateZoneRollupValue.Builder builderForValue)
    
    
    public DailyRollupDataPoint.Builder setTimeInHeartRateZone(TimeInHeartRateZoneRollupValue.Builder builderForValue)

Returned by default when rolling up data points from the `time-in-heart-rate-zone` data type, or when requested explicitly using the `time-in-heart-rate-zone` rollup type identifier.

` .google.devicesandservices.health.v4.TimeInHeartRateZoneRollupValue time_in_heart_rate_zone = 23; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[TimeInHeartRateZoneRollupValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.TimeInHeartRateZoneRollupValue.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### setTotalCalories(TotalCaloriesRollupValue value)
    
    
    public DailyRollupDataPoint.Builder setTotalCalories(TotalCaloriesRollupValue value)

Returned by default when rolling up data points from the `total-calories` data type, or when requested explicitly using the `total-calories` rollup type identifier.

`.google.devicesandservices.health.v4.TotalCaloriesRollupValue total_calories = 14; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[TotalCaloriesRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.TotalCaloriesRollupValue)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### setTotalCalories(TotalCaloriesRollupValue.Builder builderForValue)
    
    
    public DailyRollupDataPoint.Builder setTotalCalories(TotalCaloriesRollupValue.Builder builderForValue)

Returned by default when rolling up data points from the `total-calories` data type, or when requested explicitly using the `total-calories` rollup type identifier.

`.google.devicesandservices.health.v4.TotalCaloriesRollupValue total_calories = 14; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[TotalCaloriesRollupValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.TotalCaloriesRollupValue.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### setWeight(WeightRollupValue value)
    
    
    public DailyRollupDataPoint.Builder setWeight(WeightRollupValue value)

Returned by default when rolling up data points from the `weight` data type, or when requested explicitly using the `weight` rollup type identifier.

`.google.devicesandservices.health.v4.WeightRollupValue weight = 10;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[WeightRollupValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.WeightRollupValue)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
### setWeight(WeightRollupValue.Builder builderForValue)
    
    
    public DailyRollupDataPoint.Builder setWeight(WeightRollupValue.Builder builderForValue)

Returned by default when rolling up data points from the `weight` data type, or when requested explicitly using the `weight` rollup type identifier.

`.google.devicesandservices.health.v4.WeightRollupValue weight = 10;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[WeightRollupValue.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.WeightRollupValue.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollupDataPoint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollupDataPoint.Builder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
