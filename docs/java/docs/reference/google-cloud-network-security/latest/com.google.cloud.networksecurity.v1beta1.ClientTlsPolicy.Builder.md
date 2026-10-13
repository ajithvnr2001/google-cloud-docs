---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ClientTlsPolicy.Builder
title: Class ClientTlsPolicy.Builder (0.102.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:23:52.536572+00:00
---

# Class ClientTlsPolicy.Builder (0.102.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ClientTlsPolicy.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ClientTlsPolicy.Builder (0.102.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.102.0 (latest)  0.98.0  0.97.0  0.96.0  0.94.0  0.91.0  0.90.0  0.88.0  0.86.0  0.85.0  0.83.0  0.81.0  0.79.0  0.78.0  0.77.0  0.76.0  0.75.0  0.73.0  0.71.0  0.70.0  0.67.0  0.66.0  0.65.0  0.63.0  0.62.0  0.61.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.4  0.5.1  0.4.4 
    
    
    public static final class ClientTlsPolicy.Builder extends GeneratedMessage.Builder<ClientTlsPolicy.Builder> implements ClientTlsPolicyOrBuilder

ClientTlsPolicy is a resource that specifies how a client should authenticate connections to backends of a service. This resource itself does not affect configuration unless it is attached to a backend service resource.

Protobuf type `google.cloud.networksecurity.v1beta1.ClientTlsPolicy`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > ClientTlsPolicy.Builder

## Implements

[ClientTlsPolicyOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ClientTlsPolicyOrBuilder)

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

### addAllServerValidationCa(Iterable<? extends ValidationCA> values)
    
    
    public ClientTlsPolicy.Builder addAllServerValidationCa(Iterable<? extends ValidationCA> values)

Optional. Defines the mechanism to obtain the Certificate Authority certificate to validate the server certificate. If empty, client does not validate the server certificate.

` repeated .google.cloud.networksecurity.v1beta1.ValidationCA server_validation_ca = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<? extends com.google.cloud.networksecurity.v1beta1.ValidationCA>`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClientTlsPolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ClientTlsPolicy.Builder)` |   
  
### addServerValidationCa(ValidationCA value)
    
    
    public ClientTlsPolicy.Builder addServerValidationCa(ValidationCA value)

Optional. Defines the mechanism to obtain the Certificate Authority certificate to validate the server certificate. If empty, client does not validate the server certificate.

` repeated .google.cloud.networksecurity.v1beta1.ValidationCA server_validation_ca = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ValidationCA](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ValidationCA)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClientTlsPolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ClientTlsPolicy.Builder)` |   
  
### addServerValidationCa(ValidationCA.Builder builderForValue)
    
    
    public ClientTlsPolicy.Builder addServerValidationCa(ValidationCA.Builder builderForValue)

Optional. Defines the mechanism to obtain the Certificate Authority certificate to validate the server certificate. If empty, client does not validate the server certificate.

` repeated .google.cloud.networksecurity.v1beta1.ValidationCA server_validation_ca = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[ValidationCA.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ValidationCA.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClientTlsPolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ClientTlsPolicy.Builder)` |   
  
### addServerValidationCa(int index, ValidationCA value)
    
    
    public ClientTlsPolicy.Builder addServerValidationCa(int index, ValidationCA value)

Optional. Defines the mechanism to obtain the Certificate Authority certificate to validate the server certificate. If empty, client does not validate the server certificate.

` repeated .google.cloud.networksecurity.v1beta1.ValidationCA server_validation_ca = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[ValidationCA](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ValidationCA)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClientTlsPolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ClientTlsPolicy.Builder)` |   
  
### addServerValidationCa(int index, ValidationCA.Builder builderForValue)
    
    
    public ClientTlsPolicy.Builder addServerValidationCa(int index, ValidationCA.Builder builderForValue)

Optional. Defines the mechanism to obtain the Certificate Authority certificate to validate the server certificate. If empty, client does not validate the server certificate.

` repeated .google.cloud.networksecurity.v1beta1.ValidationCA server_validation_ca = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[ValidationCA.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ValidationCA.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClientTlsPolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ClientTlsPolicy.Builder)` |   
  
### addServerValidationCaBuilder()
    
    
    public ValidationCA.Builder addServerValidationCaBuilder()

Optional. Defines the mechanism to obtain the Certificate Authority certificate to validate the server certificate. If empty, client does not validate the server certificate.

` repeated .google.cloud.networksecurity.v1beta1.ValidationCA server_validation_ca = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ValidationCA.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ValidationCA.Builder)` |   
  
### addServerValidationCaBuilder(int index)
    
    
    public ValidationCA.Builder addServerValidationCaBuilder(int index)

Optional. Defines the mechanism to obtain the Certificate Authority certificate to validate the server certificate. If empty, client does not validate the server certificate.

` repeated .google.cloud.networksecurity.v1beta1.ValidationCA server_validation_ca = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ValidationCA.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ValidationCA.Builder)` |   
  
### build()
    
    
    public ClientTlsPolicy build()

**Returns**  
---  
**Type** | **Description**  
`[ClientTlsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ClientTlsPolicy)` |   
  
### buildPartial()
    
    
    public ClientTlsPolicy buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[ClientTlsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ClientTlsPolicy)` |   
  
