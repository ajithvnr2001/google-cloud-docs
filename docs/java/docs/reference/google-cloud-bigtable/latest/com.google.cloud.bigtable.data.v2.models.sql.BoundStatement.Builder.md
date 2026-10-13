---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.sql.BoundStatement.Builder
title: Class BoundStatement.Builder (2.85.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:36:44.444000+00:00
---

# Class BoundStatement.Builder (2.85.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.sql.BoundStatement.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class BoundStatement.Builder (2.85.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.85.0 (latest)  2.81.0  2.80.0  2.79.0  2.78.1  2.77.0  2.74.0  2.73.0  2.72.0  2.71.0  2.70.0  2.68.0  2.67.1  2.66.0  2.65.1  2.63.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.2  2.56.0  2.54.0  2.52.0  2.51.2  2.49.0  2.46.0  2.45.1  2.44.1  2.43.0  2.42.0  2.40.0  2.39.5  2.37.0  2.35.1  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.1  2.28.0 
    
    
    public static class BoundStatement.Builder

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > BoundStatement.Builder

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

## Constructors 

### Builder(PreparedStatementImpl preparedStatement, Map<String,SqlType<?>> paramTypes)
    
    
    public Builder(PreparedStatementImpl preparedStatement, Map<String,SqlType<?>> paramTypes)

**Internal Only** : This feature is not stable for application use.

_For internal use only_

Creates a builder from a [PreparedStatement](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.sql.PreparedStatement)

This is considered an internal implementation detail and should not be used by applications.

**Parameters**  
---  
**Name** | **Description**  
`preparedStatement` | `com.google.cloud.bigtable.data.v2.internal.PreparedStatementImpl`  
  
`paramTypes` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[SqlType](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.sql.SqlType)<?>>`  
  
  
## Methods 

### <T>setListParam(String paramName, List<T> value, SqlType.Array<T> arrayType)
    
    
    public BoundStatement.Builder <T>setListParam(String paramName, List<T> value, SqlType.Array<T> arrayType)

Sets a query parameter with the name `paramName` and the ARRAY typed value ` value`. The array element type is specified by `arrayType` and the List elements must be of the corresponding Java type. Null array elements are valid.

**Parameters**  
---  
**Name** | **Description**  
`paramName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`value` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<T>`  
  
`arrayType` | `[Array](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.sql.SqlType.Array)<T>`  
  
**Returns**  
---  
**Type** | **Description**  
`[BoundStatement.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.sql.BoundStatement.Builder)` |   
  
### build()
    
    
    public BoundStatement build()

Builds a [BoundStatement](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.sql.BoundStatement) from the builder

**Returns**  
---  
**Type** | **Description**  
`[BoundStatement](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.sql.BoundStatement)` |   
  
### setBooleanParam(String paramName, Boolean value)
    
    
    public BoundStatement.Builder setBooleanParam(String paramName, Boolean value)

Sets a query parameter with the name `paramName` and the BOOL typed value `value`

**Parameters**  
---  
**Name** | **Description**  
`paramName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`value` | `[Boolean](https://docs.oracle.com/javase/8/docs/api/java/lang/Boolean.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BoundStatement.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.sql.BoundStatement.Builder)` |   
  
### setBytesParam(String paramName, ByteString value)
    
    
    public BoundStatement.Builder setBytesParam(String paramName, ByteString value)

Sets a query parameter with the name `paramName` and the Bytes typed value ` value`

**Parameters**  
---  
**Name** | **Description**  
`paramName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BoundStatement.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.sql.BoundStatement.Builder)` |   
  
### setDateParam(String paramName, Date value)
    
    
    public BoundStatement.Builder setDateParam(String paramName, Date value)

Sets a query parameter with the name `paramName` and the DATE typed value `value`

**Parameters**  
---  
**Name** | **Description**  
`paramName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`value` | `com.google.cloud.Date`  
  
**Returns**  
---  
**Type** | **Description**  
`[BoundStatement.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.sql.BoundStatement.Builder)` |   
  
### setDoubleParam(String paramName, Double value)
    
    
    public BoundStatement.Builder setDoubleParam(String paramName, Double value)

Sets a query parameter with the name `paramName` and the FLOAT64 typed value ` value`

**Parameters**  
---  
**Name** | **Description**  
`paramName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`value` | `[Double](https://docs.oracle.com/javase/8/docs/api/java/lang/Double.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BoundStatement.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.sql.BoundStatement.Builder)` |   
  
### setFloatParam(String paramName, Float value)
    
    
    public BoundStatement.Builder setFloatParam(String paramName, Float value)

Sets a query parameter with the name `paramName` and the FLOAT32 typed value ` value`

**Parameters**  
---  
**Name** | **Description**  
`paramName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`value` | `[Float](https://docs.oracle.com/javase/8/docs/api/java/lang/Float.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BoundStatement.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.sql.BoundStatement.Builder)` |   
  
### setLongParam(String paramName, Long value)
    
    
    public BoundStatement.Builder setLongParam(String paramName, Long value)

Sets a query parameter with the name `paramName` and the INT64 typed value ` value`

**Parameters**  
---  
**Name** | **Description**  
`paramName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`value` | `[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BoundStatement.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.sql.BoundStatement.Builder)` |   
  
### setStringParam(String paramName, String value)
    
    
    public BoundStatement.Builder setStringParam(String paramName, String value)

Sets a query parameter with the name `paramName` and the String typed value ` value`

**Parameters**  
---  
**Name** | **Description**  
`paramName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BoundStatement.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.sql.BoundStatement.Builder)` |   
  
### setStringViewParameter(String paramName, String value)
    
    
    public BoundStatement.Builder setStringViewParameter(String paramName, String value)

Sets a view parameter with the name `paramName` and the String typed value ` value`. This map provides the runtime values returned by the VIEW_PARAMETERS() function calls.

**Parameters**  
---  
**Name** | **Description**  
`paramName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BoundStatement.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.sql.BoundStatement.Builder)` |   
  
### setTimestampParam(String paramName, Instant value)
    
    
    public BoundStatement.Builder setTimestampParam(String paramName, Instant value)

Sets a query parameter with the name `paramName` and the TIMESTAMP typed value ` value`

**Parameters**  
---  
**Name** | **Description**  
`paramName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`value` | `[Instant](https://docs.oracle.com/javase/8/docs/api/java/time/Instant.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BoundStatement.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.sql.BoundStatement.Builder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
