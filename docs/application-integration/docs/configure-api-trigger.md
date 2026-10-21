---
url: https://docs.cloud.google.com/application-integration/docs/configure-api-trigger/
title: API trigger \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:17:36.956653+00:00
---

# API trigger  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/configure-api-trigger/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# API trigger

API triggers are used to directly invoke executions for integrations. 

Configuring an API trigger in your integration enables you to do the following: 

  * Set request and response payload using trigger specific input and output variables.
  * Generate and view the OpenAPI Specification (OAS) for your integration.
  * Invoke an integration [synchronously](https://docs.cloud.google.com/application-integration/docs/error-handling-strategy#synchronous-and-asynchronous-error-handling) or [asynchronously](https://docs.cloud.google.com/application-integration/docs/error-handling-strategy#synchronous-and-asynchronous-error-handling).

To help you get started with API triggers, see the [API fulfillment](https://docs.cloud.google.com/application-integration/docs/api-fulfilment) tutorial. The tutorial shows you how to create an integration with an API trigger that receives API requests for retrieving customer information. 

## Add an API trigger

To add an **API trigger** to your integration, perform the following steps: 

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
  5. Click and place the **API trigger** element to the designer.



## Configure an API trigger

To configure an API trigger, click the **API trigger** element in the integration editor. The API trigger configuration pane appears showing the following fields: 

  * **Label:** The visible name of the API trigger in your integration. You can change the label to a name of your choice. 
  * **Notes:** You can add notes to the API trigger to provide additional information about the trigger.
  * **Trigger ID:** A unique ID that is assigned to the API trigger in the format `api_trigger/TRIGGER_NAME`. **Note** : You can have more than one API trigger in your integration. Each API trigger is assigned a unique **Trigger ID**.
  * **Input variables:** Trigger specific input variables that you can use to set the request payload for the API trigger. 
    * To add or remove existing integration variables to the API trigger, click **Modify** and select the required variables from the **API trigger input variables** pane.
    * To add a new variable, specifically for the selected API trigger, click **Modify** and select **\+ Add new variable** from the **API trigger input variables** pane. For information about the supported data types, see [Supported variable data types](https://docs.cloud.google.com/application-integration/docs/variables#datatype).
  * **Output variables:** Trigger specific output variables that you can use to set the response payload for the API trigger. 
    * To add or remove existing integration variables to the API trigger, click **Modify** and select the required variables from the **API trigger output variables** pane.
    * To add a new variable, specifically for the selected API trigger, click **Modify** and select **\+ Add new variable** from the **API trigger output variables** pane. For information about the supported data types, see [Supported variable data types](https://docs.cloud.google.com/application-integration/docs/variables#datatype).
**Note** : You can create input and output variables from both the [Variables pane](https://docs.cloud.google.com/application-integration/docs/variables#create-a-variable) and the API trigger configuration pane. 
    * Application Integration automatically adds variables created from the API trigger configuration pane to that specific trigger as input or output variables.
    * You can manually add variables from one API trigger to another as input or output variables.
    * By default, all elements in your integration can access variables created from the Variables pane.
    * Changing the **Variable type** of a variable affects all the elements in your integration that use that variable.



## View OpenAPI Specification for your API trigger

Application Integration provides the ability to dynamically generate and view the OpenAPI Specifications of your published integrations that are configured with one or more API triggers. For information about how to view the OpenAPI Specification, see [View OpenAPI Specification for your integration](https://docs.cloud.google.com/application-integration/docs/view-openapi-spec). 

**Note:** This page focuses on invoking the API trigger using the v1 API. The OpenAPI Specification generated for your integration might include definitions for other API versions, such as v2.

##  Invoke an API trigger using an API call 

After you have published an integration that has an **API trigger** configured, you can use the [`projects.locations.integrations.execute`](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.integrations/execute) method to invoke that trigger from any application. This method triggers the execution in the [synchronous mode](https://docs.cloud.google.com/application-integration/docs/error-handling#error-handling-methods). 

### Syntax
    
    
    curl -X POST \
        -H "authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        -H "X-Server-Timeout: TIMEOUT_SECONDS" \
        -d '{"trigger_id":"api_trigger/TRIGGER_NAME"}' \
        "https://LOCATION-integrations.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/integrations/-:execute"
    

Replace the following: 

  * `TIMEOUT_SECONDS`: The timeout in seconds for the API call. By default, the timeout is 120 seconds. For a list of pre-defined set of request parameters, see [System parameters](https://docs.cloud.google.com/apis/docs/system-parameters).
  * `TRIGGER_NAME`: The name of the **API trigger** in your integration.
  * `PROJECT_ID`: The ID of your Google Cloud project.
  * `LOCATION`: The location of your Google Cloud project.



### Example

The following example invokes an integration in `us-east1` region containing the `test_API_1` API trigger in the `demo-project` Google Cloud project:
    
    
    curl -X POST \
        -H "authorization: Bearer $(gcloud auth print-access-token)"
        -H "Content-Type: application/json" \
        -H "X-Server-Timeout: 300"
        -d '{"trigger_id":"api_trigger/test_API_1"}' \
        "https://us-east1-integrations.googleapis.com/v1/projects/demo-project/locations/us-central1/integrations/-:execute"
    

## Considerations

When using the API trigger, the cumulative size of all the input variables can be a maximum of 8 MB. If the size exceeds 8 MB, Application Integration doesn't run the integration and you will get an error.

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
