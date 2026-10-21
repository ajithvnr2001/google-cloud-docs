---
url: https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/pull/leasing-pull-tasks/
title: Leasing Pull Tasks \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:47:57.682411+00:00
---

# Leasing Pull Tasks  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/pull/leasing-pull-tasks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Leasing Pull Tasks Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

Once tasks are in a pull queue, a worker can lease them. After the tasks are processed the worker must delete them.

## Before you begin

  * Create a [pull queue](https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/pull/creating-pull-queues).
  * [Create tasks](https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/pull/creating-tasks) and add them to the pull queue.



## Important context

  * This method is only applicable to workers that are running within a service in the standard environment.
  * When you use pull queues, you are responsible for scaling your workers based on your processing volume.



## Leasing tasks

After the tasks are in the queue, a worker can lease one or more of them using the [`lease_tasks()`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/Queue#lease_tasks) method. There may be a short delay before tasks recently added using [`add()`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/Queue#add) become available via [`lease_tasks()`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/Queue#lease_tasks) .

When you request a lease, you specify the number of tasks to lease (up to a maximum of 1,000 tasks) and the duration of the lease in seconds (up to a maximum of one week). The lease duration needs to be long enough to ensure that the slowest task will have time to finish before the lease period expires. You can modify a task lease using [`modify_task_lease()`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/Queue#modify_task_lease) .

Leasing a task makes it unavailable for processing by another worker, and it remains unavailable until the lease expires.

The [`lease_tasks()`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/Queue#lease_tasks) method returns a [Task](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/Task) object containing a list of tasks leased from the queue.

**Note:** `lease_tasks()` operates only on pull queues. If you attempt to lease tasks added in a push queue, App Engine throws an exception.

The following code sample leases 100 tasks from the queue `pull-queue` for one hour:
    
    
    from google.appengine.api import taskqueue
    
    q = taskqueue.Queue('pull-queue')
    q.lease_tasks(3600, 100)
    

### Batching with task tags

Not all tasks are alike; your code can "tag" tasks and then choose tasks to lease by tag. The tag acts as a filter.
    
    
    from google.appengine.api import taskqueue
    
    q = taskqueue.Queue('pull-queue')
    q.add(taskqueue.Task(payload='parse1', method='PULL', tag='parse'))
    q.add(taskqueue.Task(payload='parse2', method='PULL', tag='parse'))
    q.add(taskqueue.Task(payload='render1', method='PULL', tag='render'))
    q.add(taskqueue.Task(payload='render2', method='PULL', tag='render'))
    
    q.lease_tasks_by_tag(3600, 100, 'render') # leases render tasks, but not parse
    
    q.lease_tasks_by_tag(3600, 100) # Leases up to 100 tasks that have same tag.
    

### Regulating polling rates

Workers that poll the queue for tasks to lease should detect whether they are attempting to lease tasks faster than the queue can supply them. If this failure occurs, the following exceptions from [`lease_tasks()`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/Queue#lease_tasks) can be generated:

  * `google.appengine.api.taskqueue.TransientError`
  * `google.appengine.runtime.apiproxy_errors.DeadlineExceededError`



  
Your code must catch these exceptions, back off from calling [`lease_tasks()`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/Queue#lease_tasks) , and then try again later. To avoid this problem, consider setting a higher RPC deadline when calling [`lease_tasks()`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/Queue#lease_tasks) . You should also back off when a lease request returns an empty list of tasks.  
  
If you generate more than 10 LeaseTasks requests per queue per second, only the first 10 requests will return results. If requests exceed this limit, `OK` is returned with zero results.

## Monitoring tasks in the Google Cloud console

To view information about all the tasks and queues in your application:

  1. Open the **Cloud Tasks** page in the Google Cloud console and look for the _Pull_ value in column **Type**.

[Go to Cloud Tasks](https://console.cloud.google.com/cloudtasks)

  2. Click on the name of the queue in which you are interested, opening the queue details page. It displays all of the tasks in the selected queue.




## Deleting tasks

Once a worker completes a task, it needs to delete the task from the queue. If you see tasks remaining in a queue after a worker finishes processing them, it is likely that the worker failed; in this case, the tasks will be processed by another worker.

You can delete a list of tasks, such as that returned by `lease_tasks()` , simply by passing it to [`delete_tasks()`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/Queue#delete_tasks):
    
    
    from google.appengine.api import taskqueue
    
    q = taskqueue.Queue('pull-queue')
    tasks = q.lease_tasks(3600, 100)
    # Perform some work with the tasks here
    q.delete_tasks(tasks)
    

## An end-to-end example of pull queues

For a simple but complete end-to-end example of using pull queues in Python, see [appengine-pullqueue-counter](https://github.com/GoogleCloudPlatform/appengine-pullqueue-counter).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
