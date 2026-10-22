---
url: https://docs.cloud.google.com/application-integration/docs/triggers/
title: Triggers \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:35:40.483783+00:00
---

# Triggers  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/triggers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Triggers

A trigger is an external event that initiates a task, or sequence of tasks, in an integration. You can think of a trigger as an entry point to your integration and the event tied to the trigger causes the tasks associated with the trigger to run.

You can add multiple triggers to your integration. However, when an event occurs, only the trigger associated with the event begins executing its tasks. For more information, see Adding multiple triggers in an integration. 

For the list of all the available out-of-the-box triggers, see [All triggers](https://docs.cloud.google.com/application-integration/docs/all-triggers-tasks). 

## Connector Event triggers

Connector Event triggers are specialized triggers that let you invoke an integration based on the [event subscription](https://docs.cloud.google.com/integration-connectors/docs/eventsubscription) created in various business applications using [Integration Connectors](https://docs.cloud.google.com/integration-connectors/docs). 

For the list of all the available Connector Event triggers, see [Connector Event triggers](https://docs.cloud.google.com/application-integration/docs/all-triggers-tasks#event_triggers). For more information about event subscriptions in Integration Connectors, see [Event subscriptions](https://docs.cloud.google.com/integration-connectors/docs/eventsubscription).

## Adding multiple triggers in an integration

You can add one or more triggers in an integration where each trigger is associated with a different task. The integration starts from the trigger for which the event occurs. For example, consider your integration has two triggers where `Trigger-1` is associated with `Task-1`, and `Trigger-2` is associated with a downstream task `Task-5`. Now suppose an event triggers `Trigger-2`, the integration runs from `Task-5` onwards. 

If multiple triggers run at the same time, each trigger runs its copy of the integration. In the preceding example, if both `Trigger-1` and `Trigger-2` run simultaneously, `Trigger-1` runs the integration from `Task-1` onwards, and `Trigger-2` runs a separate copy of the integration from `Task-5` onwards. There is no overlap between the execution flows of the two integrations. 

## Execution modes

Based on the trigger, your integration is executed in either synchronous or asynchronous mode: 

  * **Synchronous executions:** In synchronous mode, the execution result of the integration is available soon after the integration runs. Synchronous mode is helpful in scenarios where you want the execution result immediately after the integration runs. Triggers execute the integration in the synchronous mode include the following: 
    * [Test or publish an integration](https://docs.cloud.google.com/application-integration/docs/test-publish-integrations)
    * Call the [`projects.locations.integrations.execute`](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.integrations/execute) API
    * Call the integration from a [sub-integration in the synchronous mode](https://docs.cloud.google.com/application-integration/docs/configure-call-integration-task)
  * **Asynchronous executions:** Asynchronous executions use the fire and forget model. Asynchronous mode is helpful in scenarios where integrations can take a long time to run, or the execution result is not required immediately after the integration runs. Triggers that execute the integration in the asynchronous mode include the following: 
    * All execution that are not synchronous are executed in asynchronous mode. Some of the common asynchronous mode includes, but is not limited to: 
      * [Schedule trigger](https://docs.cloud.google.com/application-integration/docs/configure-schedule-trigger)
      * [Cloud Scheduler trigger](https://docs.cloud.google.com/application-integration/docs/configure-cloud-scheduler-trigger)
      * [Cloud Pub/Sub trigger](https://docs.cloud.google.com/application-integration/docs/configure-pubsub-trigger)
      * [Salesforce trigger](https://docs.cloud.google.com/application-integration/docs/configure-salesforce-trigger)
      * Call the [`projects.locations.integrations.schedule`](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.integrations/schedule) API
    * Executions that are resumed from a suspension or a approval task are also executed in aynchronous mode, even if the initial execution was is synchronous mode. 



## Quotas and limits

For information about quotas and limits, see [Quotas and limits](https://docs.cloud.google.com/application-integration/docs/quotas).

## What's next

  * Learn about [all tasks and triggers](https://docs.cloud.google.com/application-integration/docs/all-triggers-tasks).
  * Learn how to [test and publish an integration](https://docs.cloud.google.com/application-integration/docs/test-publish-integrations).
  * Learn about [error handling](https://docs.cloud.google.com/application-integration/docs/error-handling-strategy).
  * Learn about [integration execution logs](https://docs.cloud.google.com/application-integration/docs/introduction-logs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
