---
url: https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues.tasks
title: REST Resource: projects.locations.queues.tasks \u00a0|\u00a0 Cloud Tasks \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:36:37.269483+00:00
---

# REST Resource: projects.locations.queues.tasks  |  Cloud Tasks  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues.tasks

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Tasks ](https://docs.cloud.google.com/tasks/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/tasks/docs/apis)



Send feedback 

#  REST Resource: projects.locations.queues.tasks Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Task
    * JSON representation
  * AppEngineHttpRequest
    * JSON representation
  * HttpRequest
    * JSON representation
  * PullMessage
    * JSON representation
  * Attempt
    * JSON representation
  * View
  * Methods



## Resource: Task

A unit of scheduled work.

JSON representation  
---  
      
    
    {
      "name": string,
      "scheduleTime": string,
      "createTime": string,
      "dispatchDeadline": string,
      "dispatchCount": integer,
      "responseCount": integer,
      "firstAttempt": {
        object ([Attempt](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues.tasks#Attempt))
      },
      "lastAttempt": {
        object ([Attempt](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues.tasks#Attempt))
      },
      "view": enum ([View](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues.tasks#View)),
      "retryConfig": {
        object ([RetryConfig](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/RetryConfig))
      },
    
      // Union field payload_type can be only one of the following:
      "appEngineHttpRequest": {
        object ([AppEngineHttpRequest](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues.tasks#AppEngineHttpRequest))
      },
      "httpRequest": {
        object ([HttpRequest](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues.tasks#HttpRequest))
      },
      "pullMessage": {
        object ([PullMessage](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues.tasks#PullMessage))
      }
      // End of list of possible types for union field payload_type.
    }  
  
Fields  
---  
`name` |  `string` Optionally caller-specified in `[tasks.create](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues.tasks/create#google.cloud.tasks.v2beta3.CloudTasks.CreateTask)`.The task name.The task name must have the following format: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID`

  * `PROJECT_ID` can contain letters ([A-Za-z]), numbers ([0-9]), hyphens (-), colons (:), or periods (.). For more information, see [Identifying projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects)
  * `LOCATION_ID` is the canonical ID for the task's location. The list of available locations can be obtained by calling `locations.list`. For more information, see <https://cloud.google.com/about/locations/>.
  * `QUEUE_ID` can contain letters ([A-Za-z]), numbers ([0-9]), or hyphens (-). The maximum length is 100 characters.
  * `TASK_ID` can contain only letters ([A-Za-z]), numbers ([0-9]), hyphens (-), or underscores (_). The maximum length is 500 characters.

  
`scheduleTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time when the task is scheduled to be attempted.For App Engine queues, this is when the task will be attempted or retried.`scheduleTime` will be truncated to the nearest microsecond.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time that the task was created.`createTime` will be truncated to the nearest second.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`dispatchDeadline` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` The deadline for requests sent to the worker. If the worker does not respond by this deadline then the request is cancelled and the attempt is marked as a `DEADLINE_EXCEEDED` failure. Cloud Tasks will retry the task according to the `[RetryConfig](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/RetryConfig)`.Note that when the request is cancelled, Cloud Tasks will stop listening for the response, but whether the worker stops processing depends on the worker. For example, if the worker is stuck, it may not react to cancelled requests.The default and maximum values depend on the type of request:

  * For `[HTTP tasks](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues.tasks#HttpRequest)`, the default is 10 minutes. The deadline must be in the interval [15 seconds, 30 minutes].
  * For `[App Engine tasks](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues.tasks#AppEngineHttpRequest)`, 0 indicates that the request has the default deadline. The default deadline depends on the [scaling type](https://cloud.google.com/appengine/docs/standard/go/how-instances-are-managed#instance_scaling) of the service: 10 minutes for standard apps with automatic scaling, 24 hours for standard apps with manual and basic scaling, and 60 minutes for flex apps. If the request deadline is set, it must be in the interval [15 seconds, 24 hours 15 seconds]. Regardless of the task's `dispatchDeadline`, the app handler will not run for longer than than the service's timeout. We recommend setting the `dispatchDeadline` to at most a few seconds more than the app handler's timeout. For more information see [Timeouts](https://cloud.google.com/tasks/docs/creating-appengine-handlers#timeouts).

The value must be given as a string that indicates the length of time (in seconds) followed by `s` (for "seconds"). For more information on the format, see the documentation for [Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration). `dispatchDeadline` will be truncated to the nearest millisecond. The deadline is an approximate deadline.  
`dispatchCount` |  `integer` Output only. The number of attempts dispatched.This count includes attempts which have been dispatched but haven't received a response.  
`responseCount` |  `integer` Output only. The number of attempts which have received a response.  
`firstAttempt` |  `object (`[Attempt](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues.tasks#Attempt)`)` Output only. The status of the task's first attempt.Only `[dispatchTime](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues.tasks#Attempt.FIELDS.dispatch_time)` will be set. The other `[Attempt](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues.tasks#Attempt)` information is not retained by Cloud Tasks.  
`lastAttempt` |  `object (`[Attempt](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues.tasks#Attempt)`)` Output only. The status of the task's last attempt.  
`view` |  `enum (`[View](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues.tasks#View)`)` Output only. The view specifies which subset of the `[Task](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues.tasks#Task)` has been returned.  
`retryConfig` |  `object (`[RetryConfig](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/RetryConfig)`)` Optional. Specifies the task-level retry config.If present, this overrides the queue-level retry config for this task.  
Union field `payload_type`. Required. The message to send to the worker. `payload_type` can be only one of the following:  
`appEngineHttpRequest` |  `object (`[AppEngineHttpRequest](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues.tasks#AppEngineHttpRequest)`)` HTTP request that is sent to the App Engine app handler.An App Engine task is a task that has `[AppEngineHttpRequest](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues.tasks#AppEngineHttpRequest)` set.  
`httpRequest` |  `object (`[HttpRequest](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues.tasks#HttpRequest)`)` HTTP request that is sent to the task's target.An HTTP task is a task that has `[HttpRequest](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues.tasks#HttpRequest)` set.  
`pullMessage` |  `object (`[PullMessage](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues.tasks#PullMessage)`)` Pull Message contained in a task in a `[PULL](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues#Queue.FIELDS.type)` queue type. This payload type cannot be explicitly set through Cloud Tasks API. Its purpose, currently is to provide backward compatibility with App Engine Task Queue [pull](https://cloud.google.com/appengine/docs/standard/java/taskqueue/pull/) queues to provide a way to inspect contents of pull tasks through the `[CloudTasks.GetTask](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues.tasks/get#google.cloud.tasks.v2beta3.CloudTasks.GetTask)`.  
  
## AppEngineHttpRequest

App Engine HTTP request.

The message defines the HTTP request that is sent to an App Engine app when the task is dispatched.

Using `[AppEngineHttpRequest](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues.tasks#AppEngineHttpRequest)` requires [`appengine.applications.get`](https://cloud.google.com/appengine/docs/admin-api/access-control) Google IAM permission for the project and the following scope:

`https://www.googleapis.com/auth/cloud-platform`

The task will be delivered to the App Engine app which belongs to the same project as the queue. For more information, see [How Requests are Routed](https://cloud.google.com/appengine/docs/standard/python/how-requests-are-routed) and how routing is affected by [dispatch files](https://cloud.google.com/appengine/docs/python/config/dispatchref). Traffic is encrypted during transport and never leaves Google datacenters. Because this traffic is carried over a communication mechanism internal to Google, you cannot explicitly set the protocol (for example, HTTP or HTTPS). The request to the handler, however, will appear to have used the HTTP protocol.

The `[AppEngineRouting](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/AppEngineRouting)` used to construct the URL that the task is delivered to can be set at the queue-level or task-level:

  * If set, `[appEngineRoutingOverride](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues#AppEngineHttpQueue.FIELDS.app_engine_routing_override)` is used for all tasks in the queue, no matter what the setting is for the `[task-level appEngineRouting](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues.tasks#AppEngineHttpRequest.FIELDS.app_engine_routing)`.



The `url` that the task will be sent to is:

  * `url =` `[host](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/AppEngineRouting#FIELDS.host)` `+` `[relativeUri](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues.tasks#AppEngineHttpRequest.FIELDS.relative_uri)`



Tasks can be dispatched to secure app handlers, unsecure app handlers, and URIs restricted with [`login: admin`](https://cloud.google.com/appengine/docs/standard/python/config/appref). Because tasks are not run as any user, they cannot be dispatched to URIs restricted with [`login: required`](https://cloud.google.com/appengine/docs/standard/python/config/appref) Task dispatches also do not follow redirects.

The task attempt has succeeded if the app's request handler returns an HTTP response code in the range [`200` \- `299`]. The task attempt has failed if the app's handler returns a non-2xx response code or Cloud Tasks does not receive response before the `[deadline](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues.tasks#Task.FIELDS.dispatch_deadline)`. Failed tasks will be retried according to the `[retry configuration](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues#Queue.FIELDS.retry_config)`. `503` (Service Unavailable) is considered an App Engine system error instead of an application error and will cause Cloud Tasks' traffic congestion control to temporarily throttle the queue's dispatches. Unlike other types of task targets, a `429` (Too Many Requests) response from an app handler does not cause traffic congestion control to throttle the queue.

JSON representation  
---  
      
    
    {
      "httpMethod": enum ([HttpMethod](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/HttpMethod)),
      "appEngineRouting": {
        object ([AppEngineRouting](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/AppEngineRouting))
      },
      "relativeUri": string,
      "headers": {
        string: string,
        ...
      },
      "body": string
    }  
  
Fields  
---  
`httpMethod` |  `enum (`[HttpMethod](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/HttpMethod)`)` The HTTP method to use for the request. The default is POST.The app's request handler for the task's target URL must be able to handle HTTP requests with this httpMethod, otherwise the task attempt fails with error code 405 (Method Not Allowed). See [Writing a push task request handler](https://cloud.google.com/appengine/docs/java/taskqueue/push/creating-handlers#writing_a_push_task_request_handler) and the App Engine documentation for your runtime on [How Requests are Handled](https://cloud.google.com/appengine/docs/standard/python3/how-requests-are-handled).  
`appEngineRouting` |  `object (`[AppEngineRouting](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/AppEngineRouting)`)` Task-level setting for App Engine routing.If set, `[appEngineRoutingOverride](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues#AppEngineHttpQueue.FIELDS.app_engine_routing_override)` is used for all tasks in the queue, no matter what the setting is for the `[task-level appEngineRouting](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues.tasks#AppEngineHttpRequest.FIELDS.app_engine_routing)`.  
`relativeUri` |  `string` The relative URI.The relative URI must begin with "/" and must be a valid HTTP relative URI. It can contain a path and query string arguments. If the relative URI is empty, then the root path "/" will be used. No spaces are allowed, and the maximum length allowed is 2083 characters.  
`headers` |  `map (key: string, value: string)` HTTP request headers.This map contains the header field names and values. Headers can be set when the `[task is created](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues.tasks/create#google.cloud.tasks.v2beta3.CloudTasks.CreateTask)`. Repeated headers are not supported but a header value can contain commas.Cloud Tasks sets some headers to default values:

  * `User-Agent`: By default, this header is `"AppEngine-Google; (+http://code.google.com/appengine)"`. This header can be modified, but Cloud Tasks will append `"AppEngine-Google; (+http://code.google.com/appengine)"` to the modified `User-Agent`.

If the task has a `[body](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues.tasks#AppEngineHttpRequest.FIELDS.body)`, Cloud Tasks sets the following headers:

  * `Content-Type`: By default, the `Content-Type` header is set to `"application/octet-stream"`. The default can be overridden by explicitly setting `Content-Type` to a particular media type when the `[task is created](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues.tasks/create#google.cloud.tasks.v2beta3.CloudTasks.CreateTask)`. For example, `Content-Type` can be set to `"application/json"`.
  * `Content-Length`: This is computed by Cloud Tasks. This value is output only. It cannot be changed.

The headers below cannot be set or overridden:

  * `Host`
  * `X-Google-*`
  * `X-AppEngine-*`

In addition, Cloud Tasks sets some headers when the task is dispatched, such as headers containing information about the task; see [request headers](https://cloud.google.com/tasks/docs/creating-appengine-handlers#reading_request_headers). These headers are set only when the task is dispatched, so they are not visible when the task is returned in a Cloud Tasks response.Although there is no specific limit for the maximum number of headers or the size, there is a limit on the maximum size of the `[Task](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues.tasks#Task)`. For more information, see the `[tasks.create](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues.tasks/create#google.cloud.tasks.v2beta3.CloudTasks.CreateTask)` documentation.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`body` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` HTTP request body.A request body is allowed only if the HTTP method is POST or PUT. It is an error to set a body on a task with an incompatible `[HttpMethod](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/HttpMethod)`.A base64-encoded string.  
  
## HttpRequest

HTTP request.

The task will be pushed to the worker as an HTTP request. If the worker or the redirected worker acknowledges the task by returning a successful HTTP response code ([`200` \- `299`]), the task will be removed from the queue. If any other HTTP response code is returned or no response is received, the task will be retried according to the following:

  * User-specified throttling: `[retry configuration](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues#Queue.FIELDS.retry_config)`, `[rate limits](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues#Queue.FIELDS.rate_limits)`, and the `[queue's state](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues#Queue.FIELDS.state)`.

  * System throttling: To prevent the worker from overloading, Cloud Tasks may temporarily reduce the queue's effective rate. User-specified settings will not be changed.




System throttling happens because:

  * Cloud Tasks backs off on all errors. Normally the backoff specified in `[rate limits](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues#Queue.FIELDS.rate_limits)` will be used. But if the worker returns `429` (Too Many Requests), `503` (Service Unavailable), or the rate of errors is high, Cloud Tasks will use a higher backoff rate. The retry specified in the `Retry-After` HTTP response header is considered.

  * To prevent traffic spikes and to smooth sudden increases in traffic, dispatches ramp up slowly when the queue is newly created or idle and if large numbers of tasks suddenly become available to dispatch (due to spikes in create task rates, the queue being unpaused, or many tasks that are scheduled at the same time).


JSON representation  
---  
      
    
    {
      "url": string,
      "httpMethod": enum ([HttpMethod](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/HttpMethod)),
      "headers": {
        string: string,
        ...
      },
      "body": string,
    
      // Union field authorization_header can be only one of the following:
      "oauthToken": {
        object ([OAuthToken](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/OAuthToken))
      },
      "oidcToken": {
        object ([OidcToken](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/OidcToken))
      }
      // End of list of possible types for union field authorization_header.
    }  
  
Fields  
---  
`url` |  `string` Required. The full url path that the request will be sent to.This string must begin with either "http://" or "https://". Some examples are: `http://acme.com` and `https://acme.com/sales:8080`. Cloud Tasks will encode some characters for safety and compatibility. The maximum allowed URL length is 2083 characters after encoding.The `Location` header response from a redirect response [`300` \- `399`] may be followed. The redirect is not counted as a separate attempt.  
`httpMethod` |  `enum (`[HttpMethod](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/HttpMethod)`)` The HTTP method to use for the request. The default is POST.  
`headers` |  `map (key: string, value: string)` HTTP request headers.This map contains the header field names and values. Headers can be set when the `[task is created](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues.tasks/create#google.cloud.tasks.v2beta3.CloudTasks.CreateTask)`.These headers represent a subset of the headers that will accompany the task's HTTP request. Some HTTP request headers will be ignored or replaced.A partial list of headers that will be ignored or replaced is:

  * Any header that is prefixed with "X-CloudTasks-" will be treated as service header. Service headers define properties of the task and are predefined in Cloud Tasks.
  * Host: This will be computed by Cloud Tasks and derived from `[HttpRequest.url](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues.tasks#HttpRequest.FIELDS.url)`.
  * Content-Length: This will be computed by Cloud Tasks.
  * User-Agent: This will be set to `"Google-Cloud-Tasks"`.
  * `X-Google-*`: Google use only.
  * `X-AppEngine-*`: Google use only.

`Content-Type` won't be set by Cloud Tasks. You can explicitly set `Content-Type` to a media type when the `[task is created](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues.tasks/create#google.cloud.tasks.v2beta3.CloudTasks.CreateTask)`. For example, `Content-Type` can be set to `"application/octet-stream"` or `"application/json"`.Headers which can have multiple values (according to RFC2616) can be specified using comma-separated values.The size of the headers must be less than 80KB.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`body` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` HTTP request body.A request body is allowed only if the `[HTTP method](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues.tasks#HttpRequest.FIELDS.http_method)` is POST, PUT, or PATCH. It is an error to set body on a task with an incompatible `[HttpMethod](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/HttpMethod)`.A base64-encoded string.  
Union field `authorization_header`. The mode for generating an `Authorization` header for HTTP requests.If specified at the `[Queue](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues#Queue)` level, all `Authorization` headers in the `[HttpRequest.headers](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues.tasks#HttpRequest.FIELDS.headers)` field are overridden. `authorization_header` can be only one of the following:  
`oauthToken` |  `object (`[OAuthToken](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/OAuthToken)`)` If specified, an [OAuth token](https://developers.google.com/identity/protocols/OAuth2) will be generated and attached as an `Authorization` header in the HTTP request.This type of authorization should generally only be used when calling Google APIs hosted on *.googleapis.com.  
`oidcToken` |  `object (`[OidcToken](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/OidcToken)`)` If specified, an [OIDC](https://developers.google.com/identity/protocols/OpenIDConnect) token will be generated and attached as an `Authorization` header in the HTTP request.This type of authorization can be used for many scenarios, including calling Cloud Run, or endpoints where you intend to validate the token yourself.  
  
## PullMessage

Pull Message.

This proto can only be used for tasks in a queue which has `[PULL](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues#Queue.FIELDS.type)` type. It currently exists for backwards compatibility with the App Engine Task Queue SDK. This message type maybe returned with methods `[list](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues.tasks/list#google.cloud.tasks.v2beta3.CloudTasks.ListTasks)` and `[get](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues.tasks/list#google.cloud.tasks.v2beta3.CloudTasks.ListTasks)`, when the response view is `[FULL](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues.tasks#View.ENUM_VALUES.FULL)`.

JSON representation  
---  
      
    
    {
      "payload": string,
      "tag": string
    }  
  
Fields  
---  
`payload` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` A data payload consumed by the worker to execute the task.A base64-encoded string.  
`tag` |  `string` The tasks's tag.The tag is less than 500 characters.SDK compatibility: Although the SDK allows tags to be either string or [bytes](https://cloud.google.com/appengine/docs/standard/java/javadoc/com/google/appengine/api/taskqueue/TaskOptions.html#tag-byte:A-), only UTF-8 encoded tags can be used in Cloud Tasks. If a tag isn't UTF-8 encoded, the tag will be empty when the task is returned by Cloud Tasks.  
  
## Attempt

The status of a task attempt.

JSON representation  
---  
      
    
    {
      "scheduleTime": string,
      "dispatchTime": string,
      "responseTime": string,
      "responseStatus": {
        object ([Status](https://docs.cloud.google.com/tasks/docs/reference/rest/Shared.Types/Operation#Status))
      }
    }  
  
Fields  
---  
`scheduleTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time that this attempt was scheduled.`scheduleTime` will be truncated to the nearest microsecond.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`dispatchTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time that this attempt was dispatched.`dispatchTime` will be truncated to the nearest microsecond.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`responseTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time that this attempt response was received.`responseTime` will be truncated to the nearest microsecond.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`responseStatus` |  `object (`[Status](https://docs.cloud.google.com/tasks/docs/reference/rest/Shared.Types/Operation#Status)`)` Output only. The response from the worker for this attempt.If `responseTime` is unset, then the task has not been attempted or is currently running and the `responseStatus` field is meaningless.  
  
## View

The view specifies a subset of `[Task](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues.tasks#Task)` data.

When a task is returned in a response, not all information is retrieved by default because some data, such as payloads, might be desirable to return only when needed because of its large size or because of the sensitivity of data that it contains.

Enums  
---  
`VIEW_UNSPECIFIED` | Unspecified. Defaults to BASIC.  
`BASIC` | The basic view omits fields which can be large or can contain sensitive data.This view does not include the `[body in AppEngineHttpRequest](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues.tasks#AppEngineHttpRequest.FIELDS.body)`. Bodies are desirable to return only when needed, because they can be large and because of the sensitivity of the data that you choose to store in it.  
`FULL` | All information is returned.Authorization for `[FULL](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues.tasks#View.ENUM_VALUES.FULL)` requires `cloudtasks.tasks.fullView` [Google IAM](https://cloud.google.com/iam/) permission on the `[Queue](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues#Queue)` resource.  
  
## Methods  
  
---  
  
### `[batchCreate](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues.tasks/batchCreate)`

|  Creates a batch of tasks and adds them to a queue.  
  
### `[batchDelete](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues.tasks/batchDelete)`

|  Deletes a batch of tasks.  
  
### `[buffer](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues.tasks/buffer)`

|  Creates and buffers a new task without the need to explicitly define a Task message.  
  
### `[create](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues.tasks/create)`

|  Creates a task and adds it to a queue.  
  
### `[delete](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues.tasks/delete)`

|  Deletes a task.  
  
### `[get](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues.tasks/get)`

|  Gets a task.  
  
### `[list](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues.tasks/list)`

|  Lists the tasks in a queue.  
  
### `[run](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues.tasks/run)`

|  Forces a task to run now.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-30 UTC."],[],[]] 
