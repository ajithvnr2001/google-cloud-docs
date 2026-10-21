---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreServiceConfig.Builder
title: Class DatastoreServiceConfig.Builder (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:07:54.950420+00:00
---

# Class DatastoreServiceConfig.Builder (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreServiceConfig.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class DatastoreServiceConfig.Builder (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public static final class DatastoreServiceConfig.Builder

Contains static creation methods for [DatastoreServiceConfig](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreServiceConfig).

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > DatastoreServiceConfig.Builder

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

### withDeadline(double deadline)
    
    
    public static DatastoreServiceConfig withDeadline(double deadline)

Create a [DatastoreServiceConfig](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreServiceConfig) with the given deadline, in seconds.

**Parameter**  
---  
**Name** | **Description**  
`deadline` | `[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
the deadline to set.  
**Returns**  
---  
**Type** | **Description**  
`[DatastoreServiceConfig](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreServiceConfig)` | The newly created DatastoreServiceConfig instance.  
  
### withDefaults()
    
    
    public static DatastoreServiceConfig withDefaults()

Helper method for creating a [DatastoreServiceConfig](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreServiceConfig) instance with default values: Implicit transactions are disabled, reads execute with Consistency#STRONG, and no deadline is provided. When no deadline is provided, datastore rpcs execute with the system-defined deadline.

**Returns**  
---  
**Type** | **Description**  
`[DatastoreServiceConfig](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreServiceConfig)` | The newly created DatastoreServiceConfig instance.  
  
### withImplicitTransactionManagementPolicy(ImplicitTransactionManagementPolicy p)
    
    
    public static DatastoreServiceConfig withImplicitTransactionManagementPolicy(ImplicitTransactionManagementPolicy p)

Create a [DatastoreServiceConfig](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreServiceConfig) with the given implicit transaction management policy.

**Parameter**  
---  
**Name** | **Description**  
`p` | `[ImplicitTransactionManagementPolicy](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.ImplicitTransactionManagementPolicy)`  
the implicit transaction management policy to set.  
**Returns**  
---  
**Type** | **Description**  
`[DatastoreServiceConfig](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreServiceConfig)` | The newly created DatastoreServiceConfig instance.  
  
### withMaxEntityGroupsPerRpc(int maxEntityGroupsPerRpc)
    
    
    public static DatastoreServiceConfig withMaxEntityGroupsPerRpc(int maxEntityGroupsPerRpc)

Create a [DatastoreServiceConfig](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreServiceConfig) with the given maximum entity groups per rpc. See Also: [DatastoreServiceConfig#maxEntityGroupsPerRpc(int)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreServiceConfig#com_google_appengine_api_datastore_DatastoreServiceConfig_maxEntityGroupsPerRpc_int_)

**Parameter**  
---  
**Name** | **Description**  
`maxEntityGroupsPerRpc` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
the maximum entity groups per rpc to set.  
**Returns**  
---  
**Type** | **Description**  
`[DatastoreServiceConfig](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreServiceConfig)` | The newly created DatastoreServiceConfig instance.  
  
### withReadPolicy(ReadPolicy readPolicy)
    
    
    public static DatastoreServiceConfig withReadPolicy(ReadPolicy readPolicy)

Create a [DatastoreServiceConfig](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreServiceConfig) with the given read policy.

**Parameter**  
---  
**Name** | **Description**  
`readPolicy` | `[ReadPolicy](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.ReadPolicy)`  
the read policy to set.  
**Returns**  
---  
**Type** | **Description**  
`[DatastoreServiceConfig](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreServiceConfig)` | The newly created DatastoreServiceConfig instance.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
