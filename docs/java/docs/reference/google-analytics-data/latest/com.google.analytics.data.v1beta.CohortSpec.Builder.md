---
url: https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CohortSpec.Builder
title: Class CohortSpec.Builder (0.110.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:10:48.091431+00:00
---

# Class CohortSpec.Builder (0.110.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CohortSpec.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class CohortSpec.Builder (0.110.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.110.0 (latest)  0.106.0  0.105.0  0.104.0  0.102.0  0.99.0  0.98.0  0.96.0  0.94.0  0.93.0  0.92.0  0.91.0  0.89.0  0.87.0  0.86.0  0.85.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.75.0  0.74.0  0.73.0  0.71.0  0.70.0  0.69.0  0.68.0  0.67.0  0.66.0  0.65.0  0.64.0  0.63.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0 
    
    
    public static final class CohortSpec.Builder extends GeneratedMessage.Builder<CohortSpec.Builder> implements CohortSpecOrBuilder

The specification of cohorts for a cohort report.

Cohort reports create a time series of user retention for the cohort. For example, you could select the cohort of users that were acquired in the first week of September and follow that cohort for the next six weeks. Selecting the users acquired in the first week of September cohort is specified in the `cohort` object. Following that cohort for the next six weeks is specified in the `cohortsRange` object.

For examples, see [Cohort Report Examples](https://developers.google.com/analytics/devguides/reporting/data/v1/advanced#cohort_report_examples).

The report response could show a weekly time series where say your app has retained 60% of this cohort after three weeks and 25% of this cohort after six weeks. These two percentages can be calculated by the metric `cohortActiveUsers/cohortTotalUsers` and will be separate rows in the report.

Protobuf type `google.analytics.data.v1beta.CohortSpec`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > CohortSpec.Builder

## Implements

[CohortSpecOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CohortSpecOrBuilder)

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

### addAllCohorts(Iterable<? extends Cohort> values)
    
    
    public CohortSpec.Builder addAllCohorts(Iterable<? extends Cohort> values)

Defines the selection criteria to group users into cohorts.

Most cohort reports define only a single cohort. If multiple cohorts are specified, each cohort can be recognized in the report by their name.

`repeated .google.analytics.data.v1beta.Cohort cohorts = 1;`

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<? extends com.google.analytics.data.v1beta.Cohort>`  
  
**Returns**  
---  
**Type** | **Description**  
`[CohortSpec.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CohortSpec.Builder)` |   
  
### addCohorts(Cohort value)
    
    
    public CohortSpec.Builder addCohorts(Cohort value)

Defines the selection criteria to group users into cohorts.

Most cohort reports define only a single cohort. If multiple cohorts are specified, each cohort can be recognized in the report by their name.

`repeated .google.analytics.data.v1beta.Cohort cohorts = 1;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Cohort](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.Cohort)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CohortSpec.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CohortSpec.Builder)` |   
  
### addCohorts(Cohort.Builder builderForValue)
    
    
    public CohortSpec.Builder addCohorts(Cohort.Builder builderForValue)

Defines the selection criteria to group users into cohorts.

Most cohort reports define only a single cohort. If multiple cohorts are specified, each cohort can be recognized in the report by their name.

`repeated .google.analytics.data.v1beta.Cohort cohorts = 1;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Cohort.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.Cohort.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CohortSpec.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CohortSpec.Builder)` |   
  
### addCohorts(int index, Cohort value)
    
    
    public CohortSpec.Builder addCohorts(int index, Cohort value)

Defines the selection criteria to group users into cohorts.

Most cohort reports define only a single cohort. If multiple cohorts are specified, each cohort can be recognized in the report by their name.

`repeated .google.analytics.data.v1beta.Cohort cohorts = 1;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[Cohort](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.Cohort)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CohortSpec.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CohortSpec.Builder)` |   
  
### addCohorts(int index, Cohort.Builder builderForValue)
    
    
    public CohortSpec.Builder addCohorts(int index, Cohort.Builder builderForValue)

Defines the selection criteria to group users into cohorts.

Most cohort reports define only a single cohort. If multiple cohorts are specified, each cohort can be recognized in the report by their name.

`repeated .google.analytics.data.v1beta.Cohort cohorts = 1;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[Cohort.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.Cohort.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CohortSpec.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CohortSpec.Builder)` |   
  
### addCohortsBuilder()
    
    
    public Cohort.Builder addCohortsBuilder()

Defines the selection criteria to group users into cohorts.

Most cohort reports define only a single cohort. If multiple cohorts are specified, each cohort can be recognized in the report by their name.

`repeated .google.analytics.data.v1beta.Cohort cohorts = 1;`

**Returns**  
---  
**Type** | **Description**  
`[Cohort.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.Cohort.Builder)` |   
  
### addCohortsBuilder(int index)
    
    
    public Cohort.Builder addCohortsBuilder(int index)

Defines the selection criteria to group users into cohorts.

Most cohort reports define only a single cohort. If multiple cohorts are specified, each cohort can be recognized in the report by their name.

`repeated .google.analytics.data.v1beta.Cohort cohorts = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cohort.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.Cohort.Builder)` |   
  
### build()
    
    
    public CohortSpec build()

**Returns**  
---  
**Type** | **Description**  
`[CohortSpec](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CohortSpec)` |   
  
### buildPartial()
    
    
    public CohortSpec buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[CohortSpec](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CohortSpec)` |   
  
