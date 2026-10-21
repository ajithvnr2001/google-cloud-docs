---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/queueinfo/
title: Module: google.appengine.api.queueinfo \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:15:32.254054+00:00
---

# Module: google.appengine.api.queueinfo  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/queueinfo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Module: google.appengine.api.queueinfo Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/queueinfo.py) QueueInfo tools. QueueInfo is a library for working with QueueInfo records, describing task queue entries for an application. QueueInfo loads the records from `queue.yaml`. To learn more about the parameters you can specify in `queue.yaml`, review the `queue.yaml` reference guide: https://cloud.google.com/appengine/docs/python/config/queueref

## Classes

[`class Acl`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/queueinfo/Acl): Controls the access control list for a single task queue. [`class MalformedQueueConfiguration`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/queueinfo/MalformedQueueConfiguration): The configuration file for the task queue is malformed. [`class QueueEntry`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/queueinfo/QueueEntry): Describes a single task queue. [`class QueueInfoExternal`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/queueinfo/QueueInfoExternal): Describes all of the queue entries for an application. [`class RetryParameters`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/queueinfo/RetryParameters): Specifies the retry parameters for a single task queue.

## Functions

[`LoadSingleQueue(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/queueinfo/LoadSingleQueue): Loads a `queue.yaml` file/string and returns a `QueueInfoExternal` object. [`ParseRate(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/queueinfo/ParseRate): Parses a rate string in the form `number/unit`, or the literal `0`. [`ParseTaskAgeLimit(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/queueinfo/ParseTaskAgeLimit): Parses a string representing the task's age limit (maximum allowed age). [`ParseTotalStorageLimit(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/queueinfo/ParseTotalStorageLimit): Parses a string representing the storage bytes limit. [`TranslateRetryParameters(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/queueinfo/TranslateRetryParameters): Populates a `TaskQueueRetryParameters` from a [`queueinfo.RetryParameters`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/queueinfo/RetryParameters). | 

## Other Members  
  
---  
  
ACL |  `'acl'`  
BUCKET_SIZE |  `'bucket_size'`  
BYTE_SUFFIXES |  `'BKMGT'`  
MAX_BACKOFF_SECONDS |  `'max_backoff_seconds'`  
MAX_CONCURRENT_REQUESTS |  `'max_concurrent_requests'`  
MAX_DOUBLINGS |  `'max_doublings'`  
MIN_BACKOFF_SECONDS |  `'min_backoff_seconds'`  
MODE |  `'mode'`  
MODULE_ID_RE_STRING |  `'(?!-)[a-z\\d\\-]{1,63}'`  
MODULE_VERSION_RE_STRING |  `'(?!-)[a-z\\d\\-]{1,100}'`  
NAME |  `'name'`  
QUEUE |  `'queue'`  
RATE |  `'rate'`  
RESUME_PAUSED_QUEUES |  `'resume_paused_queues'`  
RETRY_PARAMETERS |  `'retry_parameters'`  
TARGET |  `'target'`  
TASK_AGE_LIMIT |  `'task_age_limit'`  
TASK_RETRY_LIMIT |  `'task_retry_limit'`  
TOTAL_STORAGE_LIMIT |  `'total_storage_limit'`  
USER_EMAIL |  `'user_email'`  
WRITER_EMAIL |  `'writer_email'`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
