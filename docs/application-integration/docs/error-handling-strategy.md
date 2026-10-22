---
url: https://docs.cloud.google.com/application-integration/docs/error-handling-strategy/
title: Error handling strategies for tasks \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:39:40.424934+00:00
---

# Error handling strategies for tasks  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/error-handling-strategy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Error handling strategies for tasks

The error handling strategy for a task specifies the action to take if the task fails due to a temporary error.

## Configure error handling strategies

To configure an error handling strategy for a task, follow these steps: 

  1. Click the existing task in your integration editor. The task configuration pane appears. 
  2. In the task configuration pane, expand the **Error handling** section. The following image shows the **Error handling** section: 

![Error handling strategy](https://docs.cloud.google.com/static/application-integration/images/error-handling-strategy.png)![Error handling strategy](https://docs.cloud.google.com/static/application-integration/images/error-handling-strategy.png)

In the **Error handling** section, follow these steps:

     1. To add a new failure policy, click **\+ Add Failure Policy**. If multiple conditional failure policies are configured, they are checked and matched in order. 
        1. In the **Retry strategy** field, select the error handling strategy that you want to use. For a list of strategies, see Retry strategies.
        2. In the **Retry condition** field, enter the condition that must match the error for this error strategy to execute. For example, for a [Call REST Endpoint task](https://docs.cloud.google.com/application-integration/docs/configure-call-rest-endpoint-task), to execute the error strategy if the error code matches `404`, enter the following: 
               
               $`ErrorInfo.code`$ = 404

For information about how to add these conditions, see Retry conditions.
     2. In the **Default error policy** section, add the default policy that must be applied if no conditional failure policy matches. The default failure policy is optional.
     3. In the **Error catcher** section, add the [error catcher](https://docs.cloud.google.com/application-integration/docs/error-catcher) for your integration.



For information about error codes and error handling, see [Error handling](https://docs.cloud.google.com/application-integration/docs/error-handling). Retry strategies The following tables describes the different error handling strategies that you can use for a task: 

Strategy type  | Description   
---|---  
**Fatal** | Stops the execution of the entire integration and marks the execution status as **Failed**.   
**Ignore** | Ignores the failure of the task. The integration continues to run the next tasks assuming the failed task has **Succeeded**.   
**None** | Stops execution of the task and marks the integration status as **Failed**. If an alternate path to the final task (leaf task) exists, tasks in the alternate path are run. If all tasks in the alternate path run successfully, marks the integration status as **Succeeded**.   
**Restart integration with backoff** | Runs the entire integration from the first task. However, the task might fail again. To avoid repeat failure, specify the time interval between restarts in the Retry interval (in seconds) field and the number of permitted restart attempts in the Maximum retry count field.   
**Retry task with exponential backoff** | Runs the integration from the failed task. If the task fails during a retry, the time interval between each retry attempt increases by the power of 2. There is a delay of 1 to 5 seconds that is added to the backoff time.  For example, if the specified retry interval is 3 seconds, the first retry occurs after 3 seconds. The second retry occurs after 9 seconds, the third retry after 81 seconds, and so on. The process continues until the maximum number of retries is reached or the task succeeds, whichever is earlier.   
**Retry task with fixed interval** | Runs the integration from the failed task. If the task fails during a retry, the time interval between each retry attempt remains constant.  For example, if the specified retry interval is 3 seconds, retries occur every 3 seconds. The process continues until the maximum number of retries is reached or the task succeeds, whichever is earlier.   
**Retry task with linear backoff** | Runs the integration from the failed task. If the task fails during a retry, the time interval between each retry attempt increases linearly. There is a delay of 1 to 5 seconds that is added to the backoff time.  For example, if the specified retry interval is 3 seconds, the first retry occurs after 3 seconds. The second retry occurs after 6 seconds, the third retry after 9 seconds, and so on. The process continues until the maximum number of retries is reached or the task succeeds, whichever is earlier.   
  
### Backoff retries

The default concurrency limit is set to 50 executions for each project and region. Failed executions are queued and retried using an exponential backoff algorithm, which gradually increases the wait time between retries up to 10 times. For example:

  1. Execute an integration.
  2. If the request fails, waits 10 minutes and retries the request.
  3. If the request fails, waits 20 minutes and retries the request.
  4. If the request fails, waits 40 minutes and retries the request.
  5. And so on, up to a maximum backoff retries of 10 times.



## Retry conditions

The retry condition specifies the condition that must match for the error handling strategy to execute. The following table describes the supported operators and functions that you can use in the retry condition: 

### Supported operators

The following table describes the supported operators available for use in retry conditions. 

**Operator** | **Description** | **Example**  
---|---|---  
**=** | Checks for equality between two values  | `$var$ = "value"`  
**!=** | Checks for inequality between two values  | `$var$ != "value"`  
**<** | Checks if a value is less than another value  | `5 < 10`  
**< =** | Checks if a value is less than or equal to another value  | `$var$ <= 5`  
**>** | Checks if a value is greater than another value  | `1 > 0`  
**> =** | Checks if a value is greater than or equal to another value  | `$var$ >= 0`  
**:** | Checks if a string contains a substring within it, or checks if a list contains a specific primitive value.  | `$longString$ : "substring"` `$list of values$ : "value"`  
**AND** | Checks two expressions and returns true if both the expressions evaluate to true.  | `$a$ > $b$ AND $b$ < $c$`  
**OR** | Checks two expressions and returns true if any one of the expressions evaluates to true.  | `$a$ > $b$ OR $b$ < $c$`  
**NOT** | Negation operator. Flips the result of an expression.  | `NOT($var$ = "value")`  
  
### Supported functions

The following table describes supported functions available for use in retry conditions. 

**Function** | **Description**  
---|---  
`exists(VARIABLE)` | Checks if a given variable exists   
`does_not_exist(VARIABLE)` | Checks if a given variable does not exist   
`is_empty(VARIABLE)` | Checks if a given variable is a list AND is empty. Supports array variable type except JSON array.   
`is_not_empty(VARIABLE)` | Checks if a given variable is a list AND is not empty. Supports array variable type except JSON array.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
