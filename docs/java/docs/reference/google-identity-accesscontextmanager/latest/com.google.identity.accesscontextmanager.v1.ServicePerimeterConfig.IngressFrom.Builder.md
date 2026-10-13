---
url: https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressFrom.Builder
title: Class ServicePerimeterConfig.IngressFrom.Builder (1.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:59:33.641050+00:00
---

# Class ServicePerimeterConfig.IngressFrom.Builder (1.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressFrom.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ServicePerimeterConfig.IngressFrom.Builder (1.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.100.0 (latest)  1.96.0  1.95.0  1.94.0  1.92.0  1.89.0  1.88.0  1.86.0  1.84.0  1.83.0  1.82.0  1.81.0  1.79.0  1.77.0  1.76.0  1.75.0  1.74.0  1.73.0  1.71.0  1.69.0  1.68.0  1.65.0  1.64.0  1.63.0  1.61.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.50.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.5  1.3.1  1.2.10 
    
    
    public static final class ServicePerimeterConfig.IngressFrom.Builder extends GeneratedMessage.Builder<ServicePerimeterConfig.IngressFrom.Builder> implements ServicePerimeterConfig.IngressFromOrBuilder

Defines the conditions under which an [IngressPolicy] [google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressPolicy] matches a request. Conditions are based on information about the source of the request. The request must satisfy what is defined in `sources` AND identity related fields in order to match.

Protobuf type ` google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressFrom`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > ServicePerimeterConfig.IngressFrom.Builder

## Implements

[ServicePerimeterConfig.IngressFromOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressFromOrBuilder)

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

### addAllIdentities(Iterable<String> values)
    
    
    public ServicePerimeterConfig.IngressFrom.Builder addAllIdentities(Iterable<String> values)

A list of identities that are allowed access through this ingress policy. Should be in the format of email address. The email address should represent individual user or service account only.

`repeated string identities = 2;`

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
The identities to add.  
**Returns**  
---  
**Type** | **Description**  
`[ServicePerimeterConfig.IngressFrom.Builder](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressFrom.Builder)` | This builder for chaining.  
  
### addAllSources(Iterable<? extends ServicePerimeterConfig.IngressSource> values)
    
    
    public ServicePerimeterConfig.IngressFrom.Builder addAllSources(Iterable<? extends ServicePerimeterConfig.IngressSource> values)

Sources that this [IngressPolicy] [google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressPolicy] authorizes access from.

` repeated .google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressSource sources = 1; `

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<? extends com.google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressSource>`  
  
**Returns**  
---  
**Type** | **Description**  
`[ServicePerimeterConfig.IngressFrom.Builder](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressFrom.Builder)` |   
  
### addIdentities(String value)
    
    
    public ServicePerimeterConfig.IngressFrom.Builder addIdentities(String value)

A list of identities that are allowed access through this ingress policy. Should be in the format of email address. The email address should represent individual user or service account only.

`repeated string identities = 2;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The identities to add.  
**Returns**  
---  
**Type** | **Description**  
`[ServicePerimeterConfig.IngressFrom.Builder](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressFrom.Builder)` | This builder for chaining.  
  
### addIdentitiesBytes(ByteString value)
    
    
    public ServicePerimeterConfig.IngressFrom.Builder addIdentitiesBytes(ByteString value)

A list of identities that are allowed access through this ingress policy. Should be in the format of email address. The email address should represent individual user or service account only.

`repeated string identities = 2;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes of the identities to add.  
**Returns**  
---  
**Type** | **Description**  
`[ServicePerimeterConfig.IngressFrom.Builder](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressFrom.Builder)` | This builder for chaining.  
  
### addSources(ServicePerimeterConfig.IngressSource value)
    
    
    public ServicePerimeterConfig.IngressFrom.Builder addSources(ServicePerimeterConfig.IngressSource value)

Sources that this [IngressPolicy] [google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressPolicy] authorizes access from.

` repeated .google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressSource sources = 1; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ServicePerimeterConfig.IngressSource](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressSource)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ServicePerimeterConfig.IngressFrom.Builder](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressFrom.Builder)` |   
  
### addSources(ServicePerimeterConfig.IngressSource.Builder builderForValue)
    
    
    public ServicePerimeterConfig.IngressFrom.Builder addSources(ServicePerimeterConfig.IngressSource.Builder builderForValue)

Sources that this [IngressPolicy] [google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressPolicy] authorizes access from.

` repeated .google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressSource sources = 1; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[ServicePerimeterConfig.IngressSource.Builder](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressSource.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ServicePerimeterConfig.IngressFrom.Builder](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressFrom.Builder)` |   
  
### addSources(int index, ServicePerimeterConfig.IngressSource value)
    
    
    public ServicePerimeterConfig.IngressFrom.Builder addSources(int index, ServicePerimeterConfig.IngressSource value)

Sources that this [IngressPolicy] [google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressPolicy] authorizes access from.

` repeated .google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressSource sources = 1; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[ServicePerimeterConfig.IngressSource](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressSource)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ServicePerimeterConfig.IngressFrom.Builder](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressFrom.Builder)` |   
  
### addSources(int index, ServicePerimeterConfig.IngressSource.Builder builderForValue)
    
    
    public ServicePerimeterConfig.IngressFrom.Builder addSources(int index, ServicePerimeterConfig.IngressSource.Builder builderForValue)

Sources that this [IngressPolicy] [google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressPolicy] authorizes access from.

` repeated .google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressSource sources = 1; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[ServicePerimeterConfig.IngressSource.Builder](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressSource.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ServicePerimeterConfig.IngressFrom.Builder](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressFrom.Builder)` |   
  
### addSourcesBuilder()
    
    
    public ServicePerimeterConfig.IngressSource.Builder addSourcesBuilder()

Sources that this [IngressPolicy] [google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressPolicy] authorizes access from.

` repeated .google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressSource sources = 1; `

**Returns**  
---  
**Type** | **Description**  
`[ServicePerimeterConfig.IngressSource.Builder](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressSource.Builder)` |   
  
### addSourcesBuilder(int index)
    
    
    public ServicePerimeterConfig.IngressSource.Builder addSourcesBuilder(int index)

Sources that this [IngressPolicy] [google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressPolicy] authorizes access from.

` repeated .google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressSource sources = 1; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ServicePerimeterConfig.IngressSource.Builder](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressSource.Builder)` |   
  
### build()
    
    
    public ServicePerimeterConfig.IngressFrom build()

**Returns**  
---  
**Type** | **Description**  
`[ServicePerimeterConfig.IngressFrom](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressFrom)` |   
  
### buildPartial()
    
    
    public ServicePerimeterConfig.IngressFrom buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[ServicePerimeterConfig.IngressFrom](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressFrom)` |   
  
