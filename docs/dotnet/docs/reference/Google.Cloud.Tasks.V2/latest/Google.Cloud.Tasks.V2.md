---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2
title: Google Cloud Tasks v2 API - Namespace Google.Cloud.Tasks.V2 (3.7.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:32:21.592154+00:00
---

# Google Cloud Tasks v2 API - Namespace Google.Cloud.Tasks.V2 (3.7.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Tasks v2 API - Namespace Google.Cloud.Tasks.V2 (3.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.7.0 (latest)  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.5.0  2.4.0  2.3.0  2.2.0 

## Classes 

### [AppEngineHttpRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.AppEngineHttpRequest)

App Engine HTTP request.

The message defines the HTTP request that is sent to an App Engine app when the task is dispatched.

Using [AppEngineHttpRequest][google.cloud.tasks.v2.AppEngineHttpRequest] requires [`appengine.applications.get`](https://cloud.google.com/appengine/docs/admin-api/access-control) Google IAM permission for the project and the following scope:

`https://www.googleapis.com/auth/cloud-platform`

The task will be delivered to the App Engine app which belongs to the same project as the queue. For more information, see [How Requests are Routed](https://cloud.google.com/appengine/docs/standard/python/how-requests-are-routed) and how routing is affected by [dispatch files](https://cloud.google.com/appengine/docs/python/config/dispatchref). Traffic is encrypted during transport and never leaves Google datacenters. Because this traffic is carried over a communication mechanism internal to Google, you cannot explicitly set the protocol (for example, HTTP or HTTPS). The request to the handler, however, will appear to have used the HTTP protocol.

The [AppEngineRouting][google.cloud.tasks.v2.AppEngineRouting] used to construct the URL that the task is delivered to can be set at the queue-level or task-level:

  * If [app_engine_routing_override is set on the queue][google.cloud.tasks.v2.Queue.app_engine_routing_override], this value is used for all tasks in the queue, no matter what the setting is for the [task-level app_engine_routing][google.cloud.tasks.v2.AppEngineHttpRequest.app_engine_routing].



The `url` that the task will be sent to is:

  * `url =` [host][google.cloud.tasks.v2.AppEngineRouting.host] `+` [relative_uri][google.cloud.tasks.v2.AppEngineHttpRequest.relative_uri]



Tasks can be dispatched to secure app handlers, unsecure app handlers, and URIs restricted with [`login: admin`](https://cloud.google.com/appengine/docs/standard/python/config/appref). Because tasks are not run as any user, they cannot be dispatched to URIs restricted with [`login: required`](https://cloud.google.com/appengine/docs/standard/python/config/appref) Task dispatches also do not follow redirects.

The task attempt has succeeded if the app's request handler returns an HTTP response code in the range [`200` \- `299`]. The task attempt has failed if the app's handler returns a non-2xx response code or Cloud Tasks does not receive response before the [deadline][google.cloud.tasks.v2.Task.dispatch_deadline]. Failed tasks will be retried according to the [retry configuration][google.cloud.tasks.v2.Queue.retry_config]. `503` (Service Unavailable) is considered an App Engine system error instead of an application error and will cause Cloud Tasks' traffic congestion control to temporarily throttle the queue's dispatches. Unlike other types of task targets, a `429` (Too Many Requests) response from an app handler does not cause traffic congestion control to throttle the queue.

### [AppEngineRouting](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.AppEngineRouting)

App Engine Routing.

Defines routing characteristics specific to App Engine - service, version, and instance.

For more information about services, versions, and instances see [An Overview of App Engine](https://cloud.google.com/appengine/docs/python/an-overview-of-app-engine), [Microservices Architecture on Google App Engine](https://cloud.google.com/appengine/docs/python/microservices-on-app-engine), [App Engine Standard request routing](https://cloud.google.com/appengine/docs/standard/python/how-requests-are-routed), and [App Engine Flex request routing](https://cloud.google.com/appengine/docs/flexible/python/how-requests-are-routed).

Using [AppEngineRouting][google.cloud.tasks.v2.AppEngineRouting] requires [`appengine.applications.get`](https://cloud.google.com/appengine/docs/admin-api/access-control) Google IAM permission for the project and the following scope:

`https://www.googleapis.com/auth/cloud-platform`

### [Attempt](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Attempt)

The status of a task attempt.

### [BatchCreateTasksMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchCreateTasksMetadata)

Metadata message for [BatchCreateTasks].

### [BatchCreateTasksMetadata.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchCreateTasksMetadata.Types)

Container for nested types declared in the BatchCreateTasksMetadata message type.

### [BatchCreateTasksRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchCreateTasksRequest)

Request message for [BatchCreateTasks].

### [BatchCreateTasksResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchCreateTasksResponse)

Response message for [BatchCreateTasks].

### [BatchDeleteTasksMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchDeleteTasksMetadata)

Metadata for the long-running operation returned by [BatchDeleteTasks][google.cloud.tasks.v2.CloudTasks.BatchDeleteTasks]. This message is used to hold metadata information about the batch delete tasks operation; that is, it is put in [google.longrunning.Operation.metadata][google.longrunning.Operation.metadata].

### [BatchDeleteTasksMetadata.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchDeleteTasksMetadata.Types)

Container for nested types declared in the BatchDeleteTasksMetadata message type.

### [BatchDeleteTasksRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchDeleteTasksRequest)

Request message for deleting a batch of tasks using [BatchDeleteTasks][google.cloud.tasks.v2.CloudTasks.BatchDeleteTasks].

### [CloudTasks](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasks)

Cloud Tasks allows developers to manage the execution of background work in their applications.

### [CloudTasks.CloudTasksBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasks.CloudTasksBase)

Base class for server-side implementations of CloudTasks

### [CloudTasks.CloudTasksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasks.CloudTasksClient)

Client for CloudTasks

### [CloudTasksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient)

CloudTasks client wrapper, for convenient use.

### [CloudTasksClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClientBuilder)

Builder class for [CloudTasksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient) to provide simple configuration of credentials, endpoint etc.

### [CloudTasksClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClientImpl)

CloudTasks client wrapper implementation, for convenient use.

### [CloudTasksSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksSettings)

Settings for [CloudTasksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient) instances.

### [CmekConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CmekConfig)

Describes the customer-managed encryption key (CMEK) configuration associated with a project and location.

### [CmekConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CmekConfigName)

Resource name for the `CmekConfig` resource.

### [CreateQueueRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CreateQueueRequest)

Request message for [CreateQueue][google.cloud.tasks.v2.CloudTasks.CreateQueue].

### [CreateTaskRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CreateTaskRequest)

Request message for [CreateTask][google.cloud.tasks.v2.CloudTasks.CreateTask].

### [CryptoKeyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CryptoKeyName)

Resource name for the `CryptoKey` resource.

### [DeleteQueueRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.DeleteQueueRequest)

Request message for [DeleteQueue][google.cloud.tasks.v2.CloudTasks.DeleteQueue].

### [DeleteTaskRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.DeleteTaskRequest)

Request message for deleting a task using [DeleteTask][google.cloud.tasks.v2.CloudTasks.DeleteTask].

### [GetCmekConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.GetCmekConfigRequest)

Request message for [GetCmekConfig][google.cloud.tasks.v2.CloudTasks.GetCmekConfig].

### [GetQueueRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.GetQueueRequest)

Request message for [GetQueue][google.cloud.tasks.v2.CloudTasks.GetQueue].

### [GetTaskRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.GetTaskRequest)

Request message for getting a task using [GetTask][google.cloud.tasks.v2.CloudTasks.GetTask].

### [HttpRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.HttpRequest)

HTTP request.

The task will be pushed to the worker as an HTTP request. If the worker or the redirected worker acknowledges the task by returning a successful HTTP response code ([`200` \- `299`]), the task will be removed from the queue. If any other HTTP response code is returned or no response is received, the task will be retried according to the following:

  * User-specified throttling: [retry configuration][google.cloud.tasks.v2.Queue.retry_config], [rate limits][google.cloud.tasks.v2.Queue.rate_limits], and the [queue's state][google.cloud.tasks.v2.Queue.state].

  * System throttling: To prevent the worker from overloading, Cloud Tasks may temporarily reduce the queue's effective rate. User-specified settings will not be changed.

System throttling happens because:

    * Cloud Tasks backs off on all errors. Normally the backoff specified in [rate limits][google.cloud.tasks.v2.Queue.rate_limits] will be used. But if the worker returns `429` (Too Many Requests), `503` (Service Unavailable), or the rate of errors is high, Cloud Tasks will use a higher backoff rate. The retry specified in the `Retry-After` HTTP response header is considered.

    * To prevent traffic spikes and to smooth sudden increases in traffic, dispatches ramp up slowly when the queue is newly created or idle and if large numbers of tasks suddenly become available to dispatch (due to spikes in create task rates, the queue being unpaused, or many tasks that are scheduled at the same time).




### [HttpTarget](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.HttpTarget)

HTTP target.

When specified at the [Queue][google.cloud.tasks.v2.Queue] level, all tasks with [HttpRequest][google.cloud.tasks.v2.HttpRequest] are overridden according to the target.

### [HttpTarget.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.HttpTarget.Types)

Container for nested types declared in the HttpTarget message type.

### [HttpTarget.Types.Header](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.HttpTarget.Types.Header)

Defines a header message. A header can have a key and a value.

### [HttpTarget.Types.HeaderOverride](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.HttpTarget.Types.HeaderOverride)

Wraps the Header object.

### [ListQueuesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.ListQueuesRequest)

Request message for [ListQueues][google.cloud.tasks.v2.CloudTasks.ListQueues].

### [ListQueuesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.ListQueuesResponse)

Response message for [ListQueues][google.cloud.tasks.v2.CloudTasks.ListQueues].

### [ListTasksRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.ListTasksRequest)

Request message for listing tasks using [ListTasks][google.cloud.tasks.v2.CloudTasks.ListTasks].

### [ListTasksResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.ListTasksResponse)

Response message for listing tasks using [ListTasks][google.cloud.tasks.v2.CloudTasks.ListTasks].

### [OAuthToken](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.OAuthToken)

Contains information needed for generating an [OAuth token](https://developers.google.com/identity/protocols/OAuth2). This type of authorization should generally only be used when calling Google APIs hosted on *.googleapis.com.

### [OidcToken](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.OidcToken)

Contains information needed for generating an [OpenID Connect token](https://developers.google.com/identity/protocols/OpenIDConnect). This type of authorization can be used for many scenarios, including calling Cloud Run, or endpoints where you intend to validate the token yourself.

### [PathOverride](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.PathOverride)

PathOverride.

Path message defines path override for HTTP targets.

### [PauseQueueRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.PauseQueueRequest)

Request message for [PauseQueue][google.cloud.tasks.v2.CloudTasks.PauseQueue].

### [PurgeQueueRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.PurgeQueueRequest)

Request message for [PurgeQueue][google.cloud.tasks.v2.CloudTasks.PurgeQueue].

### [QueryOverride](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.QueryOverride)

QueryOverride.

Query message defines query override for HTTP targets.

### [Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)

A queue is a container of related tasks. Queues are configured to manage how those tasks are dispatched. Configurable properties include rate limits, retry options, queue types, and others.

### [Queue.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue.Types)

Container for nested types declared in the Queue message type.

### [QueueName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.QueueName)

Resource name for the `Queue` resource.

### [RateLimits](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.RateLimits)

Rate limits.

This message determines the maximum rate that tasks can be dispatched by a queue, regardless of whether the dispatch is a first task attempt or a retry.

Note: The debugging command, [RunTask][google.cloud.tasks.v2.CloudTasks.RunTask], will run a task even if the queue has reached its [RateLimits][google.cloud.tasks.v2.RateLimits].

### [ResumeQueueRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.ResumeQueueRequest)

Request message for [ResumeQueue][google.cloud.tasks.v2.CloudTasks.ResumeQueue].

### [RetryConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.RetryConfig)

Retry config.

These settings determine when a failed task attempt is retried.

### [RunTaskRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.RunTaskRequest)

Request message for forcing a task to run now using [RunTask][google.cloud.tasks.v2.CloudTasks.RunTask].

### [StackdriverLoggingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.StackdriverLoggingConfig)

Configuration options for writing logs to [Stackdriver Logging](https://cloud.google.com/logging/docs/).

### [Task](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Task)

A unit of scheduled work.

### [Task.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Task.Types)

Container for nested types declared in the Task message type.

### [TaskName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.TaskName)

Resource name for the `Task` resource.

### [UpdateCmekConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.UpdateCmekConfigRequest)

Request message for [UpdateCmekConfig][google.cloud.tasks.v2.CloudTasks.UpdateCmekConfig].

### [UpdateQueueRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.UpdateQueueRequest)

Request message for [UpdateQueue][google.cloud.tasks.v2.CloudTasks.UpdateQueue].

### [UriOverride](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.UriOverride)

URI Override.

When specified, all the HTTP tasks inside the queue will be partially or fully overridden depending on the configured values.

### [UriOverride.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.UriOverride.Types)

Container for nested types declared in the UriOverride message type.

## Enums 

### [BatchCreateTasksMetadata.Types.State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchCreateTasksMetadata.Types.State)

The state of the batch create operation.

### [BatchDeleteTasksMetadata.Types.State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchDeleteTasksMetadata.Types.State)

The state of the batch delete operation. This enum is not frozen and new values may be added in the future.

### [CmekConfigName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CmekConfigName.ResourceNameType)

The possible contents of [CmekConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CmekConfigName).

### [CryptoKeyName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CryptoKeyName.ResourceNameType)

The possible contents of [CryptoKeyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CryptoKeyName).

### [HttpMethod](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.HttpMethod)

The HTTP method used to deliver the task.

### [HttpRequest.AuthorizationHeaderOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.HttpRequest.AuthorizationHeaderOneofCase)

Enum of possible cases for the "authorization_header" oneof.

### [HttpTarget.AuthorizationHeaderOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.HttpTarget.AuthorizationHeaderOneofCase)

Enum of possible cases for the "authorization_header" oneof.

### [Queue.Types.State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue.Types.State)

State of the queue.

### [QueueName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.QueueName.ResourceNameType)

The possible contents of [QueueName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.QueueName).

### [Task.MessageTypeOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Task.MessageTypeOneofCase)

Enum of possible cases for the "message_type" oneof.

### [Task.Types.View](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Task.Types.View)

The view specifies a subset of [Task][google.cloud.tasks.v2.Task] data.

When a task is returned in a response, not all information is retrieved by default because some data, such as payloads, might be desirable to return only when needed because of its large size or because of the sensitivity of data that it contains.

### [TaskName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.TaskName.ResourceNameType)

The possible contents of [TaskName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.TaskName).

### [UriOverride.Types.Scheme](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.UriOverride.Types.Scheme)

The Scheme for an HTTP request. By default, it is HTTPS.

### [UriOverride.Types.UriOverrideEnforceMode](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.UriOverride.Types.UriOverrideEnforceMode)

UriOverrideEnforceMode defines when the URI override is enforced.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
