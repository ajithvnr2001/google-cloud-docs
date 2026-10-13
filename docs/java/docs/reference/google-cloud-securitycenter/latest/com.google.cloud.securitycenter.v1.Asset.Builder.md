---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Asset.Builder
title: Class Asset.Builder (2.107.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:32:34.983002+00:00
---

# Class Asset.Builder (2.107.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Asset.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class Asset.Builder (2.107.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.107.0 (latest)  2.103.0  2.102.0  2.101.0  2.99.0  2.96.0  2.95.0  2.93.0  2.91.0  2.90.0  2.88.0  2.86.0  2.84.0  2.83.0  2.82.0  2.81.0  2.80.0  2.78.0  2.76.0  2.75.0  2.72.0  2.71.0  2.70.0  2.68.0  2.67.0  2.66.0  2.65.0  2.64.0  2.63.0  2.62.0  2.61.0  2.60.0  2.59.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.1  2.10.0  2.9.0  2.8.0  2.7.1  2.6.0  2.5.6  2.3.2 
    
    
    public static final class Asset.Builder extends GeneratedMessage.Builder<Asset.Builder> implements AssetOrBuilder

Security Command Center representation of a Google Cloud resource.

The Asset is a Security Command Center resource that captures information about a single Google Cloud resource. All modifications to an Asset are only within the context of Security Command Center and don't affect the referenced Google Cloud resource.

Protobuf type `google.cloud.securitycenter.v1.Asset`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > Asset.Builder

## Implements

[AssetOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.AssetOrBuilder)

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
    
    
    public Asset build()

**Returns**  
---  
**Type** | **Description**  
`[Asset](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Asset)` |   
  
### buildPartial()
    
    
    public Asset buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[Asset](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Asset)` |   
  
### clear()
    
    
    public Asset.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[Asset.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Asset.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearCanonicalName()
    
    
    public Asset.Builder clearCanonicalName()

The canonical name of the resource. It's either "organizations/{organization_id}/assets/{asset_id}", "folders/{folder_id}/assets/{asset_id}" or "projects/{project_number}/assets/{asset_id}", depending on the closest CRM ancestor of the resource.

`string canonical_name = 13;`

**Returns**  
---  
**Type** | **Description**  
`[Asset.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Asset.Builder)` | This builder for chaining.  
  
### clearCreateTime()
    
    
    public Asset.Builder clearCreateTime()

The time at which the asset was created in Security Command Center.

`.google.protobuf.Timestamp create_time = 9;`

**Returns**  
---  
**Type** | **Description**  
`[Asset.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Asset.Builder)` |   
  
### clearIamPolicy()
    
    
    public Asset.Builder clearIamPolicy()

Cloud IAM Policy information associated with the Google Cloud resource described by the Security Command Center asset. This information is managed and defined by the Google Cloud resource and cannot be modified by the user.

`.google.cloud.securitycenter.v1.Asset.IamPolicy iam_policy = 11;`

**Returns**  
---  
**Type** | **Description**  
`[Asset.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Asset.Builder)` |   
  
### clearName()
    
    
    public Asset.Builder clearName()

The relative resource name of this asset. See: <https://cloud.google.com/apis/design/resource_names#relative_resource_name> Example: "organizations/{organization_id}/assets/{asset_id}".

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[Asset.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Asset.Builder)` | This builder for chaining.  
  
### clearResourceProperties()
    
    
    public Asset.Builder clearResourceProperties()

**Returns**  
---  
**Type** | **Description**  
`[Asset.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Asset.Builder)` |   
  
### clearSecurityCenterProperties()
    
    
    public Asset.Builder clearSecurityCenterProperties()

Security Command Center managed properties. These properties are managed by Security Command Center and cannot be modified by the user.

` .google.cloud.securitycenter.v1.Asset.SecurityCenterProperties security_center_properties = 2; `

**Returns**  
---  
**Type** | **Description**  
`[Asset.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Asset.Builder)` |   
  
### clearSecurityMarks()
    
    
    public Asset.Builder clearSecurityMarks()

User specified security marks. These marks are entirely managed by the user and come from the SecurityMarks resource that belongs to the asset.

`.google.cloud.securitycenter.v1.SecurityMarks security_marks = 8;`

**Returns**  
---  
**Type** | **Description**  
`[Asset.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Asset.Builder)` |   
  
### clearUpdateTime()
    
    
    public Asset.Builder clearUpdateTime()

The time at which the asset was last updated or added in Cloud SCC.

`.google.protobuf.Timestamp update_time = 10;`

**Returns**  
---  
**Type** | **Description**  
`[Asset.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Asset.Builder)` |   
  
### containsResourceProperties(String key)
    
    
    public boolean containsResourceProperties(String key)

Resource managed properties. These properties are managed and defined by the Google Cloud resource and cannot be modified by the user.

`map<string, .google.protobuf.Value> resource_properties = 7;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getCanonicalName()
    
    
    public String getCanonicalName()

The canonical name of the resource. It's either "organizations/{organization_id}/assets/{asset_id}", "folders/{folder_id}/assets/{asset_id}" or "projects/{project_number}/assets/{asset_id}", depending on the closest CRM ancestor of the resource.

`string canonical_name = 13;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The canonicalName.  
  
### getCanonicalNameBytes()
    
    
    public ByteString getCanonicalNameBytes()

The canonical name of the resource. It's either "organizations/{organization_id}/assets/{asset_id}", "folders/{folder_id}/assets/{asset_id}" or "projects/{project_number}/assets/{asset_id}", depending on the closest CRM ancestor of the resource.

`string canonical_name = 13;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for canonicalName.  
  
### getCreateTime()
    
    
    public Timestamp getCreateTime()

The time at which the asset was created in Security Command Center.

`.google.protobuf.Timestamp create_time = 9;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeBuilder()
    
    
    public Timestamp.Builder getCreateTimeBuilder()

The time at which the asset was created in Security Command Center.

`.google.protobuf.Timestamp create_time = 9;`

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)` |   
  
### getCreateTimeOrBuilder()
    
    
    public TimestampOrBuilder getCreateTimeOrBuilder()

The time at which the asset was created in Security Command Center.

`.google.protobuf.Timestamp create_time = 9;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDefaultInstanceForType()
    
    
    public Asset getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[Asset](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Asset)` |   
  
### getDescriptorForType()
    
    
    public Descriptors.Descriptor getDescriptorForType()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getDescriptorForType__)

### getIamPolicy()
    
    
    public Asset.IamPolicy getIamPolicy()

Cloud IAM Policy information associated with the Google Cloud resource described by the Security Command Center asset. This information is managed and defined by the Google Cloud resource and cannot be modified by the user.

`.google.cloud.securitycenter.v1.Asset.IamPolicy iam_policy = 11;`

**Returns**  
---  
**Type** | **Description**  
`[Asset.IamPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Asset.IamPolicy)` | The iamPolicy.  
  
### getIamPolicyBuilder()
    
    
    public Asset.IamPolicy.Builder getIamPolicyBuilder()

Cloud IAM Policy information associated with the Google Cloud resource described by the Security Command Center asset. This information is managed and defined by the Google Cloud resource and cannot be modified by the user.

`.google.cloud.securitycenter.v1.Asset.IamPolicy iam_policy = 11;`

**Returns**  
---  
**Type** | **Description**  
`[Asset.IamPolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Asset.IamPolicy.Builder)` |   
  
### getIamPolicyOrBuilder()
    
    
    public Asset.IamPolicyOrBuilder getIamPolicyOrBuilder()

Cloud IAM Policy information associated with the Google Cloud resource described by the Security Command Center asset. This information is managed and defined by the Google Cloud resource and cannot be modified by the user.

`.google.cloud.securitycenter.v1.Asset.IamPolicy iam_policy = 11;`

**Returns**  
---  
**Type** | **Description**  
`[Asset.IamPolicyOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Asset.IamPolicyOrBuilder)` |   
  
### getMutableResourceProperties() (deprecated)
    
    
    public Map<String,Value> getMutableResourceProperties()

Use alternate mutation accessors instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[Value](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html)>` |   
  
