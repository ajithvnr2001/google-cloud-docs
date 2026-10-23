---
url: https://docs.cloud.google.com/tasks/docs/queue-yaml/
title: Use queue.yaml to manage queues \u00a0|\u00a0 Cloud Tasks \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:36:42.877236+00:00
---

# Use queue.yaml to manage queues  |  Cloud Tasks  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tasks/docs/queue-yaml/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Tasks ](https://docs.cloud.google.com/tasks/docs)
  * [ Guides ](https://docs.cloud.google.com/tasks/docs/dual-overview)



Send feedback 

#  Use queue.yaml to manage queues Stay organized with collections  Save and categorize content based on your preferences. 

While you can use a [`queue.yaml`](https://docs.cloud.google.com/appengine/docs/standard/reference/queueref) file to manage queues, mixing queue management methods can cause unexpected results. This guide explains the risks of mixing these methods and shows you how to resolve common configuration problems.

The Cloud Tasks API provides an independent interface to the [App Engine Task Queue](https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue) service. Using this interface, you can manage queues through the Google Cloud console or the Google Cloud CLI. Queues that you create with the Cloud Tasks API are accessible from the [App Engine SDK](https://docs.cloud.google.com/appengine/docs/standard/apis)—a collection of platform-specific APIs, standalone tools, and runtime files—and queues created with the App Engine SDK are accessible from the Cloud Tasks API.

To maintain compatibility, you can use `queue.yaml`, the configuration file for the App Engine SDK, to create and configure queues for the Cloud Tasks API. However, managing queues using this file as well as the Cloud Tasks API can cause issues that are detailed in this guide.

## Before you begin

**Caution:** We recommend that you use **either** the configuration file method **or** the Cloud Tasks API to configure your queues, but not both.

If you are new to Cloud Tasks or App Engine, use the Cloud Tasks API exclusively to manage your queues and avoid using `queue.yaml`. Cloud Tasks queue management methods give you more options for creating, updating, and deleting queues.

If you are an existing `queue.yaml` user, consider switching to Cloud Tasks queue management methods only if you understand the risks of mixing queue management methods.

### Enforce a queue management method

To prevent mixing queue management methods, you can create a web app or command-line tool for creating, updating, and deleting queues. Whether that tool uses Cloud Tasks queue management methods or `queue.yaml` is an implementation detail that users don't need to be aware of. By enforcing usage of the tool, you can ensure that there is no inadvertent mixing of methods. Grant the Cloud Tasks Queue Admin Identity and Access Management (IAM) role to the tool and require users to authenticate. For more information about access management, see [Secure queue configuration](https://docs.cloud.google.com/tasks/docs/secure-queue-configuration).

### Queue configuration delays

Queue configuration changes can require several minutes to take effect. For example, after calling `CreateQueue` or `UpdateQueue`, several minutes might pass before you can successfully call `CreateTask` on that queue.

### App Engine `default` queue

The App Engine queue named `default` receives special treatment in the App Engine SDK and in the Cloud Tasks API.

When is the `default` queue created?  
---  
If the `default` queue doesn't exist, it is created in these situations: | 

  * When a task is first added to the `default` queue using the App Engine SDK
  * When a `queue.yaml` file that specifies a `default` queue is uploaded 
  * When `CreateQueue` or `UpdateQueue` is called to create the `default` queue

  
What restrictions does Cloud Tasks enforce?  
To preserve compatibility with App Engine, Cloud Tasks enforces these restrictions regarding the `default` queue: | 

  * The Cloud Tasks API doesn't automatically create the `default` queue or any other queue
  * If a queue named `default` is created, it must be a queue using App Engine tasks
  * Calling `GetQueue` on the `default` queue returns a `not found` error if the queue doesn't yet exist
  * The `default` queue doesn't appear in the `ListQueues` output until it is created
  * You can modify the `default` queue configuration using the `UpdateQueue` call
  * After it is created, you can't delete the `default` queue 

  
  
## Risks of mixing queue management methods

For the underlying service, `queue.yaml` files are definitive. Uploading a `queue.yaml` file that omits existing queues in your project, regardless of how they were created, disables or [pauses](https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/push/deleting-tasks-and-queues#pausing_queues) those queues. For example, if you use the Cloud Tasks API to call `CreateQueue` or `UpdateQueue`, and then upload a `queue.yaml` file that omits those queues, the queues are disabled. You will then need to resume the disabled queues.

**Note:** The `default` queue is an exception. It is never disabled by App Engine. For more information, see App Engine `default` queue.

Mixing queue management methods can result in behavior that is unexpected. For example, consider the following scenarios:

**Scenario 1**

You call `CreateQueue` to create a queue named `cloud-tasks-queue` and then upload a `queue.yaml` file with the following contents:
    
    
    queue:
    - name: queue-yaml-queue
    

This results in the following queue states:

  * The queue named `cloud-tasks-queue` and any other pre-existing queues are in a `DISABLED` state.
  * The queue named `queue-yaml-queue` is in a `RUNNING` state.



**Scenario 2**

You use the Cloud Tasks API to disable a queue but it later appears in an uploaded `queue.yaml` file. The queue is resumed.

**Scenario 3**

You delete a queue with the `DeleteQueue` method and it later appears in a `queue.yaml` file. The `queue.yaml` upload might fail because [queue names can't be reused for several days](https://docs.cloud.google.com/tasks/docs/common-pitfalls#same-name-queue) after deletion.

### Debug using audit logs

You can inspect your project's [Admin Activity audit logs](https://docs.cloud.google.com/logging/docs/audit#admin-activity) and retrieve a history of queue configuration changes, including queue creations, updates, and deletions.

For example, if a `queue.yaml` upload disables an existing queue, you can run the following command to return a `Disabled queue QUEUE_NAME` log message through the `com.google.appengine.legacy.queue_updated` method:
    
    
    gcloud logging read \
      'protoPayload.methodName=
       (com.google.appengine.legacy.queue_created OR
        com.google.appengine.legacy.queue_updated OR
        google.cloud.tasks.v2.CloudTasks.CreateQueue OR
        google.cloud.tasks.v2.CloudTasks.UpdateQueue OR
        google.cloud.tasks.v2.CloudTasks.DeleteQueue)'
    

For more information, see [Reading log entries](https://docs.cloud.google.com/logging/docs/reference/tools/gcloud-logging#reading_log_entries).

### Resume a queue disabled by a `queue.yaml` upload

If you mix queue management methods, uploading a `queue.yaml` file might accidentally disable a queue created through the Cloud Tasks API. To resume the queue, you can either call `ResumeQueue` on the queue, or add it to `queue.yaml` and upload it.

**Warning:** Resuming many high-QPS queues simultaneously can lead to target overloading. If you are resuming high-QPS queues, follow the 500/50/5 pattern described in [Manage scaling risks](https://docs.cloud.google.com/tasks/docs/manage-cloud-task-scaling).

If you previously set a custom processing [`rate`](https://docs.cloud.google.com/appengine/docs/standard/reference/queueref#rate) in the `queue.yaml` configuration, `ResumeQueue` resets the queue to the default `rate`. This is reflected in the [`maxDispatchesPerSecond`](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues#RateLimits.FIELDS.max_dispatches_per_second) field of the response to `ResumeQueue`.

### Resolve quota issues

If you use `queue.yaml` to create your queues, your project has a default quota for the [maximum number of queues](https://docs.cloud.google.com/appengine/docs/standard/quotas#Task_Queue) you can create. Queues created using the Cloud Tasks API also have a [default quota](https://docs.cloud.google.com/tasks/docs/quotas). As in other cases, mixing `queue.yaml` and Cloud Tasks API methods can produce unexpected results.

For example, when you create queues using `queue.yaml` and then receive a quota increase, if you subsequently use the Cloud Tasks API to create additional queues, you might receive out-of-quota errors. To resolve this, you can manage your quotas using the Google Cloud console. For more information, see [Manage your quotas using the console](https://docs.cloud.google.com/docs/quotas/view-manage#managing_your_quota_console).

## What's next

  * [Cloud Tasks API REST overview](https://docs.cloud.google.com/tasks/docs/reference/rest)
  * [Cloud Tasks API RPC overview](https://docs.cloud.google.com/tasks/docs/reference/rpc)
  * [`queue.yaml` reference](https://docs.cloud.google.com/appengine/docs/standard/reference/queueref)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
