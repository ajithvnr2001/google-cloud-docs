---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Mutation.SendBuilder
title: Class Mutation.SendBuilder (2.46.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:37:54.775744+00:00
---

# Class Mutation.SendBuilder (2.46.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Mutation.SendBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class Mutation.SendBuilder (2.46.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.46.0 (latest)  2.42.0  2.41.0  2.40.0  2.38.0  2.35.4  2.34.0  2.33.2  2.32.3  2.31.2  2.30.4  2.28.0  2.27.1  2.26.1  2.25.1  2.24.1  2.23.0  2.22.1  2.21.0  2.20.2  2.19.3  2.18.1  2.17.0  2.16.1  2.15.5  2.14.6  2.13.4  2.11.4  2.10.0  2.9.16  2.8.0  2.7.12  2.6.4  2.5.11 
    
    
    public static class Mutation.SendBuilder

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > Mutation.SendBuilder

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

## Methods 

### build()
    
    
    public Mutation build()

**Returns**  
---  
**Type** | **Description**  
`[Mutation](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Mutation)` |   
  
### setDeliveryTime(Instant arg0)
    
    
    public Mutation.SendBuilder setDeliveryTime(Instant arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[Instant](https://docs.oracle.com/javase/8/docs/api/java/time/Instant.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Mutation.SendBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Mutation.SendBuilder)` |   
  
### setKey(Key arg0)
    
    
    public Mutation.SendBuilder setKey(Key arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[Key](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Key)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Mutation.SendBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Mutation.SendBuilder)` |   
  
### setPayload(Value arg0)
    
    
    public Mutation.SendBuilder setPayload(Value arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Value)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Mutation.SendBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.Mutation.SendBuilder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
