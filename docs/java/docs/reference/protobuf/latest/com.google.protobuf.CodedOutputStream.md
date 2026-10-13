---
url: https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedOutputStream
title: Class CodedOutputStream (3.19.4) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:35:56.254130+00:00
---

# Class CodedOutputStream (3.19.4)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedOutputStream

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class CodedOutputStream (3.19.4) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public abstract class CodedOutputStream extends ByteOutput

Encodes and writes protocol message fields.

This class contains two kinds of methods: methods that write specific protocol message constructs and field types (e.g. [#writeTag](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedOutputStream#com_google_protobuf_CodedOutputStream_writeTag_) and [#writeInt32](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedOutputStream#com_google_protobuf_CodedOutputStream_writeInt32_)) and methods that write low-level values (e.g. [#writeRawVarint32](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedOutputStream#com_google_protobuf_CodedOutputStream_writeRawVarint32_) and [#writeRawBytes](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedOutputStream#com_google_protobuf_CodedOutputStream_writeRawBytes_)). If you are writing encoded protocol messages, you should use the former methods, but if you are writing some other format of your own design, use the latter.

This class is totally unsynchronized.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [ByteOutput](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteOutput) > CodedOutputStream

## Inherited Members

[ByteOutput.write(byte)](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteOutput#com_google_protobuf_ByteOutput_write_byte_)

[ByteOutput.write(byte[],int,int)](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteOutput#com_google_protobuf_ByteOutput_write_byte___int_int_)

[ByteOutput.write(ByteBuffer)](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteOutput#com_google_protobuf_ByteOutput_write_java_nio_ByteBuffer_)

[ByteOutput.writeLazy(byte[],int,int)](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteOutput#com_google_protobuf_ByteOutput_writeLazy_byte___int_int_)

[ByteOutput.writeLazy(ByteBuffer)](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteOutput#com_google_protobuf_ByteOutput_writeLazy_java_nio_ByteBuffer_)

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Static Fields 

### DEFAULT_BUFFER_SIZE
    
    
    public static final int DEFAULT_BUFFER_SIZE

The buffer size used in [#newInstance(OutputStream)](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedOutputStream#com_google_protobuf_CodedOutputStream_newInstance_java_io_OutputStream_).

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### LITTLE_ENDIAN_32_SIZE (deprecated)
    
    
    public static final int LITTLE_ENDIAN_32_SIZE

**Deprecated.** _Use[#computeFixed32SizeNoTag(int)](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedOutputStream#com_google_protobuf_CodedOutputStream_computeFixed32SizeNoTag_int_) instead._

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
## Static Methods 

### computeBoolSize(int fieldNumber, boolean value)
    
    
    public static int computeBoolSize(int fieldNumber, boolean value)

Compute the number of bytes that would be needed to encode a `bool` field, including tag.

**Parameters**  
---  
**Name** | **Description**  
`fieldNumber` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### computeBoolSizeNoTag(boolean unused)
    
    
    public static int computeBoolSizeNoTag(boolean unused)

Compute the number of bytes that would be needed to encode a `bool` field.

**Parameter**  
---  
**Name** | **Description**  
`unused` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### computeByteArraySize(int fieldNumber, byte[] value)
    
    
    public static int computeByteArraySize(int fieldNumber, byte[] value)

Compute the number of bytes that would be needed to encode a `bytes` field, including tag.

**Parameters**  
---  
**Name** | **Description**  
`fieldNumber` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[byte](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### computeByteArraySizeNoTag(byte[] value)
    
    
    public static int computeByteArraySizeNoTag(byte[] value)

Compute the number of bytes that would be needed to encode a `bytes` field.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[byte](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### computeByteBufferSize(int fieldNumber, ByteBuffer value)
    
    
    public static int computeByteBufferSize(int fieldNumber, ByteBuffer value)

Compute the number of bytes that would be needed to encode a `bytes` field, including tag.

**Parameters**  
---  
**Name** | **Description**  
`fieldNumber` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[ByteBuffer](https://docs.oracle.com/javase/8/docs/api/java/nio/ByteBuffer.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### computeByteBufferSizeNoTag(ByteBuffer value)
    
    
    public static int computeByteBufferSizeNoTag(ByteBuffer value)

Compute the number of bytes that would be needed to encode a `bytes` field.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteBuffer](https://docs.oracle.com/javase/8/docs/api/java/nio/ByteBuffer.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### computeBytesSize(int fieldNumber, ByteString value)
    
    
    public static int computeBytesSize(int fieldNumber, ByteString value)

Compute the number of bytes that would be needed to encode a `bytes` field, including tag.

**Parameters**  
---  
**Name** | **Description**  
`fieldNumber` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString)`  
  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### computeBytesSizeNoTag(ByteString value)
    
    
    public static int computeBytesSizeNoTag(ByteString value)

Compute the number of bytes that would be needed to encode a `bytes` field.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString)`  
  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### computeDoubleSize(int fieldNumber, double value)
    
    
    public static int computeDoubleSize(int fieldNumber, double value)

Compute the number of bytes that would be needed to encode a `double` field, including tag.

**Parameters**  
---  
**Name** | **Description**  
`fieldNumber` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### computeDoubleSizeNoTag(double unused)
    
    
    public static int computeDoubleSizeNoTag(double unused)

Compute the number of bytes that would be needed to encode a `double` field, including tag.

**Parameter**  
---  
**Name** | **Description**  
`unused` | `[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### computeEnumSize(int fieldNumber, int value)
    
    
    public static int computeEnumSize(int fieldNumber, int value)

Compute the number of bytes that would be needed to encode an enum field, including tag. The provided value is the numeric value used to represent the enum value on the wire (not the enum ordinal value).

**Parameters**  
---  
**Name** | **Description**  
`fieldNumber` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### computeEnumSizeNoTag(int value)
    
    
    public static int computeEnumSizeNoTag(int value)

Compute the number of bytes that would be needed to encode an enum field. The provided value is the numeric value used to represent the enum value on the wire (not the enum ordinal value).

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### computeFixed32Size(int fieldNumber, int value)
    
    
    public static int computeFixed32Size(int fieldNumber, int value)

Compute the number of bytes that would be needed to encode a `fixed32` field, including tag.

**Parameters**  
---  
**Name** | **Description**  
`fieldNumber` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### computeFixed32SizeNoTag(int unused)
    
    
    public static int computeFixed32SizeNoTag(int unused)

Compute the number of bytes that would be needed to encode a `fixed32` field.

**Parameter**  
---  
**Name** | **Description**  
`unused` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### computeFixed64Size(int fieldNumber, long value)
    
    
    public static int computeFixed64Size(int fieldNumber, long value)

Compute the number of bytes that would be needed to encode a `fixed64` field, including tag.

**Parameters**  
---  
**Name** | **Description**  
`fieldNumber` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### computeFixed64SizeNoTag(long unused)
    
    
    public static int computeFixed64SizeNoTag(long unused)

Compute the number of bytes that would be needed to encode a `fixed64` field.

**Parameter**  
---  
**Name** | **Description**  
`unused` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### computeFloatSize(int fieldNumber, float value)
    
    
    public static int computeFloatSize(int fieldNumber, float value)

Compute the number of bytes that would be needed to encode a `float` field, including tag.

**Parameters**  
---  
**Name** | **Description**  
`fieldNumber` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[float](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### computeFloatSizeNoTag(float unused)
    
    
    public static int computeFloatSizeNoTag(float unused)

Compute the number of bytes that would be needed to encode a `float` field, including tag.

**Parameter**  
---  
**Name** | **Description**  
`unused` | `[float](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### computeGroupSize(int fieldNumber, MessageLite value) (deprecated)
    
    
    public static int computeGroupSize(int fieldNumber, MessageLite value)

**Deprecated.** _groups are deprecated._

Compute the number of bytes that would be needed to encode a `group` field, including tag.

**Parameters**  
---  
**Name** | **Description**  
`fieldNumber` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[MessageLite](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageLite)`  
  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### computeGroupSizeNoTag(MessageLite value)
    
    
    public static int computeGroupSizeNoTag(MessageLite value)

Compute the number of bytes that would be needed to encode a `group` field.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[MessageLite](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageLite)`  
  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### computeInt32Size(int fieldNumber, int value)
    
    
    public static int computeInt32Size(int fieldNumber, int value)

Compute the number of bytes that would be needed to encode an `int32` field, including tag.

**Parameters**  
---  
**Name** | **Description**  
`fieldNumber` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### computeInt32SizeNoTag(int value)
    
    
    public static int computeInt32SizeNoTag(int value)

Compute the number of bytes that would be needed to encode an `int32` field, including tag.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### computeInt64Size(int fieldNumber, long value)
    
    
    public static int computeInt64Size(int fieldNumber, long value)

Compute the number of bytes that would be needed to encode an `int64` field, including tag.

**Parameters**  
---  
**Name** | **Description**  
`fieldNumber` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### computeInt64SizeNoTag(long value)
    
    
    public static int computeInt64SizeNoTag(long value)

Compute the number of bytes that would be needed to encode an `int64` field, including tag.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### computeLazyFieldMessageSetExtensionSize(int fieldNumber, LazyFieldLite value)
    
    
    public static int computeLazyFieldMessageSetExtensionSize(int fieldNumber, LazyFieldLite value)

Compute the number of bytes that would be needed to encode a lazily parsed MessageSet extension field to the stream. For historical reasons, the wire format differs from normal fields.

**Parameters**  
---  
**Name** | **Description**  
`fieldNumber` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[LazyFieldLite](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.LazyFieldLite)`  
  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### computeLazyFieldSize(int fieldNumber, LazyFieldLite value)
    
    
    public static int computeLazyFieldSize(int fieldNumber, LazyFieldLite value)

Compute the number of bytes that would be needed to encode an embedded message in lazy field, including tag.

**Parameters**  
---  
**Name** | **Description**  
`fieldNumber` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[LazyFieldLite](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.LazyFieldLite)`  
  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### computeLazyFieldSizeNoTag(LazyFieldLite value)
    
    
    public static int computeLazyFieldSizeNoTag(LazyFieldLite value)

Compute the number of bytes that would be needed to encode an embedded message stored in lazy field.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[LazyFieldLite](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.LazyFieldLite)`  
  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### computeMessageSetExtensionSize(int fieldNumber, MessageLite value)
    
    
    public static int computeMessageSetExtensionSize(int fieldNumber, MessageLite value)

Compute the number of bytes that would be needed to encode a MessageSet extension to the stream. For historical reasons, the wire format differs from normal fields.

**Parameters**  
---  
**Name** | **Description**  
`fieldNumber` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[MessageLite](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageLite)`  
  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### computeMessageSize(int fieldNumber, MessageLite value)
    
    
    public static int computeMessageSize(int fieldNumber, MessageLite value)

Compute the number of bytes that would be needed to encode an embedded message field, including tag.

**Parameters**  
---  
**Name** | **Description**  
`fieldNumber` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[MessageLite](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageLite)`  
  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### computeMessageSizeNoTag(MessageLite value)
    
    
    public static int computeMessageSizeNoTag(MessageLite value)

Compute the number of bytes that would be needed to encode an embedded message field.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[MessageLite](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageLite)`  
  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### computeRawMessageSetExtensionSize(int fieldNumber, ByteString value)
    
    
    public static int computeRawMessageSetExtensionSize(int fieldNumber, ByteString value)

Compute the number of bytes that would be needed to encode an unparsed MessageSet extension field to the stream. For historical reasons, the wire format differs from normal fields.

**Parameters**  
---  
**Name** | **Description**  
`fieldNumber` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString)`  
  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### computeRawVarint32Size(int value) (deprecated)
    
    
    public static int computeRawVarint32Size(int value)

**Deprecated.** _use[#computeUInt32SizeNoTag(int)](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedOutputStream#com_google_protobuf_CodedOutputStream_computeUInt32SizeNoTag_int_) instead._

Compute the number of bytes that would be needed to encode a varint. `value` is treated as unsigned, so it won't be sign-extended if negative.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### computeRawVarint64Size(long value) (deprecated)
    
    
    public static int computeRawVarint64Size(long value)

**Deprecated.** _use[#computeUInt64SizeNoTag(long)](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedOutputStream#com_google_protobuf_CodedOutputStream_computeUInt64SizeNoTag_long_) instead._

Compute the number of bytes that would be needed to encode a varint.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### computeSFixed32Size(int fieldNumber, int value)
    
    
    public static int computeSFixed32Size(int fieldNumber, int value)

Compute the number of bytes that would be needed to encode an `sfixed32` field, including tag.

**Parameters**  
---  
**Name** | **Description**  
`fieldNumber` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### computeSFixed32SizeNoTag(int unused)
    
    
    public static int computeSFixed32SizeNoTag(int unused)

Compute the number of bytes that would be needed to encode an `sfixed32` field.

**Parameter**  
---  
**Name** | **Description**  
`unused` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### computeSFixed64Size(int fieldNumber, long value)
    
    
    public static int computeSFixed64Size(int fieldNumber, long value)

Compute the number of bytes that would be needed to encode an `sfixed64` field, including tag.

**Parameters**  
---  
**Name** | **Description**  
`fieldNumber` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### computeSFixed64SizeNoTag(long unused)
    
    
    public static int computeSFixed64SizeNoTag(long unused)

Compute the number of bytes that would be needed to encode an `sfixed64` field.

**Parameter**  
---  
**Name** | **Description**  
`unused` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### computeSInt32Size(int fieldNumber, int value)
    
    
    public static int computeSInt32Size(int fieldNumber, int value)

Compute the number of bytes that would be needed to encode an `sint32` field, including tag.

**Parameters**  
---  
**Name** | **Description**  
`fieldNumber` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### computeSInt32SizeNoTag(int value)
    
    
    public static int computeSInt32SizeNoTag(int value)

Compute the number of bytes that would be needed to encode an `sint32` field.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### computeSInt64Size(int fieldNumber, long value)
    
    
    public static int computeSInt64Size(int fieldNumber, long value)

Compute the number of bytes that would be needed to encode an `sint64` field, including tag.

**Parameters**  
---  
**Name** | **Description**  
`fieldNumber` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### computeSInt64SizeNoTag(long value)
    
    
    public static int computeSInt64SizeNoTag(long value)

Compute the number of bytes that would be needed to encode an `sint64` field.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### computeStringSize(int fieldNumber, String value)
    
    
    public static int computeStringSize(int fieldNumber, String value)

Compute the number of bytes that would be needed to encode a `string` field, including tag.

**Parameters**  
---  
**Name** | **Description**  
`fieldNumber` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### computeStringSizeNoTag(String value)
    
    
    public static int computeStringSizeNoTag(String value)

Compute the number of bytes that would be needed to encode a `string` field.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### computeTagSize(int fieldNumber)
    
    
    public static int computeTagSize(int fieldNumber)

Compute the number of bytes that would be needed to encode a tag.

**Parameter**  
---  
**Name** | **Description**  
`fieldNumber` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### computeUInt32Size(int fieldNumber, int value)
    
    
    public static int computeUInt32Size(int fieldNumber, int value)

Compute the number of bytes that would be needed to encode a `uint32` field, including tag.

**Parameters**  
---  
**Name** | **Description**  
`fieldNumber` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### computeUInt32SizeNoTag(int value)
    
    
    public static int computeUInt32SizeNoTag(int value)

Compute the number of bytes that would be needed to encode a `uint32` field.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### computeUInt64Size(int fieldNumber, long value)
    
    
    public static int computeUInt64Size(int fieldNumber, long value)

Compute the number of bytes that would be needed to encode a `uint64` field, including tag.

**Parameters**  
---  
**Name** | **Description**  
`fieldNumber` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### computeUInt64SizeNoTag(long value)
    
    
    public static int computeUInt64SizeNoTag(long value)

Compute the number of bytes that would be needed to encode a `uint64` field, including tag.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### encodeZigZag32(int n)
    
    
    public static int encodeZigZag32(int n)

Encode a ZigZag-encoded 32-bit value. ZigZag encodes signed integers into values that can be efficiently encoded with varint. (Otherwise, negative values must be sign-extended to 64 bits to be varint encoded, thus always taking 10 bytes on the wire.)

**Parameter**  
---  
**Name** | **Description**  
`n` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
A signed 32-bit integer.  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | An unsigned 32-bit integer, stored in a signed int because Java has no explicit unsigned support.  
  
### encodeZigZag64(long n)
    
    
    public static long encodeZigZag64(long n)

Encode a ZigZag-encoded 64-bit value. ZigZag encodes signed integers into values that can be efficiently encoded with varint. (Otherwise, negative values must be sign-extended to 64 bits to be varint encoded, thus always taking 10 bytes on the wire.)

**Parameter**  
---  
**Name** | **Description**  
`n` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
A signed 64-bit integer.  
**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | An unsigned 64-bit integer, stored in a signed int because Java has no explicit unsigned support.  
  
### newInstance(byte[] flatArray)
    
    
    public static CodedOutputStream newInstance(byte[] flatArray)

Create a new `CodedOutputStream` that writes directly to the given byte array. If more bytes are written than fit in the array, OutOfSpaceException will be thrown. Writing directly to a flat array is faster than writing to an `OutputStream`. See also ByteString#newCodedBuilder.

**Parameter**  
---  
**Name** | **Description**  
`flatArray` | `[byte](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[CodedOutputStream](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedOutputStream)` |   
  
### newInstance(byte[] flatArray, int offset, int length)
    
    
    public static CodedOutputStream newInstance(byte[] flatArray, int offset, int length)

Create a new `CodedOutputStream` that writes directly to the given byte array slice. If more bytes are written than fit in the slice, OutOfSpaceException will be thrown. Writing directly to a flat array is faster than writing to an `OutputStream`. See also ByteString#newCodedBuilder.

**Parameters**  
---  
**Name** | **Description**  
`flatArray` | `[byte](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)[]`  
  
`offset` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`length` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CodedOutputStream](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedOutputStream)` |   
  
### newInstance(OutputStream output)
    
    
    public static CodedOutputStream newInstance(OutputStream output)

Create a new `CodedOutputStream` wrapping the given `OutputStream`.

NOTE: The provided [OutputStream](https://docs.oracle.com/javase/8/docs/api/java/io/OutputStream.html) **MUST NOT** retain access or modify the provided byte arrays. Doing so may result in corrupted data, which would be difficult to debug.

**Parameter**  
---  
**Name** | **Description**  
`output` | `[OutputStream](https://docs.oracle.com/javase/8/docs/api/java/io/OutputStream.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CodedOutputStream](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedOutputStream)` |   
  
### newInstance(OutputStream output, int bufferSize)
    
    
    public static CodedOutputStream newInstance(OutputStream output, int bufferSize)

Create a new `CodedOutputStream` wrapping the given `OutputStream` with a given buffer size.

NOTE: The provided [OutputStream](https://docs.oracle.com/javase/8/docs/api/java/io/OutputStream.html) **MUST NOT** retain access or modify the provided byte arrays. Doing so may result in corrupted data, which would be difficult to debug.

**Parameters**  
---  
**Name** | **Description**  
`output` | `[OutputStream](https://docs.oracle.com/javase/8/docs/api/java/io/OutputStream.html)`  
  
`bufferSize` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CodedOutputStream](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedOutputStream)` |   
  
### newInstance(ByteBuffer buffer)
    
    
    public static CodedOutputStream newInstance(ByteBuffer buffer)

Create a new `CodedOutputStream` that writes to the given [ByteBuffer](https://docs.oracle.com/javase/8/docs/api/java/nio/ByteBuffer.html).

**Parameter**  
---  
**Name** | **Description**  
`buffer` | `[ByteBuffer](https://docs.oracle.com/javase/8/docs/api/java/nio/ByteBuffer.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CodedOutputStream](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedOutputStream)` |   
  
### newInstance(ByteBuffer byteBuffer, int unused) (deprecated)
    
    
    public static CodedOutputStream newInstance(ByteBuffer byteBuffer, int unused)

**Deprecated.** _the size parameter is no longer used since use of an internal buffer is useless (and wasteful) when writing to a[ByteBuffer](https://docs.oracle.com/javase/8/docs/api/java/nio/ByteBuffer.html). Use [#newInstance(ByteBuffer)](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedOutputStream#com_google_protobuf_CodedOutputStream_newInstance_java_nio_ByteBuffer_) instead._

Create a new `CodedOutputStream` that writes to the given [ByteBuffer](https://docs.oracle.com/javase/8/docs/api/java/nio/ByteBuffer.html).

**Parameters**  
---  
**Name** | **Description**  
`byteBuffer` | `[ByteBuffer](https://docs.oracle.com/javase/8/docs/api/java/nio/ByteBuffer.html)`  
  
`unused` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CodedOutputStream](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedOutputStream)` |   
  
## Methods 

### checkNoSpaceLeft()
    
    
    public final void checkNoSpaceLeft()

Verifies that [#spaceLeft()](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedOutputStream#com_google_protobuf_CodedOutputStream_spaceLeft__) returns zero. It's common to create a byte array that is exactly big enough to hold a message, then write to it with a `CodedOutputStream`. Calling `checkNoSpaceLeft()` after writing verifies that the message was actually as big as expected, which can help catch bugs.

### flush()
    
    
    public abstract void flush()

Flushes the stream and forces any buffered bytes to be written. This does not flush the underlying OutputStream.

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### getTotalBytesWritten()
    
    
    public abstract int getTotalBytesWritten()

Get the total number of bytes successfully written to this stream. The returned value is not guaranteed to be accurate if exceptions have been found in the middle of writing.

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### spaceLeft()
    
    
    public abstract int spaceLeft()

If writing to a flat array, return the space left in the array. Otherwise, throws ` UnsupportedOperationException`.

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### useDeterministicSerialization()
    
    
    public void useDeterministicSerialization()

Configures serialization to be deterministic.

The deterministic serialization guarantees that for a given binary, equal (defined by the `equals()` methods in protos) messages will always be serialized to the same bytes. This implies:

  * repeated serialization of a message will return the same bytes 
  * different processes of the same binary (which may be executing on different machines) will serialize equal messages to the same bytes. 



Note the deterministic serialization is NOT canonical across languages; it is also unstable across different builds with schema changes due to unknown fields. Users who need canonical serialization, e.g. persistent storage in a canonical form, fingerprinting, etc, should define their own canonicalization specification and implement the serializer using reflection APIs rather than relying on this API.

Once set, the serializer will: (Note this is an implementation detail and may subject to change in the future)

  * sort map entries by keys in lexicographical order or numerical order. Note: For string keys, the order is based on comparing the Unicode value of each character in the strings. The order may be different from the deterministic serialization in other languages where maps are sorted on the lexicographical order of the UTF8 encoded keys. 



### write(byte value)
    
    
    public abstract void write(byte value)

Writes a single byte.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[byte](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Overrides**

[ByteOutput.write(byte value)](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteOutput#com_google_protobuf_ByteOutput_write_byte_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### write(byte[] value, int offset, int length)
    
    
    public abstract void write(byte[] value, int offset, int length)

Writes a sequence of bytes. The [ByteOutput](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteOutput) must copy `value` if it will not be processed prior to the return of this method call, since `value` may be reused/altered by the caller.

NOTE: This method **MUST NOT** modify the `value`. Doing so is a programming error and will lead to data corruption which will be difficult to debug.

**Parameters**  
---  
**Name** | **Description**  
`value` | `[byte](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)[]`  
  
`offset` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`length` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Overrides**

[ByteOutput.write(byte[] value, int offset, int length)](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteOutput#com_google_protobuf_ByteOutput_write_byte___int_int_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### write(ByteBuffer value)
    
    
    public abstract void write(ByteBuffer value)

Writes a sequence of bytes. The [ByteOutput](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteOutput) must copy `value` if it will not be processed prior to the return of this method call, since `value` may be reused/altered by the caller.

NOTE: This method **MUST NOT** modify the `value`. Doing so is a programming error and will lead to data corruption which will be difficult to debug.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteBuffer](https://docs.oracle.com/javase/8/docs/api/java/nio/ByteBuffer.html)`  
  
**Overrides**

[ByteOutput.write(ByteBuffer value)](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteOutput#com_google_protobuf_ByteOutput_write_java_nio_ByteBuffer_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### writeBool(int fieldNumber, boolean value)
    
    
    public abstract void writeBool(int fieldNumber, boolean value)

Write a `bool` field, including tag, to the stream.

**Parameters**  
---  
**Name** | **Description**  
`fieldNumber` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### writeBoolNoTag(boolean value)
    
    
    public final void writeBoolNoTag(boolean value)

Write a `bool` field to the stream.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### writeByteArray(int fieldNumber, byte[] value)
    
    
    public abstract void writeByteArray(int fieldNumber, byte[] value)

Write a `bytes` field, including tag, to the stream.

**Parameters**  
---  
**Name** | **Description**  
`fieldNumber` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[byte](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)[]`  
  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### writeByteArray(int fieldNumber, byte[] value, int offset, int length)
    
    
    public abstract void writeByteArray(int fieldNumber, byte[] value, int offset, int length)

Write a `bytes` field, including tag, to the stream.

**Parameters**  
---  
**Name** | **Description**  
`fieldNumber` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[byte](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)[]`  
  
`offset` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`length` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### writeByteArrayNoTag(byte[] value)
    
    
    public final void writeByteArrayNoTag(byte[] value)

Write a `bytes` field to the stream.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[byte](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)[]`  
  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### writeByteBuffer(int fieldNumber, ByteBuffer value)
    
    
    public abstract void writeByteBuffer(int fieldNumber, ByteBuffer value)

Write a `bytes` field, including tag, to the stream. This method will write all content of the ByteBuffer regardless of the current position and limit (i.e., the number of bytes to be written is value.capacity(), not value.remaining()). Furthermore, this method doesn't alter the state of the passed-in ByteBuffer. Its position, limit, mark, etc. will remain unchanged. If you only want to write the remaining bytes of a ByteBuffer, you can call ` writeByteBuffer(fieldNumber, byteBuffer.slice())`.

**Parameters**  
---  
**Name** | **Description**  
`fieldNumber` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[ByteBuffer](https://docs.oracle.com/javase/8/docs/api/java/nio/ByteBuffer.html)`  
  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### writeBytes(int fieldNumber, ByteString value)
    
    
    public abstract void writeBytes(int fieldNumber, ByteString value)

Write a `bytes` field, including tag, to the stream.

**Parameters**  
---  
**Name** | **Description**  
`fieldNumber` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString)`  
  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### writeBytesNoTag(ByteString value)
    
    
    public abstract void writeBytesNoTag(ByteString value)

Write a `bytes` field to the stream.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString)`  
  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### writeDouble(int fieldNumber, double value)
    
    
    public final void writeDouble(int fieldNumber, double value)

Write a `double` field, including tag, to the stream.

**Parameters**  
---  
**Name** | **Description**  
`fieldNumber` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### writeDoubleNoTag(double value)
    
    
    public final void writeDoubleNoTag(double value)

Write a `double` field to the stream.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### writeEnum(int fieldNumber, int value)
    
    
    public final void writeEnum(int fieldNumber, int value)

Write an enum field, including tag, to the stream. The provided value is the numeric value used to represent the enum value on the wire (not the enum ordinal value).

**Parameters**  
---  
**Name** | **Description**  
`fieldNumber` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### writeEnumNoTag(int value)
    
    
    public final void writeEnumNoTag(int value)

Write an enum field to the stream. The provided value is the numeric value used to represent the enum value on the wire (not the enum ordinal value).

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### writeFixed32(int fieldNumber, int value)
    
    
    public abstract void writeFixed32(int fieldNumber, int value)

Write a `fixed32` field, including tag, to the stream.

**Parameters**  
---  
**Name** | **Description**  
`fieldNumber` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### writeFixed32NoTag(int value)
    
    
    public abstract void writeFixed32NoTag(int value)

Write a `fixed32` field to the stream.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### writeFixed64(int fieldNumber, long value)
    
    
    public abstract void writeFixed64(int fieldNumber, long value)

Write a `fixed64` field, including tag, to the stream.

**Parameters**  
---  
**Name** | **Description**  
`fieldNumber` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### writeFixed64NoTag(long value)
    
    
    public abstract void writeFixed64NoTag(long value)

Write a `fixed64` field to the stream.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### writeFloat(int fieldNumber, float value)
    
    
    public final void writeFloat(int fieldNumber, float value)

Write a `float` field, including tag, to the stream.

**Parameters**  
---  
**Name** | **Description**  
`fieldNumber` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[float](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### writeFloatNoTag(float value)
    
    
    public final void writeFloatNoTag(float value)

Write a `float` field to the stream.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[float](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### writeGroup(int fieldNumber, MessageLite value) (deprecated)
    
    
    public final void writeGroup(int fieldNumber, MessageLite value)

**Deprecated.** _groups are deprecated._

Write a `group` field, including tag, to the stream.

**Parameters**  
---  
**Name** | **Description**  
`fieldNumber` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[MessageLite](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageLite)`  
  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### writeGroupNoTag(MessageLite value) (deprecated)
    
    
    public final void writeGroupNoTag(MessageLite value)

**Deprecated.** _groups are deprecated._

Write a `group` field to the stream.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[MessageLite](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageLite)`  
  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### writeInt32(int fieldNumber, int value)
    
    
    public abstract void writeInt32(int fieldNumber, int value)

Write an `int32` field, including tag, to the stream.

**Parameters**  
---  
**Name** | **Description**  
`fieldNumber` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### writeInt32NoTag(int value)
    
    
    public abstract void writeInt32NoTag(int value)

Write an `int32` field to the stream.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### writeInt64(int fieldNumber, long value)
    
    
    public final void writeInt64(int fieldNumber, long value)

Write an `int64` field, including tag, to the stream.

**Parameters**  
---  
**Name** | **Description**  
`fieldNumber` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### writeInt64NoTag(long value)
    
    
    public final void writeInt64NoTag(long value)

Write an `int64` field to the stream.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### writeLazy(byte[] value, int offset, int length)
    
    
    public abstract void writeLazy(byte[] value, int offset, int length)

Writes a sequence of bytes. The [ByteOutput](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteOutput) is free to retain a reference to the value beyond the scope of this method call (e.g. write later) since it is considered immutable and is guaranteed not to change by the caller.

NOTE: This method **MUST NOT** modify the `value`. Doing so is a programming error and will lead to data corruption which will be difficult to debug.

**Parameters**  
---  
**Name** | **Description**  
`value` | `[byte](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)[]`  
  
`offset` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`length` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Overrides**

[ByteOutput.writeLazy(byte[] value, int offset, int length)](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteOutput#com_google_protobuf_ByteOutput_writeLazy_byte___int_int_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### writeLazy(ByteBuffer value)
    
    
    public abstract void writeLazy(ByteBuffer value)

Writes a sequence of bytes. The [ByteOutput](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteOutput) is free to retain a reference to the value beyond the scope of this method call (e.g. write later) since it is considered immutable and is guaranteed not to change by the caller.

NOTE: This method **MUST NOT** modify the `value`. Doing so is a programming error and will lead to data corruption which will be difficult to debug.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteBuffer](https://docs.oracle.com/javase/8/docs/api/java/nio/ByteBuffer.html)`  
  
**Overrides**

[ByteOutput.writeLazy(ByteBuffer value)](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteOutput#com_google_protobuf_ByteOutput_writeLazy_java_nio_ByteBuffer_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### writeMessage(int fieldNumber, MessageLite value)
    
    
    public abstract void writeMessage(int fieldNumber, MessageLite value)

Write an embedded message field, including tag, to the stream.

**Parameters**  
---  
**Name** | **Description**  
`fieldNumber` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[MessageLite](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageLite)`  
  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### writeMessageNoTag(MessageLite value)
    
    
    public abstract void writeMessageNoTag(MessageLite value)

Write an embedded message field to the stream.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[MessageLite](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageLite)`  
  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### writeMessageSetExtension(int fieldNumber, MessageLite value)
    
    
    public abstract void writeMessageSetExtension(int fieldNumber, MessageLite value)

Write a MessageSet extension field to the stream. For historical reasons, the wire format differs from normal fields.

**Parameters**  
---  
**Name** | **Description**  
`fieldNumber` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[MessageLite](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageLite)`  
  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### writeRawByte(byte value)
    
    
    public final void writeRawByte(byte value)

Write a single byte.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[byte](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### writeRawByte(int value)
    
    
    public final void writeRawByte(int value)

Write a single byte, represented by an integer value.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### writeRawBytes(byte[] value)
    
    
    public final void writeRawBytes(byte[] value)

Write an array of bytes.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[byte](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)[]`  
  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### writeRawBytes(byte[] value, int offset, int length)
    
    
    public final void writeRawBytes(byte[] value, int offset, int length)

Write part of an array of bytes.

**Parameters**  
---  
**Name** | **Description**  
`value` | `[byte](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)[]`  
  
`offset` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`length` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### writeRawBytes(ByteString value)
    
    
    public final void writeRawBytes(ByteString value)

Write a byte string.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString)`  
  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### writeRawBytes(ByteBuffer value)
    
    
    public abstract void writeRawBytes(ByteBuffer value)

Write a ByteBuffer. This method will write all content of the ByteBuffer regardless of the current position and limit (i.e., the number of bytes to be written is value.capacity(), not value.remaining()). Furthermore, this method doesn't alter the state of the passed-in ByteBuffer. Its position, limit, mark, etc. will remain unchanged. If you only want to write the remaining bytes of a ByteBuffer, you can call `writeRawBytes(byteBuffer.slice())`.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteBuffer](https://docs.oracle.com/javase/8/docs/api/java/nio/ByteBuffer.html)`  
  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### writeRawLittleEndian32(int value) (deprecated)
    
    
    public final void writeRawLittleEndian32(int value)

**Deprecated.** _Use[#writeFixed32NoTag](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedOutputStream#com_google_protobuf_CodedOutputStream_writeFixed32NoTag_) instead._

Write a little-endian 32-bit integer.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### writeRawLittleEndian64(long value) (deprecated)
    
    
    public final void writeRawLittleEndian64(long value)

**Deprecated.** _Use[#writeFixed64NoTag](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedOutputStream#com_google_protobuf_CodedOutputStream_writeFixed64NoTag_) instead._

Write a little-endian 64-bit integer.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### writeRawMessageSetExtension(int fieldNumber, ByteString value)
    
    
    public abstract void writeRawMessageSetExtension(int fieldNumber, ByteString value)

Write an unparsed MessageSet extension field to the stream. For historical reasons, the wire format differs from normal fields.

**Parameters**  
---  
**Name** | **Description**  
`fieldNumber` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString)`  
  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### writeRawVarint32(int value) (deprecated)
    
    
    public final void writeRawVarint32(int value)

**Deprecated.** _use[#writeUInt32NoTag](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedOutputStream#com_google_protobuf_CodedOutputStream_writeUInt32NoTag_) instead._

Encode and write a varint. `value` is treated as unsigned, so it won't be sign-extended if negative.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### writeRawVarint64(long value) (deprecated)
    
    
    public final void writeRawVarint64(long value)

**Deprecated.** _use[#writeUInt64NoTag](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedOutputStream#com_google_protobuf_CodedOutputStream_writeUInt64NoTag_) instead._

Encode and write a varint.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### writeSFixed32(int fieldNumber, int value)
    
    
    public final void writeSFixed32(int fieldNumber, int value)

Write an `sfixed32` field, including tag, to the stream.

**Parameters**  
---  
**Name** | **Description**  
`fieldNumber` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### writeSFixed32NoTag(int value)
    
    
    public final void writeSFixed32NoTag(int value)

Write a `sfixed32` field to the stream.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### writeSFixed64(int fieldNumber, long value)
    
    
    public final void writeSFixed64(int fieldNumber, long value)

Write an `sfixed64` field, including tag, to the stream.

**Parameters**  
---  
**Name** | **Description**  
`fieldNumber` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### writeSFixed64NoTag(long value)
    
    
    public final void writeSFixed64NoTag(long value)

Write a `sfixed64` field to the stream.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### writeSInt32(int fieldNumber, int value)
    
    
    public final void writeSInt32(int fieldNumber, int value)

Write a `sint32` field, including tag, to the stream.

**Parameters**  
---  
**Name** | **Description**  
`fieldNumber` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### writeSInt32NoTag(int value)
    
    
    public final void writeSInt32NoTag(int value)

Write a `sint32` field to the stream.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### writeSInt64(int fieldNumber, long value)
    
    
    public final void writeSInt64(int fieldNumber, long value)

Write an `sint64` field, including tag, to the stream.

**Parameters**  
---  
**Name** | **Description**  
`fieldNumber` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### writeSInt64NoTag(long value)
    
    
    public final void writeSInt64NoTag(long value)

Write a `sint64` field to the stream.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### writeString(int fieldNumber, String value)
    
    
    public abstract void writeString(int fieldNumber, String value)

Write a `string` field, including tag, to the stream.

**Parameters**  
---  
**Name** | **Description**  
`fieldNumber` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### writeStringNoTag(String value)
    
    
    public abstract void writeStringNoTag(String value)

Write a `string` field to the stream.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### writeTag(int fieldNumber, int wireType)
    
    
    public abstract void writeTag(int fieldNumber, int wireType)

Encode and write a tag.

**Parameters**  
---  
**Name** | **Description**  
`fieldNumber` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`wireType` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### writeUInt32(int fieldNumber, int value)
    
    
    public abstract void writeUInt32(int fieldNumber, int value)

Write a `uint32` field, including tag, to the stream.

**Parameters**  
---  
**Name** | **Description**  
`fieldNumber` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### writeUInt32NoTag(int value)
    
    
    public abstract void writeUInt32NoTag(int value)

Write a `uint32` field to the stream.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### writeUInt64(int fieldNumber, long value)
    
    
    public abstract void writeUInt64(int fieldNumber, long value)

Write a `uint64` field, including tag, to the stream.

**Parameters**  
---  
**Name** | **Description**  
`fieldNumber` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### writeUInt64NoTag(long value)
    
    
    public abstract void writeUInt64NoTag(long value)

Write a `uint64` field to the stream.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-30 UTC."],[],[]] 
