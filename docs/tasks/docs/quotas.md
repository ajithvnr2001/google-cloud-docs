---
url: https://docs.cloud.google.com/tasks/docs/quotas/
title: Quotas and limits \u00a0|\u00a0 Cloud Tasks \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:24.850456+00:00
---

# Quotas and limits  |  Cloud Tasks  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tasks/docs/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Tasks ](https://docs.cloud.google.com/tasks/docs)
  * [ Resources ](https://docs.cloud.google.com/tasks/docs/resources)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the quotas and system limits that apply to Cloud Tasks.

  * _Quotas_ have default values, but you can typically request adjustments.
  * _System limits_ are fixed values that can't be changed.



## Quotas

Google Cloud uses quotas to help ensure fairness and reduce spikes in resource use and availability. A quota restricts how much of a Google Cloud resource your Google Cloud project can use. Quotas apply to a range of resource types, including hardware, software, and network components. For example, quotas can restrict the number of API calls to a service, the number of load balancers used concurrently by your project, or the number of projects that you can create. Quotas protect the community of Google Cloud users by preventing the overloading of services. Quotas also help you to manage your own Google Cloud resources.

The Cloud Quotas system does the following:

  * Monitors your consumption of Google Cloud products and services
  * Restricts your consumption of those resources
  * Provides a way to [request changes to the quota value](https://docs.cloud.google.com/docs/quotas/help/request_increase) and [automate quota adjustments](https://docs.cloud.google.com/docs/quotas/quota-adjuster)



In most cases, when you attempt to consume more of a resource than its quota allows, the system blocks access to the resource, and the task that you're trying to perform fails.

Quotas generally apply at the Google Cloud project level. Your use of a resource in one project doesn't affect your available quota in another project. Within a Google Cloud project, quotas are shared across all applications and IP addresses. 

For more information, see the [Cloud Quotas overview](https://docs.cloud.google.com/docs/quotas/overview). 

The following table describes the quotas for Cloud Tasks resources.

Resource | Console quota name | Default value | Description  
---|---|---|---  
Maximum number of queues | **Number of queues per region** | 1,000 per region | The total number of queues (for both HTTP and App Engine targets) that can exist in a project per region, including the default queue. Queues that process tasks for App Engine targets must be in the same region as the App Engine app. This is the quota for queues created using Cloud Tasks API methods. Any queues created using `queue.yaml`, however, are based on the older Task Queues method. These queues continue to have an initial quota of 100.  
API requests | **Requests per minute per region** | 6,000,000 per minute | The total number of API requests that can be made per minute. Note that when [creating a batch of tasks](https://docs.cloud.google.com/tasks/docs/create-tasks#create-batch-tasks) (`batchCreate`) or [deleting a batch of tasks](https://docs.cloud.google.com/tasks/docs/manage-queues-and-tasks#delete-batch-tasks) (`batchDelete`), quota consumption is based on the number of tasks in the batch. Each individual task in the batch counts as one request against the API requests quota limit.  
Force run task requests | **Run task requests per minute per region** | 60 per minute | The total number of [`run task`](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues.tasks/run) requests per minute. This API is intended for manual debugging and is unrelated to normal task execution.  
List requests | **List group requests per minute per region** | 600 per minute | The total number of [`list tasks`](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues.tasks/list), [`list queues`](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues/list), and [`list locations`](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations/list) requests per minute.  
  
To adjust most quotas, use the Google Cloud console. For more information, see [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase). 

## System limits

There are also _system limits_ on Cloud Tasks resources. System limits can't be changed. 

The following table describes the system limits for Cloud Tasks.

Resource | Value | Description  
---|---|---  
Queue dispatch rate | 500 tasks per second per queue | The maximum rate at which tasks can be dispatched from a queue. To dispatch at higher rates, use multiple queues.  
Maximum task size | 1 MiB | The maximum size of a task that can be added to a queue.  
Maximum batch size | 10 MiB | The maximum size of a batch of tasks that can be added to a queue.  
Maximum number of tasks created in a batch | 100 tasks | The maximum number of tasks that can be created in a single `batchCreate` request.  
Maximum number of tasks deleted in a batch | 1,000 tasks | The maximum number of tasks that can be deleted in a single `batchDelete` request.  
Task deduplication window | Up to 24 hours | The time period during which adding a task with the same name as a recently deleted task will cause the service to reject it with an error. This is the length of time that task deduplication remains in effect after a task is deleted.  
Batch operation deduplication window | 7 days | The time period during which batch operation IDs and their results are persisted for deduplication.  
Inactive queues | Inactive after 30 days | A queue is considered `INACTIVE` if no method calls are made to it from any API, and it has had no task dispatches for this period.  
Maximum task retention | 31 days |  The time between when a task is added to a queue and when it is automatically deleted.   
Maximum schedule time for a task | 30 days from current date and time |  The maximum amount of time in the future that a task can be scheduled.   
Queue re-creation  | 3 days |  The time you must wait after deleting a queue to re-create a queue with the same name.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
