---
url: https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/push/creating-handlers/
title: Creating Task Handlers \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:17:34.577415+00:00
---

# Creating Task Handlers  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/push/creating-handlers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Creating Task Handlers Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

**Note:** To upgrade App Engine Push Queues to Cloud Tasks without making code changes, [upgrade your App Engine services SDK to the latest version](https://docs.cloud.google.com/appengine/migration-center/standard/python/migrating-push-queues-upgrade-sdk) (Preview). 

This page describes how to create a _task handler_ , the code that handles a push task. You must provide a request handler to process the task. The mapping from the request URL to the appropriate handler is declared in your service's `app.yaml` , just like any other request handler. Because you control how to map task requests to a handler, you're free to organize your task handlers. If your application processes many different kinds of tasks, you can add all the handlers to a single service, or you can distribute them among multiple services.

## Writing a push task request handler

In the queue, the Task Queue service creates an HTTP header and sends it to an instance of the worker service specified by the task's target. Task Queue requests are sent from the IP address `0.1.0.2`.

Your handler does not need to be written in the same language that created and enqueued the task if the handler is in a [separate service](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine).

When you write your handler, follow these guidelines:

  * The code must return an HTTP status code within the range 200–299 to indicate success. Any other code indicates that the task failed.

**Note:** App Engine itself returns a `503` status code when instances are overloaded or otherwise unavailable. The Task Queue service responds to this by slowing delivery from queues to handlers, to avoid making the problem worse. If you wish to trigger a retry intentionally, use any status code _other_ than `2xx` or `503`.
  * Push tasks have a fixed [completion deadline](https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/push#the_task_deadline) that depends on the scaling type of the service that's running them. Automatic scaling services must finish before 10 minutes have elapsed. Manual and basic scaling services can run up to 24 hours. If your handler misses the deadline, the Task Queue service assumes the task failed and will retry it.

When a task's execution time nears the deadline, App Engine raises a `DeadlineExceededError` (from the module `google.appengine.runtime`) before the deadline is reached, so you can save your work or log whatever progress was made. 

  * The handler must be [idempotent](https://wikipedia.org/wiki/idempotent). App Engine's Task Queue API is designed to provide "at least once" delivery; that is, if a task is successfully added, App Engine will deliver it to a handler at least once. Note that in some rare circumstances, multiple task execution is possible, so your code must ensure that there are no harmful side-effects of repeated execution.




Task Queue uses the HTTP code in the handler's response to determine if the task succeeded. The response from the handler is seen only by the Task Queue service and only to determine if the task succeeded. The queue ignores all other fields in the response. Then the service discards the response. The originating app **never receives** any of the data. If a task fails, the Task Queue service retries the task by sending another request.

User-supplied data can be delivered to the handler in the request as a query string or as a payload in the request body. Inserting user data is described in [Creating Tasks](https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/push/creating-push-tasks#adding_user_data). If the request includes data, the handler must know how it was inserted into the request. The exact code you use to fetch the data from the request depends on the particular web framework you're using.

To test a task handler, sign in as an administrator and visit the handler's URL in your browser.

## Reading request headers

A push task HTTP request has special headers set by App Engine, which contain task-specific information your handler can use.

If these headers are present in an external user request to your app, they are stripped and replaced. The sole exception is for requests from logged-in administrators of the application, who are allowed to set headers for testing purposes. On the other hand, headers are not removed when your app is running in the development server.

Requests from Task Queue will always contain the following headers:

Header | Description  
---|---  
`X-Appengine-QueueName` | The name of the queue (possibly "default" for the default push queue).  
`X-Appengine-TaskName` | The name of the task, or a system-generated unique ID if no name was specified.  
`X-Appengine-TaskRetryCount` | The number of times this task has been retried. For the first attempt, this value is `0`. This number includes attempts where the task failed due to a lack of available instances and never reached the execution phase.  
`X-Appengine-TaskExecutionCount` | The number of times this task has previously failed during the execution phase. This number does not include failures due to a lack of available instances.  
`X-Appengine-TaskETA` | The target execution time of the task, specified in seconds since January 1st 1970.  
  
If your request handler finds any of the headers listed above, it can trust that the request is a Task Queue request.

In addition, requests from Task Queue can contain the following headers:

Header | Description  
---|---  
`X-Appengine-TaskPreviousResponse` | The HTTP response code from the previous retry.  
`X-Appengine-TaskRetryReason` | The reason for retrying the task.  
`X-Appengine-FailFast` | Indicates that a task running [fails immediately if an existing instance is not available](https://docs.cloud.google.com/tasks/docs/creating-appengine-handlers).  
  
## Securing task handler URLs

If a task performs sensitive operations (such as modifying data), you might want to secure the handler URL to prevent a malicious external user from calling it directly. You can prevent users from accessing task URLs by restricting access to [App Engine administrators](https://docs.cloud.google.com/appengine/docs/standard/access-control). Task requests themselves are issued by App Engine and can always target a restricted URL.

You can restrict a URL by adding the [`login: admin`](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#handlers-login) element to the handler configuration in your `app.yaml` file.

For example:
    
    
    handlers:
    - url: /your-task
      script: worker.app
      login: admin
    

**Note:** While tasks can use URL paths restricted with `login: admin`, they _cannot_ use URL paths restricted with `login: required` because tasks are not run as any user. The `admin` restriction is satisfied by the inclusion of the `X-Appengine-QueueName` header described in Reading request headers.

## What's next

  * Learn how to [delete tasks](https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/push/deleting-tasks-and-queues).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
