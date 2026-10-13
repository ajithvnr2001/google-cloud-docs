---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.CompositeIndexManager
title: Class CompositeIndexManager (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:07:51.048904+00:00
---

# Class CompositeIndexManager (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.CompositeIndexManager

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class CompositeIndexManager (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public class CompositeIndexManager

Composite index management operations needed by the datastore api.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > CompositeIndexManager

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

### CompositeIndexManager()
    
    
    public CompositeIndexManager()

## Methods 

### compositeIndexForQuery(CompositeIndexManager.IndexComponentsOnlyQuery indexOnlyQuery)
    
    
    protected OnestoreEntity.@Nullable Index compositeIndexForQuery(CompositeIndexManager.IndexComponentsOnlyQuery indexOnlyQuery)

Given a IndexComponentsOnlyQuery, return the Index needed to fulfill the query, or `null` if no index is needed.

This code needs to remain in sync with its counterparts in other languages. If you modify this code please make sure you make the same update in the local datastore for other languages.

**Parameter**  
---  
**Name** | **Description**  
`indexOnlyQuery` | `[CompositeIndexManager.IndexComponentsOnlyQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.CompositeIndexManager.IndexComponentsOnlyQuery)`  
The query.  
**Returns**  
---  
**Type** | **Description**  
`com.google.storage.onestore.v3_bytes.proto2api.OnestoreEntity.@org.jspecify.annotations.Nullable Index` | The index that must be present in order to fulfill the query, or `null` if no index is needed.  
  
### generateXmlForIndex(OnestoreEntity.Index index, CompositeIndexManager.IndexSource source)
    
    
    protected String generateXmlForIndex(OnestoreEntity.Index index, CompositeIndexManager.IndexSource source)

Generate an xml representation of the provided Index.

**Parameters**  
---  
**Name** | **Description**  
`index` | `com.google.storage.onestore.v3_bytes.proto2api.OnestoreEntity.Index`  
The index for which we want an xml representation.  
`source` | `[CompositeIndexManager.IndexSource](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.CompositeIndexManager.IndexSource)`  
The source of the provided index.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The xml representation of the provided index.  
  
### minimumCompositeIndexForQuery(CompositeIndexManager.IndexComponentsOnlyQuery indexOnlyQuery, Collection<OnestoreEntity.Index> indexes)
    
    
    protected OnestoreEntity.@Nullable Index minimumCompositeIndexForQuery(CompositeIndexManager.IndexComponentsOnlyQuery indexOnlyQuery, Collection<OnestoreEntity.Index> indexes)

Given a IndexComponentsOnlyQuery and a collection of existing Indexs, return the minimum Index needed to fulfill the query, or `null` if no index is needed.

This code needs to remain in sync with its counterparts in other languages. If you modify this code please make sure you make the same update in the local datastore for other languages.

**Parameters**  
---  
**Name** | **Description**  
`indexOnlyQuery` | `[CompositeIndexManager.IndexComponentsOnlyQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.CompositeIndexManager.IndexComponentsOnlyQuery)`  
The query.  
`indexes` | `[Collection](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html)<com.google.storage.onestore.v3_bytes.proto2api.OnestoreEntity.Index>`  
The existing indexes.  
**Returns**  
---  
**Type** | **Description**  
`com.google.storage.onestore.v3_bytes.proto2api.OnestoreEntity.@org.jspecify.annotations.Nullable Index` | The minimum index that must be present in order to fulfill the query, or `null` if no index is needed.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
