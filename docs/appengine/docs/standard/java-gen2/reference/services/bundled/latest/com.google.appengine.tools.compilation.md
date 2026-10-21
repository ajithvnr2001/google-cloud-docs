---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.tools.compilation
title: Package com.google.appengine.tools.compilation (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:27:16.794593+00:00
---

# Package com.google.appengine.tools.compilation (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.tools.compilation

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Package com.google.appengine.tools.compilation (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 

## Classes 

### [DatastoreCallbacksProcessor](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.tools.compilation.DatastoreCallbacksProcessor)

Processes datastore callback annotations ( [PrePut](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PrePut), [PostPut](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PostPut), [PreDelete](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PreDelete), [PostDelete](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PostDelete), [PreGet](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PreGet), [com.google.appengine.api.datastore.PostLoad](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PostLoad), [PreQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PreQuery)) and generates a config file that the Datastore API can load at runtime. Each line of the config file is of the format:   
kind.callback_type=comma-separated list of methods  
where 'kind' is the kind of the entity to which the config on that line applies, 'callback_type' is one of PrePut, PostPut, PreDelete, PostDelete, and each entry in the comma-separated list of methods is a colon-delimited fully-qualified classname:method name tuple. So for example, if the dev wants a method named 'prePutCallback1' belonging to class 'com.example.MyCallbacks and a method named 'prePutCallback2' belonging to the same class to be invoked before any entity of kind 'yar' is put, the config file will look like this: 

> yar.PrePut=com.example.MyCallbacks:prePutCallback1,com.example.MyCallbacks:prePutCallback2

Note that it is possible to have a line which refers to all kinds by omitting the kind name: 

> .PreDelete=com.example.MyCallbacks:preDeleteCallback1

Each type of callback has its own signature requirements for the methods it annotates. If any of these signature requirements are violated the processor will produce an error. See the javadoc for the annotations for more information about the callback-specific signature requirements.

Processor Options:

  * debug - turns on debug statements



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
