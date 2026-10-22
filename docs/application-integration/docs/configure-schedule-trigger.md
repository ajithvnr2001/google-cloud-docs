---
url: https://docs.cloud.google.com/application-integration/docs/configure-schedule-trigger/
title: Schedule trigger \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:39:03.029444+00:00
---

# Schedule trigger  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/configure-schedule-trigger/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Schedule trigger

The **Schedule trigger** lets you run your integration periodically at specific time intervals. This trigger is useful when you want to run your integration automatically without any manual intervention. For example, you can consider using the **Schedule trigger** for the following type of tasks: 

  * Uploading files from one system to another system at regular intervals 
  * Sending periodic email reminders 
  * Syncing database at regular intervals

**Note:** For more stable and reliable scheduled triggering, we recommend using the [Cloud Scheduler trigger](https://docs.cloud.google.com/application-integration/docs/configure-cloud-scheduler-trigger).

## Add a Schedule trigger

To add a **Schedule trigger** to a new or existing integration, perform the following steps: 

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
  5. Click and place the **Schedule trigger** element to the designer.



## Configure a Schedule trigger

Click the **Schedule trigger** element in the integration editor to view the trigger configuration pane.

You can configure the **Schedule trigger** using either of the following modes: 

  * **Basic** : Provides a user interface to configure the frequency of the run. 
  * **Advanced** : Uses a cron expression to configure the frequency of the run.



In **Basic** mode, you can choose to run the integration at a specific time or at hourly intervals. If you want to run the integration at a specific time, select the **Run at a specific time** from the **Times** drop-down and set the following properties: 

  * **Time** : The time (in 24-hour format) at which the integration must run. 
  * **Days** : The days on which the integration must run. You can select to run the integration every day, on specific days of the week, on a specific day of the month, etc. 
  * **Months** : The month(s) in which the integration must run. You can run the integration every month or choose specific months.



In **Advanced** mode, you can specify the frequency of the run using a cron expression. The cron expression has five values that must be specified in the following order: 

  * Minute (0-59)
  * Hour (0-23)
  * Day of the month (1-31)
  * Month, either of the following values: 
    * A number 1-12
    * A three-letter month abbreviation (e.g. Jan, Feb, Mar, etc.)
  * Day of week, either of the following values: 
    * A number from 0 - 6 starting with Sunday as 0
    * A three-letter day abbreviation (e.g. Mon, Tue, Wed, etc.)



For example, to run the integration on the first day of every month, use the `* * 1 * *` cron expression. 

## Best practices

As a best practice, deactivate **Schedule triggers** when they are no longer needed. If you leave a redundant **Schedule trigger** active, it will continue to trigger the integration automatically.

To deactivate a **Schedule trigger** , you can do one of the following: 

  * Unpublish the integration containing the **Schedule trigger**. Your integration will no longer be active and the trigger will not run.
  * Replace the **Schedule trigger** with a different trigger and re-publish the integration. The re-published, active version of the integration will not use the **Schedule trigger**. 
  * Delete the current version of the integration. You can find the **Delete** option under the version list next to the integration name.



## SLA exclusions

All executions of `active` integrations that fail because the Schedule trigger didn't get scheduled for any reason, are excluded from the [Application Integration Service Level Agreement (SLA)](https://cloud.google.com/application-integration/sla) terms and conditions.

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
