---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions.Builder
title: Class TaskOptions.Builder (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:41:06.562186+00:00
---

# Class TaskOptions.Builder (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class TaskOptions.Builder (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public static final class TaskOptions.Builder

Provides static creation methods for [TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions).

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > TaskOptions.Builder

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

### withCountdownMillis(long countdownMillis)
    
    
    public static TaskOptions withCountdownMillis(long countdownMillis)

Returns default [TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions) and calls [TaskOptions#countdownMillis(long)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions#com_google_appengine_api_taskqueue_TaskOptions_countdownMillis_long_).

**Parameter**  
---  
**Name** | **Description**  
`countdownMillis` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions)` |   
  
### withDefaults()
    
    
    public static TaskOptions withDefaults()

Returns default [TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions) with default values.

**Returns**  
---  
**Type** | **Description**  
`[TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions)` |   
  
### withEtaMillis(long etaMillis)
    
    
    public static TaskOptions withEtaMillis(long etaMillis)

Returns default [TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions) and calls [TaskOptions#etaMillis(long)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions#com_google_appengine_api_taskqueue_TaskOptions_etaMillis_long_).

**Parameter**  
---  
**Name** | **Description**  
`etaMillis` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions)` |   
  
### withHeader(String headerName, String value)
    
    
    public static TaskOptions withHeader(String headerName, String value)

Returns default [TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions) and calls [TaskOptions#header(String, String)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions#com_google_appengine_api_taskqueue_TaskOptions_header_java_lang_String_java_lang_String_).

**Parameters**  
---  
**Name** | **Description**  
`headerName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions)` |   
  
### withHeaders(Map<String,String> headers)
    
    
    public static TaskOptions withHeaders(Map<String,String> headers)

Returns default [TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions) and calls [TaskOptions#headers(Map)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions#com_google_appengine_api_taskqueue_TaskOptions_headers_java_util_Map_java_lang_String_java_lang_String__).

**Parameter**  
---  
**Name** | **Description**  
`headers` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions)` |   
  
### withMethod(TaskOptions.Method method)
    
    
    public static TaskOptions withMethod(TaskOptions.Method method)

Returns default [TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions) and calls [TaskOptions#method(Method)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions#com_google_appengine_api_taskqueue_TaskOptions_method_).

**Parameter**  
---  
**Name** | **Description**  
`method` | `[TaskOptions.Method](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions.Method)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions)` |   
  
### withParam(String paramName, byte[] value)
    
    
    public static TaskOptions withParam(String paramName, byte[] value)

Returns default [TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions) and calls [TaskOptions#param(String, byte[])](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions#com_google_appengine_api_taskqueue_TaskOptions_param_java_lang_String_byte___).

**Parameters**  
---  
**Name** | **Description**  
`paramName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`value` | `byte[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions)` |   
  
### withParam(String paramName, String value)
    
    
    public static TaskOptions withParam(String paramName, String value)

Returns default [TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions) and calls [TaskOptions#param(String, String)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions#com_google_appengine_api_taskqueue_TaskOptions_param_java_lang_String_java_lang_String_).

**Parameters**  
---  
**Name** | **Description**  
`paramName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions)` |   
  
### withPayload(byte[] payload, String contentType)
    
    
    public static TaskOptions withPayload(byte[] payload, String contentType)

Returns default [TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions) and calls [TaskOptions#payload(byte[], String)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions#com_google_appengine_api_taskqueue_TaskOptions_payload_byte___java_lang_String_).

**Parameters**  
---  
**Name** | **Description**  
`payload` | `byte[]`  
  
`contentType` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions)` |   
  
### withPayload(DeferredTask deferredTask)
    
    
    public static TaskOptions withPayload(DeferredTask deferredTask)

Returns default [TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions) and calls [TaskOptions#payload(DeferredTask)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions#com_google_appengine_api_taskqueue_TaskOptions_payload_com_google_appengine_api_taskqueue_DeferredTask_).

**Parameter**  
---  
**Name** | **Description**  
`deferredTask` | `[DeferredTask](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.DeferredTask)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions)` |   
  
### withPayload(String payload)
    
    
    public static TaskOptions withPayload(String payload)

Returns default [TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions) and calls [TaskOptions#payload(String)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions#com_google_appengine_api_taskqueue_TaskOptions_payload_java_lang_String_).

**Parameter**  
---  
**Name** | **Description**  
`payload` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions)` |   
  
### withPayload(String payload, String charset)
    
    
    public static TaskOptions withPayload(String payload, String charset)

Returns default [TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions) and calls [TaskOptions#payload(String, String)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions#com_google_appengine_api_taskqueue_TaskOptions_payload_java_lang_String_java_lang_String_).

**Parameters**  
---  
**Name** | **Description**  
`payload` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`charset` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions)` |   
  
### withRetryOptions(RetryOptions retryOptions)
    
    
    public static TaskOptions withRetryOptions(RetryOptions retryOptions)

Returns default [TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions) and calls [TaskOptions#retryOptions(RetryOptions)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions#com_google_appengine_api_taskqueue_TaskOptions_retryOptions_com_google_appengine_api_taskqueue_RetryOptions_).

**Parameter**  
---  
**Name** | **Description**  
`retryOptions` | `[RetryOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.RetryOptions)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions)` |   
  
### withTag(byte[] tag)
    
    
    public static TaskOptions withTag(byte[] tag)

Returns default [TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions) and calls [TaskOptions#tag(byte[])](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions#com_google_appengine_api_taskqueue_TaskOptions_tag_byte___).

**Parameter**  
---  
**Name** | **Description**  
`tag` | `byte[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions)` |   
  
### withTag(String tag)
    
    
    public static TaskOptions withTag(String tag)

Returns default [TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions) and calls [TaskOptions#tag(String)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions#com_google_appengine_api_taskqueue_TaskOptions_tag_java_lang_String_).

**Parameter**  
---  
**Name** | **Description**  
`tag` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions)` |   
  
### withTaskName(String taskName)
    
    
    public static TaskOptions withTaskName(String taskName)

Returns default [TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions) and calls [TaskOptions#taskName(String)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions#com_google_appengine_api_taskqueue_TaskOptions_taskName_java_lang_String_).

**Parameter**  
---  
**Name** | **Description**  
`taskName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions)` |   
  
### withUrl(String url)
    
    
    public static TaskOptions withUrl(String url)

Returns default [TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions) and calls [TaskOptions#url(String)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions#com_google_appengine_api_taskqueue_TaskOptions_url_java_lang_String_).

**Parameter**  
---  
**Name** | **Description**  
`url` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
