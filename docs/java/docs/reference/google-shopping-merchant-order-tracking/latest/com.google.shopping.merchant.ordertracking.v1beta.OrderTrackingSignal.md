---
url: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-order-tracking/latest/com.google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignal
title: Class OrderTrackingSignal (1.27.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:13:35.017006+00:00
---

# Class OrderTrackingSignal (1.27.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-order-tracking/latest/com.google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignal

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class OrderTrackingSignal (1.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.27.0 (latest)  1.23.0  1.22.0  1.21.0  1.19.0  1.16.0  1.15.0  1.13.0  1.11.0  1.10.0  1.9.0  1.8.0  1.6.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.10.0  0.8.0  0.7.0  0.4.0  0.3.0  0.2.0 
    
    
    public final class OrderTrackingSignal extends GeneratedMessage implements OrderTrackingSignalOrBuilder

Represents a business trade from which signals are extracted, such as shipping.

Protobuf type `google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignal`

## Inheritance

[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.html) > [AbstractMessage](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.html) > [GeneratedMessage](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html) > OrderTrackingSignal

## Implements

[OrderTrackingSignalOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-order-tracking/latest/com.google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignalOrBuilder)

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

### CUSTOMER_SHIPPING_FEE_FIELD_NUMBER
    
    
    public static final int CUSTOMER_SHIPPING_FEE_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### DELIVERY_POSTAL_CODE_FIELD_NUMBER
    
    
    public static final int DELIVERY_POSTAL_CODE_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### DELIVERY_REGION_CODE_FIELD_NUMBER
    
    
    public static final int DELIVERY_REGION_CODE_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### LINE_ITEMS_FIELD_NUMBER
    
    
    public static final int LINE_ITEMS_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### MERCHANT_ID_FIELD_NUMBER
    
    
    public static final int MERCHANT_ID_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### ORDER_CREATED_TIME_FIELD_NUMBER
    
    
    public static final int ORDER_CREATED_TIME_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### ORDER_ID_FIELD_NUMBER
    
    
    public static final int ORDER_ID_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### ORDER_TRACKING_SIGNAL_ID_FIELD_NUMBER
    
    
    public static final int ORDER_TRACKING_SIGNAL_ID_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### SHIPMENT_LINE_ITEM_MAPPING_FIELD_NUMBER
    
    
    public static final int SHIPMENT_LINE_ITEM_MAPPING_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### SHIPPING_INFO_FIELD_NUMBER
    
    
    public static final int SHIPPING_INFO_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
## Static Methods 

### getDefaultInstance()
    
    
    public static OrderTrackingSignal getDefaultInstance()

**Returns**  
---  
**Type** | **Description**  
`[OrderTrackingSignal](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-order-tracking/latest/com.google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignal)` |   
  
### getDescriptor()
    
    
    public static final Descriptors.Descriptor getDescriptor()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
  
### newBuilder()
    
    
    public static OrderTrackingSignal.Builder newBuilder()

**Returns**  
---  
**Type** | **Description**  
`[OrderTrackingSignal.Builder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-order-tracking/latest/com.google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignal.Builder)` |   
  
### newBuilder(OrderTrackingSignal prototype)
    
    
    public static OrderTrackingSignal.Builder newBuilder(OrderTrackingSignal prototype)

**Parameter**  
---  
**Name** | **Description**  
`prototype` | `[OrderTrackingSignal](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-order-tracking/latest/com.google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignal)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OrderTrackingSignal.Builder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-order-tracking/latest/com.google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignal.Builder)` |   
  
### parseDelimitedFrom(InputStream input)
    
    
    public static OrderTrackingSignal parseDelimitedFrom(InputStream input)

**Parameter**  
---  
**Name** | **Description**  
`input` | `[InputStream](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OrderTrackingSignal](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-order-tracking/latest/com.google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignal)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseDelimitedFrom(InputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public static OrderTrackingSignal parseDelimitedFrom(InputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[InputStream](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OrderTrackingSignal](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-order-tracking/latest/com.google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignal)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseFrom(byte[] data)
    
    
    public static OrderTrackingSignal parseFrom(byte[] data)

**Parameter**  
---  
**Name** | **Description**  
`data` | `byte[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[OrderTrackingSignal](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-order-tracking/latest/com.google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignal)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parseFrom(byte[] data, ExtensionRegistryLite extensionRegistry)
    
    
    public static OrderTrackingSignal parseFrom(byte[] data, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`data` | `byte[]`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OrderTrackingSignal](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-order-tracking/latest/com.google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignal)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parseFrom(ByteString data)
    
    
    public static OrderTrackingSignal parseFrom(ByteString data)

**Parameter**  
---  
**Name** | **Description**  
`data` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OrderTrackingSignal](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-order-tracking/latest/com.google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignal)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parseFrom(ByteString data, ExtensionRegistryLite extensionRegistry)
    
    
    public static OrderTrackingSignal parseFrom(ByteString data, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`data` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OrderTrackingSignal](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-order-tracking/latest/com.google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignal)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parseFrom(CodedInputStream input)
    
    
    public static OrderTrackingSignal parseFrom(CodedInputStream input)

**Parameter**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OrderTrackingSignal](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-order-tracking/latest/com.google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignal)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public static OrderTrackingSignal parseFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OrderTrackingSignal](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-order-tracking/latest/com.google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignal)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseFrom(InputStream input)
    
    
    public static OrderTrackingSignal parseFrom(InputStream input)

