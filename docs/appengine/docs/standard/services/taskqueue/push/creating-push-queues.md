---
url: https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/push/creating-push-queues/
title: Create Push Queues \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:25:26.298104+00:00
---

# Create Push Queues  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/push/creating-push-queues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Create Push Queues Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

**Note:** To upgrade App Engine Push Queues to Cloud Tasks without making code changes, [upgrade your App Engine services SDK to the latest version](https://docs.cloud.google.com/appengine/migration-center/standard/python/migrating-push-queues-upgrade-sdk) (Preview). 

This page describes how to create and customize a push queue, and how to examine the contents of a queue.

## Using a queue configuration file to create queues

To process a task, you must add it to a push queue. App Engine provides a default push queue, named `default`, which is configured and ready to use with default settings. If you want, you can just add all your tasks to the default queue, without having to create and configure other queues.

To add queues or change the default configuration, edit the queue configuration file for your application, which you upload to App Engine. You can create up to 100 queues. Queues cannot be created dynamically.

This queue configuration file defines two queues:
    
    
    queue:
    - name: queue-blue
      target: v2.task-module
      rate: 5/s
    
    - name: queue-red
      rate: 1/s
    

To upload the file:
    
    
    gcloud app deploy queue.yaml
    

**Note:** Your app should not assume App Engine processes tasks in a queue in the order in which they were enqueued.

All tasks added to `queue-blue` are sent to the target module `v2.task-module`. The refresh rate of `queue-red` is changed from 5/s to 1/s. Tasks will be dequeued and sent to their targets at the rate of 1 task per second.

If you delete a queue, you must wait approximately 7 days before creating a new queue with the same name.

There are many other parameters that can be added to the configuration file to customize the behavior of a push queue. For more information, see the [queue configuration file reference](https://docs.cloud.google.com/appengine/docs/standard/reference/queueref).

**Note:** If you are using a service account to manage authentication for deploying your queue configuration file, it needs to have the `serviceusage.services.list` permission. This permission can be added either using the [`serviceusage.serviceUsageViewer`](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage) role or by creating a [custom role](https://docs.cloud.google.com/iam/docs/understanding-custom-roles) with that permission.

## Defining the push queue processing rate

You can control the rate at which tasks are processed in each of your queues by defining other directives, such as [`rate`](https://docs.cloud.google.com/appengine/docs/standard/reference/queueref#rate), [`bucket_size`](https://docs.cloud.google.com/appengine/docs/standard/reference/queueref#bucket_size), and [`max_concurrent_requests`](https://docs.cloud.google.com/appengine/docs/standard/reference/queueref#max_concurrent_requests).

The task queue uses [token buckets](https://wikipedia.org/wiki/Token_bucket) to control the rate of task execution. Each named queue has a token bucket that holds tokens, up to the maximum specified by the `bucket_size`, or a maximum of 5 tokens if you don't specify the bucket size.

Each time your application executes a task, a token is removed from the bucket. Your app continues processing tasks in the queue until the queue's bucket runs out of tokens. App Engine refills the bucket with new tokens continuously based on the `rate` that you specified for the queue.

If your queue contains tasks to process, and the queue's bucket contains tokens, App Engine simultaneously processes as many tasks as there are tokens. This can lead to bursts of processing, consuming system resources and competing with user-serving requests.

If you want to prevent too many tasks from running at once or to prevent datastore contention, use `max_concurrent_requests`.

The following sample shows how to set `max_concurrent_requests` to limit tasks and also shows how to adjust the bucket size and rate based on your application's needs and available resources:
    
    
    queue:
    - name: queue-blue
      rate: 20/s
      bucket_size: 40
      max_concurrent_requests: 10
    

## Setting storage limits for all queues

You can use your queue configuration file to define the total amount of storage that task data can consume over all queues. To define the total storage limit, include an element named [`total_storage_limit`](https://docs.cloud.google.com/appengine/docs/standard/reference/queueref#total_storage_limit) at the top level:
    
    
    # Set the total storage limit for all queues to 120MB
    total_storage_limit: 120M
    queue:
    - name: queue-blue
      rate: 35/s
    

The value is a number followed by a unit: `B` for bytes, `K` for kilobytes, `M` for megabytes, `G` for gigabytes, `T` for terabytes. For example, `100K` specifies a limit of 100 kilobytes. If adding a task would cause the queue to exceed its storage limit, the call to add the task will fail. The default limit is `500M` (500 megabytes) for free apps. For billed apps there is no limit until you explicitly set one. You can use this limit to protect your app from a [fork bomb](https://wikipedia.org/wiki/Fork_bomb) programming error in which each task adds multiple other tasks during its execution.

If your app is receiving errors for insufficient quota when adding tasks, increasing the total storage limit can help. If you are using this feature, we strongly recommend setting a limit that corresponds to the storage required for several days' worth of tasks. This allows the queues to be temporarily backed up and continue to accept new tasks while working through the backlog while still being protected from a fork bomb programming error.

## Monitoring queues in the Google Cloud console

  1. In the Google Cloud console, go to the Cloud Tasks page.

[Go to **Cloud Tasks**](https://console.cloud.google.com/cloudtasks)

Note that if you go to the App Engine **Task queue** page, there will be instructions that guide you to the Cloud Tasks page. This update in the Google Cloud console does not change how Task queues function.

  2. Enable the Cloud Tasks API.

  3. Once you're in the Cloud Tasks page, you will see a list of all of the queues in the application. Clicking on a the name of a queue brings up the **Queue Details** page, which shows all of the tasks in the selected queue.




## What's next

Learn about [creating tasks](https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/push/creating-push-tasks).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