### clear()
    
    
    public ServicePerimeterConfig.IngressFrom.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[ServicePerimeterConfig.IngressFrom.Builder](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressFrom.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearIdentities()
    
    
    public ServicePerimeterConfig.IngressFrom.Builder clearIdentities()

A list of identities that are allowed access through this ingress policy. Should be in the format of email address. The email address should represent individual user or service account only.

`repeated string identities = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ServicePerimeterConfig.IngressFrom.Builder](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressFrom.Builder)` | This builder for chaining.  
  
### clearIdentityType()
    
    
    public ServicePerimeterConfig.IngressFrom.Builder clearIdentityType()

Specifies the type of identities that are allowed access from outside the perimeter. If left unspecified, then members of `identities` field will be allowed access.

` .google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IdentityType identity_type = 3; `

**Returns**  
---  
**Type** | **Description**  
`[ServicePerimeterConfig.IngressFrom.Builder](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressFrom.Builder)` | This builder for chaining.  
  
### clearSources()
    
    
    public ServicePerimeterConfig.IngressFrom.Builder clearSources()

Sources that this [IngressPolicy] [google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressPolicy] authorizes access from.

` repeated .google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressSource sources = 1; `

**Returns**  
---  
**Type** | **Description**  
`[ServicePerimeterConfig.IngressFrom.Builder](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressFrom.Builder)` |   
  
### getDefaultInstanceForType()
    
    
    public ServicePerimeterConfig.IngressFrom getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[ServicePerimeterConfig.IngressFrom](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressFrom)` |   
  
### getDescriptorForType()
    
    
    public Descriptors.Descriptor getDescriptorForType()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getDescriptorForType__)

### getIdentities(int index)
    
    
    public String getIdentities(int index)

A list of identities that are allowed access through this ingress policy. Should be in the format of email address. The email address should represent individual user or service account only.

`repeated string identities = 2;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The identities at the given index.  
  
### getIdentitiesBytes(int index)
    
    
    public ByteString getIdentitiesBytes(int index)

A list of identities that are allowed access through this ingress policy. Should be in the format of email address. The email address should represent individual user or service account only.

`repeated string identities = 2;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the identities at the given index.  
  
### getIdentitiesCount()
    
    
    public int getIdentitiesCount()

A list of identities that are allowed access through this ingress policy. Should be in the format of email address. The email address should represent individual user or service account only.

`repeated string identities = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of identities.  
  
### getIdentitiesList()
    
    
    public ProtocolStringList getIdentitiesList()

A list of identities that are allowed access through this ingress policy. Should be in the format of email address. The email address should represent individual user or service account only.

`repeated string identities = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ProtocolStringList](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ProtocolStringList.html)` | A list containing the identities.  
  
### getIdentityType()
    
    
    public ServicePerimeterConfig.IdentityType getIdentityType()

Specifies the type of identities that are allowed access from outside the perimeter. If left unspecified, then members of `identities` field will be allowed access.

` .google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IdentityType identity_type = 3; `

**Returns**  
---  
**Type** | **Description**  
`[ServicePerimeterConfig.IdentityType](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IdentityType)` | The identityType.  
  
### getIdentityTypeValue()
    
    
    public int getIdentityTypeValue()

Specifies the type of identities that are allowed access from outside the perimeter. If left unspecified, then members of `identities` field will be allowed access.

` .google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IdentityType identity_type = 3; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for identityType.  
  
### getSources(int index)
    
    
    public ServicePerimeterConfig.IngressSource getSources(int index)

Sources that this [IngressPolicy] [google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressPolicy] authorizes access from.

` repeated .google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressSource sources = 1; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ServicePerimeterConfig.IngressSource](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressSource)` |   
  
### getSourcesBuilder(int index)
    
    
    public ServicePerimeterConfig.IngressSource.Builder getSourcesBuilder(int index)

Sources that this [IngressPolicy] [google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressPolicy] authorizes access from.

` repeated .google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressSource sources = 1; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ServicePerimeterConfig.IngressSource.Builder](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressSource.Builder)` |   
  
### getSourcesBuilderList()
    
    
    public List<ServicePerimeterConfig.IngressSource.Builder> getSourcesBuilderList()

Sources that this [IngressPolicy] [google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressPolicy] authorizes access from.

` repeated .google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressSource sources = 1; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Builder](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressSource.Builder)>` |   
  
### getSourcesCount()
    
    
    public int getSourcesCount()

Sources that this [IngressPolicy] [google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressPolicy] authorizes access from.

` repeated .google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressSource sources = 1; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getSourcesList()
    
    
    public List<ServicePerimeterConfig.IngressSource> getSourcesList()