**Parameter**  
---  
**Name** | **Description**  
`input` | `[InputStream](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OrderTrackingSignal](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-order-tracking/latest/com.google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignal)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseFrom(InputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public static OrderTrackingSignal parseFrom(InputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[InputStream](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OrderTrackingSignal](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-order-tracking/latest/com.google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignal)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseFrom(ByteBuffer data)
    
    
    public static OrderTrackingSignal parseFrom(ByteBuffer data)

**Parameter**  
---  
**Name** | **Description**  
`data` | `[ByteBuffer](https://docs.oracle.com/javase/8/docs/api/java/nio/ByteBuffer.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OrderTrackingSignal](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-order-tracking/latest/com.google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignal)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parseFrom(ByteBuffer data, ExtensionRegistryLite extensionRegistry)
    
    
    public static OrderTrackingSignal parseFrom(ByteBuffer data, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`data` | `[ByteBuffer](https://docs.oracle.com/javase/8/docs/api/java/nio/ByteBuffer.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OrderTrackingSignal](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-order-tracking/latest/com.google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignal)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parser()
    
    
    public static Parser<OrderTrackingSignal> parser()

**Returns**  
---  
**Type** | **Description**  
`[Parser](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Parser.html)<[OrderTrackingSignal](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-order-tracking/latest/com.google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignal)>` |   
  
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

### getCustomerShippingFee()
    
    
    public Price getCustomerShippingFee()

Optional. The shipping fee of the order; this value should be set to zero in the case of free shipping.

` optional .google.shopping.type.Price customer_shipping_fee = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`com.google.shopping.type.Price` | The customerShippingFee.  
  
### getCustomerShippingFeeOrBuilder()
    
    
    public PriceOrBuilder getCustomerShippingFeeOrBuilder()

Optional. The shipping fee of the order; this value should be set to zero in the case of free shipping.

` optional .google.shopping.type.Price customer_shipping_fee = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`com.google.shopping.type.PriceOrBuilder` |   
  
### getDefaultInstanceForType()
    
    
    public OrderTrackingSignal getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[OrderTrackingSignal](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-order-tracking/latest/com.google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignal)` |   
  
### getDeliveryPostalCode()
    
    
    public String getDeliveryPostalCode()

Optional. The delivery postal code, as a continuous string without spaces or dashes, for example "95016". This field will be anonymized in returned OrderTrackingSignal creation response.

`string delivery_postal_code = 9 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The deliveryPostalCode.  
  
### getDeliveryPostalCodeBytes()
    
    
    public ByteString getDeliveryPostalCodeBytes()

Optional. The delivery postal code, as a continuous string without spaces or dashes, for example "95016". This field will be anonymized in returned OrderTrackingSignal creation response.

`string delivery_postal_code = 9 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for deliveryPostalCode.  
  
### getDeliveryRegionCode()
    
    
    public String getDeliveryRegionCode()

Optional. The [CLDR territory code](http://www.unicode.org/repos/cldr/tags/latest/common/main/en.xml) for the shipping destination.

`string delivery_region_code = 10 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The deliveryRegionCode.  
  
### getDeliveryRegionCodeBytes()
    
    
    public ByteString getDeliveryRegionCodeBytes()

Optional. The [CLDR territory code](http://www.unicode.org/repos/cldr/tags/latest/common/main/en.xml) for the shipping destination.

`string delivery_region_code = 10 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for deliveryRegionCode.  
  
### getLineItems(int index)
    
    
    public OrderTrackingSignal.LineItemDetails getLineItems(int index)

Required. Information about line items in the order.

` repeated .google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignal.LineItemDetails line_items = 4 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OrderTrackingSignal.LineItemDetails](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-order-tracking/latest/com.google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignal.LineItemDetails)` |   
  
### getLineItemsCount()
    
    
    public int getLineItemsCount()

Required. Information about line items in the order.

` repeated .google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignal.LineItemDetails line_items = 4 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getLineItemsList()
    
    
    public List<OrderTrackingSignal.LineItemDetails> getLineItemsList()

Required. Information about line items in the order.

` repeated .google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignal.LineItemDetails line_items = 4 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[LineItemDetails](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-order-tracking/latest/com.google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignal.LineItemDetails)>` |   
  
### getLineItemsOrBuilder(int index)
    
    
    public OrderTrackingSignal.LineItemDetailsOrBuilder getLineItemsOrBuilder(int index)

Required. Information about line items in the order.

` repeated .google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignal.LineItemDetails line_items = 4 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OrderTrackingSignal.LineItemDetailsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-order-tracking/latest/com.google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignal.LineItemDetailsOrBuilder)` |   
  
### getLineItemsOrBuilderList()
    
    
    public List<? extends OrderTrackingSignal.LineItemDetailsOrBuilder> getLineItemsOrBuilderList()

Required. Information about line items in the order.

` repeated .google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignal.LineItemDetails line_items = 4 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignal.LineItemDetailsOrBuilder>` |   
  
### getMerchantId()
    
    
    public long getMerchantId()

Optional. The Google Merchant Center ID of this order tracking signal. This value is optional. If left unset, the caller's Merchant Center ID is used. You must request access in order to provide data on behalf of another business. For more information, see [Submitting Order Tracking Signals](https://docs.cloud.google.com/shopping-content/guides/order-tracking-signals).

`int64 merchant_id = 12 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The merchantId.  
  
### getOrderCreatedTime()
    
    
    public DateTime getOrderCreatedTime()

Required. The time when the order was created on the businesses side. Include the year and timezone string, if available.

`.google.type.DateTime order_created_time = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`com.google.type.DateTime` | The orderCreatedTime.  
  
### getOrderCreatedTimeOrBuilder()
    
    
    public DateTimeOrBuilder getOrderCreatedTimeOrBuilder()

Required. The time when the order was created on the businesses side. Include the year and timezone string, if available.

`.google.type.DateTime order_created_time = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`com.google.type.DateTimeOrBuilder` |   
  
### getOrderId()
    
    
    public String getOrderId()

Required. The ID of the order on the businesses side. This field will be hashed in returned OrderTrackingSignal creation response.

`string order_id = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The orderId.  
  
### getOrderIdBytes()
    
    
    public ByteString getOrderIdBytes()

Required. The ID of the order on the businesses side. This field will be hashed in returned OrderTrackingSignal creation response.

`string order_id = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for orderId.  
  
### getOrderTrackingSignalId()
    
    
    public long getOrderTrackingSignalId()

Output only. The ID that uniquely identifies this order tracking signal.

`int64 order_tracking_signal_id = 11 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The orderTrackingSignalId.  
  
### getParserForType()
    
    
    public Parser<OrderTrackingSignal> getParserForType()

**Returns**  
---  
**Type** | **Description**  
`[Parser](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Parser.html)<[OrderTrackingSignal](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-order-tracking/latest/com.google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignal)>` |   
**Overrides**

[GeneratedMessage.getParserForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_getParserForType__)

### getSerializedSize()
    
    
    public int getSerializedSize()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[GeneratedMessage.getSerializedSize()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_getSerializedSize__)

### getShipmentLineItemMapping(int index)
    
    
    public OrderTrackingSignal.ShipmentLineItemMapping getShipmentLineItemMapping(int index)

Optional. The mapping of the line items to the shipment information.

` repeated .google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignal.ShipmentLineItemMapping shipment_line_item_mapping = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OrderTrackingSignal.ShipmentLineItemMapping](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-order-tracking/latest/com.google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignal.ShipmentLineItemMapping)` |   
  
### getShipmentLineItemMappingCount()
    
    
    public int getShipmentLineItemMappingCount()

Optional. The mapping of the line items to the shipment information.

` repeated .google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignal.ShipmentLineItemMapping shipment_line_item_mapping = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getShipmentLineItemMappingList()
    
    
    public List<OrderTrackingSignal.ShipmentLineItemMapping> getShipmentLineItemMappingList()

Optional. The mapping of the line items to the shipment information.

` repeated .google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignal.ShipmentLineItemMapping shipment_line_item_mapping = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ShipmentLineItemMapping](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-order-tracking/latest/com.google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignal.ShipmentLineItemMapping)>` |   
  
### getShipmentLineItemMappingOrBuilder(int index)
    
    
    public OrderTrackingSignal.ShipmentLineItemMappingOrBuilder getShipmentLineItemMappingOrBuilder(int index)

Optional. The mapping of the line items to the shipment information.

` repeated .google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignal.ShipmentLineItemMapping shipment_line_item_mapping = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OrderTrackingSignal.ShipmentLineItemMappingOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-order-tracking/latest/com.google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignal.ShipmentLineItemMappingOrBuilder)` |   
  
### getShipmentLineItemMappingOrBuilderList()
    
    
    public List<? extends OrderTrackingSignal.ShipmentLineItemMappingOrBuilder> getShipmentLineItemMappingOrBuilderList()

Optional. The mapping of the line items to the shipment information.

` repeated .google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignal.ShipmentLineItemMapping shipment_line_item_mapping = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignal.ShipmentLineItemMappingOrBuilder>` |   
  
### getShippingInfo(int index)
    
    
    public OrderTrackingSignal.ShippingInfo getShippingInfo(int index)

Required. The shipping information for the order.

` repeated .google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignal.ShippingInfo shipping_info = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OrderTrackingSignal.ShippingInfo](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-order-tracking/latest/com.google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignal.ShippingInfo)` |   
  
### getShippingInfoCount()
    
    
    public int getShippingInfoCount()

Required. The shipping information for the order.

` repeated .google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignal.ShippingInfo shipping_info = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getShippingInfoList()
    
    
    public List<OrderTrackingSignal.ShippingInfo> getShippingInfoList()

Required. The shipping information for the order.

` repeated .google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignal.ShippingInfo shipping_info = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ShippingInfo](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-order-tracking/latest/com.google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignal.ShippingInfo)>` |   
  
### getShippingInfoOrBuilder(int index)
    
    
    public OrderTrackingSignal.ShippingInfoOrBuilder getShippingInfoOrBuilder(int index)

Required. The shipping information for the order.

` repeated .google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignal.ShippingInfo shipping_info = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OrderTrackingSignal.ShippingInfoOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-order-tracking/latest/com.google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignal.ShippingInfoOrBuilder)` |   
  
### getShippingInfoOrBuilderList()
    
    
    public List<? extends OrderTrackingSignal.ShippingInfoOrBuilder> getShippingInfoOrBuilderList()

Required. The shipping information for the order.

` repeated .google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignal.ShippingInfo shipping_info = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignal.ShippingInfoOrBuilder>` |   
  
### hasCustomerShippingFee()
    
    
    public boolean hasCustomerShippingFee()

Optional. The shipping fee of the order; this value should be set to zero in the case of free shipping.

` optional .google.shopping.type.Price customer_shipping_fee = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the customerShippingFee field is set.  
  
