---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1beta1.Finding.Builder
title: Class Finding.Builder (2.107.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:35:32.815941+00:00
---

# Class Finding.Builder (2.107.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1beta1.Finding.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class Finding.Builder (2.107.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.107.0 (latest)  2.103.0  2.102.0  2.101.0  2.99.0  2.96.0  2.95.0  2.93.0  2.91.0  2.90.0  2.88.0  2.86.0  2.84.0  2.83.0  2.82.0  2.81.0  2.80.0  2.78.0  2.76.0  2.75.0  2.72.0  2.71.0  2.70.0  2.68.0  2.67.0  2.66.0  2.65.0  2.64.0  2.63.0  2.62.0  2.61.0  2.60.0  2.59.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.1  2.10.0  2.9.0  2.8.0  2.7.1  2.6.0  2.5.6  2.3.2 
    
    
    public static final class Finding.Builder extends GeneratedMessage.Builder<Finding.Builder> implements FindingOrBuilder

Security Command Center finding.

A finding is a record of assessment data (security, risk, health or privacy) ingested into Security Command Center for presentation, notification, analysis, policy testing, and enforcement. For example, an XSS vulnerability in an App Engine application is a finding.

Protobuf type `google.cloud.securitycenter.v1beta1.Finding`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > Finding.Builder

## Implements

[FindingOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1beta1.FindingOrBuilder)

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
    
    
    public Finding build()

**Returns**  
---  
**Type** | **Description**  
`[Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1beta1.Finding)` |   
  
### buildPartial()
    
    
    public Finding buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1beta1.Finding)` |   
  
### clear()
    
    
    public Finding.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[Finding.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1beta1.Finding.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearCategory()
    
    
    public Finding.Builder clearCategory()

The additional taxonomy group within findings from a given source. This field is immutable after creation time. Example: "XSS_FLASH_INJECTION"

`string category = 5;`

**Returns**  
---  
**Type** | **Description**  
`[Finding.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1beta1.Finding.Builder)` | This builder for chaining.  
  
### clearCreateTime()
    
    
    public Finding.Builder clearCreateTime()

The time at which the finding was created in Security Command Center.

`.google.protobuf.Timestamp create_time = 10;`

**Returns**  
---  
**Type** | **Description**  
`[Finding.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1beta1.Finding.Builder)` |   
  
### clearEventTime()
    
    
    public Finding.Builder clearEventTime()

The time at which the event took place, or when an update to the finding occurred. For example, if the finding represents an open firewall it would capture the time the detector believes the firewall became open. The accuracy is determined by the detector. If the finding were to be resolved afterward, this time would reflect when the finding was resolved.

`.google.protobuf.Timestamp event_time = 9;`

**Returns**  
---  
**Type** | **Description**  
`[Finding.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1beta1.Finding.Builder)` |   
  
### clearExternalUri()
    
    
    public Finding.Builder clearExternalUri()

The URI that, if available, points to a web page outside of Security Command Center where additional information about the finding can be found. This field is guaranteed to be either empty or a well formed URL.

`string external_uri = 6;`

**Returns**  
---  
**Type** | **Description**  
`[Finding.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1beta1.Finding.Builder)` | This builder for chaining.  
  
### clearName()
    
    
    public Finding.Builder clearName()

The relative resource name of this finding. See: <https://cloud.google.com/apis/design/resource_names#relative_resource_name> Example: "organizations/{organization_id}/sources/{source_id}/findings/{finding_id}"

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[Finding.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1beta1.Finding.Builder)` | This builder for chaining.  
  
### clearParent()
    
    
    public Finding.Builder clearParent()

Immutable. The relative resource name of the source the finding belongs to. See: <https://cloud.google.com/apis/design/resource_names#relative_resource_name> This field is immutable after creation time. For example: "organizations/{organization_id}/sources/{source_id}"

`string parent = 2 [(.google.api.field_behavior) = IMMUTABLE];`

**Returns**  
---  
**Type** | **Description**  
`[Finding.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1beta1.Finding.Builder)` | This builder for chaining.  
  
### clearResourceName()
    
    
    public Finding.Builder clearResourceName()

For findings on Google Cloud resources, the full resource name of the Google Cloud resource this finding is for. See: <https://cloud.google.com/apis/design/resource_names#full_resource_name> When the finding is for a non-Google Cloud resource, the resourceName can be a customer or partner defined string. This field is immutable after creation time.

`string resource_name = 3;`

