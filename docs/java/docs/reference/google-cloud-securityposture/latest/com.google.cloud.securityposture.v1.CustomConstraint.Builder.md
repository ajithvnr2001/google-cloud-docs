---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.CustomConstraint.Builder
title: Class CustomConstraint.Builder (0.64.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:49:12.599910+00:00
---

# Class CustomConstraint.Builder (0.64.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.CustomConstraint.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class CustomConstraint.Builder (0.64.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.64.0 (latest)  0.60.0  0.59.0  0.58.0  0.56.0  0.53.0  0.52.0  0.50.0  0.48.0  0.47.0  0.45.0  0.43.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.35.0  0.33.0  0.32.0  0.29.0  0.28.0  0.27.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.2.0  0.1.0 
    
    
    public static final class CustomConstraint.Builder extends GeneratedMessage.Builder<CustomConstraint.Builder> implements CustomConstraintOrBuilder

A custom constraint defined by customers which can _only_ be applied to the given resource types and organization.

By creating a custom constraint, customers can apply policies of this custom constraint. _Creating a custom constraint itself does NOT apply any policy enforcement_.

Protobuf type `google.cloud.securityposture.v1.CustomConstraint`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > CustomConstraint.Builder

## Implements

[CustomConstraintOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.CustomConstraintOrBuilder)

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

### addAllMethodTypes(Iterable<? extends CustomConstraint.MethodType> values)
    
    
    public CustomConstraint.Builder addAllMethodTypes(Iterable<? extends CustomConstraint.MethodType> values)

All the operations being applied for this constraint.

`repeated .google.cloud.securityposture.v1.CustomConstraint.MethodType method_types = 3; `

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<? extends com.google.cloud.securityposture.v1.CustomConstraint.MethodType>`  
The methodTypes to add.  
**Returns**  
---  
**Type** | **Description**  
`[CustomConstraint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.CustomConstraint.Builder)` | This builder for chaining.  
  
### addAllMethodTypesValue(Iterable<Integer> values)
    
    
    public CustomConstraint.Builder addAllMethodTypesValue(Iterable<Integer> values)

All the operations being applied for this constraint.

`repeated .google.cloud.securityposture.v1.CustomConstraint.MethodType method_types = 3; `

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)>`  
The enum numeric values on the wire for methodTypes to add.  
**Returns**  
---  
**Type** | **Description**  
`[CustomConstraint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.CustomConstraint.Builder)` | This builder for chaining.  
  
### addAllResourceTypes(Iterable<String> values)
    
    
    public CustomConstraint.Builder addAllResourceTypes(Iterable<String> values)

Immutable. The resource instance type on which this policy applies. Format will be of the form : `<canonical service name>/<type>` Example:

  * `compute.googleapis.com/Instance`.



`repeated string resource_types = 2 [(.google.api.field_behavior) = IMMUTABLE];`

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
The resourceTypes to add.  
**Returns**  
---  
**Type** | **Description**  
`[CustomConstraint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.CustomConstraint.Builder)` | This builder for chaining.  
  
### addMethodTypes(CustomConstraint.MethodType value)
    
    
    public CustomConstraint.Builder addMethodTypes(CustomConstraint.MethodType value)

All the operations being applied for this constraint.

`repeated .google.cloud.securityposture.v1.CustomConstraint.MethodType method_types = 3; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[CustomConstraint.MethodType](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.CustomConstraint.MethodType)`  
The methodTypes to add.  
**Returns**  
---  
**Type** | **Description**  
`[CustomConstraint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.CustomConstraint.Builder)` | This builder for chaining.  
  
### addMethodTypesValue(int value)
    
    
    public CustomConstraint.Builder addMethodTypesValue(int value)

All the operations being applied for this constraint.

`repeated .google.cloud.securityposture.v1.CustomConstraint.MethodType method_types = 3; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The enum numeric value on the wire for methodTypes to add.  
**Returns**  
---  
**Type** | **Description**  
`[CustomConstraint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.CustomConstraint.Builder)` | This builder for chaining.  
  
### addResourceTypes(String value)
    
    
    public CustomConstraint.Builder addResourceTypes(String value)

Immutable. The resource instance type on which this policy applies. Format will be of the form : `<canonical service name>/<type>` Example:

  * `compute.googleapis.com/Instance`.



`repeated string resource_types = 2 [(.google.api.field_behavior) = IMMUTABLE];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The resourceTypes to add.  
**Returns**  
---  
**Type** | **Description**  
`[CustomConstraint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.CustomConstraint.Builder)` | This builder for chaining.  
  
### addResourceTypesBytes(ByteString value)
    
    
    public CustomConstraint.Builder addResourceTypesBytes(ByteString value)

Immutable. The resource instance type on which this policy applies. Format will be of the form : `<canonical service name>/<type>` Example:

  * `compute.googleapis.com/Instance`.



`repeated string resource_types = 2 [(.google.api.field_behavior) = IMMUTABLE];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes of the resourceTypes to add.  
**Returns**  
---  
**Type** | **Description**  
`[CustomConstraint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.CustomConstraint.Builder)` | This builder for chaining.  
  
### build()
    
    
    public CustomConstraint build()

**Returns**  
---  
**Type** | **Description**  
`[CustomConstraint](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.CustomConstraint)` |   
  
### buildPartial()
    
    
    public CustomConstraint buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[CustomConstraint](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.CustomConstraint)` |   
  
### clear()
    
    
    public CustomConstraint.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[CustomConstraint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.CustomConstraint.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearActionType()
    
    
    public CustomConstraint.Builder clearActionType()

Allow or deny type.

`.google.cloud.securityposture.v1.CustomConstraint.ActionType action_type = 5;`

**Returns**  
---  
**Type** | **Description**  
`[CustomConstraint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.CustomConstraint.Builder)` | This builder for chaining.  
  
### clearCondition()
    
    
    public CustomConstraint.Builder clearCondition()

Org policy condition/expression. For example: `resource.instanceName.matches("[production|test]_.*_(\d)+")` or, `resource.management.auto_upgrade == true`

The max length of the condition is 1000 characters.

`string condition = 4;`

**Returns**  
---  
**Type** | **Description**  
`[CustomConstraint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.CustomConstraint.Builder)` | This builder for chaining.  
  
### clearDescription()
    
    
    public CustomConstraint.Builder clearDescription()

Detailed information about this custom policy constraint. The max length of the description is 2000 characters.

`string description = 7;`

**Returns**  
---  
**Type** | **Description**  
`[CustomConstraint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.CustomConstraint.Builder)` | This builder for chaining.  
  
### clearDisplayName()
    
    
    public CustomConstraint.Builder clearDisplayName()

One line display name for the UI. The max length of the display_name is 200 characters.

`string display_name = 6;`

**Returns**  
---  
**Type** | **Description**  
`[CustomConstraint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.CustomConstraint.Builder)` | This builder for chaining.  
  
### clearMethodTypes()
    
    
    public CustomConstraint.Builder clearMethodTypes()

All the operations being applied for this constraint.

`repeated .google.cloud.securityposture.v1.CustomConstraint.MethodType method_types = 3; `

**Returns**  
---  
**Type** | **Description**  
`[CustomConstraint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.CustomConstraint.Builder)` | This builder for chaining.  
  
### clearName()
    
    
    public CustomConstraint.Builder clearName()

Immutable. Name of the constraint. This is unique within the organization. Format of the name should be

\- `organizations/{organization_id}/customConstraints/{custom_constraint_id}`

Example: `organizations/123/customConstraints/custom.createOnlyE2TypeVms`

The max length is 70 characters and the minimum length is 1. Note that the prefix `organizations/{organization_id}/customConstraints/` is not counted.

`string name = 1 [(.google.api.field_behavior) = IMMUTABLE];`

**Returns**  
---  
**Type** | **Description**  
`[CustomConstraint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.CustomConstraint.Builder)` | This builder for chaining.  
  
### clearResourceTypes()
    
    
    public CustomConstraint.Builder clearResourceTypes()

Immutable. The resource instance type on which this policy applies. Format will be of the form : `<canonical service name>/<type>` Example:

  * `compute.googleapis.com/Instance`.



`repeated string resource_types = 2 [(.google.api.field_behavior) = IMMUTABLE];`

**Returns**  
---  
**Type** | **Description**  
`[CustomConstraint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.CustomConstraint.Builder)` | This builder for chaining.  
  
### clearUpdateTime()
    
    
    public CustomConstraint.Builder clearUpdateTime()

Output only. The last time this custom constraint was updated. This represents the last time that the `CreateCustomConstraint` or `UpdateCustomConstraint` RPC was called

` .google.protobuf.Timestamp update_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[CustomConstraint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.CustomConstraint.Builder)` |   
  
### getActionType()
    
    
    public CustomConstraint.ActionType getActionType()

Allow or deny type.

`.google.cloud.securityposture.v1.CustomConstraint.ActionType action_type = 5;`

**Returns**  
---  
**Type** | **Description**  
`[CustomConstraint.ActionType](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.CustomConstraint.ActionType)` | The actionType.  
  
### getActionTypeValue()
    
    
    public int getActionTypeValue()

Allow or deny type.

`.google.cloud.securityposture.v1.CustomConstraint.ActionType action_type = 5;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for actionType.  
  
### getCondition()
    
    
    public String getCondition()

Org policy condition/expression. For example: `resource.instanceName.matches("[production|test]_.*_(\d)+")` or, `resource.management.auto_upgrade == true`

The max length of the condition is 1000 characters.

`string condition = 4;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The condition.  
  
### getConditionBytes()
    
    
    public ByteString getConditionBytes()

Org policy condition/expression. For example: `resource.instanceName.matches("[production|test]_.*_(\d)+")` or, `resource.management.auto_upgrade == true`

The max length of the condition is 1000 characters.

`string condition = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for condition.  
  
### getDefaultInstanceForType()
    
    
    public CustomConstraint getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[CustomConstraint](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.CustomConstraint)` |   
  
### getDescription()
    
    
    public String getDescription()

Detailed information about this custom policy constraint. The max length of the description is 2000 characters.

`string description = 7;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The description.  
  
### getDescriptionBytes()
    
    
    public ByteString getDescriptionBytes()

Detailed information about this custom policy constraint. The max length of the description is 2000 characters.

`string description = 7;`

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

### getDisplayName()
    
    
    public String getDisplayName()

One line display name for the UI. The max length of the display_name is 200 characters.

`string display_name = 6;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The displayName.  
  
### getDisplayNameBytes()
    
    
    public ByteString getDisplayNameBytes()

One line display name for the UI. The max length of the display_name is 200 characters.

`string display_name = 6;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for displayName.  
  
### getMethodTypes(int index)
    
    
    public CustomConstraint.MethodType getMethodTypes(int index)

All the operations being applied for this constraint.

`repeated .google.cloud.securityposture.v1.CustomConstraint.MethodType method_types = 3; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[CustomConstraint.MethodType](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.CustomConstraint.MethodType)` | The methodTypes at the given index.  
  
### getMethodTypesCount()
    
    
    public int getMethodTypesCount()

All the operations being applied for this constraint.

`repeated .google.cloud.securityposture.v1.CustomConstraint.MethodType method_types = 3; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of methodTypes.  
  
### getMethodTypesList()
    
    
    public List<CustomConstraint.MethodType> getMethodTypesList()

All the operations being applied for this constraint.

`repeated .google.cloud.securityposture.v1.CustomConstraint.MethodType method_types = 3; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[MethodType](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.CustomConstraint.MethodType)>` | A list containing the methodTypes.  
  
### getMethodTypesValue(int index)
    
    
    public int getMethodTypesValue(int index)

All the operations being applied for this constraint.

`repeated .google.cloud.securityposture.v1.CustomConstraint.MethodType method_types = 3; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire of methodTypes at the given index.  
  
### getMethodTypesValueList()
    
    
    public List<Integer> getMethodTypesValueList()

All the operations being applied for this constraint.

`repeated .google.cloud.securityposture.v1.CustomConstraint.MethodType method_types = 3; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)>` | A list containing the enum numeric values on the wire for methodTypes.  
  
### getName()
    
    
    public String getName()

Immutable. Name of the constraint. This is unique within the organization. Format of the name should be

\- `organizations/{organization_id}/customConstraints/{custom_constraint_id}`

Example: `organizations/123/customConstraints/custom.createOnlyE2TypeVms`

The max length is 70 characters and the minimum length is 1. Note that the prefix `organizations/{organization_id}/customConstraints/` is not counted.

`string name = 1 [(.google.api.field_behavior) = IMMUTABLE];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public ByteString getNameBytes()

Immutable. Name of the constraint. This is unique within the organization. Format of the name should be

\- `organizations/{organization_id}/customConstraints/{custom_constraint_id}`

Example: `organizations/123/customConstraints/custom.createOnlyE2TypeVms`

The max length is 70 characters and the minimum length is 1. Note that the prefix `organizations/{organization_id}/customConstraints/` is not counted.

`string name = 1 [(.google.api.field_behavior) = IMMUTABLE];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getResourceTypes(int index)
    
    
    public String getResourceTypes(int index)

Immutable. The resource instance type on which this policy applies. Format will be of the form : `<canonical service name>/<type>` Example:

  * `compute.googleapis.com/Instance`.



`repeated string resource_types = 2 [(.google.api.field_behavior) = IMMUTABLE];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The resourceTypes at the given index.  
  
### getResourceTypesBytes(int index)
    
    
    public ByteString getResourceTypesBytes(int index)

Immutable. The resource instance type on which this policy applies. Format will be of the form : `<canonical service name>/<type>` Example:

  * `compute.googleapis.com/Instance`.



`repeated string resource_types = 2 [(.google.api.field_behavior) = IMMUTABLE];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the resourceTypes at the given index.  
  
### getResourceTypesCount()
    
    
    public int getResourceTypesCount()

Immutable. The resource instance type on which this policy applies. Format will be of the form : `<canonical service name>/<type>` Example:

  * `compute.googleapis.com/Instance`.



`repeated string resource_types = 2 [(.google.api.field_behavior) = IMMUTABLE];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of resourceTypes.  
  
### getResourceTypesList()
    
    
    public ProtocolStringList getResourceTypesList()

Immutable. The resource instance type on which this policy applies. Format will be of the form : `<canonical service name>/<type>` Example:

  * `compute.googleapis.com/Instance`.



`repeated string resource_types = 2 [(.google.api.field_behavior) = IMMUTABLE];`

**Returns**  
---  
**Type** | **Description**  
`[ProtocolStringList](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ProtocolStringList.html)` | A list containing the resourceTypes.  
  
### getUpdateTime()
    
    
    public Timestamp getUpdateTime()

Output only. The last time this custom constraint was updated. This represents the last time that the `CreateCustomConstraint` or `UpdateCustomConstraint` RPC was called

` .google.protobuf.Timestamp update_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The updateTime.  
  
### getUpdateTimeBuilder()
    
    
    public Timestamp.Builder getUpdateTimeBuilder()

Output only. The last time this custom constraint was updated. This represents the last time that the `CreateCustomConstraint` or `UpdateCustomConstraint` RPC was called

` .google.protobuf.Timestamp update_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)` |   
  
### getUpdateTimeOrBuilder()
    
    
    public TimestampOrBuilder getUpdateTimeOrBuilder()

Output only. The last time this custom constraint was updated. This represents the last time that the `CreateCustomConstraint` or `UpdateCustomConstraint` RPC was called

` .google.protobuf.Timestamp update_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### hasUpdateTime()
    
    
    public boolean hasUpdateTime()

