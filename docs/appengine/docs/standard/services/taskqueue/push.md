---
url: https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/push/
title: Use Push Queues \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:47:55.972984+00:00
---

# Use Push Queues  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/push/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Use Push Queues Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

**Note:** To upgrade App Engine Push Queues to Cloud Tasks without making code changes, [upgrade your App Engine services SDK to the latest version](https://docs.cloud.google.com/appengine/migration-center/standard/python/migrating-push-queues-upgrade-sdk) (Preview). 

This page provides an overview of push queues. Push queues run tasks by dispatching HTTP requests to App Engine worker services. The requests are delivered at a constant rate. If a task fails, the service retries the task, sending another request. You must provide a handler for every kind of task you use. A single service can have multiple handlers for different kinds of tasks, or you can use different services to manage different task types.

![The application offloads the task to the task queue service, which uses HTTP to
send it to the worker](https://docs.cloud.google.com/static/appengine/docs/images/push-queue.svg)

## The task deadline

When a worker service receives a push task request, it must handle the request and send an HTTP response before a deadline that depends on the [scaling type](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine#instances) of the worker service.

Automatic scaling services must finish before 10 minutes have elapsed. Manual and basic scaling services can run up to 24 hours.

An HTTP response code between 200–299 indicates success; all other values indicate the task failed. If the task fails to respond within the deadline, or returns an invalid response value, the task is retried.

## Retrying a failed task

If a push task request handler returns an HTTP status code outside the range 200–299, or fails to return any response before the task deadline occurs, the queue retries the task until it succeeds. The system backs off gradually to avoid flooding your application with too many requests, but schedules retry attempts for failed tasks to recur at a minimum of once per hour.

## Working with push queues

When working with push queues, at a minimum, you'll need to do the following things:

  * [Create tasks programmatically](https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/push/creating-push-tasks) and add them to the default push queue, or to one or more named push queues that you have created.
  * [Write a handler](https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/push/creating-handlers) that processes a task's request, and assign the handler to an App Engine service.



Optionally, you can also:

  * [Create and customize multiple queues](https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/push/creating-push-queues) to perform multiple tasks efficiently.
  * [Monitor and manage](https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/push/creating-push-queues#monitoring_queues_in_the_console_name_short) your push queues in the Google Cloud console.



When you use push queues, your application is subject to additional [quotas](https://docs.cloud.google.com/appengine/docs/quotas#Task_Queue).

## What's next

  * Learn how to [create push queues](https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/push/creating-push-queues).
  * Learn how to [create tasks](https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/push/creating-push-tasks).
  * Learn about [writing handlers](https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/push/creating-handlers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
