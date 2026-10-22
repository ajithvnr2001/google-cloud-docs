---
url: https://docs.cloud.google.com/application-integration/docs/edge-and-edge-conditions/
title: Edge and edge conditions \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:59.521230+00:00
---

# Edge and edge conditions  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/edge-and-edge-conditions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Edge and edge conditions

## Edge

An edge is a connection between any two elements in an integration. The connection denotes the direction of the control flow from one element(task or trigger) to another. The connection can be between a [trigger](https://docs.cloud.google.com/application-integration/docs/trigger-overview) and a [task](https://docs.cloud.google.com/application-integration/docs/task-overview) or between a task and another task. By using an edge along with fork and join, you can implement complex branching and conditions in your integration. For more information, see [Forks and joins](https://docs.cloud.google.com/application-integration/docs/forks-joins). 

For example, if there is an edge from a **Send Email** task to a **Call Integration** task, it means that after the **Send Email** task is run, the next task to run is the **Call Integration** task. An edge also supports conditional checks. Before the control passes to the next task, you can check for a condition in the edge and based on the result, decide to run the task or not. For more information about the supported conditional checks, see Edge conditions. 

![image showing highlighted edge](https://docs.cloud.google.com/static/application-integration/images/integrations_edge.png)![image showing highlighted edge](https://docs.cloud.google.com/static/application-integration/images/integrations_edge.png)

##  Edge conditions 

Edge conditions let you specify the conditions that must be met for control of an integration to pass to the task connected by the edge. The task is run _only if_ the specified conditions are met. Edge conditions are useful in cases where there are multiple incoming edges to a task, where each edge checks for specific conditions before the task.

Specify edge conditions using the following steps: 

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
  5. Select an existing integration or create a new one. 
  6. In the integration editor, click on the edge to open the Edge configuration pane. 
  7. Configure the edge: 
     * **Label** (optional): Add a custom name for the edge.
     * **Condition** : Set an edge condition using the supported operators and functions. 

Important tips for specifying conditions: 

  * To reference a variable value, use dollar sign notation (`$`) before and after the variable name. For example, if you want to check if a variable `productId` is greater than 10, the syntax is `$productId$ > 10`. 
  * Text without dollar sign notation is interpreted as a literal value. For example the text `customerId` is interpreted as a literal value. 
  * To check multiple conditions, split the conditions into individual checks and combine them using **AND** or **OR**. For example, instead of using `$productId$ > 5 AND < 9 `, use ` $productId$ > 5 AND $productId$ < 9`.

![image showing highlighted edge condition](https://docs.cloud.google.com/static/application-integration/images/integrations_edge_condition.png)![image showing highlighted edge condition](https://docs.cloud.google.com/static/application-integration/images/integrations_edge_condition.png)

## Supported operators

The following table describes the supported operators available for use in edge conditions. 

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
  
## Supported functions

The following table describes supported functions available for use in edge conditions. 

**Function** | **Description**  
---|---  
`exists(VARIABLE)` | Checks if a given variable exists   
`does_not_exist(VARIABLE)` | Checks if a given variable does not exist   
`is_empty(VARIABLE)` | Checks if a given variable is a list AND is empty. Supports array variable type except JSON array.   
`is_not_empty(VARIABLE)` | Checks if a given variable is a list AND is not empty. Supports array variable type except JSON array.   
  
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