### clear()
    
    
    public CohortSpec.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[CohortSpec.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CohortSpec.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearCohortReportSettings()
    
    
    public CohortSpec.Builder clearCohortReportSettings()

Optional settings for a cohort report.

`.google.analytics.data.v1beta.CohortReportSettings cohort_report_settings = 3;`

**Returns**  
---  
**Type** | **Description**  
`[CohortSpec.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CohortSpec.Builder)` |   
  
### clearCohorts()
    
    
    public CohortSpec.Builder clearCohorts()

Defines the selection criteria to group users into cohorts.

Most cohort reports define only a single cohort. If multiple cohorts are specified, each cohort can be recognized in the report by their name.

`repeated .google.analytics.data.v1beta.Cohort cohorts = 1;`

**Returns**  
---  
**Type** | **Description**  
`[CohortSpec.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CohortSpec.Builder)` |   
  
### clearCohortsRange()
    
    
    public CohortSpec.Builder clearCohortsRange()

Cohort reports follow cohorts over an extended reporting date range. This range specifies an offset duration to follow the cohorts over.

`.google.analytics.data.v1beta.CohortsRange cohorts_range = 2;`

**Returns**  
---  
**Type** | **Description**  
`[CohortSpec.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CohortSpec.Builder)` |   
  
### getCohortReportSettings()
    
    
    public CohortReportSettings getCohortReportSettings()

Optional settings for a cohort report.

`.google.analytics.data.v1beta.CohortReportSettings cohort_report_settings = 3;`

**Returns**  
---  
**Type** | **Description**  
`[CohortReportSettings](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CohortReportSettings)` | The cohortReportSettings.  
  
### getCohortReportSettingsBuilder()
    
    
    public CohortReportSettings.Builder getCohortReportSettingsBuilder()

Optional settings for a cohort report.

`.google.analytics.data.v1beta.CohortReportSettings cohort_report_settings = 3;`

**Returns**  
---  
**Type** | **Description**  
`[CohortReportSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CohortReportSettings.Builder)` |   
  
### getCohortReportSettingsOrBuilder()
    
    
    public CohortReportSettingsOrBuilder getCohortReportSettingsOrBuilder()

Optional settings for a cohort report.

`.google.analytics.data.v1beta.CohortReportSettings cohort_report_settings = 3;`

**Returns**  
---  
**Type** | **Description**  
`[CohortReportSettingsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CohortReportSettingsOrBuilder)` |   
  
### getCohorts(int index)
    
    
    public Cohort getCohorts(int index)

Defines the selection criteria to group users into cohorts.

Most cohort reports define only a single cohort. If multiple cohorts are specified, each cohort can be recognized in the report by their name.

`repeated .google.analytics.data.v1beta.Cohort cohorts = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cohort](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.Cohort)` |   
  
### getCohortsBuilder(int index)
    
    
    public Cohort.Builder getCohortsBuilder(int index)

Defines the selection criteria to group users into cohorts.

Most cohort reports define only a single cohort. If multiple cohorts are specified, each cohort can be recognized in the report by their name.

`repeated .google.analytics.data.v1beta.Cohort cohorts = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cohort.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.Cohort.Builder)` |   
  
### getCohortsBuilderList()
    
    
    public List<Cohort.Builder> getCohortsBuilderList()

Defines the selection criteria to group users into cohorts.

Most cohort reports define only a single cohort. If multiple cohorts are specified, each cohort can be recognized in the report by their name.

`repeated .google.analytics.data.v1beta.Cohort cohorts = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.Cohort.Builder)>` |   
  
### getCohortsCount()
    
    
    public int getCohortsCount()

Defines the selection criteria to group users into cohorts.

Most cohort reports define only a single cohort. If multiple cohorts are specified, each cohort can be recognized in the report by their name.

`repeated .google.analytics.data.v1beta.Cohort cohorts = 1;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getCohortsList()
    
    
    public List<Cohort> getCohortsList()

Defines the selection criteria to group users into cohorts.

Most cohort reports define only a single cohort. If multiple cohorts are specified, each cohort can be recognized in the report by their name.

`repeated .google.analytics.data.v1beta.Cohort cohorts = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Cohort](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.Cohort)>` |   
  
### getCohortsOrBuilder(int index)
    
    
    public CohortOrBuilder getCohortsOrBuilder(int index)

Defines the selection criteria to group users into cohorts.

Most cohort reports define only a single cohort. If multiple cohorts are specified, each cohort can be recognized in the report by their name.

`repeated .google.analytics.data.v1beta.Cohort cohorts = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CohortOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CohortOrBuilder)` |   
  
### getCohortsOrBuilderList()
    
    
    public List<? extends CohortOrBuilder> getCohortsOrBuilderList()

Defines the selection criteria to group users into cohorts.

Most cohort reports define only a single cohort. If multiple cohorts are specified, each cohort can be recognized in the report by their name.

`repeated .google.analytics.data.v1beta.Cohort cohorts = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.analytics.data.v1beta.CohortOrBuilder>` |   
  
### getCohortsRange()
    
    
    public CohortsRange getCohortsRange()

Cohort reports follow cohorts over an extended reporting date range. This range specifies an offset duration to follow the cohorts over.

`.google.analytics.data.v1beta.CohortsRange cohorts_range = 2;`

**Returns**  
---  
**Type** | **Description**  
`[CohortsRange](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CohortsRange)` | The cohortsRange.  
  
### getCohortsRangeBuilder()
    
    
    public CohortsRange.Builder getCohortsRangeBuilder()

Cohort reports follow cohorts over an extended reporting date range. This range specifies an offset duration to follow the cohorts over.

`.google.analytics.data.v1beta.CohortsRange cohorts_range = 2;`

**Returns**  
---  
**Type** | **Description**  
`[CohortsRange.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CohortsRange.Builder)` |   
  
### getCohortsRangeOrBuilder()
    
    
    public CohortsRangeOrBuilder getCohortsRangeOrBuilder()

Cohort reports follow cohorts over an extended reporting date range. This range specifies an offset duration to follow the cohorts over.

`.google.analytics.data.v1beta.CohortsRange cohorts_range = 2;`

**Returns**  
---  
**Type** | **Description**  
`[CohortsRangeOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CohortsRangeOrBuilder)` |   
  
### getDefaultInstanceForType()
    
    
    public CohortSpec getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[CohortSpec](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CohortSpec)` |   
  