Output only. The last time this custom constraint was updated. This represents the last time that the `CreateCustomConstraint` or `UpdateCustomConstraint` RPC was called

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

### isInitialized()
    
    
    public final boolean isInitialized()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.isInitialized()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_isInitialized__)

### mergeFrom(CustomConstraint other)
    
    
    public CustomConstraint.Builder mergeFrom(CustomConstraint other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CustomConstraint](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.CustomConstraint)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CustomConstraint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.CustomConstraint.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public CustomConstraint.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CustomConstraint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.CustomConstraint.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public CustomConstraint.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CustomConstraint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.CustomConstraint.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### mergeUpdateTime(Timestamp value)
    
    
    public CustomConstraint.Builder mergeUpdateTime(Timestamp value)

Output only. The last time this custom constraint was updated. This represents the last time that the `CreateCustomConstraint` or `UpdateCustomConstraint` RPC was called

` .google.protobuf.Timestamp update_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CustomConstraint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.CustomConstraint.Builder)` |   
  
### setActionType(CustomConstraint.ActionType value)
    
    
    public CustomConstraint.Builder setActionType(CustomConstraint.ActionType value)

Allow or deny type.

`.google.cloud.securityposture.v1.CustomConstraint.ActionType action_type = 5;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[CustomConstraint.ActionType](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.CustomConstraint.ActionType)`  
The actionType to set.  
**Returns**  
---  
**Type** | **Description**  
`[CustomConstraint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.CustomConstraint.Builder)` | This builder for chaining.  
  
