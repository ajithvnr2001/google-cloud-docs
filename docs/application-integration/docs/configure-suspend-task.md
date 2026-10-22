---
url: https://docs.cloud.google.com/application-integration/docs/configure-suspend-task/
title: Suspend task \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:38:36.950126+00:00
---

# Suspend task  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/configure-suspend-task/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Suspend task

The **Suspend** task lets you temporarily pause and then resume the execution of an integration.

During an integration execution, when the control reaches a Suspend task, execution is halted, and all tasks after the Suspend task are suspended. Integration resumes the execution when any of the following events occur:

  * Expiry of the specified suspension time.
  * After receiving a resume execution request from the `Suspensions` API.



You can also configure an output variable (**Suspension result**) for the Suspend task and set it to any value and use the value to create branching conditions for executing the downstream tasks.

**Note:** When a new version of the integration is published, any suspended executions of the previous version are automatically cancelled. 

## Compare Approval task, Suspend task, and Timer task

All the three ([Approval](https://docs.cloud.google.com/application-integration/docs/approval-task), [Suspend](https://docs.cloud.google.com/application-integration/docs/run-suspend-task), and [Timer](https://docs.cloud.google.com/application-integration/docs/run-timer-task)) tasks perform a similar function of pausing and resuming an integration. However, there are subtle differences among them. The following table describes the differences amongst the three tasks.

Approval task | Suspend task | Timer task  
---|---|---  
Doesn't support automatic resumption of an integration and requires manual intervention to resume the integration. | Supports both manual and automatic resumption of an integration. If there is no manual intervention to revoke the suspension, the integration will automatically resume execution after the expiry of the suspension time limit. | Supports only automatic resumption of an integration. The integration execution automatically resumes after the exipry of the suspension time limit.  
Can't resume an integration via an API call. You must manually resolve the suspension by using the Integrations UI. | Can resume an integration by using the `Suspensions` API for integrations. | Supports only automatic resumption of an integration.  
Users receive notification when an integration pauses (suspended). | Users don't receive any notification when an integration pauses (suspended). | Users don't receive any notification when an integration pauses (suspended).  
Supports a output variable (boolean), which allows you to perform conditional checks before resuming an integration. However, the output variable can only have the value as either `true` or `false`. | Supports a output variable (string), which allows you to perform conditional checks before resuming an integration. You can set any value to the output variable. | Doesn't support any output variables.  
  
## Configure the Suspend task

To configure the **Suspend** task, perform the following steps: 

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
  5. Click and place the **Suspend** task element in the integration editor.
  6. Click the **Suspend** task element on the designer to view the **Suspend** task configuration pane.
  7. Configure the remaining fields using the Configuration properties for the task as detailed in the tables below. 

All changes to the properties are saved automatically. 




## Configuration properties

The following table describes the configuration properties of the Suspend task. 

**Property** | **Data type** | **Description**  
---|---|---  
`**Suspension Time**` | Integer | Time (in minutes) till which the integration execution must be suspended. The maximum time limit is **44640** minutes (31 days) which is also the default value. If the integration execution doesn't resume within the specified time limit, integration automatically resumes the execution after the expiry of the time limit and sets the value of the `Suspension result` variable to `**Expired**`.   
`**Suspension result**` | String  | A variable to store the result of the Suspend task. Setting the value to this variable is optional. You can set this variable to any value based on your requirement. This variable is helpful if you want to have more control over your integration's execution flow. For example, you can read the suspension result and configure conditional decisions based on the value in any of your downstream tasks.  
`**Suspension Id**` | String | A unique identifier for the Suspend task. The value of this variable is set immediately after the integration is suspended. You can get the identifier value from the [execution logs](https://docs.cloud.google.com/application-integration/docs/viewing-logs) page in the integration UI. You can also get the get the identifier value from the response object of an API if you are using an API to trigger the integration. You can resume the integration execution either by using the suspension ID or by using the integration's execution ID.  
  
## Revoke a suspension with the Suspensions API

The Suspensions API lets you revoke a suspension via a API call. To revoke a suspension with the **Suspensions** API, you must have either the execution ID of the integration or the suspension ID of the Suspend task. To revoke a suspension, you must issue a `POST` request to the following API:
    
    
    https://REGION-integrations.googleapis.com/v1/{name=projects/PROJECT/locations/LOCATION/integrations/INTEGRATION_ID/executions/EXECUTION_ID/suspensions/SUSPENSION_ID}:lift
        

In this API, the `INTEGRATION_ID` is optional. However, you must provide either the `EXECUTION_ID` or the `SUSPENSION_ID`. If you don't have any of the ID values, you can substitute the value with `-`. In this API, `REGION`, `PROJECT`, and `LOCATION` are required fields.

**Note:**

  * If you don't specify both the execution ID and the suspension ID, the API doesn't run and reports an error.
  * If you don't specify the `suspension_result`, value of the suspension result is set to `Resolved`.



After you revoke the suspension, integration execution resumes and executes the downstream tasks after the Suspend task.

The following examples show how to revoke a suspension by using the **suspensions** API.

### Example 1: Revoke a suspension with only the suspension ID

The following `curl` command shows you how to revoke a suspension when you only have the suspension ID:
    
    
      curl -H "Authorization: Bearer $TOKEN" \
      -H "Content-type: application/json" \
      -H X-GFE-SSL: yes \
      -X POST \
      -d '{"suspension_result":"Approved"}' \
      https://us-east1-integrations.googleapis.com/v1/projects/demo-project/locations/us-east1/integrations/-/executions/-/suspensions/c6a13a79-a918-41e2-82b9-32b5a010755a:lift
    

In this example, the `Suspension result` variable is set to `Approved` for the supension ID `c6a13a79-a918-41e2-82b9-32b5a010755a`.

### Example 2: Revoke a suspension with only the execution ID

The following `curl` command shows you how to revoke a suspension when you only have the execution ID:
    
    
      curl -H "Authorization: Bearer $TOKEN" \
      -H "Content-type: application/json" \
      -H X-GFE-SSL: yes \
      -X POST \
      -d '{"suspension_result":"true"}' \
      https://us-east1-integrations.googleapis.com/v1/projects/demo-project/locations/us-east1/integrations/-/executions/76a391e7-c801-45d7-8046-eab20d167ec5/suspensions/-:lift
    

In this example, the `Suspension result` variable is set to `true` for the execution ID `76a391e7-c801-45d7-8046-eab20d167ec5`.

### Example 3: Revoke a suspension with both the execution ID and the suspension ID

The following `curl` command shows you how to revoke a suspension when you have both the execution ID and the suspension ID:
    
    
      curl -H "Authorization: Bearer $TOKEN" \
      -H "Content-type: application/json" \
      -H X-GFE-SSL: yes \
      -X POST \
      -d '{"suspension_result":"{processname: "Release", owner: "John", status: "approved"};"}' \
      https://us-east1-integrations.googleapis.com/v1/projects/demo-project/locations/us-east1/integrations/-/executions/9b721baa-0a23-4576-b2b6-d251d163ea6f/suspensions/f01815bf-ed18-4e01-9d41-cc2ce7861e95:lift
    

In this example, the `Suspension result` variable is set to `{processname: "Release", owner: "John", status: "approved"};` for the suspension ID `f01815bf-ed18-4e01-9d41-cc2ce7861e95`.

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
