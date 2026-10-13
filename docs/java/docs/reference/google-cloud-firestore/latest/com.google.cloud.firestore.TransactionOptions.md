---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.TransactionOptions
title: Class TransactionOptions (3.49.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:20:02.284643+00:00
---

# Class TransactionOptions (3.49.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.TransactionOptions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class TransactionOptions (3.49.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.49.0 (latest)  3.45.0  3.44.0  3.43.1  3.41.0  3.38.0  3.37.0  3.36.0  3.35.1  3.33.4  3.32.2  3.31.9  3.30.11  3.28.0  3.27.2  3.26.5  3.25.1  3.24.3  3.22.0  3.21.4  3.20.0  3.17.0  3.16.3  3.15.7  3.14.4  3.13.2  3.12.1  3.11.0  3.10.0  3.9.6  3.8.2  3.7.10  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.1.0  3.0.21 
    
    
    public final class TransactionOptions

Options specifying the behavior of Firestore Transactions.

A transaction in Firestore can be either read-write or read-only.

The default set of options is a read-write transaction with a maximum number of 5 attempts. This attempt count can be customized via the ReadWriteOptionsBuilder#setNumberOfAttempts(int) method. A new instance of a builder can be created by calling [#createReadWriteOptionsBuilder()](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.TransactionOptions#com_google_cloud_firestore_TransactionOptions_createReadWriteOptionsBuilder__).

A read-only transaction can be configured via the ReadOnlyOptionsBuilder class. A new instance can be created by calling [#createReadOnlyOptionsBuilder()](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.TransactionOptions#com_google_cloud_firestore_TransactionOptions_createReadOnlyOptionsBuilder__). See Also: [com.google.firestore.v1.TransactionOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.v1.TransactionOptions)

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > TransactionOptions

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

### create()
    
    
    public static TransactionOptions create()

Create a default set of options suitable for most use cases. Transactions will be opened as ReadWrite transactions and attempted up to 5 times. See Also: [#createReadWriteOptionsBuilder()](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.TransactionOptions#com_google_cloud_firestore_TransactionOptions_createReadWriteOptionsBuilder__)

**Returns**  
---  
**Type** | **Description**  
`[TransactionOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.TransactionOptions)` | The TransactionOptions object.  
  
### create(int numberOfAttempts) (deprecated)
    
    
    public static TransactionOptions create(int numberOfAttempts)

**Deprecated.** _as of 2.0.0, replaced by ReadWriteOptionsBuilder#setNumberOfAttempts(int)_

Create a default set of options with a custom number of retry attempts. See Also: [#createReadWriteOptionsBuilder()](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.TransactionOptions#com_google_cloud_firestore_TransactionOptions_createReadWriteOptionsBuilder__)

**Parameter**  
---  
**Name** | **Description**  
`numberOfAttempts` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The number of execution attempts.  
**Returns**  
---  
**Type** | **Description**  
`[TransactionOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.TransactionOptions)` | The TransactionOptions object.  
  
### create(Executor executor) (deprecated)
    
    
    public static TransactionOptions create(Executor executor)

**Deprecated.** _as of 2.0.0, replaced by ReadWriteOptionsBuilder#setExecutor(Executor)_

Create a default set of options with a custom executor. See Also: [#createReadWriteOptionsBuilder()](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.TransactionOptions#com_google_cloud_firestore_TransactionOptions_createReadWriteOptionsBuilder__)

**Parameter**  
---  
**Name** | **Description**  
`executor` | `[Executor](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Executor.html)`  
The executor to run the user callback code on.  
**Returns**  
---  
**Type** | **Description**  
`[TransactionOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.TransactionOptions)` | The TransactionOptions object.  
  
### create(Executor executor, int numberOfAttempts) (deprecated)
    
    
    public static TransactionOptions create(Executor executor, int numberOfAttempts)

**Deprecated.** _as of 2.0.0, replaced by ReadWriteOptionsBuilder#setExecutor(Executor) and ReadWriteOptionsBuilder#setNumberOfAttempts(int)_

Create a default set of options with a custom executor and a custom number of retry attempts. See Also: [#createReadWriteOptionsBuilder()](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.TransactionOptions#com_google_cloud_firestore_TransactionOptions_createReadWriteOptionsBuilder__)

**Parameters**  
---  
**Name** | **Description**  
`executor` | `[Executor](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Executor.html)`  
The executor to run the user callback code on.  
`numberOfAttempts` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The number of execution attempts.  
**Returns**  
---  
**Type** | **Description**  
`[TransactionOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.TransactionOptions)` | The TransactionOptions object.  
  
### createReadOnlyOptionsBuilder()
    
    
    public static TransactionOptions.ReadOnlyOptionsBuilder createReadOnlyOptionsBuilder()

**Returns**  
---  
**Type** | **Description**  
`[TransactionOptions.ReadOnlyOptionsBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.TransactionOptions.ReadOnlyOptionsBuilder)` | a new Builder with default values applicable to configuring options for a read-only transaction.  
  
### createReadWriteOptionsBuilder()
    
    
    public static TransactionOptions.ReadWriteOptionsBuilder createReadWriteOptionsBuilder()

**Returns**  
---  
**Type** | **Description**  
`[TransactionOptions.ReadWriteOptionsBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.TransactionOptions.ReadWriteOptionsBuilder)` | a new Builder with default values applicable to configuring options for a read-write transaction.  
  
## Methods 

### getExecutor()
    
    
    public Executor getExecutor()

**Returns**  
---  
**Type** | **Description**  
`[Executor](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Executor.html)` | Executor to be used to run user callbacks on  
  
### getNumberOfAttempts()
    
    
    public int getNumberOfAttempts()

Returns the maximum number of times a transaction will be attempted before resulting in an error.

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The max number of attempts to try and commit the transaction.  
  
### getReadTime()
    
    
    public Timestamp getReadTime()

A [Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html) specifying the time documents are to be read at. If null, the server will read documents at the most up to date available. If non-null, the specified `Timestamp` may not be more than 60 minutes in the past (evaluated when the request is processed by the server).

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The specific time to read documents at. A null value means reading the most up to date data.  
  
### getType()
    
    
    public TransactionOptions.TransactionOptionsType getType()

A type flag indicating the type of transaction represented.

**Returns**  
---  
**Type** | **Description**  
`[TransactionOptions.TransactionOptionsType](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.TransactionOptions.TransactionOptionsType)` | The type of transaction this represents. Either read-only or read-write.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
