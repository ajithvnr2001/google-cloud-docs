---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.setup.ApiProxyEnvironment
title: Class ApiProxyEnvironment (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T12:34:29.272727+00:00
---

# Class ApiProxyEnvironment (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.setup.ApiProxyEnvironment

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class ApiProxyEnvironment (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public class ApiProxyEnvironment implements ApiProxy.Environment

Implements the ApiProxy environment. 

Supports instantiation within a request as well as outside the context of a request. 

Instances should be registered using ApiProxy.setEnvironmentForCurrentThread(Environment).

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ApiProxyEnvironment

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

## Static Fields 

### AUTH_DOMAIN_HEADER
    
    
    public static final String AUTH_DOMAIN_HEADER

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### BACKEND_ID_KEY
    
    
    public static final String BACKEND_ID_KEY

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### BACKGROUND_THREAD_FACTORY_ATTR
    
    
    public static final String BACKGROUND_THREAD_FACTORY_ATTR

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### EMAIL_HEADER
    
    
    public static final String EMAIL_HEADER

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### INSTANCE_ID_KEY
    
    
    public static final String INSTANCE_ID_KEY

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### IS_ADMIN_HEADER
    
    
    public static final String IS_ADMIN_HEADER

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### IS_FEDERATED_USER_KEY
    
    
    public static final String IS_FEDERATED_USER_KEY

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### IS_TRUSTED_IP_HEADER
    
    
    public static final String IS_TRUSTED_IP_HEADER

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### IS_TRUSTED_IP_KEY
    
    
    public static final String IS_TRUSTED_IP_KEY

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### REQUEST_THREAD_FACTORY_ATTR
    
    
    public static final String REQUEST_THREAD_FACTORY_ATTR

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### TICKET_HEADER
    
    
    public static final String TICKET_HEADER

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
## Static Methods 

### createFromHeaders(Map<String,String> envMap, HttpRequest request, String server, Timer wallTimer, Long millisUntilSoftDeadline)
    
    
    public static ApiProxyEnvironment createFromHeaders(Map<String,String> envMap, HttpRequest request, String server, Timer wallTimer, Long millisUntilSoftDeadline)

**Parameters**  
---  
**Name** | **Description**  
`envMap` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
  
`request` | `[HttpRequest](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.setup.utils.http.HttpRequest)`  
  
`server` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`wallTimer` | `[Timer](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.setup.timer.Timer)`  
  
`millisUntilSoftDeadline` | `[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiProxyEnvironment](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.setup.ApiProxyEnvironment)` |   
  
## Constructors 

### ApiProxyEnvironment(String server, String ticket, String appId, String service, String version, String instance, String email, boolean admin, String authDomain, Timer wallTimer, Long millisUntilSoftDeadline, Map<String,Object> attributes)
    
    
    public ApiProxyEnvironment(String server, String ticket, String appId, String service, String version, String instance, String email, boolean admin, String authDomain, Timer wallTimer, Long millisUntilSoftDeadline, Map<String,Object> attributes)

Constructs a VM AppEngine API environment.

**Parameters**  
---  
**Name** | **Description**  
`server` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the host:port address of the VM's HTTP proxy server.  
`ticket` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the request ticket (if null the default one will be computed).  
`appId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the application ID (required if ticket is null).  
`service` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the module name (required if ticket is null).  
`version` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the major application version (required if ticket is null).  
`instance` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the VM instance ID (required if ticket is null).  
`email` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the user's e-mail address (may be null).  
`admin` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
true if the user is an administrator.  
`authDomain` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the user's authentication domain (may be null).  
`wallTimer` | `[Timer](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.setup.timer.Timer)`  
optional wall clock timer for the current request (required for deadline).  
`millisUntilSoftDeadline` | `[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)`  
optional soft deadline in milliseconds relative to 'wallTimer'.  
`attributes` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)>`  
map containing any attributes set on this environment.  
  
## Methods 

### aSyncApiCallAdded(long maxWaitMs)
    
    
    public void aSyncApiCallAdded(long maxWaitMs)

Notifies the environment that an API call was queued up.

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

Notifies the environment that an API call completed.

### apiCallStarted(long maxWaitMs, boolean releasePendingCall)
    
    
    public void apiCallStarted(long maxWaitMs, boolean releasePendingCall)

Notifies the environment that an API call was started.

**Parameters**  
---  
**Name** | **Description**  
`maxWaitMs` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`releasePendingCall` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
If true a pending call semaphore will be released (required if this API call was requested asynchronously).  
**Exceptions**  
---  
**Type** | **Description**  
`[ApiProxyException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.apphosting.api.ApiProxy.ApiProxyException)` | If the thread was interrupted while waiting for a semaphore.  
  
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
