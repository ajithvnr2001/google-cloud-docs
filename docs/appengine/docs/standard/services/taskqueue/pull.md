---
url: https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/pull/
title: Using Pull Queues \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:18:50.484886+00:00
---

# Using Pull Queues  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/pull/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Using Pull Queues Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

This page provides an overview of pull queues in the App Engine standard environment.

In _push_ queues tasks are delivered to a worker service based on the queue's configuration. In _pull_ queues the worker service must _ask_ the queue for tasks. The queue responds by allowing that worker unique access to process the task for a specified period of time, which is called a _lease_.

![The application offloads the task to the task queue service and then the worker leases
it from the task queue service](https://docs.cloud.google.com/static/appengine/docs/images/app-engine-task-diagram.svg)

Using pull queues, you can also group related tasks using tags and then configure your worker to pull multiple tasks with a certain tag all at once. This process is called _batching_.

If a worker cannot process a task before its lease expires, it can either renew the lease or let it expire, at which point another worker can acquire it. Once the work associated with a task is complete, the worker must delete it.

Using pull queues requires your code to handle some functions that are automated in push queues:

Scaling your workers
    Your code needs to scale the number of workers based on processing volume. If your code does not handle scaling, you risk wasting computing resources if there are no tasks to process; you also risk latency if you have too many tasks to process.
Deleting the tasks
    Your code also needs to explicitly delete tasks after processing. In push queues, App Engine deletes the tasks for you. If your worker does not delete pull queue tasks after processing, another worker will re-process the task. This wastes computing resources and risks errors if tasks are not [idempotent](https://wikipedia.org/wiki/Idempotence).

Pull queues in the App Engine standard environment are created by setting a property in a configuration file called ` queue.yaml `.

## Pull queue workflow

Workers that process tasks from pull queues must be defined within a service that runs in the App Engine standard environment.

The workflow is as follows:

  1. You [create a pull queue](https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/pull/creating-pull-queues), using ` queue.yaml `.
  2. You [create tasks](https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/pull/creating-tasks) and add them to the queue.
  3. The worker you have created [leases the task](https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/pull/leasing-pull-tasks), using [TaskQueue](/appengine/docs/standard/go/reference/services/bundled/latest/taskqueue).
  4. App Engine sends task data to the worker in the lease response.
  5. The worker processes the task. If the task fails to execute before the lease expires, the worker can modify the lease duration. If the lease expires, the task will be available to be leased to another worker.
  6. After a task is processed successfully, the [worker deletes it](https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/pull/leasing-pull-tasks#deleting-tasks).



## What's next

  * Learn how to [create pull queues](https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/pull/creating-pull-queues).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
