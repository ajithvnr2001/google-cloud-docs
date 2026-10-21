---
url: https://docs.cloud.google.com/tasks/docs/migrating/
title: Migrate from Task Queues to Cloud Tasks \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:53.903065+00:00
---

# Migrate from Task Queues to Cloud Tasks  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tasks/docs/migrating/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Tasks ](https://docs.cloud.google.com/tasks/docs)
  * [ Guides ](https://docs.cloud.google.com/tasks/docs/dual-overview)



Send feedback 

#  Migrate from Task Queues to Cloud Tasks Stay organized with collections  Save and categorize content based on your preferences. 

You can migrate from using App Engine standard environment's queue service (Task Queues) via the App Engine Task Queue API to accessing that same service using Cloud Tasks, a new RPC/REST API. Cloud Tasks can be employed outside of first generation App Engine runtimes, particularly from all [App Engine flexible environments](https://docs.cloud.google.com/appengine/docs/flexible), as well as from [second generation App Engine standard environment runtimes](https://docs.cloud.google.com/appengine/docs/standard/runtimes).

Cloud Tasks and the current App Engine standard environment task queue service exist in a single universe. You can add to the same queues through either API. Regardless of whether you use the App Engine SDK or the new Cloud Tasks API, a queue within the app forwards a task to a handler URL for asynchronous processing.

### New features

Cloud Tasks provides some features not available via the App Engine SDK, including the following:

  * Queue management via the API:

You can create, delete, pause, and perform other queue management tasks using the API, through the Console, or via the `gcloud` command.

  * List Queues command:

You can list all the queues you have set up in your project.

  * List Tasks command:

You can list all the tasks in any of your queues.

  * Identity and Access Management (IAM) integration:

You can secure access to your queues and tasks in a highly granular way using [IAM](https://docs.cloud.google.com/iam).

  * HTTP targets

You can target handlers at any HTTP endpoint with a public IP address.




### Features in Task Queues not yet available via Cloud Tasks API:

  * [Pull queues](https://docs.cloud.google.com/appengine/docs/standard/python/taskqueue/pull):

You can use [Cloud Pub/Sub](https://docs.cloud.google.com/pubsub), a GA product, to implement many of the same use cases as pull queues.

  * [Transactional tasks](https://docs.cloud.google.com/appengine/docs/standard/python/taskqueue/push/creating-tasks#enqueuing_tasks_in_cloud_datastore_transactions):

Cloud Tasks does not support enqueuing a task as part of a Cloud Datastore transaction, such that the task is only enqueued - and is guaranteed to be enqueued - if the transaction is committed successfully.

  * [Deferred/delayed tasks](https://docs.cloud.google.com/appengine/docs/standard/python/taskqueue/push/creating-tasks#using_the_instead_of_a_worker_service):

In some cases where you might need a series of diverse small tasks handled asynchronously but you don't want to go through the work of setting up individual distinct handlers, the App Engine SDK allows you to use runtime specific libraries to create simple functions to manage these tasks. This feature is not available in Cloud Tasks. Note, though, that normal tasks _can_ be scheduled in the future using Cloud Tasks.

  * [Namespacing](https://docs.cloud.google.com/appengine/docs/standard/python/taskqueue/push/creating-tasks#working_with_tasks_in_a_multi-tenant_application):

Some of the runtimes that use the App Engine SDK have APIs that support task multitenancy through namespacing. This feature is not available in Cloud Tasks.

  * [Local emulator](https://docs.cloud.google.com/appengine/docs/standard/python/tools/using-local-server):

The local development server provided by the gcloud CLI or the App Engine SDK does not support simulated endpoints for Cloud Tasks API calls.

  * [Asynchronous task add](https://docs.cloud.google.com/appengine/docs/standard/python/taskqueue/push/creating-tasks#adding_tasks_asynchronously):

Users of the App Engine SDK can choose to add tasks to queues asynchronously. This feature is not available in Cloud Tasks.




### For more information

More detailed guides for migrating your code can be found in the App Engine Task Queue documentation set:

  * Migrating from Python 2.7 [pull queues](https://docs.cloud.google.com/appengine/docs/standard/python/taskqueue/pull/migrating-pull-queues) to Pub/Sub
  * Migrating from Python 2.7 [push queues](https://docs.cloud.google.com/appengine/docs/standard/python/taskqueue/push/migrating-push-queues) to Cloud Tasks
  * Migrating from Java 8 [pull queues](https://docs.cloud.google.com/appengine/docs/standard/java/taskqueue/pull/migrating-pull-queues) to Pub/Sub
  * Migrating from Java 8 [push queues](https://docs.cloud.google.com/appengine/docs/standard/java/taskqueue/push/migrating-push-queues) to Cloud Tasks



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
