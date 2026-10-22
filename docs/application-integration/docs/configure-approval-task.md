---
url: https://docs.cloud.google.com/application-integration/docs/configure-approval-task/
title: Approval Task \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:47.041962+00:00
---

# Approval Task  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/configure-approval-task/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Approval Task

The **Approval** task lets you configure approval-based integrations. It also lets you control the flow of an integration. 

You can use the **Approval** task to send approval request emails to one or more integration users. The email includes a link to the integration where the users can manually approve or reject the request. 

During an integration execution, when the control reaches the **Approval** task, execution is halted, and all tasks after the **Approval** task are suspended. The integration resumes the execution only when a user manually approves or rejects the approval request. 

An **Approval** task can be used for the following purposes:

  * To suspend and branch an integration based on user approval or rejection.
  * To suspend an integration until a specified duration. 
  * To use as a breakpoint to debug the integration.



## Compare Approval task, Suspend task, and Timer task

All the three ([Approval](https://docs.cloud.google.com/application-integration/docs/approval-task), [Suspend](https://docs.cloud.google.com/application-integration/docs/run-suspend-task), and [Timer](https://docs.cloud.google.com/application-integration/docs/run-timer-task)) tasks perform a similar function of pausing and resuming an integration. However, there are subtle differences among them. The following table describes the differences amongst the three tasks.

Approval task | Suspend task | Timer task  
---|---|---  
Doesn't support automatic resumption of an integration and requires manual intervention to resume the integration. | Supports both manual and automatic resumption of an integration. If there is no manual intervention to revoke the suspension, the integration will automatically resume execution after the expiry of the suspension time limit. | Supports only automatic resumption of an integration. The integration execution automatically resumes after the exipry of the suspension time limit.  
Can't resume an integration via an API call. You must manually resolve the suspension by using the Integrations UI. | Can resume an integration by using the `Suspensions` API for integrations. | Supports only automatic resumption of an integration.  
Users receive notification when an integration pauses (suspended). | Users don't receive any notification when an integration pauses (suspended). | Users don't receive any notification when an integration pauses (suspended).  
Supports a output variable (boolean), which allows you to perform conditional checks before resuming an integration. However, the output variable can only have the value as either `true` or `false`. | Supports a output variable (string), which allows you to perform conditional checks before resuming an integration. You can set any value to the output variable. | Doesn't support any output variables.  
  
## Configure the Approval task

To configure the **Approval** task: 

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
  5. Click and place the **Approval** task element in the integration editor.
  6. Click the **Approval** task element on the designer to view the Approval task configuration pane.
  7. Configure the displayed fields using the Configuration properties for the task as detailed in the table below. 

All changes to the properties are saved automatically. 




## Configuration properties

The following table describes the configuration properties of the **Approval** task. 

**Property** | **Data type** | **Description**  
---|---|---  
`**Recipients**` | String Array  | Email addresses to which notification is sent when the task is suspended. Enter multiple email addresses separated by a comma. **Note:** In your Google Cloud project, you must grant the **Application Integration Approver** IAM role to all the email addresses provided in the **Recipients** field. For information on granting IAM roles, see [Granting, changing, and revoking access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).   
`**Custom notification message**` | String  | Custom message to include in the email notification when the task is suspended. The value can be a literal or a variable. If the custom message is available in a variable, click `VAR` and select the variable.   
`**Reminder frequency (in hours)**` | Integer  | Frequency of reminder notifications.  If the suspension is in an unresolved state, you can send reminder email notifications requesting authorized users to resolve the suspension.   
`**Time until expiration (in hours)**` | Integer  | Time period of the suspension.  If the suspension is not resolved within the time limit, the suspension is rejected by default.   
`**On expiration**` | Boolean  | Action to be taken after the suspension has expired.  You can choose either to reject the suspension or lift the suspension. By default the suspension is rejected.   
`**isApproved (Approval)**` | Boolean  | Output variable which has the status of the suspension after resolution.  The `isApproved` variable is set to `True` if the suspension is approved and set to `False` if the suspension is rejected. **Tip:** Use the `isApproved` variable when specifying edge conditions for subsequent tasks to control the flow of the integration. For more information about edge conditions, see [Edges conditions](https://docs.cloud.google.com/application-integration/docs/edge-overview#edge_condition).  Following is a sample edge condition configured using the `isApproved` variable: 
    
    
    $TASK_ID_isApproved$ = TRUE
      
  
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

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
