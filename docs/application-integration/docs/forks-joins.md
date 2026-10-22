---
url: https://docs.cloud.google.com/application-integration/docs/forks-joins/
title: Forks and joins \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:58.761830+00:00
---

# Forks and joins  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/forks-joins/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Forks and joins

Forks and joins are control points in an integration that let you specify the behaviour of a task (also known as the task's execution strategy) based on the task's incoming and outgoing conditions.

If you have enabled the [canvas view](https://docs.cloud.google.com/application-integration/docs/canvas-view), you can configure the fork and join execution policies directly in the task configuration pane.

## Fork

A fork is a control point for the _outgoing_ [edges](https://docs.cloud.google.com/application-integration/docs/edge-overview) of a task. It lets you specify the execution strategy for the immediate next tasks. You can click on a fork to open the **Fork configuration pane** and configure any one of the following execution strategies for a task: 

  * **Run all match** : Runs all the immediate next tasks whose edge conditions evaluate to true. 
  * **Run first match** : Runs the immediate next task (in no specific order) whose edge conditions evaluate to true. For example, if there are three immediate next tasks and the edge conditions for any task (in no specific order) evaluate to true, then that task is run.



The following image shows how to configure fork for a task in the old canvas view:

![image showing highlighted fork](https://docs.cloud.google.com/static/application-integration/images/integrations_fork.png)![image showing highlighted fork](https://docs.cloud.google.com/static/application-integration/images/integrations_fork.png)

If you have enabled the [canvas view](https://docs.cloud.google.com/application-integration/docs/canvas-view), you can configure the fork execution policy directly in the task configuration pane. 

![Configure fork in the canvas](https://docs.cloud.google.com/static/application-integration/images/configure-fork.png)![Configure fork in the canvas](https://docs.cloud.google.com/static/application-integration/images/configure-fork.png)

## Join

A join is a control point for the _incoming[edges](https://docs.cloud.google.com/application-integration/docs/edge-overview)_ of a task. It lets you specify the execution strategy for the current task. When there are multiple incoming edges for a task, you can specify the conditions for which the task runs. You can click on a join to open the **Join configuration pane** and configure any one of the following execution strategies for a task: 

  * **When all tasks and conditions succeed** : Runs the task when all tasks and conditions are met, that is, all the upstream dependent tasks run successfully and the edge conditions of all tasks evaluate to true. If any of the upstream tasks or edge conditions fail, the task is not run.
  * **When all succeed** : Runs the task if all its prerequisites are met, that is, all the upstream dependent tasks run successfully. If any of the upstream tasks fail, the task is not run. 
  * **When any succeed** : Runs the task if any one of its prerequisites are met, that is, at least one of the dependent tasks runs successfully. If all of the previous tasks fail, the task is not run.



The following image shows how to configure edge for a task in the old canvas view:

![image showing highlighted join](https://docs.cloud.google.com/static/application-integration/images/integrations_join.png)![image showing highlighted join](https://docs.cloud.google.com/static/application-integration/images/integrations_join.png)

If you have enabled the [canvas view](https://docs.cloud.google.com/application-integration/docs/canvas-view), you can configure the edge execution strategy directly in the task configuration pane. 

![Configure edge in the canvas](https://docs.cloud.google.com/static/application-integration/images/configure-edge.png)![Configure edge in the canvas](https://docs.cloud.google.com/static/application-integration/images/configure-edge.png)

## Quotas and limits

For information about quotas and limits, see [Quotas and limits](https://docs.cloud.google.com/application-integration/docs/quotas).

## What's next

  * Learn about [all tasks and triggers](https://docs.cloud.google.com/application-integration/docs/all-triggers-tasks).
  * Learn how to [test and publish an integration](https://docs.cloud.google.com/application-integration/docs/test-publish-integrations).
  * Learn about [error handling](https://docs.cloud.google.com/application-integration/docs/error-handling-strategy).
  * Learn about [integration execution logs](https://docs.cloud.google.com/application-integration/docs/introduction-logs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
