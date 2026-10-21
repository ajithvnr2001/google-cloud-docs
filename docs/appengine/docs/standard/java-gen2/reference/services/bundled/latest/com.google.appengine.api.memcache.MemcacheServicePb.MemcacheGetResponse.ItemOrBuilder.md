---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheGetResponse.ItemOrBuilder
title: Interface MemcacheServicePb.MemcacheGetResponse.ItemOrBuilder (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:13:40.726206+00:00
---

# Interface MemcacheServicePb.MemcacheGetResponse.ItemOrBuilder (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheGetResponse.ItemOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Interface MemcacheServicePb.MemcacheGetResponse.ItemOrBuilder (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public static interface MemcacheServicePb.MemcacheGetResponse.ItemOrBuilder extends MessageOrBuilder

## Implements

com.google.protobuf.MessageOrBuilder

## Methods 

### getCasId()
    
    
    public abstract long getCasId()

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getExpiresInSeconds()
    
    
    public abstract int getExpiresInSeconds()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getFlags()
    
    
    public abstract int getFlags()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getIsDeleteLocked()
    
    
    public abstract boolean getIsDeleteLocked()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getKey()
    
    
    public abstract ByteString getKey()

**Returns**  
---  
**Type** | **Description**  
`com.google.protobuf.ByteString` |   
  
### getTimestamps()
    
    
    public abstract MemcacheServicePb.ItemTimestamps getTimestamps()

**Returns**  
---  
**Type** | **Description**  
`[ItemTimestamps](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.ItemTimestamps)` |   
  
### getTimestampsOrBuilder()
    
    
    public abstract MemcacheServicePb.ItemTimestampsOrBuilder getTimestampsOrBuilder()

**Returns**  
---  
**Type** | **Description**  
`[ItemTimestampsOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.ItemTimestampsOrBuilder)` |   
  
### getValue()
    
    
    public abstract ByteString getValue()

**Returns**  
---  
**Type** | **Description**  
`com.google.protobuf.ByteString` |   
  
### hasCasId()
    
    
    public abstract boolean hasCasId()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### hasExpiresInSeconds()
    
    
    public abstract boolean hasExpiresInSeconds()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### hasFlags()
    
    
    public abstract boolean hasFlags()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### hasIsDeleteLocked()
    
    
    public abstract boolean hasIsDeleteLocked()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### hasKey()
    
    
    public abstract boolean hasKey()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### hasTimestamps()
    
    
    public abstract boolean hasTimestamps()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### hasValue()
    
    
    public abstract boolean hasValue()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
