---
url: https://docs.cloud.google.com/application-integration/docs/configure-timer-task/
title: Timer task \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:39:15.406535+00:00
---

# Timer task  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/configure-timer-task/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Timer task

The **Timer** task lets you add a time delay to the integration execution flow.

During an integration execution, when the control reaches the Timer task, execution is paused for the specified time limit, and all tasks after the Timer task are suspended. This task supports only automatic resumption of an integration. The integration execution automatically resumes after the expiry of the suspension time limit. For example, if you set the timer task to 180 seconds, the execution is paused for 3 minutes before resuming automatically.

**Note:** If you set the timer task to less than 60 seconds, the suspend state will be consistent as synchronous execution mode. Otherwise, the suspend state is consistent with the asynchronous execution mode.

## Compare Approval task, Suspend task, and Timer task

All the three ([Approval](https://docs.cloud.google.com/application-integration/docs/approval-task), [Suspend](https://docs.cloud.google.com/application-integration/docs/run-suspend-task), and [Timer](https://docs.cloud.google.com/application-integration/docs/run-timer-task)) tasks perform a similar function of pausing and resuming an integration. However, there are subtle differences among them. The following table describes the differences amongst the three tasks.

Approval task | Suspend task | Timer task  
---|---|---  
Doesn't support automatic resumption of an integration and requires manual intervention to resume the integration. | Supports both manual and automatic resumption of an integration. If there is no manual intervention to revoke the suspension, the integration will automatically resume execution after the expiry of the suspension time limit. | Supports only automatic resumption of an integration. The integration execution automatically resumes after the exipry of the suspension time limit.  
Can't resume an integration via an API call. You must manually resolve the suspension by using the Integrations UI. | Can resume an integration by using the `Suspensions` API for integrations. | Supports only automatic resumption of an integration.  
Users receive notification when an integration pauses (suspended). | Users don't receive any notification when an integration pauses (suspended). | Users don't receive any notification when an integration pauses (suspended).  
Supports a output variable (boolean), which allows you to perform conditional checks before resuming an integration. However, the output variable can only have the value as either `true` or `false`. | Supports a output variable (string), which allows you to perform conditional checks before resuming an integration. You can set any value to the output variable. | Doesn't support any output variables.  
  
## Configure the Timer task

To configure the **Timer** task: 

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. In the navigation menu, click **Integrations**. 

The **Integrations** page appears listing all the integrations available in the Google Cloud project. 

  3. Select an existing integration or click **Create integration** to create a new one. 

If you are creating a new integration: 

     1. Enter a name and description in the **Create Integration** pane.
     2. Select a region for the integration. **Note:** The **Regions** dropdown only lists the regions provisioned in your Google Cloud project. To provision a new region, click **Enable Region**. See [Enable new region](https://docs.cloud.google.com/application-integration/docs/enable-new-region) for more information. 
     3. Select a service account for the integration. You can change or update the service account details of an integration any time from the info **Integration summary** pane in the integration toolbar. **Note:** The option to select a service account is displayed only if you have enabled integration governance for the selected region. 
     4. Click **Create**. The newly created integration opens in the _integration editor_. 

  4. In the _integration editor_ navigation bar, click **Tasks** to view the list of available tasks and connectors. 
  5. Click and place the **Timer** task element in the integration editor.
  6. Click the **Timer** task element on the designer to view the **Timer** task configuration pane.
  7. Configure the remaining fields using the Configuration properties for the task. For example, if you set **Timeout after** to `180` and **Time unit** to `Seconds`, the execution is paused for 3 minutes before resuming automatically.
  8. Changes to the properties are saved automatically. 



## Configuration properties

The following table describes the configuration properties of the Timer task. 

**Property** | **Data type** | **Description**  
---|---|---  
`**Timeout after**` | Integer |  Time till which the integration execution must be paused. Integration automatically resumes the execution of the next downstream task after the expiry of the time limit. **Default value:** 120 seconds (2 minutes). **Maximum time limit allowed:** 44640 minutes (31 days).  
`**Time unit**` | Seconds, Minutes, Hours, Days  | Time unit for the **Timeout after** property.   
  
## Error handling strategy

An error handling strategy for a task specifies the action to take if the task fails due to a [temporary error](https://docs.cloud.google.com/application-integration/docs/error-handling). For information about how to use an error handling strategy, and to know about the different types of error handling strategies, see [Error handling strategies](https://docs.cloud.google.com/application-integration/docs/error-handling-strategy). 

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
