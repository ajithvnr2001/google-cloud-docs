---
url: https://docs.cloud.google.com/application-integration/docs/configure-for-each-parallel-task/
title: For Each Parallel task \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:44.898234+00:00
---

# For Each Parallel task  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/configure-for-each-parallel-task/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# For Each Parallel task

The **For Each Parallel** task lets you run other integrations (sub-integrations) from your main integration. As the task name suggests, the sub-integrations run in parallel. 

This task uses the API **Trigger ID** as a handle to identify the integrations to run. For example, if you specify the API **Trigger ID** as `api_trigger/APITriggerX`, the task runs all the sub-integrations that have the `api_trigger/APITriggerX` trigger ID.

After running a sub-integration, you can also read the response of the sub-integration in your main integration. Use this task to run sub-integrations as dependencies of the main integration. 

## Before you begin

  * Ensure that you have [attached a user-managed service account](https://docs.cloud.google.com/application-integration/docs/access-control#add-service-account) to your integration. If your integration does not have user-managed service account configured, then by default the [default service account](https://docs.cloud.google.com/application-integration/docs/access-control#default-service-account) (`service-PROJECT_NUMBER@gcp-sa-integrations.iam.gserviceaccount.com`) is used for authentication.
  * Ensure that your service account has the **Application Integration Invoker** IAM role. For information about granting roles to a service account, see [Manage access to service accounts](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts).



## Configure the For Each Parallel task

To configure the **For Each Parallel** task:

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
  5. Click and place the **For Each Parallel** task element in the integration editor.
  6. Click the **For Each Parallel** task element on the designer to open the **For Each Parallel** task configuration pane.
  7. Configure the displayed fields using the Configuration properties for the task as detailed in the tables below. 

All changes to the properties are saved automatically. 




## Configuration properties

This section describes the configuration properties of the **For Each Parallel** task. 

### Input properties

**Property Name** | **Parameter Name** | **Data type** | **Description**  
---|---|---|---  
**Array Selection** | `**List to iterate**` | An array of type string, integer, double, or JSON.  | List of values for which the sub-integrations must run. A separate sub-integration thread runs for each value in the list, and all the threads run in parallel.  You can pass the iterated value to the sub-integration by setting the Where to map individual array elements field.  You can also pass additional values from the main integration to the sub-integration in the Map to additional sub-integration input(s) field.   
**Sub-integration Details** | `**API Trigger ID**` | String  | Trigger ID of the published sub-integration to run.  This value is available in the **Trigger ID** field of the **API Trigger** in the sub-integration.   
`**Execution strategy**` | N/A  |  **SYNC** : Runs the sub-integrations in synchronous mode. In this mode, the main integration waits for the sub-integrations to complete before continuing with the downstream tasks. **ASYNC** : Runs the sub-integrations in asynchronous mode. In this mode, the main integration does not wait for the sub-integrations to complete. Immediately after calling the sub-integrations, the main integration runs the downstream tasks.  
`**Run all integrations with this API Trigger ID**` | N/A | Runs all integrations that have the same API **Trigger ID**.  For example, if integration `A` and integration `B`, have the same API **Trigger ID** , both the integrations `A` and `B` are run for each item in List to iterate.  **Note** : If you select this option, the response from the sub-integrations is not be available in the main integration. If you want to use the response of the sub-integrations, select the **Run a single integration** option.   
`**Run a single integration**` | N/A |  Runs only the integration specified in the **Integration name** field. You can use the response from the sub-integrations by configuring the **Collect values from sub-integration output(s)** section.   
**On each execution** | `**Where to map individual array elements**` | String | The name of the sub-integration input variable where the array elements should be mapped. The array elements can be mapped directly to a sub-integration input variable. If a single sub-integration is selected, you can select the sub-integration input variable from a dropdown list.  
`**Map to additional sub-integration input(s)**` | String | Additional sub-integration mapping option. 

  * **Integration variable to map from** : The name of the variable in the current integration to be passed to the sub-integration's input variable.
  * **Sub-integration input to map to** : The name of the sub-integration input variable to map to.

This field takes values in the form of key-value pairs, where the key is a variable in the main integration, and the value is the corresponding input variable in the sub-integration.  For example, consider your main integration has the `productID` variable, which you want to map to the `subIntProductID` sub-integration variable; you must select `productID` from the **Integration variable to map from** field and enter `subIntProductID` in the **Sub-integration input to map to** field.   
`**Collect values from sub-integration output(s)**` | String | If the execution strategy is synchronous (SYNC) and a single sub-integration (Run a single integration) is selected, the outputs of the sub-integration can be collected into array variables in the current integration. 

  * **Sub-integration output to collect from** : The name of the sub-integration output variable to be aggregated.
  * **Integration variable to collect into** : The name of the variable in the current integration to collect the aggregated outputs.

  
**Execution Settings** | `**Integrations to execute at a time (parallel)**` | Integer  | Maximum number of parallel executions allowed for sub-integrations. The default value is `50` (`10000` maximum).  All sub-integrations in a cohort run completely before the next cohort of sub-integrations run.   
`**Ignore failures**` | Boolean  |  You can specify any one of the following values:

  * **True** : Task ignores sub-integration failures and runs all executions.
  * **False** : Task fails for sub-integration failures and ends all executions.

  
  
##  Best practices 

We recommend the following best practices when using the **For Each Parallel** task:

  * Set your cohort size based on any quota limitations imposed by your sub-integrations.
  * Use a **SYNC** execution strategy when you want to collect the output of the sub-integration for later use.
  * Use an **ASYNC** execution strategy when your sub-integration might run longer than **2 minutes**.



For information about the usage limits that apply to the **For Each Parallel** task, see [ Usage limits](https://docs.cloud.google.com/application-integration/docs/quotas#usage-limits). 

## Considerations

In general, do not use a **SYNC** execution strategy if your sub-integration takes longer than **2 minutes** to run or you plan to use this task in conjunction with naturally asynchronous tasks like the Approval task. 

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