**Returns**  
---  
**Type** | **Description**  
`[Finding.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1beta1.Finding.Builder)` | This builder for chaining.  
  
### clearSecurityMarks()
    
    
    public Finding.Builder clearSecurityMarks()

Output only. User specified security marks. These marks are entirely managed by the user and come from the SecurityMarks resource that belongs to the finding.

` .google.cloud.securitycenter.v1beta1.SecurityMarks security_marks = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Finding.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1beta1.Finding.Builder)` |   
  
### clearSourceProperties()
    
    
    public Finding.Builder clearSourceProperties()

**Returns**  
---  
**Type** | **Description**  
`[Finding.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1beta1.Finding.Builder)` |   
  
### clearState()
    
    
    public Finding.Builder clearState()

The state of the finding.

`.google.cloud.securitycenter.v1beta1.Finding.State state = 4;`

**Returns**  
---  
**Type** | **Description**  
`[Finding.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1beta1.Finding.Builder)` | This builder for chaining.  
  
### containsSourceProperties(String key)
    
    
    public boolean containsSourceProperties(String key)

Source specific properties. These properties are managed by the source that writes the finding. The key names in the source_properties map must be between 1 and 255 characters, and must start with a letter and contain alphanumeric characters or underscores only.

`map<string, .google.protobuf.Value> source_properties = 7;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getCategory()
    
    
    public String getCategory()

The additional taxonomy group within findings from a given source. This field is immutable after creation time. Example: "XSS_FLASH_INJECTION"

`string category = 5;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The category.  
  
### getCategoryBytes()
    
    
    public ByteString getCategoryBytes()

The additional taxonomy group within findings from a given source. This field is immutable after creation time. Example: "XSS_FLASH_INJECTION"

`string category = 5;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for category.  
  
### getCreateTime()
    
    
    public Timestamp getCreateTime()

The time at which the finding was created in Security Command Center.

`.google.protobuf.Timestamp create_time = 10;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeBuilder()
    
    
    public Timestamp.Builder getCreateTimeBuilder()

The time at which the finding was created in Security Command Center.

`.google.protobuf.Timestamp create_time = 10;`

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)` |   
  
### getCreateTimeOrBuilder()
    
    
    public TimestampOrBuilder getCreateTimeOrBuilder()

The time at which the finding was created in Security Command Center.

`.google.protobuf.Timestamp create_time = 10;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDefaultInstanceForType()
    
    
    public Finding getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1beta1.Finding)` |   
  
### getDescriptorForType()
    
    
    public Descriptors.Descriptor getDescriptorForType()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getDescriptorForType__)

### getEventTime()
    
    
    public Timestamp getEventTime()

The time at which the event took place, or when an update to the finding occurred. For example, if the finding represents an open firewall it would capture the time the detector believes the firewall became open. The accuracy is determined by the detector. If the finding were to be resolved afterward, this time would reflect when the finding was resolved.

`.google.protobuf.Timestamp event_time = 9;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The eventTime.  
  
### getEventTimeBuilder()
    
    
    public Timestamp.Builder getEventTimeBuilder()

The time at which the event took place, or when an update to the finding occurred. For example, if the finding represents an open firewall it would capture the time the detector believes the firewall became open. The accuracy is determined by the detector. If the finding were to be resolved afterward, this time would reflect when the finding was resolved.

`.google.protobuf.Timestamp event_time = 9;`

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)` |   
  
### getEventTimeOrBuilder()
    
    
    public TimestampOrBuilder getEventTimeOrBuilder()

The time at which the event took place, or when an update to the finding occurred. For example, if the finding represents an open firewall it would capture the time the detector believes the firewall became open. The accuracy is determined by the detector. If the finding were to be resolved afterward, this time would reflect when the finding was resolved.

`.google.protobuf.Timestamp event_time = 9;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getExternalUri()
    
    
    public String getExternalUri()

The URI that, if available, points to a web page outside of Security Command Center where additional information about the finding can be found. This field is guaranteed to be either empty or a well formed URL.

`string external_uri = 6;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The externalUri.  
  
### getExternalUriBytes()
    
    
    public ByteString getExternalUriBytes()

The URI that, if available, points to a web page outside of Security Command Center where additional information about the finding can be found. This field is guaranteed to be either empty or a well formed URL.

`string external_uri = 6;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for externalUri.  
  
### getMutableSourceProperties() (deprecated)
    
    
    public Map<String,Value> getMutableSourceProperties()

