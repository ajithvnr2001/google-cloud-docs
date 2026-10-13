---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference.Builder
title: Class QuotaPreference.Builder (0.67.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:10:33.995223+00:00
---

# Class QuotaPreference.Builder (0.67.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class QuotaPreference.Builder (0.67.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.67.0 (latest)  0.63.0  0.62.0  0.61.0  0.59.0  0.56.0  0.55.0  0.53.0  0.51.0  0.50.0  0.49.0  0.48.0  0.46.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.38.0  0.36.0  0.35.0  0.32.0  0.31.0  0.30.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static final class QuotaPreference.Builder extends GeneratedMessage.Builder<QuotaPreference.Builder> implements QuotaPreferenceOrBuilder

QuotaPreference represents the preferred quota configuration specified for a project, folder or organization. There is only one QuotaPreference resource for a quota value targeting a unique set of dimensions.

Protobuf type `google.api.cloudquotas.v1beta.QuotaPreference`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > QuotaPreference.Builder

## Implements

[QuotaPreferenceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreferenceOrBuilder)

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
    
    
    public QuotaPreference build()

**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference)` |   
  
### buildPartial()
    
    
    public QuotaPreference buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference)` |   
  
### clear()
    
    
    public QuotaPreference.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearContactEmail()
    
    
    public QuotaPreference.Builder clearContactEmail()

Input only. An email address that can be used to contact the user, in case Google Cloud needs more information to make a decision before additional quota can be granted.

When requesting a quota increase, the email address is required. When requesting a quota decrease, the email address is optional. For example, the email address is optional when the `QuotaConfig.preferred_value` is smaller than the `QuotaDetails.reset_value`.

`string contact_email = 12 [(.google.api.field_behavior) = INPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference.Builder)` | This builder for chaining.  
  
### clearCreateTime()
    
    
    public QuotaPreference.Builder clearCreateTime()

Output only. Create time stamp

` .google.protobuf.Timestamp create_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference.Builder)` |   
  
### clearDimensions()
    
    
    public QuotaPreference.Builder clearDimensions()

**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference.Builder)` |   
  
### clearEtag()
    
    
    public QuotaPreference.Builder clearEtag()

Optional. The current etag of the quota preference. If an etag is provided on update and does not match the current server's etag of the quota preference, the request will be blocked and an ABORTED error will be returned. See <https://google.aip.dev/134#etags> for more details on etags.

`string etag = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference.Builder)` | This builder for chaining.  
  
### clearJustification()
    
    
    public QuotaPreference.Builder clearJustification()

The reason / justification for this quota preference.

`string justification = 11;`

**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference.Builder)` | This builder for chaining.  
  
### clearName()
    
    
    public QuotaPreference.Builder clearName()

Required except in the CREATE requests. The resource name of the quota preference. The path that follows `/locations` must be `/global`. For example: `projects/123/locations/global/quotaPreferences/my-config-for-us-east1`

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference.Builder)` | This builder for chaining.  
  
### clearQuotaConfig()
    
    
    public QuotaPreference.Builder clearQuotaConfig()

Required. Preferred quota configuration.

` .google.api.cloudquotas.v1beta.QuotaConfig quota_config = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference.Builder)` |   
  
### clearQuotaId()
    
    
    public QuotaPreference.Builder clearQuotaId()

Required. The id of the quota to which the quota preference is applied. A quota name is unique in the service. For example, `CpusPerProjectPerRegion`

`string quota_id = 8 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference.Builder)` | This builder for chaining.  
  
### clearReconciling()
    
    
    public QuotaPreference.Builder clearReconciling()

Output only. Is the quota preference pending Google Cloud approval and fulfillment.

`bool reconciling = 10 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference.Builder)` | This builder for chaining.  
  
### clearService()
    
    
    public QuotaPreference.Builder clearService()

Required. The name of the service to which the quota preference is applied.

`string service = 7 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference.Builder)` | This builder for chaining.  
  
### clearUpdateTime()
    
    
    public QuotaPreference.Builder clearUpdateTime()

Output only. Update time stamp

` .google.protobuf.Timestamp update_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference.Builder)` |   
  
### containsDimensions(String key)
    
    
    public boolean containsDimensions(String key)

Immutable. The dimensions that this quota preference applies to. The key of the map entry is the name of a dimension, such as `region`, `zone`, `network_id`, and the value of the map entry is the dimension value.

If a dimension is missing from the map of dimensions, the quota preference applies to all the dimension values except for those that have other quota preferences configured for the specific value.

Note: QuotaPreferences can only be applied across all values of `user` and `resource` dimension. Do not set values for `user` or `resource` in the dimension map.

For example: `{"provider" : "Example Organization"}` where `provider` is a service-specific quota dimension and `Example Organization` is the provider name.

`map<string, string> dimensions = 2 [(.google.api.field_behavior) = IMMUTABLE]; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getContactEmail()
    
    
    public String getContactEmail()

