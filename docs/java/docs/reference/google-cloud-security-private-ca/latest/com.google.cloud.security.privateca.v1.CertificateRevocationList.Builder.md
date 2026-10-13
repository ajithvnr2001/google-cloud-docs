---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList.Builder
title: Class CertificateRevocationList.Builder (2.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:13:59.001160+00:00
---

# Class CertificateRevocationList.Builder (2.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class CertificateRevocationList.Builder (2.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.101.0 (latest)  2.97.0  2.96.0  2.95.0  2.93.0  2.90.0  2.89.0  2.87.0  2.85.0  2.84.0  2.82.0  2.80.0  2.78.0  2.77.0  2.76.0  2.75.0  2.74.0  2.72.0  2.70.0  2.69.0  2.66.0  2.65.0  2.64.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.4  2.4.0  2.3.0  2.2.5 
    
    
    public static final class CertificateRevocationList.Builder extends GeneratedMessage.Builder<CertificateRevocationList.Builder> implements CertificateRevocationListOrBuilder

A CertificateRevocationList corresponds to a signed X.509 certificate Revocation List (CRL). A CRL contains the serial numbers of certificates that should no longer be trusted.

Protobuf type `google.cloud.security.privateca.v1.CertificateRevocationList`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > CertificateRevocationList.Builder

## Implements

[CertificateRevocationListOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationListOrBuilder)

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

### addAllRevokedCertificates(Iterable<? extends CertificateRevocationList.RevokedCertificate> values)
    
    
    public CertificateRevocationList.Builder addAllRevokedCertificates(Iterable<? extends CertificateRevocationList.RevokedCertificate> values)

Output only. The revoked serial numbers that appear in pem_crl.

` repeated .google.cloud.security.privateca.v1.CertificateRevocationList.RevokedCertificate revoked_certificates = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<? extends com.google.cloud.security.privateca.v1.CertificateRevocationList.RevokedCertificate>`  
  
**Returns**  
---  
**Type** | **Description**  
`[CertificateRevocationList.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList.Builder)` |   
  
### addRevokedCertificates(CertificateRevocationList.RevokedCertificate value)
    
    
    public CertificateRevocationList.Builder addRevokedCertificates(CertificateRevocationList.RevokedCertificate value)

Output only. The revoked serial numbers that appear in pem_crl.

` repeated .google.cloud.security.privateca.v1.CertificateRevocationList.RevokedCertificate revoked_certificates = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[CertificateRevocationList.RevokedCertificate](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList.RevokedCertificate)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CertificateRevocationList.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList.Builder)` |   
  
### addRevokedCertificates(CertificateRevocationList.RevokedCertificate.Builder builderForValue)
    
    
    public CertificateRevocationList.Builder addRevokedCertificates(CertificateRevocationList.RevokedCertificate.Builder builderForValue)

Output only. The revoked serial numbers that appear in pem_crl.

` repeated .google.cloud.security.privateca.v1.CertificateRevocationList.RevokedCertificate revoked_certificates = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[CertificateRevocationList.RevokedCertificate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList.RevokedCertificate.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CertificateRevocationList.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList.Builder)` |   
  
### addRevokedCertificates(int index, CertificateRevocationList.RevokedCertificate value)
    
    
    public CertificateRevocationList.Builder addRevokedCertificates(int index, CertificateRevocationList.RevokedCertificate value)

Output only. The revoked serial numbers that appear in pem_crl.

` repeated .google.cloud.security.privateca.v1.CertificateRevocationList.RevokedCertificate revoked_certificates = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[CertificateRevocationList.RevokedCertificate](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList.RevokedCertificate)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CertificateRevocationList.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList.Builder)` |   
  
### addRevokedCertificates(int index, CertificateRevocationList.RevokedCertificate.Builder builderForValue)
    
    
    public CertificateRevocationList.Builder addRevokedCertificates(int index, CertificateRevocationList.RevokedCertificate.Builder builderForValue)

Output only. The revoked serial numbers that appear in pem_crl.

` repeated .google.cloud.security.privateca.v1.CertificateRevocationList.RevokedCertificate revoked_certificates = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[CertificateRevocationList.RevokedCertificate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList.RevokedCertificate.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CertificateRevocationList.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList.Builder)` |   
  
### addRevokedCertificatesBuilder()
    
    
    public CertificateRevocationList.RevokedCertificate.Builder addRevokedCertificatesBuilder()

Output only. The revoked serial numbers that appear in pem_crl.

` repeated .google.cloud.security.privateca.v1.CertificateRevocationList.RevokedCertificate revoked_certificates = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[CertificateRevocationList.RevokedCertificate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList.RevokedCertificate.Builder)` |   
  
### addRevokedCertificatesBuilder(int index)
    
    
    public CertificateRevocationList.RevokedCertificate.Builder addRevokedCertificatesBuilder(int index)

Output only. The revoked serial numbers that appear in pem_crl.

` repeated .google.cloud.security.privateca.v1.CertificateRevocationList.RevokedCertificate revoked_certificates = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CertificateRevocationList.RevokedCertificate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList.RevokedCertificate.Builder)` |   
  
### build()
    
    
    public CertificateRevocationList build()

**Returns**  
---  
**Type** | **Description**  
`[CertificateRevocationList](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList)` |   
  
### buildPartial()
    
    
    public CertificateRevocationList buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[CertificateRevocationList](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList)` |   
  
### clear()
    
    
    public CertificateRevocationList.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[CertificateRevocationList.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearAccessUrl()
    
    
    public CertificateRevocationList.Builder clearAccessUrl()

Output only. The location where 'pem_crl' can be accessed.

`string access_url = 5 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[CertificateRevocationList.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList.Builder)` | This builder for chaining.  
  
### clearCreateTime()
    
    
    public CertificateRevocationList.Builder clearCreateTime()

Output only. The time at which this CertificateRevocationList was created.

` .google.protobuf.Timestamp create_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[CertificateRevocationList.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList.Builder)` |   
  
### clearLabels()
    
    
    public CertificateRevocationList.Builder clearLabels()

**Returns**  
---  
**Type** | **Description**  
`[CertificateRevocationList.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList.Builder)` |   
  
### clearName()
    
    
    public CertificateRevocationList.Builder clearName()

Identifier. The resource name for this CertificateRevocationList in the format `projects/*/locations/*/caPools/*certificateAuthorities/*/ certificateRevocationLists/*`.

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[CertificateRevocationList.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList.Builder)` | This builder for chaining.  
  
### clearPemCrl()
    
    
    public CertificateRevocationList.Builder clearPemCrl()

Output only. The PEM-encoded X.509 CRL.

`string pem_crl = 4 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[CertificateRevocationList.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList.Builder)` | This builder for chaining.  
  
### clearRevisionId()
    
    
    public CertificateRevocationList.Builder clearRevisionId()

Output only. The revision ID of this CertificateRevocationList. A new revision is committed whenever a new CRL is published. The format is an 8-character hexadecimal string.

`string revision_id = 9 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[CertificateRevocationList.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList.Builder)` | This builder for chaining.  
  
### clearRevokedCertificates()
    
    
    public CertificateRevocationList.Builder clearRevokedCertificates()

Output only. The revoked serial numbers that appear in pem_crl.

` repeated .google.cloud.security.privateca.v1.CertificateRevocationList.RevokedCertificate revoked_certificates = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[CertificateRevocationList.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList.Builder)` |   
  
### clearSequenceNumber()
    
    
    public CertificateRevocationList.Builder clearSequenceNumber()

Output only. The CRL sequence number that appears in pem_crl.

`int64 sequence_number = 2 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[CertificateRevocationList.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList.Builder)` | This builder for chaining.  
  
### clearState()
    
    
    public CertificateRevocationList.Builder clearState()

Output only. The State for this CertificateRevocationList.

` .google.cloud.security.privateca.v1.CertificateRevocationList.State state = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[CertificateRevocationList.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList.Builder)` | This builder for chaining.  
  
### clearUpdateTime()
    
    
    public CertificateRevocationList.Builder clearUpdateTime()

Output only. The time at which this CertificateRevocationList was updated.

` .google.protobuf.Timestamp update_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[CertificateRevocationList.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList.Builder)` |   
  
### containsLabels(String key)
    
    
    public boolean containsLabels(String key)

Optional. Labels with user-defined metadata.

`map<string, string> labels = 10 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAccessUrl()
    
    
    public String getAccessUrl()

Output only. The location where 'pem_crl' can be accessed.

`string access_url = 5 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The accessUrl.  
  
### getAccessUrlBytes()
    
    
    public ByteString getAccessUrlBytes()

Output only. The location where 'pem_crl' can be accessed.

`string access_url = 5 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for accessUrl.  
  
### getCreateTime()
    
    
    public Timestamp getCreateTime()

Output only. The time at which this CertificateRevocationList was created.

` .google.protobuf.Timestamp create_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeBuilder()
    
    
    public Timestamp.Builder getCreateTimeBuilder()

Output only. The time at which this CertificateRevocationList was created.

` .google.protobuf.Timestamp create_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)` |   
  
### getCreateTimeOrBuilder()
    
    
    public TimestampOrBuilder getCreateTimeOrBuilder()

Output only. The time at which this CertificateRevocationList was created.

` .google.protobuf.Timestamp create_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDefaultInstanceForType()
    
    
    public CertificateRevocationList getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[CertificateRevocationList](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList)` |   
  
### getDescriptorForType()
    
    
    public Descriptors.Descriptor getDescriptorForType()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getDescriptorForType__)

### getLabels() (deprecated)
    
    
    public Map<String,String> getLabels()

Use [#getLabelsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList.Builder#com_google_cloud_security_privateca_v1_CertificateRevocationList_Builder_getLabelsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsCount()
    
    
    public int getLabelsCount()

Optional. Labels with user-defined metadata.

`map<string, string> labels = 10 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getLabelsMap()
    
    
    public Map<String,String> getLabelsMap()

Optional. Labels with user-defined metadata.

`map<string, string> labels = 10 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsOrDefault(String key, String defaultValue)
    
    
    public String getLabelsOrDefault(String key, String defaultValue)

Optional. Labels with user-defined metadata.

`map<string, string> labels = 10 [(.google.api.field_behavior) = OPTIONAL];`

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

Optional. Labels with user-defined metadata.

`map<string, string> labels = 10 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getMutableLabels() (deprecated)
    
    
    public Map<String,String> getMutableLabels()

Use alternate mutation accessors instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getName()
    
    
    public String getName()

Identifier. The resource name for this CertificateRevocationList in the format `projects/*/locations/*/caPools/*certificateAuthorities/*/ certificateRevocationLists/*`.

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public ByteString getNameBytes()

Identifier. The resource name for this CertificateRevocationList in the format `projects/*/locations/*/caPools/*certificateAuthorities/*/ certificateRevocationLists/*`.

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getPemCrl()
    
    
    public String getPemCrl()

Output only. The PEM-encoded X.509 CRL.

`string pem_crl = 4 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The pemCrl.  
  
### getPemCrlBytes()
    
    
    public ByteString getPemCrlBytes()

Output only. The PEM-encoded X.509 CRL.

`string pem_crl = 4 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for pemCrl.  
  
### getRevisionId()
    
    
    public String getRevisionId()

Output only. The revision ID of this CertificateRevocationList. A new revision is committed whenever a new CRL is published. The format is an 8-character hexadecimal string.

`string revision_id = 9 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The revisionId.  
  
### getRevisionIdBytes()
    
    
    public ByteString getRevisionIdBytes()

Output only. The revision ID of this CertificateRevocationList. A new revision is committed whenever a new CRL is published. The format is an 8-character hexadecimal string.

`string revision_id = 9 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for revisionId.  
  
### getRevokedCertificates(int index)
    
    
    public CertificateRevocationList.RevokedCertificate getRevokedCertificates(int index)

Output only. The revoked serial numbers that appear in pem_crl.

` repeated .google.cloud.security.privateca.v1.CertificateRevocationList.RevokedCertificate revoked_certificates = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CertificateRevocationList.RevokedCertificate](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList.RevokedCertificate)` |   
  
### getRevokedCertificatesBuilder(int index)
    
    
    public CertificateRevocationList.RevokedCertificate.Builder getRevokedCertificatesBuilder(int index)

Output only. The revoked serial numbers that appear in pem_crl.

` repeated .google.cloud.security.privateca.v1.CertificateRevocationList.RevokedCertificate revoked_certificates = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CertificateRevocationList.RevokedCertificate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList.RevokedCertificate.Builder)` |   
  
### getRevokedCertificatesBuilderList()
    
    
    public List<CertificateRevocationList.RevokedCertificate.Builder> getRevokedCertificatesBuilderList()

Output only. The revoked serial numbers that appear in pem_crl.

` repeated .google.cloud.security.privateca.v1.CertificateRevocationList.RevokedCertificate revoked_certificates = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList.RevokedCertificate.Builder)>` |   
  
### getRevokedCertificatesCount()
    
    
    public int getRevokedCertificatesCount()

Output only. The revoked serial numbers that appear in pem_crl.

` repeated .google.cloud.security.privateca.v1.CertificateRevocationList.RevokedCertificate revoked_certificates = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getRevokedCertificatesList()
    
    
    public List<CertificateRevocationList.RevokedCertificate> getRevokedCertificatesList()

Output only. The revoked serial numbers that appear in pem_crl.

` repeated .google.cloud.security.privateca.v1.CertificateRevocationList.RevokedCertificate revoked_certificates = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[RevokedCertificate](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList.RevokedCertificate)>` |   
  
### getRevokedCertificatesOrBuilder(int index)
    
    
    public CertificateRevocationList.RevokedCertificateOrBuilder getRevokedCertificatesOrBuilder(int index)

Output only. The revoked serial numbers that appear in pem_crl.

` repeated .google.cloud.security.privateca.v1.CertificateRevocationList.RevokedCertificate revoked_certificates = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CertificateRevocationList.RevokedCertificateOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList.RevokedCertificateOrBuilder)` |   
  
### getRevokedCertificatesOrBuilderList()
    
    
    public List<? extends CertificateRevocationList.RevokedCertificateOrBuilder> getRevokedCertificatesOrBuilderList()

Output only. The revoked serial numbers that appear in pem_crl.

` repeated .google.cloud.security.privateca.v1.CertificateRevocationList.RevokedCertificate revoked_certificates = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.security.privateca.v1.CertificateRevocationList.RevokedCertificateOrBuilder>` |   
  
### getSequenceNumber()
    
    
    public long getSequenceNumber()

Output only. The CRL sequence number that appears in pem_crl.

`int64 sequence_number = 2 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The sequenceNumber.  
  
### getState()
    
    
    public CertificateRevocationList.State getState()

Output only. The State for this CertificateRevocationList.

` .google.cloud.security.privateca.v1.CertificateRevocationList.State state = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[CertificateRevocationList.State](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList.State)` | The state.  
  
### getStateValue()
    
    
    public int getStateValue()

Output only. The State for this CertificateRevocationList.

` .google.cloud.security.privateca.v1.CertificateRevocationList.State state = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for state.  
  
### getUpdateTime()
    
    
    public Timestamp getUpdateTime()

Output only. The time at which this CertificateRevocationList was updated.

` .google.protobuf.Timestamp update_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The updateTime.  
  
### getUpdateTimeBuilder()
    
    
    public Timestamp.Builder getUpdateTimeBuilder()

Output only. The time at which this CertificateRevocationList was updated.

` .google.protobuf.Timestamp update_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)` |   
  
### getUpdateTimeOrBuilder()
    
    
    public TimestampOrBuilder getUpdateTimeOrBuilder()

Output only. The time at which this CertificateRevocationList was updated.

` .google.protobuf.Timestamp update_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### hasCreateTime()
    
    
    public boolean hasCreateTime()

Output only. The time at which this CertificateRevocationList was created.

` .google.protobuf.Timestamp create_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasUpdateTime()
    
    
    public boolean hasUpdateTime()

Output only. The time at which this CertificateRevocationList was updated.

` .google.protobuf.Timestamp update_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

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
    
    
    public CertificateRevocationList.Builder mergeCreateTime(Timestamp value)

Output only. The time at which this CertificateRevocationList was created.

` .google.protobuf.Timestamp create_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CertificateRevocationList.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList.Builder)` |   
  
### mergeFrom(CertificateRevocationList other)
    
    
    public CertificateRevocationList.Builder mergeFrom(CertificateRevocationList other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CertificateRevocationList](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CertificateRevocationList.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public CertificateRevocationList.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CertificateRevocationList.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public CertificateRevocationList.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CertificateRevocationList.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### mergeUpdateTime(Timestamp value)
    
    
    public CertificateRevocationList.Builder mergeUpdateTime(Timestamp value)

Output only. The time at which this CertificateRevocationList was updated.

` .google.protobuf.Timestamp update_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CertificateRevocationList.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList.Builder)` |   
  
### putAllLabels(Map<String,String> values)
    
    
    public CertificateRevocationList.Builder putAllLabels(Map<String,String> values)

Optional. Labels with user-defined metadata.

`map<string, string> labels = 10 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[CertificateRevocationList.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList.Builder)` |   
  
### putLabels(String key, String value)
    
    
    public CertificateRevocationList.Builder putLabels(String key, String value)

Optional. Labels with user-defined metadata.

`map<string, string> labels = 10 [(.google.api.field_behavior) = OPTIONAL];`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CertificateRevocationList.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList.Builder)` |   
  
### removeLabels(String key)
    
    
    public CertificateRevocationList.Builder removeLabels(String key)

Optional. Labels with user-defined metadata.

`map<string, string> labels = 10 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CertificateRevocationList.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList.Builder)` |   
  
### removeRevokedCertificates(int index)
    
    
    public CertificateRevocationList.Builder removeRevokedCertificates(int index)

Output only. The revoked serial numbers that appear in pem_crl.

` repeated .google.cloud.security.privateca.v1.CertificateRevocationList.RevokedCertificate revoked_certificates = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CertificateRevocationList.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList.Builder)` |   
  
### setAccessUrl(String value)
    
    
    public CertificateRevocationList.Builder setAccessUrl(String value)

Output only. The location where 'pem_crl' can be accessed.

`string access_url = 5 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The accessUrl to set.  
**Returns**  
---  
**Type** | **Description**  
`[CertificateRevocationList.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList.Builder)` | This builder for chaining.  
  
### setAccessUrlBytes(ByteString value)
    
    
    public CertificateRevocationList.Builder setAccessUrlBytes(ByteString value)

Output only. The location where 'pem_crl' can be accessed.

`string access_url = 5 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for accessUrl to set.  
**Returns**  
---  
**Type** | **Description**  
`[CertificateRevocationList.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList.Builder)` | This builder for chaining.  
  
### setCreateTime(Timestamp value)
    
    
    public CertificateRevocationList.Builder setCreateTime(Timestamp value)

Output only. The time at which this CertificateRevocationList was created.

` .google.protobuf.Timestamp create_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CertificateRevocationList.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList.Builder)` |   
  
### setCreateTime(Timestamp.Builder builderForValue)
    
    
    public CertificateRevocationList.Builder setCreateTime(Timestamp.Builder builderForValue)

Output only. The time at which this CertificateRevocationList was created.

` .google.protobuf.Timestamp create_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CertificateRevocationList.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList.Builder)` |   
  
### setName(String value)
    
    
    public CertificateRevocationList.Builder setName(String value)

Identifier. The resource name for this CertificateRevocationList in the format `projects/*/locations/*/caPools/*certificateAuthorities/*/ certificateRevocationLists/*`.

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name to set.  
**Returns**  
---  
**Type** | **Description**  
`[CertificateRevocationList.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList.Builder)` | This builder for chaining.  
  
### setNameBytes(ByteString value)
    
    
    public CertificateRevocationList.Builder setNameBytes(ByteString value)

Identifier. The resource name for this CertificateRevocationList in the format `projects/*/locations/*/caPools/*certificateAuthorities/*/ certificateRevocationLists/*`.

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for name to set.  
**Returns**  
---  
**Type** | **Description**  
`[CertificateRevocationList.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList.Builder)` | This builder for chaining.  
  
### setPemCrl(String value)
    
    
    public CertificateRevocationList.Builder setPemCrl(String value)

Output only. The PEM-encoded X.509 CRL.

`string pem_crl = 4 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The pemCrl to set.  
**Returns**  
---  
**Type** | **Description**  
`[CertificateRevocationList.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList.Builder)` | This builder for chaining.  
  
### setPemCrlBytes(ByteString value)
    
    
    public CertificateRevocationList.Builder setPemCrlBytes(ByteString value)

Output only. The PEM-encoded X.509 CRL.

`string pem_crl = 4 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for pemCrl to set.  
**Returns**  
---  
**Type** | **Description**  
`[CertificateRevocationList.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList.Builder)` | This builder for chaining.  
  
### setRevisionId(String value)
    
    
    public CertificateRevocationList.Builder setRevisionId(String value)

Output only. The revision ID of this CertificateRevocationList. A new revision is committed whenever a new CRL is published. The format is an 8-character hexadecimal string.

`string revision_id = 9 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The revisionId to set.  
**Returns**  
---  
**Type** | **Description**  
`[CertificateRevocationList.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList.Builder)` | This builder for chaining.  
  
### setRevisionIdBytes(ByteString value)
    
    
    public CertificateRevocationList.Builder setRevisionIdBytes(ByteString value)

Output only. The revision ID of this CertificateRevocationList. A new revision is committed whenever a new CRL is published. The format is an 8-character hexadecimal string.

`string revision_id = 9 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for revisionId to set.  
**Returns**  
---  
**Type** | **Description**  
`[CertificateRevocationList.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList.Builder)` | This builder for chaining.  
  
### setRevokedCertificates(int index, CertificateRevocationList.RevokedCertificate value)
    
    
    public CertificateRevocationList.Builder setRevokedCertificates(int index, CertificateRevocationList.RevokedCertificate value)

Output only. The revoked serial numbers that appear in pem_crl.

` repeated .google.cloud.security.privateca.v1.CertificateRevocationList.RevokedCertificate revoked_certificates = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[CertificateRevocationList.RevokedCertificate](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList.RevokedCertificate)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CertificateRevocationList.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList.Builder)` |   
  
### setRevokedCertificates(int index, CertificateRevocationList.RevokedCertificate.Builder builderForValue)
    
    
    public CertificateRevocationList.Builder setRevokedCertificates(int index, CertificateRevocationList.RevokedCertificate.Builder builderForValue)

Output only. The revoked serial numbers that appear in pem_crl.

` repeated .google.cloud.security.privateca.v1.CertificateRevocationList.RevokedCertificate revoked_certificates = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[CertificateRevocationList.RevokedCertificate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList.RevokedCertificate.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CertificateRevocationList.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList.Builder)` |   
  
### setSequenceNumber(long value)
    
    
    public CertificateRevocationList.Builder setSequenceNumber(long value)

Output only. The CRL sequence number that appears in pem_crl.

`int64 sequence_number = 2 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The sequenceNumber to set.  
**Returns**  
---  
**Type** | **Description**  
`[CertificateRevocationList.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList.Builder)` | This builder for chaining.  
  
### setState(CertificateRevocationList.State value)
    
    
    public CertificateRevocationList.Builder setState(CertificateRevocationList.State value)

Output only. The State for this CertificateRevocationList.

` .google.cloud.security.privateca.v1.CertificateRevocationList.State state = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[CertificateRevocationList.State](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList.State)`  
The state to set.  
**Returns**  
---  
**Type** | **Description**  
`[CertificateRevocationList.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList.Builder)` | This builder for chaining.  
  
### setStateValue(int value)
    
    
    public CertificateRevocationList.Builder setStateValue(int value)

Output only. The State for this CertificateRevocationList.

` .google.cloud.security.privateca.v1.CertificateRevocationList.State state = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The enum numeric value on the wire for state to set.  
**Returns**  
---  
**Type** | **Description**  
`[CertificateRevocationList.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList.Builder)` | This builder for chaining.  
  
### setUpdateTime(Timestamp value)
    
    
    public CertificateRevocationList.Builder setUpdateTime(Timestamp value)

Output only. The time at which this CertificateRevocationList was updated.

` .google.protobuf.Timestamp update_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CertificateRevocationList.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList.Builder)` |   
  
### setUpdateTime(Timestamp.Builder builderForValue)
    
    
    public CertificateRevocationList.Builder setUpdateTime(Timestamp.Builder builderForValue)

Output only. The time at which this CertificateRevocationList was updated.

` .google.protobuf.Timestamp update_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CertificateRevocationList.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList.Builder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
