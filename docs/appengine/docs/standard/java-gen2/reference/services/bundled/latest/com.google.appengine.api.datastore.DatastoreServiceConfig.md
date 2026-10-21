---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreServiceConfig
title: Class DatastoreServiceConfig (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:07:54.734850+00:00
---

# Class DatastoreServiceConfig (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreServiceConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class DatastoreServiceConfig (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public final class DatastoreServiceConfig

User-configurable properties of the datastore.

Notes on usage:  
The recommended way to instantiate a `DatastoreServiceConfig` object is to statically import Builder.* and invoke a static creation method followed by an instance mutator (if needed):
    
    
     import static com.google.appengine.api.datastore.DatastoreServiceConfig.Builder.*;
     import com.google.appengine.api.datastore.ReadPolicy.Consistency;
    
     ...
    
     // eventually consistent reads
     DatastoreServiceConfig config = withReadPolicy(new ReadPolicy(Consistency.EVENTUAL));
    
     // eventually consistent reads with a 5 second deadline
     DatastoreServiceConfig config =
       withReadPolicy(new ReadPolicy(Consistency.EVENTUAL)).deadline(5.0);
     

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > DatastoreServiceConfig

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

## Static Fields 

### DATASTORE_EMPTY_LIST_SUPPORT
    
    
    public static final String DATASTORE_EMPTY_LIST_SUPPORT

This is the name of a system property that determines how the Java SDK writes/reads empty lists to/from Datastore.

Historically Datastore has not had the ability to represent an empty list in its persistent store. Different SDKs have made different decisions on what to write to Datastore when a client attempts to insert an empty list to the persistent store. The Java SDK has historically written both empty lists and null values as null values to the persistent store.

With the release of this flag, Datastore can now represent empty lists within its persistent store. This means that Datastore SDKs can distinguish between empty lists and null values. This property controls whether this SDK writes an empty list as empty list or null to the persistent store.

A note on queries: Null values can be indexed by Datastore which means they can interact with queries. For example queries that find all entities with null values or order by a property will include null values. Empty lists are not indexable by Datastore and so cannot appear in similar queries.

Thus, if this flag was unset (the old behavior) and an empty list was stored into the persistent store, it could appear in query results because it was really stored as a null value.

If this flag is set (the new behavior) and an empty list is stored into the persistent store, it will not appear it query results because it is stored as an empty list.

When this variable is set to anything other than "true" the system provides legacy behavior.

  * Null properties are written as null to Datastore 
  * Empty collections are written as null to Datastore 
  * A null is read as null from Datastore 
  * An empty collection is read as null. **Note that a read modify write of an entity with an empty list will cause that list to be turned into a null value.**



When this variable is set to "true":

  * Null properties are written as null to Datastore 
  * Empty collections (#Collection#isEmpty()) are written as empty list to Datastore 
  * A null is read as null from Datastore 
  * An empty collection is read as null 
  * When reading from Datastore an empty list is returned as an empty [Collection](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html). 



It is strongly recommended that this property be set to true in order to provide compatibility with other Datastore SDK's, as well as future versions of Datastore.

To set the flag: ` System.setProperty(DatastoreServiceConfig.DATASTORE_EMPTY_LIST_SUPPORT, Boolean.TRUE.toString()); `

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
## Static Methods 

### getEmptyListSupport()
    
    
    public static boolean getEmptyListSupport()

Returns whether or not empty list support is enabled; see [#DATASTORE_EMPTY_LIST_SUPPORT](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreServiceConfig#com_google_appengine_api_datastore_DatastoreServiceConfig_DATASTORE_EMPTY_LIST_SUPPORT).

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
## Methods 

### deadline(double deadline)
    
    
    public DatastoreServiceConfig deadline(double deadline)

Sets the deadline, in seconds, for all rpcs initiated by the [DatastoreService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService) with which this config is associated.

**Parameter**  
---  
**Name** | **Description**  
`deadline` | `[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
the deadline to set.  
**Returns**  
---  
**Type** | **Description**  
`[DatastoreServiceConfig](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreServiceConfig)` | `this` (for chaining)  
  
### getDeadline()
    
    
    public Double getDeadline()

Returns the deadline, in seconds, to use. Can be `null`.

**Returns**  
---  
**Type** | **Description**  
`[Double](https://docs.oracle.com/javase/8/docs/api/java/lang/Double.html)` |   
  
### getImplicitTransactionManagementPolicy()
    
    
    public ImplicitTransactionManagementPolicy getImplicitTransactionManagementPolicy()

Returns the `ImplicitTransactionManagementPolicy` to use.

**Returns**  
---  
**Type** | **Description**  
`[ImplicitTransactionManagementPolicy](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.ImplicitTransactionManagementPolicy)` |   
  
### getMaxEntityGroupsPerRpc()
    
    
    public Integer getMaxEntityGroupsPerRpc()

Returns the maximum number of entity groups per rpc.

**Returns**  
---  
**Type** | **Description**  
`[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)` |   
  
### getReadPolicy()
    
    
    public ReadPolicy getReadPolicy()

Returns the `ReadPolicy` to use.

**Returns**  
---  
**Type** | **Description**  
`[ReadPolicy](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.ReadPolicy)` |   
  
### implicitTransactionManagementPolicy(ImplicitTransactionManagementPolicy p)
    
    
    public DatastoreServiceConfig implicitTransactionManagementPolicy(ImplicitTransactionManagementPolicy p)

Sets the implicit transaction management policy.

**Parameter**  
---  
**Name** | **Description**  
`p` | `[ImplicitTransactionManagementPolicy](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.ImplicitTransactionManagementPolicy)`  
the implicit transaction management policy to set.  
**Returns**  
---  
**Type** | **Description**  
`[DatastoreServiceConfig](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreServiceConfig)` | `this` (for chaining)  
  
### maxEntityGroupsPerRpc(int maxEntityGroupsPerRpc)
    
    
    public DatastoreServiceConfig maxEntityGroupsPerRpc(int maxEntityGroupsPerRpc)

Sets the maximum number of entity groups that can be represented in a single rpc.

For a non-transactional operation that involves more entity groups than the maximum, the operation will be performed by executing multiple, asynchronous rpcs to the datastore, each of which has no more entity groups represented than the maximum. So, if a put() operation has 8 entity groups and the maximum is 3, we will send 3 rpcs, 2 with 3 entity groups and 1 with 2 entity groups. This is a performance optimization - in many cases multiple, small, asynchronous rpcs will finish faster than a single large asynchronous rpc. The optimal value for this property will be application-specific, so experimentation is encouraged.

**Parameter**  
---  
**Name** | **Description**  
`maxEntityGroupsPerRpc` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
the maximum number of entity groups per rpc  
**Returns**  
---  
**Type** | **Description**  
`[DatastoreServiceConfig](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreServiceConfig)` | `this` (for chaining)  
  
### readPolicy(ReadPolicy readPolicy)
    
    
    public DatastoreServiceConfig readPolicy(ReadPolicy readPolicy)

Sets the read policy.

**Parameter**  
---  
**Name** | **Description**  
`readPolicy` | `[ReadPolicy](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.ReadPolicy)`  
the read policy to set.  
**Returns**  
---  
**Type** | **Description**  
`[DatastoreServiceConfig](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreServiceConfig)` | `this` (for chaining)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
