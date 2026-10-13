---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.TransactionOptions.ReadWriteOptionsBuilder
title: Class TransactionOptions.ReadWriteOptionsBuilder (3.49.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:12:33.955799+00:00
---

# Class TransactionOptions.ReadWriteOptionsBuilder (3.49.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.TransactionOptions.ReadWriteOptionsBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class TransactionOptions.ReadWriteOptionsBuilder (3.49.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.49.0 (latest)  3.45.0  3.44.0  3.43.1  3.41.0  3.38.0  3.37.0  3.36.0  3.35.1  3.33.4  3.32.2  3.31.9  3.30.11  3.28.0  3.27.2  3.26.5  3.25.1  3.24.3  3.22.0  3.21.4  3.20.0  3.17.0  3.16.3  3.15.7  3.14.4  3.13.2  3.12.1  3.11.0  3.10.0  3.9.6  3.8.2  3.7.10  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.1.0  3.0.21 
    
    
    public static final class TransactionOptions.ReadWriteOptionsBuilder extends TransactionOptions.Builder<TransactionOptions.ReadWriteOptionsBuilder>

A typesafe builder class representing those options that are applicable when configuring a transaction to be read-write. All methods function as "set" rather than returning a new copy with a value set on it. By default, a read-write transaction will be attempted a max of 5 times.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [TransactionOptions.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.TransactionOptions.Builder) > TransactionOptions.ReadWriteOptionsBuilder

## Inherited Members

[TransactionOptions.Builder.build()](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.TransactionOptions.Builder#com_google_cloud_firestore_TransactionOptions_Builder_build__)

[TransactionOptions.Builder.getExecutor()](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.TransactionOptions.Builder#com_google_cloud_firestore_TransactionOptions_Builder_getExecutor__)

[TransactionOptions.Builder.setExecutor(Executor)](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.TransactionOptions.Builder#com_google_cloud_firestore_TransactionOptions_Builder_setExecutor_java_util_concurrent_Executor_)

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
    
    
    public TransactionOptions build()

**Returns**  
---  
**Type** | **Description**  
`[TransactionOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.TransactionOptions)` |   
**Overrides**

[TransactionOptions.Builder<B>.build()](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.TransactionOptions.Builder#com_google_cloud_firestore_TransactionOptions_Builder_build__)

### getNumberOfAttempts()
    
    
    public int getNumberOfAttempts()

Specify the max number of attempts a transaction will be attempted before resulting in an error.

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The max number of attempts to try and commit the transaction.  
  
### setNumberOfAttempts(int numberOfAttempts)
    
    
    public TransactionOptions.ReadWriteOptionsBuilder setNumberOfAttempts(int numberOfAttempts)

Specify the max number of attempts a transaction will be attempted before resulting in an error.

**Parameter**  
---  
**Name** | **Description**  
`numberOfAttempts` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The max number of attempts to try and commit the transaction.  
**Returns**  
---  
**Type** | **Description**  
`[TransactionOptions.ReadWriteOptionsBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.TransactionOptions.ReadWriteOptionsBuilder)` | `this` builder  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
