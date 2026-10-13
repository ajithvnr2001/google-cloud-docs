---
url: https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.parsers.BinaryParser
title: Class BinaryParser (0.27.1) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:53:11.844171+00:00
---

# Class BinaryParser (0.27.1)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.parsers.BinaryParser

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class BinaryParser (0.27.1) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 0.27.1 (latest) ](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.parsers.BinaryParser)
  * [ 0.27.0 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.27.0/com.google.cloud.spanner.pgadapter.parsers.BinaryParser)
  * [ 0.26.0 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.26.0/com.google.cloud.spanner.pgadapter.parsers.BinaryParser)
  * [ 0.25.0 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.25.0/com.google.cloud.spanner.pgadapter.parsers.BinaryParser)
  * [ 0.24.0 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.24.0/com.google.cloud.spanner.pgadapter.parsers.BinaryParser)
  * [ 0.23.1 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.23.1/com.google.cloud.spanner.pgadapter.parsers.BinaryParser)
  * [ 0.22.1 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.22.1/com.google.cloud.spanner.pgadapter.parsers.BinaryParser)
  * [ 0.21.0 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.21.0/com.google.cloud.spanner.pgadapter.parsers.BinaryParser)
  * [ 0.20.0 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.20.0/com.google.cloud.spanner.pgadapter.parsers.BinaryParser)
  * [ 0.19.1 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.19.1/com.google.cloud.spanner.pgadapter.parsers.BinaryParser)
  * [ 0.18.4 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.18.4/com.google.cloud.spanner.pgadapter.parsers.BinaryParser)
  * [ 0.17.0 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.17.0/com.google.cloud.spanner.pgadapter.parsers.BinaryParser)
  * [ 0.16.0 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.16.0/com.google.cloud.spanner.pgadapter.parsers.BinaryParser)
  * [ 0.15.0 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.15.0/com.google.cloud.spanner.pgadapter.parsers.BinaryParser)
  * [ 0.14.1 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.14.1/com.google.cloud.spanner.pgadapter.parsers.BinaryParser)
  * [ 0.9.0 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.9.0/com.google.cloud.spanner.pgadapter.parsers.BinaryParser)
  * [ 0.8.0 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.8.0/com.google.cloud.spanner.pgadapter.parsers.BinaryParser)
  * [ 0.7.0 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.7.0/com.google.cloud.spanner.pgadapter.parsers.BinaryParser)
  * [ 0.6.1 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.6.1/com.google.cloud.spanner.pgadapter.parsers.BinaryParser)
  * [ 0.5.1 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.5.1/com.google.cloud.spanner.pgadapter.parsers.BinaryParser)


    
    
    public class BinaryParser extends Parser<ByteArray>

Parse specified type to binary (generally this is the simplest parse class, as items are generally represented in binary for wire format).

## Inheritance

