---
url: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reports/latest/com.google.shopping.merchant.reports.v1alpha.ProductView
title: Class ProductView (1.27.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:51:28.205904+00:00
---

# Class ProductView (1.27.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reports/latest/com.google.shopping.merchant.reports.v1alpha.ProductView

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ProductView (1.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.27.0 (latest)  1.23.0  1.22.0  1.21.0  1.19.0  1.16.0  1.15.0  1.13.0  1.11.0  1.10.0  1.8.0  1.6.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.46.0  0.44.0  0.43.0  0.40.0  0.39.0  0.38.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0 
    
    
    public final class ProductView extends GeneratedMessage implements ProductViewOrBuilder

Fields available for query in `product_view` table.

Products in the current inventory. Products in this table are the same as in Products sub-API but not all product attributes from Products sub-API are available for query in this table. In contrast to Products sub-API, this table allows to filter the returned list of products by product attributes. To retrieve a single product by `id` or list all products, Products sub-API should be used.

Values are only set for fields requested explicitly in the request's search query.

Protobuf type `google.shopping.merchant.reports.v1alpha.ProductView`

## Inheritance

[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.html) > [AbstractMessage](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.html) > [GeneratedMessage](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html) > ProductView

## Implements

[ProductViewOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reports/latest/com.google.shopping.merchant.reports.v1alpha.ProductViewOrBuilder)

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

### AGGREGATED_REPORTING_CONTEXT_STATUS_FIELD_NUMBER
    
    
    public static final int AGGREGATED_REPORTING_CONTEXT_STATUS_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### AVAILABILITY_FIELD_NUMBER
    
    
    public static final int AVAILABILITY_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### BRAND_FIELD_NUMBER
    
    
    public static final int BRAND_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### CATEGORY_L1_FIELD_NUMBER
    
    
    public static final int CATEGORY_L1_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### CATEGORY_L2_FIELD_NUMBER
    
    
    public static final int CATEGORY_L2_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### CATEGORY_L3_FIELD_NUMBER
    
    
    public static final int CATEGORY_L3_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### CATEGORY_L4_FIELD_NUMBER
    
    
    public static final int CATEGORY_L4_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### CATEGORY_L5_FIELD_NUMBER
    
    
    public static final int CATEGORY_L5_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### CHANNEL_FIELD_NUMBER
    
    
    public static final int CHANNEL_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### CLICK_POTENTIAL_FIELD_NUMBER
    
    
    public static final int CLICK_POTENTIAL_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### CLICK_POTENTIAL_RANK_FIELD_NUMBER
    
    
    public static final int CLICK_POTENTIAL_RANK_FIELD_NUMBER

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
  
### CREATION_TIME_FIELD_NUMBER
    
    
    public static final int CREATION_TIME_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### EXPIRATION_DATE_FIELD_NUMBER
    
    
    public static final int EXPIRATION_DATE_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### FEED_LABEL_FIELD_NUMBER
    
    
    public static final int FEED_LABEL_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### GTIN_FIELD_NUMBER
    
    
    public static final int GTIN_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### ID_FIELD_NUMBER
    
    
    public static final int ID_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### ITEM_GROUP_ID_FIELD_NUMBER
    
    
    public static final int ITEM_GROUP_ID_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### ITEM_ISSUES_FIELD_NUMBER
    
    
    public static final int ITEM_ISSUES_FIELD_NUMBER

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
  
### OFFER_ID_FIELD_NUMBER
    
    
    public static final int OFFER_ID_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### PRICE_FIELD_NUMBER
    
    
    public static final int PRICE_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### PRODUCT_TYPE_L1_FIELD_NUMBER
    
    
    public static final int PRODUCT_TYPE_L1_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### PRODUCT_TYPE_L2_FIELD_NUMBER
    
    
    public static final int PRODUCT_TYPE_L2_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### PRODUCT_TYPE_L3_FIELD_NUMBER
    
    
    public static final int PRODUCT_TYPE_L3_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### PRODUCT_TYPE_L4_FIELD_NUMBER
    
    
    public static final int PRODUCT_TYPE_L4_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### PRODUCT_TYPE_L5_FIELD_NUMBER
    
    
    public static final int PRODUCT_TYPE_L5_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### SHIPPING_LABEL_FIELD_NUMBER
    
    
    public static final int SHIPPING_LABEL_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### THUMBNAIL_LINK_FIELD_NUMBER
    
    
    public static final int THUMBNAIL_LINK_FIELD_NUMBER

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
  
## Static Methods 

### getDefaultInstance()
    
    
    public static ProductView getDefaultInstance()

**Returns**  
---  
**Type** | **Description**  
`[ProductView](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reports/latest/com.google.shopping.merchant.reports.v1alpha.ProductView)` |   
  
### getDescriptor()
    
    
    public static final Descriptors.Descriptor getDescriptor()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
  
### newBuilder()
    
    
    public static ProductView.Builder newBuilder()

**Returns**  
---  
**Type** | **Description**  
`[ProductView.Builder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reports/latest/com.google.shopping.merchant.reports.v1alpha.ProductView.Builder)` |   
  
### newBuilder(ProductView prototype)
    
    
    public static ProductView.Builder newBuilder(ProductView prototype)

**Parameter**  
---  
**Name** | **Description**  
`prototype` | `[ProductView](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reports/latest/com.google.shopping.merchant.reports.v1alpha.ProductView)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProductView.Builder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reports/latest/com.google.shopping.merchant.reports.v1alpha.ProductView.Builder)` |   
  
### parseDelimitedFrom(InputStream input)
    
    
    public static ProductView parseDelimitedFrom(InputStream input)

**Parameter**  
---  
**Name** | **Description**  
`input` | `[InputStream](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProductView](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reports/latest/com.google.shopping.merchant.reports.v1alpha.ProductView)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseDelimitedFrom(InputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public static ProductView parseDelimitedFrom(InputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[InputStream](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProductView](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reports/latest/com.google.shopping.merchant.reports.v1alpha.ProductView)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseFrom(byte[] data)
    
    
    public static ProductView parseFrom(byte[] data)

**Parameter**  
---  
**Name** | **Description**  
`data` | `byte[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProductView](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reports/latest/com.google.shopping.merchant.reports.v1alpha.ProductView)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parseFrom(byte[] data, ExtensionRegistryLite extensionRegistry)
    
    
    public static ProductView parseFrom(byte[] data, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`data` | `byte[]`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProductView](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reports/latest/com.google.shopping.merchant.reports.v1alpha.ProductView)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parseFrom(ByteString data)
    
    
    public static ProductView parseFrom(ByteString data)

**Parameter**  
---  
**Name** | **Description**  
`data` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProductView](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reports/latest/com.google.shopping.merchant.reports.v1alpha.ProductView)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parseFrom(ByteString data, ExtensionRegistryLite extensionRegistry)
    
    
    public static ProductView parseFrom(ByteString data, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`data` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProductView](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reports/latest/com.google.shopping.merchant.reports.v1alpha.ProductView)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parseFrom(CodedInputStream input)
    
    
    public static ProductView parseFrom(CodedInputStream input)

**Parameter**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProductView](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reports/latest/com.google.shopping.merchant.reports.v1alpha.ProductView)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public static ProductView parseFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProductView](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reports/latest/com.google.shopping.merchant.reports.v1alpha.ProductView)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseFrom(InputStream input)
    
    
    public static ProductView parseFrom(InputStream input)