### hasOrderCreatedTime()
    
    
    public boolean hasOrderCreatedTime()

Required. The time when the order was created on the businesses side. Include the year and timezone string, if available.

`.google.type.DateTime order_created_time = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the orderCreatedTime field is set.  
  
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
    
    
    public OrderTrackingSignal.Builder newBuilderForType()

**Returns**  
---  
**Type** | **Description**  
`[OrderTrackingSignal.Builder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-order-tracking/latest/com.google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignal.Builder)` |   
  
### newBuilderForType(AbstractMessage.BuilderParent parent)
    
    
    protected OrderTrackingSignal.Builder newBuilderForType(AbstractMessage.BuilderParent parent)

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[BuilderParent](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.BuilderParent.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OrderTrackingSignal.Builder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-order-tracking/latest/com.google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignal.Builder)` |   
**Overrides**

[AbstractMessage.newBuilderForType(AbstractMessage.BuilderParent parent)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.html#com_google_protobuf_AbstractMessage_newBuilderForType_com_google_protobuf_AbstractMessage_BuilderParent_)

### toBuilder()
    
    
    public OrderTrackingSignal.Builder toBuilder()

**Returns**  
---  
**Type** | **Description**  
`[OrderTrackingSignal.Builder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-order-tracking/latest/com.google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignal.Builder)` |   
  
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
