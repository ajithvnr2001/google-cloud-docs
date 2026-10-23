---
url: https://docs.cloud.google.com/application-integration/docs/configure-send-email-task/
title: Send Email task \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:18:06.694058+00:00
---

# Send Email task  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/configure-send-email-task/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Send Email task

The **Send Email** task lets you send custom email notifications from your integration. You can email one or more recipients with a custom subject and a custom message.

## Configure the Send Email task

To configure the **Send Email** task: 

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
  5. Click and place the **Send Email** task element in the integration editor.
  6. Click the **Send Email** task element on the designer to open the **Send Email** task configuration pane.
  7. Configure the displayed fields using the Configuration properties for the task as detailed in the tables below. 

All changes to the properties are saved automatically. 




## Configuration properties

The following table describes the configuration properties of the **Send Email** task. 

**Property** | **Data type** | **Description**  
---|---|---  
`**Recipients**` | String  | Email address of the recipient(s). You can specify multiple email addresses separated by a comma. For example, `test1@gmail.com,test2@gmail.com`. Alternatively, you can also [create a variable](https://docs.cloud.google.com/application-integration/docs/variables#create-a-variable) of type **String Array** and add comma separated emails in the value. **Note:** You can only add a maximum of 30 recipients to the task.   
`**Subject**` | String  | Email subject line.   
`**Body**` | String  | Email body in plaintext.   
  
You can set the properties to any of the following values: 

  * A literal
  * An integration variable
  * A combination of a literal and an integration variable



For the **Subject** and **Body** fields, you can enter combinations of literals and integration variables for the string values. Use dollar sign notation for variable names, that is, precede and follow the variable name with a `$` sign. For example, if you want to use a variable `$varSubject$` in the email **Subject** , you will enter text similar to `Test $varSubject$ `where `Test` is a literal and `$varSubject$` is the variable. 

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
