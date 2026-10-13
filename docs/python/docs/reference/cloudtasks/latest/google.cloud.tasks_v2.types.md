---
url: https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.types
title: Package types (2.26.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:31:59.818143+00:00
---

# Package types (2.26.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.types

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package types (2.26.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.26.0 (latest)  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.3  2.18.0  2.17.1  2.16.5  2.15.1  2.14.2  2.13.2  2.12.1  2.11.0  2.10.4  2.9.1  2.8.1  2.7.2  2.6.0  2.5.3  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.5.2  1.4.0  1.3.0  1.2.1 

API documentation for `tasks_v2.types` package.

## Classes 

### [AppEngineHttpRequest](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.types.AppEngineHttpRequest)

App Engine HTTP request.

The message defines the HTTP request that is sent to an App Engine app when the task is dispatched.

Using AppEngineHttpRequest requires ``appengine.applications.get` <https://cloud.google.com/appengine/docs/admin-api/access-control>`__ Google IAM permission for the project and the following scope:

`https://www.googleapis.com/auth/cloud-platform`

The task will be delivered to the App Engine app which belongs to the same project as the queue. For more information, see `How Requests are Routed <https://cloud.google.com/appengine/docs/standard/python/how-requests-are-routed>`**and how routing is affected by`dispatch files <https://cloud.google.com/appengine/docs/python/config/dispatchref>`**. Traffic is encrypted during transport and never leaves Google datacenters. Because this traffic is carried over a communication mechanism internal to Google, you cannot explicitly set the protocol (for example, HTTP or HTTPS). The request to the handler, however, will appear to have used the HTTP protocol.

The AppEngineRouting used to construct the URL that the task is delivered to can be set at the queue-level or task-level:

  * If [app_engine_routing_override is set on the queue][google.cloud.tasks.v2.Queue.app_engine_routing_override], this value is used for all tasks in the queue, no matter what the setting is for the [task-level app_engine_routing][google.cloud.tasks.v2.AppEngineHttpRequest.app_engine_routing].



The `url` that the task will be sent to is:

  * `url =` host `+` relative_uri



Tasks can be dispatched to secure app handlers, unsecure app handlers, and URIs restricted with `login: admin`` <https://cloud.google.com/appengine/docs/standard/python/config/appref>`__. Because tasks are not run as any user, they cannot be dispatched to URIs restricted with`login: required`` <https://cloud.google.com/appengine/docs/standard/python/config/appref>`__ Task dispatches also do not follow redirects.

The task attempt has succeeded if the app's request handler returns an HTTP response code in the range [`200` \- `299`]. The task attempt has failed if the app's handler returns a non-2xx response code or Cloud Tasks does not receive response before the deadline. Failed tasks will be retried according to the [retry configuration][google.cloud.tasks.v2.Queue.retry_config]. `503` (Service Unavailable) is considered an App Engine system error instead of an application error and will cause Cloud Tasks' traffic congestion control to temporarily throttle the queue's dispatches. Unlike other types of task targets, a `429` (Too Many Requests) response from an app handler does not cause traffic congestion control to throttle the queue.

### [AppEngineRouting](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.types.AppEngineRouting)

App Engine Routing.

Defines routing characteristics specific to App Engine - service, version, and instance.

For more information about services, versions, and instances see `An Overview of App Engine <https://cloud.google.com/appengine/docs/python/an-overview-of-app-engine>`**,`Microservices Architecture on Google App Engine <https://cloud.google.com/appengine/docs/python/microservices-on-app-engine>`**, `App Engine Standard request routing <https://cloud.google.com/appengine/docs/standard/python/how-requests-are-routed>`**, and`App Engine Flex request routing <https://cloud.google.com/appengine/docs/flexible/python/how-requests-are-routed>`**.

Using AppEngineRouting requires ``appengine.applications.get` <https://cloud.google.com/appengine/docs/admin-api/access-control>`__ Google IAM permission for the project and the following scope:

`https://www.googleapis.com/auth/cloud-platform`

### [Attempt](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.types.Attempt)

The status of a task attempt.

### [BatchCreateTasksMetadata](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.types.BatchCreateTasksMetadata)

Metadata message for [BatchCreateTasks].

### [BatchCreateTasksRequest](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.types.BatchCreateTasksRequest)

Request message for [BatchCreateTasks].

### [BatchCreateTasksResponse](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.types.BatchCreateTasksResponse)

Response message for [BatchCreateTasks].

### [BatchDeleteTasksMetadata](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.types.BatchDeleteTasksMetadata)

Metadata for the long-running operation returned by BatchDeleteTasks. This message is used to hold metadata information about the batch delete tasks operation; that is, it is put in `google.longrunning.Operation.metadata][google.longrunning.Operation.metadata]`.

### [BatchDeleteTasksRequest](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.types.BatchDeleteTasksRequest)

Request message for deleting a batch of tasks using BatchDeleteTasks.

### [CmekConfig](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.types.CmekConfig)

Describes the customer-managed encryption key (CMEK) configuration associated with a project and location.

### [CreateQueueRequest](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.types.CreateQueueRequest)

Request message for CreateQueue.

### [CreateTaskRequest](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.types.CreateTaskRequest)

Request message for CreateTask.

### [DeleteQueueRequest](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.types.DeleteQueueRequest)

Request message for DeleteQueue.

### [DeleteTaskRequest](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.types.DeleteTaskRequest)

Request message for deleting a task using DeleteTask.

### [GetCmekConfigRequest](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.types.GetCmekConfigRequest)

Request message for GetCmekConfig.

### [GetQueueRequest](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.types.GetQueueRequest)

Request message for GetQueue.

### [GetTaskRequest](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.types.GetTaskRequest)

Request message for getting a task using GetTask.

### [HttpMethod](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.types.HttpMethod)

The HTTP method used to deliver the task.

### [HttpRequest](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.types.HttpRequest)

HTTP request.

The task will be pushed to the worker as an HTTP request. If the worker or the redirected worker acknowledges the task by returning a successful HTTP response code ([`200` \- `299`]), the task will be removed from the queue. If any other HTTP response code is returned or no response is received, the task will be retried according to the following:

  * User-specified throttling: [retry configuration][google.cloud.tasks.v2.Queue.retry_config], [rate limits][google.cloud.tasks.v2.Queue.rate_limits], and the [queue's state][google.cloud.tasks.v2.Queue.state].

  * System throttling: To prevent the worker from overloading, Cloud Tasks may temporarily reduce the queue's effective rate. User-specified settings will not be changed.




System throttling happens because:

  * Cloud Tasks backs off on all errors. Normally the backoff specified in [rate limits][google.cloud.tasks.v2.Queue.rate_limits] will be used. But if the worker returns `429` (Too Many Requests), `503` (Service Unavailable), or the rate of errors is high, Cloud Tasks will use a higher backoff rate. The retry specified in the `Retry-After` HTTP response header is considered.

  * To prevent traffic spikes and to smooth sudden increases in traffic, dispatches ramp up slowly when the queue is newly created or idle and if large numbers of tasks suddenly become available to dispatch (due to spikes in create task rates, the queue being unpaused, or many tasks that are scheduled at the same time).




This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [HttpTarget](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.types.HttpTarget)

HTTP target.

When specified at the Queue level, all tasks with HttpRequest are overridden according to the target.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ListQueuesRequest](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.types.ListQueuesRequest)

Request message for ListQueues.

### [ListQueuesResponse](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.types.ListQueuesResponse)

Response message for ListQueues.

### [ListTasksRequest](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.types.ListTasksRequest)

Request message for listing tasks using ListTasks.

### [ListTasksResponse](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.types.ListTasksResponse)

Response message for listing tasks using ListTasks.

### [OAuthToken](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.types.OAuthToken)

Contains information needed for generating an `OAuth token <https://developers.google.com/identity/protocols/OAuth2>`__. This type of authorization should generally only be used when calling Google APIs hosted on *.googleapis.com.

### [OidcToken](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.types.OidcToken)

Contains information needed for generating an `OpenID Connect token <https://developers.google.com/identity/protocols/OpenIDConnect>`__. This type of authorization can be used for many scenarios, including calling Cloud Run, or endpoints where you intend to validate the token yourself.

### [PathOverride](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.types.PathOverride)

PathOverride.

Path message defines path override for HTTP targets.

### [PauseQueueRequest](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.types.PauseQueueRequest)

Request message for PauseQueue.

### [PurgeQueueRequest](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.types.PurgeQueueRequest)

Request message for PurgeQueue.

### [QueryOverride](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.types.QueryOverride)

QueryOverride.

Query message defines query override for HTTP targets.

### [Queue](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.types.Queue)

A queue is a container of related tasks. Queues are configured to manage how those tasks are dispatched. Configurable properties include rate limits, retry options, queue types, and others.

### [RateLimits](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.types.RateLimits)

Rate limits.

This message determines the maximum rate that tasks can be dispatched by a queue, regardless of whether the dispatch is a first task attempt or a retry.

Note: The debugging command, RunTask, will run a task even if the queue has reached its RateLimits.

### [ResumeQueueRequest](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.types.ResumeQueueRequest)

Request message for ResumeQueue.

### [RetryConfig](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.types.RetryConfig)

Retry config.

These settings determine when a failed task attempt is retried.

### [RunTaskRequest](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.types.RunTaskRequest)

Request message for forcing a task to run now using RunTask.

### [StackdriverLoggingConfig](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.types.StackdriverLoggingConfig)

Configuration options for writing logs to `Stackdriver Logging <https://cloud.google.com/logging/docs/>`__.

### [Task](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.types.Task)

A unit of scheduled work.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [UpdateCmekConfigRequest](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.types.UpdateCmekConfigRequest)

Request message for UpdateCmekConfig.

### [UpdateQueueRequest](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.types.UpdateQueueRequest)

Request message for UpdateQueue.

### [UriOverride](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.types.UriOverride)

URI Override.

When specified, all the HTTP tasks inside the queue will be partially or fully overridden depending on the configured values.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