### getDescriptorForType()
    
    
    public Descriptors.Descriptor getDescriptorForType()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getDescriptorForType__)

### hasCohortReportSettings()
    
    
    public boolean hasCohortReportSettings()

Optional settings for a cohort report.

`.google.analytics.data.v1beta.CohortReportSettings cohort_report_settings = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the cohortReportSettings field is set.  
  
### hasCohortsRange()
    
    
    public boolean hasCohortsRange()

Cohort reports follow cohorts over an extended reporting date range. This range specifies an offset duration to follow the cohorts over.

`.google.analytics.data.v1beta.CohortsRange cohorts_range = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the cohortsRange field is set.  
  
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

### mergeCohortReportSettings(CohortReportSettings value)
    
    
    public CohortSpec.Builder mergeCohortReportSettings(CohortReportSettings value)

Optional settings for a cohort report.

`.google.analytics.data.v1beta.CohortReportSettings cohort_report_settings = 3;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[CohortReportSettings](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CohortReportSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CohortSpec.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CohortSpec.Builder)` |   
  
### mergeCohortsRange(CohortsRange value)
    
    
    public CohortSpec.Builder mergeCohortsRange(CohortsRange value)

Cohort reports follow cohorts over an extended reporting date range. This range specifies an offset duration to follow the cohorts over.

