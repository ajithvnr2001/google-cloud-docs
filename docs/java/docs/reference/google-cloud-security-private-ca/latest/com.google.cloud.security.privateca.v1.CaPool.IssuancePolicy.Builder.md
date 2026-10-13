---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.Builder
title: Class CaPool.IssuancePolicy.Builder (2.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:23:02.299047+00:00
---

# Class CaPool.IssuancePolicy.Builder (2.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class CaPool.IssuancePolicy.Builder (2.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.101.0 (latest)  2.97.0  2.96.0  2.95.0  2.93.0  2.90.0  2.89.0  2.87.0  2.85.0  2.84.0  2.82.0  2.80.0  2.78.0  2.77.0  2.76.0  2.75.0  2.74.0  2.72.0  2.70.0  2.69.0  2.66.0  2.65.0  2.64.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.4  2.4.0  2.3.0  2.2.5 
    
    
    public static final class CaPool.IssuancePolicy.Builder extends GeneratedMessage.Builder<CaPool.IssuancePolicy.Builder> implements CaPool.IssuancePolicyOrBuilder

Defines controls over all certificate issuance within a CaPool.

Protobuf type `google.cloud.security.privateca.v1.CaPool.IssuancePolicy`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > CaPool.IssuancePolicy.Builder

## Implements

[CaPool.IssuancePolicyOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicyOrBuilder)

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

### addAllAllowedKeyTypes(Iterable<? extends CaPool.IssuancePolicy.AllowedKeyType> values)
    
    
    public CaPool.IssuancePolicy.Builder addAllAllowedKeyTypes(Iterable<? extends CaPool.IssuancePolicy.AllowedKeyType> values)

Optional. If any AllowedKeyType is specified, then the certificate request's public key must match one of the key types listed here. Otherwise, any key may be used.

` repeated .google.cloud.security.privateca.v1.CaPool.IssuancePolicy.AllowedKeyType allowed_key_types = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<? extends com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.AllowedKeyType>`  
  
**Returns**  
---  
**Type** | **Description**  
`[CaPool.IssuancePolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.Builder)` |   
  
### addAllowedKeyTypes(CaPool.IssuancePolicy.AllowedKeyType value)
    
    
    public CaPool.IssuancePolicy.Builder addAllowedKeyTypes(CaPool.IssuancePolicy.AllowedKeyType value)

Optional. If any AllowedKeyType is specified, then the certificate request's public key must match one of the key types listed here. Otherwise, any key may be used.

` repeated .google.cloud.security.privateca.v1.CaPool.IssuancePolicy.AllowedKeyType allowed_key_types = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[CaPool.IssuancePolicy.AllowedKeyType](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.AllowedKeyType)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CaPool.IssuancePolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.Builder)` |   
  
### addAllowedKeyTypes(CaPool.IssuancePolicy.AllowedKeyType.Builder builderForValue)
    
    
    public CaPool.IssuancePolicy.Builder addAllowedKeyTypes(CaPool.IssuancePolicy.AllowedKeyType.Builder builderForValue)

Optional. If any AllowedKeyType is specified, then the certificate request's public key must match one of the key types listed here. Otherwise, any key may be used.

` repeated .google.cloud.security.privateca.v1.CaPool.IssuancePolicy.AllowedKeyType allowed_key_types = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[CaPool.IssuancePolicy.AllowedKeyType.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.AllowedKeyType.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CaPool.IssuancePolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.Builder)` |   
  
### addAllowedKeyTypes(int index, CaPool.IssuancePolicy.AllowedKeyType value)
    
    
    public CaPool.IssuancePolicy.Builder addAllowedKeyTypes(int index, CaPool.IssuancePolicy.AllowedKeyType value)

Optional. If any AllowedKeyType is specified, then the certificate request's public key must match one of the key types listed here. Otherwise, any key may be used.

` repeated .google.cloud.security.privateca.v1.CaPool.IssuancePolicy.AllowedKeyType allowed_key_types = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[CaPool.IssuancePolicy.AllowedKeyType](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.AllowedKeyType)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CaPool.IssuancePolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.Builder)` |   
  
### addAllowedKeyTypes(int index, CaPool.IssuancePolicy.AllowedKeyType.Builder builderForValue)
    
    
    public CaPool.IssuancePolicy.Builder addAllowedKeyTypes(int index, CaPool.IssuancePolicy.AllowedKeyType.Builder builderForValue)

Optional. If any AllowedKeyType is specified, then the certificate request's public key must match one of the key types listed here. Otherwise, any key may be used.

` repeated .google.cloud.security.privateca.v1.CaPool.IssuancePolicy.AllowedKeyType allowed_key_types = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[CaPool.IssuancePolicy.AllowedKeyType.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.AllowedKeyType.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CaPool.IssuancePolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.Builder)` |   
  
### addAllowedKeyTypesBuilder()
    
    
    public CaPool.IssuancePolicy.AllowedKeyType.Builder addAllowedKeyTypesBuilder()

Optional. If any AllowedKeyType is specified, then the certificate request's public key must match one of the key types listed here. Otherwise, any key may be used.

` repeated .google.cloud.security.privateca.v1.CaPool.IssuancePolicy.AllowedKeyType allowed_key_types = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[CaPool.IssuancePolicy.AllowedKeyType.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.AllowedKeyType.Builder)` |   
  
### addAllowedKeyTypesBuilder(int index)
    
    
    public CaPool.IssuancePolicy.AllowedKeyType.Builder addAllowedKeyTypesBuilder(int index)

Optional. If any AllowedKeyType is specified, then the certificate request's public key must match one of the key types listed here. Otherwise, any key may be used.

` repeated .google.cloud.security.privateca.v1.CaPool.IssuancePolicy.AllowedKeyType allowed_key_types = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CaPool.IssuancePolicy.AllowedKeyType.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.AllowedKeyType.Builder)` |   
  
### build()
    
    
    public CaPool.IssuancePolicy build()

**Returns**  
---  
**Type** | **Description**  
`[CaPool.IssuancePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy)` |   
  
### buildPartial()
    
    
    public CaPool.IssuancePolicy buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[CaPool.IssuancePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy)` |   
  
### clear()
    
    
    public CaPool.IssuancePolicy.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[CaPool.IssuancePolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearAllowRequesterSpecifiedNotBeforeTime()
    
    
    public CaPool.IssuancePolicy.Builder clearAllowRequesterSpecifiedNotBeforeTime()

Optional. If set to true, allows requesters to specify the requested_not_before_time field when creating a Certificate. Certificates requested with this option enabled will have a 'not_before_time' equal to the value specified in the request. The 'not_after_time' will be adjusted to preserve the requested lifetime. The maximum time that a certificate can be backdated with these options is 48 hours in the past. This option cannot be set if backdate_duration is set.

` bool allow_requester_specified_not_before_time = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[CaPool.IssuancePolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.Builder)` | This builder for chaining.  
  
### clearAllowedIssuanceModes()
    
    
    public CaPool.IssuancePolicy.Builder clearAllowedIssuanceModes()

Optional. If specified, then only methods allowed in the IssuanceModes may be used to issue Certificates.

` .google.cloud.security.privateca.v1.CaPool.IssuancePolicy.IssuanceModes allowed_issuance_modes = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[CaPool.IssuancePolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.Builder)` |   
  
### clearAllowedKeyTypes()
    
    
    public CaPool.IssuancePolicy.Builder clearAllowedKeyTypes()

Optional. If any AllowedKeyType is specified, then the certificate request's public key must match one of the key types listed here. Otherwise, any key may be used.

` repeated .google.cloud.security.privateca.v1.CaPool.IssuancePolicy.AllowedKeyType allowed_key_types = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[CaPool.IssuancePolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.Builder)` |   
  
### clearBackdateDuration()
    
    
    public CaPool.IssuancePolicy.Builder clearBackdateDuration()

Optional. If set, all certificates issued from this CaPool will be backdated by this duration. The 'not_before_time' will be the issuance time minus this backdate_duration, and the 'not_after_time' will be adjusted to preserve the requested lifetime. The maximum duration that a certificate can be backdated with these options is 48 hours in the past. This option cannot be set if allow_requester_specified_not_before_time is set.

` .google.protobuf.Duration backdate_duration = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[CaPool.IssuancePolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.Builder)` |   
  
### clearBaselineValues()
    
    
    public CaPool.IssuancePolicy.Builder clearBaselineValues()

Optional. A set of X.509 values that will be applied to all certificates issued through this CaPool. If a certificate request includes conflicting values for the same properties, they will be overwritten by the values defined here. If a certificate request uses a CertificateTemplate that defines conflicting predefined_values for the same properties, the certificate issuance request will fail.

` .google.cloud.security.privateca.v1.X509Parameters baseline_values = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[CaPool.IssuancePolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.Builder)` |   
  
### clearIdentityConstraints()
    
    
    public CaPool.IssuancePolicy.Builder clearIdentityConstraints()

Optional. Describes constraints on identities that may appear in Certificates issued through this CaPool. If this is omitted, then this CaPool will not add restrictions on a certificate's identity.

` .google.cloud.security.privateca.v1.CertificateIdentityConstraints identity_constraints = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[CaPool.IssuancePolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.Builder)` |   
  
### clearMaximumLifetime()
    
    
    public CaPool.IssuancePolicy.Builder clearMaximumLifetime()

Optional. The maximum lifetime allowed for issued Certificates. Note that if the issuing CertificateAuthority expires before a Certificate resource's requested maximum_lifetime, the effective lifetime will be explicitly truncated to match it.

` .google.protobuf.Duration maximum_lifetime = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[CaPool.IssuancePolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.Builder)` |   
  
### clearPassthroughExtensions()
    
    
    public CaPool.IssuancePolicy.Builder clearPassthroughExtensions()

Optional. Describes the set of X.509 extensions that may appear in a Certificate issued through this CaPool. If a certificate request sets extensions that don't appear in the passthrough_extensions, those extensions will be dropped. If a certificate request uses a CertificateTemplate with predefined_values that don't appear here, the certificate issuance request will fail. If this is omitted, then this CaPool will not add restrictions on a certificate's X.509 extensions. These constraints do not apply to X.509 extensions set in this CaPool's baseline_values.

` .google.cloud.security.privateca.v1.CertificateExtensionConstraints passthrough_extensions = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[CaPool.IssuancePolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.Builder)` |   
  
### getAllowRequesterSpecifiedNotBeforeTime()
    
    
    public boolean getAllowRequesterSpecifiedNotBeforeTime()

Optional. If set to true, allows requesters to specify the requested_not_before_time field when creating a Certificate. Certificates requested with this option enabled will have a 'not_before_time' equal to the value specified in the request. The 'not_after_time' will be adjusted to preserve the requested lifetime. The maximum time that a certificate can be backdated with these options is 48 hours in the past. This option cannot be set if backdate_duration is set.

` bool allow_requester_specified_not_before_time = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The allowRequesterSpecifiedNotBeforeTime.  
  
### getAllowedIssuanceModes()
    
    
    public CaPool.IssuancePolicy.IssuanceModes getAllowedIssuanceModes()

Optional. If specified, then only methods allowed in the IssuanceModes may be used to issue Certificates.

` .google.cloud.security.privateca.v1.CaPool.IssuancePolicy.IssuanceModes allowed_issuance_modes = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[CaPool.IssuancePolicy.IssuanceModes](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.IssuanceModes)` | The allowedIssuanceModes.  
  
### getAllowedIssuanceModesBuilder()
    
    
    public CaPool.IssuancePolicy.IssuanceModes.Builder getAllowedIssuanceModesBuilder()

Optional. If specified, then only methods allowed in the IssuanceModes may be used to issue Certificates.

` .google.cloud.security.privateca.v1.CaPool.IssuancePolicy.IssuanceModes allowed_issuance_modes = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[CaPool.IssuancePolicy.IssuanceModes.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.IssuanceModes.Builder)` |   
  
### getAllowedIssuanceModesOrBuilder()
    
    
    public CaPool.IssuancePolicy.IssuanceModesOrBuilder getAllowedIssuanceModesOrBuilder()

Optional. If specified, then only methods allowed in the IssuanceModes may be used to issue Certificates.

` .google.cloud.security.privateca.v1.CaPool.IssuancePolicy.IssuanceModes allowed_issuance_modes = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[CaPool.IssuancePolicy.IssuanceModesOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.IssuanceModesOrBuilder)` |   
  
### getAllowedKeyTypes(int index)
    
    
    public CaPool.IssuancePolicy.AllowedKeyType getAllowedKeyTypes(int index)

Optional. If any AllowedKeyType is specified, then the certificate request's public key must match one of the key types listed here. Otherwise, any key may be used.

` repeated .google.cloud.security.privateca.v1.CaPool.IssuancePolicy.AllowedKeyType allowed_key_types = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CaPool.IssuancePolicy.AllowedKeyType](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.AllowedKeyType)` |   
  
### getAllowedKeyTypesBuilder(int index)
    
    
    public CaPool.IssuancePolicy.AllowedKeyType.Builder getAllowedKeyTypesBuilder(int index)

Optional. If any AllowedKeyType is specified, then the certificate request's public key must match one of the key types listed here. Otherwise, any key may be used.

` repeated .google.cloud.security.privateca.v1.CaPool.IssuancePolicy.AllowedKeyType allowed_key_types = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CaPool.IssuancePolicy.AllowedKeyType.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.AllowedKeyType.Builder)` |   
  
### getAllowedKeyTypesBuilderList()
    
    
    public List<CaPool.IssuancePolicy.AllowedKeyType.Builder> getAllowedKeyTypesBuilderList()

Optional. If any AllowedKeyType is specified, then the certificate request's public key must match one of the key types listed here. Otherwise, any key may be used.

` repeated .google.cloud.security.privateca.v1.CaPool.IssuancePolicy.AllowedKeyType allowed_key_types = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.AllowedKeyType.Builder)>` |   
  
### getAllowedKeyTypesCount()
    
    
    public int getAllowedKeyTypesCount()

Optional. If any AllowedKeyType is specified, then the certificate request's public key must match one of the key types listed here. Otherwise, any key may be used.

` repeated .google.cloud.security.privateca.v1.CaPool.IssuancePolicy.AllowedKeyType allowed_key_types = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAllowedKeyTypesList()
    
    
    public List<CaPool.IssuancePolicy.AllowedKeyType> getAllowedKeyTypesList()

Optional. If any AllowedKeyType is specified, then the certificate request's public key must match one of the key types listed here. Otherwise, any key may be used.

` repeated .google.cloud.security.privateca.v1.CaPool.IssuancePolicy.AllowedKeyType allowed_key_types = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[AllowedKeyType](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.AllowedKeyType)>` |   
  
### getAllowedKeyTypesOrBuilder(int index)
    
    
    public CaPool.IssuancePolicy.AllowedKeyTypeOrBuilder getAllowedKeyTypesOrBuilder(int index)

Optional. If any AllowedKeyType is specified, then the certificate request's public key must match one of the key types listed here. Otherwise, any key may be used.

` repeated .google.cloud.security.privateca.v1.CaPool.IssuancePolicy.AllowedKeyType allowed_key_types = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CaPool.IssuancePolicy.AllowedKeyTypeOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.AllowedKeyTypeOrBuilder)` |   
  
### getAllowedKeyTypesOrBuilderList()
    
    
    public List<? extends CaPool.IssuancePolicy.AllowedKeyTypeOrBuilder> getAllowedKeyTypesOrBuilderList()

Optional. If any AllowedKeyType is specified, then the certificate request's public key must match one of the key types listed here. Otherwise, any key may be used.

` repeated .google.cloud.security.privateca.v1.CaPool.IssuancePolicy.AllowedKeyType allowed_key_types = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.AllowedKeyTypeOrBuilder>` |   
  
### getBackdateDuration()
    
    
    public Duration getBackdateDuration()

Optional. If set, all certificates issued from this CaPool will be backdated by this duration. The 'not_before_time' will be the issuance time minus this backdate_duration, and the 'not_after_time' will be adjusted to preserve the requested lifetime. The maximum duration that a certificate can be backdated with these options is 48 hours in the past. This option cannot be set if allow_requester_specified_not_before_time is set.

` .google.protobuf.Duration backdate_duration = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)` | The backdateDuration.  
  
### getBackdateDurationBuilder()
    
    
    public Duration.Builder getBackdateDurationBuilder()

Optional. If set, all certificates issued from this CaPool will be backdated by this duration. The 'not_before_time' will be the issuance time minus this backdate_duration, and the 'not_after_time' will be adjusted to preserve the requested lifetime. The maximum duration that a certificate can be backdated with these options is 48 hours in the past. This option cannot be set if allow_requester_specified_not_before_time is set.

` .google.protobuf.Duration backdate_duration = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.Builder.html)` |   
  
### getBackdateDurationOrBuilder()
    
    
    public DurationOrBuilder getBackdateDurationOrBuilder()

Optional. If set, all certificates issued from this CaPool will be backdated by this duration. The 'not_before_time' will be the issuance time minus this backdate_duration, and the 'not_after_time' will be adjusted to preserve the requested lifetime. The maximum duration that a certificate can be backdated with these options is 48 hours in the past. This option cannot be set if allow_requester_specified_not_before_time is set.

` .google.protobuf.Duration backdate_duration = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[DurationOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DurationOrBuilder.html)` |   
  
### getBaselineValues()
    
    
    public X509Parameters getBaselineValues()

Optional. A set of X.509 values that will be applied to all certificates issued through this CaPool. If a certificate request includes conflicting values for the same properties, they will be overwritten by the values defined here. If a certificate request uses a CertificateTemplate that defines conflicting predefined_values for the same properties, the certificate issuance request will fail.

` .google.cloud.security.privateca.v1.X509Parameters baseline_values = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[X509Parameters](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.X509Parameters)` | The baselineValues.  
  
### getBaselineValuesBuilder()
    
    
    public X509Parameters.Builder getBaselineValuesBuilder()

Optional. A set of X.509 values that will be applied to all certificates issued through this CaPool. If a certificate request includes conflicting values for the same properties, they will be overwritten by the values defined here. If a certificate request uses a CertificateTemplate that defines conflicting predefined_values for the same properties, the certificate issuance request will fail.

` .google.cloud.security.privateca.v1.X509Parameters baseline_values = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[X509Parameters.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.X509Parameters.Builder)` |   
  
### getBaselineValuesOrBuilder()
    
    
    public X509ParametersOrBuilder getBaselineValuesOrBuilder()

Optional. A set of X.509 values that will be applied to all certificates issued through this CaPool. If a certificate request includes conflicting values for the same properties, they will be overwritten by the values defined here. If a certificate request uses a CertificateTemplate that defines conflicting predefined_values for the same properties, the certificate issuance request will fail.

` .google.cloud.security.privateca.v1.X509Parameters baseline_values = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[X509ParametersOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.X509ParametersOrBuilder)` |   
  
### getDefaultInstanceForType()
    
    
    public CaPool.IssuancePolicy getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[CaPool.IssuancePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy)` |   
  