Input only. An email address that can be used to contact the user, in case Google Cloud needs more information to make a decision before additional quota can be granted.

When requesting a quota increase, the email address is required. When requesting a quota decrease, the email address is optional. For example, the email address is optional when the `QuotaConfig.preferred_value` is smaller than the `QuotaDetails.reset_value`.

`string contact_email = 12 [(.google.api.field_behavior) = INPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The contactEmail.  
  
### getContactEmailBytes()
    
    
    public ByteString getContactEmailBytes()

Input only. An email address that can be used to contact the user, in case Google Cloud needs more information to make a decision before additional quota can be granted.

When requesting a quota increase, the email address is required. When requesting a quota decrease, the email address is optional. For example, the email address is optional when the `QuotaConfig.preferred_value` is smaller than the `QuotaDetails.reset_value`.

`string contact_email = 12 [(.google.api.field_behavior) = INPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for contactEmail.  
  
### getCreateTime()
    
    
    public Timestamp getCreateTime()

Output only. Create time stamp

` .google.protobuf.Timestamp create_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeBuilder()
    
    
    public Timestamp.Builder getCreateTimeBuilder()

Output only. Create time stamp

` .google.protobuf.Timestamp create_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)` |   
  
### getCreateTimeOrBuilder()
    
    
    public TimestampOrBuilder getCreateTimeOrBuilder()

Output only. Create time stamp

` .google.protobuf.Timestamp create_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDefaultInstanceForType()
    
    
    public QuotaPreference getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference)` |   
  
### getDescriptorForType()
    
    
    public Descriptors.Descriptor getDescriptorForType()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getDescriptorForType__)

### getDimensions() (deprecated)
    
    
    public Map<String,String> getDimensions()

Use [#getDimensionsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference.Builder#com_google_api_cloudquotas_v1beta_QuotaPreference_Builder_getDimensionsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getDimensionsCount()
    
    
    public int getDimensionsCount()

Immutable. The dimensions that this quota preference applies to. The key of the map entry is the name of a dimension, such as `region`, `zone`, `network_id`, and the value of the map entry is the dimension value.

If a dimension is missing from the map of dimensions, the quota preference applies to all the dimension values except for those that have other quota preferences configured for the specific value.

Note: QuotaPreferences can only be applied across all values of `user` and `resource` dimension. Do not set values for `user` or `resource` in the dimension map.

For example: `{"provider" : "Example Organization"}` where `provider` is a service-specific quota dimension and `Example Organization` is the provider name.

`map<string, string> dimensions = 2 [(.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getDimensionsMap()
    
    
    public Map<String,String> getDimensionsMap()

Immutable. The dimensions that this quota preference applies to. The key of the map entry is the name of a dimension, such as `region`, `zone`, `network_id`, and the value of the map entry is the dimension value.

If a dimension is missing from the map of dimensions, the quota preference applies to all the dimension values except for those that have other quota preferences configured for the specific value.

Note: QuotaPreferences can only be applied across all values of `user` and `resource` dimension. Do not set values for `user` or `resource` in the dimension map.

For example: `{"provider" : "Example Organization"}` where `provider` is a service-specific quota dimension and `Example Organization` is the provider name.

`map<string, string> dimensions = 2 [(.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getDimensionsOrDefault(String key, String defaultValue)
    
    
    public String getDimensionsOrDefault(String key, String defaultValue)

Immutable. The dimensions that this quota preference applies to. The key of the map entry is the name of a dimension, such as `region`, `zone`, `network_id`, and the value of the map entry is the dimension value.

If a dimension is missing from the map of dimensions, the quota preference applies to all the dimension values except for those that have other quota preferences configured for the specific value.

Note: QuotaPreferences can only be applied across all values of `user` and `resource` dimension. Do not set values for `user` or `resource` in the dimension map.

For example: `{"provider" : "Example Organization"}` where `provider` is a service-specific quota dimension and `Example Organization` is the provider name.

`map<string, string> dimensions = 2 [(.google.api.field_behavior) = IMMUTABLE]; `

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getDimensionsOrThrow(String key)
    
    
    public String getDimensionsOrThrow(String key)

Immutable. The dimensions that this quota preference applies to. The key of the map entry is the name of a dimension, such as `region`, `zone`, `network_id`, and the value of the map entry is the dimension value.

If a dimension is missing from the map of dimensions, the quota preference applies to all the dimension values except for those that have other quota preferences configured for the specific value.

Note: QuotaPreferences can only be applied across all values of `user` and `resource` dimension. Do not set values for `user` or `resource` in the dimension map.

For example: `{"provider" : "Example Organization"}` where `provider` is a service-specific quota dimension and `Example Organization` is the provider name.

`map<string, string> dimensions = 2 [(.google.api.field_behavior) = IMMUTABLE]; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getEtag()
    
    
    public String getEtag()

Optional. The current etag of the quota preference. If an etag is provided on update and does not match the current server's etag of the quota preference, the request will be blocked and an ABORTED error will be returned. See <https://google.aip.dev/134#etags> for more details on etags.

`string etag = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The etag.  
  
### getEtagBytes()
    
    
    public ByteString getEtagBytes()

Optional. The current etag of the quota preference. If an etag is provided on update and does not match the current server's etag of the quota preference, the request will be blocked and an ABORTED error will be returned. See <https://google.aip.dev/134#etags> for more details on etags.

`string etag = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for etag.  
  
### getJustification()
    
    
    public String getJustification()

The reason / justification for this quota preference.

`string justification = 11;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The justification.  
  
### getJustificationBytes()
    
    
    public ByteString getJustificationBytes()

The reason / justification for this quota preference.

`string justification = 11;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for justification.  
  
### getMutableDimensions() (deprecated)
    
    
    public Map<String,String> getMutableDimensions()

Use alternate mutation accessors instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getName()
    
    
    public String getName()

Required except in the CREATE requests. The resource name of the quota preference. The path that follows `/locations` must be `/global`. For example: `projects/123/locations/global/quotaPreferences/my-config-for-us-east1`

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public ByteString getNameBytes()

Required except in the CREATE requests. The resource name of the quota preference. The path that follows `/locations` must be `/global`. For example: `projects/123/locations/global/quotaPreferences/my-config-for-us-east1`

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getQuotaConfig()
    
    
    public QuotaConfig getQuotaConfig()

Required. Preferred quota configuration.

` .google.api.cloudquotas.v1beta.QuotaConfig quota_config = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[QuotaConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaConfig)` | The quotaConfig.  
  
### getQuotaConfigBuilder()
    
    
    public QuotaConfig.Builder getQuotaConfigBuilder()

Required. Preferred quota configuration.

` .google.api.cloudquotas.v1beta.QuotaConfig quota_config = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[QuotaConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaConfig.Builder)` |   
  
### getQuotaConfigOrBuilder()
    
    
    public QuotaConfigOrBuilder getQuotaConfigOrBuilder()

Required. Preferred quota configuration.

` .google.api.cloudquotas.v1beta.QuotaConfig quota_config = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[QuotaConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaConfigOrBuilder)` |   
  
### getQuotaId()
    
    
    public String getQuotaId()

Required. The id of the quota to which the quota preference is applied. A quota name is unique in the service. For example, `CpusPerProjectPerRegion`

`string quota_id = 8 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The quotaId.  
  
### getQuotaIdBytes()
    
    
    public ByteString getQuotaIdBytes()

Required. The id of the quota to which the quota preference is applied. A quota name is unique in the service. For example, `CpusPerProjectPerRegion`

`string quota_id = 8 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for quotaId.  
  
### getReconciling()
    
    
    public boolean getReconciling()

Output only. Is the quota preference pending Google Cloud approval and fulfillment.

`bool reconciling = 10 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The reconciling.  
  
### getService()
    
    
    public String getService()

Required. The name of the service to which the quota preference is applied.

`string service = 7 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The service.  
  
### getServiceBytes()
    
    
    public ByteString getServiceBytes()

Required. The name of the service to which the quota preference is applied.

`string service = 7 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for service.  
  
### getUpdateTime()
    
    
    public Timestamp getUpdateTime()

Output only. Update time stamp

` .google.protobuf.Timestamp update_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The updateTime.  
  
### getUpdateTimeBuilder()
    
    
    public Timestamp.Builder getUpdateTimeBuilder()

Output only. Update time stamp

` .google.protobuf.Timestamp update_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)` |   
  
### getUpdateTimeOrBuilder()
    
    
    public TimestampOrBuilder getUpdateTimeOrBuilder()

Output only. Update time stamp

` .google.protobuf.Timestamp update_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### hasCreateTime()
    
    
    public boolean hasCreateTime()

Output only. Create time stamp

` .google.protobuf.Timestamp create_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasQuotaConfig()
    
    
    public boolean hasQuotaConfig()

Required. Preferred quota configuration.

` .google.api.cloudquotas.v1beta.QuotaConfig quota_config = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the quotaConfig field is set.  
  
### hasUpdateTime()
    
    
    public boolean hasUpdateTime()

Output only. Update time stamp

` .google.protobuf.Timestamp update_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

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

### mergeCreateTime(Timestamp value)
    
    
    public QuotaPreference.Builder mergeCreateTime(Timestamp value)

Output only. Create time stamp

` .google.protobuf.Timestamp create_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference.Builder)` |   
  
### mergeFrom(QuotaPreference other)
    
    
    public QuotaPreference.Builder mergeFrom(QuotaPreference other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[QuotaPreference](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference)`  
  
**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public QuotaPreference.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public QuotaPreference.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### mergeQuotaConfig(QuotaConfig value)
    
    
    public QuotaPreference.Builder mergeQuotaConfig(QuotaConfig value)

Required. Preferred quota configuration.

` .google.api.cloudquotas.v1beta.QuotaConfig quota_config = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[QuotaConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference.Builder)` |   
  
### mergeUpdateTime(Timestamp value)
    
    
    public QuotaPreference.Builder mergeUpdateTime(Timestamp value)

Output only. Update time stamp

` .google.protobuf.Timestamp update_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference.Builder)` |   
  
### putAllDimensions(Map<String,String> values)
    
    
    public QuotaPreference.Builder putAllDimensions(Map<String,String> values)

Immutable. The dimensions that this quota preference applies to. The key of the map entry is the name of a dimension, such as `region`, `zone`, `network_id`, and the value of the map entry is the dimension value.

If a dimension is missing from the map of dimensions, the quota preference applies to all the dimension values except for those that have other quota preferences configured for the specific value.

Note: QuotaPreferences can only be applied across all values of `user` and `resource` dimension. Do not set values for `user` or `resource` in the dimension map.

For example: `{"provider" : "Example Organization"}` where `provider` is a service-specific quota dimension and `Example Organization` is the provider name.

`map<string, string> dimensions = 2 [(.google.api.field_behavior) = IMMUTABLE]; `

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference.Builder)` |   
  
### putDimensions(String key, String value)
    
    
    public QuotaPreference.Builder putDimensions(String key, String value)

Immutable. The dimensions that this quota preference applies to. The key of the map entry is the name of a dimension, such as `region`, `zone`, `network_id`, and the value of the map entry is the dimension value.

If a dimension is missing from the map of dimensions, the quota preference applies to all the dimension values except for those that have other quota preferences configured for the specific value.

Note: QuotaPreferences can only be applied across all values of `user` and `resource` dimension. Do not set values for `user` or `resource` in the dimension map.

For example: `{"provider" : "Example Organization"}` where `provider` is a service-specific quota dimension and `Example Organization` is the provider name.

`map<string, string> dimensions = 2 [(.google.api.field_behavior) = IMMUTABLE]; `

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference.Builder)` |   
  
### removeDimensions(String key)
    
    
    public QuotaPreference.Builder removeDimensions(String key)

Immutable. The dimensions that this quota preference applies to. The key of the map entry is the name of a dimension, such as `region`, `zone`, `network_id`, and the value of the map entry is the dimension value.

If a dimension is missing from the map of dimensions, the quota preference applies to all the dimension values except for those that have other quota preferences configured for the specific value.

Note: QuotaPreferences can only be applied across all values of `user` and `resource` dimension. Do not set values for `user` or `resource` in the dimension map.

For example: `{"provider" : "Example Organization"}` where `provider` is a service-specific quota dimension and `Example Organization` is the provider name.

`map<string, string> dimensions = 2 [(.google.api.field_behavior) = IMMUTABLE]; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference.Builder)` |   
  
### setContactEmail(String value)
    
    
    public QuotaPreference.Builder setContactEmail(String value)

Input only. An email address that can be used to contact the user, in case Google Cloud needs more information to make a decision before additional quota can be granted.

When requesting a quota increase, the email address is required. When requesting a quota decrease, the email address is optional. For example, the email address is optional when the `QuotaConfig.preferred_value` is smaller than the `QuotaDetails.reset_value`.

`string contact_email = 12 [(.google.api.field_behavior) = INPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The contactEmail to set.  
**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference.Builder)` | This builder for chaining.  
  
### setContactEmailBytes(ByteString value)
    
    
    public QuotaPreference.Builder setContactEmailBytes(ByteString value)

Input only. An email address that can be used to contact the user, in case Google Cloud needs more information to make a decision before additional quota can be granted.

When requesting a quota increase, the email address is required. When requesting a quota decrease, the email address is optional. For example, the email address is optional when the `QuotaConfig.preferred_value` is smaller than the `QuotaDetails.reset_value`.

`string contact_email = 12 [(.google.api.field_behavior) = INPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for contactEmail to set.  
**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference.Builder)` | This builder for chaining.  
  
### setCreateTime(Timestamp value)
    
    
    public QuotaPreference.Builder setCreateTime(Timestamp value)

Output only. Create time stamp

` .google.protobuf.Timestamp create_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference.Builder)` |   
  
### setCreateTime(Timestamp.Builder builderForValue)
    
    
    public QuotaPreference.Builder setCreateTime(Timestamp.Builder builderForValue)

Output only. Create time stamp

` .google.protobuf.Timestamp create_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference.Builder)` |   
  
### setEtag(String value)
    
    
    public QuotaPreference.Builder setEtag(String value)

Optional. The current etag of the quota preference. If an etag is provided on update and does not match the current server's etag of the quota preference, the request will be blocked and an ABORTED error will be returned. See <https://google.aip.dev/134#etags> for more details on etags.

`string etag = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The etag to set.  
**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference.Builder)` | This builder for chaining.  
  
### setEtagBytes(ByteString value)
    
    
    public QuotaPreference.Builder setEtagBytes(ByteString value)

Optional. The current etag of the quota preference. If an etag is provided on update and does not match the current server's etag of the quota preference, the request will be blocked and an ABORTED error will be returned. See <https://google.aip.dev/134#etags> for more details on etags.

`string etag = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for etag to set.  
**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference.Builder)` | This builder for chaining.  
  
### setJustification(String value)
    
    
    public QuotaPreference.Builder setJustification(String value)

The reason / justification for this quota preference.

`string justification = 11;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The justification to set.  
**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference.Builder)` | This builder for chaining.  
  
### setJustificationBytes(ByteString value)
    
    
    public QuotaPreference.Builder setJustificationBytes(ByteString value)

The reason / justification for this quota preference.

`string justification = 11;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for justification to set.  
**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference.Builder)` | This builder for chaining.  
  
### setName(String value)
    
    
    public QuotaPreference.Builder setName(String value)

Required except in the CREATE requests. The resource name of the quota preference. The path that follows `/locations` must be `/global`. For example: `projects/123/locations/global/quotaPreferences/my-config-for-us-east1`

`string name = 1;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name to set.  
**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference.Builder)` | This builder for chaining.  
  
### setNameBytes(ByteString value)
    
    
    public QuotaPreference.Builder setNameBytes(ByteString value)

Required except in the CREATE requests. The resource name of the quota preference. The path that follows `/locations` must be `/global`. For example: `projects/123/locations/global/quotaPreferences/my-config-for-us-east1`

`string name = 1;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for name to set.  
**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference.Builder)` | This builder for chaining.  
  
### setQuotaConfig(QuotaConfig value)
    
    
    public QuotaPreference.Builder setQuotaConfig(QuotaConfig value)

Required. Preferred quota configuration.

` .google.api.cloudquotas.v1beta.QuotaConfig quota_config = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[QuotaConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference.Builder)` |   
  
### setQuotaConfig(QuotaConfig.Builder builderForValue)
    
    
    public QuotaPreference.Builder setQuotaConfig(QuotaConfig.Builder builderForValue)

Required. Preferred quota configuration.

` .google.api.cloudquotas.v1beta.QuotaConfig quota_config = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[QuotaConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference.Builder)` |   
  
### setQuotaId(String value)
    
    
    public QuotaPreference.Builder setQuotaId(String value)

Required. The id of the quota to which the quota preference is applied. A quota name is unique in the service. For example, `CpusPerProjectPerRegion`

`string quota_id = 8 [(.google.api.field_behavior) = REQUIRED];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The quotaId to set.  
**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference.Builder)` | This builder for chaining.  
  
### setQuotaIdBytes(ByteString value)
    
    
    public QuotaPreference.Builder setQuotaIdBytes(ByteString value)

Required. The id of the quota to which the quota preference is applied. A quota name is unique in the service. For example, `CpusPerProjectPerRegion`

`string quota_id = 8 [(.google.api.field_behavior) = REQUIRED];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for quotaId to set.  
**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference.Builder)` | This builder for chaining.  
  
### setReconciling(boolean value)
    
    
    public QuotaPreference.Builder setReconciling(boolean value)

Output only. Is the quota preference pending Google Cloud approval and fulfillment.

`bool reconciling = 10 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The reconciling to set.  
**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference.Builder)` | This builder for chaining.  
  
### setService(String value)
    
    
    public QuotaPreference.Builder setService(String value)

Required. The name of the service to which the quota preference is applied.

`string service = 7 [(.google.api.field_behavior) = REQUIRED];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The service to set.  
**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference.Builder)` | This builder for chaining.  
  
### setServiceBytes(ByteString value)
    
    
    public QuotaPreference.Builder setServiceBytes(ByteString value)

Required. The name of the service to which the quota preference is applied.

`string service = 7 [(.google.api.field_behavior) = REQUIRED];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for service to set.  
**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference.Builder)` | This builder for chaining.  
  
### setUpdateTime(Timestamp value)
    
    
    public QuotaPreference.Builder setUpdateTime(Timestamp value)

Output only. Update time stamp

` .google.protobuf.Timestamp update_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference.Builder)` |   
  
### setUpdateTime(Timestamp.Builder builderForValue)
    
    
    public QuotaPreference.Builder setUpdateTime(Timestamp.Builder builderForValue)

Output only. Update time stamp

` .google.protobuf.Timestamp update_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference.Builder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
