---
url: https://docs.cloud.google.com/application-integration/docs/configure-call-integration-task/
title: Call Integration task \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:10:34.879315+00:00
---

# Call Integration task  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/configure-call-integration-task/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Call Integration task

The **Call Integration** task lets you invoke or call other integrations created within your Google Cloud project.

The **Call Integration** task is useful in scenarios where you need to define multiple small integrations (sub-integrations) that is controlled using a main integration (parent integration). After running a sub-integration, you can also read the response of the sub-integration in your main integration. 

## Before you begin

  * The **Call Integration** task uses the API trigger to identify and call other integrations and sub-integrations. Therefore, you must ensure that the integrations you want to call are configured using the API trigger. For information about configuring an API trigger see [API trigger](https://docs.cloud.google.com/application-integration/docs/configuring-api-trigger). 
  * Ensure that you have [attached a user-managed service account](https://docs.cloud.google.com/application-integration/docs/access-control#add-service-account) to your integration. If your integration does not have user-managed service account configured, then by default the [default service account](https://docs.cloud.google.com/application-integration/docs/access-control#default-service-account) (`service-PROJECT_NUMBER@gcp-sa-integrations.iam.gserviceaccount.com`) is used for authentication.
  * Ensure that your service account has the **Application Integration Invoker** IAM role. For information about granting roles to a service account, see [Manage access to service accounts](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts).



## Configure the Call Integration task

To configure the **Call Integration** task: 

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
  5. Click and place the **Call Integration** element in the integration editor.
  6. Click the **Call Integration** task element on the designer to view the **Call Integration** task configuration pane.
  7. Configure the following sub integration details: 
     1. **API Trigger ID:** Type the [API trigger ID](https://docs.cloud.google.com/application-integration/docs/configuring-api-trigger#configure-an-api-trigger) of the integration that you want to call. You can call a single integration or multiple integrations with the same trigger ID.
     2. **Run all integrations with this API Trigger ID:** Select this option to call all the integrations that have the same API **Trigger ID**. 

For example, if integration `A` and integration `B`, have the same API **Trigger ID** , both the integrations `A` and `B` are run. 

**Note** : If you select this option, the response from the sub-integrations will not be available in the main integration. If you want to access the response of the sub-integrations, select the **Run a single integration** option. 

     3. **Run a single integration** : Select this option to call only the integration specified in the **Integration name** field. You can access and map the response from the sub-integration by configuring the fields detailed in Map sub-integration response variables. 

     4. **Execution strategy:** Select the execution modes for the sub-integrations that you want to call. 
        * **SYNC** : Runs the sub-integration in synchronous mode. In this mode, the main integration waits for the sub-integrations to complete before continuing with the downstream tasks. 

        * **ASYNC** : Runs the sub-integration in asynchronous mode. In this mode, the main integration does not wait for the sub-integrations to complete. Immediately after calling the sub integrations, the main integration runs the downstream tasks. 

If this option is selected, set the **Execution delay (in milliseconds)**. When set, this specifies the time delay until the integration is run. 

All changes to the properties are saved automatically. 




## Map sub-integration response variables

The following table describes the configuration properties to map variables between the main integration and sub-integrations: **Property** | **Description**  
---|---  
`Map to sub-integration input(s)` |  Maps values from the main integration to the sub-integration. This field takes values in the form of key-value pairs, where the key is a variable in the main integration, and the value is the corresponding input variable in the sub-integration.  For example, if you want to map the main integration's `productID` variable to the `subIntProductID` sub-integration variable, select `productID` from the **Integration variable to map from** field and enter `subIntProductID` in the **Subintegration input to map to** field.  
`Map values to sub-integration output(s)` |  Maps the sub-integration output variables to the main integration variables. Click **Subintegration output to map from** and select the sub-integration. Click **Integration variable to map to** and select the corresponding main integration variable.  **Note:** This field is only displayed when the **Run a single integration** option is selected with the **SYNC** execution strategy.   
  
## Best practices

For information about the usage limits that apply to the **Call Integration** task, see [ Usage limits](https://docs.cloud.google.com/application-integration/docs/quotas#usage-limits). 

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