### setActionTypeValue(int value)
    
    
    public CustomConstraint.Builder setActionTypeValue(int value)

Allow or deny type.

`.google.cloud.securityposture.v1.CustomConstraint.ActionType action_type = 5;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The enum numeric value on the wire for actionType to set.  
**Returns**  
---  
**Type** | **Description**  
`[CustomConstraint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.CustomConstraint.Builder)` | This builder for chaining.  
  
### setCondition(String value)
    
    
    public CustomConstraint.Builder setCondition(String value)

Org policy condition/expression. For example: `resource.instanceName.matches("[production|test]_.*_(\d)+")` or, `resource.management.auto_upgrade == true`

The max length of the condition is 1000 characters.

`string condition = 4;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The condition to set.  
**Returns**  
---  
**Type** | **Description**  
`[CustomConstraint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.CustomConstraint.Builder)` | This builder for chaining.  
  
### setConditionBytes(ByteString value)
    
    
    public CustomConstraint.Builder setConditionBytes(ByteString value)

Org policy condition/expression. For example: `resource.instanceName.matches("[production|test]_.*_(\d)+")` or, `resource.management.auto_upgrade == true`

The max length of the condition is 1000 characters.

`string condition = 4;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for condition to set.  
**Returns**  
---  
**Type** | **Description**  
`[CustomConstraint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.CustomConstraint.Builder)` | This builder for chaining.  
  
### setDescription(String value)
    
    
    public CustomConstraint.Builder setDescription(String value)

Detailed information about this custom policy constraint. The max length of the description is 2000 characters.

`string description = 7;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The description to set.  
**Returns**  
---  
**Type** | **Description**  
`[CustomConstraint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.CustomConstraint.Builder)` | This builder for chaining.  
  
