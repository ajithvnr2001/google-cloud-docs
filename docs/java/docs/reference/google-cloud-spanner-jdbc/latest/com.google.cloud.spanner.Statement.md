---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Statement
title: Class Statement (2.46.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:21:28.229494+00:00
---

# Class Statement (2.46.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Statement

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class Statement (2.46.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.46.0 (latest)  2.42.0  2.41.0  2.40.0  2.38.0  2.35.4  2.34.0  2.33.2  2.32.3  2.31.2  2.30.4  2.28.0  2.27.1  2.26.1  2.25.1  2.24.1  2.23.0  2.22.1  2.21.0  2.20.2  2.19.3  2.18.1  2.17.0  2.16.1  2.15.5  2.14.6  2.13.4  2.11.4  2.10.0  2.9.16  2.8.0  2.7.12  2.6.4  2.5.11 
    
    
    public final class Statement implements Serializable

## Inheritance

[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > Statement

## Implements

[Serializable](https://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html)

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

### getParameterName(int arg0)
    
    
    public static String getParameterName(int arg0)

**Internal Only** : This feature is not stable for application use.

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### newBuilder(String arg0)
    
    
    public static Statement.Builder newBuilder(String arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Statement.Builder)` |   
  
### of(String arg0)
    
    
    public static Statement of(String arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Statement](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Statement)` |   
  
### of(String arg0, ImmutableMap<String,Value> arg1)
    
    
    public static Statement of(String arg0, ImmutableMap<String,Value> arg1)

**Parameters**  
---  
**Name** | **Description**  
`arg0` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`arg1` | `com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Value)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[Statement](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Statement)` |   
  
## Methods 

### analyzeQuery(ReadContext arg0, ReadContext.QueryAnalyzeMode arg1)
    
    
    public ResultSet analyzeQuery(ReadContext arg0, ReadContext.QueryAnalyzeMode arg1)

**Parameters**  
---  
**Name** | **Description**  
`arg0` | `[ReadContext](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ReadContext)`  
  
`arg1` | `[QueryAnalyzeMode](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ReadContext.QueryAnalyzeMode)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ResultSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ResultSet)` |   
  
### equals(Object arg0)
    
    
    public boolean equals(Object arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

### executeQuery(ReadContext arg0, Options.QueryOption[] arg1)
    
    
    public ResultSet executeQuery(ReadContext arg0, Options.QueryOption[] arg1)

**Parameters**  
---  
**Name** | **Description**  
`arg0` | `[ReadContext](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ReadContext)`  
  
`arg1` | `[QueryOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Options.QueryOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[ResultSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.ResultSet)` |   
  
### getParameters()
    
    
    public Map<String,Value> getParameters()

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Value)>` |   
  
### getQueryOptions()
    
    
    public ExecuteSqlRequest.QueryOptions getQueryOptions()

**Returns**  
---  
**Type** | **Description**  
`com.google.spanner.v1.ExecuteSqlRequest.QueryOptions` |   
  
### getSql()
    
    
    public String getSql()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### hasBinding(String arg0)
    
    
    public boolean hasBinding(String arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### hashCode()
    
    
    public int hashCode()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

### toBuilder()
    
    
    public Statement.Builder toBuilder()

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Statement.Builder)` |   
  
### toString()
    
    
    public String toString()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
**Overrides**

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

### withReplacedSql(String arg0)
    
    
    public Statement withReplacedSql(String arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Statement](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Statement)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
