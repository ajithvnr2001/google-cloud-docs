---
url: https://docs.cloud.google.com/application-integration/docs/configure-javascript-task/
title: JavaScript task \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:17:43.528168+00:00
---

# JavaScript task  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/configure-javascript-task/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# JavaScript task

**Deprecated:** Effective January 24, 2025, Application Integration will no longer support Rhino as the JavaScript execution engine. All existing published **JavaScript tasks** will continue to use Rhino and can be [migrated to V8 manually](https://docs.cloud.google.com/application-integration/docs/configure-javascript-task#migrate-javascript-tasks). Newly created **JavaScript tasks** will exclusively use V8. See [JavaScript execution engine](https://docs.cloud.google.com/application-integration/docs/configure-javascript-task#javascript-execution-engine) for more information. 

The **JavaScript** task lets you write custom JavaScript code snippets for your integration. 

Using the **JavaScript Editor** , you can code complex data mapping logic for your integration, perform variable assignments, and add or modify integration variables. 

The **JavaScript Editor** supports the following features: 

  * A minimap that displays a high-level overview of the script code and helps with quick navigation. 
  * Syntax/code highlighting, indentation, and line numbering for easier code readability and structure recognition. 
  * Error highlighting to find and track errors in code. 
  * Folding to expand and collapse regions of the script code. 
  * Click-to-copy option to copy the script code to the clipboard.



## Configure the JavaScript task

To add a **JavaScript** task to your integration, perform the following steps: 

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
  5. Click and place the **JavaScript** element in the integration editor.
  6. Click the **JavaScript** element on the designer to view the **JavaScript** task configuration pane.
  7. Click **Open script editor** to view and edit the **JavaScript Editor**. You can also use Gemini to generate JavaScript code by click **Script with Gemini**. For information about using Gemini to generate JavaScript code, see [Configure **JavaScript tasks** with Gemini assistance](https://docs.cloud.google.com/application-integration/docs/build-integrations-gemini#configure-javascript-tasks).
  8. Write your JavaScript code inside the `executesScript(event)` function that is automatically created in the **JavaScript Editor**. Close the editor once complete, any changes will be autosaved. **Warning:** Don't delete the `executesScript(event)` function. This function is called when the **JavaScript** task executes. 

For information about accessing integration variables and the supported functions, see [ Using the JavaScript Editor](https://docs.cloud.google.com/application-integration/docs/run-javascript-task#using-the-javascript-editor).

For information about viewing the generated execution logs, see [Execution logs](https://docs.cloud.google.com/application-integration/docs/viewing-logs). 




The following image shows a sample layout of the **JavaScript Editor** : ![image showing javascript editor](https://docs.cloud.google.com/static/application-integration/images/javascript_editor.png)![image showing javascript editor](https://docs.cloud.google.com/static/application-integration/images/javascript_editor.png)

## Use the JavaScript Editor

To view and edit the **JavaScript Editor** , go to the **JavaScript** task configuration pane and click **Open script editor**. The **JavaScript Editor** by default contains a function named `executesScript(event)`, where:

  * `executesScript()`: the function that is called when Application Integration executes the **JavaScript** task during an integration's run. 
  * `event`: the [in-memory object](https://docs.cloud.google.com/application-integration/docs/variables-overview#using-variable-data-in-integrations) of Application Integration. 

For information about the supported methods of the _event_ object, see [ Access integration variables](https://docs.cloud.google.com/application-integration/docs/run-javascript-task#access-integration-variables).


**Warning:** Don't delete the `executesScript(event)` function. This function is called when the **JavaScript** task executes. 

## JavaScript execution engine

**Deprecated:** Effective January 24, 2025, Application Integration will no longer support Rhino as the JavaScript execution engine. All existing published **JavaScript tasks** will continue to use Rhino and can be [migrated to V8 manually](https://docs.cloud.google.com/application-integration/docs/configure-javascript-task#migrate-javascript-tasks). Newly created **JavaScript tasks** will exclusively use V8. 

Application Integration previously supported Rhino as the JavaScript execution engine for running **JavaScript tasks**. To leverage the performance and security benefits of Google's open-source high-performance JavaScript engine, Rhino will be deprecated and all JavaScript executions will now utilize V8, Google's open-source high-performance JavaScript engine.

### Benefits of V8

The V8 JavaScript engine offers the following benefits:

  * **Performance:** V8 is significantly faster than Rhino, leading to improved execution speeds for your **JavaScript tasks**. Scripts with large sized variables and complex computations can be executed faster.
  * **Standards Compliance:** V8 supports ECMAScript 2024, ensuring better compatibility and maintainability.
  * **Security:** V8 benefits from ongoing security updates and improvements, providing a more secure environment for your integrations.
  * **Modern Features:** V8 supports the latest JavaScript features, allowing you to leverage modern language constructs and libraries.



### Migrate existing JavaScript tasks to V8

To migrate your existing **JavaScript tasks** running on Rhino to V8, do the following:

  1. Identify the published integrations that contain **JavaScript tasks** and unpublish them.
  2. For each **JavaScript** , click **Open script editor** from the task configuration pane. 

Application Integration automatically updates the existing script to use V8.

  3. Review and test the JavaScript code.
  4. Publish the integrations.



## Access integration variables

Variables defined in your integration can be accessed from the **JavaScript Editor** using the Application Integration [ in-memory _event_](https://docs.cloud.google.com/application-integration/docs/variables-overview#using-variable-data-in-integrations) object. 

The following methods are supported to access integration variables from your **JavaScript Editor** : 

Function name  | Description  | Usage   
---|---|---  
  
### `getEventExecutionInfoId`

| Returns the integration's run execution ID.  **Return type:** String  |  **Syntax:**`event.getEventExecutionInfoId()` **Example:**
    
    
    function executeScript(event) {
      event.getEventExecutionInfoId();
      }
            
  
### `getGoogleCloudProjectId`

| Returns the Google Cloud project ID.  **Return type:** String  |  **Syntax:** `event.getGoogleCloudProjectId()` **Example:**
    
    
    function executeScript(event) {
      event.getGcpProjectId();
      }  
  
### `getIntegrationName`

| Returns the current name of the integration.  **Return type:** String  |  **Syntax:** `event.getIntegrationName` **Example:**
    
    
    function executeScript(event) {
      event.getIntegrationName();
      }  
  
### `getParameter`

| Returns the value of the provided integration variable.  **Return type:** Data type of the integration variable  |  **Syntax:** `event.getParameter("variable_name")` **Input parameter:** Integration variable name. If the `variable_name` is an auto-generated variable, then enclose the variable in backticks (````). For example, ``responseBody``. **Example:**
    
    
    function executeScript(event) { 
      event.getParameter("var1");
      }  
  
### `getRegion`

| Returns the name of the integration region.  **Return type:** String  |  **Syntax:** `event.getRegion()` **Example:**
    
    
    function executeScript(event) {
      event.getRegion();
      }  
  
### `log`

| Writes the specified value to the execution logs. For information about viewing the generated execution logs, see [Execution logs](https://docs.cloud.google.com/application-integration/docs/viewing-logs).  |  **Syntax:** `event.log(value)` **Input parameter:** Any variable or function that is used in the script.  **Example 1:**
    
    
    function executeScript(event) {
      event.log(event.getParameter("var1"));
      }

**Example 2:**
    
    
    function executeScript(event) {
      event.log("Lorem ipsum");
      }  
  
### `setParameter`

| Sets or updates the value of an integration variable.  |  **Syntax:** `event.setParameter("variable_name", "variable_value")` **Input parameter:** This function takes the following arguments: 

  * First argument: Variable name. If the `variable_name` is an auto-generated variable, then enclose the variable in backticks (````). For example, ``responseBody``.
  * Second argument: Value.

**Example:**
    
    
    function executeScript(event) {
      event.setParameter("`responseBody`", "NewStringValue");
      }  
  
## Set task parameters

If your integration has multiple large sized parameters that are not used by the JavaScript task, you can set the `TaskParameter` field for the JavaScript task to improve performance.

To set the `TaskParameter` field for the JavaScript task, select one of the following options:

### Console

  1. Go to the **Application Integration** page. 

[ Go to Application Integration](https://console.cloud.google.com/integrations/list)

  2. Select an integration. The integration editor opens. 
  3. Click more_vert **Action** > **Download Integration** > **Integration Version**. The integration version is downloaded as a JSON file. 
  4. Open the integration version file in an editor, and then do the following: 
     1. Locate the `taskConfigs` field with the task as `JavaScriptTask`. In the `parameters` field, locate the parameter named `script`. 
            
            "taskConfigs": [{
              "task": "JavaScriptTask",
              "taskId": 1,
              "parameters": {
                "script": {
                  "key": "script",
                  "value": {
                    "stringValue": "function that is called during the JavaScriptTask execution"
                  }
              }"
            }]
            

     2. In this `parameters` field, add parameters that are used in the `JavaScriptTask` field by using the following template: 
            
            "ParamName": {
              "key": "ParamName",
              "value": {
                "stringValue": "$ParamName$"
              }
            }
            

  5. Save the changes that you made to the integration version file.
  6. [Upload the integration version](https://docs.cloud.google.com/application-integration/docs/upload-download-integrations#upload-an-integration) file to the integration.



### API

  1. To download the integration version, make a call to the `[projects.locations.integrations.versions.download](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.integrations.versions/download)` method with the `filFormat` set to `JSON`.
  2. Open the integration version file in an editor, and then do the following: 
     1. Locate the `taskConfigs` field with the task as `JavaScriptTask`. In the `parameters` field, locate the parameter named `script`. 
            
            "taskConfigs": [{
              "task": "JavaScriptTask",
              "taskId": 1,
              "parameters": {
                "script": {
                  "key": "script",
                  "value": {
                    "stringValue": "function that is called during the JavaScriptTask execution"
                  }
              }"
            }]
            

     2. In this `parameters` field, add parameters that are used in the `JavaScriptTask` field by using the following template: 
            
            "ParamName": {
              "key": "ParamName",
              "value": {
                "stringValue": "$ParamName$"
              }
            }
            

  3. To upload the integration version, make a call to the `[projects.locations.integrations.versions.upload](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.integrations.versions/upload)` method with the updated integration version file.



## Error handling strategy

An error handling strategy for a task specifies the action to take if the task fails due to a [temporary error](https://docs.cloud.google.com/application-integration/docs/error-handling). For information about how to use an error handling strategy, and to know about the different types of error handling strategies, see [Error handling strategies](https://docs.cloud.google.com/application-integration/docs/error-handling-strategy). 

## Quotas and limits

For information about quotas and limits, see [Quotas and limits](https://docs.cloud.google.com/application-integration/docs/quotas).

## What's next

  * Learn about the following: 
    * [Configuring JavaScript tasks with Gemini assistance](https://docs.cloud.google.com/application-integration/docs/build-integrations-gemini#configure-javascript-tasks)
[All tasks and triggers](https://docs.cloud.google.com/application-integration/docs/all-triggers-tasks)
  * [Testing and publishing integrations](https://docs.cloud.google.com/application-integration/docs/test-publish-integrations)
  * [Error handling](https://docs.cloud.google.com/application-integration/docs/error-handling-strategy)
  * [Integration execution logs](https://docs.cloud.google.com/application-integration/docs/introduction-logs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
