---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PreDelete
title: Annotation Type PreDelete (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:10:21.349129+00:00
---

# Annotation Type PreDelete (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PreDelete

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Annotation Type PreDelete (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public interface PreDelete implements Annotation

Identifies a callback method to be invoked before an [Entity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity) of any of the specified kinds is deleted from the datastore. If [#kinds()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PreDelete#com_google_appengine_api_datastore_PreDelete_kinds__) is not provided the callback will execute for all kinds. Methods with this annotation must return `void`, must accept a single argument of type [DeleteContext](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DeleteContext), must not throw any checked exceptions, must not be static, and must belong to a class with a no-arg constructor. Neither the method nor the no-arg constructor of the class to which it belongs are required to be public. Methods with this annotation are free to throw any unchecked exception they like. Throwing an unchecked exception will prevent callbacks that have not yet been executed from running, and the exception will propagate to the code that invoked the datastore operation that resulted in the invocation of the callback. Throwing an unchecked exception from a callback will prevent the datastore operation from executing.

## Implements

[Annotation](https://docs.oracle.com/javase/8/docs/api/java/lang/annotation/Annotation.html)

## Methods 

### kinds()
    
    
    public abstract String[] kinds()

The kinds to which this callback applies. The default value is an empty array, which indicates that the callback should run for all kinds.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)[]` | The kinds to which this callback applies.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
