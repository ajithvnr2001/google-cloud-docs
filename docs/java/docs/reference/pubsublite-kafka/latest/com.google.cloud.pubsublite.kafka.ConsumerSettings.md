---
url: https://docs.cloud.google.com/java/docs/reference/pubsublite-kafka/latest/com.google.cloud.pubsublite.kafka.ConsumerSettings
title: Class ConsumerSettings (1.1.2) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:29:49.492253+00:00
---

# Class ConsumerSettings (1.1.2)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/pubsublite-kafka/latest/com.google.cloud.pubsublite.kafka.ConsumerSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ConsumerSettings (1.1.2) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.1.2 (latest) ](https://docs.cloud.google.com/java/docs/reference/pubsublite-kafka/latest/com.google.cloud.pubsublite.kafka.ConsumerSettings)
  * [ 1.1.1 ](https://docs.cloud.google.com/java/docs/reference/pubsublite-kafka/1.1.1/com.google.cloud.pubsublite.kafka.ConsumerSettings)
  * [ 1.0.4 ](https://docs.cloud.google.com/java/docs/reference/pubsublite-kafka/1.0.4/com.google.cloud.pubsublite.kafka.ConsumerSettings)
  * [ 0.6.11 ](https://docs.cloud.google.com/java/docs/reference/pubsublite-kafka/0.6.11/com.google.cloud.pubsublite.kafka.ConsumerSettings)


    
    
    public abstract class ConsumerSettings

## Inheritance

java.lang.Object > ConsumerSettings

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

### newBuilder()
    
    
    public static ConsumerSettings.Builder newBuilder()

**Returns**  
---  
**Type** | **Description**  
`[ConsumerSettings.Builder](https://docs.cloud.google.com/java/docs/reference/pubsublite-kafka/latest/com.google.cloud.pubsublite.kafka.ConsumerSettings.Builder)` |   
  
## Constructors 

### ConsumerSettings()
    
    
    public ConsumerSettings()

## Methods 

### instantiate()
    
    
    public Consumer<byte[],byte[]> instantiate()

**Returns**  
---  
**Type** | **Description**  
`org.apache.kafka.clients.consumer.Consumer<byte[],byte[]>` |   
**Exceptions**  
---  
**Type** | **Description**  
`[ApiException](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
