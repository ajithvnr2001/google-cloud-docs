---
url: https://docs.cloud.google.com/tasks/docs/choose-task-creation-method/
title: Choose your task creation method \u00a0|\u00a0 Cloud Tasks \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:34:49.398693+00:00
---

# Choose your task creation method  |  Cloud Tasks  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tasks/docs/choose-task-creation-method/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Tasks ](https://docs.cloud.google.com/tasks/docs)
  * [ Guides ](https://docs.cloud.google.com/tasks/docs/dual-overview)



Send feedback 

#  Choose your task creation method Stay organized with collections  Save and categorize content based on your preferences. 

You can create HTTP tasks using either the `BufferTask` method or the `CreateTask` method. This page provides guidance on how to choose between the two methods for creating HTTP tasks.

The `BufferTask` method lets you create a task by sending an HTTP request to the queue. The `CreateTask` method lets you create a task by constructing the task object. For most use cases, explicitly constructing the task object is unnecessary. The best method for creating tasks depends on whether your queue has queue-level routing.

## Before you begin

Check the following list of use cases to see if any apply to you:

  * You want to create tasks using the RPC API or client libraries (rather than the REST API)
  * You want to create tasks as [App Engine task](https://docs.cloud.google.com/tasks/docs/dual-overview#appe) objects (rather than as the more typical task objects for generic HTTP targets which may or may not be App Engine targets)



If any of these apply to you, you don't need to choose your task creation method because only one method (the `CreateTask` method) is supported. Go directly to the `CreateTask` documentation for your task type:

  * [HTTP tasks](https://docs.cloud.google.com/tasks/docs/creating-http-target-tasks#createtask_method)
  * [App Engine tasks](https://docs.cloud.google.com/tasks/docs/creating-appengine-tasks)



## Check if your queue has queue-level routing

  1. Run the [gcloud tasks queues describe](https://docs.cloud.google.com/sdk/gcloud/reference/tasks/queues/describe) command in your terminal:
         
         gcloud tasks queues describe QUEUE_NAME \
             --location=LOCATION

Replace the following:

     * `QUEUE_NAME`: the name of your queue.
     * `LOCATION`: the [region](https://docs.cloud.google.com/tasks/docs/locations) where your queue is located. If not specified, and if there is an associated app, the location of your project's [App Engine app](https://docs.cloud.google.com/appengine/docs/standard/managing-projects-apps-billing) is used.
  2. In the output, look for the field `httpTarget` and check if the `uriOverride` has been set.

     * If the output includes a line for `uriOverride` with a `host` specified, your queue has queue-level routing. To choose your task creation method, see the section Queues with queue-level routing.

     * If the output does not include a line for `uriOverride` or if the `uriOverride` description does not show a `host` specified, your queue does not have queue-level routing. To choose your task creation method, see the section Queues without queue-level routing (or [configure queue-level routing](https://docs.cloud.google.com/tasks/docs/configuring-queues#configure_queue-level_routing_for_http_tasks)).




## Queues with queue-level routing

For queues with queue-level routing, the task creation method depends on the task's routing requirements:

  * **Task has the same routing requirements as specified at the queue level:** Use `BufferTask`. Learn how to create tasks with the [`BufferTask`](https://docs.cloud.google.com/tasks/docs/creating-http-target-tasks#buffertask_method) method.
  * **Task has different routing requirements from those specified at the queue-level:** Set the queue's [UriOverrideEnforceMode](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues#UriOverrideEnforceMode) to `IF_NOT_EXISTS` to ensure that the queue-level routing applies to tasks for which routing does not exist (for example, `BufferTask` tasks), but respects the routing of tasks that carry their own routing specifications. Then use `CreateTask`. This method lets you specify individual routing for the task. Learn how to create tasks with the [`CreateTask`](https://docs.cloud.google.com/tasks/docs/creating-http-target-tasks#createtask_method) method.



## Queues without queue-level routing

For queues without queue-level routing, create tasks by using the `CreateTask` method (or [configure](https://docs.cloud.google.com/tasks/docs/configuring-queues#configure_queue-level_routing_for_http_tasks) queue-level routing). The `CreateTask` method includes specifying routing for the task, which is required for queues that don't already have routing information at the queue-level. Learn how to create tasks with the [`CreateTask`](https://docs.cloud.google.com/tasks/docs/creating-http-target-tasks#createtask_method) method.

## Understand queue-level routing

Queue-level routing lets you specify default routing information for tasks based on the queue they're in. You can specify whether you want the default routing to apply only to tasks that don't have their own routing information, or to all tasks.

Choose queue-level routing if you want to:

  * Create tasks with standard HTTP requests (rather than by constructing the task object)
  * Use a queue as a buffer in front of a target service

**Note:** In the case of App Engine targets, any routing done by Cloud Tasks is handled prior to any routing defined in an [App Engine dispatch file](https://docs.cloud.google.com/appengine/docs/flexible/how-requests-are-routed?tab=python#dispatch). This dispatch file lets you send incoming requests to a specific service based on the path or hostname in the request URL.

### The per-target approach

Queue-level routing works best with architectures that use one queue for each target service. This model lets you:

  * Manage tasks based on their target (for example, redirecting a group of tasks if the target service is down)
  * Send all tasks in a queue to the same target
  * Create tasks without explicitly constructing the task object by using the `BufferTask` method



### Turning queue-level override behavior on and off

Once you configure queue-level routing, you can decide when it gets enforced by setting the queue's [UriOverrideEnforceMode](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues#UriOverrideEnforceMode).

  * `IF_NOT_EXISTS`: The queue-level routing applies only when a task doesn't contain its own routing information. Use this setting if you want the queue to be able to dispatch tasks to different targets.
  * `ALWAYS`: The queue-level routing always applies, even if a task contains its own routing information. Any routing information set at the task level is overridden by the queue-level routing. Use this setting if you want to require tasks in a given queue to use the same routing information.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