Sources that this [IngressPolicy] [google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressPolicy] authorizes access from.

` repeated .google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressSource sources = 1; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[IngressSource](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressSource)>` |   
  
### getSourcesOrBuilder(int index)
    
    
    public ServicePerimeterConfig.IngressSourceOrBuilder getSourcesOrBuilder(int index)

Sources that this [IngressPolicy] [google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressPolicy] authorizes access from.

` repeated .google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressSource sources = 1; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ServicePerimeterConfig.IngressSourceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressSourceOrBuilder)` |   
  
### getSourcesOrBuilderList()
    
    
    public List<? extends ServicePerimeterConfig.IngressSourceOrBuilder> getSourcesOrBuilderList()

Sources that this [IngressPolicy] [google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressPolicy] authorizes access from.

` repeated .google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressSource sources = 1; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressSourceOrBuilder>` |   
  
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

### mergeFrom(ServicePerimeterConfig.IngressFrom other)
    
    
    public ServicePerimeterConfig.IngressFrom.Builder mergeFrom(ServicePerimeterConfig.IngressFrom other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ServicePerimeterConfig.IngressFrom](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressFrom)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ServicePerimeterConfig.IngressFrom.Builder](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressFrom.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public ServicePerimeterConfig.IngressFrom.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ServicePerimeterConfig.IngressFrom.Builder](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressFrom.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public ServicePerimeterConfig.IngressFrom.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ServicePerimeterConfig.IngressFrom.Builder](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressFrom.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### removeSources(int index)
    
    
    public ServicePerimeterConfig.IngressFrom.Builder removeSources(int index)

Sources that this [IngressPolicy] [google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressPolicy] authorizes access from.

` repeated .google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressSource sources = 1; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ServicePerimeterConfig.IngressFrom.Builder](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressFrom.Builder)` |   
  
### setIdentities(int index, String value)
    
    
    public ServicePerimeterConfig.IngressFrom.Builder setIdentities(int index, String value)

A list of identities that are allowed access through this ingress policy. Should be in the format of email address. The email address should represent individual user or service account only.

`repeated string identities = 2;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index to set the value at.  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The identities to set.  
**Returns**  
---  
**Type** | **Description**  
`[ServicePerimeterConfig.IngressFrom.Builder](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressFrom.Builder)` | This builder for chaining.  
  
### setIdentityType(ServicePerimeterConfig.IdentityType value)
    
    
    public ServicePerimeterConfig.IngressFrom.Builder setIdentityType(ServicePerimeterConfig.IdentityType value)

Specifies the type of identities that are allowed access from outside the perimeter. If left unspecified, then members of `identities` field will be allowed access.

` .google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IdentityType identity_type = 3; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ServicePerimeterConfig.IdentityType](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IdentityType)`  
The identityType to set.  
**Returns**  
---  
**Type** | **Description**  
`[ServicePerimeterConfig.IngressFrom.Builder](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressFrom.Builder)` | This builder for chaining.  
  
### setIdentityTypeValue(int value)
    
    
    public ServicePerimeterConfig.IngressFrom.Builder setIdentityTypeValue(int value)

Specifies the type of identities that are allowed access from outside the perimeter. If left unspecified, then members of `identities` field will be allowed access.

` .google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IdentityType identity_type = 3; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The enum numeric value on the wire for identityType to set.  
**Returns**  
---  
**Type** | **Description**  
`[ServicePerimeterConfig.IngressFrom.Builder](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressFrom.Builder)` | This builder for chaining.  
  
### setSources(int index, ServicePerimeterConfig.IngressSource value)
    
    
    public ServicePerimeterConfig.IngressFrom.Builder setSources(int index, ServicePerimeterConfig.IngressSource value)

Sources that this [IngressPolicy] [google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressPolicy] authorizes access from.

` repeated .google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressSource sources = 1; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[ServicePerimeterConfig.IngressSource](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressSource)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ServicePerimeterConfig.IngressFrom.Builder](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressFrom.Builder)` |   
  
### setSources(int index, ServicePerimeterConfig.IngressSource.Builder builderForValue)
    
    
    public ServicePerimeterConfig.IngressFrom.Builder setSources(int index, ServicePerimeterConfig.IngressSource.Builder builderForValue)

Sources that this [IngressPolicy] [google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressPolicy] authorizes access from.

` repeated .google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressSource sources = 1; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[ServicePerimeterConfig.IngressSource.Builder](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressSource.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ServicePerimeterConfig.IngressFrom.Builder](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressFrom.Builder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
