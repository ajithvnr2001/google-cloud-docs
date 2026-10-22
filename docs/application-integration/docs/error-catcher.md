---
url: https://docs.cloud.google.com/application-integration/docs/error-catcher/
title: Error catcher \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:39:00.026096+00:00
---

# Error catcher  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/error-catcher/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Error catcher

Error catcher is one of the error handling methods in Application Integration that helps you handle task and event failures encountered during the execution of an integration. 

Error catchers work very similar to a sub integration flow within your main integration. Each error catcher can be invoked using a trigger, called the [Error catcher](https://docs.cloud.google.com/application-integration/docs/configure-error-catcher-trigger) trigger, to run the set of configured [integration tasks](https://docs.cloud.google.com/application-integration/docs/how-to-guides#configure-integration-tasks) customized to handle the error. **Note:** Error catchers can't be nested. You cannot define an error catcher that in turn calls another error catcher using a different Error catcher trigger in your integration.  You can define one or more error catchers in a single integration to the handle errors or execution failures at both, the task and event levels. 

## Error catcher at the task level

Error catchers at the task level handle individual task failures during the execution of your integration. 

The following image shows a sample integration flow that uses error catcher at the task level: 

![image showing error catcher at the task level](https://docs.cloud.google.com/static/application-integration/images/error-catcher-task.png)![image showing error catcher at the task level](https://docs.cloud.google.com/static/application-integration/images/error-catcher-task.png)

## Error catcher at the event level

Event-level error catchers handle execution failures such as integration failures, edge condition failures, task failures, and retry execution failures. Error catchers at the event level are invoked when you have not defined or attached task-level error catchers to handle any task failures. 

The following image shows a sample integration flow that uses error catcher at the event level: 

![image showing error catcher at the event level](https://docs.cloud.google.com/static/application-integration/images/error-catcher-event.png)![image showing error catcher at the event level](https://docs.cloud.google.com/static/application-integration/images/error-catcher-event.png)

For information about how to define and use an error catcher in your integration, see [Create the error catcher logic](https://docs.cloud.google.com/application-integration/docs/configure-error-catcher-trigger#logic).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