### getDescriptorForType()
    
    
    public Descriptors.Descriptor getDescriptorForType()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getDescriptorForType__)

### getIdentityConstraints()
    
    
    public CertificateIdentityConstraints getIdentityConstraints()

Optional. Describes constraints on identities that may appear in Certificates issued through this CaPool. If this is omitted, then this CaPool will not add restrictions on a certificate's identity.

` .google.cloud.security.privateca.v1.CertificateIdentityConstraints identity_constraints = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[CertificateIdentityConstraints](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateIdentityConstraints)` | The identityConstraints.  
  
### getIdentityConstraintsBuilder()
    
    
    public CertificateIdentityConstraints.Builder getIdentityConstraintsBuilder()

Optional. Describes constraints on identities that may appear in Certificates issued through this CaPool. If this is omitted, then this CaPool will not add restrictions on a certificate's identity.

` .google.cloud.security.privateca.v1.CertificateIdentityConstraints identity_constraints = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[CertificateIdentityConstraints.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateIdentityConstraints.Builder)` |   
  
### getIdentityConstraintsOrBuilder()
    
    
    public CertificateIdentityConstraintsOrBuilder getIdentityConstraintsOrBuilder()

Optional. Describes constraints on identities that may appear in Certificates issued through this CaPool. If this is omitted, then this CaPool will not add restrictions on a certificate's identity.

