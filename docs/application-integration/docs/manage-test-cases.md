---
url: https://docs.cloud.google.com/application-integration/docs/manage-test-cases/
title: Manage test cases \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:35:48.993123+00:00
---

# Manage test cases  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/manage-test-cases/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage test cases

**Preview — Test cases**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how to manage test cases for your integrations. You can manage your test cases in the following ways: 

  * List test cases
  * Edit a test case
  * Copy a test case
  * Delete a test case

For information about test cases, supported test configurations, and its limitations, see [Introduction to test cases](https://docs.cloud.google.com/application-integration/docs/test-cases). 

## Before you begin

  * To get the permissions that you need to manage test cases, ask your administrator to grant you the [Application Integration Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to manage test cases. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to manage test cases:

    * List test cases: `integrations.googleapis.com/testCases.get`
    * Copy a test case: 
      * `integrations.googleapis.com/testCases.get`
      * `integrations.googleapis.com/testCases.create`
    * Delete a test case: `integrations.googleapis.com/testCases.delete`

You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  * Ensure that your integration is in the `DRAFT` state. If your integration is in the `PUBLISHED` state, click **Enable Editing**. A new version in the `DRAFT` state is created in the integration for you. The following figure shows the edit lock in the integration editor. 

![Integrations edit lock](https://docs.cloud.google.com/static/application-integration/images/integration-edit-lock.png)![Integrations edit lock](https://docs.cloud.google.com/static/application-integration/images/integration-edit-lock.png)

  * Ensure that you have a test case in the integration. For information about how to create a test case, see [Create Test Cases](https://docs.cloud.google.com/application-integration/docs/create-test-cases).



## Test Case edit locks

In Application Integration, test cases are design-time entities that are often developed in collaboration with multiple authors. Although a test case can only be actively edited by one author at a time, teams can collaborate on a test case. 

If you open the test case that is being edited by another user, the following message appears in the integration editor because only one user can update the test case at a given time: 
    
    
    test-user@gmail.com is currently editing the test case. Edit features are temporarily disabled.

**Note:** The test case is locked for editing by others for 15 minutes from the last update. Locks are released after 15 minutes from the last update.

To edit the test case, click **Take Over**. The following figure shows the edit lock.

![Test case edit lock](https://docs.cloud.google.com/static/application-integration/images/test-case-take-over-edit-lock.png)![Test case edit lock](https://docs.cloud.google.com/static/application-integration/images/test-case-take-over-edit-lock.png)

## List test cases

To list test cases, select one of the following options:

### Console

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. In the navigation menu, click **Integrations**. 

The **Integrations** page appears listing all the integrations available in the Google Cloud project.

  3. Select an existing integration that contains test cases. 

This opens the integration in the _integration editor_.

  4. Click **Test Case** and then click **Open test cases**. The **Test Cases** pane appears with a list of test cases for the current integration version.



### API

Call the [`projects.locations.integrations.versions.testCases.list` method](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.integrations.versions.testCases/list) and provide any relevant parameters. For example:
    
    
    GET https://integrations.googleapis.com/v1/{parent=projects/PROJECT_ID/locations/LOCATION/integrations/INTEGRATION_NAME/versions/INTEGRATION_VERSION}/testCases
          

Replace the following:

  * `PROJECT_ID`: the ID of the Google Cloud project
  * `LOCATION`: the region where the integration is located
  * `INTEGRATION_NAME`: the name of the integration
  * `INTEGRATION_VERSION`: the version of the integration



## Edit a test case

To edit a test case, follow these steps:

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. In the navigation menu, click **Integrations**. 

The **Integrations** page appears listing all the integrations available in the Google Cloud project.

  3. Select an existing integration that contains test cases. 

This opens the integration in the _integration editor_.

  4. Click **Test Case** and then click **Open test cases**. The **Test Cases** pane appears with a list of test cases for the current integration version.
  5. Select the test case that you want to edit. 

In the Integration editor page, the designer canvas displays **Test case mode is active**. 

If a task in the integration is deleted, the test case becomes invalid as shown in the following image: 

![Integrations edit lock](https://docs.cloud.google.com/static/application-integration/images/test-case-edit.png)![Integrations edit lock](https://docs.cloud.google.com/static/application-integration/images/test-case-edit.png)

  6. If a task in the integration is deleted, click **delete Delete ** to update the test case.
  7. Update the [configuration details of the test case](https://docs.cloud.google.com/application-integration/docs/configure-test-cases) and [run the test case](https://docs.cloud.google.com/application-integration/docs/run-test-cases).



## Copy a test case

To create a copy a test case in the same integration, select one of the following options:

### Console

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. In the navigation menu, click **Integrations**. 

The **Integrations** page appears listing all the integrations available in the Google Cloud project.

  3. Select an existing integration that contains test cases. 

This opens the integration in the _integration editor_.

  4. Click **Test Case** and then click **Open test cases**. The **Test Cases** pane appears with a list of test cases for the current integration version.
  5. Select the test case that you want to copy. 

In the Integration editor page, the designer canvas displays **Test case mode is active**.

  6. Click **content_copy Duplicate**. The **Duplicate the test case** page appears. Then, do the following: 
     1. In the **Test name** field, enter the name of the test case.
     2. Optionally, in the **Description** field, enter a description of the test case.
     3. Click **Create**. The test case is created in the same integration.



### API

Follow these steps:

  * Call the [`projects.locations.integrations.versions.testCases.get` method](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.integrations.versions.testCases/get) and provide any relevant parameters. For example: 
        
        GET https://integrations.googleapis.com/v1/{parent=projects/PROJECT_ID/locations/LOCATION/integrations/INTEGRATION_NAME/versions/INTEGRATION_VERSION}/testCases/TEST_CASE_ID
        

Replace the following:

    * `PROJECT_ID`: the ID of the Google Cloud project
    * `LOCATION`: the region where the integration is located
    * `INTEGRATION_NAME`: the name of the integration
    * `INTEGRATION_VERSION`: the version of the integration
    * `TEST_CASE_ID`: the ID of the test case

In the output response, copy the text proto of the test case.

  * Call the [`projects.locations.integrations.versions.testCases.create` method](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.integrations.versions.testCases/create) and provide the text proto that you copied in the preceding step. 

For example:
        
        POST https://integrations.googleapis.com/v1/{parent=projects/PROJECT_ID/locations/LOCATION/integrations/INTEGRATION_NAME/versions/INTEGRATION_VERSION}/testCases
        




## Delete a test case

To delete a test case, select one of the following options:

### Console

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. In the navigation menu, click **Integrations**. 

The **Integrations** page appears listing all the integrations available in the Google Cloud project.

  3. Select an existing integration for which you want to create a test. 

This opens the integration in the _integration editor_.

  4. Click **Test Case** and then click **Open test cases**. The **Test Cases** pane appears with a list of test cases for the current integration version.
  5. Select the test case that you want to delete. 

In the Integration editor page, the designer canvas displays **Test case mode is active**.

  6. Click **delete Delete**. 



### API

Call the [`projects.locations.integrations.versions.testCases.delete` method](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.integrations.versions.testCases/delete). For example:
    
    
    DELETE https://integrations.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/integrations/INTEGRATION_NAME/versions/INTEGRATION_VERSION/testCases/TEST_CASE_ID
    

Replace the following:

  * `PROJECT_ID`: the ID of the Google Cloud project
  * `LOCATION`: the region where the integration is located
  * `INTEGRATION_NAME`: the name of the integration
  * `INTEGRATION_VERSION`: the version of the integration
  * `TEST_CASE_ID`: the ID of the test case that you want delete



## What's next

  * Learn about [test cases](https://docs.cloud.google.com/application-integration/docs/test-cases).
  * Learn how to do the following:

    * [Create test cases](https://docs.cloud.google.com/application-integration/docs/create-test-cases).
    * [Configure test cases](https://docs.cloud.google.com/application-integration/docs/configure-test-cases).
    * [Run a test case](https://docs.cloud.google.com/application-integration/docs/run-test-cases) and [view test case execution logs](https://docs.cloud.google.com/application-integration/docs/integration-execution-logs#view-integration-execution-logs).
    * [Upload and download test cases](https://docs.cloud.google.com/application-integration/docs/upload-download-test-cases).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
