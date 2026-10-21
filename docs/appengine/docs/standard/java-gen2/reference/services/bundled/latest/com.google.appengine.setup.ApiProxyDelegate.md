---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.setup.ApiProxyDelegate
title: Class ApiProxyDelegate (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T14:30:37.315578+00:00
---

# Class ApiProxyDelegate (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.setup.ApiProxyDelegate

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class ApiProxyDelegate (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public class ApiProxyDelegate implements ApiProxy.Delegate<LazyApiProxyEnvironment>

Delegates AppEngine API calls to a local http API proxy. 

Instances should be registered using ApiProxy.setDelegate(ApiProxy.Delegate).

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ApiProxyDelegate

## Implements

com.google.apphosting.api.ApiProxy.Delegate<com.google.appengine.setup.LazyApiProxyEnvironment>

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

### API_DEADLINE_KEY
    
    
    protected static final String API_DEADLINE_KEY

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### REQUEST_ENDPOINT
    
    
    public static final String REQUEST_ENDPOINT

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### REQUEST_STUB_ID
    
    
    public static final String REQUEST_STUB_ID

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### REQUEST_STUB_METHOD
    
    
    public static final String REQUEST_STUB_METHOD

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### RPC_DEADLINE_HEADER
    
    
    public static final String RPC_DEADLINE_HEADER

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### RPC_METHOD_HEADER
    
    
    public static final String RPC_METHOD_HEADER

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### RPC_STUB_ID_HEADER
    
    
    public static final String RPC_STUB_ID_HEADER

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
## Constructors 

### ApiProxyDelegate()
    
    
    public ApiProxyDelegate()

## Fields 

### defaultTimeoutMs
    
    
    protected int defaultTimeoutMs

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### executor
    
    
    protected final ExecutorService executor

**Field Value**  
---  
**Type** | **Description**  
`[ExecutorService](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ExecutorService.html)` |   
  
### httpclient
    
    
    protected final HttpClient httpclient

**Field Value**  
---  
**Type** | **Description**  
`org.apache.http.client.HttpClient` |   
  
## Methods 

### flushLogs(LazyApiProxyEnvironment environment)
    
    
    public void flushLogs(LazyApiProxyEnvironment environment)

**Parameter**  
---  
**Name** | **Description**  
`environment` | `[LazyApiProxyEnvironment](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.setup.LazyApiProxyEnvironment)`  
  
  
### getRequestThreads(LazyApiProxyEnvironment environment)
    
    
    public List<Thread> getRequestThreads(LazyApiProxyEnvironment environment)

**Parameter**  
---  
**Name** | **Description**  
`environment` | `[LazyApiProxyEnvironment](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.setup.LazyApiProxyEnvironment)`  
  
**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Thread](https://docs.oracle.com/javase/8/docs/api/java/lang/Thread.html)>` |   
  
### log(LazyApiProxyEnvironment environment, ApiProxy.LogRecord record)
    
    
    public void log(LazyApiProxyEnvironment environment, ApiProxy.LogRecord record)

**Parameters**  
---  
**Name** | **Description**  
`environment` | `[LazyApiProxyEnvironment](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.setup.LazyApiProxyEnvironment)`  
  
`record` | `[LogRecord](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.apphosting.api.ApiProxy.LogRecord)`  
  
  
### makeAsyncCall(LazyApiProxyEnvironment environment, String packageName, String methodName, byte[] request, ApiProxy.ApiConfig apiConfig)
    
    
    public Future<byte[]> makeAsyncCall(LazyApiProxyEnvironment environment, String packageName, String methodName, byte[] request, ApiProxy.ApiConfig apiConfig)

**Parameters**  
---  
**Name** | **Description**  
`environment` | `[LazyApiProxyEnvironment](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.setup.LazyApiProxyEnvironment)`  
  
`packageName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`methodName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`request` | `byte[]`  
  
`apiConfig` | `[ApiConfig](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.apphosting.api.ApiProxy.ApiConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<byte[]>` |   
  
### makeSyncCall(LazyApiProxyEnvironment environment, String packageName, String methodName, byte[] requestData)
    
    
    public byte[] makeSyncCall(LazyApiProxyEnvironment environment, String packageName, String methodName, byte[] requestData)

**Parameters**  
---  
**Name** | **Description**  
`environment` | `[LazyApiProxyEnvironment](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.setup.LazyApiProxyEnvironment)`  
  
`packageName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`methodName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`requestData` | `byte[]`  
  
**Returns**  
---  
**Type** | **Description**  
`byte[]` |   
**Exceptions**  
---  
**Type** | **Description**  
`[ApiProxyException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.apphosting.api.ApiProxy.ApiProxyException)` |   
  
### runSyncCall(LazyApiProxyEnvironment environment, String packageName, String methodName, byte[] requestData, int timeoutMs)
    
    
    protected byte[] runSyncCall(LazyApiProxyEnvironment environment, String packageName, String methodName, byte[] requestData, int timeoutMs)

**Parameters**  
---  
**Name** | **Description**  
`environment` | `[LazyApiProxyEnvironment](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.setup.LazyApiProxyEnvironment)`  
  
`packageName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`methodName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`requestData` | `byte[]`  
  
`timeoutMs` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`byte[]` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
