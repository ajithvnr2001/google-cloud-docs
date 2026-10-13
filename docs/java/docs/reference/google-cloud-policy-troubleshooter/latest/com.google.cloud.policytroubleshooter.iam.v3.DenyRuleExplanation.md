---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation
title: Class DenyRuleExplanation (1.98.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:46:11.406373+00:00
---

# Class DenyRuleExplanation (1.98.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DenyRuleExplanation (1.98.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.98.0 (latest)  1.94.0  1.93.0  1.92.0  1.90.0  1.87.0  1.86.0  1.84.0  1.82.0  1.81.0  1.79.0  1.77.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.0  1.69.0  1.67.0  1.66.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.6  1.1.0  1.0.4  0.4.4 
    
    
    public final class DenyRuleExplanation extends GeneratedMessage implements DenyRuleExplanationOrBuilder

Details about how a deny rule in a deny policy affects a principal's ability to use a permission.

Protobuf type `google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation`

## Inheritance

[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.html) > [AbstractMessage](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.html) > [GeneratedMessage](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html) > DenyRuleExplanation

## Implements

[DenyRuleExplanationOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanationOrBuilder)

## Inherited Members

[AbstractMessage.equals(Object)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.html#com_google_protobuf_AbstractMessage_equals_java_lang_Object_)

[AbstractMessage.findInitializationErrors()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.html#com_google_protobuf_AbstractMessage_findInitializationErrors__)

[AbstractMessage.getInitializationErrorString()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.html#com_google_protobuf_AbstractMessage_getInitializationErrorString__)

[AbstractMessage.hashCode()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.html#com_google_protobuf_AbstractMessage_hashCode__)

[AbstractMessage.hashFields(int,Map<Descriptors.FieldDescriptor,Object>)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.html#com_google_protobuf_AbstractMessage_hashFields_int_java_util_Map_com_google_protobuf_Descriptors_FieldDescriptor_java_lang_Object__)

[AbstractMessage.newBuilderForType(AbstractMessage.BuilderParent)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.html#com_google_protobuf_AbstractMessage_newBuilderForType_com_google_protobuf_AbstractMessage_BuilderParent_)

[AbstractMessage.toString()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.html#com_google_protobuf_AbstractMessage_toString__)

[AbstractMessageLite.<T>addAll(Iterable<T>,List<? super T>)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.html#com_google_protobuf_AbstractMessageLite__T_addAll_java_lang_Iterable_T__java_util_List___super_T__)

[AbstractMessageLite.checkByteStringIsUtf8(ByteString)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.html#com_google_protobuf_AbstractMessageLite_checkByteStringIsUtf8_com_google_protobuf_ByteString_)

[AbstractMessageLite.toByteArray()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.html#com_google_protobuf_AbstractMessageLite_toByteArray__)

[AbstractMessageLite.toByteString()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.html#com_google_protobuf_AbstractMessageLite_toByteString__)

[AbstractMessageLite.writeDelimitedTo(OutputStream)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.html#com_google_protobuf_AbstractMessageLite_writeDelimitedTo_java_io_OutputStream_)

[AbstractMessageLite.writeTo(OutputStream)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.html#com_google_protobuf_AbstractMessageLite_writeTo_java_io_OutputStream_)

com.google.protobuf.GeneratedMessage.<ContainingT,T>newFileScopedGeneratedExtension(java.lang.Class<?>,com.google.protobuf.Message)

com.google.protobuf.GeneratedMessage.<ContainingT,T>newMessageScopedGeneratedExtension(com.google.protobuf.Message,int,java.lang.Class<?>,com.google.protobuf.Message)

com.google.protobuf.GeneratedMessage.<ListT>makeMutableCopy(ListT)

com.google.protobuf.GeneratedMessage.<ListT>makeMutableCopy(ListT,int)

[GeneratedMessage.<M>parseDelimitedWithIOException(Parser<M>,InputStream)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage__M_parseDelimitedWithIOException_com_google_protobuf_Parser_M__java_io_InputStream_)

[GeneratedMessage.<M>parseDelimitedWithIOException(Parser<M>,InputStream,ExtensionRegistryLite)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage__M_parseDelimitedWithIOException_com_google_protobuf_Parser_M__java_io_InputStream_com_google_protobuf_ExtensionRegistryLite_)

[GeneratedMessage.<M>parseWithIOException(Parser<M>,CodedInputStream)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage__M_parseWithIOException_com_google_protobuf_Parser_M__com_google_protobuf_CodedInputStream_)

[GeneratedMessage.<M>parseWithIOException(Parser<M>,CodedInputStream,ExtensionRegistryLite)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage__M_parseWithIOException_com_google_protobuf_Parser_M__com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

[GeneratedMessage.<M>parseWithIOException(Parser<M>,InputStream)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage__M_parseWithIOException_com_google_protobuf_Parser_M__java_io_InputStream_)

[GeneratedMessage.<M>parseWithIOException(Parser<M>,InputStream,ExtensionRegistryLite)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage__M_parseWithIOException_com_google_protobuf_Parser_M__java_io_InputStream_com_google_protobuf_ExtensionRegistryLite_)

com.google.protobuf.GeneratedMessage.<T>emptyList(java.lang.Class<T>)

com.google.protobuf.GeneratedMessage.<V>serializeBooleanMapTo(com.google.protobuf.CodedOutputStream,com.google.protobuf.MapField<java.lang.Boolean,V>,com.google.protobuf.MapEntry<java.lang.Boolean,V>,int)

com.google.protobuf.GeneratedMessage.<V>serializeIntegerMapTo(com.google.protobuf.CodedOutputStream,com.google.protobuf.MapField<java.lang.Integer,V>,com.google.protobuf.MapEntry<java.lang.Integer,V>,int)

com.google.protobuf.GeneratedMessage.<V>serializeLongMapTo(com.google.protobuf.CodedOutputStream,com.google.protobuf.MapField<java.lang.Long,V>,com.google.protobuf.MapEntry<java.lang.Long,V>,int)

com.google.protobuf.GeneratedMessage.<V>serializeStringMapTo(com.google.protobuf.CodedOutputStream,com.google.protobuf.MapField<java.lang.String,V>,com.google.protobuf.MapEntry<java.lang.String,V>,int)

com.google.protobuf.GeneratedMessage.canUseUnsafe()

[GeneratedMessage.computeStringSize(int,Object)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_computeStringSize_int_java_lang_Object_)

[GeneratedMessage.computeStringSizeNoTag(Object)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_computeStringSizeNoTag_java_lang_Object_)

com.google.protobuf.GeneratedMessage.emptyBooleanList()

com.google.protobuf.GeneratedMessage.emptyDoubleList()

com.google.protobuf.GeneratedMessage.emptyFloatList()

com.google.protobuf.GeneratedMessage.emptyIntList()

com.google.protobuf.GeneratedMessage.emptyLongList()

[GeneratedMessage.getAllFields()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_getAllFields__)

[GeneratedMessage.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_getDescriptorForType__)

[GeneratedMessage.getField(Descriptors.FieldDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_getField_com_google_protobuf_Descriptors_FieldDescriptor_)

[GeneratedMessage.getOneofFieldDescriptor(Descriptors.OneofDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_getOneofFieldDescriptor_com_google_protobuf_Descriptors_OneofDescriptor_)

[GeneratedMessage.getParserForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_getParserForType__)

[GeneratedMessage.getRepeatedField(Descriptors.FieldDescriptor,int)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_getRepeatedField_com_google_protobuf_Descriptors_FieldDescriptor_int_)

[GeneratedMessage.getRepeatedFieldCount(Descriptors.FieldDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_getRepeatedFieldCount_com_google_protobuf_Descriptors_FieldDescriptor_)

[GeneratedMessage.getSerializedSize()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_getSerializedSize__)

[GeneratedMessage.getUnknownFields()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_getUnknownFields__)

[GeneratedMessage.hasField(Descriptors.FieldDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_hasField_com_google_protobuf_Descriptors_FieldDescriptor_)

[GeneratedMessage.hasOneof(Descriptors.OneofDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_hasOneof_com_google_protobuf_Descriptors_OneofDescriptor_)

[GeneratedMessage.internalGetFieldAccessorTable()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_internalGetFieldAccessorTable__)

[GeneratedMessage.internalGetMapField(int)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_internalGetMapField_int_)

com.google.protobuf.GeneratedMessage.internalGetMapFieldReflection(int)

[GeneratedMessage.isInitialized()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_isInitialized__)

com.google.protobuf.GeneratedMessage.isStringEmpty(java.lang.Object)

[GeneratedMessage.makeExtensionsImmutable()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_makeExtensionsImmutable__)

com.google.protobuf.GeneratedMessage.mergeFromAndMakeImmutableInternal(com.google.protobuf.CodedInputStream,com.google.protobuf.ExtensionRegistryLite)

com.google.protobuf.GeneratedMessage.newInstance(com.google.protobuf.GeneratedMessage.UnusedPrivateParameter)

[GeneratedMessage.parseUnknownField(CodedInputStream,UnknownFieldSet.Builder,ExtensionRegistryLite,int)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_parseUnknownField_com_google_protobuf_CodedInputStream_com_google_protobuf_UnknownFieldSet_Builder_com_google_protobuf_ExtensionRegistryLite_int_)

com.google.protobuf.GeneratedMessage.parseUnknownFieldProto3(com.google.protobuf.CodedInputStream,com.google.protobuf.UnknownFieldSet.Builder,com.google.protobuf.ExtensionRegistryLite,int)

[GeneratedMessage.writeReplace()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_writeReplace__)

[GeneratedMessage.writeString(CodedOutputStream,int,Object)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_writeString_com_google_protobuf_CodedOutputStream_int_java_lang_Object_)

[GeneratedMessage.writeStringNoTag(CodedOutputStream,Object)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_writeStringNoTag_com_google_protobuf_CodedOutputStream_java_lang_Object_)

[GeneratedMessage.writeTo(CodedOutputStream)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_writeTo_com_google_protobuf_CodedOutputStream_)

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Static Fields 

### COMBINED_DENIED_PERMISSION_FIELD_NUMBER
    
    
    public static final int COMBINED_DENIED_PERMISSION_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### COMBINED_DENIED_PRINCIPAL_FIELD_NUMBER
    
    
    public static final int COMBINED_DENIED_PRINCIPAL_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### COMBINED_EXCEPTION_PERMISSION_FIELD_NUMBER
    
    
    public static final int COMBINED_EXCEPTION_PERMISSION_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### COMBINED_EXCEPTION_PRINCIPAL_FIELD_NUMBER
    
    
    public static final int COMBINED_EXCEPTION_PRINCIPAL_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### CONDITION_EXPLANATION_FIELD_NUMBER
    
    
    public static final int CONDITION_EXPLANATION_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### CONDITION_FIELD_NUMBER
    
    
    public static final int CONDITION_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### DENIED_PERMISSIONS_FIELD_NUMBER
    
    
    public static final int DENIED_PERMISSIONS_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### DENIED_PRINCIPALS_FIELD_NUMBER
    
    
    public static final int DENIED_PRINCIPALS_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### DENY_ACCESS_STATE_FIELD_NUMBER
    
    
    public static final int DENY_ACCESS_STATE_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### EXCEPTION_PERMISSIONS_FIELD_NUMBER
    
    
    public static final int EXCEPTION_PERMISSIONS_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### EXCEPTION_PRINCIPALS_FIELD_NUMBER
    
    
    public static final int EXCEPTION_PRINCIPALS_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### RELEVANCE_FIELD_NUMBER
    
    
    public static final int RELEVANCE_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
## Static Methods 

### getDefaultInstance()
    
    
    public static DenyRuleExplanation getDefaultInstance()

**Returns**  
---  
**Type** | **Description**  
`[DenyRuleExplanation](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation)` |   
  
### getDescriptor()
    
    
    public static final Descriptors.Descriptor getDescriptor()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
  
### newBuilder()
    
    
    public static DenyRuleExplanation.Builder newBuilder()

**Returns**  
---  
**Type** | **Description**  
`[DenyRuleExplanation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.Builder)` |   
  
### newBuilder(DenyRuleExplanation prototype)
    
    
    public static DenyRuleExplanation.Builder newBuilder(DenyRuleExplanation prototype)

**Parameter**  
---  
**Name** | **Description**  
`prototype` | `[DenyRuleExplanation](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DenyRuleExplanation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.Builder)` |   
  
### parseDelimitedFrom(InputStream input)
    
    
    public static DenyRuleExplanation parseDelimitedFrom(InputStream input)

**Parameter**  
---  
**Name** | **Description**  
`input` | `[InputStream](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DenyRuleExplanation](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseDelimitedFrom(InputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public static DenyRuleExplanation parseDelimitedFrom(InputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[InputStream](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DenyRuleExplanation](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseFrom(byte[] data)
    
    
    public static DenyRuleExplanation parseFrom(byte[] data)

**Parameter**  
---  
**Name** | **Description**  
`data` | `byte[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[DenyRuleExplanation](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parseFrom(byte[] data, ExtensionRegistryLite extensionRegistry)
    
    
    public static DenyRuleExplanation parseFrom(byte[] data, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`data` | `byte[]`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DenyRuleExplanation](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parseFrom(ByteString data)
    
    
    public static DenyRuleExplanation parseFrom(ByteString data)

**Parameter**  
---  
**Name** | **Description**  
`data` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DenyRuleExplanation](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parseFrom(ByteString data, ExtensionRegistryLite extensionRegistry)
    
    
    public static DenyRuleExplanation parseFrom(ByteString data, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`data` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DenyRuleExplanation](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parseFrom(CodedInputStream input)
    
    
    public static DenyRuleExplanation parseFrom(CodedInputStream input)

**Parameter**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DenyRuleExplanation](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public static DenyRuleExplanation parseFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DenyRuleExplanation](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseFrom(InputStream input)
    
    
    public static DenyRuleExplanation parseFrom(InputStream input)

**Parameter**  
---  
**Name** | **Description**  
`input` | `[InputStream](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DenyRuleExplanation](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseFrom(InputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public static DenyRuleExplanation parseFrom(InputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[InputStream](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DenyRuleExplanation](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseFrom(ByteBuffer data)
    
    
    public static DenyRuleExplanation parseFrom(ByteBuffer data)

**Parameter**  
---  
**Name** | **Description**  
`data` | `[ByteBuffer](https://docs.oracle.com/javase/8/docs/api/java/nio/ByteBuffer.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DenyRuleExplanation](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parseFrom(ByteBuffer data, ExtensionRegistryLite extensionRegistry)
    
    
    public static DenyRuleExplanation parseFrom(ByteBuffer data, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`data` | `[ByteBuffer](https://docs.oracle.com/javase/8/docs/api/java/nio/ByteBuffer.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DenyRuleExplanation](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parser()
    
    
    public static Parser<DenyRuleExplanation> parser()

**Returns**  
---  
**Type** | **Description**  
`[Parser](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Parser.html)<[DenyRuleExplanation](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation)>` |   
  
## Methods 

### containsDeniedPermissions(String key)
    
    
    public boolean containsDeniedPermissions(String key)

Lists all denied permissions in the deny rule and indicates whether each permission matches the permission in the request.

Each key identifies a denied permission in the rule, and each value indicates whether the denied permission matches the permission in the request.

` map<string, .google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedPermissionMatching> denied_permissions = 3; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### containsDeniedPrincipals(String key)
    
    
    public boolean containsDeniedPrincipals(String key)

Lists all denied principals in the deny rule and indicates whether each principal matches the principal in the request, either directly or through membership in a principal set.

Each key identifies a denied principal in the rule, and each value indicates whether the denied principal matches the principal in the request.

` map<string, .google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedDenyPrincipalMatching> denied_principals = 7; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### containsExceptionPermissions(String key)
    
    
    public boolean containsExceptionPermissions(String key)

Lists all exception permissions in the deny rule and indicates whether each permission matches the permission in the request.

Each key identifies a exception permission in the rule, and each value indicates whether the exception permission matches the permission in the request.

` map<string, .google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedPermissionMatching> exception_permissions = 5; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### containsExceptionPrincipals(String key)
    
    
    public boolean containsExceptionPrincipals(String key)

Lists all exception principals in the deny rule and indicates whether each principal matches the principal in the request, either directly or through membership in a principal set.

Each key identifies a exception principal in the rule, and each value indicates whether the exception principal matches the principal in the request.

` map<string, .google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedDenyPrincipalMatching> exception_principals = 9; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### equals(Object obj)
    
    
    public boolean equals(Object obj)

**Parameter**  
---  
**Name** | **Description**  
`obj` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[AbstractMessage.equals(Object other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.html#com_google_protobuf_AbstractMessage_equals_java_lang_Object_)

### getCombinedDeniedPermission()
    
    
    public DenyRuleExplanation.AnnotatedPermissionMatching getCombinedDeniedPermission()

Indicates whether the permission in the request is listed as a denied permission in the deny rule.

` .google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedPermissionMatching combined_denied_permission = 2; `

**Returns**  
---  
**Type** | **Description**  
`[DenyRuleExplanation.AnnotatedPermissionMatching](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedPermissionMatching)` | The combinedDeniedPermission.  
  
### getCombinedDeniedPermissionOrBuilder()
    
    
    public DenyRuleExplanation.AnnotatedPermissionMatchingOrBuilder getCombinedDeniedPermissionOrBuilder()

Indicates whether the permission in the request is listed as a denied permission in the deny rule.

` .google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedPermissionMatching combined_denied_permission = 2; `

**Returns**  
---  
**Type** | **Description**  
`[DenyRuleExplanation.AnnotatedPermissionMatchingOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedPermissionMatchingOrBuilder)` |   
  
### getCombinedDeniedPrincipal()
    
    
    public DenyRuleExplanation.AnnotatedDenyPrincipalMatching getCombinedDeniedPrincipal()

Indicates whether the principal is listed as a denied principal in the deny rule, either directly or through membership in a principal set.

` .google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedDenyPrincipalMatching combined_denied_principal = 6; `

**Returns**  
---  
**Type** | **Description**  
`[DenyRuleExplanation.AnnotatedDenyPrincipalMatching](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedDenyPrincipalMatching)` | The combinedDeniedPrincipal.  
  
### getCombinedDeniedPrincipalOrBuilder()
    
    
    public DenyRuleExplanation.AnnotatedDenyPrincipalMatchingOrBuilder getCombinedDeniedPrincipalOrBuilder()

Indicates whether the principal is listed as a denied principal in the deny rule, either directly or through membership in a principal set.

` .google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedDenyPrincipalMatching combined_denied_principal = 6; `

**Returns**  
---  
**Type** | **Description**  
`[DenyRuleExplanation.AnnotatedDenyPrincipalMatchingOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedDenyPrincipalMatchingOrBuilder)` |   
  
### getCombinedExceptionPermission()
    
    
    public DenyRuleExplanation.AnnotatedPermissionMatching getCombinedExceptionPermission()

Indicates whether the permission in the request is listed as an exception permission in the deny rule.

` .google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedPermissionMatching combined_exception_permission = 4; `

**Returns**  
---  
**Type** | **Description**  
`[DenyRuleExplanation.AnnotatedPermissionMatching](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedPermissionMatching)` | The combinedExceptionPermission.  
  
### getCombinedExceptionPermissionOrBuilder()
    
    
    public DenyRuleExplanation.AnnotatedPermissionMatchingOrBuilder getCombinedExceptionPermissionOrBuilder()

Indicates whether the permission in the request is listed as an exception permission in the deny rule.

` .google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedPermissionMatching combined_exception_permission = 4; `

**Returns**  
---  
**Type** | **Description**  
`[DenyRuleExplanation.AnnotatedPermissionMatchingOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedPermissionMatchingOrBuilder)` |   
  
### getCombinedExceptionPrincipal()
    
    
    public DenyRuleExplanation.AnnotatedDenyPrincipalMatching getCombinedExceptionPrincipal()

Indicates whether the principal is listed as an exception principal in the deny rule, either directly or through membership in a principal set.

` .google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedDenyPrincipalMatching combined_exception_principal = 8; `

**Returns**  
---  
**Type** | **Description**  
`[DenyRuleExplanation.AnnotatedDenyPrincipalMatching](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedDenyPrincipalMatching)` | The combinedExceptionPrincipal.  
  
### getCombinedExceptionPrincipalOrBuilder()
    
    
    public DenyRuleExplanation.AnnotatedDenyPrincipalMatchingOrBuilder getCombinedExceptionPrincipalOrBuilder()

Indicates whether the principal is listed as an exception principal in the deny rule, either directly or through membership in a principal set.

` .google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedDenyPrincipalMatching combined_exception_principal = 8; `

**Returns**  
---  
**Type** | **Description**  
`[DenyRuleExplanation.AnnotatedDenyPrincipalMatchingOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedDenyPrincipalMatchingOrBuilder)` |   
  
### getCondition()
    
    
    public Expr getCondition()

A condition expression that specifies when the deny rule denies the principal access.

To learn about IAM Conditions, see <https://cloud.google.com/iam/help/conditions/overview>.

`.google.type.Expr condition = 11;`

**Returns**  
---  
**Type** | **Description**  
`com.google.type.Expr` | The condition.  
  
### getConditionExplanation()
    
    
    public ConditionExplanation getConditionExplanation()

Condition evaluation state for this role binding.

` .google.cloud.policytroubleshooter.iam.v3.ConditionExplanation condition_explanation = 12; `

**Returns**  
---  
**Type** | **Description**  
`[ConditionExplanation](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.ConditionExplanation)` | The conditionExplanation.  
  
### getConditionExplanationOrBuilder()
    
    
    public ConditionExplanationOrBuilder getConditionExplanationOrBuilder()

Condition evaluation state for this role binding.

` .google.cloud.policytroubleshooter.iam.v3.ConditionExplanation condition_explanation = 12; `

**Returns**  
---  
**Type** | **Description**  
`[ConditionExplanationOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.ConditionExplanationOrBuilder)` |   
  
### getConditionOrBuilder()
    
    
    public ExprOrBuilder getConditionOrBuilder()

A condition expression that specifies when the deny rule denies the principal access.

To learn about IAM Conditions, see <https://cloud.google.com/iam/help/conditions/overview>.

`.google.type.Expr condition = 11;`

**Returns**  
---  
**Type** | **Description**  
`com.google.type.ExprOrBuilder` |   
  
### getDefaultInstanceForType()
    
    
    public DenyRuleExplanation getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[DenyRuleExplanation](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation)` |   
  
### getDeniedPermissions() (deprecated)
    
    
    public Map<String,DenyRuleExplanation.AnnotatedPermissionMatching> getDeniedPermissions()

Use [#getDeniedPermissionsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation#com_google_cloud_policytroubleshooter_iam_v3_DenyRuleExplanation_getDeniedPermissionsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[AnnotatedPermissionMatching](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedPermissionMatching)>` |   
  
### getDeniedPermissionsCount()
    
    
    public int getDeniedPermissionsCount()

Lists all denied permissions in the deny rule and indicates whether each permission matches the permission in the request.

Each key identifies a denied permission in the rule, and each value indicates whether the denied permission matches the permission in the request.

` map<string, .google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedPermissionMatching> denied_permissions = 3; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getDeniedPermissionsMap()
    
    
    public Map<String,DenyRuleExplanation.AnnotatedPermissionMatching> getDeniedPermissionsMap()

Lists all denied permissions in the deny rule and indicates whether each permission matches the permission in the request.

Each key identifies a denied permission in the rule, and each value indicates whether the denied permission matches the permission in the request.

` map<string, .google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedPermissionMatching> denied_permissions = 3; `

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[AnnotatedPermissionMatching](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedPermissionMatching)>` |   
  
### getDeniedPermissionsOrDefault(String key, DenyRuleExplanation.AnnotatedPermissionMatching defaultValue)
    
    
    public DenyRuleExplanation.AnnotatedPermissionMatching getDeniedPermissionsOrDefault(String key, DenyRuleExplanation.AnnotatedPermissionMatching defaultValue)

Lists all denied permissions in the deny rule and indicates whether each permission matches the permission in the request.

Each key identifies a denied permission in the rule, and each value indicates whether the denied permission matches the permission in the request.

` map<string, .google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedPermissionMatching> denied_permissions = 3; `

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[DenyRuleExplanation.AnnotatedPermissionMatching](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedPermissionMatching)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DenyRuleExplanation.AnnotatedPermissionMatching](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedPermissionMatching)` |   
  
### getDeniedPermissionsOrThrow(String key)
    
    
    public DenyRuleExplanation.AnnotatedPermissionMatching getDeniedPermissionsOrThrow(String key)

Lists all denied permissions in the deny rule and indicates whether each permission matches the permission in the request.

Each key identifies a denied permission in the rule, and each value indicates whether the denied permission matches the permission in the request.

` map<string, .google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedPermissionMatching> denied_permissions = 3; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DenyRuleExplanation.AnnotatedPermissionMatching](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedPermissionMatching)` |   
  
### getDeniedPrincipals() (deprecated)
    
    
    public Map<String,DenyRuleExplanation.AnnotatedDenyPrincipalMatching> getDeniedPrincipals()

Use [#getDeniedPrincipalsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation#com_google_cloud_policytroubleshooter_iam_v3_DenyRuleExplanation_getDeniedPrincipalsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[AnnotatedDenyPrincipalMatching](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedDenyPrincipalMatching)>` |   
  
### getDeniedPrincipalsCount()
    
    
    public int getDeniedPrincipalsCount()

Lists all denied principals in the deny rule and indicates whether each principal matches the principal in the request, either directly or through membership in a principal set.

Each key identifies a denied principal in the rule, and each value indicates whether the denied principal matches the principal in the request.

` map<string, .google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedDenyPrincipalMatching> denied_principals = 7; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getDeniedPrincipalsMap()
    
    
    public Map<String,DenyRuleExplanation.AnnotatedDenyPrincipalMatching> getDeniedPrincipalsMap()

Lists all denied principals in the deny rule and indicates whether each principal matches the principal in the request, either directly or through membership in a principal set.

Each key identifies a denied principal in the rule, and each value indicates whether the denied principal matches the principal in the request.

` map<string, .google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedDenyPrincipalMatching> denied_principals = 7; `

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[AnnotatedDenyPrincipalMatching](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedDenyPrincipalMatching)>` |   
  
### getDeniedPrincipalsOrDefault(String key, DenyRuleExplanation.AnnotatedDenyPrincipalMatching defaultValue)
    
    
    public DenyRuleExplanation.AnnotatedDenyPrincipalMatching getDeniedPrincipalsOrDefault(String key, DenyRuleExplanation.AnnotatedDenyPrincipalMatching defaultValue)

Lists all denied principals in the deny rule and indicates whether each principal matches the principal in the request, either directly or through membership in a principal set.

Each key identifies a denied principal in the rule, and each value indicates whether the denied principal matches the principal in the request.

` map<string, .google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedDenyPrincipalMatching> denied_principals = 7; `

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[DenyRuleExplanation.AnnotatedDenyPrincipalMatching](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedDenyPrincipalMatching)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DenyRuleExplanation.AnnotatedDenyPrincipalMatching](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedDenyPrincipalMatching)` |   
  
### getDeniedPrincipalsOrThrow(String key)
    
    
    public DenyRuleExplanation.AnnotatedDenyPrincipalMatching getDeniedPrincipalsOrThrow(String key)

Lists all denied principals in the deny rule and indicates whether each principal matches the principal in the request, either directly or through membership in a principal set.

Each key identifies a denied principal in the rule, and each value indicates whether the denied principal matches the principal in the request.

` map<string, .google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedDenyPrincipalMatching> denied_principals = 7; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DenyRuleExplanation.AnnotatedDenyPrincipalMatching](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedDenyPrincipalMatching)` |   
  
### getDenyAccessState()
    
    
    public DenyAccessState getDenyAccessState()

Required. Indicates whether _this rule_ denies the specified permission to the specified principal for the specified resource.

This field does _not_ indicate whether the principal is actually denied on the permission for the resource. There might be another rule that overrides this rule. To determine whether the principal actually has the permission, use the `overall_access_state` field in the TroubleshootIamPolicyResponse.

` .google.cloud.policytroubleshooter.iam.v3.DenyAccessState deny_access_state = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[DenyAccessState](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.DenyAccessState)` | The denyAccessState.  
  
### getDenyAccessStateValue()
    
    
    public int getDenyAccessStateValue()

Required. Indicates whether _this rule_ denies the specified permission to the specified principal for the specified resource.

This field does _not_ indicate whether the principal is actually denied on the permission for the resource. There might be another rule that overrides this rule. To determine whether the principal actually has the permission, use the `overall_access_state` field in the TroubleshootIamPolicyResponse.

` .google.cloud.policytroubleshooter.iam.v3.DenyAccessState deny_access_state = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for denyAccessState.  
  
### getExceptionPermissions() (deprecated)
    
    
    public Map<String,DenyRuleExplanation.AnnotatedPermissionMatching> getExceptionPermissions()

Use [#getExceptionPermissionsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation#com_google_cloud_policytroubleshooter_iam_v3_DenyRuleExplanation_getExceptionPermissionsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[AnnotatedPermissionMatching](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedPermissionMatching)>` |   
  
### getExceptionPermissionsCount()
    
    
    public int getExceptionPermissionsCount()

Lists all exception permissions in the deny rule and indicates whether each permission matches the permission in the request.

Each key identifies a exception permission in the rule, and each value indicates whether the exception permission matches the permission in the request.

` map<string, .google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedPermissionMatching> exception_permissions = 5; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getExceptionPermissionsMap()
    
    
    public Map<String,DenyRuleExplanation.AnnotatedPermissionMatching> getExceptionPermissionsMap()

Lists all exception permissions in the deny rule and indicates whether each permission matches the permission in the request.

Each key identifies a exception permission in the rule, and each value indicates whether the exception permission matches the permission in the request.

` map<string, .google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedPermissionMatching> exception_permissions = 5; `

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[AnnotatedPermissionMatching](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedPermissionMatching)>` |   
  
### getExceptionPermissionsOrDefault(String key, DenyRuleExplanation.AnnotatedPermissionMatching defaultValue)
    
    
    public DenyRuleExplanation.AnnotatedPermissionMatching getExceptionPermissionsOrDefault(String key, DenyRuleExplanation.AnnotatedPermissionMatching defaultValue)

Lists all exception permissions in the deny rule and indicates whether each permission matches the permission in the request.

Each key identifies a exception permission in the rule, and each value indicates whether the exception permission matches the permission in the request.

` map<string, .google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedPermissionMatching> exception_permissions = 5; `

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[DenyRuleExplanation.AnnotatedPermissionMatching](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedPermissionMatching)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DenyRuleExplanation.AnnotatedPermissionMatching](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedPermissionMatching)` |   
  
### getExceptionPermissionsOrThrow(String key)
    
    
    public DenyRuleExplanation.AnnotatedPermissionMatching getExceptionPermissionsOrThrow(String key)

Lists all exception permissions in the deny rule and indicates whether each permission matches the permission in the request.

Each key identifies a exception permission in the rule, and each value indicates whether the exception permission matches the permission in the request.

` map<string, .google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedPermissionMatching> exception_permissions = 5; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DenyRuleExplanation.AnnotatedPermissionMatching](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedPermissionMatching)` |   
  
### getExceptionPrincipals() (deprecated)
    
    
    public Map<String,DenyRuleExplanation.AnnotatedDenyPrincipalMatching> getExceptionPrincipals()

Use [#getExceptionPrincipalsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation#com_google_cloud_policytroubleshooter_iam_v3_DenyRuleExplanation_getExceptionPrincipalsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[AnnotatedDenyPrincipalMatching](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedDenyPrincipalMatching)>` |   
  
### getExceptionPrincipalsCount()
    
    
    public int getExceptionPrincipalsCount()

Lists all exception principals in the deny rule and indicates whether each principal matches the principal in the request, either directly or through membership in a principal set.

Each key identifies a exception principal in the rule, and each value indicates whether the exception principal matches the principal in the request.

` map<string, .google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedDenyPrincipalMatching> exception_principals = 9; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getExceptionPrincipalsMap()
    
    
    public Map<String,DenyRuleExplanation.AnnotatedDenyPrincipalMatching> getExceptionPrincipalsMap()

Lists all exception principals in the deny rule and indicates whether each principal matches the principal in the request, either directly or through membership in a principal set.

Each key identifies a exception principal in the rule, and each value indicates whether the exception principal matches the principal in the request.

` map<string, .google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedDenyPrincipalMatching> exception_principals = 9; `

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[AnnotatedDenyPrincipalMatching](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedDenyPrincipalMatching)>` |   
  
### getExceptionPrincipalsOrDefault(String key, DenyRuleExplanation.AnnotatedDenyPrincipalMatching defaultValue)
    
    
    public DenyRuleExplanation.AnnotatedDenyPrincipalMatching getExceptionPrincipalsOrDefault(String key, DenyRuleExplanation.AnnotatedDenyPrincipalMatching defaultValue)

Lists all exception principals in the deny rule and indicates whether each principal matches the principal in the request, either directly or through membership in a principal set.

Each key identifies a exception principal in the rule, and each value indicates whether the exception principal matches the principal in the request.

` map<string, .google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedDenyPrincipalMatching> exception_principals = 9; `

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[DenyRuleExplanation.AnnotatedDenyPrincipalMatching](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedDenyPrincipalMatching)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DenyRuleExplanation.AnnotatedDenyPrincipalMatching](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedDenyPrincipalMatching)` |   
  
### getExceptionPrincipalsOrThrow(String key)
    
    
    public DenyRuleExplanation.AnnotatedDenyPrincipalMatching getExceptionPrincipalsOrThrow(String key)

Lists all exception principals in the deny rule and indicates whether each principal matches the principal in the request, either directly or through membership in a principal set.

Each key identifies a exception principal in the rule, and each value indicates whether the exception principal matches the principal in the request.

` map<string, .google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedDenyPrincipalMatching> exception_principals = 9; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DenyRuleExplanation.AnnotatedDenyPrincipalMatching](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedDenyPrincipalMatching)` |   
  
### getParserForType()
    
    
    public Parser<DenyRuleExplanation> getParserForType()

**Returns**  
---  
**Type** | **Description**  
`[Parser](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Parser.html)<[DenyRuleExplanation](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation)>` |   
**Overrides**

[GeneratedMessage.getParserForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_getParserForType__)

### getRelevance()
    
    
    public HeuristicRelevance getRelevance()

The relevance of this role binding to the overall determination for the entire policy.

`.google.cloud.policytroubleshooter.iam.v3.HeuristicRelevance relevance = 10;`

**Returns**  
---  
**Type** | **Description**  
`[HeuristicRelevance](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.HeuristicRelevance)` | The relevance.  
  
### getRelevanceValue()
    
    
    public int getRelevanceValue()

The relevance of this role binding to the overall determination for the entire policy.

`.google.cloud.policytroubleshooter.iam.v3.HeuristicRelevance relevance = 10;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for relevance.  
  
### getSerializedSize()
    
    
    public int getSerializedSize()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[GeneratedMessage.getSerializedSize()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_getSerializedSize__)

### hasCombinedDeniedPermission()
    
    
    public boolean hasCombinedDeniedPermission()

Indicates whether the permission in the request is listed as a denied permission in the deny rule.

` .google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedPermissionMatching combined_denied_permission = 2; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the combinedDeniedPermission field is set.  
  
### hasCombinedDeniedPrincipal()
    
    
    public boolean hasCombinedDeniedPrincipal()

Indicates whether the principal is listed as a denied principal in the deny rule, either directly or through membership in a principal set.

` .google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedDenyPrincipalMatching combined_denied_principal = 6; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the combinedDeniedPrincipal field is set.  
  
### hasCombinedExceptionPermission()
    
    
    public boolean hasCombinedExceptionPermission()

Indicates whether the permission in the request is listed as an exception permission in the deny rule.

` .google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedPermissionMatching combined_exception_permission = 4; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the combinedExceptionPermission field is set.  
  
### hasCombinedExceptionPrincipal()
    
    
    public boolean hasCombinedExceptionPrincipal()

Indicates whether the principal is listed as an exception principal in the deny rule, either directly or through membership in a principal set.

` .google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedDenyPrincipalMatching combined_exception_principal = 8; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the combinedExceptionPrincipal field is set.  
  
### hasCondition()
    
    
    public boolean hasCondition()

A condition expression that specifies when the deny rule denies the principal access.

To learn about IAM Conditions, see <https://cloud.google.com/iam/help/conditions/overview>.

`.google.type.Expr condition = 11;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the condition field is set.  
  
### hasConditionExplanation()
    
    
    public boolean hasConditionExplanation()

Condition evaluation state for this role binding.

` .google.cloud.policytroubleshooter.iam.v3.ConditionExplanation condition_explanation = 12; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the conditionExplanation field is set.  
  
### hashCode()
    
    
    public int hashCode()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[AbstractMessage.hashCode()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.html#com_google_protobuf_AbstractMessage_hashCode__)

### internalGetFieldAccessorTable()
    
    
    protected GeneratedMessage.FieldAccessorTable internalGetFieldAccessorTable()

**Returns**  
---  
**Type** | **Description**  
`[FieldAccessorTable](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.FieldAccessorTable.html)` |   
**Overrides**

[GeneratedMessage.internalGetFieldAccessorTable()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_internalGetFieldAccessorTable__)

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

com.google.protobuf.GeneratedMessage.internalGetMapFieldReflection(int)

### isInitialized()
    
    
    public final boolean isInitialized()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[GeneratedMessage.isInitialized()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_isInitialized__)

### newBuilderForType()
    
    
    public DenyRuleExplanation.Builder newBuilderForType()

**Returns**  
---  
**Type** | **Description**  
`[DenyRuleExplanation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.Builder)` |   
  
### newBuilderForType(AbstractMessage.BuilderParent parent)
    
    
    protected DenyRuleExplanation.Builder newBuilderForType(AbstractMessage.BuilderParent parent)

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[BuilderParent](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.BuilderParent.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DenyRuleExplanation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.Builder)` |   
**Overrides**

[AbstractMessage.newBuilderForType(AbstractMessage.BuilderParent parent)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.html#com_google_protobuf_AbstractMessage_newBuilderForType_com_google_protobuf_AbstractMessage_BuilderParent_)

### toBuilder()
    
    
    public DenyRuleExplanation.Builder toBuilder()

**Returns**  
---  
**Type** | **Description**  
`[DenyRuleExplanation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.Builder)` |   
  
### writeTo(CodedOutputStream output)
    
    
    public void writeTo(CodedOutputStream output)

**Parameter**  
---  
**Name** | **Description**  
`output` | `[CodedOutputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedOutputStream.html)`  
  
**Overrides**

[GeneratedMessage.writeTo(CodedOutputStream output)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_writeTo_com_google_protobuf_CodedOutputStream_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
