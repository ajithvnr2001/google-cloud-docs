---
url: https://docs.cloud.google.com/application-integration/docs/test-publish-integrations/
title: Test and publish integrations \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:30:25.723954+00:00
---

# Test and publish integrations  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/test-publish-integrations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Test and publish integrations

You can test or publish an integration from the [integration editor](https://docs.cloud.google.com/application-integration/docs/integrations-ui-layout) after you have added and configured the integration with the necessary [triggers](https://docs.cloud.google.com/application-integration/docs/trigger-overview), [tasks](https://docs.cloud.google.com/application-integration/docs/task-overview), and [edge](https://docs.cloud.google.com/application-integration/docs/edge-overview) connections. When you test an integration using the Google Cloud console, the integration is executed in the [synchronous mode](https://docs.cloud.google.com/application-integration/docs/triggers#execution-modes). 

## Required role

To get the permissions that you need to test or publish an integration, ask your administrator to grant you the [Application Integration Service Agent ](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Test an integration

Optionally, if you want to verify that your integration is working as intended, you can test it before publishing. Testing an integration lets you experiment with the integration input variable values, and helps in identifying any faults in the integration connection flow. 

**Note:** Integrations that are configured with suspension-based tasks, such as [Approval task](https://docs.cloud.google.com/application-integration/docs/approval-task), [Suspend task](https://docs.cloud.google.com/application-integration/docs/run-suspend-task), or [Timer task](https://docs.cloud.google.com/application-integration/docs/run-timer-task), cannot be tested before publishing the integration. 

To test run an integration, select one of the following options: 

### Console

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. Click **Integrations** from the left navigation menu to open the **Integrations** page. 
  3. Select the integration that you want to test. 
  4. In the designer navigation bar, click **Test**. 

If you have multiple triggers configured in your integration, then select the trigger from which you want to test run your integration. The **Test Integration** pane appears. 

  5. Click **Test integration**.

Application Integration test runs the integration and displays the execution result in the **Test Integration** pane: 

     * To edit the input variables, click **Edit input variables**.
     * To retest the integration, click **Retest integration**.
     * To restore the values, click **Restore values**.
     * To view and inspect the [execution logs](https://docs.cloud.google.com/application-integration/docs/viewing-logs) of the test run, click **View logs**.
     * If you have [enabled Cloud Logging](https://docs.cloud.google.com/application-integration/docs/cloud-logging#enable-cloud-logging), then to view logs in Cloud Logging, click **View Cloud logs**.
     * To edit the integration without creating a new version of the integration, click **Edit integration**.
     * To close the test operation and return to the integration editor, click **Close**.



### API

Call the [`projects.locations.integrations.test`](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.integrations/test) method. 

To set the timeout of the flow, set the `X-Server-Timeout` field in the header. By default, the timeout is 120 seconds. For a list of pre-defined set of request parameters, see [System parameters](https://docs.cloud.google.com/apis/docs/system-parameters).

## Publish an integration

Publishing an integration version deploys that integration version, and puts it in an [active state](https://docs.cloud.google.com/application-integration/docs/integration-versions). Any previously published version of the integration will automatically be unpublished, and all the services that rely on the previously published integration version will automatically use the latest published version. 

To publish an integration, select one of the following options: 

### Console

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. Click **Integrations** from the left navigation menu to open the **Integrations** page. 
  3. Select the integration that you want to publish.
  4. In the designer navigation bar, click the **Version dropdown** , and select the integration version that you want to publish.
  5. Click **Publish**. 

The **Autogenerate Integration description** dialog appears. If you want to generate a description, click **Sure, continue**. Otherwise, click **No, just publish**.




Upon successfully publishing your integration, you can view and inspect the [execution logs](https://docs.cloud.google.com/application-integration/docs/integration-execution-logs) of the published integration. To view logs, click **Logs** in the toolbar of the integration editor. 

By default, Application Integration locks an integration from editing when it is published. To make any changes to the published integration, click **Enable editing** in the integration editor. Editing a published integration will create a new version of that integration. 

### API

Call the [`projects.locations.integrations.versions.publish`](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.integrations.versions/publish) method. 

### Unpublish an integration

Unpublishing an [active](https://docs.cloud.google.com/application-integration/docs/integration-versions) integration version undeploys that integration version, and puts it in a [snapshot](https://docs.cloud.google.com/application-integration/docs/integration-versions) state. Any services that rely on the published version of the integration will automatically be stopped. 

To unpublish an integration, select one of the following options:

### Console

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. Click **Integrations** from the left navigation menu to open the **Integrations** page. 
  3. Select the integration that you want to unpublish.
  4. In the designer navigation bar, click the **Version dropdown** , and select the integration version that you want to unpublish.
  5. Click **Unpublish**. 

After the integration is successfully unpublished, you can click **Enable editing** in the integration editor to edit the integration. Editing the integration will create a new version of that integration. 




### API

Call the [`projects.locations.integrations.versions.unpublish`](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.integrations.versions/unpublish) method. 

## Quota and limits

For information about Application Integration quotas and limits, see [Quotas and limits](https://docs.cloud.google.com/application-integration/docs/quotas).

## Best practice

  * Define the usability of a [variable (input variable or output variable)](https://docs.cloud.google.com/application-integration/docs/variables) before testing your integration. See Integration variables.
  * Define [error handling](https://docs.cloud.google.com/application-integration/docs/error-handling) for your integration.



## Quotas and limits

For information about quotas and limits, see [Quotas and limits](https://docs.cloud.google.com/application-integration/docs/quotas).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
