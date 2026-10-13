---
url: https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.datastream.v1.MysqlProfileOrBuilder
title: Interface MysqlProfileOrBuilder (0.16.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:33:14.997041+00:00
---

# Interface MysqlProfileOrBuilder (0.16.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.datastream.v1.MysqlProfileOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface MysqlProfileOrBuilder (0.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 0.16.0 (latest) ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.datastream.v1.MysqlProfileOrBuilder)
  * [ 0.15.0 ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/0.15.0/com.google.events.cloud.datastream.v1.MysqlProfileOrBuilder)
  * [ 0.14.1 ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/0.14.1/com.google.events.cloud.datastream.v1.MysqlProfileOrBuilder)


    
    
    public interface MysqlProfileOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getHostname()
    
    
    public abstract String getHostname()

Required. Hostname for the MySQL connection.

`string hostname = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The hostname.  
  
### getHostnameBytes()
    
    
    public abstract ByteString getHostnameBytes()

Required. Hostname for the MySQL connection.

`string hostname = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for hostname.  
  
### getPort()
    
    
    public abstract int getPort()

Port for the MySQL connection, default value is 3306.

`int32 port = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The port.  
  
### getSslConfig()
    
    
    public abstract MysqlSslConfig getSslConfig()

SSL configuration for the MySQL connection.

`.google.events.cloud.datastream.v1.MysqlSslConfig ssl_config = 5;`

**Returns**  
---  
**Type** | **Description**  
`[MysqlSslConfig](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.datastream.v1.MysqlSslConfig)` | The sslConfig.  
  
### getSslConfigOrBuilder()
    
    
    public abstract MysqlSslConfigOrBuilder getSslConfigOrBuilder()

SSL configuration for the MySQL connection.

`.google.events.cloud.datastream.v1.MysqlSslConfig ssl_config = 5;`

**Returns**  
---  
**Type** | **Description**  
`[MysqlSslConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.datastream.v1.MysqlSslConfigOrBuilder)` |   
  
### getUsername()
    
    
    public abstract String getUsername()

Required. Username for the MySQL connection.

`string username = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The username.  
  
### getUsernameBytes()
    
    
    public abstract ByteString getUsernameBytes()

Required. Username for the MySQL connection.

`string username = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for username.  
  
### hasSslConfig()
    
    
    public abstract boolean hasSslConfig()

SSL configuration for the MySQL connection.

`.google.events.cloud.datastream.v1.MysqlSslConfig ssl_config = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the sslConfig field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
