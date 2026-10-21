---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.AdminDatastoreService.KeyBuilder
title: Class AdminDatastoreService.KeyBuilder (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:07:48.723987+00:00
---

# Class AdminDatastoreService.KeyBuilder (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.AdminDatastoreService.KeyBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class AdminDatastoreService.KeyBuilder (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public static final class AdminDatastoreService.KeyBuilder extends AdminDatastoreService.AbstractKeyBuilder<AdminDatastoreService.KeyBuilder>

A [Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key) builder that pins it to the AdminUtils `appId` and `namespace`.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > com.google.appengine.api.datastore.AdminDatastoreService.AbstractKeyBuilder > AdminDatastoreService.KeyBuilder

## Inherited Members

com.google.appengine.api.datastore.AdminDatastoreService.AbstractKeyBuilder.createKey()

com.google.appengine.api.datastore.AdminDatastoreService.AbstractKeyBuilder.getId()

com.google.appengine.api.datastore.AdminDatastoreService.AbstractKeyBuilder.getIdAsPrimitiveLong()

com.google.appengine.api.datastore.AdminDatastoreService.AbstractKeyBuilder.getKind()

com.google.appengine.api.datastore.AdminDatastoreService.AbstractKeyBuilder.getName()

com.google.appengine.api.datastore.AdminDatastoreService.AbstractKeyBuilder.getParent()

com.google.appengine.api.datastore.AdminDatastoreService.AbstractKeyBuilder.setId(java.lang.Long)

com.google.appengine.api.datastore.AdminDatastoreService.AbstractKeyBuilder.setKind(java.lang.String)

com.google.appengine.api.datastore.AdminDatastoreService.AbstractKeyBuilder.setName(java.lang.String)

com.google.appengine.api.datastore.AdminDatastoreService.AbstractKeyBuilder.setParent(com.google.appengine.api.datastore.Key)

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

## Methods 

### build()
    
    
    public Key build()

**Returns**  
---  
**Type** | **Description**  
`[Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
