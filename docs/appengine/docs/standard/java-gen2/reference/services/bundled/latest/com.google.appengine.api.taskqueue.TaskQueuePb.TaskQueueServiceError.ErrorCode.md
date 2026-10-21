---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskQueuePb.TaskQueueServiceError.ErrorCode
title: Enum TaskQueuePb.TaskQueueServiceError.ErrorCode (3.0.2) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:27:58.182432+00:00
---

# Enum TaskQueuePb.TaskQueueServiceError.ErrorCode (3.0.2)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskQueuePb.TaskQueueServiceError.ErrorCode

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)



Send feedback 

#  Enum TaskQueuePb.TaskQueueServiceError.ErrorCode (3.0.2) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public enum TaskQueuePb.TaskQueueServiceError.ErrorCode extends Enum<TaskQueuePb.TaskQueueServiceError.ErrorCode> implements ProtocolMessageEnum

## Implements

com.google.protobuf.ProtocolMessageEnum

## Inherited Members

[Enum.<T>valueOf(Class<T>,String)](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#valueOf-java.lang.Class-java.lang.String-)

[Enum.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#clone--)

[Enum.compareTo(E)](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#compareTo-E-)

[Enum.describeConstable()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#describeConstable--)

[Enum.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#equals-java.lang.Object-)

[Enum.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#finalize--)

[Enum.getDeclaringClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#getDeclaringClass--)

[Enum.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#hashCode--)

[Enum.name()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#name--)

[Enum.ordinal()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#ordinal--)

[Enum.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#toString--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Static Fields   
  
---  
**Name** | **Description**  
`ACL_LOOKUP_ERROR` |   
`ACL_LOOKUP_ERROR_VALUE` |   
`DATASTORE_ABORTED` |   
`DATASTORE_ABORTED_VALUE` |   
`DATASTORE_ALREADY_EXISTS` |   
`DATASTORE_ALREADY_EXISTS_VALUE` |   
`DATASTORE_BAD_REQUEST` |   
`DATASTORE_BAD_REQUEST_VALUE` |   
`DATASTORE_BIGTABLE_ERROR` |   
`DATASTORE_BIGTABLE_ERROR_VALUE` |   
`DATASTORE_CAPABILITY_DISABLED` |   
`DATASTORE_CAPABILITY_DISABLED_VALUE` |   
`DATASTORE_COMMITTED_BUT_STILL_APPLYING` |   
`DATASTORE_COMMITTED_BUT_STILL_APPLYING_VALUE` |   
`DATASTORE_CONCURRENT_TRANSACTION` |   
`DATASTORE_CONCURRENT_TRANSACTION_VALUE` |   
`DATASTORE_ERROR` |   
`DATASTORE_ERROR_VALUE` |   
`DATASTORE_FAILED_PRECONDITION` |   
`DATASTORE_FAILED_PRECONDITION_VALUE` |   
`DATASTORE_INTERNAL_ERROR` |   
`DATASTORE_INTERNAL_ERROR_VALUE` |   
`DATASTORE_NEED_INDEX` |   
`DATASTORE_NEED_INDEX_VALUE` |   
`DATASTORE_NOT_FOUND` |   
`DATASTORE_NOT_FOUND_VALUE` |   
`DATASTORE_PERMISSION_DENIED` |   
`DATASTORE_PERMISSION_DENIED_VALUE` |   
`DATASTORE_RESOURCE_EXHAUSTED` |   
`DATASTORE_RESOURCE_EXHAUSTED_VALUE` |   
`DATASTORE_SAFE_TIME_TOO_OLD` |   
`DATASTORE_SAFE_TIME_TOO_OLD_VALUE` |   
`DATASTORE_SNAPSHOT_VERSION_TOO_OLD` |   
`DATASTORE_SNAPSHOT_VERSION_TOO_OLD_VALUE` |   
`DATASTORE_TIMEOUT` |   
`DATASTORE_TIMEOUT_VALUE` |   
`DATASTORE_TRY_ALTERNATE_BACKEND` |   
`DATASTORE_TRY_ALTERNATE_BACKEND_VALUE` |   
`DATASTORE_UNAUTHENTICATED` |   
`DATASTORE_UNAUTHENTICATED_VALUE` |   
`DUPLICATE_TASK_NAME` |   
`DUPLICATE_TASK_NAME_VALUE` |   
`INCORRECT_CREATOR_NAME` |   
`INCORRECT_CREATOR_NAME_VALUE` |   
`INTERNAL_ERROR` |   
`INTERNAL_ERROR_VALUE` |   
`INVALID_DISPATCH_DEADLINE` |   
`INVALID_DISPATCH_DEADLINE_VALUE` |   
`INVALID_ETA` |   
`INVALID_ETA_VALUE` |   
`INVALID_LOGGING_CONFIG` |   
`INVALID_LOGGING_CONFIG_VALUE` |   
`INVALID_PAYLOAD` |   
`INVALID_PAYLOAD_VALUE` |   
`INVALID_QUEUE_MODE` |   
`INVALID_QUEUE_MODE_VALUE` |   
`INVALID_QUEUE_NAME` |   
`INVALID_QUEUE_NAME_VALUE` |   
`INVALID_QUEUE_RATE` |   
`INVALID_QUEUE_RATE_VALUE` |   
`INVALID_REQUEST` |   
`INVALID_REQUEST_VALUE` |   
`INVALID_RETRY_PARAMETERS` |   
`INVALID_RETRY_PARAMETERS_VALUE` |   
`INVALID_TAG` |   
`INVALID_TAG_VALUE` |   
`INVALID_TASK_NAME` |   
`INVALID_TASK_NAME_VALUE` |   
`INVALID_URL` |   
`INVALID_URL_VALUE` |   
`OK` |   
`OK_VALUE` |   
`PERMISSION_DENIED` |   
`PERMISSION_DENIED_VALUE` |   
`QUEUE_PAUSED` |   
`QUEUE_PAUSED_VALUE` |   
`SKIPPED` |   
`SKIPPED_VALUE` |   
`TASK_ALREADY_EXISTS` |   
`TASK_ALREADY_EXISTS_VALUE` |   
`TASK_LEASE_EXPIRED` |   
`TASK_LEASE_EXPIRED_VALUE` |   
`TASK_TOO_LARGE` |   
`TASK_TOO_LARGE_VALUE` |   
`TOMBSTONED_QUEUE` |   
`TOMBSTONED_QUEUE_VALUE` |   
`TOMBSTONED_TASK` |   
`TOMBSTONED_TASK_VALUE` |   
`TOO_MANY_TASKS` |   
`TOO_MANY_TASKS_VALUE` |   
`TRANSACTIONAL_REQUEST_TOO_LARGE` |   
`TRANSACTIONAL_REQUEST_TOO_LARGE_VALUE` |   
`TRANSIENT_ERROR` |   
`TRANSIENT_ERROR_VALUE` |   
`UNKNOWN_QUEUE` |   
`UNKNOWN_QUEUE_VALUE` |   
`UNKNOWN_TASK` |   
`UNKNOWN_TASK_VALUE` |   
  
## Static Methods   
  
---  
**Name** | **Description**  
`forNumber(int arg0)` |   
`getDescriptor()` |   
`internalGetValueMap()` |   
`valueOf(Descriptors.EnumValueDescriptor arg0)` |   
`valueOf(int arg0)` |   
`valueOf(String arg0)` |   
`values()` |   
  
## Methods   
  
---  
**Name** | **Description**  
`getDescriptorForType()` |   
`getNumber()` |   
`getValueDescriptor()` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-06 UTC."],[],[]] 
