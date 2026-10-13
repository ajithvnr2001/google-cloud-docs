---
url: https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.utils.Converter
title: Class Converter (0.27.1) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:51:04.492801+00:00
---

# Class Converter (0.27.1)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.utils.Converter

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class Converter (0.27.1) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 0.27.1 (latest) ](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.utils.Converter)
  * [ 0.27.0 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.27.0/com.google.cloud.spanner.pgadapter.utils.Converter)
  * [ 0.26.0 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.26.0/com.google.cloud.spanner.pgadapter.utils.Converter)
  * [ 0.25.0 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.25.0/com.google.cloud.spanner.pgadapter.utils.Converter)
  * [ 0.24.0 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.24.0/com.google.cloud.spanner.pgadapter.utils.Converter)
  * [ 0.23.1 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.23.1/com.google.cloud.spanner.pgadapter.utils.Converter)
  * [ 0.22.1 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.22.1/com.google.cloud.spanner.pgadapter.utils.Converter)
  * [ 0.21.0 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.21.0/com.google.cloud.spanner.pgadapter.utils.Converter)
  * [ 0.20.0 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.20.0/com.google.cloud.spanner.pgadapter.utils.Converter)
  * [ 0.19.1 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.19.1/com.google.cloud.spanner.pgadapter.utils.Converter)
  * [ 0.18.4 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.18.4/com.google.cloud.spanner.pgadapter.utils.Converter)
  * [ 0.17.0 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.17.0/com.google.cloud.spanner.pgadapter.utils.Converter)
  * [ 0.16.0 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.16.0/com.google.cloud.spanner.pgadapter.utils.Converter)
  * [ 0.15.0 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.15.0/com.google.cloud.spanner.pgadapter.utils.Converter)
  * [ 0.14.1 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.14.1/com.google.cloud.spanner.pgadapter.utils.Converter)
  * [ 0.9.0 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.9.0/com.google.cloud.spanner.pgadapter.utils.Converter)
  * [ 0.8.0 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.8.0/com.google.cloud.spanner.pgadapter.utils.Converter)
  * [ 0.7.0 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.7.0/com.google.cloud.spanner.pgadapter.utils.Converter)
  * [ 0.6.1 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.6.1/com.google.cloud.spanner.pgadapter.utils.Converter)
  * [ 0.5.1 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.5.1/com.google.cloud.spanner.pgadapter.utils.Converter)


    
    
    public class Converter implements AutoCloseable

Utility class for converting between generic PostgreSQL conversions.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > Converter

## Implements

[AutoCloseable](https://docs.oracle.com/javase/8/docs/api/java/lang/AutoCloseable.html)

## Inherited Members

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

### convertToPG(ResultSet result, int position, ProxyServer.DataFormat format, SessionState sessionState)
    
    
    public static byte[] convertToPG(ResultSet result, int position, ProxyServer.DataFormat format, SessionState sessionState)

Return the data of the specified column of the ResultSet as a byte array. The column may not contain a null value.

**Parameters**  
---  
**Name** | **Description**  
`result` | `com.google.cloud.spanner.ResultSet`  
The ResultSet to read the data from.  
`position` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The column index.  
`format` | `[ProxyServer.DataFormat](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.ProxyServer.DataFormat)`  
The DataFormat format to use to encode the data.  
`sessionState` | `[SessionState](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.session.SessionState)`  
  
**Returns**  
---  
**Type** | **Description**  
`[byte](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)[]` | a byte array containing the data in the specified format.  
  
## Constructors 

### Converter(IntermediateStatement statement, ConnectionHandler.QueryMode mode, OptionsMetadata options, ResultSet resultSet, boolean includeBinaryCopyHeaderInFirstRow)
    
    
    public Converter(IntermediateStatement statement, ConnectionHandler.QueryMode mode, OptionsMetadata options, ResultSet resultSet, boolean includeBinaryCopyHeaderInFirstRow)

**Parameters**  
---  
**Name** | **Description**  
`statement` | `[IntermediateStatement](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.statements.IntermediateStatement)`  
  
`mode` | `[ConnectionHandler.QueryMode](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.ConnectionHandler.QueryMode)`  
  
`options` | `[OptionsMetadata](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.metadata.OptionsMetadata)`  
  
`resultSet` | `com.google.cloud.spanner.ResultSet`  
  
`includeBinaryCopyHeaderInFirstRow` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
  
## Methods 

### close()
    
    
    public void close()

**Exceptions**  
---  
**Type** | **Description**  
`[Exception](https://docs.oracle.com/javase/8/docs/api/java/lang/Exception.html)` |   
  
### convertResultSetRowToDataRowResponse()
    
    
    public int convertResultSetRowToDataRowResponse()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### getResultSet()
    
    
    public ResultSet getResultSet()

**Returns**  
---  
**Type** | **Description**  
`com.google.cloud.spanner.ResultSet` |   
  
### includeBinaryCopyHeader()
    
    
    public Converter includeBinaryCopyHeader()

**Returns**  
---  
**Type** | **Description**  
`[Converter](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.utils.Converter)` |   
  
### isIncludeBinaryCopyHeaderInFirstRow()
    
    
    public boolean isIncludeBinaryCopyHeaderInFirstRow()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### writeBuffer(DataOutputStream outputStream)
    
    
    public void writeBuffer(DataOutputStream outputStream)

**Parameter**  
---  
**Name** | **Description**  
`outputStream` | `[DataOutputStream](https://docs.oracle.com/javase/8/docs/api/java/io/DataOutputStream.html)`  
  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