### getName()
    
    
    public String getName()

The relative resource name of this asset. See: <https://cloud.google.com/apis/design/resource_names#relative_resource_name> Example: "organizations/{organization_id}/assets/{asset_id}".

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public ByteString getNameBytes()

The relative resource name of this asset. See: <https://cloud.google.com/apis/design/resource_names#relative_resource_name> Example: "organizations/{organization_id}/assets/{asset_id}".

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getResourceProperties() (deprecated)
    
    
    public Map<String,Value> getResourceProperties()

Use [#getResourcePropertiesMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Asset.Builder#com_google_cloud_securitycenter_v1_Asset_Builder_getResourcePropertiesMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[Value](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html)>` |   
  
### getResourcePropertiesCount()
    
    
    public int getResourcePropertiesCount()

Resource managed properties. These properties are managed and defined by the Google Cloud resource and cannot be modified by the user.

`map<string, .google.protobuf.Value> resource_properties = 7;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getResourcePropertiesMap()
    
    
    public Map<String,Value> getResourcePropertiesMap()

Resource managed properties. These properties are managed and defined by the Google Cloud resource and cannot be modified by the user.

`map<string, .google.protobuf.Value> resource_properties = 7;`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[Value](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html)>` |   
  
### getResourcePropertiesOrDefault(String key, Value defaultValue)
    
    
    public Value getResourcePropertiesOrDefault(String key, Value defaultValue)

Resource managed properties. These properties are managed and defined by the Google Cloud resource and cannot be modified by the user.

`map<string, .google.protobuf.Value> resource_properties = 7;`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[Value](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Value](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html)` |   
  
### getResourcePropertiesOrThrow(String key)
    
    
    public Value getResourcePropertiesOrThrow(String key)

Resource managed properties. These properties are managed and defined by the Google Cloud resource and cannot be modified by the user.

`map<string, .google.protobuf.Value> resource_properties = 7;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Value](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html)` |   
  
### getSecurityCenterProperties()
    
    
    public Asset.SecurityCenterProperties getSecurityCenterProperties()

Security Command Center managed properties. These properties are managed by Security Command Center and cannot be modified by the user.

` .google.cloud.securitycenter.v1.Asset.SecurityCenterProperties security_center_properties = 2; `

**Returns**  
---  
**Type** | **Description**  
`[Asset.SecurityCenterProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Asset.SecurityCenterProperties)` | The securityCenterProperties.  
  
### getSecurityCenterPropertiesBuilder()
    
    
    public Asset.SecurityCenterProperties.Builder getSecurityCenterPropertiesBuilder()

Security Command Center managed properties. These properties are managed by Security Command Center and cannot be modified by the user.

` .google.cloud.securitycenter.v1.Asset.SecurityCenterProperties security_center_properties = 2; `

**Returns**  
---  
**Type** | **Description**  
`[Asset.SecurityCenterProperties.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Asset.SecurityCenterProperties.Builder)` |   
  
### getSecurityCenterPropertiesOrBuilder()
    
    
    public Asset.SecurityCenterPropertiesOrBuilder getSecurityCenterPropertiesOrBuilder()

Security Command Center managed properties. These properties are managed by Security Command Center and cannot be modified by the user.

` .google.cloud.securitycenter.v1.Asset.SecurityCenterProperties security_center_properties = 2; `

**Returns**  
---  
**Type** | **Description**  
`[Asset.SecurityCenterPropertiesOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Asset.SecurityCenterPropertiesOrBuilder)` |   
  
### getSecurityMarks()
    
    
    public SecurityMarks getSecurityMarks()

User specified security marks. These marks are entirely managed by the user and come from the SecurityMarks resource that belongs to the asset.

`.google.cloud.securitycenter.v1.SecurityMarks security_marks = 8;`

**Returns**  
---  
**Type** | **Description**  
`[SecurityMarks](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.SecurityMarks)` | The securityMarks.  
  
### getSecurityMarksBuilder()
    
    
    public SecurityMarks.Builder getSecurityMarksBuilder()

User specified security marks. These marks are entirely managed by the user and come from the SecurityMarks resource that belongs to the asset.

`.google.cloud.securitycenter.v1.SecurityMarks security_marks = 8;`

**Returns**  
---  
**Type** | **Description**  
`[SecurityMarks.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.SecurityMarks.Builder)` |   
  
### getSecurityMarksOrBuilder()
    
    
    public SecurityMarksOrBuilder getSecurityMarksOrBuilder()

User specified security marks. These marks are entirely managed by the user and come from the SecurityMarks resource that belongs to the asset.

`.google.cloud.securitycenter.v1.SecurityMarks security_marks = 8;`

**Returns**  
---  
**Type** | **Description**  
`[SecurityMarksOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.SecurityMarksOrBuilder)` |   
  
### getUpdateTime()
    
    
    public Timestamp getUpdateTime()

The time at which the asset was last updated or added in Cloud SCC.

`.google.protobuf.Timestamp update_time = 10;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The updateTime.  
  