` .google.cloud.security.privateca.v1.CertificateIdentityConstraints identity_constraints = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[CertificateIdentityConstraintsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateIdentityConstraintsOrBuilder)` |   
  
### getMaximumLifetime()
    
    
    public Duration getMaximumLifetime()

Optional. The maximum lifetime allowed for issued Certificates. Note that if the issuing CertificateAuthority expires before a Certificate resource's requested maximum_lifetime, the effective lifetime will be explicitly truncated to match it.

` .google.protobuf.Duration maximum_lifetime = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)` | The maximumLifetime.  
  
### getMaximumLifetimeBuilder()
    
    
    public Duration.Builder getMaximumLifetimeBuilder()

Optional. The maximum lifetime allowed for issued Certificates. Note that if the issuing CertificateAuthority expires before a Certificate resource's requested maximum_lifetime, the effective lifetime will be explicitly truncated to match it.

` .google.protobuf.Duration maximum_lifetime = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.Builder.html)` |   
  
### getMaximumLifetimeOrBuilder()
    
    
    public DurationOrBuilder getMaximumLifetimeOrBuilder()

Optional. The maximum lifetime allowed for issued Certificates. Note that if the issuing CertificateAuthority expires before a Certificate resource's requested maximum_lifetime, the effective lifetime will be explicitly truncated to match it.