Use alternate mutation accessors instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[Value](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html)>` |   
  
### getName()
    
    
    public String getName()

The relative resource name of this finding. See: <https://cloud.google.com/apis/design/resource_names#relative_resource_name> Example: "organizations/{organization_id}/sources/{source_id}/findings/{finding_id}"

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public ByteString getNameBytes()

The relative resource name of this finding. See: <https://cloud.google.com/apis/design/resource_names#relative_resource_name> Example: "organizations/{organization_id}/sources/{source_id}/findings/{finding_id}"

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getParent()
    
    
    public String getParent()

Immutable. The relative resource name of the source the finding belongs to. See: <https://cloud.google.com/apis/design/resource_names#relative_resource_name> This field is immutable after creation time. For example: "organizations/{organization_id}/sources/{source_id}"

`string parent = 2 [(.google.api.field_behavior) = IMMUTABLE];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The parent.  
  
### getParentBytes()
    
    
    public ByteString getParentBytes()

Immutable. The relative resource name of the source the finding belongs to. See: <https://cloud.google.com/apis/design/resource_names#relative_resource_name> This field is immutable after creation time. For example: "organizations/{organization_id}/sources/{source_id}"

`string parent = 2 [(.google.api.field_behavior) = IMMUTABLE];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for parent.  
  
### getResourceName()
    
    
    public String getResourceName()

For findings on Google Cloud resources, the full resource name of the Google Cloud resource this finding is for. See: <https://cloud.google.com/apis/design/resource_names#full_resource_name> When the finding is for a non-Google Cloud resource, the resourceName can be a customer or partner defined string. This field is immutable after creation time.

`string resource_name = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The resourceName.  
  
### getResourceNameBytes()
    
    
    public ByteString getResourceNameBytes()

For findings on Google Cloud resources, the full resource name of the Google Cloud resource this finding is for. See: <https://cloud.google.com/apis/design/resource_names#full_resource_name> When the finding is for a non-Google Cloud resource, the resourceName can be a customer or partner defined string. This field is immutable after creation time.

`string resource_name = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for resourceName.  
  
### getSecurityMarks()
    
    
    public SecurityMarks getSecurityMarks()

Output only. User specified security marks. These marks are entirely managed by the user and come from the SecurityMarks resource that belongs to the finding.

` .google.cloud.securitycenter.v1beta1.SecurityMarks security_marks = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[SecurityMarks](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1beta1.SecurityMarks)` | The securityMarks.  
  
### getSecurityMarksBuilder()
    
    
    public SecurityMarks.Builder getSecurityMarksBuilder()

Output only. User specified security marks. These marks are entirely managed by the user and come from the SecurityMarks resource that belongs to the finding.

` .google.cloud.securitycenter.v1beta1.SecurityMarks security_marks = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[SecurityMarks.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1beta1.SecurityMarks.Builder)` |   
  
### getSecurityMarksOrBuilder()
    
    
    public SecurityMarksOrBuilder getSecurityMarksOrBuilder()

Output only. User specified security marks. These marks are entirely managed by the user and come from the SecurityMarks resource that belongs to the finding.

` .google.cloud.securitycenter.v1beta1.SecurityMarks security_marks = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[SecurityMarksOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1beta1.SecurityMarksOrBuilder)` |   
  
### getSourceProperties() (deprecated)
    
    
    public Map<String,Value> getSourceProperties()

Use [#getSourcePropertiesMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1beta1.Finding.Builder#com_google_cloud_securitycenter_v1beta1_Finding_Builder_getSourcePropertiesMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[Value](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html)>` |   
  
### getSourcePropertiesCount()
    
    
    public int getSourcePropertiesCount()

Source specific properties. These properties are managed by the source that writes the finding. The key names in the source_properties map must be between 1 and 255 characters, and must start with a letter and contain alphanumeric characters or underscores only.

`map<string, .google.protobuf.Value> source_properties = 7;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getSourcePropertiesMap()
    
    
    public Map<String,Value> getSourcePropertiesMap()

Source specific properties. These properties are managed by the source that writes the finding. The key names in the source_properties map must be between 1 and 255 characters, and must start with a letter and contain alphanumeric characters or underscores only.

`map<string, .google.protobuf.Value> source_properties = 7;`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[Value](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html)>` |   
  
### getSourcePropertiesOrDefault(String key, Value defaultValue)
    
    
    public Value getSourcePropertiesOrDefault(String key, Value defaultValue)

