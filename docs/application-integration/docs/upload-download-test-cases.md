---
url: https://docs.cloud.google.com/application-integration/docs/upload-download-test-cases/
title: Upload and download test cases \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:17:51.438585+00:00
---

# Upload and download test cases  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/upload-download-test-cases/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Upload and download test cases

**Preview — Test cases**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how to upload and download test cases for your integrations. For information about test cases, supported test configurations, and its limitations, see [Introduction to test cases](https://docs.cloud.google.com/application-integration/docs/test-cases).

## Before you begin

  * To get the permissions that you need to upload and download test cases, ask your administrator to grant you the [Application Integration Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to upload and download test cases. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to upload and download test cases:

    * Upload a test case: `integrations.googleapis.com/testCases.create`
    * Download a test case: `integrations.googleapis.com/testCases.get`

You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  * To download a test case, ensure that you have a test case in the integration. For information about how to create a test case, see [Create Test Cases](https://docs.cloud.google.com/application-integration/docs/create-test-cases).



## Upload a test case

To upload a test case, select one of the following options:

### Console

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. In the navigation menu, click **Integrations**. 

The **Integrations** page appears listing all the integrations available in the Google Cloud project.

  3. Select an existing integration for which you want to create a test. 

This opens the integration in the _integration editor_.

  4. To upload a test case from your local machine, from the **Test Case** list, select **Upload a test case**.



### API

Call the [`projects.locations.integrations.versions.testCases.upload` method](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.integrations.versions.testCases/upload) and provide any relevant parameters. For example:
    
    
    POST https://integrations.googleapis.com/v1/{parent=projects/PROJECT_ID/locations/LOCATION/integrations/INTEGRATION_NAME/versions/INTEGRATION_VERSION}/testCases:upload
    

Replace the following:

  * `PROJECT_ID`: the ID of the Google Cloud project
  * `LOCATION`: the region where the integration is located
  * `INTEGRATION_NAME`: the name of the integration
  * `INTEGRATION_VERSION`: the version of the integration



The request body contains the content of the file in a string format and the file format. The valid file formats are `.json` and `.yaml`.

## Download a test case

To download a test case for an integration version, select one of the following options:

### Console

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. In the navigation menu, click **Integrations**. 

The **Integrations** page appears listing all the integrations available in the Google Cloud project.

  3. Select an existing integration that contains test cases. 

This opens the integration in the _integration editor_.

  4. Click **Test Case** and then click **Open test cases**. The **Test Cases** pane appears with a list of test cases for the current integration version.
  5. Select the test case that you want to download. 

In the Integration editor page, the designer canvas displays **Test case mode is active**.

  6. Click download **Download**.



### API

Call the [`projects.locations.integrations.versions.testCases.download` method](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.integrations.versions.testCases/download). For example:
    
    
    POST https://integrations.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/integrations/INTEGRATION_NAME/versions/INTEGRATION_VERSION/testCases/TEST_CASE_ID
    

Replace the following:

  * `PROJECT_ID`: the ID of the Google Cloud project
  * `LOCATION`: the region where the integration is located
  * `INTEGRATION_NAME`: the name of the integration
  * `INTEGRATION_VERSION`: the version of the integration
  * `TEST_CASE_ID`: the ID of the test case that you want download



## What's next

  * Learn about [test cases](https://docs.cloud.google.com/application-integration/docs/test-cases).
  * Learn how to do the following:

    * [Create test cases](https://docs.cloud.google.com/application-integration/docs/create-test-cases).
    * [Configure test cases](https://docs.cloud.google.com/application-integration/docs/configure-test-cases).
    * [Run a test case](https://docs.cloud.google.com/application-integration/docs/run-test-cases) and [view test case execution logs](https://docs.cloud.google.com/application-integration/docs/integration-execution-logs#view-integration-execution-logs).
    * [Copy](https://docs.cloud.google.com/application-integration/docs/manage-test-cases#copy) and [delete](https://docs.cloud.google.com/application-integration/docs/manage-test-cases#delete) test cases.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
