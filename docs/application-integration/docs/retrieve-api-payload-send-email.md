---
url: https://docs.cloud.google.com/application-integration/docs/retrieve-api-payload-send-email/
title: Retrieve API payload and send an email \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:17:51.655382+00:00
---

# Retrieve API payload and send an email  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/retrieve-api-payload-send-email/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Retrieve API payload and send an email 

Learn how to create a sample integration in Application Integration. The following steps describe how to configure the trigger, tasks, edges, variables, and data mappings required to run a complete integration. 

## Overview

In this quickstart, you will retrieve the number of page views from a public API, transform the data into a usable format, and send the resulting list in an email, all from within the integration editor. 

* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/freetrial?redirectPath=/integrations?walkthrough_id=application-integration--qs_task_call_rest_endpoint)

* * *

## Create a new integration

To create a new integration, perform the following steps: 

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. Click **Integrations** from the left navigation menu to open the **Integrations** page. 
  3. Click **Create Integration**.
  4. Enter a name and description in the **Create Integration** dialog. 

For this quickstart, enter the name `my-test-integration` and the description `Integration for quickstart`. 

  5. Select a region for the integration. **Note:** The **Regions** dropdown only lists the regions provisioned in your Google Cloud project. To provision a new region, Click **Enable Region**. See [Enable new region](https://docs.cloud.google.com/application-integration/docs/enable-new-region) for more information. 
  6. Click **Create** to open the integration editor.



## Add and configure an API trigger

Triggers are required to start the sequence of tasks that make up an integration. Any available trigger can be used to start an integration. For this quickstart, use the **API trigger**.

To configure the **API trigger, do the following:**

  1. In the integration editor, click **Triggers** to display a list of available triggers. 
  2. Click **API trigger** in the integration editor.
  3. To configure the trigeer, click **API trigger**. The trigger configuration pane appears.
  4. Application Integration automatically populates the trigger **Label** and **Trigger ID**. The **Trigger ID** is machine-generated and you cannot edit the value. However, you can edit the value of the **Label** property. 

Changes to the properties are saved automatically.




## Add and configure tasks

A task is an executable set of steps that can take variables as inputs and generate variables as outputs. As with triggers, any available task can be used in an integration. This quickstart uses the **Call REST Endpoint** , **Data Mapping** , and **Send Email** tasks. Configuration details for each task are described in the steps below.

### Configure the Call REST Endpoint task 

To configure the **Call REST Endpoint** task, do the following: 

  1. Select **Tasks** to display a list of available tasks. 
  2. Click and place **Call REST Endpoint** in the integration editor.
  3. Add an edge connection from **API trigger** to **Call REST Endpoint** by hovering over a control point on **API trigger** , then clicking and dragging a line to a control point on the **Call REST Endpoint** task. The edge denotes the flow of control from the **API trigger** to the **Call REST Endpoint** task. 

An edge is a connection between any two elements in an integration. The connection denotes the direction of the control flow from one element (task or trigger) to another. For more information about edges, see [Edges](https://docs.cloud.google.com/application-integration/docs/edge-overview).

  4. To configure the task, click **Call REST Endpoint**. The task configuration pane appears. Set the following properties: 
     * **Label:** Enter a custom name for this task. For example, enter `Call REST Endpoint Task`. 
     * **Authentication:** For this quickstart, an authentication profile is not required. For more information on using authentication profiles for other use cases, see [ Create authentication profiles in Application Integration](https://docs.cloud.google.com/application-integration/docs/configuring-auth-profile).
     * **Task Input:** Enter the details for calling the REST endpoint. The information entered here is used as input for the **Call REST Endpoint** task. The following diagram shows the **Task Input** and **HTTP settings** sections for the **Call REST Endpoint** task: 

![Call rest endpoint task input](https://docs.cloud.google.com/static/application-integration/images/call-rest-endpoint-task-input.png)![Call rest endpoint task input](https://docs.cloud.google.com/static/application-integration/images/call-rest-endpoint-task-input.png)

Enter the following information:

       * **Endpoint base URL:** Enter `https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/desktop/user/Tree/monthly/20201001/20201031`. This public API from wikimedia.org returns the number of page views for an article named **Tree** for a given month.
       * **HTTP method:** Select `GET` using the dropdown list.
     * **HTTP settings:** Application Integration populates the following values: 
       1. **Follow redirects:** `True`
       2. **Task should fail on HTTP Error:** `True`
     * **Task Output:** Application Integration populates three variables to hold the response data output of calling the REST endpoint. The following diagram shows the **Task Output** and other sections for the **Call REST Endpoint** task: 

![Call rest endpoint task output](https://docs.cloud.google.com/static/application-integration/images/call-rest-endpoint-task-output.png)![Call rest endpoint task output](https://docs.cloud.google.com/static/application-integration/images/call-rest-endpoint-task-output.png)

Review the following information:

       * **responseHeader(Call REST Endpoint):** This variable holds the response header data associated with the **Call REST Endpoint** task. The variable data is of type `String` (STR).
       * **responseBody(Call REST Endpoint):** This variable holds the response body data associated with the **Call REST Endpoint** task. The variable data is of type `String` (STR).
       * **responseStatus(Call REST Endpoint):** This variable holds the response status data associated with the **Call REST Endpoint** task. The variable data is of type `String` (STR).
     * The remaining fields should contain the following default values: 
       * **Execution strategy for this task:** `When all tasks succeed`
       * **Execution policy for next task:** `Run all match`

Changes to the properties are saved automatically.




### Add and configure the Data Mapping task

To configure the **Data Mapping** task: 

  1. Select **Tasks** to display a list of available tasks. 
  2. Click and place **Data Mapping** in the integration editor.
  3. Add an edge connection from **Call REST Endpoint** to **Data Mapping** by hovering over a control point on **Call REST Endpoint** , then clicking and dragging a line to a control point on the **Data Mapping** task. The edge denotes the flow of control from the **Call REST Endpoint** task to the **Data Mapping** task. 
  4. To configure the task, click the **Data Mapping** task. The configuration pane of the task appears. 
  5. Click **Open Data Mapping Editor**. 

The **Data Mapping Editor** lets you to map input variables to the desired output variables, using the available transformation functions. The output is then available as a variable to any other integration task or trigger. For more details on passing data as variables, see [ Variables](https://docs.cloud.google.com/application-integration/docs/variables).

For this quickstart, create a mapping using the **responseBody(Call REST Endpoint)** as input: 

     1. Drag the **responseBody** variable from the **Variables** pane to the first **Input** row.
     2. Click **\+ (Add a function)** in the **responseBody** variable chip to view the list of available functions. You can apply a number of functions to transform the data in the input variable. 

In this case, you can convert the payload to JSON and then iterate over the response array to get the list of product names required for your email notifications. To do so, follow these steps: 

        * Select `TO_JSON()` to convert the **responseBody** string to JSON.
        * Click **\+ (Add a function)** in the **responseBody** variable chip to select and chain the `GET_PROPERTY()` function.
        * To add the input parameter for `GET_PROPERTY()`, click **Variable or Value** and in **Value** enter `items`. 

This function will extract a property from the JSON payload. Pass in the `items` property as the parameter for this function. This will return a list of ONLY the product names, with no other product information. Your function should read as follows: 
              
              responseBody(Call REST Endpoint).TO_JSON().GET_PROPERTY(items)

        * If you need to remove or delete a function, click the **-** symbol.
     3. Click the first field in the **Output** column to create a new output variable to hold the value of the transformed data. Complete the following fields: 
        * In the **Name** field, enter `JSONList`.
        * From the **Variable Type** list, select **Output from integration**.
        * From the **Data Type** list, select **JSON**
        * To create the variable and close the pane, click **Create**. The new **JSONList** variable will appear in the **Variables** list on the left side of the Data Mapping editor.
     4. Close the Data Mapping Editor after your mapping is complete. Any changes will be autosaved. The following images shows the Data Mapping Editor with the mapping created in this quickstart: 

![Data mapping editor](https://docs.cloud.google.com/static/application-integration/images/data-mapping-editor-screen.png)![Data mapping editor](https://docs.cloud.google.com/static/application-integration/images/data-mapping-editor-screen.png)




### Add and configure the Send Email task

To configure the **Send Email** task: 

  1. Select **Tasks** in the integration editor to display the list of available tasks.
  2. Click and place **Send Email** in the integration editor.
  3. Add an edge connection from **Data Mapping** to **Send Email** by hovering over a control point on **Data Mapping** , then clicking and dragging a line to a control point on the **Send Email** task. The edge denotes the flow of control from the **Data Mapping** task to the **Send Email** task. 
  4. To configure the task, click **Send Email**. The configuration pane of the task appears. In the **Task Input** section, set the following properties: 
     * **To Recipient(s):** Enter your email address. You will use this email to confirm the successful completion of the integration. 
     * **Subject:** Enter `Email from Application Integration`. 
     * **Body in Plain Text:** Select the `JSONList` variable created earlier in the **Data Mapping** task. 
     * The remaining options can be left in the default configuration.

Changes to the properties are saved automatically.




###  Verify the required edge connections 

Verify that you've added edge connection between task and triggers in your integration. The connection denotes the direction of the control flow from one element (task or trigger) to another. For more information about edges, see [Edges](https://docs.cloud.google.com/application-integration/docs/edge-and-edge-conditions). 

The completed connection should appear as shown in the figure below: 

![image showing quickstart flow](https://docs.cloud.google.com/static/application-integration/images/quickstart-int-map.png)![image showing quickstart flow](https://docs.cloud.google.com/static/application-integration/images/quickstart-int-map.png)

## Test the integration

To test the new integration: 

  1. Click **Test** in the integration editor toolbar. 

The **Test Integration** pane appears. 

  2. Click **Test integration**.



For more information about testing, see [Test and publish integrations](https://docs.cloud.google.com/application-integration/docs/test-publish-integrations).

Upon successful completion, the integration sends an email with the JSON values to the email address specified in the **Send Email** task. Confirm receipt of the email in your email client.

The email sent by the integration should contain a body similar to the following: 
    
    
    [{
       "project": "en.wikipedia",
       "article": "Tree",
       "granularity": "monthly",
       "timestamp": "2020100100",
       "access": "desktop",
       "agent": "user",
       "views": 33828.0
    }]

In addition to verifying the contents of the email, you can inspect the logs to view the status and payload of a given integration. To view logs: 

  1. Click **Logs** in the toolbar of the integration editor.
  2. On the **Execution Logs** page, you can view details about each attempt to run an integration. Each entry includes details for the execution attempt, including: 
     * **Integration name**
     * **Execution ID**
     * **Status**
     * **Start time**
     * **Duration**
     * **Integration Version**
     * **Trigger ID**
     * **Cloud Logging**
  3. Click the expander arrow (**>**) next to the executed integration to view an expanded list of tasks and variables in the integration, along with task status and variable payloads.



## Quotas and limits

For information about quotas and limits, see [Quotas and limits](https://docs.cloud.google.com/application-integration/docs/quotas).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