Source specific properties. These properties are managed by the source that writes the finding. The key names in the source_properties map must be between 1 and 255 characters, and must start with a letter and contain alphanumeric characters or underscores only.

`map<string, .google.protobuf.Value> source_properties = 7;`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[Value](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Value](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html)` |   
  
### getSourcePropertiesOrThrow(String key)
    
    
    public Value getSourcePropertiesOrThrow(String key)

Source specific properties. These properties are managed by the source that writes the finding. The key names in the source_properties map must be between 1 and 255 characters, and must start with a letter and contain alphanumeric characters or underscores only.

`map<string, .google.protobuf.Value> source_properties = 7;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Value](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html)` |   
  
### getState()
    
    
    public Finding.State getState()

The state of the finding.

`.google.cloud.securitycenter.v1beta1.Finding.State state = 4;`

**Returns**  
---  
**Type** | **Description**  
`[Finding.State](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1beta1.Finding.State)` | The state.  
  
### getStateValue()
    
    
    public int getStateValue()

The state of the finding.

`.google.cloud.securitycenter.v1beta1.Finding.State state = 4;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for state.  
  
### hasCreateTime()
    
    
    public boolean hasCreateTime()

The time at which the finding was created in Security Command Center.

`.google.protobuf.Timestamp create_time = 10;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasEventTime()
    
    
    public boolean hasEventTime()

The time at which the event took place, or when an update to the finding occurred. For example, if the finding represents an open firewall it would capture the time the detector believes the firewall became open. The accuracy is determined by the detector. If the finding were to be resolved afterward, this time would reflect when the finding was resolved.

`.google.protobuf.Timestamp event_time = 9;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the eventTime field is set.  
  
### hasSecurityMarks()
    
    
    public boolean hasSecurityMarks()

Output only. User specified security marks. These marks are entirely managed by the user and come from the SecurityMarks resource that belongs to the finding.

` .google.cloud.securitycenter.v1beta1.SecurityMarks security_marks = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the securityMarks field is set.  
  
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
    
    
    public Finding.Builder mergeCreateTime(Timestamp value)

The time at which the finding was created in Security Command Center.

`.google.protobuf.Timestamp create_time = 10;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Finding.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1beta1.Finding.Builder)` |   
  
### mergeEventTime(Timestamp value)
    
    
    public Finding.Builder mergeEventTime(Timestamp value)

The time at which the event took place, or when an update to the finding occurred. For example, if the finding represents an open firewall it would capture the time the detector believes the firewall became open. The accuracy is determined by the detector. If the finding were to be resolved afterward, this time would reflect when the finding was resolved.

`.google.protobuf.Timestamp event_time = 9;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Finding.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1beta1.Finding.Builder)` |   
  
### mergeFrom(Finding other)
    
    
    public Finding.Builder mergeFrom(Finding other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1beta1.Finding)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Finding.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1beta1.Finding.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public Finding.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Finding.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1beta1.Finding.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public Finding.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Finding.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1beta1.Finding.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### mergeSecurityMarks(SecurityMarks value)
    
    
    public Finding.Builder mergeSecurityMarks(SecurityMarks value)

Output only. User specified security marks. These marks are entirely managed by the user and come from the SecurityMarks resource that belongs to the finding.

` .google.cloud.securitycenter.v1beta1.SecurityMarks security_marks = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[SecurityMarks](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1beta1.SecurityMarks)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Finding.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1beta1.Finding.Builder)` |   
  
### putAllSourceProperties(Map<String,Value> values)
    
    
    public Finding.Builder putAllSourceProperties(Map<String,Value> values)

Source specific properties. These properties are managed by the source that writes the finding. The key names in the source_properties map must be between 1 and 255 characters, and must start with a letter and contain alphanumeric characters or underscores only.

`map<string, .google.protobuf.Value> source_properties = 7;`

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[Value](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[Finding.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1beta1.Finding.Builder)` |   
  
### putSourceProperties(String key, Value value)
    
    
    public Finding.Builder putSourceProperties(String key, Value value)

Source specific properties. These properties are managed by the source that writes the finding. The key names in the source_properties map must be between 1 and 255 characters, and must start with a letter and contain alphanumeric characters or underscores only.

`map<string, .google.protobuf.Value> source_properties = 7;`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`value` | `[Value](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Finding.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1beta1.Finding.Builder)` |   
  