**Parameter**  
---  
**Name** | **Description**  
`input` | `[InputStream](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProductView](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reports/latest/com.google.shopping.merchant.reports.v1alpha.ProductView)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseFrom(InputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public static ProductView parseFrom(InputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[InputStream](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProductView](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reports/latest/com.google.shopping.merchant.reports.v1alpha.ProductView)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseFrom(ByteBuffer data)
    
    
    public static ProductView parseFrom(ByteBuffer data)

**Parameter**  
---  
**Name** | **Description**  
`data` | `[ByteBuffer](https://docs.oracle.com/javase/8/docs/api/java/nio/ByteBuffer.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProductView](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reports/latest/com.google.shopping.merchant.reports.v1alpha.ProductView)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parseFrom(ByteBuffer data, ExtensionRegistryLite extensionRegistry)
    
    
    public static ProductView parseFrom(ByteBuffer data, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`data` | `[ByteBuffer](https://docs.oracle.com/javase/8/docs/api/java/nio/ByteBuffer.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProductView](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reports/latest/com.google.shopping.merchant.reports.v1alpha.ProductView)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parser()
    
    
    public static Parser<ProductView> parser()

**Returns**  
---  
**Type** | **Description**  
`[Parser](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Parser.html)<[ProductView](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reports/latest/com.google.shopping.merchant.reports.v1alpha.ProductView)>` |   
  
## Methods 

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

### getAggregatedReportingContextStatus()
    
    
    public ProductView.AggregatedReportingContextStatus getAggregatedReportingContextStatus()

Aggregated status.

` optional .google.shopping.merchant.reports.v1alpha.ProductView.AggregatedReportingContextStatus aggregated_reporting_context_status = 26; `

**Returns**  
---  
**Type** | **Description**  
`[ProductView.AggregatedReportingContextStatus](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reports/latest/com.google.shopping.merchant.reports.v1alpha.ProductView.AggregatedReportingContextStatus)` | The aggregatedReportingContextStatus.  
  
### getAggregatedReportingContextStatusValue()
    
    
    public int getAggregatedReportingContextStatusValue()

Aggregated status.

` optional .google.shopping.merchant.reports.v1alpha.ProductView.AggregatedReportingContextStatus aggregated_reporting_context_status = 26; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for aggregatedReportingContextStatus.  
  
### getAvailability()
    
    
    public String getAvailability()

[Availability](https://support.google.com/merchants/answer/6324448) of the product.

`optional string availability = 19;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The availability.  
  
### getAvailabilityBytes()
    
    
    public ByteString getAvailabilityBytes()

[Availability](https://support.google.com/merchants/answer/6324448) of the product.

`optional string availability = 19;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for availability.  
  
### getBrand()
    
    
    public String getBrand()

Brand of the product.

`optional string brand = 6;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The brand.  
  
### getBrandBytes()
    
    
    public ByteString getBrandBytes()

Brand of the product.

`optional string brand = 6;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for brand.  
  
### getCategoryL1()
    
    
    public String getCategoryL1()

Product category (1st level) in [Google's product taxonomy](https://support.google.com/merchants/answer/6324436).

`optional string category_l1 = 7;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The categoryL1.  
  
### getCategoryL1Bytes()
    
    
    public ByteString getCategoryL1Bytes()

Product category (1st level) in [Google's product taxonomy](https://support.google.com/merchants/answer/6324436).

`optional string category_l1 = 7;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for categoryL1.  
  
### getCategoryL2()
    
    
    public String getCategoryL2()

Product category (2nd level) in [Google's product taxonomy](https://support.google.com/merchants/answer/6324436).

`optional string category_l2 = 8;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The categoryL2.  
  
### getCategoryL2Bytes()
    
    
    public ByteString getCategoryL2Bytes()

Product category (2nd level) in [Google's product taxonomy](https://support.google.com/merchants/answer/6324436).

`optional string category_l2 = 8;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for categoryL2.  
  
### getCategoryL3()
    
    
    public String getCategoryL3()

Product category (3rd level) in [Google's product taxonomy](https://support.google.com/merchants/answer/6324436).

`optional string category_l3 = 9;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The categoryL3.  
  
### getCategoryL3Bytes()
    
    
    public ByteString getCategoryL3Bytes()

Product category (3rd level) in [Google's product taxonomy](https://support.google.com/merchants/answer/6324436).

`optional string category_l3 = 9;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for categoryL3.  
  
### getCategoryL4()
    
    
    public String getCategoryL4()

Product category (4th level) in [Google's product taxonomy](https://support.google.com/merchants/answer/6324436).

`optional string category_l4 = 10;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The categoryL4.  
  
### getCategoryL4Bytes()
    
    
    public ByteString getCategoryL4Bytes()

Product category (4th level) in [Google's product taxonomy](https://support.google.com/merchants/answer/6324436).

`optional string category_l4 = 10;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for categoryL4.  
  
### getCategoryL5()
    
    
    public String getCategoryL5()

Product category (5th level) in [Google's product taxonomy](https://support.google.com/merchants/answer/6324436).

`optional string category_l5 = 11;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The categoryL5.  
  
### getCategoryL5Bytes()
    
    
    public ByteString getCategoryL5Bytes()

Product category (5th level) in [Google's product taxonomy](https://support.google.com/merchants/answer/6324436).

`optional string category_l5 = 11;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for categoryL5.  
  
### getChannel()
    
    
    public Channel.ChannelEnum getChannel()

Channel of the product. Can be `ONLINE` or `LOCAL`.

`optional .google.shopping.type.Channel.ChannelEnum channel = 28;`

**Returns**  
---  
**Type** | **Description**  
`com.google.shopping.type.Channel.ChannelEnum` | The channel.  
  
### getChannelValue()
    
    
    public int getChannelValue()

Channel of the product. Can be `ONLINE` or `LOCAL`.

`optional .google.shopping.type.Channel.ChannelEnum channel = 28;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for channel.  
  
### getClickPotential()
    
    
    public ProductView.ClickPotential getClickPotential()

Estimated performance potential compared to highest performing products of the merchant.

` .google.shopping.merchant.reports.v1alpha.ProductView.ClickPotential click_potential = 29; `

**Returns**  
---  
**Type** | **Description**  
`[ProductView.ClickPotential](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reports/latest/com.google.shopping.merchant.reports.v1alpha.ProductView.ClickPotential)` | The clickPotential.  
  
### getClickPotentialRank()
    
    
    public long getClickPotentialRank()

Rank of the product based on its click potential. A product with `click_potential_rank` 1 has the highest click potential among the merchant's products that fulfill the search query conditions.

`optional int64 click_potential_rank = 30;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The clickPotentialRank.  
  
### getClickPotentialValue()
    
    
    public int getClickPotentialValue()

Estimated performance potential compared to highest performing products of the merchant.

` .google.shopping.merchant.reports.v1alpha.ProductView.ClickPotential click_potential = 29; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for clickPotential.  
  
### getCondition()
    
    
    public String getCondition()

[Condition](https://support.google.com/merchants/answer/6324469) of the product.

`optional string condition = 18;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The condition.  
  
### getConditionBytes()
    
    
    public ByteString getConditionBytes()

[Condition](https://support.google.com/merchants/answer/6324469) of the product.

`optional string condition = 18;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for condition.  
  
### getCreationTime()
    
    
    public Timestamp getCreationTime()

The time the merchant created the product in timestamp seconds.

`.google.protobuf.Timestamp creation_time = 24;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The creationTime.  
  
### getCreationTimeOrBuilder()
    
    
    public TimestampOrBuilder getCreationTimeOrBuilder()

The time the merchant created the product in timestamp seconds.

`.google.protobuf.Timestamp creation_time = 24;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDefaultInstanceForType()
    
    
    public ProductView getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[ProductView](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reports/latest/com.google.shopping.merchant.reports.v1alpha.ProductView)` |   
  
### getExpirationDate()
    
    
    public Date getExpirationDate()

Expiration date for the product, specified on insertion.

`.google.type.Date expiration_date = 25;`

**Returns**  
---  
**Type** | **Description**  
`com.google.type.Date` | The expirationDate.  
  
### getExpirationDateOrBuilder()
    
    
    public DateOrBuilder getExpirationDateOrBuilder()

Expiration date for the product, specified on insertion.

`.google.type.Date expiration_date = 25;`

**Returns**  
---  
**Type** | **Description**  
`com.google.type.DateOrBuilder` |   
  
### getFeedLabel()
    
    
    public String getFeedLabel()

Feed label of the product.

`optional string feed_label = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The feedLabel.  
  
### getFeedLabelBytes()
    
    
    public ByteString getFeedLabelBytes()

Feed label of the product.

`optional string feed_label = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for feedLabel.  
  
### getGtin(int index)
    
    
    public String getGtin(int index)

List of Global Trade Item Numbers (GTINs) of the product.

`repeated string gtin = 21;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The gtin at the given index.  
  
### getGtinBytes(int index)
    
    
    public ByteString getGtinBytes(int index)

List of Global Trade Item Numbers (GTINs) of the product.

`repeated string gtin = 21;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the gtin at the given index.  
  
### getGtinCount()
    
    
    public int getGtinCount()

List of Global Trade Item Numbers (GTINs) of the product.

`repeated string gtin = 21;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of gtin.  
  
### getGtinList()
    
    
    public ProtocolStringList getGtinList()

List of Global Trade Item Numbers (GTINs) of the product.

`repeated string gtin = 21;`

**Returns**  
---  
**Type** | **Description**  
`[ProtocolStringList](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ProtocolStringList.html)` | A list containing the gtin.  
  
### getId()
    
    
    public String getId()

REST ID of the product, in the form of `channel~languageCode~feedLabel~offerId`. Merchant API methods that operate on products take this as their `name` parameter.

Required in the `SELECT` clause.

`optional string id = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The id.  
  
### getIdBytes()
    
    
    public ByteString getIdBytes()

REST ID of the product, in the form of `channel~languageCode~feedLabel~offerId`. Merchant API methods that operate on products take this as their `name` parameter.

Required in the `SELECT` clause.

`optional string id = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for id.  
  
### getItemGroupId()
    
    
    public String getItemGroupId()

Item group id provided by the merchant for grouping variants together.

`optional string item_group_id = 22;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The itemGroupId.  
  
### getItemGroupIdBytes()
    
    
    public ByteString getItemGroupIdBytes()

Item group id provided by the merchant for grouping variants together.

`optional string item_group_id = 22;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for itemGroupId.  
  
### getItemIssues(int index)
    
    
    public ProductView.ItemIssue getItemIssues(int index)

List of item issues for the product.

**This field cannot be used for sorting the results.**

**Only selected attributes of this field (for example,`item_issues.severity.aggregated_severity`) can be used for filtering the results.**

` repeated .google.shopping.merchant.reports.v1alpha.ProductView.ItemIssue item_issues = 27; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProductView.ItemIssue](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reports/latest/com.google.shopping.merchant.reports.v1alpha.ProductView.ItemIssue)` |   
  
### getItemIssuesCount()
    
    
    public int getItemIssuesCount()

List of item issues for the product.

**This field cannot be used for sorting the results.**

**Only selected attributes of this field (for example,`item_issues.severity.aggregated_severity`) can be used for filtering the results.**

` repeated .google.shopping.merchant.reports.v1alpha.ProductView.ItemIssue item_issues = 27; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getItemIssuesList()
    
    
    public List<ProductView.ItemIssue> getItemIssuesList()

List of item issues for the product.

**This field cannot be used for sorting the results.**

**Only selected attributes of this field (for example,`item_issues.severity.aggregated_severity`) can be used for filtering the results.**

` repeated .google.shopping.merchant.reports.v1alpha.ProductView.ItemIssue item_issues = 27; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ItemIssue](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reports/latest/com.google.shopping.merchant.reports.v1alpha.ProductView.ItemIssue)>` |   
  
### getItemIssuesOrBuilder(int index)
    
    
    public ProductView.ItemIssueOrBuilder getItemIssuesOrBuilder(int index)

List of item issues for the product.

**This field cannot be used for sorting the results.**

**Only selected attributes of this field (for example,`item_issues.severity.aggregated_severity`) can be used for filtering the results.**

` repeated .google.shopping.merchant.reports.v1alpha.ProductView.ItemIssue item_issues = 27; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProductView.ItemIssueOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reports/latest/com.google.shopping.merchant.reports.v1alpha.ProductView.ItemIssueOrBuilder)` |   
  
### getItemIssuesOrBuilderList()
    
    
    public List<? extends ProductView.ItemIssueOrBuilder> getItemIssuesOrBuilderList()

List of item issues for the product.

**This field cannot be used for sorting the results.**

**Only selected attributes of this field (for example,`item_issues.severity.aggregated_severity`) can be used for filtering the results.**

` repeated .google.shopping.merchant.reports.v1alpha.ProductView.ItemIssue item_issues = 27; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.shopping.merchant.reports.v1alpha.ProductView.ItemIssueOrBuilder>` |   
  
### getLanguageCode()
    
    
    public String getLanguageCode()

Language code of the product in BCP 47 format.

`optional string language_code = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The languageCode.  
  
### getLanguageCodeBytes()
    
    
    public ByteString getLanguageCodeBytes()

Language code of the product in BCP 47 format.

`optional string language_code = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for languageCode.  
  
### getOfferId()
    
    
    public String getOfferId()

Merchant-provided id of the product.

`optional string offer_id = 4;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The offerId.  
  
### getOfferIdBytes()
    
    
    public ByteString getOfferIdBytes()

Merchant-provided id of the product.

`optional string offer_id = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for offerId.  
  
### getParserForType()
    
    
    public Parser<ProductView> getParserForType()

**Returns**  
---  
**Type** | **Description**  
`[Parser](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Parser.html)<[ProductView](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reports/latest/com.google.shopping.merchant.reports.v1alpha.ProductView)>` |   
**Overrides**

[GeneratedMessage.getParserForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_getParserForType__)

### getPrice()
    
    
    public Price getPrice()

Product price. Absent if the information about the price of the product is not available.

`.google.shopping.type.Price price = 17;`

**Returns**  
---  
**Type** | **Description**  
`com.google.shopping.type.Price` | The price.  
  
### getPriceOrBuilder()
    
    
    public PriceOrBuilder getPriceOrBuilder()

Product price. Absent if the information about the price of the product is not available.

`.google.shopping.type.Price price = 17;`

**Returns**  
---  
**Type** | **Description**  
`com.google.shopping.type.PriceOrBuilder` |   
  
### getProductTypeL1()
    
    
    public String getProductTypeL1()

Product type (1st level) in merchant's own [product taxonomy](https://support.google.com/merchants/answer/6324406).

`optional string product_type_l1 = 12;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The productTypeL1.  
  
### getProductTypeL1Bytes()
    
    
    public ByteString getProductTypeL1Bytes()

Product type (1st level) in merchant's own [product taxonomy](https://support.google.com/merchants/answer/6324406).

`optional string product_type_l1 = 12;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for productTypeL1.  
  
### getProductTypeL2()
    
    
    public String getProductTypeL2()

Product type (2nd level) in merchant's own [product taxonomy](https://support.google.com/merchants/answer/6324406).

`optional string product_type_l2 = 13;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The productTypeL2.  
  
### getProductTypeL2Bytes()
    
    
    public ByteString getProductTypeL2Bytes()

Product type (2nd level) in merchant's own [product taxonomy](https://support.google.com/merchants/answer/6324406).

`optional string product_type_l2 = 13;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for productTypeL2.  
  
### getProductTypeL3()
    
    
    public String getProductTypeL3()

Product type (3rd level) in merchant's own [product taxonomy](https://support.google.com/merchants/answer/6324406).

`optional string product_type_l3 = 14;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The productTypeL3.  
  
### getProductTypeL3Bytes()
    
    
    public ByteString getProductTypeL3Bytes()

Product type (3rd level) in merchant's own [product taxonomy](https://support.google.com/merchants/answer/6324406).

`optional string product_type_l3 = 14;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for productTypeL3.  
  
### getProductTypeL4()
    
    
    public String getProductTypeL4()

Product type (4th level) in merchant's own [product taxonomy](https://support.google.com/merchants/answer/6324406).

`optional string product_type_l4 = 15;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The productTypeL4.  
  
### getProductTypeL4Bytes()
    
    
    public ByteString getProductTypeL4Bytes()

Product type (4th level) in merchant's own [product taxonomy](https://support.google.com/merchants/answer/6324406).

`optional string product_type_l4 = 15;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for productTypeL4.  
  
### getProductTypeL5()
    
    
    public String getProductTypeL5()

Product type (5th level) in merchant's own [product taxonomy](https://support.google.com/merchants/answer/6324406).

`optional string product_type_l5 = 16;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The productTypeL5.  
  
### getProductTypeL5Bytes()
    
    
    public ByteString getProductTypeL5Bytes()

Product type (5th level) in merchant's own [product taxonomy](https://support.google.com/merchants/answer/6324406).

`optional string product_type_l5 = 16;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for productTypeL5.  
  
### getSerializedSize()
    
    
    public int getSerializedSize()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[GeneratedMessage.getSerializedSize()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_getSerializedSize__)

### getShippingLabel()
    
    
    public String getShippingLabel()

Normalized [shipping label](https://support.google.com/merchants/answer/6324504) specified in the data source.

`optional string shipping_label = 20;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The shippingLabel.  
  
### getShippingLabelBytes()
    
    
    public ByteString getShippingLabelBytes()

Normalized [shipping label](https://support.google.com/merchants/answer/6324504) specified in the data source.

`optional string shipping_label = 20;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for shippingLabel.  
  
### getThumbnailLink()
    
    
    public String getThumbnailLink()

Link to the processed image of the product, hosted on the Google infrastructure.

`optional string thumbnail_link = 23;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The thumbnailLink.  
  
### getThumbnailLinkBytes()
    
    
    public ByteString getThumbnailLinkBytes()

Link to the processed image of the product, hosted on the Google infrastructure.

`optional string thumbnail_link = 23;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for thumbnailLink.  
  
### getTitle()
    
    
    public String getTitle()

Title of the product.

`optional string title = 5;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The title.  
  
### getTitleBytes()
    
    
    public ByteString getTitleBytes()

Title of the product.

`optional string title = 5;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for title.  
  
### hasAggregatedReportingContextStatus()
    
    
    public boolean hasAggregatedReportingContextStatus()

Aggregated status.

` optional .google.shopping.merchant.reports.v1alpha.ProductView.AggregatedReportingContextStatus aggregated_reporting_context_status = 26; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the aggregatedReportingContextStatus field is set.  
  
### hasAvailability()
    
    
    public boolean hasAvailability()

[Availability](https://support.google.com/merchants/answer/6324448) of the product.

`optional string availability = 19;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the availability field is set.  
  
### hasBrand()
    
    
    public boolean hasBrand()

Brand of the product.

`optional string brand = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the brand field is set.  
  
### hasCategoryL1()
    
    
    public boolean hasCategoryL1()

Product category (1st level) in [Google's product taxonomy](https://support.google.com/merchants/answer/6324436).

`optional string category_l1 = 7;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the categoryL1 field is set.  
  
### hasCategoryL2()
    
    
    public boolean hasCategoryL2()

Product category (2nd level) in [Google's product taxonomy](https://support.google.com/merchants/answer/6324436).

`optional string category_l2 = 8;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the categoryL2 field is set.  
  
### hasCategoryL3()
    
    
    public boolean hasCategoryL3()

Product category (3rd level) in [Google's product taxonomy](https://support.google.com/merchants/answer/6324436).

`optional string category_l3 = 9;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the categoryL3 field is set.  
  
### hasCategoryL4()
    
    
    public boolean hasCategoryL4()

Product category (4th level) in [Google's product taxonomy](https://support.google.com/merchants/answer/6324436).

`optional string category_l4 = 10;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the categoryL4 field is set.  
  
### hasCategoryL5()
    
    
    public boolean hasCategoryL5()

Product category (5th level) in [Google's product taxonomy](https://support.google.com/merchants/answer/6324436).

`optional string category_l5 = 11;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the categoryL5 field is set.  
  
### hasChannel()
    
    
    public boolean hasChannel()

Channel of the product. Can be `ONLINE` or `LOCAL`.

`optional .google.shopping.type.Channel.ChannelEnum channel = 28;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the channel field is set.  
  
### hasClickPotentialRank()
    
    
    public boolean hasClickPotentialRank()

Rank of the product based on its click potential. A product with `click_potential_rank` 1 has the highest click potential among the merchant's products that fulfill the search query conditions.

`optional int64 click_potential_rank = 30;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the clickPotentialRank field is set.  
  
### hasCondition()
    
    
    public boolean hasCondition()

[Condition](https://support.google.com/merchants/answer/6324469) of the product.

`optional string condition = 18;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the condition field is set.  
  
### hasCreationTime()
    
    
    public boolean hasCreationTime()

The time the merchant created the product in timestamp seconds.

`.google.protobuf.Timestamp creation_time = 24;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the creationTime field is set.  
  
### hasExpirationDate()
    
    
    public boolean hasExpirationDate()

Expiration date for the product, specified on insertion.

`.google.type.Date expiration_date = 25;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the expirationDate field is set.  
  
### hasFeedLabel()
    
    
    public boolean hasFeedLabel()

Feed label of the product.

`optional string feed_label = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the feedLabel field is set.  
  
### hasId()
    
    
    public boolean hasId()

REST ID of the product, in the form of `channel~languageCode~feedLabel~offerId`. Merchant API methods that operate on products take this as their `name` parameter.

Required in the `SELECT` clause.

`optional string id = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the id field is set.  
  
### hasItemGroupId()
    
    
    public boolean hasItemGroupId()

Item group id provided by the merchant for grouping variants together.

`optional string item_group_id = 22;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the itemGroupId field is set.  
  
### hasLanguageCode()
    
    
    public boolean hasLanguageCode()

Language code of the product in BCP 47 format.

`optional string language_code = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the languageCode field is set.  
  
### hasOfferId()
    
    
    public boolean hasOfferId()

Merchant-provided id of the product.

`optional string offer_id = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the offerId field is set.  
  
### hasPrice()
    
    
    public boolean hasPrice()

Product price. Absent if the information about the price of the product is not available.

`.google.shopping.type.Price price = 17;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the price field is set.  
  
### hasProductTypeL1()
    
    
    public boolean hasProductTypeL1()

Product type (1st level) in merchant's own [product taxonomy](https://support.google.com/merchants/answer/6324406).

`optional string product_type_l1 = 12;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the productTypeL1 field is set.  
  
### hasProductTypeL2()
    
    
    public boolean hasProductTypeL2()

Product type (2nd level) in merchant's own [product taxonomy](https://support.google.com/merchants/answer/6324406).

`optional string product_type_l2 = 13;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the productTypeL2 field is set.  
  
### hasProductTypeL3()
    
    
    public boolean hasProductTypeL3()

Product type (3rd level) in merchant's own [product taxonomy](https://support.google.com/merchants/answer/6324406).

`optional string product_type_l3 = 14;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the productTypeL3 field is set.  
  
### hasProductTypeL4()
    
    
    public boolean hasProductTypeL4()

Product type (4th level) in merchant's own [product taxonomy](https://support.google.com/merchants/answer/6324406).

`optional string product_type_l4 = 15;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the productTypeL4 field is set.  
  
### hasProductTypeL5()
    
    
    public boolean hasProductTypeL5()

Product type (5th level) in merchant's own [product taxonomy](https://support.google.com/merchants/answer/6324406).

`optional string product_type_l5 = 16;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the productTypeL5 field is set.  
  
### hasShippingLabel()
    
    
    public boolean hasShippingLabel()

Normalized [shipping label](https://support.google.com/merchants/answer/6324504) specified in the data source.

`optional string shipping_label = 20;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the shippingLabel field is set.  
  
### hasThumbnailLink()
    
    
    public boolean hasThumbnailLink()

Link to the processed image of the product, hosted on the Google infrastructure.

`optional string thumbnail_link = 23;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the thumbnailLink field is set.  
  
### hasTitle()
    
    
    public boolean hasTitle()

Title of the product.

`optional string title = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the title field is set.  
  
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

### isInitialized()
    
    
    public final boolean isInitialized()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[GeneratedMessage.isInitialized()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_isInitialized__)

### newBuilderForType()
    
    
    public ProductView.Builder newBuilderForType()

**Returns**  
---  
**Type** | **Description**  
`[ProductView.Builder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reports/latest/com.google.shopping.merchant.reports.v1alpha.ProductView.Builder)` |   
  
### newBuilderForType(AbstractMessage.BuilderParent parent)
    
    
    protected ProductView.Builder newBuilderForType(AbstractMessage.BuilderParent parent)

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[BuilderParent](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.BuilderParent.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProductView.Builder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reports/latest/com.google.shopping.merchant.reports.v1alpha.ProductView.Builder)` |   
**Overrides**

[AbstractMessage.newBuilderForType(AbstractMessage.BuilderParent parent)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.html#com_google_protobuf_AbstractMessage_newBuilderForType_com_google_protobuf_AbstractMessage_BuilderParent_)

### toBuilder()
    
    
    public ProductView.Builder toBuilder()

**Returns**  
---  
**Type** | **Description**  
`[ProductView.Builder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reports/latest/com.google.shopping.merchant.reports.v1alpha.ProductView.Builder)` |   
  
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
