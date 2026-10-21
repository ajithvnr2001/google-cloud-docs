---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.EntityProtoComparators.EntityProtoComparator
title: Class EntityProtoComparators.EntityProtoComparator (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:07:57.504762+00:00
---

# Class EntityProtoComparators.EntityProtoComparator (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.EntityProtoComparators.EntityProtoComparator

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class EntityProtoComparators.EntityProtoComparator (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public static final class EntityProtoComparators.EntityProtoComparator extends BaseEntityComparator<OnestoreEntity.EntityProto>

A comparator for EntityProto objects with the same ordering as EntityComparator.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > com.google.appengine.api.datastore.BaseEntityComparator > EntityProtoComparators.EntityProtoComparator

## Inherited Members

com.google.appengine.api.datastore.BaseEntityComparator.compare(EntityT,EntityT)

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

### EntityProtoComparator(List<DatastoreV3Pb.Query.Order> orders)
    
    
    public EntityProtoComparator(List<DatastoreV3Pb.Query.Order> orders)

**Parameter**  
---  
**Name** | **Description**  
`orders` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<com.google.apphosting.datastore_bytes.proto2api.DatastoreV3Pb.Query.Order>`  
  
  
### EntityProtoComparator(List<DatastoreV3Pb.Query.Order> orders, List<DatastoreV3Pb.Query.Filter> filters)
    
    
    public EntityProtoComparator(List<DatastoreV3Pb.Query.Order> orders, List<DatastoreV3Pb.Query.Filter> filters)

**Parameters**  
---  
**Name** | **Description**  
`orders` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<com.google.apphosting.datastore_bytes.proto2api.DatastoreV3Pb.Query.Order>`  
  
`filters` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<com.google.apphosting.datastore_bytes.proto2api.DatastoreV3Pb.Query.Filter>`  
  
  
## Methods 

### getAdjustedOrders()
    
    
    public List<DatastoreV3Pb.Query.Order> getAdjustedOrders()

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<com.google.apphosting.datastore_bytes.proto2api.DatastoreV3Pb.Query.Order>` |   
  
### matches(OnestoreEntity.EntityProto proto)
    
    
    public boolean matches(OnestoreEntity.EntityProto proto)

**Parameter**  
---  
**Name** | **Description**  
`proto` | `com.google.storage.onestore.v3_bytes.proto2api.OnestoreEntity.EntityProto`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### matches(OnestoreEntity.Property prop)
    
    
    public boolean matches(OnestoreEntity.Property prop)

**Parameter**  
---  
**Name** | **Description**  
`prop` | `com.google.storage.onestore.v3_bytes.proto2api.OnestoreEntity.Property`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
