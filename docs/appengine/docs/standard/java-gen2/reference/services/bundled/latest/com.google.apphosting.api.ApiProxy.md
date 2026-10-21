---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.apphosting.api.ApiProxy
title: Class ApiProxy (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:08:27.641676+00:00
---

# Class ApiProxy (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.apphosting.api.ApiProxy

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class ApiProxy (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public class ApiProxy

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ApiProxy

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

### clearEnvironmentForCurrentThread()
    
    
    public static void clearEnvironmentForCurrentThread()

### flushLogs()
    
    
    public static void flushLogs()

### getCurrentEnvironment()
    
    
    public static ApiProxy.Environment getCurrentEnvironment()

**Returns**  
---  
**Type** | **Description**  
`[Environment](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.apphosting.api.ApiProxy.Environment)` |   
  
### getDelegate()
    
    
    public static ApiProxy.Delegate getDelegate()

**Returns**  
---  
**Type** | **Description**  
`[Delegate](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.apphosting.api.ApiProxy.Delegate)` |   
  
### getEnvironmentFactory()
    
    
    public static synchronized ApiProxy.EnvironmentFactory getEnvironmentFactory()

**Returns**  
---  
**Type** | **Description**  
`[EnvironmentFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.apphosting.api.ApiProxy.EnvironmentFactory)` |   
  
### getRequestThreads()
    
    
    public static List<Thread> getRequestThreads()

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Thread](https://docs.oracle.com/javase/8/docs/api/java/lang/Thread.html)>` |   
  
### log(ApiProxy.LogRecord arg0)
    
    
    public static void log(ApiProxy.LogRecord arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[LogRecord](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.apphosting.api.ApiProxy.LogRecord)`  
  
  
### makeAsyncCall(String arg0, String arg1, byte[] arg2)
    
    
    public static Future<byte[]> makeAsyncCall(String arg0, String arg1, byte[] arg2)

**Parameters**  
---  
**Name** | **Description**  
`arg0` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`arg1` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`arg2` | `byte[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<byte[]>` |   
  
### makeAsyncCall(String arg0, String arg1, byte[] arg2, ApiProxy.ApiConfig arg3)
    
    
    public static Future<byte[]> makeAsyncCall(String arg0, String arg1, byte[] arg2, ApiProxy.ApiConfig arg3)

**Parameters**  
---  
**Name** | **Description**  
`arg0` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`arg1` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`arg2` | `byte[]`  
  
`arg3` | `[ApiConfig](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.apphosting.api.ApiProxy.ApiConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<byte[]>` |   
  
### makeSyncCall(String arg0, String arg1, byte[] arg2)
    
    
    public static byte[] makeSyncCall(String arg0, String arg1, byte[] arg2)

**Parameters**  
---  
**Name** | **Description**  
`arg0` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`arg1` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`arg2` | `byte[]`  
  
**Returns**  
---  
**Type** | **Description**  
`byte[]` |   
  
### makeSyncCall(String arg0, String arg1, byte[] arg2, ApiProxy.ApiConfig arg3)
    
    
    public static byte[] makeSyncCall(String arg0, String arg1, byte[] arg2, ApiProxy.ApiConfig arg3)

**Parameters**  
---  
**Name** | **Description**  
`arg0` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`arg1` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`arg2` | `byte[]`  
  
`arg3` | `[ApiConfig](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.apphosting.api.ApiProxy.ApiConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`byte[]` |   
  
### setDelegate(ApiProxy.Delegate<?> arg0)
    
    
    public static void setDelegate(ApiProxy.Delegate<?> arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[Delegate](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.apphosting.api.ApiProxy.Delegate)<?>`  
  
  
### setEnvironmentFactory(ApiProxy.EnvironmentFactory arg0)
    
    
    public static synchronized void setEnvironmentFactory(ApiProxy.EnvironmentFactory arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[EnvironmentFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.apphosting.api.ApiProxy.EnvironmentFactory)`  
  
  
### setEnvironmentForCurrentThread(ApiProxy.Environment arg0)
    
    
    public static void setEnvironmentForCurrentThread(ApiProxy.Environment arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[Environment](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.apphosting.api.ApiProxy.Environment)`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