### getUpdateTimeBuilder()
    
    
    public Timestamp.Builder getUpdateTimeBuilder()

The time at which the asset was last updated or added in Cloud SCC.

`.google.protobuf.Timestamp update_time = 10;`

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)` |   
  
### getUpdateTimeOrBuilder()
    
    
    public TimestampOrBuilder getUpdateTimeOrBuilder()

The time at which the asset was last updated or added in Cloud SCC.

`.google.protobuf.Timestamp update_time = 10;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### hasCreateTime()
    
    
    public boolean hasCreateTime()

The time at which the asset was created in Security Command Center.

`.google.protobuf.Timestamp create_time = 9;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasIamPolicy()
    
    
    public boolean hasIamPolicy()

Cloud IAM Policy information associated with the Google Cloud resource described by the Security Command Center asset. This information is managed and defined by the Google Cloud resource and cannot be modified by the user.

`.google.cloud.securitycenter.v1.Asset.IamPolicy iam_policy = 11;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the iamPolicy field is set.  
  
### hasSecurityCenterProperties()
    
    
    public boolean hasSecurityCenterProperties()

Security Command Center managed properties. These properties are managed by Security Command Center and cannot be modified by the user.

` .google.cloud.securitycenter.v1.Asset.SecurityCenterProperties security_center_properties = 2; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the securityCenterProperties field is set.  
  
### hasSecurityMarks()
    
    
    public boolean hasSecurityMarks()

User specified security marks. These marks are entirely managed by the user and come from the SecurityMarks resource that belongs to the asset.

`.google.cloud.securitycenter.v1.SecurityMarks security_marks = 8;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the securityMarks field is set.  
  