### setDescriptionBytes(ByteString value)
    
    
    public CustomConstraint.Builder setDescriptionBytes(ByteString value)

Detailed information about this custom policy constraint. The max length of the description is 2000 characters.

`string description = 7;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for description to set.  
**Returns**  
---  
**Type** | **Description**  
`[CustomConstraint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.CustomConstraint.Builder)` | This builder for chaining.  
  
### setDisplayName(String value)
    
    
    public CustomConstraint.Builder setDisplayName(String value)

One line display name for the UI. The max length of the display_name is 200 characters.

`string display_name = 6;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The displayName to set.  
**Returns**  
---  
**Type** | **Description**  
`[CustomConstraint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.CustomConstraint.Builder)` | This builder for chaining.  
  
### setDisplayNameBytes(ByteString value)
    
    
    public CustomConstraint.Builder setDisplayNameBytes(ByteString value)

One line display name for the UI. The max length of the display_name is 200 characters.

`string display_name = 6;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for displayName to set.  
**Returns**  
---  
**Type** | **Description**  
`[CustomConstraint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.CustomConstraint.Builder)` | This builder for chaining.  
  
### setMethodTypes(int index, CustomConstraint.MethodType value)
    
    
    public CustomConstraint.Builder setMethodTypes(int index, CustomConstraint.MethodType value)

All the operations being applied for this constraint.

`repeated .google.cloud.securityposture.v1.CustomConstraint.MethodType method_types = 3; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index to set the value at.  
`value` | `[CustomConstraint.MethodType](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.CustomConstraint.MethodType)`  
The methodTypes to set.  
**Returns**  
---  
**Type** | **Description**  
`[CustomConstraint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.CustomConstraint.Builder)` | This builder for chaining.  
  
