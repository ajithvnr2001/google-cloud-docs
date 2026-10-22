---
url: https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/pull/creating-tasks/
title: Creating Pull Tasks \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:44:02.020272+00:00
---

# Creating Pull Tasks  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/pull/creating-tasks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Creating Pull Tasks Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

Once you have [created a pull queue](https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/pull/creating-pull-queues), you can create tasks and add them to the queue.

First you need the [name](https://docs.cloud.google.com/appengine/docs/standard/reference/queueref#name) of the queue, which is defined in `queue.yaml`. Then you set the [Task](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/Task) `method` to `PULL`. The following example puts tasks in a pull queue named `pull-queue`:
    
    
    from google.appengine.api import taskqueue
    
    q = taskqueue.Queue('pull-queue')
    tasks = []
    payload_str = 'hello world'
    tasks.append(taskqueue.Task(payload=payload_str, method='PULL'))
    q.add(tasks)
    

## What's next

  * Learn how to [lease tasks](https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/pull/leasing-pull-tasks).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
