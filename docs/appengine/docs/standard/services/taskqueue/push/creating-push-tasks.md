---
url: https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/push/creating-push-tasks/
title: Create Push Tasks \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:47:56.747696+00:00
---

# Create Push Tasks  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/push/creating-push-tasks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Create Push Tasks Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

**Note:** To upgrade App Engine Push Queues to Cloud Tasks without making code changes, [upgrade your App Engine services SDK to the latest version](https://docs.cloud.google.com/appengine/migration-center/standard/python/migrating-push-queues-upgrade-sdk) (Preview). 

This page describes how to create tasks and place them in push queues. When you want to process a task, you must create a new task object and place it on a queue. You can explicitly specify the service and handler that process the task, and optionally pass task-specific data along to the handler. You can also fine-tune the configuration for the task, like scheduling a time in the future when it should be executed or limiting the number of times you want the task to be retried if it fails.

## Creating a new task

To create and enqueue a task, call the [`taskqueue.add()`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/Queue#add) function.

## Specifying the worker service

When a task is popped off its queue, the Task Queue service sends it on to a worker service. Every task has a _target_ and a _url_ , which determine what service and handler will ultimately perform the task.

### `target`

The target specifies the service that will receive the HTTP request to perform the task. It is a string that specifies a service/version/instance in any one of the [canonical forms](https://docs.cloud.google.com/appengine/docs/standard/how-requests-are-routed#routing_via_url). The most often-used forms are:
    
    
        service
        version.service
        instance.version.service
    

The target string is prepended to the domain name of your app. There are three ways to set the target for a task:

  * Declare the target when you construct the task. You can set the target explicitly using the `target` parameter in the [`taskqueue.add()`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/add) function. See the example above. 

  * Include a `target` directive when you define a queue in the `queue.yaml`, as in the [definition](https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/push/creating-push-queues) of `queue-blue`. All tasks added to a queue with a `target` will use that target, even if a different target was assigned to the task at construction time.

  * If no target is specified according to either of the previous two methods, then the task's target is the version of the service that enqueues it. Note that if you enqueue a task from the default service and version in this manner, and the default version changes before the task executes, it will run in the new default version.




### `url`

The `url` selects one of the handlers in the target service, which will perform the task.

The `url` should match one of the handler URL patterns in the target service. The `url` can include query parameters if the method specified in the task is `GET` or `PULL`. If no `url` is specified the default URL `/_ah/queue/[QUEUE_NAME]` is used, where `[QUEUE_NAME]` is the name of the task's queue.

## Passing data to the handler

You can pass data to the handler as query parameters in the task's URL, but only if the method specified in the task is `GET` or `PULL`.

You can also use any of the following fields to add data to a task:

  * `payload`, which delivers task data in the body of the HTTP request.
  * `params`

**Note:** Don't specify params if you are using the HTTP `POST` method along with a payload, or if you are using the HTTP `GET` method and you've included a URL with query parameters.

These three calls are equivalent:
    
    
    taskqueue.add(method=GET, url='/update-counter?key=blue', target='worker')
    taskqueue.add(url='/update-counter', params={'key': 'blue'}, target='worker')
    taskqueue.add(url='/update-counter', payload="{'key': 'blue'}", target='worker')
    

## Naming a task

When you create a new task, App Engine assigns the task a unique name by default. However, you can assign your own name to a task by using the `name` parameter. An advantage of assigning your own task names is that named tasks are de-duplicated, which means you can use task names to guarantee that a task is only added once. De-duplication continues for 9 days after the task is completed or deleted.

Note that de-duplication logic introduces significant performance overhead, resulting in increased latencies and potentially increased error rates associated with named tasks. These costs can be magnified significantly if task names are sequential, such as with timestamps. So, if you assign your own names, we recommend using a well-distributed prefix for task names, such as a hash of the contents.

If you assign your own names to tasks, note that the maximum name length is 500 characters, and the name can contain uppercase and lowercase letters, numbers underscores, and hyphens.

## Adding tasks asynchronously

By default, the calls that add tasks to queues are synchronous. For most scenarios, synchronous calls work fine. Adding a task to a queue is usually a fast operation. There are a small percentage of add task operations that can take significantly longer, but the median time to add a task is less than 5 ms.

Add task operations to different queues cannot be batched, so the Task Queue API also provides asynchronous calls that give you the ability to add these tasks in parallel, further minimizing this latency. This is useful if you are building an extremely latency sensitive application that needs to perform several add task operations to different queues at the same time.

If you want to make asynchronous calls to a task queue, use the asynchronous methods provided by the [Queue](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/Queue) class and an [RPC](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/Queue#add_async) object. Call `get_result()` on the returned `RPC` object to force the request to complete. When asynchronously adding tasks in a transaction, you should call `get_result()` on the `RPC` object before committing the transaction to ensure that the request has finished

## Enqueuing tasks in Cloud Datastore transactions

You can enqueue a task as part of a Datastore transaction, such that the task is only enqueued—and guaranteed to be enqueued—if the transaction is committed successfully. Tasks added in a [transaction](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/transactions) are considered to be a part of it and have the same level of [transaction](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/transactions) . 

An application cannot insert more than five transactional tasks into [task queues](https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue) during a single transaction. Transactional tasks must not have user-specified names.

The following code sample demonstrates how to insert transactional tasks into a push queue as part of a Datastore transaction:
    
    
    from google.appengine.api import taskqueue
    from google.appengine.ext import ndb
    
    @ndb.transactional
    def do_something_in_transaction():
      taskqueue.add(url='/path/to/my/worker', transactional=True)
      #...
    
    do_something_in_transaction()
    

## Using the deferred task library instead of a worker service

Setting up a handler for each distinct task (as described in the previous sections) can be cumbersome, as can serializing and deserializing complex arguments for the task—particularly if you have many diverse but small tasks that you want to run on the queue. The Python SDK includes a library (`google.appengine.ext.deferred`) exposing a simple function that allows you to bypass all the work of setting up dedicated task handlers and serializing and deserializing your parameters.

To use this library, you need to add the `deferred` builtin to `app.yaml`. For more information, see the [Built-in Handlers section](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#builtins) of the `app.yaml` reference.

To use the `deferred` library, simply pass the function and its arguments to `deferred.defer()`:
    
    
    import logging
    
    from google.appengine.ext import deferred
    
    def do_something_expensive(a, b, c=None):
        logging.info("Doing something expensive!")
        # Do your work here
    
    # Somewhere else
    deferred.defer(do_something_expensive, "Hello, world!", 42, True)
    

The `deferred` library packages your function call and its arguments, then adds it to the task queue. When the task is executed, the `deferred` library executes `do_something_expensive("Hello, world!", 42, True)`.

## Working with tasks in a multi-tenant application

By default, push queues use the current namespace as set in the namespace manager at the time the task is created. If your application uses multitenancy, see the [Namespaces API](https://docs.cloud.google.com/appengine/docs/standard/services/multitenancy/multitenancy#Using_namespaces_with_the_Task_Queue).

## What's next

  * Learn how to [create task handlers](https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/push/creating-handlers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
