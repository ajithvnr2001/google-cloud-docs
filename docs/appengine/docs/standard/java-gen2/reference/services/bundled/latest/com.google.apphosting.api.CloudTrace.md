---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.apphosting.api.CloudTrace
title: Class CloudTrace (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:53:20.461181+00:00
---

# Class CloudTrace (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.apphosting.api.CloudTrace

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class CloudTrace (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public abstract class CloudTrace

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > CloudTrace

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

### endSpan(ApiProxy.Environment arg0, CloudTraceContext arg1, CloudTraceContext arg2)
    
    
    public static void endSpan(ApiProxy.Environment arg0, CloudTraceContext arg1, CloudTraceContext arg2)

**Parameters**  
---  
**Name** | **Description**  
`arg0` | `[Environment](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.apphosting.api.ApiProxy.Environment)`  
  
`arg1` | `[CloudTraceContext](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.apphosting.api.CloudTraceContext)`  
  
`arg2` | `[CloudTraceContext](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.apphosting.api.CloudTraceContext)`  
  
  
### getCurrentContext(ApiProxy.Environment arg0)
    
    
    public static CloudTraceContext getCurrentContext(ApiProxy.Environment arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[Environment](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.apphosting.api.ApiProxy.Environment)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CloudTraceContext](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.apphosting.api.CloudTraceContext)` |   
  
### setCurrentContext(ApiProxy.Environment arg0, CloudTraceContext arg1)
    
    
    public static void setCurrentContext(ApiProxy.Environment arg0, CloudTraceContext arg1)

**Parameters**  
---  
**Name** | **Description**  
`arg0` | `[Environment](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.apphosting.api.ApiProxy.Environment)`  
  
`arg1` | `[CloudTraceContext](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.apphosting.api.CloudTraceContext)`  
  
  
### setLabel(ApiProxy.Environment arg0, CloudTraceContext arg1, String arg2, String arg3)
    
    
    public static void setLabel(ApiProxy.Environment arg0, CloudTraceContext arg1, String arg2, String arg3)

**Parameters**  
---  
**Name** | **Description**  
`arg0` | `[Environment](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.apphosting.api.ApiProxy.Environment)`  
  
`arg1` | `[CloudTraceContext](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.apphosting.api.CloudTraceContext)`  
  
`arg2` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`arg3` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
  
### startChildSpan(ApiProxy.Environment arg0, CloudTraceContext arg1, String arg2)
    
    
    public static CloudTraceContext startChildSpan(ApiProxy.Environment arg0, CloudTraceContext arg1, String arg2)

**Parameters**  
---  
**Name** | **Description**  
`arg0` | `[Environment](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.apphosting.api.ApiProxy.Environment)`  
  
`arg1` | `[CloudTraceContext](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.apphosting.api.CloudTraceContext)`  
  
`arg2` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CloudTraceContext](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.apphosting.api.CloudTraceContext)` |   
  
## Constructors 

### CloudTrace(ApiProxy.Environment arg0)
    
    
    public CloudTrace(ApiProxy.Environment arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[Environment](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.apphosting.api.ApiProxy.Environment)`  
  
  
## Methods 

### endSpanImpl(CloudTraceContext arg0)
    
    
    protected abstract void endSpanImpl(CloudTraceContext arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[CloudTraceContext](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.apphosting.api.CloudTraceContext)`  
  
  
### getDefaultContext()
    
    
    protected abstract CloudTraceContext getDefaultContext()

**Returns**  
---  
**Type** | **Description**  
`[CloudTraceContext](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.apphosting.api.CloudTraceContext)` |   
  
### setLabelImpl(CloudTraceContext arg0, String arg1, String arg2)
    
    
    protected abstract void setLabelImpl(CloudTraceContext arg0, String arg1, String arg2)

**Parameters**  
---  
**Name** | **Description**  
`arg0` | `[CloudTraceContext](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.apphosting.api.CloudTraceContext)`  
  
`arg1` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`arg2` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
  
### startChildSpanImpl(CloudTraceContext arg0, String arg1)
    
    
    protected abstract CloudTraceContext startChildSpanImpl(CloudTraceContext arg0, String arg1)

**Parameters**  
---  
**Name** | **Description**  
`arg0` | `[CloudTraceContext](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.apphosting.api.CloudTraceContext)`  
  
`arg1` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CloudTraceContext](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.apphosting.api.CloudTraceContext)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
