---
url: https://docs.cloud.google.com/application-integration/docs/configure-while-loop-task/
title: While Loop task \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:39:01.475659+00:00
---

# While Loop task  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/configure-while-loop-task/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# While Loop task

The **While Loop** task lets you make repeated calls to a sub-integration from your current (main) integration until a specified condition is met.

The **API Trigger ID** and the **Integration name** identifies the sub-integration you want to run.

The task also lets you collect the response from each sub-integration run and store the value in your current integration for use in downstream tasks. You can use any of the following approach to collect the responses:

  * Collate the response of each run in an array variable, where each element of the array has the response from one particular run. To collate the responses, configure the `Collect values from sub-integration output(s)` property. 
  * Aggregate the responses of all the runs in a single variable. To aggregate the responses, configure the `Override values from sub-integration output(s)` property.

**Note** : 

  * The **While Loop** task can run a maximum of 8000 iterations. This constraint holds good even if the configured condition results in an infinte loop.
  * The cumulative size of the data collected from each sub-integration run cannot exceed `50 MB`. If the size exceeds `50 MB`, the integration fails, and the downstream tasks are not run.



## Before you begin

  * Ensure that you have [attached a user-managed service account](https://docs.cloud.google.com/application-integration/docs/access-control#add-service-account) to your integration. If your integration does not have user-managed service account configured, then by default the [default service account](https://docs.cloud.google.com/application-integration/docs/access-control#default-service-account) (`service-PROJECT_NUMBER@gcp-sa-integrations.iam.gserviceaccount.com`) is used for authentication.
  * Ensure that your service account has the **Application Integration Invoker** IAM role. For information about granting roles to a service account, see [Manage access to service accounts](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts).



## Configuration properties

The following table describes the configuration properties of the **While Loop** task. 

**Property** | **Data type** | **Description**  
---|---|---  
`API Trigger ID` | String  | Trigger ID of the sub-integration to run.  This value is available in the **Trigger ID** field of the **API Trigger** in the sub-integration.   
`Integration name` | String  | Name of the sub-integration to run.  
`While loop condition` | N/A | Condition to terminate the loop. The sub-integration runs till the condition is met. For example, `$loopMetadata.current_iteration_count$< 10`.  
`Map to sub-integration input(s)` | N/A  | Values to pass from the current integration to the sub-integration.  The values of this property are in the form of key-value pairs, where the key is a variable in the current integration, and the value is the corresponding input variable in the sub-integration. For example, suppose your main integration has the `productID` variable, which you want to map to the `subIntProductID` sub-integration variable; you would select `productID` from the **Integration variable to map from** drop-down and enter `subIntProductID` in the **Sub-Integration input to map to** field.   
`Collect values from sub-integration output(s)` | N/A  | Collate the results of the sub-integration runs.  Every time the sub-integration runs, you can store the output of the sub-integration in an array variable of the current integration. Enter the sub-integration's output variable in the **Sub-Integration output to collect from** field and select the array variable in current integration from the **Integration variable to collect into** drop-down. Each element of the array has the response from a particular sub-integration run. For example, if the array variable is `resultsArray`, `resultsArray[0]` has the response from the first run and `resultsArray[1]` has the response from the second run.   
`Override values from sub-integration output(s)` | N/A  | Read the output variable of a sub-integration run and store it in a variable of the current integration.  Select the sub-integration's output variable from the **Sub-integration output to map from** drop-down, and select the corresponding variable in the current integration from the **Integration variable to override** drop-down. You can send the overridden variable in the current integration to the next sub-integration run by mapping the variable in the **Map to additional sub-integration input(s)** property. As a result, you can cumulatively aggregate the responses from the sub-integration runs.  
`Loop metadata` | JSON array  | The output variable that has the execution details of the sub-integration runs like the sub-integration execution ID, errors messages, and variable values passed during execution. Loop metadata contains variables including the following output variables: `current_iteration_count`, `sub_integration_execution_ids`, `failure_location`, `current_element`, `iteration_element`, and `failure_message`. **Warning:** In the Loop metadata, you will find duplicate keys for the output variable–for example, `Current Iteration Count` and `current_iteration_count`. We recommend you to use the variables that contain the underscore (`_`) symbol because the other keys are being deprecated.  
  
## Best practices

For information about the usage limits that apply to the **While Loop** task, see [ Usage limits](https://docs.cloud.google.com/application-integration/docs/quotas#usage-limits). 

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
