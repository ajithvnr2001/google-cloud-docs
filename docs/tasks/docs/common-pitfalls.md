---
url: https://docs.cloud.google.com/tasks/docs/common-pitfalls/
title: Issues and limitations \u00a0|\u00a0 Cloud Tasks \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:27.426782+00:00
---

# Issues and limitations  |  Cloud Tasks  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tasks/docs/common-pitfalls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Tasks ](https://docs.cloud.google.com/tasks/docs)
  * [ Guides ](https://docs.cloud.google.com/tasks/docs/dual-overview)



Send feedback 

#  Issues and limitations Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Tasks lets you build resilient asynchronous systems when you design for specific queue execution behaviors and service limits. You can prevent processing bottlenecks and unexpected delays by accounting for at-least-once delivery, system throttling, and target resource capacity.

## Execution order

With the exception of tasks scheduled to run in the future, task queues are completely platform-independent about execution order. There are no guarantees or best effort attempts made to execute tasks in any particular order. Specifically: there are no guarantees that old tasks will execute unless a queue is completely emptied. A number of common cases exist where newer tasks are executed sooner than older tasks, and the patterns surrounding this can change without notice.

## Execution delay

Cloud Tasks executions might occasionally experience minor delays, usually lasting a few minutes, due to internal system restarts. Tasks are delayed, but no tasks are lost. These are system-level events with no workaround. These events aren't logged, and their occurrence has no set timeline.

## Duplicate execution

Cloud Tasks aims for a strict "execute exactly once" semantic. However, in situations where a design trade-off must be made between guaranteed execution and duplicate execution, the service errs on the side of guaranteed execution. As such, a non-zero number of duplicate executions do occur. You should ensure that duplicate executions are handled gracefully and don't cause unexpected failures. In production, more than 99.999% of tasks are executed only once.

## Resource limitations

The most common source of backlogs in immediate processing queues is exhausting resources on the target instances. If you are attempting to execute 100 tasks per second on frontend instances that can only process 10 requests per second, a backlog will build. This typically manifests in one of two ways, either of which can generally be resolved by increasing the number of instances processing requests.

### Backoff errors and enforced rates

Servers that are being overloaded can start to return backoff errors: HTTP `503` (for App Engine targets), or HTTP `429` or `5xx` (for external targets). Cloud Tasks reacts to these errors by slowing down execution until errors stop. This system throttling prevents the worker from overloading. Note that your settings are not changed.

System throttling happens in the following circumstances:

  * Cloud Tasks backs off on all errors. Normally the backoff specified in [`rate_limits`](https://docs.cloud.google.com/tasks/docs/reference/rpc/google.cloud.tasks.v2#google.cloud.tasks.v2.Queue.FIELDS.google.cloud.tasks.v2.RateLimits.google.cloud.tasks.v2.Queue.rate_limits) is used. But if the worker returns HTTP `429 Too Many Requests`, `503 Service Unavailable`, or the rate of errors is high, Cloud Tasks uses a higher backoff rate. The retry specified in the `Retry-After` HTTP response header is considered.

  * To prevent traffic spikes and to smooth sudden increases in traffic, dispatches ramp up slowly when the queue is newly created or idle, and if large numbers of tasks suddenly become available to dispatch (due to spikes in create task rates, the queue being unpaused, or many tasks that are scheduled at the same time).




### Latency spikes and max concurrent

Overloaded servers can also respond with large increases in latency. In this situation, requests remain open for longer. Because queues run with a maximum concurrent number of tasks, this can result in queues being unable to execute tasks at the expected rate. Increasing the [`max_concurrent_dispatches`](https://docs.cloud.google.com/tasks/docs/reference/rpc/google.cloud.tasks.v2#ratelimits) for the affected queues can help in situations where the value has been set too low, introducing an artificial rate limit. But increasing `max_concurrent_dispatches` is unlikely to relieve any underlying resource pressure.

### Ramp-up issues with long running tasks

Cloud Tasks queues ramp up their output in part based on the number of successful previously dispatched tasks. If the task handler takes a considerable period of time—on the order of minutes—to complete a task and return a success response, there can be a lag in the queue ramp-up rate.

## Viewing more than 5,000 tasks

If you have more than 5,000 tasks, some tasks are not visible in the Google Cloud console. Use [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/tasks/list) to view all tasks.

## Maximum reported queue depth metric

The maximum queue depth metric reported by Cloud Tasks is capped at 1,000,000 tasks. This is intended to improve the performance of underlying task workers and there is no impact to the number of tasks that can be sent to or processed by your queue. Tasks sent to the queue above the queue depth limit will continue to execute as intended.

To fetch the current queue depth beyond 1,000,000 tasks, you can use the [`queues.tasks.list` method](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues.tasks/list). This method returns all tasks with pagination, letting you aggregate the data, and perform a count operation. However, depending on the queue depth size, the method might encounter [quota](https://docs.cloud.google.com/tasks/docs/quotas) restrictions.

## Recreating a queue with the same name

If you [delete a queue](https://docs.cloud.google.com/tasks/docs/deleting-appengine-queues-and-tasks#delete-queues) from the Google Cloud console, you must wait 3 days before recreating it with the same name. This waiting period prevents unexpected behaviour in tasks that are executing at the time of deletion or waiting to be executed. It also avoids internal process failures in the delete or recreate cycle.

## Unsupported target when using a secure perimeter

If you have set up a secure perimeter using VPC Service Controls, HTTP requests from a Cloud Tasks execution are blocked for unsupported targets, and will fail with a `TARGET_TYPE_NOT_PERMITTED_FOR_VPC` error code. For more information, see [Set up a service perimeter using VPC Service Controls](https://docs.cloud.google.com/tasks/docs/use-vpc-service-controls).

## Resource locations constraints

Cloud Tasks supports [restricting resource locations](https://docs.cloud.google.com/organization-policy/reference/restrict-locations-supported-services); however, limitations apply to the following regions:

  * `us-central1`
  * `us-central2` (private Google Cloud region)



If you specify either region in your organization policy, you must include both `us-central1` and `us-central2`, even if you are not creating Cloud Tasks resources in both regions. You can include the region `us-central2` in your organization policy even if your organization doesn't use private regions.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