### putSourcePropertiesBuilderIfAbsent(String key)
    
    
    public Value.Builder putSourcePropertiesBuilderIfAbsent(String key)

Source specific properties. These properties are managed by the source that writes the finding. The key names in the source_properties map must be between 1 and 255 characters, and must start with a letter and contain alphanumeric characters or underscores only.

`map<string, .google.protobuf.Value> source_properties = 7;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.Builder.html)` |   
  
### removeSourceProperties(String key)
    
    
    public Finding.Builder removeSourceProperties(String key)

Source specific properties. These properties are managed by the source that writes the finding. The key names in the source_properties map must be between 1 and 255 characters, and must start with a letter and contain alphanumeric characters or underscores only.

`map<string, .google.protobuf.Value> source_properties = 7;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Finding.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1beta1.Finding.Builder)` |   
  
### setCategory(String value)
    
    
    public Finding.Builder setCategory(String value)

The additional taxonomy group within findings from a given source. This field is immutable after creation time. Example: "XSS_FLASH_INJECTION"

`string category = 5;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The category to set.  
**Returns**  
---  
**Type** | **Description**  
`[Finding.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1beta1.Finding.Builder)` | This builder for chaining.  
  
### setCategoryBytes(ByteString value)
    
    
    public Finding.Builder setCategoryBytes(ByteString value)

The additional taxonomy group within findings from a given source. This field is immutable after creation time. Example: "XSS_FLASH_INJECTION"

`string category = 5;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for category to set.  
**Returns**  
---  
**Type** | **Description**  
`[Finding.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1beta1.Finding.Builder)` | This builder for chaining.  
  
### setCreateTime(Timestamp value)
    
    
    public Finding.Builder setCreateTime(Timestamp value)

The time at which the finding was created in Security Command Center.

`.google.protobuf.Timestamp create_time = 10;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Finding.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1beta1.Finding.Builder)` |   
  
### setCreateTime(Timestamp.Builder builderForValue)
    
    
    public Finding.Builder setCreateTime(Timestamp.Builder builderForValue)

The time at which the finding was created in Security Command Center.

`.google.protobuf.Timestamp create_time = 10;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Finding.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1beta1.Finding.Builder)` |   
  
### setEventTime(Timestamp value)
    
    
    public Finding.Builder setEventTime(Timestamp value)

The time at which the event took place, or when an update to the finding occurred. For example, if the finding represents an open firewall it would capture the time the detector believes the firewall became open. The accuracy is determined by the detector. If the finding were to be resolved afterward, this time would reflect when the finding was resolved.

`.google.protobuf.Timestamp event_time = 9;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Finding.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1beta1.Finding.Builder)` |   
  
### setEventTime(Timestamp.Builder builderForValue)
    
    
    public Finding.Builder setEventTime(Timestamp.Builder builderForValue)

The time at which the event took place, or when an update to the finding occurred. For example, if the finding represents an open firewall it would capture the time the detector believes the firewall became open. The accuracy is determined by the detector. If the finding were to be resolved afterward, this time would reflect when the finding was resolved.

`.google.protobuf.Timestamp event_time = 9;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Finding.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1beta1.Finding.Builder)` |   
  
### setExternalUri(String value)
    
    
    public Finding.Builder setExternalUri(String value)

The URI that, if available, points to a web page outside of Security Command Center where additional information about the finding can be found. This field is guaranteed to be either empty or a well formed URL.

`string external_uri = 6;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The externalUri to set.  
**Returns**  
---  
**Type** | **Description**  
`[Finding.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1beta1.Finding.Builder)` | This builder for chaining.  
  
### setExternalUriBytes(ByteString value)
    
    
    public Finding.Builder setExternalUriBytes(ByteString value)

The URI that, if available, points to a web page outside of Security Command Center where additional information about the finding can be found. This field is guaranteed to be either empty or a well formed URL.

`string external_uri = 6;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for externalUri to set.  
**Returns**  
---  
**Type** | **Description**  
`[Finding.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1beta1.Finding.Builder)` | This builder for chaining.  
  
### setName(String value)
    
    
    public Finding.Builder setName(String value)

The relative resource name of this finding. See: <https://cloud.google.com/apis/design/resource_names#relative_resource_name> Example: "organizations/{organization_id}/sources/{source_id}/findings/{finding_id}"

