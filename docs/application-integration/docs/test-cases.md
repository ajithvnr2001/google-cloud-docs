---
url: https://docs.cloud.google.com/application-integration/docs/test-cases/
title: Introduction to test cases \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:39:06.097575+00:00
---

# Introduction to test cases  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/test-cases/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Introduction to test cases

**Preview — Test cases**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

With Application Integration, you can create and run multiple test cases on your complex integrations that connect and manage Google Cloud services and other business applications. By testing your integration flow, you can ensure that your integration is working as intended. You can test your integration using different input variables to identify the faults in the integration flow. For information about how to create test cases, see [Create test cases](https://docs.cloud.google.com/application-integration/docs/create-test-cases). 

## Test configurations

Application Integration enables you to add multiple test cases for your integration. For triggers, you can configure the input values in a test case. For tasks, you can update the following test configurations: 

  * **Mock strategy type:** There are three options that you can set for your task: 
    * **No mock:** This strategy lets you execute the task. 
    * **Mock execution:** This strategy lets you mock your task as successfully executed or failed.
    * **Mock output:** This strategy lets you mock the output of the task.
  * **Assertion type:** You can add multiple assertions for a selected task in a test. There are various assertion types available: 
    * **Assert execution:** This assertion type lets you check if the task is executed successfully, with failure, or if the task didn't get executed. 
    * **Assert parameters:** This assertion type lets you select the parameter that you want to assert and provide a value to compare it with. 
    * **Assert condition:** This assertion type lets you add conditions for the execution of the task. For more information, see Assertion conditions. 



## Assert conditions

In test configuration for tasks, you can choose to add conditions that must be met for the execution of the task. The task is run only if the specified conditions are met.

### Supported operators

The following table describes the supported operators available for use in asserted conditions. 

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

The following table describes the supported functions available for use in asserted conditions. 

**Function** | **Description**  
---|---  
`exists(VARIABLE)` | Checks if a given variable exists   
`does_not_exist(VARIABLE)` | Checks if a given variable does not exist   
`is_empty(VARIABLE)` | Checks if a given variable is a list AND is empty. Supports array variable type except JSON array.   
`is_not_empty(VARIABLE)` | Checks if a given variable is a list AND is not empty. Supports array variable type except JSON array.   
  
### Best practices

The following section lists the best practices when specifying conditions: 

  * To reference a variable value, use dollar sign notation (`$`) before and after the variable name. For example, if you want to check if a variable `productId` is greater than 10, the syntax is `$productId$ > 10`. 
  * Text without dollar sign notation is interpreted as a literal value. For example the text `customerId` is interpreted as a literal value. 
  * To check multiple conditions, split the conditions into individual checks and combine them using **AND** or **OR**. For example, instead of using `$productId$ > 5 AND < 9 `, use ` $productId$ > 5 AND $productId$ < 9`.



## Pricing

There is no additional cost for managing fuctional tests. For more information about pricing, see [Application Integration pricing](https://docs.cloud.google.com/application-integration/pricing).

## Limitations

Test cases are subject to the following limitations:

  * When you download integrations, the test cases are not downloaded along with the integration. For information about how to download test cases, see [Download test cases](https://docs.cloud.google.com/application-integration/docs/upload-download-test-cases).
  * You cannot add assertions for output variables for the integration. As a workaround, you can add assertions on the last task executed for output variables.
  * You cannot create test cases for published integrations. To create test cases, click **Enable Editing**. A new version in the `DRAFT` state is created in the integration for you. The following figure shows the edit lock in the integration editor. 

![Integrations edit lock](https://docs.cloud.google.com/static/application-integration/images/integration-edit-lock.png)![Integrations edit lock](https://docs.cloud.google.com/static/application-integration/images/integration-edit-lock.png)




## What's next

Learn how to do the following:

  * [Create test cases](https://docs.cloud.google.com/application-integration/docs/create-test-cases).
  * [Copy](https://docs.cloud.google.com/application-integration/docs/manage-test-cases#copy) and [delete](https://docs.cloud.google.com/application-integration/docs/manage-test-cases#delete) test cases.
  * [Run a test case](https://docs.cloud.google.com/application-integration/docs/run-test-cases) and [view test case execution logs](https://docs.cloud.google.com/application-integration/docs/integration-execution-logs#view-integration-execution-logs).
  * [Configure test cases](https://docs.cloud.google.com/application-integration/docs/configure-test-cases).
  * [Upload and download test cases](https://docs.cloud.google.com/application-integration/docs/upload-download-test-cases).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