` .google.protobuf.Duration maximum_lifetime = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[DurationOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DurationOrBuilder.html)` |   
  
### getPassthroughExtensions()
    
    
    public CertificateExtensionConstraints getPassthroughExtensions()

Optional. Describes the set of X.509 extensions that may appear in a Certificate issued through this CaPool. If a certificate request sets extensions that don't appear in the passthrough_extensions, those extensions will be dropped. If a certificate request uses a CertificateTemplate with predefined_values that don't appear here, the certificate issuance request will fail. If this is omitted, then this CaPool will not add restrictions on a certificate's X.509 extensions. These constraints do not apply to X.509 extensions set in this CaPool's baseline_values.

` .google.cloud.security.privateca.v1.CertificateExtensionConstraints passthrough_extensions = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[CertificateExtensionConstraints](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateExtensionConstraints)` | The passthroughExtensions.  
  
### getPassthroughExtensionsBuilder()
    
    
    public CertificateExtensionConstraints.Builder getPassthroughExtensionsBuilder()

Optional. Describes the set of X.509 extensions that may appear in a Certificate issued through this CaPool. If a certificate request sets extensions that don't appear in the passthrough_extensions, those extensions will be dropped. If a certificate request uses a CertificateTemplate with predefined_values that don't appear here, the certificate issuance request will fail. If this is omitted, then this CaPool will not add restrictions on a certificate's X.509 extensions. These constraints do not apply to X.509 extensions set in this CaPool's baseline_values.

