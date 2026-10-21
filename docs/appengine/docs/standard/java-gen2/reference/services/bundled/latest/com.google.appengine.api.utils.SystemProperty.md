---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.utils.SystemProperty
title: Class SystemProperty (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:51:13.642885+00:00
---

# Class SystemProperty (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.utils.SystemProperty

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class SystemProperty (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public class SystemProperty

Global system properties which are set by App Engine. 

Example code:
    
    
     if (SystemProperty.environment.value() == SystemProperty.Environment.Value.Production) {
       // do something that's production-only
     }
     String version = SystemProperty.version.get();
     

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > SystemProperty

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

### applicationId
    
    
    public static final SystemProperty applicationId

The application identifier for the current application. Has the key, `"com.google.appengine.application.id"`.

**Field Value**  
---  
**Type** | **Description**  
`[SystemProperty](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.utils.SystemProperty)` |   
  
### applicationVersion
    
    
    public static final SystemProperty applicationVersion

The version identifier for the current application version. Result is of the form 

**Field Value**  
---  
**Type** | **Description**  
`[SystemProperty](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.utils.SystemProperty)` |   
  
### environment
    
    
    public static final SystemProperty.Environment environment

The current executing environment. Has the key, `"com.google.appengine.runtime.environment"`. Has the values `"Production"` and `"Development"`.

**Field Value**  
---  
**Type** | **Description**  
`[SystemProperty.Environment](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.utils.SystemProperty.Environment)` |   
  
### instanceReplicaId (deprecated)
    
    
    public static final SystemProperty instanceReplicaId

**Deprecated.** _Use[com.google.appengine.api.modules.ModulesService#getCurrentInstanceId()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesService#com_google_appengine_api_modules_ModulesService_getCurrentInstanceId__)_

**Field Value**  
---  
**Type** | **Description**  
`[SystemProperty](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.utils.SystemProperty)` |   
  
### version
    
    
    public static final SystemProperty version

The current executing runtime version. Has the key, `"com.google.appengine.runtime.version"`. A Version value is composed of period-separated integers, for example, "1.2.8".

**Field Value**  
---  
**Type** | **Description**  
`[SystemProperty](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.utils.SystemProperty)` |   
  
## Methods 

### get()
    
    
    public @Nullable String get()

Gets the value of the system property. Equivalent to `System.getProperty(key())`.

**Returns**  
---  
**Type** | **Description**  
`[Nullable String](https://docs.oracle.com/javase/8/docs/api/java/lang/@org/jspecify/annotations/Nullable%20String.html)` |   
  
### key()
    
    
    public String key()

The key for the system property.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### set(String value)
    
    
    public void set(String value)

Sets the value of the system property. Equivalent to `System.setProperty(key(), value)`.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
