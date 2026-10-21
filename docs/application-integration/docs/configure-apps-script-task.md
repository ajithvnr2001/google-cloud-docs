---
url: https://docs.cloud.google.com/application-integration/docs/configure-apps-script-task/
title: Apps Script task \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:17:40.413044+00:00
---

# Apps Script task  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/configure-apps-script-task/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Apps Script task

The **Apps Script** task lets you run Google Apps Script from your integration. Google Apps Script is a rapid application development platform that makes it fast and easy to create business applications. For more information, see [Google Apps Script](https://developers.google.com/apps-script/overview). This task is useful when you want to run custom scripts or reuse existing scripts in your integration. 

**Note** : The **Apps Script** task is a non-regional global service.

## Before you begin

Before using the Apps Script task, make sure you complete the following steps: 

  * Enable AppsScript API
  * Create OAuth 2.0 Client ID
  * Set up an authentication profile
  * Ensure that [VPC Service Controls](https://docs.cloud.google.com/application-integration/docs/vpc-service-controls) is **NOT** setup for Application Integration in your Google Cloud project. **Warning:** **Cloud Function** does not function or stops functioning if [VPC Service Controls](https://docs.cloud.google.com/application-integration/docs/vpc-service-controls) is set up for Application Integration in your Google Cloud project. 



### Enable AppsScript API

You must enable the AppsScript API in your Google Cloud project and your AppsScript user account to use this task. For information about enabling the AppsScript API in your Google Cloud project, see [Enabling an API in a standard Google Cloud project](https://developers.google.com/apps-script/guides/cloud-platform-projects#enabling_an_api_in_a_standard_gcp_project). To enable the API in your user account, click [Settings](https://script.google.com/corp/home/usersettings) and set `Google Apps Script API` to `On`. 

### Create OAuth 2.0 client ID

If you have an OAuth 2.0 client ID available, you can skip this step and proceed to  Set up an authentication profile. 

For information about creating a new OAuth client ID, see [Create OAuth client ID](https://docs.cloud.google.com/application-integration/docs/configure-authentication-profiles#create-oauth).

### Set up an authentication profile

Application Integration uses the authentication profile to connect to Google Cloud for deploying and running the Apps Script project. To set up an authentication profile, perform the following steps: 

####  Add the Apps Script task 

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
  5. Click and place the **Apps Script** element in the integration editor.



####  Create an authentication profile 

  1. Click the **Apps Script** element on the designer to view the **Apps Script** task configuration pane.
  2. In the task configuration pane of the Apps Script task, click **+New authentication profile**. 
  3. In the **Authentication profile** dialog, enter a name and description for the profile and set the following properties: 
     * **Authentication type** : Select **OAuth 2.0 authorization code**
     * **Authentication endpoint** : Enter `https://accounts.google.com/o/oauth2/auth`
     * **Token endpoint** : Enter `https://oauth2.googleapis.com/token`
     * **Client ID** : Enter the client ID. 

The Client ID is available in your Google Cloud project dashboard under **Credentials > OAuth 2.0 Client IDs**. 

     * **Secret** : Enter the client secret 

The client secret is available in your Google Cloud project dashboard under **Credentials > OAuth 2.0 Client IDs**. 

     * **Scope(s)** : Enter the following: 

`https://www.googleapis.com/auth/script.projects https://www.googleapis.com/auth/script.deployments https://www.googleapis.com/auth/script.deployments.readonly https://www.googleapis.com/auth/drive.scripts https://www.googleapis.com/auth/drive https://www.googleapis.com/auth/script.external_request https://www.googleapis.com/auth/userinfo.email`

**Note** : Multiple scopes can be separated by a single space character (" ").

  4. Click **Generate Access Token and Save**. 

You are redirected to an authorization screen. Log in and provide consent to the permissions listed on the screen to generate your access token. If the generation of the access token is successful, your authentication profile is saved, and you can continue to edit your integration. 


**Note** : The same user must create both the authentication profile and deploy the Apps Script. If the users are different, the Apps Script does not run. 

## Configure the Apps Script task

To configure an Apps Script project in the **Apps Script** task, perform the following steps: 

  1. In the task configuration pane, click **Configure Apps Script Project.**

The **Apps Script Configuration** dialog appears. 

  2. You can choose to link to an existing Apps Script project or create a new Apps Script project. 

Configuring an Apps Script project associates the Apps Script project with your integration in Application Integration. 

  3. Click Save.
  4. Click **Open Apps Script Project**. 

In the Apps Script editor, you can see the following files: 

     * `Run.gs`: Contains the executable code. Write your script inside the `run` function. This function is called when the Apps Script task executes. In your script, you can use the variables defined at the integration level. For information on using the integration variables, see Using integration variables. 
     * `Main.gs`: Contains the initialization code to run Apps Script from your integration. Do not edit or modify this file. 
     * `Test.gs`: Contains the executable code for test runs. You can write your script inside the `testRun` function to test the script. 

Make sure to deploy the project in **Web apps** format. For more information on the various deployment modes, see [ Create and manage deployments](https://developers.google.com/apps-script/concepts/deployments). 




## Access integration variables

The Apps Script task uses the **AppsScriptTask** library, which enables you to use integration variables in your script. The **AppsScriptTask** library is automatically imported and is available for use in the `run` function.

To access an integration variable in your Apps Script, you must pass the variable in the form of _task parameters_ to the Apps Script task. The task parameters are key-value pairs where **Key** is the name of the variable in your AppsScript task and the **Value** is the corresponding integration variable name. You can add one or more task parameters in the **Task Parameters** section of the task configuration pane. 

For example, if you have an integration variable named **Product** that you want to use in your Apps Script, you can define **Key** as **ProductKey** and the value as **Product**. In your Apps Script, you can then use `AppsScriptTask.getTaskParameter('**ProductKey** ')` to read the **Product** variable. 

**Note** : To use an integration variable in your AppsScript, the variable must be added as a task parameter to the Apps Script task. 

The **AppsScriptTask** library provides the following methods to access integration variables: 

  * [setIntegrationVariable](https://docs.cloud.google.com/application-integration/docs/run-apps-script-task#set)
  * [getTaskParameter](https://docs.cloud.google.com/application-integration/docs/run-apps-script-task#get)

Function name  | Description  | Usage   
---|---|---  
  
### `setIntegrationVariable`

| Sets the provided value to the variable. |  **Syntax:**`setIntegrationVariable(value,value)` **Example:**
    
    
    // Write to an Integer variable
    AppsScriptTask.setIntegrationVariable('**EmployeeIDKey** ','456');
            
  
### `getTaskParameter`

| Gets the value of a variable. |  **Syntax:**`getTaskParameter(value)` **Example:**
    
    
    // Read an integration variable
    AppsScriptTask.getTaskParameter('**EmployeeIDKey** ');
             
  
To view all the functions available in the **AppsScriptTask** library, hover over the **AppsScriptTask** menu item in your Apps Script editor, click More more_vert **> Open in a new tab**. 

## Test your Apps Script

Before publishing your integration, you can test your script using the **testRun** function available in the **Test.gs** file. Write your test code in the **testRun** function, using the **AppsScriptTaskTest** library. This library lets you run assertion-based test cases and is automatically imported for use in the **testRun** function.

To view all the functions available in the **AppsScriptTaskTest** library, hover over the **AppsScriptTaskTest** menu item in your Apps Script editor, click More more_vert **> Open in a new tab**. 

The following sample shows the usage of **AppsScriptTaskTest** library functions. 
    
    
    function testRun(){
    
      // Create a new request
      let req = AppsScriptTaskTest.createNewTestRequest('myCustomTest');
    
      // Add a task parameter that references an integration variable with the value 5
      AppsScriptTaskTest.setIntegrationVariableAndCreateReference(req, 'input', '$input$', 5);
    
      // Add a task parameter that references an integration variable
      AppsScriptTaskTest.createReference(req, 'output', '$output$');
    
      // Run the task(assuming the task increments the input by 1) and get the response
      let res = AppsScriptTaskTest.runTest(req, executeScript);
    
      // Check the response for the expected integration variable and its corresponding values
      AppsScriptTaskTest.containsIntegrationVariable(res, 'output', true);
      AppsScriptTaskTest.containsIntegrationVariable(res, 'someOtherIntegrtionVariable', false);
      AppsScriptTaskTest.containsIntegrationVariableWithValue(res, 'output', 6);
    }

The following sample shows you how to access JSON and array variables in the **testRun** method: 
    
    
    function testRun(){
    
      // Create a new request
      let req = AppsScriptTaskTest.createNewTestRequest('json-test');
    
      // Add a task parameter that references a JSON integration variable
      AppsScriptTaskTest.setIntegrationVariableAndCreateReference(req, "emp", "employee", {name:"snape", age:35});
    
      // Add a task parameter that references an array integration variable
      AppsScriptTaskTest.setIntegrationVariableAndCreateReference(req, "arr", "array", ["A", "B", "C"]);
    
    
      // Run the task and get the response
      // Assume that the run method increases the age of the employee by 5 and appends a new element in the array
      let res = AppsScriptTaskTest.runTest(req, executeScript);
    
      // Check the response for the expected integration variable and its corresponding values
      AppsScriptTaskTest.containsIntegrationVariableWithValue(res, "employee", {name:"snape", age:40});
      AppsScriptTaskTest.containsIntegrationVariable(res, "array", true);
      AppsScriptTaskTest.containsIntegrationVariableWithValue(res, "array", ["A", "B", "C", "D"]);
    }

After running the test cases, you can view the assertions in the **Execution log**. To view the logs, click **Execution log** from the menu. 

## Best practices 

We do not recommend using the Apps Script task if you require latency less than 1 to 2 seconds for the task in your integration. 

In addition, we recommend coding all your logic in a single Apps Script task, rather than chaining multiple Apps Script tasks, to minimize performance bottlenecks. 

For information about the usage limits that apply to the **Apps Script** task, see [ Usage limits](https://docs.cloud.google.com/application-integration/docs/quotas#usage-limits). 

## Considerations 

When including the Apps Script task in your integration design, consider the following system limitations: 

  * Maximum active deployments for an AppsScript: 50
  * Queries per second (QPS) for API executables: 5000/min
  * Queries per second (QPS) for Webapp deployments: 5000/min
  * Latency for API executables: 1.5s
  * Latency for Webapp: 2.5s
  * Maximum cumulative size of all the integration variables in an AppsScript: 15 MB



## Error handling strategy

An error handling strategy for a task specifies the action to take if the task fails due to a [temporary error](https://docs.cloud.google.com/application-integration/docs/error-handling). For information about how to use an error handling strategy, and to know about the different types of error handling strategies, see [Error handling strategies](https://docs.cloud.google.com/application-integration/docs/error-handling-strategy). 

## SLA exclusions

The Apps Script task has a dependency on the [Google Apps Script](https://developers.google.com/apps-script) product. Because this dependency is external to the Application Integration, all executions of `active` integrations that fail because of the failure in the Apps Script task, are excluded from the [Application Integration Service Level Agreement (SLA)](https://cloud.google.com/application-integration/sla) terms and conditions.

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
