---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.client.DatastoreEmulatorOptions.Builder
title: Class DatastoreEmulatorOptions.Builder (3.7.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:04:21.871332+00:00
---

# Class DatastoreEmulatorOptions.Builder (3.7.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.client.DatastoreEmulatorOptions.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DatastoreEmulatorOptions.Builder (3.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.7.0 (latest)  3.3.0  3.2.0  3.1.0  2.40.0  2.37.0  2.36.0  2.34.0  2.33.3  2.32.3  2.31.4  2.30.0  2.29.1  2.28.2  2.27.1  2.26.4  2.25.2  2.24.3  2.23.0  2.22.0  2.21.3  2.20.2  2.19.2  2.18.5  2.17.6 
    
    
    public static class DatastoreEmulatorOptions.Builder

Builder for [DatastoreEmulatorOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.client.DatastoreEmulatorOptions).

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > DatastoreEmulatorOptions.Builder

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

### Builder()
    
    
    public Builder()

## Methods 

### addCmdLineOption(String option)
    
    
    public DatastoreEmulatorOptions.Builder addCmdLineOption(String option)

**Parameter**  
---  
**Name** | **Description**  
`option` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DatastoreEmulatorOptions.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.client.DatastoreEmulatorOptions.Builder)` |   
  
### addCmdLineOptions(Collection<String> options)
    
    
    public DatastoreEmulatorOptions.Builder addCmdLineOptions(Collection<String> options)

**Parameter**  
---  
**Name** | **Description**  
`options` | `[Collection](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[DatastoreEmulatorOptions.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.client.DatastoreEmulatorOptions.Builder)` |   
  
### addEnvVar(String var, String value)
    
    
    public DatastoreEmulatorOptions.Builder addEnvVar(String var, String value)

Adds an environment variable to pass to the emulator.

**Parameters**  
---  
**Name** | **Description**  
`var` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DatastoreEmulatorOptions.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.client.DatastoreEmulatorOptions.Builder)` |   
  
### build()
    
    
    public DatastoreEmulatorOptions build()

**Returns**  
---  
**Type** | **Description**  
`[DatastoreEmulatorOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.client.DatastoreEmulatorOptions)` |   
  
### setCommand(String cmd)
    
    
    public DatastoreEmulatorOptions.Builder setCommand(String cmd)

**Parameter**  
---  
**Name** | **Description**  
`cmd` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DatastoreEmulatorOptions.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.client.DatastoreEmulatorOptions.Builder)` |   
  
### setProjectId(String projectId)
    
    
    public DatastoreEmulatorOptions.Builder setProjectId(String projectId)

**Parameter**  
---  
**Name** | **Description**  
`projectId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DatastoreEmulatorOptions.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.client.DatastoreEmulatorOptions.Builder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
