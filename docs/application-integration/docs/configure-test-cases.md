---
url: https://docs.cloud.google.com/application-integration/docs/configure-test-cases/
title: Configure test cases \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:38:47.737298+00:00
---

# Configure test cases  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/configure-test-cases/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure test cases

**Preview — Test cases**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how to configure test cases for your integrations. For information about test cases, supported test configurations, and its limitations, see [Introduction to test cases](https://docs.cloud.google.com/application-integration/docs/test-cases).

## Before you begin

  * To get the permission that you need to configure test cases, ask your administrator to grant you the [Application Integration Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `integrations.googleapis.com/testCases.create` permission, which is required to configure test cases. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  * Ensure that your integration is in the `DRAFT` state. If your integration is in the `PUBLISHED` state, click **Enable Editing**. A new version in the `DRAFT` state is created in the integration for you. The following figure shows the edit lock in the integration editor. 

![Integrations edit lock](https://docs.cloud.google.com/static/application-integration/images/integration-edit-lock.png)![Integrations edit lock](https://docs.cloud.google.com/static/application-integration/images/integration-edit-lock.png)

  * Ensure that you have a test case in the integration. For information about how to create a test case, see [Create Test Cases](https://docs.cloud.google.com/application-integration/docs/create-test-cases).



## Configure test configurations for triggers

To configure the test configurations for the trigger, select one of the following options: 

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. In the navigation menu, click **Integrations**. 

The **Integrations** page appears listing all the integrations available in the Google Cloud project.

  3. Select an existing integration for which you want to create a test. 

This opens the integration in the _integration editor_.

  4. Click **Test Case** and then click **Open test cases**. The **Test Cases** pane appears with a list of test cases for the current integration version.
  5. Select the test case from the list. 

In the Integration editor page, the designer canvas displays **Test case mode is active**. The following image shows the **Test configuration** pane for the trigger:

![image showing the test configuration pane](https://docs.cloud.google.com/static/application-integration/images/configure-trigger-properties.png)![iimage showing the test configuration pane](https://docs.cloud.google.com/static/application-integration/images/configure-trigger-properties.png)

  6. In the Integration editor page, click the trigger to open the trigger configuration pane. Then, do the following: 
     * If you have input variables for your integration, then the **Test configuration** tab shows those input variables. The values that you enter in the variables are saved automatically.
     * To view the trigger properties, click the **Trigger properties** tab.



## Configure test configurations for tasks

To configure the test properties for the integrations task, select one of the following options: 

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. In the navigation menu, click **Integrations**. 

The **Integrations** page appears listing all the integrations available in the Google Cloud project.

  3. Select an existing integration for which you want to create a test. 

This opens the integration in the _integration editor_.

  4. Click **Test Case** and then click **Open test cases**. The **Test Cases** pane appears with a list of test cases for the current integration version.
  5. Select the test case from the list. 

In the Integration editor page, the designer canvas displays **Test case mode is active**.

  6. In the Integration editor page, click the task to open the test configuration pane. The following image shows the **Test configuration** pane for the task: 

![image showing the test configuration pane](https://docs.cloud.google.com/static/application-integration/images/configure-test-config-task.png)![iimage showing the test configuration pane](https://docs.cloud.google.com/static/application-integration/images/configure-test-config-task.png)

In the **Test configuration** tab, follow these steps: 
     1. From the **Mock strategy type** , select one of the following mock strategies: 
        * If you select **No mock** , then your task executes from the main integration as it should in the actual integration. By default, **No mock** strategy type is selected for tasks.
        * If you select **Mock execution** , then for **Mock execution status** , you must select one of the following: 
          * **Skip:** Task is marked as successfully completed
          * **Failure:** Task is marked as failed
        * If you select **Mock Output** , then for **Task Output list** , you must provide the output of the tasks for the next node in the integration.
  7. In the **Assertion strategy** section, do the following: 
     1. From the **Assertion type** field, select one of the following options: 
        * If you select **Assert execution** , then select one of the following options for **Execution status to assert** : 
          * **Success**
          * **Failure**
          * **Not executed**
        * If you select **Assert parameters** , then do the following: 
          1. From the **Parameters to assert** select if you want to assert parameters including input and output parameters.
          2. Select the **Operator** for comparing the asserted parameter with the entered value. The operations to compare the asserted parameter can be one of the following: 
             * Equals
             * Not equals
             * Contains
          3. In the **Value** field, enter the value to which you want to compare the parameter.
     2. Optional: To add more assertions, click **\+ Add Assertion**.



## What's next

  * Learn about [test cases](https://docs.cloud.google.com/application-integration/docs/test-cases).
  * Learn how to do the following:

    * [Create test cases](https://docs.cloud.google.com/application-integration/docs/create-test-cases).
    * [Copy](https://docs.cloud.google.com/application-integration/docs/manage-test-cases#copy) and [delete](https://docs.cloud.google.com/application-integration/docs/manage-test-cases#delete) test cases.
    * [Run a test case](https://docs.cloud.google.com/application-integration/docs/run-test-cases) and [view test case execution logs](https://docs.cloud.google.com/application-integration/docs/integration-execution-logs#view-integration-execution-logs).
    * [Upload and download test cases](https://docs.cloud.google.com/application-integration/docs/upload-download-test-cases).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