`.google.analytics.data.v1beta.CohortsRange cohorts_range = 2;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[CohortsRange](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CohortsRange)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CohortSpec.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CohortSpec.Builder)` |   
  
### mergeFrom(CohortSpec other)
    
    
    public CohortSpec.Builder mergeFrom(CohortSpec other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CohortSpec](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CohortSpec)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CohortSpec.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CohortSpec.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public CohortSpec.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CohortSpec.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CohortSpec.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public CohortSpec.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CohortSpec.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CohortSpec.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### removeCohorts(int index)
    
    
    public CohortSpec.Builder removeCohorts(int index)

Defines the selection criteria to group users into cohorts.

Most cohort reports define only a single cohort. If multiple cohorts are specified, each cohort can be recognized in the report by their name.

`repeated .google.analytics.data.v1beta.Cohort cohorts = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CohortSpec.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CohortSpec.Builder)` |   
  
### setCohortReportSettings(CohortReportSettings value)
    
    
    public CohortSpec.Builder setCohortReportSettings(CohortReportSettings value)

Optional settings for a cohort report.

`.google.analytics.data.v1beta.CohortReportSettings cohort_report_settings = 3;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[CohortReportSettings](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CohortReportSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CohortSpec.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CohortSpec.Builder)` |   
  
### setCohortReportSettings(CohortReportSettings.Builder builderForValue)
    
    
    public CohortSpec.Builder setCohortReportSettings(CohortReportSettings.Builder builderForValue)

Optional settings for a cohort report.

`.google.analytics.data.v1beta.CohortReportSettings cohort_report_settings = 3;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[CohortReportSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CohortReportSettings.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CohortSpec.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CohortSpec.Builder)` |   
  
### setCohorts(int index, Cohort value)
    
    
    public CohortSpec.Builder setCohorts(int index, Cohort value)

Defines the selection criteria to group users into cohorts.

Most cohort reports define only a single cohort. If multiple cohorts are specified, each cohort can be recognized in the report by their name.

`repeated .google.analytics.data.v1beta.Cohort cohorts = 1;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[Cohort](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.Cohort)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CohortSpec.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CohortSpec.Builder)` |   
  
### setCohorts(int index, Cohort.Builder builderForValue)
    
    
    public CohortSpec.Builder setCohorts(int index, Cohort.Builder builderForValue)

Defines the selection criteria to group users into cohorts.

Most cohort reports define only a single cohort. If multiple cohorts are specified, each cohort can be recognized in the report by their name.

`repeated .google.analytics.data.v1beta.Cohort cohorts = 1;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[Cohort.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.Cohort.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CohortSpec.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CohortSpec.Builder)` |   
  
### setCohortsRange(CohortsRange value)
    
    
    public CohortSpec.Builder setCohortsRange(CohortsRange value)

Cohort reports follow cohorts over an extended reporting date range. This range specifies an offset duration to follow the cohorts over.

`.google.analytics.data.v1beta.CohortsRange cohorts_range = 2;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[CohortsRange](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CohortsRange)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CohortSpec.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CohortSpec.Builder)` |   
  
### setCohortsRange(CohortsRange.Builder builderForValue)
    
    
    public CohortSpec.Builder setCohortsRange(CohortsRange.Builder builderForValue)

Cohort reports follow cohorts over an extended reporting date range. This range specifies an offset duration to follow the cohorts over.

`.google.analytics.data.v1beta.CohortsRange cohorts_range = 2;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[CohortsRange.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CohortsRange.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CohortSpec.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CohortSpec.Builder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
