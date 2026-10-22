---
url: https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/push/deleting-tasks-and-queues/
title: Delete Tasks and Queues \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:44:00.569054+00:00
---

# Delete Tasks and Queues  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/push/deleting-tasks-and-queues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Delete Tasks and Queues Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

**Note:** To upgrade App Engine Push Queues to Cloud Tasks without making code changes, [upgrade your App Engine services SDK to the latest version](https://docs.cloud.google.com/appengine/migration-center/standard/python/migrating-push-queues-upgrade-sdk) (Preview). 

This page describes how to delete tasks from a push queue and how to delete queues. In some cases you might need to delete a task that cannot be completed successfully, no matter how many times it is retried.

## Delete tasks from a queue

###  API 

Use [`delete_tasks()`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/Queue#delete_tasks) to delete an individual task:
    
    
    from google.appengine.api import taskqueue
    
    # Delete an individual task...
    q = taskqueue.Queue('queue1')
    q.delete_tasks(taskqueue.Task(name='foo'))
    

###  Console 

To delete a task from the Google Cloud console:

  1. Open the Cloud Tasks page in the console.

[Go to Cloud Tasks](https://console.cloud.google.com/cloudtasks)

  2. Click the name of the queue from which you want to remove the task.

  3. Select the task that you want to delete and click **Delete selected tasks**.

![The Delete
  selected tasks button is the last in the list of actions at the top
  right of the page.](https://docs.cloud.google.com/static/appengine/docs/images/console/delete-task.png)

  4. Click **Delete**.




## Purging all tasks from a queue

###  API 

Use [`purge()`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/Queue#purge) to delete all tasks from the specified queue:
    
    
    from google.appengine.api import taskqueue
    
    # Purge entire queue...
    q = taskqueue.Queue('queue1')
    q.purge()
    

###  Console 

To delete a task from the Google Cloud console:

  1. Open the Cloud Tasks page in the console.

[Go to Cloud Tasks](https://console.cloud.google.com/cloudtasks)

  2. Click the name of the queue from which you want to remove the task.

  3. Select the task that you want to delete and click **Delete all tasks**.

![The
  Delete all tasks button purges all tasks from the queue.](https://docs.cloud.google.com/static/appengine/docs/images/console/delete-all-tasks.png)

  4. Click **Delete**.




All tasks created before the moment of purging are expunged. Purge operations can take up to one minute to take effect.

It can take several hours to reclaim the quotas freed up by purging a queue.

**Warning:** Do not create new tasks immediately after purging a queue. Wait at least a second. Tasks created in close temporal proximity to a purge call will also be purged.

## Pausing queues

You can pause a queue by removing its definition from your `queue.yaml` file and then uploading the edited `queue.yaml` file. Setting any queue's rate to 0 will also pause the queue.

Any tasks that remain on a paused queue or any new tasks that are added to it will not be processed. You can resume the paused queue by uploading a new `queue.yaml` file with the queue defined and rate set to a non-zero value. Paused queues continue to count as a part of your quota.

You can also pause a queue from within the [Cloud Tasks page in the Google Cloud console](https://console.cloud.google.com/cloudtasks).

## Deleting queues

It is a best practice to pause a queue before you delete it:

  1. Remove the queue definition from your `queue.yaml` file.

  2. Upload the change to your `queue.yaml` file.

gcloud app deploy queue.yaml




Once the queue is removed from your `queue.yaml` file, use the Google Cloud console to delete it.

  1. In the Google Cloud console, select the queue.

[Go to Cloud Tasks](https://console.cloud.google.com/cloudtasks)

  2. Click **Delete queue**.




If you delete a queue from the Google Cloud console, you must wait 7 days before recreating with the same name.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