### hasUpdateTime()
    
    
    public boolean hasUpdateTime()

The time at which the asset was last updated or added in Cloud SCC.

`.google.protobuf.Timestamp update_time = 10;`

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
    
    
    public Asset.Builder mergeCreateTime(Timestamp value)

The time at which the asset was created in Security Command Center.

`.google.protobuf.Timestamp create_time = 9;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Asset.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Asset.Builder)` |   
  
### mergeFrom(Asset other)
    
    
    public Asset.Builder mergeFrom(Asset other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Asset](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Asset)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Asset.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Asset.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public Asset.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Asset.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Asset.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public Asset.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Asset.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Asset.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### mergeIamPolicy(Asset.IamPolicy value)
    
    
    public Asset.Builder mergeIamPolicy(Asset.IamPolicy value)

Cloud IAM Policy information associated with the Google Cloud resource described by the Security Command Center asset. This information is managed and defined by the Google Cloud resource and cannot be modified by the user.

`.google.cloud.securitycenter.v1.Asset.IamPolicy iam_policy = 11;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Asset.IamPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Asset.IamPolicy)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Asset.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Asset.Builder)` |   
  
### mergeSecurityCenterProperties(Asset.SecurityCenterProperties value)
    
    
    public Asset.Builder mergeSecurityCenterProperties(Asset.SecurityCenterProperties value)

Security Command Center managed properties. These properties are managed by Security Command Center and cannot be modified by the user.

` .google.cloud.securitycenter.v1.Asset.SecurityCenterProperties security_center_properties = 2; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Asset.SecurityCenterProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Asset.SecurityCenterProperties)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Asset.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Asset.Builder)` |   
  
