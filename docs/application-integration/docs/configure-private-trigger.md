---
url: https://docs.cloud.google.com/application-integration/docs/configure-private-trigger/
title: Private triggers \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:43.490306+00:00
---

# Private triggers  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/configure-private-trigger/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Private triggers

Private triggers enable you to break large flows into various subflows. You can invoke private triggers only from other integration flows within Application Integration. Being invokable only from other integrations increases security and reduces the risk. You can view the execution logs for a private task in the execution logs of the invoker integration.

The following list states the benefits of using private triggers:

  * **Minimize cost:** Private triggers are not counted towards execution run pricing.
  * **Increases security:** Restrict flows to be invoked only from other integrations as private triggers cannot be triggered independently from public APIs.
  * **Improve performance:** Private triggers reduces the latency between sub-integration callout.



## Add a Private trigger

To add a private trigger, perform the following steps: 

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. In the navigation menu, click **Integrations**

The **Integrations List** page appears listing all the integrations available in the Google Cloud project. 

  3. Select an existing integration or click **Create integration** to create a new one. 

If you are creating a new integration: 

     1. Enter a name and description in the **Create Integration** pane.
     2. Select a region for the integration. **Note:** The **Regions** dropdown only lists the regions provisioned in your Google Cloud project. To provision a new region, Click **Enable Region**. See [Enable new region](https://docs.cloud.google.com/application-integration/docs/enable-new-region) for more information. 
     3. Select a service account for the integration. You can change or update the service account details of an integration any time from the info **Integration summary** pane in the integration toolbar. **Note:** The option to select a service account is displayed only if you have enabled integration governance for the selected region. 
     4. Click **Create**.

The newly created integration opens in the _integration editor_. 

  4. In the _integration editor_ navigation bar, click **Triggers** to view the list of available triggers. 
  5. Click and place the **Private** element to the designer.



## Configure a Private trigger

  * Click the **Private Trigger** element in the integration editor to view the trigger configuration pane. 

The configuration panel displays the **Trigger ID** , which is a machine-generated ID in the format `private_trigger/TRIGGER_NAME`. No further configuration is required for this trigger.




## Test Private trigger

You cannot test a published private trigger workflow. You must unpublish the integration to test the private trigger workflow.

## Invoke Private trigger from another integration

After you have published an integration that has a private trigger configured, you can invoke this trigger from another integration. You can have more than one private trigger in your integration. Each private trigger is assigned a unique **Trigger ID**.

You can view the execution logs for a private trigger in the logs of the main execution workflow. Private triggers can be invoked from the following flow control tasks:

  * [Call Integration](https://docs.cloud.google.com/application-integration/docs/configure-call-integration-task)
  * [For Each Loop](https://docs.cloud.google.com/application-integration/docs/configure-for-each-loop-task)
  * [For Each Parallel](https://docs.cloud.google.com/application-integration/docs/configure-for-each-parallel-task)
  * [While Loop](https://docs.cloud.google.com/application-integration/docs/configure-while-loop-task)



## Quotas and limits

The execution of private triggers shares the _Maximum cumulative size of all the integration data_ limit, which is set to 30 MB, with the parent integration. For more information about limits, see [Usage limits](https://docs.cloud.google.com/application-integration/docs/quotas). 

## Limitation

If your private trigger workflow contains any of the following async tasks, then you can't trigger the private workflow from the main workflow with the `SYNC` execution strategy: 

  * [Timer task](https://docs.cloud.google.com/application-integration/docs/configure-timer-task)
  * [Suspend task](https://docs.cloud.google.com/application-integration/docs/configure-suspend-task)
  * [Approval task](https://docs.cloud.google.com/application-integration/docs/configure-approval-task)



## What's next

  * Learn about [all tasks and triggers](https://docs.cloud.google.com/application-integration/docs/all-triggers-tasks).
  * Learn how to [test and publish an integration](https://docs.cloud.google.com/application-integration/docs/test-publish-integrations).
  * Learn about [error handling](https://docs.cloud.google.com/application-integration/docs/error-handling-strategy).
  * Learn about [integration execution logs](https://docs.cloud.google.com/application-integration/docs/introduction-logs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
