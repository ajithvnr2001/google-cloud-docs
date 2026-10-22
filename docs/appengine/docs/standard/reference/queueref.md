---
url: https://docs.cloud.google.com/appengine/docs/standard/reference/queueref/
title: queue.yaml Reference \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:19:55.479226+00:00
---

# queue.yaml Reference  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/reference/queueref/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  queue.yaml Reference Stay organized with collections  Save and categorize content based on your preferences. 

### Region ID

The `REGION_ID` is an abbreviated code that Google assigns based on the region you select when you create your app. The code does not correspond to a country or province, even though some region IDs may appear similar to commonly used country and province codes. For apps created after February 2020, `REGION_ID.r` is included in App Engine URLs. For existing apps created before this date, the region ID is optional in the URL.

Learn more [about region IDs](https://docs.cloud.google.com/appengine/docs/standard/python/how-requests-are-routed#region-id). 

OK

Go Java Node.js PHP Python Ruby

The `queue.yaml` configuration file is used to create and configure almost all of the task queues (push or pull) your app uses. All App Engine apps come with an automatically preconfigured push queue named `default`. Although you do not create the `default` queue yourself, you can add other queues or change the configuration of the `default` queue using the `queue.yaml` file.

To configure [push queues](https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/push) you can use either `queue.yaml` or [Queue Management](https://docs.cloud.google.com/tasks/docs/queue-yaml) methods from Cloud Tasks, but [not both](https://docs.cloud.google.com/tasks/docs/queue-yaml#pitfalls) at the same time. Mixing the `queue.yaml` upload method with Queue Management methods can produce unexpected results and is not recommended.

To configure [pull queues](https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/pull) you must use the `queue.yaml` file. Cloud Tasks does not support pull queues.

**Caution:** When uploading a `queue.yaml` file via the gcloud CLI below version `332.0.0` uses a deprecated interface to the service. Starting on `2022-09-20`, attempts to use the upload method can fail with server errors. To resolve this, make sure the Cloud Tasks API is enabled in your project and your gcloud CLI is updated to at least version `332.0.0`.

## Example

The following a basic example that defines a named queue and overrides the default processing rate:
    
    
    queue:
    - name: my-push-queue
      rate: 1/s
    

The following is a more complex example of a `queue.yaml` configuration that demonstrates setting up the number of task tries and modifying the default processing rate.
    
    
    queue:
    - name: fooqueue
      rate: 1/s
      retry_parameters:
        task_retry_limit: 7
        task_age_limit: 2d
    - name: barqueue
      rate: 1/s
      retry_parameters:
        min_backoff_seconds: 10
        max_backoff_seconds: 200
        max_doublings: 0
    - name: bazqueue
      rate: 1/s
      retry_parameters:
        min_backoff_seconds: 10
        max_backoff_seconds: 200
        max_doublings: 3
    

## Syntax

The `queue.yaml` file is a YAML file whose root directive is `queue`. This directive contains zero or more named queues. Each queue definition can specify the following elements:

Element | Description  
---|---  
`bucket_size` (push queues) |  Optional. A task queue uses the [token bucket](https://wikipedia.org/wiki/Token_Bucket) algorithm to control the rate of task execution. Each named queue has a token bucket that holds tokens, up to the maximum specified by the **bucket_size** value. Each time your application executes a task, a token is removed from the bucket. You continue processing tasks in the queue until the queue's bucket runs out of tokens. App Engine refills the bucket with new tokens continuously based on the rate that you specified for the queue.  The bucket size limits how fast the queue is processed when many tasks are in the queue and the rate is high. The maximum value for bucket size is 500. This allows you to have a high rate so processing starts shortly after a task is enqueued, but still limit resource usage when many tasks are enqueued in a short period of time.  If you don't specify **bucket_size** for a queue, the default value is 5. We recommend that you set this to a larger value because the default size might be too small for many use cases. For example, you could determine your bucket size based on the processing _rate_.  For more information on this element, see the comparative description of [`max_burst_size`](https://docs.cloud.google.com/tasks/docs/reference/rpc/google.cloud.tasks.v2#ratelimits) in the Cloud Tasks API reference.   
`max_concurrent_requests` (push queues) |  Optional. Sets the maximum number of tasks that can be executed simultaneously from the specified queue. The value is an integer. By default, the limit is 1000 tasks per queue. The upper recommended limit is 5000 tasks per queue. Note that queues may slowly ramp up when they are first created or if they have been idle for a while.  Restricting the number of concurrent tasks gives you more control over the queue's rate of execution and can prevent too many tasks from running at once. It can also prevent datastore contention and make resources available for other queues or online processing.  For more information on this element, see the comparative description of [`max_concurrent_dispatches`](https://docs.cloud.google.com/tasks/docs/reference/rpc/google.cloud.tasks.v2#ratelimits) in the Cloud Tasks API reference.  
`mode` |  Optional. Identifies the queue mode. This setting defaults to `push` which identifies a queue as a push queue. To use pull queues, set the mode to `pull`.   
`name` |  Required. The name of the queue. This is the name you specify when you call `QueueFactory.getQueue()`.  A queue name can contain uppercase and lowercase letters, numbers, and hyphens. The maximum length for a queue name is 100 characters.  All apps have a push queue named default. This queue has a preset rate of 5 tasks per second. Note that this default queue doesn't display in the [Google Cloud console](https://console.cloud.google.com/) until the first time it is used or configured. You can configure the default queue, including changing the default rate, by defining a queue named `default` in your `queue.yaml` file.  
`rate` (push queues) |  Required. How often tasks are processed on this queue. The value is a number followed by a slash and a unit of time, where the unit is `s` for seconds, `m` for minutes, `h` for hours, or `d` for days. For example, the value `5/m` says tasks will be processed at a rate of 5 times per minute. The maximum value for `rate` is `500/s`.  If the number is `0` (such as `0/s`), the queue is considered "paused," and no tasks are processed.  For more information on this element, see the comparative description of [`max_dispatches_per_second`](https://docs.cloud.google.com/tasks/docs/reference/rpc/google.cloud.tasks.v2#ratelimits) in the Cloud Tasks API reference.  
`retry_parameters` |  Optional. Configures retry attempts for failed tasks in push queues. This addition allows you to specify the maximum number of times to retry failed tasks in a specific queue. You can also set a time limit for retry attempts and control the interval between attempts.  The retry parameters can contain the following subelements: 

`task_retry_limit`
     The number of retries. For example, if `0` is specified and the task _fails_ , the task is not _retried_ at all. If `1` is specified and the task _fails_ , the task is retried once. If this parameter is unspecified, the task is retried indefinitely. If `task_retry_limit` is specified with `task_age_limit`, the task is retried until both limits are reached. 
`task_age_limit` (push queues) 
     The time limit for retrying a failed task, measured from when the task was first run. The value is a number followed by a unit of time, where the unit is `s` for seconds, `m` for minutes, `h` for hours, or `d` for days. For example, the value `5d` specifies a limit of five days after the task's first execution attempt. If this parameter is unspecified, the task is retried indefinitely. If specified with `task_retry_limit`, App Engine retries the task until both limits are reached. 
`min_backoff_seconds` (push queues) 
     The minimum number of seconds to wait before retrying a task after it fails. The default value is `0.1`. 
`max_backoff_seconds` (push queues) 
     The maximum number of seconds to wait before retrying a task after it fails. The default value is `3600`. 
`max_doublings` (push queues) 
     The maximum number of times that the interval between failed task retries will be doubled before the increase becomes constant. The constant is: `2**max_doublings * min_backoff_seconds`. The default value is `16`.   
`target` (push queues) |  Optional. A string naming a service/version, a frontend version, or a backend, on which to execute all of the tasks enqueued onto this queue. The default value is the empty string.  The string is prepended to the domain name of your app when constructing the HTTP request for a task. For example, if your app ID is `my-app` and you set the target to `my-version-dot-my-service`, the URL hostname will be set to `my-version-dot-my-service-dot-my-app.REGION_ID.r.appspot.com`.  If target is unspecified, then tasks are invoked on the same version of the application where they were enqueued. So, if you enqueued a task from the default application version without specifying a target on the queue, the task is invoked in the default application version. Note that if the default application version changes between the time that the task is enqueued and the time that it executes, then the task will run in the new default version.  If you are using services along with a [dispatch file](https://docs.cloud.google.com/appengine/docs/standard/reference/dispatch-yaml), your task's HTTP request might be intercepted and re-routed to another service.   
  
The following elements can be specified for all queues within an app:

Element | Description  
---|---  
`total_storage_limit` |  Optional. A string that overrides the default quota storage limit that is available for taskqueue storage (100M). For example: 
    
    
              total_storage_limit: 1.2G
              queue:
                - name: fooqueue

This quota is part of the application's total storage quota (including the datastore and blobstore quota).  If no suffix is specified, the number that you specify is interpreted as bytes. The following suffixes are supported: 

  * `B` (bytes)
  * `K` (kilobytes)
  * `M` (megabytes)
  * `G` (gigabytes)
  * `T` (terabytes)

`total_storage_limit` exceeds the total disk storage that is available to an application, the limit is capped at the available storage.   
  
## Deploying the queue configuration file

The `queue.yaml` file should reside in the root directory or in the directory that defines the default service.

To deploy the queue configuration file, run the following command:
    
    
    gcloud app deploy queue.yaml
    

## Deleting queues

To delete a queue:

  1. Remove the queue definition from your `queue.yaml` file.

  2. Upload the change to your `queue.yaml` file.

gcloud app deploy queue.yaml

  3. Delete the queue in the Google Cloud console, select the queue and click **Delete queue** :

[Go to the Task queues page](https://console.cloud.google.com/appengine/taskqueues)




If you delete a queue from the Google Cloud console, you must wait 7 days before recreating with the same name.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
