---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GetRequest.Builder
title: Class GetRequest.Builder (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T07:04:08.844276+00:00
---

# Class GetRequest.Builder (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GetRequest.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class GetRequest.Builder (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public static class GetRequest.Builder

The builder of [GetRequest](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GetRequest)s.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > GetRequest.Builder

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
    
    
    protected Builder()

## Methods 

### build()
    
    
    public GetRequest build()

**Returns**  
---  
**Type** | **Description**  
`[GetRequest](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GetRequest)` | builds and returns a brand new instance of a [GetRequest](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GetRequest) using values set on this builder  
  
### setIncludeStart(boolean includeStart)
    
    
    public GetRequest.Builder setIncludeStart(boolean includeStart)

Sets whether or not to include the object whose ID is specified via the [#setStartId(String)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GetRequest.Builder#com_google_appengine_api_search_GetRequest_Builder_setStartId_java_lang_String_) method.

**Parameter**  
---  
**Name** | **Description**  
`includeStart` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
whether or not to return the start index  
**Returns**  
---  
**Type** | **Description**  
`[GetRequest.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GetRequest.Builder)` | this builder  
  
### setLimit(Integer limit)
    
    
    public GetRequest.Builder setLimit(Integer limit)

Sets the maximum number of objects to return.

**Parameter**  
---  
**Name** | **Description**  
`limit` | `[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)`  
the maximum number of objects to return  
**Returns**  
---  
**Type** | **Description**  
`[GetRequest.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GetRequest.Builder)` | this builder  
  
### setReturningIdsOnly(boolean returningIdsOnly)
    
    
    public GetRequest.Builder setReturningIdsOnly(boolean returningIdsOnly)

Sets whether just objects containing just their key are returned, or whether the complete objects are returned.

**Parameter**  
---  
**Name** | **Description**  
`returningIdsOnly` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
whether to only return object keys  
**Returns**  
---  
**Type** | **Description**  
`[GetRequest.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GetRequest.Builder)` | this builder  
  
### setStartId(String startId)
    
    
    public GetRequest.Builder setStartId(String startId)

Sets the Id of the first object to return. You may exclude this object by using the [#setIncludeStart(boolean)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GetRequest.Builder#com_google_appengine_api_search_GetRequest_Builder_setIncludeStart_boolean_) method.

**Parameter**  
---  
**Name** | **Description**  
`startId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the Id of the first object to return  
**Returns**  
---  
**Type** | **Description**  
`[GetRequest.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GetRequest.Builder)` | this builder  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
