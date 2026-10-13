---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job
title: Class Job (2.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:41:06.832046+00:00
---

# Class Job (2.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class Job (2.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.100.0 (latest)  2.96.0  2.95.0  2.94.0  2.92.0  2.89.0  2.88.0  2.86.0  2.84.0  2.83.0  2.81.0  2.79.0  2.77.0  2.76.0  2.75.0  2.74.0  2.73.0  2.71.0  2.69.0  2.68.0  2.65.0  2.64.0  2.63.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.6  2.2.9 
    
    
    public final class Job extends GeneratedMessage implements JobOrBuilder

A Job resource represents a job posting (also referred to as a "job listing" or "job requisition"). A job belongs to a Company, which is the hiring entity responsible for the job.

Protobuf type `google.cloud.talent.v4.Job`

## Inheritance

[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.html) > [AbstractMessage](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.html) > [GeneratedMessage](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html) > Job

## Implements

[JobOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.JobOrBuilder)

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

### ADDRESSES_FIELD_NUMBER
    
    
    public static final int ADDRESSES_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### APPLICATION_INFO_FIELD_NUMBER
    
    
    public static final int APPLICATION_INFO_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### COMPANY_DISPLAY_NAME_FIELD_NUMBER
    
    
    public static final int COMPANY_DISPLAY_NAME_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### COMPANY_FIELD_NUMBER
    
    
    public static final int COMPANY_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### COMPENSATION_INFO_FIELD_NUMBER
    
    
    public static final int COMPENSATION_INFO_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### CUSTOM_ATTRIBUTES_FIELD_NUMBER
    
    
    public static final int CUSTOM_ATTRIBUTES_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### DEGREE_TYPES_FIELD_NUMBER
    
    
    public static final int DEGREE_TYPES_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### DEPARTMENT_FIELD_NUMBER
    
    
    public static final int DEPARTMENT_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### DERIVED_INFO_FIELD_NUMBER
    
    
    public static final int DERIVED_INFO_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### DESCRIPTION_FIELD_NUMBER
    
    
    public static final int DESCRIPTION_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### EMPLOYMENT_TYPES_FIELD_NUMBER
    
    
    public static final int EMPLOYMENT_TYPES_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### INCENTIVES_FIELD_NUMBER
    
    
    public static final int INCENTIVES_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### JOB_BENEFITS_FIELD_NUMBER
    
    
    public static final int JOB_BENEFITS_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### JOB_END_TIME_FIELD_NUMBER
    
    
    public static final int JOB_END_TIME_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### JOB_LEVEL_FIELD_NUMBER
    
    
    public static final int JOB_LEVEL_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### JOB_START_TIME_FIELD_NUMBER
    
    
    public static final int JOB_START_TIME_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### LANGUAGE_CODE_FIELD_NUMBER
    
    
    public static final int LANGUAGE_CODE_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### NAME_FIELD_NUMBER
    
    
    public static final int NAME_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### POSTING_CREATE_TIME_FIELD_NUMBER
    
    
    public static final int POSTING_CREATE_TIME_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### POSTING_EXPIRE_TIME_FIELD_NUMBER
    
    
    public static final int POSTING_EXPIRE_TIME_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### POSTING_PUBLISH_TIME_FIELD_NUMBER
    
    
    public static final int POSTING_PUBLISH_TIME_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### POSTING_REGION_FIELD_NUMBER
    
    
    public static final int POSTING_REGION_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### POSTING_UPDATE_TIME_FIELD_NUMBER
    
    
    public static final int POSTING_UPDATE_TIME_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### PROCESSING_OPTIONS_FIELD_NUMBER
    
    
    public static final int PROCESSING_OPTIONS_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### PROMOTION_VALUE_FIELD_NUMBER
    
    
    public static final int PROMOTION_VALUE_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### QUALIFICATIONS_FIELD_NUMBER
    
    
    public static final int QUALIFICATIONS_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### REQUISITION_ID_FIELD_NUMBER
    
    
    public static final int REQUISITION_ID_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### RESPONSIBILITIES_FIELD_NUMBER
    
    
    public static final int RESPONSIBILITIES_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### TITLE_FIELD_NUMBER
    
    
    public static final int TITLE_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### VISIBILITY_FIELD_NUMBER
    
    
    public static final int VISIBILITY_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
## Static Methods 

### getDefaultInstance()
    
    
    public static Job getDefaultInstance()

**Returns**  
---  
**Type** | **Description**  
`[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job)` |   
  
### getDescriptor()
    
    
    public static final Descriptors.Descriptor getDescriptor()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
  
### newBuilder()
    
    
    public static Job.Builder newBuilder()

**Returns**  
---  
**Type** | **Description**  
`[Job.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job.Builder)` |   
  
### newBuilder(Job prototype)
    
    
    public static Job.Builder newBuilder(Job prototype)

**Parameter**  
---  
**Name** | **Description**  
`prototype` | `[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Job.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job.Builder)` |   
  
### parseDelimitedFrom(InputStream input)
    
    
    public static Job parseDelimitedFrom(InputStream input)

**Parameter**  
---  
**Name** | **Description**  
`input` | `[InputStream](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseDelimitedFrom(InputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public static Job parseDelimitedFrom(InputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[InputStream](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseFrom(byte[] data)
    
    
    public static Job parseFrom(byte[] data)

**Parameter**  
---  
**Name** | **Description**  
`data` | `byte[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parseFrom(byte[] data, ExtensionRegistryLite extensionRegistry)
    
    
    public static Job parseFrom(byte[] data, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`data` | `byte[]`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parseFrom(ByteString data)
    
    
    public static Job parseFrom(ByteString data)

**Parameter**  
---  
**Name** | **Description**  
`data` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parseFrom(ByteString data, ExtensionRegistryLite extensionRegistry)
    
    
    public static Job parseFrom(ByteString data, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`data` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parseFrom(CodedInputStream input)
    
    
    public static Job parseFrom(CodedInputStream input)

**Parameter**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public static Job parseFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseFrom(InputStream input)
    
    
    public static Job parseFrom(InputStream input)

**Parameter**  
---  
**Name** | **Description**  
`input` | `[InputStream](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseFrom(InputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public static Job parseFrom(InputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[InputStream](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseFrom(ByteBuffer data)
    
    
    public static Job parseFrom(ByteBuffer data)

**Parameter**  
---  
**Name** | **Description**  
`data` | `[ByteBuffer](https://docs.oracle.com/javase/8/docs/api/java/nio/ByteBuffer.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parseFrom(ByteBuffer data, ExtensionRegistryLite extensionRegistry)
    
    
    public static Job parseFrom(ByteBuffer data, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`data` | `[ByteBuffer](https://docs.oracle.com/javase/8/docs/api/java/nio/ByteBuffer.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parser()
    
    
    public static Parser<Job> parser()

**Returns**  
---  
**Type** | **Description**  
`[Parser](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Parser.html)<[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job)>` |   
  
## Methods 

### containsCustomAttributes(String key)
    
    
    public boolean containsCustomAttributes(String key)

A map of fields to hold both filterable and non-filterable custom job attributes that are not covered by the provided structured fields.

The keys of the map are strings up to 64 bytes and must match the pattern: `a-zA-Z*`. For example, key0LikeThis or KEY_1_LIKE_THIS.

At most 100 filterable and at most 100 unfilterable keys are supported. For filterable `string_values`, across all keys at most 200 values are allowed, with each string no more than 255 characters. For unfilterable `string_values`, the maximum total size of `string_values` across all keys is 50KB.

`map<string, .google.cloud.talent.v4.CustomAttribute> custom_attributes = 10;`

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

### getAddresses(int index)
    
    
    public String getAddresses(int index)

Strongly recommended for the best service experience.

Location(s) where the employer is looking to hire for this job posting.

Specifying the full street address(es) of the hiring location enables better API results, especially job searches by commute time.

At most 50 locations are allowed for best search performance. If a job has more locations, it is suggested to split it into multiple jobs with unique requisition_ids (e.g. 'ReqA' becomes 'ReqA-1', 'ReqA-2', and so on.) as multiple jobs with the same company, language_code and requisition_id are not allowed. If the original requisition_id must be preserved, a custom field should be used for storage. It is also suggested to group the locations that close to each other in the same job for better search experience.

Jobs with multiple addresses must have their addresses with the same LocationType to allow location filtering to work properly. (For example, a Job with addresses "1600 Amphitheatre Parkway, Mountain View, CA, USA" and "London, UK" may not have location filters applied correctly at search time since the first is a LocationType.STREET_ADDRESS and the second is a LocationType.LOCALITY.) If a job needs to have multiple addresses, it is suggested to split it into multiple jobs with same LocationTypes.

The maximum number of allowed characters is 500.

`repeated string addresses = 6;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The addresses at the given index.  
  
### getAddressesBytes(int index)
    
    
    public ByteString getAddressesBytes(int index)

Strongly recommended for the best service experience.

Location(s) where the employer is looking to hire for this job posting.

Specifying the full street address(es) of the hiring location enables better API results, especially job searches by commute time.

At most 50 locations are allowed for best search performance. If a job has more locations, it is suggested to split it into multiple jobs with unique requisition_ids (e.g. 'ReqA' becomes 'ReqA-1', 'ReqA-2', and so on.) as multiple jobs with the same company, language_code and requisition_id are not allowed. If the original requisition_id must be preserved, a custom field should be used for storage. It is also suggested to group the locations that close to each other in the same job for better search experience.

Jobs with multiple addresses must have their addresses with the same LocationType to allow location filtering to work properly. (For example, a Job with addresses "1600 Amphitheatre Parkway, Mountain View, CA, USA" and "London, UK" may not have location filters applied correctly at search time since the first is a LocationType.STREET_ADDRESS and the second is a LocationType.LOCALITY.) If a job needs to have multiple addresses, it is suggested to split it into multiple jobs with same LocationTypes.

The maximum number of allowed characters is 500.

`repeated string addresses = 6;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the addresses at the given index.  
  
### getAddressesCount()
    
    
    public int getAddressesCount()

Strongly recommended for the best service experience.

Location(s) where the employer is looking to hire for this job posting.

Specifying the full street address(es) of the hiring location enables better API results, especially job searches by commute time.

At most 50 locations are allowed for best search performance. If a job has more locations, it is suggested to split it into multiple jobs with unique requisition_ids (e.g. 'ReqA' becomes 'ReqA-1', 'ReqA-2', and so on.) as multiple jobs with the same company, language_code and requisition_id are not allowed. If the original requisition_id must be preserved, a custom field should be used for storage. It is also suggested to group the locations that close to each other in the same job for better search experience.

Jobs with multiple addresses must have their addresses with the same LocationType to allow location filtering to work properly. (For example, a Job with addresses "1600 Amphitheatre Parkway, Mountain View, CA, USA" and "London, UK" may not have location filters applied correctly at search time since the first is a LocationType.STREET_ADDRESS and the second is a LocationType.LOCALITY.) If a job needs to have multiple addresses, it is suggested to split it into multiple jobs with same LocationTypes.

The maximum number of allowed characters is 500.

`repeated string addresses = 6;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of addresses.  
  
### getAddressesList()
    
    
    public ProtocolStringList getAddressesList()

Strongly recommended for the best service experience.

Location(s) where the employer is looking to hire for this job posting.

Specifying the full street address(es) of the hiring location enables better API results, especially job searches by commute time.

At most 50 locations are allowed for best search performance. If a job has more locations, it is suggested to split it into multiple jobs with unique requisition_ids (e.g. 'ReqA' becomes 'ReqA-1', 'ReqA-2', and so on.) as multiple jobs with the same company, language_code and requisition_id are not allowed. If the original requisition_id must be preserved, a custom field should be used for storage. It is also suggested to group the locations that close to each other in the same job for better search experience.

Jobs with multiple addresses must have their addresses with the same LocationType to allow location filtering to work properly. (For example, a Job with addresses "1600 Amphitheatre Parkway, Mountain View, CA, USA" and "London, UK" may not have location filters applied correctly at search time since the first is a LocationType.STREET_ADDRESS and the second is a LocationType.LOCALITY.) If a job needs to have multiple addresses, it is suggested to split it into multiple jobs with same LocationTypes.

The maximum number of allowed characters is 500.

`repeated string addresses = 6;`

**Returns**  
---  
**Type** | **Description**  
`[ProtocolStringList](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ProtocolStringList.html)` | A list containing the addresses.  
  
### getApplicationInfo()
    
    
    public Job.ApplicationInfo getApplicationInfo()

Job application information.

`.google.cloud.talent.v4.Job.ApplicationInfo application_info = 7;`

**Returns**  
---  
**Type** | **Description**  
`[Job.ApplicationInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job.ApplicationInfo)` | The applicationInfo.  
  
### getApplicationInfoOrBuilder()
    
    
    public Job.ApplicationInfoOrBuilder getApplicationInfoOrBuilder()

Job application information.

`.google.cloud.talent.v4.Job.ApplicationInfo application_info = 7;`

**Returns**  
---  
**Type** | **Description**  
`[Job.ApplicationInfoOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job.ApplicationInfoOrBuilder)` |   
  
### getCompany()
    
    
    public String getCompany()

Required. The resource name of the company listing the job.

The format is "projects/{project_id}/tenants/{tenant_id}/companies/{company_id}". For example, "projects/foo/tenants/bar/companies/baz".

` string company = 2 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The company.  
  
### getCompanyBytes()
    
    
    public ByteString getCompanyBytes()

Required. The resource name of the company listing the job.

The format is "projects/{project_id}/tenants/{tenant_id}/companies/{company_id}". For example, "projects/foo/tenants/bar/companies/baz".

` string company = 2 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for company.  
  
### getCompanyDisplayName()
    
    
    public String getCompanyDisplayName()

Output only. Display name of the company listing the job.

`string company_display_name = 28 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The companyDisplayName.  
  
### getCompanyDisplayNameBytes()
    
    
    public ByteString getCompanyDisplayNameBytes()

Output only. Display name of the company listing the job.

`string company_display_name = 28 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for companyDisplayName.  
  
### getCompensationInfo()
    
    
    public CompensationInfo getCompensationInfo()

Job compensation information (a.k.a. "pay rate") i.e., the compensation that will paid to the employee.

`.google.cloud.talent.v4.CompensationInfo compensation_info = 9;`

**Returns**  
---  
**Type** | **Description**  
`[CompensationInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CompensationInfo)` | The compensationInfo.  
  
### getCompensationInfoOrBuilder()
    
    
    public CompensationInfoOrBuilder getCompensationInfoOrBuilder()

Job compensation information (a.k.a. "pay rate") i.e., the compensation that will paid to the employee.

`.google.cloud.talent.v4.CompensationInfo compensation_info = 9;`

**Returns**  
---  
**Type** | **Description**  
`[CompensationInfoOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CompensationInfoOrBuilder)` |   
  
### getCustomAttributes() (deprecated)
    
    
    public Map<String,CustomAttribute> getCustomAttributes()

Use [#getCustomAttributesMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job#com_google_cloud_talent_v4_Job_getCustomAttributesMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[CustomAttribute](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CustomAttribute)>` |   
  
### getCustomAttributesCount()
    
    
    public int getCustomAttributesCount()

A map of fields to hold both filterable and non-filterable custom job attributes that are not covered by the provided structured fields.

The keys of the map are strings up to 64 bytes and must match the pattern: `a-zA-Z*`. For example, key0LikeThis or KEY_1_LIKE_THIS.

At most 100 filterable and at most 100 unfilterable keys are supported. For filterable `string_values`, across all keys at most 200 values are allowed, with each string no more than 255 characters. For unfilterable `string_values`, the maximum total size of `string_values` across all keys is 50KB.

`map<string, .google.cloud.talent.v4.CustomAttribute> custom_attributes = 10;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getCustomAttributesMap()
    
    
    public Map<String,CustomAttribute> getCustomAttributesMap()

A map of fields to hold both filterable and non-filterable custom job attributes that are not covered by the provided structured fields.

The keys of the map are strings up to 64 bytes and must match the pattern: `a-zA-Z*`. For example, key0LikeThis or KEY_1_LIKE_THIS.

At most 100 filterable and at most 100 unfilterable keys are supported. For filterable `string_values`, across all keys at most 200 values are allowed, with each string no more than 255 characters. For unfilterable `string_values`, the maximum total size of `string_values` across all keys is 50KB.

`map<string, .google.cloud.talent.v4.CustomAttribute> custom_attributes = 10;`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[CustomAttribute](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CustomAttribute)>` |   
  
### getCustomAttributesOrDefault(String key, CustomAttribute defaultValue)
    
    
    public CustomAttribute getCustomAttributesOrDefault(String key, CustomAttribute defaultValue)

A map of fields to hold both filterable and non-filterable custom job attributes that are not covered by the provided structured fields.

The keys of the map are strings up to 64 bytes and must match the pattern: `a-zA-Z*`. For example, key0LikeThis or KEY_1_LIKE_THIS.

At most 100 filterable and at most 100 unfilterable keys are supported. For filterable `string_values`, across all keys at most 200 values are allowed, with each string no more than 255 characters. For unfilterable `string_values`, the maximum total size of `string_values` across all keys is 50KB.

`map<string, .google.cloud.talent.v4.CustomAttribute> custom_attributes = 10;`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[CustomAttribute](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CustomAttribute)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CustomAttribute](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CustomAttribute)` |   
  
### getCustomAttributesOrThrow(String key)
    
    
    public CustomAttribute getCustomAttributesOrThrow(String key)

A map of fields to hold both filterable and non-filterable custom job attributes that are not covered by the provided structured fields.

The keys of the map are strings up to 64 bytes and must match the pattern: `a-zA-Z*`. For example, key0LikeThis or KEY_1_LIKE_THIS.

At most 100 filterable and at most 100 unfilterable keys are supported. For filterable `string_values`, across all keys at most 200 values are allowed, with each string no more than 255 characters. For unfilterable `string_values`, the maximum total size of `string_values` across all keys is 50KB.

`map<string, .google.cloud.talent.v4.CustomAttribute> custom_attributes = 10;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CustomAttribute](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CustomAttribute)` |   
  
### getDefaultInstanceForType()
    
    
    public Job getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job)` |   
  
### getDegreeTypes(int index)
    
    
    public DegreeType getDegreeTypes(int index)

The desired education degrees for the job, such as Bachelors, Masters.

`repeated .google.cloud.talent.v4.DegreeType degree_types = 11;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[DegreeType](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.DegreeType)` | The degreeTypes at the given index.  
  
### getDegreeTypesCount()
    
    
    public int getDegreeTypesCount()

The desired education degrees for the job, such as Bachelors, Masters.

`repeated .google.cloud.talent.v4.DegreeType degree_types = 11;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of degreeTypes.  
  
### getDegreeTypesList()
    
    
    public List<DegreeType> getDegreeTypesList()

The desired education degrees for the job, such as Bachelors, Masters.

`repeated .google.cloud.talent.v4.DegreeType degree_types = 11;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[DegreeType](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.DegreeType)>` | A list containing the degreeTypes.  
  
### getDegreeTypesValue(int index)
    
    
    public int getDegreeTypesValue(int index)

The desired education degrees for the job, such as Bachelors, Masters.

`repeated .google.cloud.talent.v4.DegreeType degree_types = 11;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire of degreeTypes at the given index.  
  
### getDegreeTypesValueList()
    
    
    public List<Integer> getDegreeTypesValueList()

The desired education degrees for the job, such as Bachelors, Masters.

`repeated .google.cloud.talent.v4.DegreeType degree_types = 11;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)>` | A list containing the enum numeric values on the wire for degreeTypes.  
  
### getDepartment()
    
    
    public String getDepartment()

The department or functional area within the company with the open position.

The maximum number of allowed characters is 255.

`string department = 12;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The department.  
  
### getDepartmentBytes()
    
    
    public ByteString getDepartmentBytes()

The department or functional area within the company with the open position.

The maximum number of allowed characters is 255.

`string department = 12;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for department.  
  
### getDerivedInfo()
    
    
    public Job.DerivedInfo getDerivedInfo()

Output only. Derived details about the job posting.

` .google.cloud.talent.v4.Job.DerivedInfo derived_info = 29 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Job.DerivedInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job.DerivedInfo)` | The derivedInfo.  
  
### getDerivedInfoOrBuilder()
    
    
    public Job.DerivedInfoOrBuilder getDerivedInfoOrBuilder()

Output only. Derived details about the job posting.

` .google.cloud.talent.v4.Job.DerivedInfo derived_info = 29 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Job.DerivedInfoOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job.DerivedInfoOrBuilder)` |   
  
### getDescription()
    
    
    public String getDescription()

Required. The description of the job, which typically includes a multi-paragraph description of the company and related information. Separate fields are provided on the job object for responsibilities, qualifications, and other job characteristics. Use of these separate job fields is recommended.

This field accepts and sanitizes HTML input, and also accepts bold, italic, ordered list, and unordered list markup tags.

The maximum number of allowed characters is 100,000.

`string description = 5 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The description.  
  
### getDescriptionBytes()
    
    
    public ByteString getDescriptionBytes()

Required. The description of the job, which typically includes a multi-paragraph description of the company and related information. Separate fields are provided on the job object for responsibilities, qualifications, and other job characteristics. Use of these separate job fields is recommended.

This field accepts and sanitizes HTML input, and also accepts bold, italic, ordered list, and unordered list markup tags.

The maximum number of allowed characters is 100,000.

`string description = 5 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for description.  
  
### getEmploymentTypes(int index)
    
    
    public EmploymentType getEmploymentTypes(int index)

The employment type(s) of a job, for example, full time or part time.

`repeated .google.cloud.talent.v4.EmploymentType employment_types = 13;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[EmploymentType](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.EmploymentType)` | The employmentTypes at the given index.  
  
### getEmploymentTypesCount()
    
    
    public int getEmploymentTypesCount()

The employment type(s) of a job, for example, full time or part time.

`repeated .google.cloud.talent.v4.EmploymentType employment_types = 13;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of employmentTypes.  
  
### getEmploymentTypesList()
    
    
    public List<EmploymentType> getEmploymentTypesList()

The employment type(s) of a job, for example, full time or part time.

`repeated .google.cloud.talent.v4.EmploymentType employment_types = 13;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[EmploymentType](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.EmploymentType)>` | A list containing the employmentTypes.  
  
### getEmploymentTypesValue(int index)
    
    
    public int getEmploymentTypesValue(int index)

The employment type(s) of a job, for example, full time or part time.

`repeated .google.cloud.talent.v4.EmploymentType employment_types = 13;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire of employmentTypes at the given index.  
  
### getEmploymentTypesValueList()
    
    
    public List<Integer> getEmploymentTypesValueList()

The employment type(s) of a job, for example, full time or part time.

`repeated .google.cloud.talent.v4.EmploymentType employment_types = 13;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)>` | A list containing the enum numeric values on the wire for employmentTypes.  
  
### getIncentives()
    
    
    public String getIncentives()

A description of bonus, commission, and other compensation incentives associated with the job not including salary or pay.

The maximum number of allowed characters is 10,000.

`string incentives = 14;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The incentives.  
  
### getIncentivesBytes()
    
    
    public ByteString getIncentivesBytes()

A description of bonus, commission, and other compensation incentives associated with the job not including salary or pay.

The maximum number of allowed characters is 10,000.

`string incentives = 14;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for incentives.  
  
### getJobBenefits(int index)
    
    
    public JobBenefit getJobBenefits(int index)

The benefits included with the job.

`repeated .google.cloud.talent.v4.JobBenefit job_benefits = 8;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[JobBenefit](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.JobBenefit)` | The jobBenefits at the given index.  
  
### getJobBenefitsCount()
    
    
    public int getJobBenefitsCount()

The benefits included with the job.

`repeated .google.cloud.talent.v4.JobBenefit job_benefits = 8;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of jobBenefits.  
  
### getJobBenefitsList()
    
    
    public List<JobBenefit> getJobBenefitsList()

The benefits included with the job.

`repeated .google.cloud.talent.v4.JobBenefit job_benefits = 8;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[JobBenefit](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.JobBenefit)>` | A list containing the jobBenefits.  
  
### getJobBenefitsValue(int index)
    
    
    public int getJobBenefitsValue(int index)

The benefits included with the job.

`repeated .google.cloud.talent.v4.JobBenefit job_benefits = 8;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire of jobBenefits at the given index.  
  
### getJobBenefitsValueList()
    
    
    public List<Integer> getJobBenefitsValueList()

The benefits included with the job.

`repeated .google.cloud.talent.v4.JobBenefit job_benefits = 8;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)>` | A list containing the enum numeric values on the wire for jobBenefits.  
  
### getJobEndTime()
    
    
    public Timestamp getJobEndTime()

The end timestamp of the job. Typically this field is used for contracting engagements. Invalid timestamps are ignored.

`.google.protobuf.Timestamp job_end_time = 23;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The jobEndTime.  
  
### getJobEndTimeOrBuilder()
    
    
    public TimestampOrBuilder getJobEndTimeOrBuilder()

The end timestamp of the job. Typically this field is used for contracting engagements. Invalid timestamps are ignored.

`.google.protobuf.Timestamp job_end_time = 23;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getJobLevel()
    
    
    public JobLevel getJobLevel()

The experience level associated with the job, such as "Entry Level".

`.google.cloud.talent.v4.JobLevel job_level = 16;`

**Returns**  
---  
**Type** | **Description**  
`[JobLevel](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.JobLevel)` | The jobLevel.  
  
### getJobLevelValue()
    
    
    public int getJobLevelValue()

The experience level associated with the job, such as "Entry Level".

`.google.cloud.talent.v4.JobLevel job_level = 16;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for jobLevel.  
  
### getJobStartTime()
    
    
    public Timestamp getJobStartTime()

The start timestamp of the job in UTC time zone. Typically this field is used for contracting engagements. Invalid timestamps are ignored.

`.google.protobuf.Timestamp job_start_time = 22;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The jobStartTime.  
  
### getJobStartTimeOrBuilder()
    
    
    public TimestampOrBuilder getJobStartTimeOrBuilder()

The start timestamp of the job in UTC time zone. Typically this field is used for contracting engagements. Invalid timestamps are ignored.

`.google.protobuf.Timestamp job_start_time = 22;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getLanguageCode()
    
    
    public String getLanguageCode()

The language of the posting. This field is distinct from any requirements for fluency that are associated with the job.

Language codes must be in BCP-47 format, such as "en-US" or "sr-Latn". For more information, see [Tags for Identifying Languages](https://tools.ietf.org/html/bcp47){: class="external" target="_blank" }.

If this field is unspecified and Job.description is present, detected language code based on Job.description is assigned, otherwise defaults to 'en_US'.

`string language_code = 15;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The languageCode.  
  
### getLanguageCodeBytes()
    
    
    public ByteString getLanguageCodeBytes()

The language of the posting. This field is distinct from any requirements for fluency that are associated with the job.

Language codes must be in BCP-47 format, such as "en-US" or "sr-Latn". For more information, see [Tags for Identifying Languages](https://tools.ietf.org/html/bcp47){: class="external" target="_blank" }.

If this field is unspecified and Job.description is present, detected language code based on Job.description is assigned, otherwise defaults to 'en_US'.

`string language_code = 15;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for languageCode.  
  
### getName()
    
    
    public String getName()

Required during job update.

The resource name for the job. This is generated by the service when a job is created.

The format is "projects/{project_id}/tenants/{tenant_id}/jobs/{job_id}". For example, "projects/foo/tenants/bar/jobs/baz".

Use of this field in job queries and API calls is preferred over the use of requisition_id since this value is unique.

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public ByteString getNameBytes()

Required during job update.

The resource name for the job. This is generated by the service when a job is created.

The format is "projects/{project_id}/tenants/{tenant_id}/jobs/{job_id}". For example, "projects/foo/tenants/bar/jobs/baz".

Use of this field in job queries and API calls is preferred over the use of requisition_id since this value is unique.

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getParserForType()
    
    
    public Parser<Job> getParserForType()

**Returns**  
---  
**Type** | **Description**  
`[Parser](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Parser.html)<[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job)>` |   
**Overrides**

[GeneratedMessage.getParserForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_getParserForType__)

### getPostingCreateTime()
    
    
    public Timestamp getPostingCreateTime()

Output only. The timestamp when this job posting was created.

` .google.protobuf.Timestamp posting_create_time = 26 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The postingCreateTime.  
  
### getPostingCreateTimeOrBuilder()
    
    
    public TimestampOrBuilder getPostingCreateTimeOrBuilder()

Output only. The timestamp when this job posting was created.

` .google.protobuf.Timestamp posting_create_time = 26 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getPostingExpireTime()
    
    
    public Timestamp getPostingExpireTime()

Strongly recommended for the best service experience.

The expiration timestamp of the job. After this timestamp, the job is marked as expired, and it no longer appears in search results. The expired job can't be listed by the ListJobs API, but it can be retrieved with the GetJob API or updated with the UpdateJob API or deleted with the DeleteJob API. An expired job can be updated and opened again by using a future expiration timestamp. Updating an expired job fails if there is another existing open job with same company, language_code and requisition_id.

The expired jobs are retained in our system for 90 days. However, the overall expired job count cannot exceed 3 times the maximum number of open jobs over previous 7 days. If this threshold is exceeded, expired jobs are cleaned out in order of earliest expire time. Expired jobs are no longer accessible after they are cleaned out.

Invalid timestamps are ignored, and treated as expire time not provided.

If the timestamp is before the instant request is made, the job is treated as expired immediately on creation. This kind of job can not be updated. And when creating a job with past timestamp, the posting_publish_time must be set before posting_expire_time. The purpose of this feature is to allow other objects, such as ApplicationInfo, to refer a job that didn't exist in the system prior to becoming expired. If you want to modify a job that was expired on creation, delete it and create a new one.

If this value isn't provided at the time of job creation or is invalid, the job posting expires after 30 days from the job's creation time. For example, if the job was created on 2017/01/01 13:00AM UTC with an unspecified expiration date, the job expires after 2017/01/31 13:00AM UTC.

If this value isn't provided on job update, it depends on the field masks set by UpdateJobRequest.update_mask. If the field masks include job_end_time, or the masks are empty meaning that every field is updated, the job posting expires after 30 days from the job's last update time. Otherwise the expiration date isn't updated.

`.google.protobuf.Timestamp posting_expire_time = 25;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The postingExpireTime.  
  
### getPostingExpireTimeOrBuilder()
    
    
    public TimestampOrBuilder getPostingExpireTimeOrBuilder()

Strongly recommended for the best service experience.

The expiration timestamp of the job. After this timestamp, the job is marked as expired, and it no longer appears in search results. The expired job can't be listed by the ListJobs API, but it can be retrieved with the GetJob API or updated with the UpdateJob API or deleted with the DeleteJob API. An expired job can be updated and opened again by using a future expiration timestamp. Updating an expired job fails if there is another existing open job with same company, language_code and requisition_id.

The expired jobs are retained in our system for 90 days. However, the overall expired job count cannot exceed 3 times the maximum number of open jobs over previous 7 days. If this threshold is exceeded, expired jobs are cleaned out in order of earliest expire time. Expired jobs are no longer accessible after they are cleaned out.

Invalid timestamps are ignored, and treated as expire time not provided.

If the timestamp is before the instant request is made, the job is treated as expired immediately on creation. This kind of job can not be updated. And when creating a job with past timestamp, the posting_publish_time must be set before posting_expire_time. The purpose of this feature is to allow other objects, such as ApplicationInfo, to refer a job that didn't exist in the system prior to becoming expired. If you want to modify a job that was expired on creation, delete it and create a new one.

If this value isn't provided at the time of job creation or is invalid, the job posting expires after 30 days from the job's creation time. For example, if the job was created on 2017/01/01 13:00AM UTC with an unspecified expiration date, the job expires after 2017/01/31 13:00AM UTC.

If this value isn't provided on job update, it depends on the field masks set by UpdateJobRequest.update_mask. If the field masks include job_end_time, or the masks are empty meaning that every field is updated, the job posting expires after 30 days from the job's last update time. Otherwise the expiration date isn't updated.

`.google.protobuf.Timestamp posting_expire_time = 25;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getPostingPublishTime()
    
    
    public Timestamp getPostingPublishTime()

The timestamp this job posting was most recently published. The default value is the time the request arrives at the server. Invalid timestamps are ignored.

`.google.protobuf.Timestamp posting_publish_time = 24;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The postingPublishTime.  
  
### getPostingPublishTimeOrBuilder()
    
    
    public TimestampOrBuilder getPostingPublishTimeOrBuilder()

The timestamp this job posting was most recently published. The default value is the time the request arrives at the server. Invalid timestamps are ignored.

`.google.protobuf.Timestamp posting_publish_time = 24;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getPostingRegion()
    
    
    public PostingRegion getPostingRegion()

The job PostingRegion (for example, state, country) throughout which the job is available. If this field is set, a LocationFilter in a search query within the job region finds this job posting if an exact location match isn't specified. If this field is set to PostingRegion.NATION or PostingRegion.ADMINISTRATIVE_AREA, setting job Job.addresses to the same location level as this field is strongly recommended.

`.google.cloud.talent.v4.PostingRegion posting_region = 20;`

**Returns**  
---  
**Type** | **Description**  
`[PostingRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.PostingRegion)` | The postingRegion.  
  
### getPostingRegionValue()
    
    
    public int getPostingRegionValue()

The job PostingRegion (for example, state, country) throughout which the job is available. If this field is set, a LocationFilter in a search query within the job region finds this job posting if an exact location match isn't specified. If this field is set to PostingRegion.NATION or PostingRegion.ADMINISTRATIVE_AREA, setting job Job.addresses to the same location level as this field is strongly recommended.

`.google.cloud.talent.v4.PostingRegion posting_region = 20;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for postingRegion.  
  
### getPostingUpdateTime()
    
    
    public Timestamp getPostingUpdateTime()

Output only. The timestamp when this job posting was last updated.

` .google.protobuf.Timestamp posting_update_time = 27 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The postingUpdateTime.  
  
### getPostingUpdateTimeOrBuilder()
    
    
    public TimestampOrBuilder getPostingUpdateTimeOrBuilder()

Output only. The timestamp when this job posting was last updated.

` .google.protobuf.Timestamp posting_update_time = 27 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getProcessingOptions()
    
    
    public Job.ProcessingOptions getProcessingOptions()

Options for job processing.

`.google.cloud.talent.v4.Job.ProcessingOptions processing_options = 30;`

**Returns**  
---  
**Type** | **Description**  
`[Job.ProcessingOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job.ProcessingOptions)` | The processingOptions.  
  
### getProcessingOptionsOrBuilder()
    
    
    public Job.ProcessingOptionsOrBuilder getProcessingOptionsOrBuilder()

Options for job processing.

`.google.cloud.talent.v4.Job.ProcessingOptions processing_options = 30;`

**Returns**  
---  
**Type** | **Description**  
`[Job.ProcessingOptionsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job.ProcessingOptionsOrBuilder)` |   
  
### getPromotionValue()
    
    
    public int getPromotionValue()

A promotion value of the job, as determined by the client. The value determines the sort order of the jobs returned when searching for jobs using the featured jobs search call, with higher promotional values being returned first and ties being resolved by relevance sort. Only the jobs with a promotionValue >0 are returned in a FEATURED_JOB_SEARCH.

Default value is 0, and negative values are treated as 0.

`int32 promotion_value = 17;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The promotionValue.  
  
### getQualifications()
    
    
    public String getQualifications()

A description of the qualifications required to perform the job. The use of this field is recommended as an alternative to using the more general description field.

This field accepts and sanitizes HTML input, and also accepts bold, italic, ordered list, and unordered list markup tags.

The maximum number of allowed characters is 10,000.

`string qualifications = 18;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The qualifications.  
  
### getQualificationsBytes()
    
    
    public ByteString getQualificationsBytes()

A description of the qualifications required to perform the job. The use of this field is recommended as an alternative to using the more general description field.

This field accepts and sanitizes HTML input, and also accepts bold, italic, ordered list, and unordered list markup tags.

The maximum number of allowed characters is 10,000.

`string qualifications = 18;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for qualifications.  
  
### getRequisitionId()
    
    
    public String getRequisitionId()

Required. The requisition ID, also referred to as the posting ID, is assigned by the client to identify a job. This field is intended to be used by clients for client identification and tracking of postings. A job isn't allowed to be created if there is another job with the same company, language_code and requisition_id.

The maximum number of allowed characters is 255.

`string requisition_id = 3 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The requisitionId.  
  
### getRequisitionIdBytes()
    
    
    public ByteString getRequisitionIdBytes()

Required. The requisition ID, also referred to as the posting ID, is assigned by the client to identify a job. This field is intended to be used by clients for client identification and tracking of postings. A job isn't allowed to be created if there is another job with the same company, language_code and requisition_id.

The maximum number of allowed characters is 255.

`string requisition_id = 3 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for requisitionId.  
  
### getResponsibilities()
    
    
    public String getResponsibilities()

A description of job responsibilities. The use of this field is recommended as an alternative to using the more general description field.

This field accepts and sanitizes HTML input, and also accepts bold, italic, ordered list, and unordered list markup tags.

The maximum number of allowed characters is 10,000.

`string responsibilities = 19;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The responsibilities.  
  
### getResponsibilitiesBytes()
    
    
    public ByteString getResponsibilitiesBytes()

A description of job responsibilities. The use of this field is recommended as an alternative to using the more general description field.

This field accepts and sanitizes HTML input, and also accepts bold, italic, ordered list, and unordered list markup tags.

The maximum number of allowed characters is 10,000.

`string responsibilities = 19;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for responsibilities.  
  
### getSerializedSize()
    
    
    public int getSerializedSize()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[GeneratedMessage.getSerializedSize()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_getSerializedSize__)

### getTitle()
    
    
    public String getTitle()

Required. The title of the job, such as "Software Engineer"

The maximum number of allowed characters is 500.

`string title = 4 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The title.  
  
### getTitleBytes()
    
    
    public ByteString getTitleBytes()

Required. The title of the job, such as "Software Engineer"

The maximum number of allowed characters is 500.

`string title = 4 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for title.  
  
### getVisibility() (deprecated)
    
    
    public Visibility getVisibility()

**Deprecated.** _google.cloud.talent.v4.Job.visibility is deprecated. See google/cloud/talent/v4/job.proto;l=298_

Deprecated. The job is only visible to the owner.

The visibility of the job.

Defaults to Visibility.ACCOUNT_ONLY if not specified.

`.google.cloud.talent.v4.Visibility visibility = 21 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[Visibility](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Visibility)` | The visibility.  
  
### getVisibilityValue() (deprecated)
    
    
    public int getVisibilityValue()

**Deprecated.** _google.cloud.talent.v4.Job.visibility is deprecated. See google/cloud/talent/v4/job.proto;l=298_

Deprecated. The job is only visible to the owner.

The visibility of the job.

Defaults to Visibility.ACCOUNT_ONLY if not specified.

`.google.cloud.talent.v4.Visibility visibility = 21 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for visibility.  
  
### hasApplicationInfo()
    
    
    public boolean hasApplicationInfo()

Job application information.

`.google.cloud.talent.v4.Job.ApplicationInfo application_info = 7;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the applicationInfo field is set.  
  
### hasCompensationInfo()
    
    
    public boolean hasCompensationInfo()

Job compensation information (a.k.a. "pay rate") i.e., the compensation that will paid to the employee.

`.google.cloud.talent.v4.CompensationInfo compensation_info = 9;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the compensationInfo field is set.  
  
### hasDerivedInfo()
    
    
    public boolean hasDerivedInfo()

Output only. Derived details about the job posting.

` .google.cloud.talent.v4.Job.DerivedInfo derived_info = 29 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the derivedInfo field is set.  
  
### hasJobEndTime()
    
    
    public boolean hasJobEndTime()

The end timestamp of the job. Typically this field is used for contracting engagements. Invalid timestamps are ignored.

`.google.protobuf.Timestamp job_end_time = 23;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the jobEndTime field is set.  
  
### hasJobStartTime()
    
    
    public boolean hasJobStartTime()

The start timestamp of the job in UTC time zone. Typically this field is used for contracting engagements. Invalid timestamps are ignored.

`.google.protobuf.Timestamp job_start_time = 22;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the jobStartTime field is set.  
  
### hasPostingCreateTime()
    
    
    public boolean hasPostingCreateTime()

Output only. The timestamp when this job posting was created.

` .google.protobuf.Timestamp posting_create_time = 26 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the postingCreateTime field is set.  
  
### hasPostingExpireTime()
    
    
    public boolean hasPostingExpireTime()

Strongly recommended for the best service experience.

The expiration timestamp of the job. After this timestamp, the job is marked as expired, and it no longer appears in search results. The expired job can't be listed by the ListJobs API, but it can be retrieved with the GetJob API or updated with the UpdateJob API or deleted with the DeleteJob API. An expired job can be updated and opened again by using a future expiration timestamp. Updating an expired job fails if there is another existing open job with same company, language_code and requisition_id.

The expired jobs are retained in our system for 90 days. However, the overall expired job count cannot exceed 3 times the maximum number of open jobs over previous 7 days. If this threshold is exceeded, expired jobs are cleaned out in order of earliest expire time. Expired jobs are no longer accessible after they are cleaned out.

Invalid timestamps are ignored, and treated as expire time not provided.

If the timestamp is before the instant request is made, the job is treated as expired immediately on creation. This kind of job can not be updated. And when creating a job with past timestamp, the posting_publish_time must be set before posting_expire_time. The purpose of this feature is to allow other objects, such as ApplicationInfo, to refer a job that didn't exist in the system prior to becoming expired. If you want to modify a job that was expired on creation, delete it and create a new one.

If this value isn't provided at the time of job creation or is invalid, the job posting expires after 30 days from the job's creation time. For example, if the job was created on 2017/01/01 13:00AM UTC with an unspecified expiration date, the job expires after 2017/01/31 13:00AM UTC.

If this value isn't provided on job update, it depends on the field masks set by UpdateJobRequest.update_mask. If the field masks include job_end_time, or the masks are empty meaning that every field is updated, the job posting expires after 30 days from the job's last update time. Otherwise the expiration date isn't updated.

`.google.protobuf.Timestamp posting_expire_time = 25;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the postingExpireTime field is set.  
  
### hasPostingPublishTime()
    
    
    public boolean hasPostingPublishTime()

The timestamp this job posting was most recently published. The default value is the time the request arrives at the server. Invalid timestamps are ignored.

`.google.protobuf.Timestamp posting_publish_time = 24;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the postingPublishTime field is set.  
  
### hasPostingUpdateTime()
    
    
    public boolean hasPostingUpdateTime()

Output only. The timestamp when this job posting was last updated.

` .google.protobuf.Timestamp posting_update_time = 27 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the postingUpdateTime field is set.  
  
### hasProcessingOptions()
    
    
    public boolean hasProcessingOptions()

Options for job processing.

`.google.cloud.talent.v4.Job.ProcessingOptions processing_options = 30;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the processingOptions field is set.  
  
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
    
    
    public Job.Builder newBuilderForType()

**Returns**  
---  
**Type** | **Description**  
`[Job.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job.Builder)` |   
  
### newBuilderForType(AbstractMessage.BuilderParent parent)
    
    
    protected Job.Builder newBuilderForType(AbstractMessage.BuilderParent parent)

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[BuilderParent](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.BuilderParent.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Job.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job.Builder)` |   
**Overrides**

[AbstractMessage.newBuilderForType(AbstractMessage.BuilderParent parent)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.html#com_google_protobuf_AbstractMessage_newBuilderForType_com_google_protobuf_AbstractMessage_BuilderParent_)

### toBuilder()
    
    
    public Job.Builder toBuilder()

**Returns**  
---  
**Type** | **Description**  
`[Job.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job.Builder)` |   
  
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