` .google.cloud.security.privateca.v1.CertificateExtensionConstraints passthrough_extensions = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[CertificateExtensionConstraints.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateExtensionConstraints.Builder)` |   
  
### getPassthroughExtensionsOrBuilder()
    
    
    public CertificateExtensionConstraintsOrBuilder getPassthroughExtensionsOrBuilder()

Optional. Describes the set of X.509 extensions that may appear in a Certificate issued through this CaPool. If a certificate request sets extensions that don't appear in the passthrough_extensions, those extensions will be dropped. If a certificate request uses a CertificateTemplate with predefined_values that don't appear here, the certificate issuance request will fail. If this is omitted, then this CaPool will not add restrictions on a certificate's X.509 extensions. These constraints do not apply to X.509 extensions set in this CaPool's baseline_values.

` .google.cloud.security.privateca.v1.CertificateExtensionConstraints passthrough_extensions = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[CertificateExtensionConstraintsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateExtensionConstraintsOrBuilder)` |   
  
### hasAllowedIssuanceModes()
    
    
    public boolean hasAllowedIssuanceModes()

Optional. If specified, then only methods allowed in the IssuanceModes may be used to issue Certificates.

` .google.cloud.security.privateca.v1.CaPool.IssuancePolicy.IssuanceModes allowed_issuance_modes = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the allowedIssuanceModes field is set.  
  
### hasBackdateDuration()
    
    
    public boolean hasBackdateDuration()

Optional. If set, all certificates issued from this CaPool will be backdated by this duration. The 'not_before_time' will be the issuance time minus this backdate_duration, and the 'not_after_time' will be adjusted to preserve the requested lifetime. The maximum duration that a certificate can be backdated with these options is 48 hours in the past. This option cannot be set if allow_requester_specified_not_before_time is set.

` .google.protobuf.Duration backdate_duration = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the backdateDuration field is set.  
  
### hasBaselineValues()
    
    
    public boolean hasBaselineValues()

Optional. A set of X.509 values that will be applied to all certificates issued through this CaPool. If a certificate request includes conflicting values for the same properties, they will be overwritten by the values defined here. If a certificate request uses a CertificateTemplate that defines conflicting predefined_values for the same properties, the certificate issuance request will fail.

` .google.cloud.security.privateca.v1.X509Parameters baseline_values = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the baselineValues field is set.  
  
### hasIdentityConstraints()
    
    
    public boolean hasIdentityConstraints()

Optional. Describes constraints on identities that may appear in Certificates issued through this CaPool. If this is omitted, then this CaPool will not add restrictions on a certificate's identity.

` .google.cloud.security.privateca.v1.CertificateIdentityConstraints identity_constraints = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the identityConstraints field is set.  
  
