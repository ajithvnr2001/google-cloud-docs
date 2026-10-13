---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingAsyncResultSet
title: Class ForwardingAsyncResultSet (2.46.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:20:29.418506+00:00
---

# Class ForwardingAsyncResultSet (2.46.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingAsyncResultSet

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ForwardingAsyncResultSet (2.46.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.46.0 (latest)  2.42.0  2.41.0  2.40.0  2.38.0  2.35.4  2.34.0  2.33.2  2.32.3  2.31.2  2.30.4  2.28.0  2.27.1  2.26.1  2.25.1  2.24.1  2.23.0  2.22.1  2.21.0  2.20.2  2.19.3  2.18.1  2.17.0  2.16.1  2.15.5  2.14.6  2.13.4  2.11.4  2.10.0  2.9.16  2.8.0  2.7.12  2.6.4  2.5.11 
    
    
    public class ForwardingAsyncResultSet extends ForwardingResultSet implements AsyncResultSet

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [ForwardingStructReader](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader) > [ForwardingResultSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingResultSet) > ForwardingAsyncResultSet

## Implements

[AsyncResultSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.AsyncResultSet)

## Inherited Members

[ForwardingResultSet.canGetProtobufValue(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingResultSet#com_google_cloud_spanner_ForwardingResultSet_canGetProtobufValue_int_)

[ForwardingResultSet.close()](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingResultSet#com_google_cloud_spanner_ForwardingResultSet_close__)

[ForwardingResultSet.getCurrentRowAsStruct()](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingResultSet#com_google_cloud_spanner_ForwardingResultSet_getCurrentRowAsStruct__)

[ForwardingResultSet.getMetadata()](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingResultSet#com_google_cloud_spanner_ForwardingResultSet_getMetadata__)

[ForwardingResultSet.getProtobufValue(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingResultSet#com_google_cloud_spanner_ForwardingResultSet_getProtobufValue_int_)

[ForwardingResultSet.getStats()](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingResultSet#com_google_cloud_spanner_ForwardingResultSet_getStats__)

[ForwardingResultSet.initiateStreaming(AsyncResultSet.StreamMessageListener)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingResultSet#com_google_cloud_spanner_ForwardingResultSet_initiateStreaming_com_google_cloud_spanner_AsyncResultSet_StreamMessageListener_)

[ForwardingResultSet.next()](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingResultSet#com_google_cloud_spanner_ForwardingResultSet_next__)

[ForwardingStructReader.<T>getProtoEnum(int,Function<Integer,ProtocolMessageEnum>)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader__T_getProtoEnum_int_java_util_function_Function_java_lang_Integer_com_google_protobuf_ProtocolMessageEnum__)

[ForwardingStructReader.<T>getProtoEnum(String,Function<Integer,ProtocolMessageEnum>)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader__T_getProtoEnum_java_lang_String_java_util_function_Function_java_lang_Integer_com_google_protobuf_ProtocolMessageEnum__)

[ForwardingStructReader.<T>getProtoEnumList(int,Function<Integer,ProtocolMessageEnum>)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader__T_getProtoEnumList_int_java_util_function_Function_java_lang_Integer_com_google_protobuf_ProtocolMessageEnum__)

[ForwardingStructReader.<T>getProtoEnumList(String,Function<Integer,ProtocolMessageEnum>)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader__T_getProtoEnumList_java_lang_String_java_util_function_Function_java_lang_Integer_com_google_protobuf_ProtocolMessageEnum__)

[ForwardingStructReader.<T>getProtoMessage(int,T)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader__T_getProtoMessage_int_T_)

[ForwardingStructReader.<T>getProtoMessage(String,T)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader__T_getProtoMessage_java_lang_String_T_)

[ForwardingStructReader.<T>getProtoMessageList(int,T)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader__T_getProtoMessageList_int_T_)

[ForwardingStructReader.<T>getProtoMessageList(String,T)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader__T_getProtoMessageList_java_lang_String_T_)

[ForwardingStructReader.checkValidState()](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_checkValidState__)

[ForwardingStructReader.getBigDecimal(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getBigDecimal_int_)

[ForwardingStructReader.getBigDecimal(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getBigDecimal_java_lang_String_)

[ForwardingStructReader.getBigDecimalList(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getBigDecimalList_int_)

[ForwardingStructReader.getBigDecimalList(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getBigDecimalList_java_lang_String_)

[ForwardingStructReader.getBoolean(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getBoolean_int_)

[ForwardingStructReader.getBoolean(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getBoolean_java_lang_String_)

[ForwardingStructReader.getBooleanArray(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getBooleanArray_int_)

[ForwardingStructReader.getBooleanArray(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getBooleanArray_java_lang_String_)

[ForwardingStructReader.getBooleanList(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getBooleanList_int_)

[ForwardingStructReader.getBooleanList(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getBooleanList_java_lang_String_)

[ForwardingStructReader.getBytes(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getBytes_int_)

[ForwardingStructReader.getBytes(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getBytes_java_lang_String_)

[ForwardingStructReader.getBytesList(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getBytesList_int_)

[ForwardingStructReader.getBytesList(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getBytesList_java_lang_String_)

[ForwardingStructReader.getColumnCount()](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getColumnCount__)

[ForwardingStructReader.getColumnIndex(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getColumnIndex_java_lang_String_)

[ForwardingStructReader.getColumnType(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getColumnType_int_)

[ForwardingStructReader.getColumnType(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getColumnType_java_lang_String_)

[ForwardingStructReader.getDate(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getDate_int_)

[ForwardingStructReader.getDate(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getDate_java_lang_String_)

[ForwardingStructReader.getDateList(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getDateList_int_)

[ForwardingStructReader.getDateList(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getDateList_java_lang_String_)

[ForwardingStructReader.getDouble(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getDouble_int_)

[ForwardingStructReader.getDouble(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getDouble_java_lang_String_)

[ForwardingStructReader.getDoubleArray(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getDoubleArray_int_)

[ForwardingStructReader.getDoubleArray(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getDoubleArray_java_lang_String_)

[ForwardingStructReader.getDoubleList(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getDoubleList_int_)

[ForwardingStructReader.getDoubleList(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getDoubleList_java_lang_String_)

[ForwardingStructReader.getFloat(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getFloat_int_)

[ForwardingStructReader.getFloat(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getFloat_java_lang_String_)

[ForwardingStructReader.getFloatArray(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getFloatArray_int_)

[ForwardingStructReader.getFloatArray(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getFloatArray_java_lang_String_)

[ForwardingStructReader.getFloatList(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getFloatList_int_)

[ForwardingStructReader.getFloatList(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getFloatList_java_lang_String_)

[ForwardingStructReader.getInterval(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getInterval_int_)

[ForwardingStructReader.getInterval(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getInterval_java_lang_String_)

[ForwardingStructReader.getIntervalList(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getIntervalList_int_)

[ForwardingStructReader.getIntervalList(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getIntervalList_java_lang_String_)

[ForwardingStructReader.getJson(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getJson_int_)

[ForwardingStructReader.getJson(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getJson_java_lang_String_)

[ForwardingStructReader.getJsonList(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getJsonList_int_)

[ForwardingStructReader.getJsonList(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getJsonList_java_lang_String_)

[ForwardingStructReader.getLong(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getLong_int_)

[ForwardingStructReader.getLong(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getLong_java_lang_String_)

[ForwardingStructReader.getLongArray(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getLongArray_int_)

[ForwardingStructReader.getLongArray(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getLongArray_java_lang_String_)

[ForwardingStructReader.getLongList(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getLongList_int_)

[ForwardingStructReader.getLongList(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getLongList_java_lang_String_)

[ForwardingStructReader.getPgJsonb(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getPgJsonb_int_)

[ForwardingStructReader.getPgJsonb(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getPgJsonb_java_lang_String_)

[ForwardingStructReader.getPgJsonbList(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getPgJsonbList_int_)

[ForwardingStructReader.getPgJsonbList(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getPgJsonbList_java_lang_String_)

[ForwardingStructReader.getString(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getString_int_)

[ForwardingStructReader.getString(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getString_java_lang_String_)

[ForwardingStructReader.getStringList(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getStringList_int_)

[ForwardingStructReader.getStringList(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getStringList_java_lang_String_)

[ForwardingStructReader.getStructList(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getStructList_int_)

[ForwardingStructReader.getStructList(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getStructList_java_lang_String_)

[ForwardingStructReader.getTimestamp(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getTimestamp_int_)

[ForwardingStructReader.getTimestamp(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getTimestamp_java_lang_String_)

[ForwardingStructReader.getTimestampList(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getTimestampList_int_)

[ForwardingStructReader.getTimestampList(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getTimestampList_java_lang_String_)

[ForwardingStructReader.getType()](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getType__)

[ForwardingStructReader.getUuid(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getUuid_int_)

[ForwardingStructReader.getUuid(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getUuid_java_lang_String_)

[ForwardingStructReader.getUuidList(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getUuidList_int_)

[ForwardingStructReader.getUuidList(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getUuidList_java_lang_String_)

[ForwardingStructReader.getValue(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getValue_int_)

[ForwardingStructReader.getValue(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_getValue_java_lang_String_)

[ForwardingStructReader.isNull(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_isNull_int_)

[ForwardingStructReader.isNull(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ForwardingStructReader#com_google_cloud_spanner_ForwardingStructReader_isNull_java_lang_String_)

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

## Constructors 

### ForwardingAsyncResultSet(AsyncResultSet arg0)
    
    
    public ForwardingAsyncResultSet(AsyncResultSet arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[AsyncResultSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.AsyncResultSet)`  
  
  
## Methods 

### <T>toList(Function<StructReader,T> arg0)
    
    
    public List<T> <T>toList(Function<StructReader,T> arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `com.google.common.base.Function<[StructReader](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.StructReader),T>`  
  
**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<T>` |   
**Exceptions**  
---  
**Type** | **Description**  
`[SpannerException](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.SpannerException)` |   
  
### <T>toListAsync(Function<StructReader,T> arg0, Executor arg1)
    
    
    public ApiFuture<List<T>> <T>toListAsync(Function<StructReader,T> arg0, Executor arg1)

**Parameters**  
---  
**Name** | **Description**  
`arg0` | `com.google.common.base.Function<[StructReader](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.StructReader),T>`  
  
`arg1` | `[Executor](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Executor.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<T>>` |   
  
### cancel()
    
    
    public void cancel()

### resume()
    
    
    public void resume()

### setCallback(Executor arg0, AsyncResultSet.ReadyCallback arg1)
    
    
    public ApiFuture<Void> setCallback(Executor arg0, AsyncResultSet.ReadyCallback arg1)

**Parameters**  
---  
**Name** | **Description**  
`arg0` | `[Executor](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Executor.html)`  
  
`arg1` | `[ReadyCallback](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.AsyncResultSet.ReadyCallback)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Void](https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html)>` |   
  
### tryNext()
    
    
    public AsyncResultSet.CursorState tryNext()

**Returns**  
---  
**Type** | **Description**  
`[CursorState](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.AsyncResultSet.CursorState)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[SpannerException](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.SpannerException)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
