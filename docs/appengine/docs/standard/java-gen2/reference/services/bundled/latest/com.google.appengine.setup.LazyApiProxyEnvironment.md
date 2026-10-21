---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.setup.LazyApiProxyEnvironment
title: Class LazyApiProxyEnvironment (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:36:35.961066+00:00
---

# Class LazyApiProxyEnvironment (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.setup.LazyApiProxyEnvironment

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class LazyApiProxyEnvironment (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public class LazyApiProxyEnvironment implements ApiProxy.Environment

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > LazyApiProxyEnvironment

## Implements

[ApiProxy.Environment](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.apphosting.api.ApiProxy.Environment)

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

### LazyApiProxyEnvironment(Supplier<ApiProxyEnvironment> supplier)
    
    
    public LazyApiProxyEnvironment(Supplier<ApiProxyEnvironment> supplier)

**Parameter**  
---  
**Name** | **Description**  
`supplier` | `[Supplier](https://docs.oracle.com/javase/8/docs/api/java/util/function/Supplier.html)<[ApiProxyEnvironment](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.setup.ApiProxyEnvironment)>`  
  
  
## Methods 

### aSyncApiCallAdded(long maxWaitMs)
    
    
    public void aSyncApiCallAdded(long maxWaitMs)

**Parameter**  
---  
**Name** | **Description**  
`maxWaitMs` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Exceptions**  
---  
**Type** | **Description**  
`[ApiProxyException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.apphosting.api.ApiProxy.ApiProxyException)` |   
  
### addLogRecord(ApiProxy.LogRecord record)
    
    
    public void addLogRecord(ApiProxy.LogRecord record)

**Parameter**  
---  
**Name** | **Description**  
`record` | `[LogRecord](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.apphosting.api.ApiProxy.LogRecord)`  
  
  
### apiCallCompleted()
    
    
    public void apiCallCompleted()

### apiCallStarted(long maxWaitMs, boolean releasePendingCall)
    
    
    public void apiCallStarted(long maxWaitMs, boolean releasePendingCall)

**Parameters**  
---  
**Name** | **Description**  
`maxWaitMs` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`releasePendingCall` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Exceptions**  
---  
**Type** | **Description**  
`[ApiProxyException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.apphosting.api.ApiProxy.ApiProxyException)` |   
  
### flushLogs()
    
    
    public void flushLogs()

### getAppId()
    
    
    public String getAppId()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getAttributes()
    
    
    public Map<String,Object> getAttributes()

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)>` |   
  
### getAuthDomain()
    
    
    public String getAuthDomain()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getEmail()
    
    
    public String getEmail()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getModuleId()
    
    
    public String getModuleId()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getRemainingMillis()
    
    
    public long getRemainingMillis()

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getRequestNamespace()
    
    
    public String getRequestNamespace()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getServer()
    
    
    public String getServer()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getTicket()
    
    
    public String getTicket()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getVersionId()
    
    
    public String getVersionId()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### isAdmin()
    
    
    public boolean isAdmin()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### isLoggedIn()
    
    
    public boolean isLoggedIn()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