`string name = 1;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name to set.  
**Returns**  
---  
**Type** | **Description**  
`[Finding.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1beta1.Finding.Builder)` | This builder for chaining.  
  
### setNameBytes(ByteString value)
    
    
    public Finding.Builder setNameBytes(ByteString value)

The relative resource name of this finding. See: <https://cloud.google.com/apis/design/resource_names#relative_resource_name> Example: "organizations/{organization_id}/sources/{source_id}/findings/{finding_id}"

`string name = 1;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for name to set.  
**Returns**  
---  
**Type** | **Description**  
`[Finding.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1beta1.Finding.Builder)` | This builder for chaining.  
  
### setParent(String value)
    
    
    public Finding.Builder setParent(String value)

Immutable. The relative resource name of the source the finding belongs to. See: <https://cloud.google.com/apis/design/resource_names#relative_resource_name> This field is immutable after creation time. For example: "organizations/{organization_id}/sources/{source_id}"

`string parent = 2 [(.google.api.field_behavior) = IMMUTABLE];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The parent to set.  
**Returns**  
---  
**Type** | **Description**  
`[Finding.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1beta1.Finding.Builder)` | This builder for chaining.  
  
### setParentBytes(ByteString value)
    
    
    public Finding.Builder setParentBytes(ByteString value)

Immutable. The relative resource name of the source the finding belongs to. See: <https://cloud.google.com/apis/design/resource_names#relative_resource_name> This field is immutable after creation time. For example: "organizations/{organization_id}/sources/{source_id}"

`string parent = 2 [(.google.api.field_behavior) = IMMUTABLE];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for parent to set.  
**Returns**  
---  
**Type** | **Description**  
`[Finding.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1beta1.Finding.Builder)` | This builder for chaining.  
  
### setResourceName(String value)
    
    
    public Finding.Builder setResourceName(String value)

For findings on Google Cloud resources, the full resource name of the Google Cloud resource this finding is for. See: <https://cloud.google.com/apis/design/resource_names#full_resource_name> When the finding is for a non-Google Cloud resource, the resourceName can be a customer or partner defined string. This field is immutable after creation time.

`string resource_name = 3;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The resourceName to set.  
**Returns**  
---  
**Type** | **Description**  
`[Finding.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1beta1.Finding.Builder)` | This builder for chaining.  
  
### setResourceNameBytes(ByteString value)
    
    
    public Finding.Builder setResourceNameBytes(ByteString value)

For findings on Google Cloud resources, the full resource name of the Google Cloud resource this finding is for. See: <https://cloud.google.com/apis/design/resource_names#full_resource_name> When the finding is for a non-Google Cloud resource, the resourceName can be a customer or partner defined string. This field is immutable after creation time.

`string resource_name = 3;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for resourceName to set.  
**Returns**  
---  
**Type** | **Description**  
`[Finding.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1beta1.Finding.Builder)` | This builder for chaining.  
  
### setSecurityMarks(SecurityMarks value)
    
    
    public Finding.Builder setSecurityMarks(SecurityMarks value)

Output only. User specified security marks. These marks are entirely managed by the user and come from the SecurityMarks resource that belongs to the finding.

` .google.cloud.securitycenter.v1beta1.SecurityMarks security_marks = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[SecurityMarks](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1beta1.SecurityMarks)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Finding.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1beta1.Finding.Builder)` |   
  
### setSecurityMarks(SecurityMarks.Builder builderForValue)
    
    
    public Finding.Builder setSecurityMarks(SecurityMarks.Builder builderForValue)

Output only. User specified security marks. These marks are entirely managed by the user and come from the SecurityMarks resource that belongs to the finding.

` .google.cloud.securitycenter.v1beta1.SecurityMarks security_marks = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[SecurityMarks.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1beta1.SecurityMarks.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Finding.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1beta1.Finding.Builder)` |   
  
### setState(Finding.State value)
    
    
    public Finding.Builder setState(Finding.State value)

The state of the finding.

`.google.cloud.securitycenter.v1beta1.Finding.State state = 4;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Finding.State](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1beta1.Finding.State)`  
The state to set.  
**Returns**  
---  
**Type** | **Description**  
`[Finding.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1beta1.Finding.Builder)` | This builder for chaining.  
  
### setStateValue(int value)
    
    
    public Finding.Builder setStateValue(int value)

The state of the finding.

`.google.cloud.securitycenter.v1beta1.Finding.State state = 4;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The enum numeric value on the wire for state to set.  
**Returns**  
---  
**Type** | **Description**  
`[Finding.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1beta1.Finding.Builder)` | This builder for chaining.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
