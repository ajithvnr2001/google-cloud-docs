---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.utils
title: Package com.google.appengine.api.utils (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T10:48:58.679189+00:00
---

# Package com.google.appengine.api.utils (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.utils

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Package com.google.appengine.api.utils (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 

Provides common utility classes.

## Classes 

### [FutureWrapper<K,V>](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.utils.FutureWrapper)

`FutureWrapper` is a simple [Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html) that wraps a parent `Future`. This class is thread-safe.

### [HttpRequestParser](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.utils.HttpRequestParser)

`HttpRequestParser` encapsulates helper methods used to parse incoming ` multipart/form-data` HTTP requests. Subclasses should use these methods to parse specific requests into useful data structures.

### [HttpRequestParser.StaticDataSource](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.utils.HttpRequestParser.StaticDataSource)

A read-only [DataSource](https://docs.oracle.com/javase/8/docs/api/javax/activation/DataSource.html) backed by a content type and a fixed byte array.

### [SystemProperty](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.utils.SystemProperty)

Global system properties which are set by App Engine. 

Example code:
    
    
     if (SystemProperty.environment.value() == SystemProperty.Environment.Value.Production) {
       // do something that's production-only
     }
     String version = SystemProperty.version.get();
     

### [SystemProperty.Environment](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.utils.SystemProperty.Environment)

The current executing environment. Has the key, `"com.google.appengine.runtime.environment"`. The set of values are specified by Value.

## Enums 

### [SystemProperty.Environment.Value](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.utils.SystemProperty.Environment.Value)

The set of possible values for Environment.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