### mergeSecurityMarks(SecurityMarks value)
    
    
    public Asset.Builder mergeSecurityMarks(SecurityMarks value)

User specified security marks. These marks are entirely managed by the user and come from the SecurityMarks resource that belongs to the asset.

`.google.cloud.securitycenter.v1.SecurityMarks security_marks = 8;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[SecurityMarks](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.SecurityMarks)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Asset.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Asset.Builder)` |   
  
### mergeUpdateTime(Timestamp value)
    
    
    public Asset.Builder mergeUpdateTime(Timestamp value)

The time at which the asset was last updated or added in Cloud SCC.

`.google.protobuf.Timestamp update_time = 10;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Asset.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Asset.Builder)` |   
  
### putAllResourceProperties(Map<String,Value> values)
    
    
    public Asset.Builder putAllResourceProperties(Map<String,Value> values)

Resource managed properties. These properties are managed and defined by the Google Cloud resource and cannot be modified by the user.

`map<string, .google.protobuf.Value> resource_properties = 7;`

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[Value](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[Asset.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Asset.Builder)` |   
  
### putResourceProperties(String key, Value value)
    
    
    public Asset.Builder putResourceProperties(String key, Value value)

Resource managed properties. These properties are managed and defined by the Google Cloud resource and cannot be modified by the user.

`map<string, .google.protobuf.Value> resource_properties = 7;`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`value` | `[Value](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Asset.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Asset.Builder)` |   
  
### putResourcePropertiesBuilderIfAbsent(String key)
    
    
    public Value.Builder putResourcePropertiesBuilderIfAbsent(String key)

Resource managed properties. These properties are managed and defined by the Google Cloud resource and cannot be modified by the user.

`map<string, .google.protobuf.Value> resource_properties = 7;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.Builder.html)` |   
  
### removeResourceProperties(String key)
    
    
    public Asset.Builder removeResourceProperties(String key)

Resource managed properties. These properties are managed and defined by the Google Cloud resource and cannot be modified by the user.

`map<string, .google.protobuf.Value> resource_properties = 7;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Asset.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Asset.Builder)` |   
  
### setCanonicalName(String value)
    
    
    public Asset.Builder setCanonicalName(String value)

The canonical name of the resource. It's either "organizations/{organization_id}/assets/{asset_id}", "folders/{folder_id}/assets/{asset_id}" or "projects/{project_number}/assets/{asset_id}", depending on the closest CRM ancestor of the resource.

`string canonical_name = 13;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The canonicalName to set.  
**Returns**  
---  
**Type** | **Description**  
`[Asset.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Asset.Builder)` | This builder for chaining.  
  
### setCanonicalNameBytes(ByteString value)
    
    
    public Asset.Builder setCanonicalNameBytes(ByteString value)

The canonical name of the resource. It's either "organizations/{organization_id}/assets/{asset_id}", "folders/{folder_id}/assets/{asset_id}" or "projects/{project_number}/assets/{asset_id}", depending on the closest CRM ancestor of the resource.

