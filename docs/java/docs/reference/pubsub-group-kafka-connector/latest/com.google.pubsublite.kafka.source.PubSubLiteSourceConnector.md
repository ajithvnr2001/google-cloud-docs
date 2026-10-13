---
url: https://docs.cloud.google.com/java/docs/reference/pubsub-group-kafka-connector/latest/com.google.pubsublite.kafka.source.PubSubLiteSourceConnector
title: Class PubSubLiteSourceConnector (1.2.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:29:36.341981+00:00
---

# Class PubSubLiteSourceConnector (1.2.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/pubsub-group-kafka-connector/latest/com.google.pubsublite.kafka.source.PubSubLiteSourceConnector

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class PubSubLiteSourceConnector (1.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.2.0 (latest) ](https://docs.cloud.google.com/java/docs/reference/pubsub-group-kafka-connector/latest/com.google.pubsublite.kafka.source.PubSubLiteSourceConnector)
  * [ 1.1.0 ](https://docs.cloud.google.com/java/docs/reference/pubsub-group-kafka-connector/1.1.0/com.google.pubsublite.kafka.source.PubSubLiteSourceConnector)
  * [ 1.0.0 ](https://docs.cloud.google.com/java/docs/reference/pubsub-group-kafka-connector/1.0.0/com.google.pubsublite.kafka.source.PubSubLiteSourceConnector)
  * [ 0.1.5 ](https://docs.cloud.google.com/java/docs/reference/pubsub-group-kafka-connector/0.1.5/com.google.pubsublite.kafka.source.PubSubLiteSourceConnector)


    
    
    public class PubSubLiteSourceConnector extends SourceConnector

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > org.apache.kafka.connect.connector.Connector > org.apache.kafka.connect.source.SourceConnector > PubSubLiteSourceConnector

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

org.apache.kafka.connect.connector.Connector.config()

org.apache.kafka.connect.connector.Connector.initialize(org.apache.kafka.connect.connector.ConnectorContext)

org.apache.kafka.connect.connector.Connector.initialize(org.apache.kafka.connect.connector.ConnectorContext,java.util.List<java.util.Map<java.lang.String,java.lang.String>>)

org.apache.kafka.connect.connector.Connector.reconfigure(java.util.Map<java.lang.String,java.lang.String>)

org.apache.kafka.connect.connector.Connector.start(java.util.Map<java.lang.String,java.lang.String>)

org.apache.kafka.connect.connector.Connector.stop()

org.apache.kafka.connect.connector.Connector.taskClass()

org.apache.kafka.connect.connector.Connector.taskConfigs(int)

org.apache.kafka.connect.connector.Connector.validate(java.util.Map<java.lang.String,java.lang.String>)

org.apache.kafka.connect.source.SourceConnector.canDefineTransactionBoundaries(java.util.Map<java.lang.String,java.lang.String>)

org.apache.kafka.connect.source.SourceConnector.context()

org.apache.kafka.connect.source.SourceConnector.exactlyOnceSupport(java.util.Map<java.lang.String,java.lang.String>)

## Constructors 

### PubSubLiteSourceConnector()
    
    
    public PubSubLiteSourceConnector()

## Methods 

### config()
    
    
    public ConfigDef config()

**Returns**  
---  
**Type** | **Description**  
`org.apache.kafka.common.config.ConfigDef` |   
**Overrides**

org.apache.kafka.connect.connector.Connector.config()

### start(Map<String,String> map)
    
    
    public void start(Map<String,String> map)

**Parameter**  
---  
**Name** | **Description**  
`map` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
  
**Overrides**

org.apache.kafka.connect.connector.Connector.start(java.util.Map<java.lang.String,java.lang.String>)

### stop()
    
    
    public void stop()

**Overrides**

org.apache.kafka.connect.connector.Connector.stop()

### taskClass()
    
    
    public Class<? extends Task> taskClass()

**Returns**  
---  
**Type** | **Description**  
`[Class](https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html)<? extends org.apache.kafka.connect.connector.Task>` |   
**Overrides**

org.apache.kafka.connect.connector.Connector.taskClass()

### taskConfigs(int i)
    
    
    public List<Map<String,String>> taskConfigs(int i)

**Parameter**  
---  
**Name** | **Description**  
`i` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>>` |   
**Overrides**

org.apache.kafka.connect.connector.Connector.taskConfigs(int)

### version()
    
    
    public String version()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