### hasMaximumLifetime()
    
    
    public boolean hasMaximumLifetime()

Optional. The maximum lifetime allowed for issued Certificates. Note that if the issuing CertificateAuthority expires before a Certificate resource's requested maximum_lifetime, the effective lifetime will be explicitly truncated to match it.

` .google.protobuf.Duration maximum_lifetime = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the maximumLifetime field is set.  
  
### hasPassthroughExtensions()
    
    
    public boolean hasPassthroughExtensions()

Optional. Describes the set of X.509 extensions that may appear in a Certificate issued through this CaPool. If a certificate request sets extensions that don't appear in the passthrough_extensions, those extensions will be dropped. If a certificate request uses a CertificateTemplate with predefined_values that don't appear here, the certificate issuance request will fail. If this is omitted, then this CaPool will not add restrictions on a certificate's X.509 extensions. These constraints do not apply to X.509 extensions set in this CaPool's baseline_values.

` .google.cloud.security.privateca.v1.CertificateExtensionConstraints passthrough_extensions = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the passthroughExtensions field is set.  
  
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

### mergeAllowedIssuanceModes(CaPool.IssuancePolicy.IssuanceModes value)
    
    
    public CaPool.IssuancePolicy.Builder mergeAllowedIssuanceModes(CaPool.IssuancePolicy.IssuanceModes value)

Optional. If specified, then only methods allowed in the IssuanceModes may be used to issue Certificates.

` .google.cloud.security.privateca.v1.CaPool.IssuancePolicy.IssuanceModes allowed_issuance_modes = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[CaPool.IssuancePolicy.IssuanceModes](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.IssuanceModes)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CaPool.IssuancePolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.Builder)` |   
  
### mergeBackdateDuration(Duration value)
    
    
    public CaPool.IssuancePolicy.Builder mergeBackdateDuration(Duration value)

Optional. If set, all certificates issued from this CaPool will be backdated by this duration. The 'not_before_time' will be the issuance time minus this backdate_duration, and the 'not_after_time' will be adjusted to preserve the requested lifetime. The maximum duration that a certificate can be backdated with these options is 48 hours in the past. This option cannot be set if allow_requester_specified_not_before_time is set.

` .google.protobuf.Duration backdate_duration = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CaPool.IssuancePolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.Builder)` |   
  
### mergeBaselineValues(X509Parameters value)
    
    
    public CaPool.IssuancePolicy.Builder mergeBaselineValues(X509Parameters value)

Optional. A set of X.509 values that will be applied to all certificates issued through this CaPool. If a certificate request includes conflicting values for the same properties, they will be overwritten by the values defined here. If a certificate request uses a CertificateTemplate that defines conflicting predefined_values for the same properties, the certificate issuance request will fail.

` .google.cloud.security.privateca.v1.X509Parameters baseline_values = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[X509Parameters](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.X509Parameters)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CaPool.IssuancePolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.Builder)` |   
  