`string canonical_name = 13;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for canonicalName to set.  
**Returns**  
---  
**Type** | **Description**  
`[Asset.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Asset.Builder)` | This builder for chaining.  
  
### setCreateTime(Timestamp value)
    
    
    public Asset.Builder setCreateTime(Timestamp value)

The time at which the asset was created in Security Command Center.

`.google.protobuf.Timestamp create_time = 9;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Asset.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Asset.Builder)` |   
  
### setCreateTime(Timestamp.Builder builderForValue)
    
    
    public Asset.Builder setCreateTime(Timestamp.Builder builderForValue)

The time at which the asset was created in Security Command Center.

`.google.protobuf.Timestamp create_time = 9;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Asset.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Asset.Builder)` |   
  
### setIamPolicy(Asset.IamPolicy value)
    
    
    public Asset.Builder setIamPolicy(Asset.IamPolicy value)

Cloud IAM Policy information associated with the Google Cloud resource described by the Security Command Center asset. This information is managed and defined by the Google Cloud resource and cannot be modified by the user.

`.google.cloud.securitycenter.v1.Asset.IamPolicy iam_policy = 11;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Asset.IamPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Asset.IamPolicy)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Asset.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Asset.Builder)` |   
  
### setIamPolicy(Asset.IamPolicy.Builder builderForValue)
    
    
    public Asset.Builder setIamPolicy(Asset.IamPolicy.Builder builderForValue)

Cloud IAM Policy information associated with the Google Cloud resource described by the Security Command Center asset. This information is managed and defined by the Google Cloud resource and cannot be modified by the user.

`.google.cloud.securitycenter.v1.Asset.IamPolicy iam_policy = 11;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Asset.IamPolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Asset.IamPolicy.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Asset.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Asset.Builder)` |   
  
### setName(String value)
    
    
    public Asset.Builder setName(String value)

The relative resource name of this asset. See: <https://cloud.google.com/apis/design/resource_names#relative_resource_name> Example: "organizations/{organization_id}/assets/{asset_id}".

`string name = 1;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name to set.  
**Returns**  
---  
**Type** | **Description**  
`[Asset.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Asset.Builder)` | This builder for chaining.  
  
### setNameBytes(ByteString value)
    
    
    public Asset.Builder setNameBytes(ByteString value)

The relative resource name of this asset. See: <https://cloud.google.com/apis/design/resource_names#relative_resource_name> Example: "organizations/{organization_id}/assets/{asset_id}".

`string name = 1;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for name to set.  
**Returns**  
---  
**Type** | **Description**  
`[Asset.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Asset.Builder)` | This builder for chaining.  
  
### setSecurityCenterProperties(Asset.SecurityCenterProperties value)
    
    
    public Asset.Builder setSecurityCenterProperties(Asset.SecurityCenterProperties value)

Security Command Center managed properties. These properties are managed by Security Command Center and cannot be modified by the user.

` .google.cloud.securitycenter.v1.Asset.SecurityCenterProperties security_center_properties = 2; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Asset.SecurityCenterProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Asset.SecurityCenterProperties)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Asset.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Asset.Builder)` |   
  
### setSecurityCenterProperties(Asset.SecurityCenterProperties.Builder builderForValue)
    
    
    public Asset.Builder setSecurityCenterProperties(Asset.SecurityCenterProperties.Builder builderForValue)

Security Command Center managed properties. These properties are managed by Security Command Center and cannot be modified by the user.

` .google.cloud.securitycenter.v1.Asset.SecurityCenterProperties security_center_properties = 2; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Asset.SecurityCenterProperties.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Asset.SecurityCenterProperties.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Asset.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Asset.Builder)` |   
  
### setSecurityMarks(SecurityMarks value)
    
    
    public Asset.Builder setSecurityMarks(SecurityMarks value)

User specified security marks. These marks are entirely managed by the user and come from the SecurityMarks resource that belongs to the asset.

`.google.cloud.securitycenter.v1.SecurityMarks security_marks = 8;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[SecurityMarks](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.SecurityMarks)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Asset.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Asset.Builder)` |   
  
### setSecurityMarks(SecurityMarks.Builder builderForValue)
    
    
    public Asset.Builder setSecurityMarks(SecurityMarks.Builder builderForValue)

User specified security marks. These marks are entirely managed by the user and come from the SecurityMarks resource that belongs to the asset.

`.google.cloud.securitycenter.v1.SecurityMarks security_marks = 8;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[SecurityMarks.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.SecurityMarks.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Asset.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Asset.Builder)` |   
  
### setUpdateTime(Timestamp value)
    
    
    public Asset.Builder setUpdateTime(Timestamp value)

The time at which the asset was last updated or added in Cloud SCC.

`.google.protobuf.Timestamp update_time = 10;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Asset.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Asset.Builder)` |   
  
### setUpdateTime(Timestamp.Builder builderForValue)
    
    
    public Asset.Builder setUpdateTime(Timestamp.Builder builderForValue)

The time at which the asset was last updated or added in Cloud SCC.

`.google.protobuf.Timestamp update_time = 10;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Asset.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Asset.Builder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
