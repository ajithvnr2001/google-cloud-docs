---
url: https://docs.cloud.google.com/appengine/migration-center/standard/go/migrating-push-queues-overview/
title: Migrating push queues to Cloud Tasks overview (Go) \u00a0|\u00a0 App Engine migration center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:42.713860+00:00
---

# Migrating push queues to Cloud Tasks overview (Go)  |  App Engine migration center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/migration-center/standard/go/migrating-push-queues-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Migration center ](https://docs.cloud.google.com/appengine/migration-center)
  * [ Guides ](https://docs.cloud.google.com/appengine/migration-center/standard/services/migrating-services)



Send feedback 

#  Migrating push queues to Cloud Tasks overview (Go) Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how you can migrate Task Queues push queues to Cloud Tasks. While App Engine push queues are restricted to App Engine targets, Cloud Tasks is Google Cloud's modern, fully managed task execution service that lets your App Engine service target any HTTP endpoint.

You can migrate your push queues in one of two ways:

  1. [Upgrade to the latest App Engine services SDK (Recommended)](https://docs.cloud.google.com/appengine/migration-center/standard/go/migrating-push-queues-upgrade-sdk): Migrate without making any changes to your application code by updating to the latest App Engine services SDK.
  2. [Upgrade to the Cloud Tasks client libraries](https://docs.cloud.google.com/appengine/migration-center/standard/go/migrating-push-queues): Refactor your application code to use the Cloud Tasks client libraries directly.



In Cloud Tasks, all queues operate as push queues. In the remainder of this guide and in the [Cloud Tasks documentation](https://docs.cloud.google.com/tasks/docs), the term _queue_ is equivalent to the term _push queue_. Similarly, the term _task_ is equivalent to the term _push task_.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