### mergeFrom(CaPool.IssuancePolicy other)
    
    
    public CaPool.IssuancePolicy.Builder mergeFrom(CaPool.IssuancePolicy other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CaPool.IssuancePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CaPool.IssuancePolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public CaPool.IssuancePolicy.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CaPool.IssuancePolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public CaPool.IssuancePolicy.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CaPool.IssuancePolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### mergeIdentityConstraints(CertificateIdentityConstraints value)
    
    
    public CaPool.IssuancePolicy.Builder mergeIdentityConstraints(CertificateIdentityConstraints value)

Optional. Describes constraints on identities that may appear in Certificates issued through this CaPool. If this is omitted, then this CaPool will not add restrictions on a certificate's identity.

` .google.cloud.security.privateca.v1.CertificateIdentityConstraints identity_constraints = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[CertificateIdentityConstraints](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateIdentityConstraints)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CaPool.IssuancePolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.Builder)` |   
  
### mergeMaximumLifetime(Duration value)
    
    
    public CaPool.IssuancePolicy.Builder mergeMaximumLifetime(Duration value)

Optional. The maximum lifetime allowed for issued Certificates. Note that if the issuing CertificateAuthority expires before a Certificate resource's requested maximum_lifetime, the effective lifetime will be explicitly truncated to match it.

` .google.protobuf.Duration maximum_lifetime = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CaPool.IssuancePolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.Builder)` |   
  
### mergePassthroughExtensions(CertificateExtensionConstraints value)
    
    
    public CaPool.IssuancePolicy.Builder mergePassthroughExtensions(CertificateExtensionConstraints value)

Optional. Describes the set of X.509 extensions that may appear in a Certificate issued through this CaPool. If a certificate request sets extensions that don't appear in the passthrough_extensions, those extensions will be dropped. If a certificate request uses a CertificateTemplate with predefined_values that don't appear here, the certificate issuance request will fail. If this is omitted, then this CaPool will not add restrictions on a certificate's X.509 extensions. These constraints do not apply to X.509 extensions set in this CaPool's baseline_values.

` .google.cloud.security.privateca.v1.CertificateExtensionConstraints passthrough_extensions = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[CertificateExtensionConstraints](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateExtensionConstraints)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CaPool.IssuancePolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.Builder)` |   
  
### removeAllowedKeyTypes(int index)
    
    
    public CaPool.IssuancePolicy.Builder removeAllowedKeyTypes(int index)

Optional. If any AllowedKeyType is specified, then the certificate request's public key must match one of the key types listed here. Otherwise, any key may be used.

` repeated .google.cloud.security.privateca.v1.CaPool.IssuancePolicy.AllowedKeyType allowed_key_types = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CaPool.IssuancePolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.Builder)` |   
  
### setAllowRequesterSpecifiedNotBeforeTime(boolean value)
    
    
    public CaPool.IssuancePolicy.Builder setAllowRequesterSpecifiedNotBeforeTime(boolean value)

Optional. If set to true, allows requesters to specify the requested_not_before_time field when creating a Certificate. Certificates requested with this option enabled will have a 'not_before_time' equal to the value specified in the request. The 'not_after_time' will be adjusted to preserve the requested lifetime. The maximum time that a certificate can be backdated with these options is 48 hours in the past. This option cannot be set if backdate_duration is set.

` bool allow_requester_specified_not_before_time = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The allowRequesterSpecifiedNotBeforeTime to set.  
**Returns**  
---  
**Type** | **Description**  
`[CaPool.IssuancePolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.Builder)` | This builder for chaining.  
  
### setAllowedIssuanceModes(CaPool.IssuancePolicy.IssuanceModes value)
    
    
    public CaPool.IssuancePolicy.Builder setAllowedIssuanceModes(CaPool.IssuancePolicy.IssuanceModes value)

Optional. If specified, then only methods allowed in the IssuanceModes may be used to issue Certificates.

` .google.cloud.security.privateca.v1.CaPool.IssuancePolicy.IssuanceModes allowed_issuance_modes = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[CaPool.IssuancePolicy.IssuanceModes](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.IssuanceModes)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CaPool.IssuancePolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.Builder)` |   
  
### setAllowedIssuanceModes(CaPool.IssuancePolicy.IssuanceModes.Builder builderForValue)
    
    
    public CaPool.IssuancePolicy.Builder setAllowedIssuanceModes(CaPool.IssuancePolicy.IssuanceModes.Builder builderForValue)

Optional. If specified, then only methods allowed in the IssuanceModes may be used to issue Certificates.

` .google.cloud.security.privateca.v1.CaPool.IssuancePolicy.IssuanceModes allowed_issuance_modes = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[CaPool.IssuancePolicy.IssuanceModes.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.IssuanceModes.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CaPool.IssuancePolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.Builder)` |   
  
### setAllowedKeyTypes(int index, CaPool.IssuancePolicy.AllowedKeyType value)
    
    
    public CaPool.IssuancePolicy.Builder setAllowedKeyTypes(int index, CaPool.IssuancePolicy.AllowedKeyType value)

Optional. If any AllowedKeyType is specified, then the certificate request's public key must match one of the key types listed here. Otherwise, any key may be used.

` repeated .google.cloud.security.privateca.v1.CaPool.IssuancePolicy.AllowedKeyType allowed_key_types = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[CaPool.IssuancePolicy.AllowedKeyType](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.AllowedKeyType)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CaPool.IssuancePolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.Builder)` |   
  
### setAllowedKeyTypes(int index, CaPool.IssuancePolicy.AllowedKeyType.Builder builderForValue)
    
    
    public CaPool.IssuancePolicy.Builder setAllowedKeyTypes(int index, CaPool.IssuancePolicy.AllowedKeyType.Builder builderForValue)

Optional. If any AllowedKeyType is specified, then the certificate request's public key must match one of the key types listed here. Otherwise, any key may be used.

` repeated .google.cloud.security.privateca.v1.CaPool.IssuancePolicy.AllowedKeyType allowed_key_types = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[CaPool.IssuancePolicy.AllowedKeyType.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.AllowedKeyType.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CaPool.IssuancePolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.Builder)` |   
  
### setBackdateDuration(Duration value)
    
    
    public CaPool.IssuancePolicy.Builder setBackdateDuration(Duration value)

Optional. If set, all certificates issued from this CaPool will be backdated by this duration. The 'not_before_time' will be the issuance time minus this backdate_duration, and the 'not_after_time' will be adjusted to preserve the requested lifetime. The maximum duration that a certificate can be backdated with these options is 48 hours in the past. This option cannot be set if allow_requester_specified_not_before_time is set.

` .google.protobuf.Duration backdate_duration = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CaPool.IssuancePolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.Builder)` |   
  
### setBackdateDuration(Duration.Builder builderForValue)
    
    
    public CaPool.IssuancePolicy.Builder setBackdateDuration(Duration.Builder builderForValue)

Optional. If set, all certificates issued from this CaPool will be backdated by this duration. The 'not_before_time' will be the issuance time minus this backdate_duration, and the 'not_after_time' will be adjusted to preserve the requested lifetime. The maximum duration that a certificate can be backdated with these options is 48 hours in the past. This option cannot be set if allow_requester_specified_not_before_time is set.

` .google.protobuf.Duration backdate_duration = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CaPool.IssuancePolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.Builder)` |   
  
### setBaselineValues(X509Parameters value)
    
    
    public CaPool.IssuancePolicy.Builder setBaselineValues(X509Parameters value)

Optional. A set of X.509 values that will be applied to all certificates issued through this CaPool. If a certificate request includes conflicting values for the same properties, they will be overwritten by the values defined here. If a certificate request uses a CertificateTemplate that defines conflicting predefined_values for the same properties, the certificate issuance request will fail.

` .google.cloud.security.privateca.v1.X509Parameters baseline_values = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[X509Parameters](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.X509Parameters)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CaPool.IssuancePolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.Builder)` |   
  
### setBaselineValues(X509Parameters.Builder builderForValue)
    
    
    public CaPool.IssuancePolicy.Builder setBaselineValues(X509Parameters.Builder builderForValue)

Optional. A set of X.509 values that will be applied to all certificates issued through this CaPool. If a certificate request includes conflicting values for the same properties, they will be overwritten by the values defined here. If a certificate request uses a CertificateTemplate that defines conflicting predefined_values for the same properties, the certificate issuance request will fail.

` .google.cloud.security.privateca.v1.X509Parameters baseline_values = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[X509Parameters.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.X509Parameters.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CaPool.IssuancePolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.Builder)` |   
  
### setIdentityConstraints(CertificateIdentityConstraints value)
    
    
    public CaPool.IssuancePolicy.Builder setIdentityConstraints(CertificateIdentityConstraints value)

Optional. Describes constraints on identities that may appear in Certificates issued through this CaPool. If this is omitted, then this CaPool will not add restrictions on a certificate's identity.

` .google.cloud.security.privateca.v1.CertificateIdentityConstraints identity_constraints = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[CertificateIdentityConstraints](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateIdentityConstraints)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CaPool.IssuancePolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.Builder)` |   
  
### setIdentityConstraints(CertificateIdentityConstraints.Builder builderForValue)
    
    
    public CaPool.IssuancePolicy.Builder setIdentityConstraints(CertificateIdentityConstraints.Builder builderForValue)

Optional. Describes constraints on identities that may appear in Certificates issued through this CaPool. If this is omitted, then this CaPool will not add restrictions on a certificate's identity.

` .google.cloud.security.privateca.v1.CertificateIdentityConstraints identity_constraints = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[CertificateIdentityConstraints.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateIdentityConstraints.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CaPool.IssuancePolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.Builder)` |   
  
### setMaximumLifetime(Duration value)
    
    
    public CaPool.IssuancePolicy.Builder setMaximumLifetime(Duration value)

Optional. The maximum lifetime allowed for issued Certificates. Note that if the issuing CertificateAuthority expires before a Certificate resource's requested maximum_lifetime, the effective lifetime will be explicitly truncated to match it.

` .google.protobuf.Duration maximum_lifetime = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CaPool.IssuancePolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.Builder)` |   
  
### setMaximumLifetime(Duration.Builder builderForValue)
    
    
    public CaPool.IssuancePolicy.Builder setMaximumLifetime(Duration.Builder builderForValue)

Optional. The maximum lifetime allowed for issued Certificates. Note that if the issuing CertificateAuthority expires before a Certificate resource's requested maximum_lifetime, the effective lifetime will be explicitly truncated to match it.

` .google.protobuf.Duration maximum_lifetime = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CaPool.IssuancePolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.Builder)` |   
  
### setPassthroughExtensions(CertificateExtensionConstraints value)
    
    
    public CaPool.IssuancePolicy.Builder setPassthroughExtensions(CertificateExtensionConstraints value)

Optional. Describes the set of X.509 extensions that may appear in a Certificate issued through this CaPool. If a certificate request sets extensions that don't appear in the passthrough_extensions, those extensions will be dropped. If a certificate request uses a CertificateTemplate with predefined_values that don't appear here, the certificate issuance request will fail. If this is omitted, then this CaPool will not add restrictions on a certificate's X.509 extensions. These constraints do not apply to X.509 extensions set in this CaPool's baseline_values.

` .google.cloud.security.privateca.v1.CertificateExtensionConstraints passthrough_extensions = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[CertificateExtensionConstraints](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateExtensionConstraints)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CaPool.IssuancePolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.Builder)` |   
  
### setPassthroughExtensions(CertificateExtensionConstraints.Builder builderForValue)
    
    
    public CaPool.IssuancePolicy.Builder setPassthroughExtensions(CertificateExtensionConstraints.Builder builderForValue)

Optional. Describes the set of X.509 extensions that may appear in a Certificate issued through this CaPool. If a certificate request sets extensions that don't appear in the passthrough_extensions, those extensions will be dropped. If a certificate request uses a CertificateTemplate with predefined_values that don't appear here, the certificate issuance request will fail. If this is omitted, then this CaPool will not add restrictions on a certificate's X.509 extensions. These constraints do not apply to X.509 extensions set in this CaPool's baseline_values.

` .google.cloud.security.privateca.v1.CertificateExtensionConstraints passthrough_extensions = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[CertificateExtensionConstraints.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateExtensionConstraints.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CaPool.IssuancePolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool.IssuancePolicy.Builder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
