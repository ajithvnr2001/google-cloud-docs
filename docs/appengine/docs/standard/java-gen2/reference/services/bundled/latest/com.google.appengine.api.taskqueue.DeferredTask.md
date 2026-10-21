---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.DeferredTask
title: Interface DeferredTask (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T02:08:23.435109+00:00
---

# Interface DeferredTask (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.DeferredTask

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Interface DeferredTask (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public interface DeferredTask extends Runnable, Serializable

Interface for deferred tasks. Classes implementing this interface may use [TaskOptions#payload(DeferredTask)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions#com_google_appengine_api_taskqueue_TaskOptions_payload_com_google_appengine_api_taskqueue_DeferredTask_) to serialize the [DeferredTask](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.DeferredTask) into the payload of the task definition. The DeferredTask#run() method will be called when the task is received by the built in DeferredTask servlet.

Normal return from this method is considered success and will not retry unless [DeferredTaskContext#markForRetry](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.DeferredTaskContext#com_google_appengine_api_taskqueue_DeferredTaskContext_markForRetry_) is called. Exceptions thrown from this method will indicate a failure and will be processed as a retry attempt unless [DeferredTaskContext#setDoNotRetry(boolean)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.DeferredTaskContext#com_google_appengine_api_taskqueue_DeferredTaskContext_setDoNotRetry_boolean_) was set to `true`.

## Implements

[Runnable](https://docs.oracle.com/javase/8/docs/api/java/lang/Runnable.html), [Serializable](https://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
