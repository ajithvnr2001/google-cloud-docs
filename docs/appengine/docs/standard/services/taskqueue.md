---
url: https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/
title: Task Queue Overview \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:18:24.404427+00:00
---

# Task Queue Overview  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Task Queue Overview Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

This page describes what task queues are, and when and how to use them. Task queues let applications perform work, called _tasks_ , asynchronously outside of a user request. If an app needs to execute work in the background, it adds tasks to _task queues_. The tasks are executed later, by worker services.

The Task Queue service is designed for asynchronous work. It does not provide strong guarantees around the timing of task delivery and is therefore unsuitable for interactive applications where a user is waiting for the result.

## Push queues and pull queues

Task queues come in two flavors, _push_ and _pull_. The manner in which the Task Queue service dispatches task requests to worker services is different for the different queues.

**Push queues** run tasks by delivering HTTP requests to App Engine worker services. They dispatch these requests at a reliable, steady rate and guarantee reliable task execution. Because you can control the rate at which tasks are sent from the queue, you can control the workers' scaling behavior and hence your costs.

Because tasks are executed as requests targeted at App Engine services, they are subject to stringent deadlines. Tasks handled by automatic scaling services must finish in ten minutes. Tasks handled by basic and manual scaling services can run for up to 24 hours.

**Pull queues** do not dispatch tasks at all. They depend on other worker services to "lease" tasks from the queue on their own initiative. Pull queues give you more power and flexibility over when and where tasks are processed, but they also require you to do more process management. When a task is leased the leasing worker declares a deadline. By the time the deadline arrives the worker must either complete the task and delete it or the Task Queue service will allow another worker to lease it. **Tip:** In some cases [Google Cloud Pub/Sub](https://docs.cloud.google.com/pubsub/overview) is a good alternative to pull queues.

All task queue tasks are performed **asynchronously**. The application that creates the task hands it off to the queue. The originating application is not notified whether or not the task completes, or if it was successful.

If a worker fails to process a task, the Task Queue service provides the queue with a retry mechanism, so the task can be retried a finite number of times.

## Use cases

### Push queues

One typical push queue use case is a "slow" operation. Consider a social network messaging system. Every time a user sends a message, the network needs to update the followers of the sender. This can be a very time-consuming operation. Using a push queue, the application can enqueue a task for each message as it arrives to be dispatched to a worker service for processing. When the worker receives the task request, it can retrieve the sender's list of followers and update the DB for each one. The worker can be made even more efficient by enqueuing another pushtask for each database update.

Another use for push queues is scheduled tasks. Imagine an application that implements an ad campaign. A group of tasks written to send out emails can be added to a push queue with instructions to withhold the tasks until a specified time in the future. When the due date arrives, the Task Queue service will begin to issue requests to execute the tasks.

### Pull queues

Pull queues work well when you need to batch tasks together for efficient execution. One solution takes advantage of the ability to attach a _tag_ to a pull task. Workers can lease a group of tasks that have the same tag. A typical example might be an app that maintains leaderboards for numerous different games, with many players and groups constantly in play. Every time there is a new high score, the app can enqueue a pull task with the score and the player, and use the game ID as a task tag. A worker periodically "wakes up", leases a group of tasks with the same game ID, and updates the leaderboard. You can lease tasks explicitly, using a specified tag value, or let the service decide which group of similarly tagged tasks to send.

Batching with tags can be very powerful. Since tags can be dynamically generated while your app is running, a worker can handle new game IDs with no special effort. 

## What's next

  * Read about [push queues](https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/push)
  * Read about [pull queues](https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/pull)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
