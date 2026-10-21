---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.CallbackContext
title: Interface CallbackContext<T> (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:07:44.708527+00:00
---

# Interface CallbackContext<T> (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.CallbackContext

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Interface CallbackContext<T> (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public interface CallbackContext<T>

Describes the context in which a callback runs. The context has access to the current transaction (if any), the element that the callback is operating on (eg the Entity being put or the Key being deleted), as well as all elements being operated on in the operation that triggered the callback..

## Type Parameter  
  
---  
**Name** | **Description**  
`T` |   
  
## Methods 

### getCurrentElement()
    
    
    public abstract T getCurrentElement()

Returns the element for which the callback has been invoked. Shortcut for ` getElements().getCurrentIndex()`.

**Returns**  
---  
**Type** | **Description**  
`T` |   
  
### getCurrentIndex()
    
    
    public abstract int getCurrentIndex()

Returns the index in the result of [#getElements()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.CallbackContext#com_google_appengine_api_datastore_CallbackContext_getElements__) of the element for which the callback has been invoked.

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getCurrentTransaction()
    
    
    public abstract Transaction getCurrentTransaction()

Returns the current transaction, or `null` if there is no current transaction.

**Returns**  
---  
**Type** | **Description**  
`[Transaction](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction)` |   
  
### getElements()
    
    
    public abstract List<T> getElements()

Returns an unmodifiable view of the elements involved in the operation that triggered the callback..

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<T>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
