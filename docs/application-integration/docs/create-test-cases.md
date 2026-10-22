---
url: https://docs.cloud.google.com/application-integration/docs/create-test-cases/
title: Create test cases \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:39:00.291267+00:00
---

# Create test cases  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/create-test-cases/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create test cases

**Preview — Test cases**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how to create test cases for your integrations. For information about test cases, supported test configurations, and its limitations, see [Introduction to test cases](https://docs.cloud.google.com/application-integration/docs/test-cases).

## Before you begin

  * To get the permission that you need to create test cases, ask your administrator to grant you the [Application Integration Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `integrations.googleapis.com/testCases.create` permission, which is required to create test cases. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  * Ensure that your integration is in the `DRAFT` state. If your integration is in the `PUBLISHED` state, click **Enable Editing**. A new version in the `DRAFT` state is created in the integration for you. The following figure shows the edit lock in the integration editor. 

![Integrations edit lock](https://docs.cloud.google.com/static/application-integration/images/integration-edit-lock.png)![Integrations edit lock](https://docs.cloud.google.com/static/application-integration/images/integration-edit-lock.png)




## Create a test case

To create a test case, select one of the following options: 

### Console

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. In the navigation menu, click **Integrations**. 

The **Integrations** page appears listing all the integrations available in the Google Cloud project.

  3. Select an existing integration for which you want to create a test. 

This opens the integration in the _integration editor_.

  4. Click **Test Case** and then click **\+ Create a new test case**. The **Create test case** pane appears: 

![image showing the Create  test case pane](https://docs.cloud.google.com/static/application-integration/images/create-test-case.png)![iimage showing the Create test case pane](https://docs.cloud.google.com/static/application-integration/images/create-test-case.png)

Then, do the following:

     1. From the **Trigger** list, select a trigger.
     2. In the **Test name** field, enter a name for your test.
     3. Optionally, in the **Description** field, enter a description for your test.
     4. Click **Create**. 

In the Integration editor page, the designer canvas displays **Test case mode is active**.

  5. Configure the test configuration for your trigger and tasks.



### API

Call the [`projects.locations.integrations.versions.testCases.create` method](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.integrations.versions.testCases/create) and provide any relevant parameters. For example:
    
    
    POST https://integrations.googleapis.com/v1/{parent=projects/PROJECT_ID/locations/LOCATION/integrations/INTEGRATION_NAME/versions/INTEGRATION_VERSION}/testCases
    

Replace the following:

  * `PROJECT_ID`: the ID of the Google Cloud project
  * `LOCATION`: the region where the integration is located
  * `INTEGRATION_NAME`: the name of the integration
  * `INTEGRATION_VERSION`: the version of the integration



The request body contains the `[TestCase](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.integrations.versions.testCases#TestCase)` resource. For example:
    
    
     
    {
        "displayName": "example-test-case",
        "triggerId": "api_trigger/example-trigger",
        "testTaskConfigs": [{
          "taskNumber": "1",
          "mockConfig": {
            "mockStrategy": "NO_MOCK_STRATEGY"
          },
          "task": "FieldMappingTask"
        }],
    }
    

**Note:** You cannot edit your integration when the Test Case mode is enabled.

## Configure test configurations

After creating a test case, you can [configure test configurations](https://docs.cloud.google.com/application-integration/docs/configure-test-cases) for your triggers and tasks.

## What's next

  * Learn about [test cases](https://docs.cloud.google.com/application-integration/docs/test-cases).
  * Learn how to do the following:

    * [Configure test cases](https://docs.cloud.google.com/application-integration/docs/configure-test-cases).
    * [Copy](https://docs.cloud.google.com/application-integration/docs/manage-test-cases#copy) and [delete](https://docs.cloud.google.com/application-integration/docs/manage-test-cases#delete) test cases.
    * [Run a test case](https://docs.cloud.google.com/application-integration/docs/run-test-cases) and [view test case execution logs](https://docs.cloud.google.com/application-integration/docs/integration-execution-logs#view-integration-execution-logs).
    * [Upload and download test cases](https://docs.cloud.google.com/application-integration/docs/upload-download-test-cases).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