### setMethodTypesValue(int index, int value)
    
    
    public CustomConstraint.Builder setMethodTypesValue(int index, int value)

All the operations being applied for this constraint.

`repeated .google.cloud.securityposture.v1.CustomConstraint.MethodType method_types = 3; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index to set the value at.  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The enum numeric value on the wire for methodTypes to set.  
**Returns**  
---  
**Type** | **Description**  
`[CustomConstraint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.CustomConstraint.Builder)` | This builder for chaining.  
  
### setName(String value)
    
    
    public CustomConstraint.Builder setName(String value)

Immutable. Name of the constraint. This is unique within the organization. Format of the name should be

\- `organizations/{organization_id}/customConstraints/{custom_constraint_id}`

Example: `organizations/123/customConstraints/custom.createOnlyE2TypeVms`

The max length is 70 characters and the minimum length is 1. Note that the prefix `organizations/{organization_id}/customConstraints/` is not counted.

`string name = 1 [(.google.api.field_behavior) = IMMUTABLE];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name to set.  
**Returns**  
---  
**Type** | **Description**  
`[CustomConstraint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.CustomConstraint.Builder)` | This builder for chaining.  
  
### setNameBytes(ByteString value)
    
    
    public CustomConstraint.Builder setNameBytes(ByteString value)

