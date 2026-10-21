---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.TransactionOptions
title: Class TransactionOptions (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:12:03.153367+00:00
---

# Class TransactionOptions (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.TransactionOptions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class TransactionOptions (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public final class TransactionOptions

Describes options for transactions, passed at transaction creation time.

Notes on usage:  
The recommended way to instantiate a `TransactionsOptions` object is to statically import Builder.* and invoke a static creation method followed by an instance mutator (if needed):
    
    
     import static com.google.appengine.api.datastore.TransactionOptions.Builder.*;
    
     ...
    
     datastoreService.beginTransaction(withXG(true));
     

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

## Methods 

### allowsMultipleEntityGroups() (deprecated)
    
    
    public Boolean allowsMultipleEntityGroups()

**Deprecated.** _Use[#isXG()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.TransactionOptions#com_google_appengine_api_datastore_TransactionOptions_isXG__) instead._

See [#isXG](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.TransactionOptions#com_google_appengine_api_datastore_TransactionOptions_isXG_).

**Returns**  
---  
**Type** | **Description**  
`[Boolean](https://docs.oracle.com/javase/8/docs/api/java/lang/Boolean.html)` |   
  
### clearMultipleEntityGroups() (deprecated)
    
    
    public TransactionOptions clearMultipleEntityGroups()

**Deprecated.** _Use[#clearXG()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.TransactionOptions#com_google_appengine_api_datastore_TransactionOptions_clearXG__) instead._

See [#clearXG](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.TransactionOptions#com_google_appengine_api_datastore_TransactionOptions_clearXG_).

**Returns**  
---  
**Type** | **Description**  
`[TransactionOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.TransactionOptions)` |   
  
### clearXG()
    
    
    public TransactionOptions clearXG()

Return the cross-group transaction setting to default (disabled).

**Returns**  
---  
**Type** | **Description**  
`[TransactionOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.TransactionOptions)` |   
  
### equals(@Nullable Object o)
    
    
    public boolean equals(@Nullable Object o)

**Parameter**  
---  
**Name** | **Description**  
`o` | `[Nullable Object](https://docs.oracle.com/javase/8/docs/api/java/lang/@org/jspecify/annotations/Nullable%20Object.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

### hashCode()
    
    
    public int hashCode()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

### isXG()
    
    
    public boolean isXG()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | `true` if cross-group transactions are allowed, `false` if they are not allowed.  
  
### multipleEntityGroups(boolean enable) (deprecated)
    
    
    public TransactionOptions multipleEntityGroups(boolean enable)

**Deprecated.** _Use setXG(boolean) instead._

See [#setXG](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.TransactionOptions#com_google_appengine_api_datastore_TransactionOptions_setXG_).

**Parameter**  
---  
**Name** | **Description**  
`enable` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TransactionOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.TransactionOptions)` |   
  
### previousTransaction()
    
    
    public @Nullable Transaction previousTransaction()

Return the previous transaction that is being retried, or `null` if none was provided.

**Returns**  
---  
**Type** | **Description**  
`com.google.appengine.api.datastore.@org.jspecify.annotations.Nullable Transaction` |   
  
### setPreviousTransaction(Transaction previousTransaction)
    
    
    public TransactionOptions setPreviousTransaction(Transaction previousTransaction)

Set which previous transaction to retry. Can only be used for READ_WRITE transactions. The previous transaction should have been created with the same [TransactionOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.TransactionOptions), with the exception of the `previousTransaction` property.

A rollback is not required, and should not be performed, prior to retrying the transaction.

**Parameter**  
---  
**Name** | **Description**  
`previousTransaction` | `[Transaction](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction)`  
the transaction to retry.  
**Returns**  
---  
**Type** | **Description**  
`[TransactionOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.TransactionOptions)` |   
  
### setTransactionMode(TransactionOptions.Mode mode)
    
    
    public TransactionOptions setTransactionMode(TransactionOptions.Mode mode)

Set the mode of the transaction.

Specifying the mode of the transaction can help to improve throughput, as it provides additional information about the intent (or lack of intent, in the case of read only transaction) to perform a write as part of the transaction.

**Parameter**  
---  
**Name** | **Description**  
`mode` | `[TransactionOptions.Mode](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.TransactionOptions.Mode)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TransactionOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.TransactionOptions)` |   
  
### setXG(boolean enable)
    
    
    public TransactionOptions setXG(boolean enable)

Enable or disable the use of cross-group transactions.

**Parameter**  
---  
**Name** | **Description**  
`enable` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
true to cross-group transactions, false to restrict transactions to a single entity group.  
**Returns**  
---  
**Type** | **Description**  
`[TransactionOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.TransactionOptions)` | `this` (for chaining)  
  
### toString()
    
    
    public String toString()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
**Overrides**

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

### transactionMode()
    
    
    public TransactionOptions.@Nullable Mode transactionMode()

Return the mode of the transaction, or `null` if none was specified.

**Returns**  
---  
**Type** | **Description**  
`com.google.appengine.api.datastore.TransactionOptions.@org.jspecify.annotations.Nullable Mode` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
