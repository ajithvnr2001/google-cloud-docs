---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQueryResult
title: Class LogQueryResult (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T22:30:41.249867+00:00
---

# Class LogQueryResult (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQueryResult

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class LogQueryResult (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public final class LogQueryResult implements Iterable<RequestLogs>

An object that is the result of performing a LogService.fetch() operation. LogQueryResults contain the logs from the user's query. Users of this service should use the [LogQueryResult#iterator](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQueryResult#com_google_appengine_api_log_LogQueryResult_iterator_) provided by this class to retrieve their results.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > LogQueryResult

## Implements

[Iterable<RequestLogs>](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable<com/google/appengine/api/log/RequestLogs>.html)

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

### parseOffset(String offset)
    
    
    protected static LogServicePb.LogOffset parseOffset(String offset)

Returns a LogOffset parsed from the submitted String, which is assumed to be a Base64-encoded offset produced by this class.

**Parameter**  
---  
**Name** | **Description**  
`offset` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.apphosting.api.logservice.LogServicePb.LogOffset` | A String to parse as a Base64-encoded LogOffset protocol buffer.  
  
## Constructors 

### LogQueryResult(LogServicePb.LogReadResponse response, LogQuery originalQuery)
    
    
    protected LogQueryResult(LogServicePb.LogReadResponse response, LogQuery originalQuery)

**Parameters**  
---  
**Name** | **Description**  
`response` | `com.google.apphosting.api.logservice.LogServicePb.LogReadResponse`  
  
`originalQuery` | `[LogQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery)`  
  
  
## Methods 

### iterator()
    
    
    public Iterator<RequestLogs> iterator()

Returns an Iterator that will yield all of the logs the user has requested. If the user has asked for more logs than a single request can accommodate (which is LogService.MAX_ITEMS_PER_FETCH), then this iterator grabs the first batch and returns them until they are exhausted. Once they are exhausted, a fetch() call is made to get more logs and the process is repeated until either all of the logs have been read or the user has stopped asking for more logs.

**Returns**  
---  
**Type** | **Description**  
`[Iterator](https://docs.oracle.com/javase/8/docs/api/java/util/Iterator.html)<[RequestLogs](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.RequestLogs)>` | An iterator that provides RequestLogs to the caller.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