Immutable. Name of the constraint. This is unique within the organization. Format of the name should be

\- `organizations/{organization_id}/customConstraints/{custom_constraint_id}`

Example: `organizations/123/customConstraints/custom.createOnlyE2TypeVms`

The max length is 70 characters and the minimum length is 1. Note that the prefix `organizations/{organization_id}/customConstraints/` is not counted.

`string name = 1 [(.google.api.field_behavior) = IMMUTABLE];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for name to set.  
**Returns**  
---  
**Type** | **Description**  
`[CustomConstraint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.CustomConstraint.Builder)` | This builder for chaining.  
  
### setResourceTypes(int index, String value)
    
    
    public CustomConstraint.Builder setResourceTypes(int index, String value)

Immutable. The resource instance type on which this policy applies. Format will be of the form : `<canonical service name>/<type>` Example:

  * `compute.googleapis.com/Instance`.



`repeated string resource_types = 2 [(.google.api.field_behavior) = IMMUTABLE];`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index to set the value at.  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The resourceTypes to set.  
**Returns**  
---  
**Type** | **Description**  
`[CustomConstraint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.CustomConstraint.Builder)` | This builder for chaining.  
  
### setUpdateTime(Timestamp value)
    
    
    public CustomConstraint.Builder setUpdateTime(Timestamp value)

Output only. The last time this custom constraint was updated. This represents the last time that the `CreateCustomConstraint` or `UpdateCustomConstraint` RPC was called

` .google.protobuf.Timestamp update_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CustomConstraint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.CustomConstraint.Builder)` |   
  
### setUpdateTime(Timestamp.Builder builderForValue)
    
    
    public CustomConstraint.Builder setUpdateTime(Timestamp.Builder builderForValue)

Output only. The last time this custom constraint was updated. This represents the last time that the `CreateCustomConstraint` or `UpdateCustomConstraint` RPC was called

` .google.protobuf.Timestamp update_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CustomConstraint.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.CustomConstraint.Builder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