### clear()
    
    
    public ClientTlsPolicy.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[ClientTlsPolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ClientTlsPolicy.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearClientCertificate()
    
    
    public ClientTlsPolicy.Builder clearClientCertificate()

Optional. Defines a mechanism to provision client identity (public and private keys) for peer to peer authentication. The presence of this dictates mTLS.

` .google.cloud.networksecurity.v1beta1.CertificateProvider client_certificate = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ClientTlsPolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ClientTlsPolicy.Builder)` |   
  
### clearCreateTime()
    
    
    public ClientTlsPolicy.Builder clearCreateTime()

Output only. The timestamp when the resource was created.

` .google.protobuf.Timestamp create_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ClientTlsPolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ClientTlsPolicy.Builder)` |   
  
### clearDescription()
    
    
    public ClientTlsPolicy.Builder clearDescription()

Optional. Free-text description of the resource.

`string description = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ClientTlsPolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ClientTlsPolicy.Builder)` | This builder for chaining.  
  
### clearLabels()
    
    
    public ClientTlsPolicy.Builder clearLabels()

**Returns**  
---  
**Type** | **Description**  
`[ClientTlsPolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ClientTlsPolicy.Builder)` |   
  
### clearName()
    
    
    public ClientTlsPolicy.Builder clearName()

Required. Name of the ClientTlsPolicy resource. It matches the pattern `projects/*/locations/{location}/clientTlsPolicies/{client_tls_policy}`

`string name = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ClientTlsPolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ClientTlsPolicy.Builder)` | This builder for chaining.  
  
### clearServerValidationCa()
    
    
    public ClientTlsPolicy.Builder clearServerValidationCa()

Optional. Defines the mechanism to obtain the Certificate Authority certificate to validate the server certificate. If empty, client does not validate the server certificate.

` repeated .google.cloud.networksecurity.v1beta1.ValidationCA server_validation_ca = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ClientTlsPolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ClientTlsPolicy.Builder)` |   
  
### clearSni()
    
    
    public ClientTlsPolicy.Builder clearSni()

Optional. Server Name Indication string to present to the server during TLS handshake. E.g: "secure.example.com".

`string sni = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ClientTlsPolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ClientTlsPolicy.Builder)` | This builder for chaining.  
  
### clearUpdateTime()
    
    
    public ClientTlsPolicy.Builder clearUpdateTime()

Output only. The timestamp when the resource was updated.

` .google.protobuf.Timestamp update_time = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ClientTlsPolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ClientTlsPolicy.Builder)` |   
  
### containsLabels(String key)
    
    
    public boolean containsLabels(String key)

Optional. Set of label tags associated with the resource.

`map<string, string> labels = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getClientCertificate()
    
    
    public CertificateProvider getClientCertificate()

Optional. Defines a mechanism to provision client identity (public and private keys) for peer to peer authentication. The presence of this dictates mTLS.

` .google.cloud.networksecurity.v1beta1.CertificateProvider client_certificate = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[CertificateProvider](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.CertificateProvider)` | The clientCertificate.  
  
### getClientCertificateBuilder()
    
    
    public CertificateProvider.Builder getClientCertificateBuilder()

Optional. Defines a mechanism to provision client identity (public and private keys) for peer to peer authentication. The presence of this dictates mTLS.

` .google.cloud.networksecurity.v1beta1.CertificateProvider client_certificate = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[CertificateProvider.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.CertificateProvider.Builder)` |   
  
### getClientCertificateOrBuilder()
    
    
    public CertificateProviderOrBuilder getClientCertificateOrBuilder()

Optional. Defines a mechanism to provision client identity (public and private keys) for peer to peer authentication. The presence of this dictates mTLS.

` .google.cloud.networksecurity.v1beta1.CertificateProvider client_certificate = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[CertificateProviderOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.CertificateProviderOrBuilder)` |   
  
### getCreateTime()
    
    
    public Timestamp getCreateTime()

Output only. The timestamp when the resource was created.

` .google.protobuf.Timestamp create_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeBuilder()
    
    
    public Timestamp.Builder getCreateTimeBuilder()

Output only. The timestamp when the resource was created.

` .google.protobuf.Timestamp create_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)` |   
  
### getCreateTimeOrBuilder()
    
    
    public TimestampOrBuilder getCreateTimeOrBuilder()

Output only. The timestamp when the resource was created.

` .google.protobuf.Timestamp create_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDefaultInstanceForType()
    
    
    public ClientTlsPolicy getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[ClientTlsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ClientTlsPolicy)` |   
  
### getDescription()
    
    
    public String getDescription()

Optional. Free-text description of the resource.

`string description = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The description.  
  
### getDescriptionBytes()
    
    
    public ByteString getDescriptionBytes()

Optional. Free-text description of the resource.

`string description = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for description.  
  
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

Use [#getLabelsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ClientTlsPolicy.Builder#com_google_cloud_networksecurity_v1beta1_ClientTlsPolicy_Builder_getLabelsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsCount()
    
    
    public int getLabelsCount()

Optional. Set of label tags associated with the resource.

`map<string, string> labels = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getLabelsMap()
    
    
    public Map<String,String> getLabelsMap()

Optional. Set of label tags associated with the resource.

`map<string, string> labels = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsOrDefault(String key, String defaultValue)
    
    
    public String getLabelsOrDefault(String key, String defaultValue)

Optional. Set of label tags associated with the resource.

`map<string, string> labels = 5 [(.google.api.field_behavior) = OPTIONAL];`

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

Optional. Set of label tags associated with the resource.

`map<string, string> labels = 5 [(.google.api.field_behavior) = OPTIONAL];`

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

Required. Name of the ClientTlsPolicy resource. It matches the pattern `projects/*/locations/{location}/clientTlsPolicies/{client_tls_policy}`

`string name = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public ByteString getNameBytes()

Required. Name of the ClientTlsPolicy resource. It matches the pattern `projects/*/locations/{location}/clientTlsPolicies/{client_tls_policy}`

`string name = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getServerValidationCa(int index)
    
    
    public ValidationCA getServerValidationCa(int index)

Optional. Defines the mechanism to obtain the Certificate Authority certificate to validate the server certificate. If empty, client does not validate the server certificate.

` repeated .google.cloud.networksecurity.v1beta1.ValidationCA server_validation_ca = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ValidationCA](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ValidationCA)` |   
  
### getServerValidationCaBuilder(int index)
    
    
    public ValidationCA.Builder getServerValidationCaBuilder(int index)

Optional. Defines the mechanism to obtain the Certificate Authority certificate to validate the server certificate. If empty, client does not validate the server certificate.

` repeated .google.cloud.networksecurity.v1beta1.ValidationCA server_validation_ca = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ValidationCA.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ValidationCA.Builder)` |   
  
### getServerValidationCaBuilderList()
    
    
    public List<ValidationCA.Builder> getServerValidationCaBuilderList()

Optional. Defines the mechanism to obtain the Certificate Authority certificate to validate the server certificate. If empty, client does not validate the server certificate.

` repeated .google.cloud.networksecurity.v1beta1.ValidationCA server_validation_ca = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ValidationCA.Builder)>` |   
  
### getServerValidationCaCount()
    
    
    public int getServerValidationCaCount()

Optional. Defines the mechanism to obtain the Certificate Authority certificate to validate the server certificate. If empty, client does not validate the server certificate.

` repeated .google.cloud.networksecurity.v1beta1.ValidationCA server_validation_ca = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getServerValidationCaList()
    
    
    public List<ValidationCA> getServerValidationCaList()

Optional. Defines the mechanism to obtain the Certificate Authority certificate to validate the server certificate. If empty, client does not validate the server certificate.

` repeated .google.cloud.networksecurity.v1beta1.ValidationCA server_validation_ca = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ValidationCA](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ValidationCA)>` |   
  
### getServerValidationCaOrBuilder(int index)
    
    
    public ValidationCAOrBuilder getServerValidationCaOrBuilder(int index)

Optional. Defines the mechanism to obtain the Certificate Authority certificate to validate the server certificate. If empty, client does not validate the server certificate.

` repeated .google.cloud.networksecurity.v1beta1.ValidationCA server_validation_ca = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ValidationCAOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ValidationCAOrBuilder)` |   
  
### getServerValidationCaOrBuilderList()
    
    
    public List<? extends ValidationCAOrBuilder> getServerValidationCaOrBuilderList()

Optional. Defines the mechanism to obtain the Certificate Authority certificate to validate the server certificate. If empty, client does not validate the server certificate.

` repeated .google.cloud.networksecurity.v1beta1.ValidationCA server_validation_ca = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.networksecurity.v1beta1.ValidationCAOrBuilder>` |   
  
### getSni()
    
    
    public String getSni()

Optional. Server Name Indication string to present to the server during TLS handshake. E.g: "secure.example.com".

`string sni = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The sni.  
  
### getSniBytes()
    
    
    public ByteString getSniBytes()

Optional. Server Name Indication string to present to the server during TLS handshake. E.g: "secure.example.com".

`string sni = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for sni.  
  
### getUpdateTime()
    
    
    public Timestamp getUpdateTime()

Output only. The timestamp when the resource was updated.

` .google.protobuf.Timestamp update_time = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The updateTime.  
  
### getUpdateTimeBuilder()
    
    
    public Timestamp.Builder getUpdateTimeBuilder()

Output only. The timestamp when the resource was updated.

` .google.protobuf.Timestamp update_time = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)` |   
  
### getUpdateTimeOrBuilder()
    
    
    public TimestampOrBuilder getUpdateTimeOrBuilder()

Output only. The timestamp when the resource was updated.

` .google.protobuf.Timestamp update_time = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### hasClientCertificate()
    
    
    public boolean hasClientCertificate()

Optional. Defines a mechanism to provision client identity (public and private keys) for peer to peer authentication. The presence of this dictates mTLS.

` .google.cloud.networksecurity.v1beta1.CertificateProvider client_certificate = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the clientCertificate field is set.  
  
### hasCreateTime()
    
    
    public boolean hasCreateTime()

Output only. The timestamp when the resource was created.

` .google.protobuf.Timestamp create_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasUpdateTime()
    
    
    public boolean hasUpdateTime()

Output only. The timestamp when the resource was updated.

` .google.protobuf.Timestamp update_time = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

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

### mergeClientCertificate(CertificateProvider value)
    
    
    public ClientTlsPolicy.Builder mergeClientCertificate(CertificateProvider value)

Optional. Defines a mechanism to provision client identity (public and private keys) for peer to peer authentication. The presence of this dictates mTLS.

` .google.cloud.networksecurity.v1beta1.CertificateProvider client_certificate = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[CertificateProvider](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.CertificateProvider)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClientTlsPolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ClientTlsPolicy.Builder)` |   
  
### mergeCreateTime(Timestamp value)
    
    
    public ClientTlsPolicy.Builder mergeCreateTime(Timestamp value)

Output only. The timestamp when the resource was created.

` .google.protobuf.Timestamp create_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClientTlsPolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ClientTlsPolicy.Builder)` |   
  
### mergeFrom(ClientTlsPolicy other)
    
    
    public ClientTlsPolicy.Builder mergeFrom(ClientTlsPolicy other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ClientTlsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ClientTlsPolicy)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClientTlsPolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ClientTlsPolicy.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public ClientTlsPolicy.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClientTlsPolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ClientTlsPolicy.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public ClientTlsPolicy.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClientTlsPolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ClientTlsPolicy.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### mergeUpdateTime(Timestamp value)
    
    
    public ClientTlsPolicy.Builder mergeUpdateTime(Timestamp value)

Output only. The timestamp when the resource was updated.

` .google.protobuf.Timestamp update_time = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClientTlsPolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ClientTlsPolicy.Builder)` |   
  
### putAllLabels(Map<String,String> values)
    
    
    public ClientTlsPolicy.Builder putAllLabels(Map<String,String> values)

Optional. Set of label tags associated with the resource.

`map<string, string> labels = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClientTlsPolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ClientTlsPolicy.Builder)` |   
  
### putLabels(String key, String value)
    
    
    public ClientTlsPolicy.Builder putLabels(String key, String value)

Optional. Set of label tags associated with the resource.

`map<string, string> labels = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClientTlsPolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ClientTlsPolicy.Builder)` |   
  
### removeLabels(String key)
    
    
    public ClientTlsPolicy.Builder removeLabels(String key)

Optional. Set of label tags associated with the resource.

`map<string, string> labels = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClientTlsPolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ClientTlsPolicy.Builder)` |   
  
### removeServerValidationCa(int index)
    
    
    public ClientTlsPolicy.Builder removeServerValidationCa(int index)

Optional. Defines the mechanism to obtain the Certificate Authority certificate to validate the server certificate. If empty, client does not validate the server certificate.

` repeated .google.cloud.networksecurity.v1beta1.ValidationCA server_validation_ca = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClientTlsPolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ClientTlsPolicy.Builder)` |   
  
### setClientCertificate(CertificateProvider value)
    
    
    public ClientTlsPolicy.Builder setClientCertificate(CertificateProvider value)

Optional. Defines a mechanism to provision client identity (public and private keys) for peer to peer authentication. The presence of this dictates mTLS.

` .google.cloud.networksecurity.v1beta1.CertificateProvider client_certificate = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[CertificateProvider](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.CertificateProvider)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClientTlsPolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ClientTlsPolicy.Builder)` |   
  
### setClientCertificate(CertificateProvider.Builder builderForValue)
    
    
    public ClientTlsPolicy.Builder setClientCertificate(CertificateProvider.Builder builderForValue)

Optional. Defines a mechanism to provision client identity (public and private keys) for peer to peer authentication. The presence of this dictates mTLS.

` .google.cloud.networksecurity.v1beta1.CertificateProvider client_certificate = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[CertificateProvider.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.CertificateProvider.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClientTlsPolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ClientTlsPolicy.Builder)` |   
  
### setCreateTime(Timestamp value)
    
    
    public ClientTlsPolicy.Builder setCreateTime(Timestamp value)

Output only. The timestamp when the resource was created.

` .google.protobuf.Timestamp create_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClientTlsPolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ClientTlsPolicy.Builder)` |   
  
### setCreateTime(Timestamp.Builder builderForValue)
    
    
    public ClientTlsPolicy.Builder setCreateTime(Timestamp.Builder builderForValue)

Output only. The timestamp when the resource was created.

` .google.protobuf.Timestamp create_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClientTlsPolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ClientTlsPolicy.Builder)` |   
  
### setDescription(String value)
    
    
    public ClientTlsPolicy.Builder setDescription(String value)

Optional. Free-text description of the resource.

`string description = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The description to set.  
**Returns**  
---  
**Type** | **Description**  
`[ClientTlsPolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ClientTlsPolicy.Builder)` | This builder for chaining.  
  
### setDescriptionBytes(ByteString value)
    
    
    public ClientTlsPolicy.Builder setDescriptionBytes(ByteString value)

Optional. Free-text description of the resource.

`string description = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for description to set.  
**Returns**  
---  
**Type** | **Description**  
`[ClientTlsPolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ClientTlsPolicy.Builder)` | This builder for chaining.  
  
### setName(String value)
    
    
    public ClientTlsPolicy.Builder setName(String value)

Required. Name of the ClientTlsPolicy resource. It matches the pattern `projects/*/locations/{location}/clientTlsPolicies/{client_tls_policy}`

`string name = 1 [(.google.api.field_behavior) = REQUIRED];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name to set.  
**Returns**  
---  
**Type** | **Description**  
`[ClientTlsPolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ClientTlsPolicy.Builder)` | This builder for chaining.  
  
### setNameBytes(ByteString value)
    
    
    public ClientTlsPolicy.Builder setNameBytes(ByteString value)

Required. Name of the ClientTlsPolicy resource. It matches the pattern `projects/*/locations/{location}/clientTlsPolicies/{client_tls_policy}`

`string name = 1 [(.google.api.field_behavior) = REQUIRED];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for name to set.  
**Returns**  
---  
**Type** | **Description**  
`[ClientTlsPolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ClientTlsPolicy.Builder)` | This builder for chaining.  
  
### setServerValidationCa(int index, ValidationCA value)
    
    
    public ClientTlsPolicy.Builder setServerValidationCa(int index, ValidationCA value)

Optional. Defines the mechanism to obtain the Certificate Authority certificate to validate the server certificate. If empty, client does not validate the server certificate.

` repeated .google.cloud.networksecurity.v1beta1.ValidationCA server_validation_ca = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[ValidationCA](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ValidationCA)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClientTlsPolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ClientTlsPolicy.Builder)` |   
  
### setServerValidationCa(int index, ValidationCA.Builder builderForValue)
    
    
    public ClientTlsPolicy.Builder setServerValidationCa(int index, ValidationCA.Builder builderForValue)

Optional. Defines the mechanism to obtain the Certificate Authority certificate to validate the server certificate. If empty, client does not validate the server certificate.

` repeated .google.cloud.networksecurity.v1beta1.ValidationCA server_validation_ca = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[ValidationCA.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ValidationCA.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClientTlsPolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ClientTlsPolicy.Builder)` |   
  
### setSni(String value)
    
    
    public ClientTlsPolicy.Builder setSni(String value)

Optional. Server Name Indication string to present to the server during TLS handshake. E.g: "secure.example.com".

`string sni = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The sni to set.  
**Returns**  
---  
**Type** | **Description**  
`[ClientTlsPolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ClientTlsPolicy.Builder)` | This builder for chaining.  
  
### setSniBytes(ByteString value)
    
    
    public ClientTlsPolicy.Builder setSniBytes(ByteString value)

Optional. Server Name Indication string to present to the server during TLS handshake. E.g: "secure.example.com".

`string sni = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for sni to set.  
**Returns**  
---  
**Type** | **Description**  
`[ClientTlsPolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ClientTlsPolicy.Builder)` | This builder for chaining.  
  
### setUpdateTime(Timestamp value)
    
    
    public ClientTlsPolicy.Builder setUpdateTime(Timestamp value)

Output only. The timestamp when the resource was updated.

` .google.protobuf.Timestamp update_time = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClientTlsPolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ClientTlsPolicy.Builder)` |   
  
### setUpdateTime(Timestamp.Builder builderForValue)
    
    
    public ClientTlsPolicy.Builder setUpdateTime(Timestamp.Builder builderForValue)

Output only. The timestamp when the resource was updated.

` .google.protobuf.Timestamp update_time = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClientTlsPolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ClientTlsPolicy.Builder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