[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [Parser](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.parsers.Parser) > BinaryParser

## Inherited Members

[Parser.binaryParse()](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.parsers.Parser#com_google_cloud_spanner_pgadapter_parsers_Parser_binaryParse__)

[Parser.bind(Statement.Builder,String)](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.parsers.Parser#com_google_cloud_spanner_pgadapter_parsers_Parser_bind_com_google_cloud_spanner_Statement_Builder_java_lang_String_)

[Parser.create(ResultSet,Type,int,SessionState)](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.parsers.Parser#com_google_cloud_spanner_pgadapter_parsers_Parser_create_com_google_cloud_spanner_ResultSet_com_google_cloud_spanner_Type_int_com_google_cloud_spanner_pgadapter_session_SessionState_)

[Parser.create(SessionState,byte[],int,Parser.FormatCode)](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.parsers.Parser#com_google_cloud_spanner_pgadapter_parsers_Parser_create_com_google_cloud_spanner_pgadapter_session_SessionState_byte___int_com_google_cloud_spanner_pgadapter_parsers_Parser_FormatCode_)

[Parser.create(Object,Type.Code,SessionState)](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.parsers.Parser#com_google_cloud_spanner_pgadapter_parsers_Parser_create_java_lang_Object_com_google_cloud_spanner_Type_Code_com_google_cloud_spanner_pgadapter_session_SessionState_)

[Parser.getItem()](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.parsers.Parser#com_google_cloud_spanner_pgadapter_parsers_Parser_getItem__)

[Parser.parse(ProxyServer.DataFormat)](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.parsers.Parser#com_google_cloud_spanner_pgadapter_parsers_Parser_parse_com_google_cloud_spanner_pgadapter_ProxyServer_DataFormat_)

[Parser.spannerBinaryParse()](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.parsers.Parser#com_google_cloud_spanner_pgadapter_parsers_Parser_spannerBinaryParse__)

[Parser.spannerParse()](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.parsers.Parser#com_google_cloud_spanner_pgadapter_parsers_Parser_spannerParse__)

[Parser.stringBinaryParse()](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.parsers.Parser#com_google_cloud_spanner_pgadapter_parsers_Parser_stringBinaryParse__)

[Parser.stringParse()](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.parsers.Parser#com_google_cloud_spanner_pgadapter_parsers_Parser_stringParse__)

[Parser.toOid(Type)](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.parsers.Parser#com_google_cloud_spanner_pgadapter_parsers_Parser_toOid_com_google_cloud_spanner_Type_)

[Parser.toOid(Type)](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.parsers.Parser#com_google_cloud_spanner_pgadapter_parsers_Parser_toOid_com_google_spanner_v1_Type_)

[Parser.toType(int)](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.parsers.Parser#com_google_cloud_spanner_pgadapter_parsers_Parser_toType_int_)

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

## Static Methods 

### convertToPG(ResultSet resultSet, int position, ProxyServer.DataFormat format)
    
    
    public static byte[] convertToPG(ResultSet resultSet, int position, ProxyServer.DataFormat format)

**Parameters**  
---  
**Name** | **Description**  
`resultSet` | `com.google.cloud.spanner.ResultSet`  
  
`position` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`format` | `[ProxyServer.DataFormat](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.ProxyServer.DataFormat)`  
  
**Returns**  
---  
**Type** | **Description**  
`[byte](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)[]` |   
  
### toByteArray(byte[] data)
    
    
    public static ByteArray toByteArray(byte[] data)

Converts the binary data to a ByteArray.

**Parameter**  
---  
**Name** | **Description**  
`data` | `[byte](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.cloud.ByteArray` |   
  
## Methods 

### binaryParse()
    
    
    protected byte[] binaryParse()

Used to parse data type onto binary. Override this to change binary representation.

**Returns**  
---  
**Type** | **Description**  
`[byte](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)[]` |   
**Overrides**

[Parser<T>.binaryParse()](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.parsers.Parser#com_google_cloud_spanner_pgadapter_parsers_Parser_binaryParse__)

### bind(Statement.Builder statementBuilder, String name)
    
    
    public void bind(Statement.Builder statementBuilder, String name)

**Parameters**  
---  
**Name** | **Description**  
`statementBuilder` | `com.google.cloud.spanner.Statement.Builder`  
  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Overrides**

[Parser<T>.bind(Statement.Builder statementBuilder, String name)](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.parsers.Parser#com_google_cloud_spanner_pgadapter_parsers_Parser_bind_com_google_cloud_spanner_Statement_Builder_java_lang_String_)

### spannerBinaryParse()
    
    
    protected byte[] spannerBinaryParse()

**Returns**  
---  
**Type** | **Description**  
`[byte](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)[]` |   
**Overrides**

[Parser<T>.spannerBinaryParse()](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.parsers.Parser#com_google_cloud_spanner_pgadapter_parsers_Parser_spannerBinaryParse__)

### stringParse()
    
    
    public String stringParse()

Used to parse data type into string. Override this to change the string representation.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
**Overrides**

[Parser<T>.stringParse()](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.parsers.Parser#com_google_cloud_spanner_pgadapter_parsers_Parser_stringParse__)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
