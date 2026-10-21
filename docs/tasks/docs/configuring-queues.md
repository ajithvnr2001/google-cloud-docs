---
url: https://docs.cloud.google.com/tasks/docs/configuring-queues/
title: Configure queue routing, limits, and retries \u00a0|\u00a0 Cloud Tasks \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:46.297394+00:00
---

# Configure queue routing, limits, and retries  |  Cloud Tasks  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tasks/docs/configuring-queues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Tasks ](https://docs.cloud.google.com/tasks/docs)
  * [ Guides ](https://docs.cloud.google.com/tasks/docs/dual-overview)



Send feedback 

#  Configure queue routing, limits, and retries Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Tasks lets you manage task execution by defining queue-level routing, dispatch rate limits, and retry behavior. You can configure these settings when creating a queue or updating an existing queue. The configuration flags used by either [`gcloud tasks queues create`](https://docs.cloud.google.com/sdk/gcloud/reference/tasks/queues/create) or [`gcloud tasks queues update`](https://docs.cloud.google.com/sdk/gcloud/reference/tasks/queues/update) are identical.

Configuring authentication at the queue level overrides task-level authentication. For more information, see [Use HTTP target tasks with authentication tokens](https://docs.cloud.google.com/tasks/docs/creating-http-target-tasks#token).

## Configure queue-level routing

Configuring routing at the queue level overrides routing set at the task level. This is useful if you want to use Cloud Tasks as a buffer in front of your target service, or if you need to change the routing for all tasks in a queue.

Queue-level routing applies to:

  * Tasks that are in the queue
  * Tasks that are added to the queue after queue-level routing has been set



### Limitations

Queue-level routing is not compatible with Cloud Key Management Service (Cloud KMS) customer-managed encryption keys (CMEK). If CMEK is enabled, you can't do the following:

  * Create tasks on a queue that has queue-level routing
  * Apply queue-level routing



### Configure queue-level routing for HTTP tasks

You can configure a queue to override task-level routing either when creating the queue or when updating the queue. To configure queue-level routing, set the queue's [`uriOverride`](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues#urioverride) parameter to your preferred route.

If you are applying queue-level routing as an update to an existing queue, pause the queue before applying the changes and wait one minute after applying the changes to resume the queue.

  1. [Pause the queue](https://docs.cloud.google.com/tasks/docs/deleting-appengine-queues-and-tasks#pause-queues) by running the following command:
         
         gcloud tasks queues pause QUEUE_ID
           

Replace `QUEUE_ID` with the ID of your queue.

  2. Update or remove queue-level routing.

     * To update queue-level routing, set the [`uriOverride`](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues#urioverride) parameter to your updated route.

     * To remove queue-level routing using either the REST or RPC API:

       * **REST API:** Send a [`patch`](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues/patch) request for the queue with an empty payload and the `updateMask` parameter set to `httpTarget`.

       * **RPC API:** Send an [`updateQueueRequest`](https://docs.cloud.google.com/tasks/docs/reference/rpc/google.cloud.tasks.v2#updatequeuerequest) for the queue with an empty payload and the `update_mask` parameter set to `http_target`.

The following example uses the REST API to update the host that tasks are routed to:
    
    curl -X PATCH -d @- -i \
      -H "Authorization: Bearer ACCESS_TOKEN" \
      -H "Content-Type: application/json" \
      "https://cloudtasks.googleapis.com/v2/projects/PROJECT_ID/locations/LOCATION/queues/QUEUE_ID?updateMask=httpTarget.uriOverride" << EOF
    {
      "httpTarget": {"uriOverride":{"host":"NEW_HOST"}}
    }
    EOF
    

Replace the following:

     * `ACCESS_TOKEN`: your access token. You can get this by running the following in your terminal:
           
           gcloud auth application-default login
           gcloud auth application-default print-access-token

     * `PROJECT_ID`: the ID of your Google Cloud project. You can get this by running the following in your terminal: 
           
           gcloud config get-value project

     * `LOCATION`: the location of your queue.

     * `NEW_HOST`: the new host you want your queue to route to.

  3. Wait one minute.

It can take up to one minute for the new configuration to take effect. Waiting to resume the queue helps to prevent tasks from dispatching with the old configuration.

  4. Resume the queue by running the following command:
         
         gcloud tasks queues resume QUEUE_ID




### Configure queue-level routing for App Engine tasks

To configure queue-level routing for App Engine tasks, set the queue's [`appEngineRoutingOverride`](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues#Queue) parameter to your preferred App Engine service and version.

  1. Set up queue-level routing and override any task-level routing:
         
         gcloud tasks queues update QUEUE_ID \
             --routing-override=service:SERVICE,version:VERSION

Replace the following:

     * `QUEUE_ID`: the queue ID (its short name).
     * `SERVICE`: the App Engine worker service responsible for task handling.
     * `VERSION`: the app version.

For example, if you set up a worker service to handle all tasks in a queue, you can route to that service and the default version:
    
    gcloud tasks queues update QUEUE_ID \
        --routing-override=service:SERVICE

  2. Verify your queue was configured successfully by running the following command:
         
         gcloud tasks queues describe QUEUE_ID --location=LOCATION

Replace `LOCATION` with the location of the queue.

The output should be similar to the following:
         
         appEngineRoutingOverride:
           host: SERVICE.PROJECT_ID.appspot.com
           service: SERVICE
         name: projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID
         rateLimits:
           maxBurstSize: 100
           maxConcurrentDispatches: 1000
           maxDispatchesPerSecond: 500.0
         retryConfig:
           maxAttempts: 100
           maxBackoff: 3600s
           maxDoublings: 16
           minBackoff: 0.100s
         state: RUNNING

  3. To remove queue-level routing, run the following command:
         
         gcloud tasks queues update QUEUE_ID \
             --clear-routing-override

When queue-level routing is removed, task-level routing is applied to tasks in the queue and tasks added to the queue in the future.




## Define rate limits

The rate limit determines the maximum rate at which tasks can be dispatched by a queue, regardless of whether the dispatch is a first task attempt or a retry.

  1. Set the maximum rate and number of concurrent tasks that can be dispatched by a queue by running the following command:
         
         gcloud tasks queues update QUEUE_ID \
             --max-dispatches-per-second=DISPATCH_RATE \
             --max-concurrent-dispatches=MAX_CONCURRENT_DISPATCHES

Replace the following:

     * `QUEUE_ID`: the queue ID (its short name).
     * `DISPATCH_RATE`: the dispatch rate. This is the rate at which tokens in the bucket are refreshed. In conditions where there is a relatively steady flow of tasks, this is the equivalent of the rate at which tasks are dispatched.
     * `MAX_CONCURRENT_DISPATCHES`: the maximum number of tasks in the queue that can run at once.

For example, if you created a queue without setting any parameters, you can update the maximum number of concurrent tasks by running the following command:
    
    gcloud tasks queues update QUEUE_ID \
        --max-concurrent-dispatches=MAX_CONCURRENT_DISPATCHES

  2. Verify your queue was configured successfully by running the following command:
         
         gcloud tasks queues describe QUEUE_ID --location=LOCATION

Replace `LOCATION` with the location of the queue.

The output should be similar to the following:
         
         name: projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID
         rateLimits:
           maxBurstSize: 100
           maxConcurrentDispatches: MAX_CONCURRENT_DISPATCHES
           maxDispatchesPerSecond: 500.0
         retryConfig:
           maxAttempts: 100
           maxBackoff: 3600s
           maxDoublings: 16
           minBackoff: 0.100s
         state: RUNNING




### Methods to define queue processing rates

You can define queue processing rates using either the Cloud Tasks API or by uploading a `queue.yaml` file. Both methods result in queues that use the same underlying mechanism.

**Caution:** While either method can be used to create queues, it is strongly recommended that you use either a `queue.yaml` file **or** the Cloud Tasks API to configure your queues, but not both. For more information, see [Use Queue Management or queue.yaml](https://docs.cloud.google.com/tasks/docs/queue-yaml).

In both cases, the queue uses the [token bucket](https://wikipedia.org/wiki/Token_bucket) algorithm to control the rate of task execution. Each named queue has a bucket that holds its tokens.

Each time your application executes a task, a token is removed from the bucket. The queue continues processing tasks until its bucket runs out of tokens. The system refills the bucket with new tokens continuously based on the `max_dispatches_per_second` rate that you specify for the queue. If your queue contains tasks to process, and the queue's bucket contains tokens, the system simultaneously processes as many tasks as there are tokens, up to the `max_concurrent_dispatches` value you have set.

An uneven load can allow the number of tokens in the bucket to grow significantly, which can lead to bursts of processing when a burst of requests comes in. In this case, your queue might experience an actual dispatch rate that exceeds your `max_dispatches_per_second` rate, consuming system resources and competing with user-serving requests. In cases where you are using queues to manage dispatch rates based on relatively slow SLAs for downstream services, this can lead to errors like HTTP `429` (Too Many Requests) or HTTP `503` (Service Unavailable).

  * When you use any Cloud Tasks API method, you have two fields to define the queue dispatch rate:

    * `max_dispatches_per_second`
    * `max_concurrent_dispatches`

A third field, `max_burst_size`, is calculated by the system based on the value you set for `max_dispatches_per_second`. For more information, see [`RateLimits` messages](https://docs.cloud.google.com/tasks/docs/reference/rpc/google.cloud.tasks.v2#ratelimits).

  * When you use the [`queue.yaml` method](https://docs.cloud.google.com/appengine/docs/standard/python/config/queueref#syntax), you can set all three elements:

    * `max_concurrent_requests`, which is equivalent to `max_concurrent_dispatches`
    * `rate`, which is equivalent to `max_dispatches_per_second`
    * `bucket_size`, which is equivalent to `max_burst_size`



In most cases, using the Cloud Tasks API method and letting the system set `max_burst_size` produce a very efficient rate for managing request bursts. In some cases, however, particularly when the rate needed is relatively slow, either using the `queue.yaml` method to manually set `bucket_size` to a small value, or setting your `max_concurrent_dispatches` to a small value using the Cloud Tasks API, can give you more control.

## Set retry parameters

If a task doesn't complete successfully, Cloud Tasks retries the task with an exponential backoff according to the parameters you have set. After a task successfully executes, it is removed from the queue. In all cases, the [maximum task retention](https://docs.cloud.google.com/tasks/docs/quotas#limits) limit also applies.

Optionally, you can specify a task-level retry configuration which overrides the queue-level retry configuration for the task. For more information, see [Set retry parameters for a task](https://docs.cloud.google.com/tasks/docs/configure-retry-task).

**Tip:** To debug your retry parameters, you can log the status code for each invocation of a task by [using Cloud Logging with your queues](https://docs.cloud.google.com/tasks/docs/monitor#logging-queues) and by setting a log sampling ratio to specify what fraction of operations to write to Cloud Logging.

  1. Specify the maximum number of times to retry failed tasks in the queue, set a time limit for retry attempts, and control the interval between attempts by running the following command:
         
         gcloud tasks queues update QUEUE_ID \
             --max-attempts=MAX_ATTEMPTS \
             --max-retry-duration=MAX_RETRY_DURATION \
             --min-backoff=MIN_INTERVAL \
             --max-backoff=MAX_INTERVAL \
             --max-doublings=MAX_DOUBLINGS

Replace the following:

     * `QUEUE_ID`: the queue ID (its short name).
     * `MAX_ATTEMPTS`: the maximum number of attempts for a task, including the first. To allow unlimited retries, set this to `-1`. `MAX_RETRY_DURATION` still applies even if `MAX_ATTEMPTS` is reached or set to `-1`.
     * `MAX_RETRY_DURATION`: the maximum amount of time for retrying a failed task, measured from when the task was first attempted. The value must be a string that ends in "s," such as `5s`. To specify an unlimited duration, set this to `0s`. `MAX_ATTEMPTS` still applies even if `MAX_RETRY_DURATION` is reached or set to `0s`.
**Note:** If you specify unlimited attempts (`MAX_ATTEMPTS` is `-1`) and an unlimited duration (`MAX_RETRY_DURATION` is `0s`), then the task is retried until it reaches the [maximum task retention](https://docs.cloud.google.com/tasks/docs/quotas#limits) limit. Otherwise, Cloud Tasks stops retrying only after both conditions are met or the task succeeds. When the task has been attempted `MAX_ATTEMPTS` times and the `MAX_RETRY_DURATION` time has passed, no further attempts are made, and the task is deleted.
     * `MIN_INTERVAL`: the minimum amount of time to wait between retry attempts. The value must be a string that ends in "s," such as `5s`.
     * `MAX_INTERVAL`: the maximum amount of time to wait between retry attempts. The value must be a string that ends in "s," such as `5s`.
     * `MAX_DOUBLINGS`: the maximum number of times that the interval between failed task retries will be doubled before the increase becomes constant. A task's retry interval starts at `MIN_INTERVAL`, then doubles `MAX_DOUBLINGS` times, then increases linearly, and finally retries at intervals of `MAX_INTERVAL` up to `MAX_ATTEMPTS` times.

For example, if `MIN_INTERVAL` is `10s`, `MAX_INTERVAL` is `300s`, and `MAX_DOUBLINGS` is `3`, the retry interval will double `3` times, increase linearly by 2^3 * 10s, and then retry at intervals of `MAX_INTERVAL` until the task has been attempted `MAX_ATTEMPTS` times: 10s, 20s, 40s, 80s, 160s, 240s, 300s, 300s, and so forth.




For more parameter details, see the [`RetryConfig` settings for the `Queue` resource](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues#retryconfig).

  1. Verify your queue was configured successfully by running the following command:
         
         gcloud tasks queues describe QUEUE_ID --location=LOCATION

Replace `LOCATION` with the location of the queue.

The output should contain the retry parameters that you set.




## What's next

  * Learn about creating [HTTP target tasks](https://docs.cloud.google.com/tasks/docs/creating-http-target-tasks).
  * Learn about creating [App Engine tasks](https://docs.cloud.google.com/tasks/docs/creating-appengine-tasks).
  * Learn more about queue management in the [RPC API reference](https://docs.cloud.google.com/tasks/docs/reference/rpc).
  * Learn more about queue management in the [REST API reference](https://docs.cloud.google.com/tasks/docs/reference/rest).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
