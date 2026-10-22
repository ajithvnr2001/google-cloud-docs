---
url: https://docs.cloud.google.com/application-integration/docs/try-sample-integration-ecommerce/
title: Try the sample integration \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:30:29.753536+00:00
---

# Try the sample integration  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/try-sample-integration-ecommerce/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Try the sample integration

While setting up Application Integration in your Google Cloud project for the first time, Application Integration, by default, creates an _unpublished_ sample integration named **ExampleIntegration-EcomOrderProcessing**. 

## View sample integration

To view the sample integtration, do the following: 

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. Click **Integrations** from the left navigation menu to open the **Integrations** page. 
  3. Click the integration named **ExampleIntegration-EcomOrderProcessing**. 

The sample integration opens in the [integration editor](https://docs.cloud.google.com/application-integration/docs/integrations-ui-layout) similar to the following layout: 

![Sample integration layout image](https://docs.cloud.google.com/static/application-integration/images/sample-integration-ecom.png)![Sample integration layout image](https://docs.cloud.google.com/static/application-integration/images/sample-integration-ecom.png)


**Tip:** If you are unable to find or open the sample integration, you can download the JSON version of the integration and upload it back using the integration editor. For more information, see [E-commerce sample integration](https://docs.cloud.google.com/application-integration/docs/samples/ecom-order-processing). 

## E-commerce sample integration

You can use this sample integration to get a hands-on experience of the various [triggers](https://docs.cloud.google.com/application-integration/docs/triggers), [tasks](https://docs.cloud.google.com/application-integration/docs/tasks), and [concepts](https://docs.cloud.google.com/application-integration/docs/concepts) of Application Integration. 

The sample integration illustrates a basic e-commerce back-end scenario implementing the following order processing operation: 

  1. Receive the following order request payload from an API endpoint: 
         
         {
           "order_no": "12345",
           "buyer_id": "raambo",
           "line_items": [
             {
               "line": 1,
               "sku": "tr100",
               "vendor": "Internal",
               "quantity": 1,
               "price_per_unit": 10
             },
             {
               "line": 2,
               "sku": "tbz",
               "vendor": "External",
               "quantity": 24.0,
               "price_per_unit": 1
             }
           ]
         }

  2. Extract the order payload and calculate the total order value.
  3. Check if the total order value is greater than or equal to $100. If yes, then get an additional approval to continue.
  4. Check if any of the order items have an _external_ vendor. If yes, then send the details to the vendor using a REST API call.
  5. Send out the order response with the total order value, filtered external vendor items and their respective HTTP response status.



The following table lists all the triggers, tasks, and edge conditions used in **ExampleIntegration-EcomOrderProcessing** :

Component  | Configuration  | Description   
---|---|---  
[API trigger](https://docs.cloud.google.com/application-integration/docs/configure-api-trigger) (OrderProcessAPITrigger)  | **Trigger ID:**`api_trigger/ecom-order-processing_API_1` | Invokes the integration for every order request.   
[Data mapping task](https://docs.cloud.google.com/application-integration/docs/configure-data-mapping-task) (Find Total Order Price)  | Input  | Output  | Extracts the `order_request` JSON input variable and iterates through all the order items using the [FOR_EACH](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#foreach-function) mapping function to calculate the total order price value.  The total order price value is calculated by multiplying the item `quantity` and the `price_per_item` using the [GET_PROPERTY](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#get_property-function) and [MULTIPLY](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#multiply-function) mapping functions.  The final value is then converted to a double data type and stored in the `total_order_value` output variable.   
      
    
    orders_request.line_items
    .FOR_EACH(~obj1->~obj1
      .GET_PROPERTY("quantity")
      .TO_DOUBLE()
      .MULTIPLY(~obj1
        .GET_PROPERTY("price_per_unit")
        .TO_DOUBLE()))
    .TO_DOUBLE_ARRAY()
    .SUM()

| `total_order_value`  
[Edge condition](https://docs.cloud.google.com/application-integration/docs/edge-and-edge-conditions) (Total OrderValue Above Threshold)  | **Condition:**`$total_order_value$ >= $threshold_order_value$` | Checks if the total order value is greater than or equal to $100. If yes, then the control is passed to an Approval task.   
[Edge condition](https://docs.cloud.google.com/application-integration/docs/edge-and-edge-conditions) (TotalOrderValue Below Threshold)  | **Condition:**`$total_order_value$ < $threshold_order_value$` | Checks if the total order value is less than $100. If yes, then the control is passed to the Filter External Items task.   
[Approval task](https://docs.cloud.google.com/application-integration/docs/configure-approval-task) (Approval)  | **Recipients:** Enter the approver's email address For the purpose of testing this sample integration, you can use your email to confirm the successful completion of the integration.  **Note:** In your Google Cloud project, you must grant the **Application Integration Approver** IAM role to all the email addresses provided in the **Recipients** field. For information on granting IAM roles, see [Granting, changing, and revoking access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).  | Send an approval request email to one or more integration users. The email includes a link to the integration where the users can manually approve or reject the request.   
[Data mapping task](https://docs.cloud.google.com/application-integration/docs/configure-data-mapping-task) (Filter External Items)  | Input  | Output  | Extracts the `order_request` JSON input variable and filters all the order items with external vendors using the [FILTER](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#filter-function) mapping function.  The filtered values are then stored in the `filtered_external_items` output variable.   
      
    
    orders_request
    .GET_PROPERTY("line_items")
    .FILTER(~obj1->~obj1
      .GET_PROPERTY("vendor")
      .TO_STRING()
      .EQUALS("External"))

| `filtered_external_items`  
[For Each Loop task](https://docs.cloud.google.com/application-integration/docs/configure-for-each-loop-task) (For Each Loop)  | **List to iterate:** `filtered_external_items` **API Trigger ID:** `api_trigger/ecom-order-processing_API_2` **Integration name:**`ExampleIntegration-EcomOrderProcessing` | Iterates over the `filtered_external_items` variable and calls the sub-integration for each element in the array. It also collates the response of each run in `rest_call_response_status`, where each element of the array has the response from one particular run.   
[API trigger](https://docs.cloud.google.com/application-integration/docs/configure-api-trigger) (Report ExternalOrders)  | **Trigger ID:**`api_trigger/ecom-order-processing_API_2` | Invokes the sub-integration for each element in filtered_external_items.   
[Call REST Endpoint task](https://docs.cloud.google.com/application-integration/docs/configure-call-rest-endpoint-task) (Call REST Endpoint)  | **Endpoint base URL:**`https://mocktarget.apigee.net/echo` **HTTP method:** `POST` **Request body:**`sub_integration_input` | Makes a REST call to https://mocktarget.apigee.net/echo.   
  
##  Publish and test the sample integration 

To publish the integration click **Publish** in the integration editor toolbar.

Upon successfully publishing your integration, you can view and inspect the [execution logs](https://docs.cloud.google.com/application-integration/docs/integration-execution-logs) of the published integration. To view logs, click **![image showing the icon for execution logs](https://docs.cloud.google.com/static/application-integration/images/logs-icon.png)View execution logs for this integration**. The **Execution Logs** page appears.

###  Test from the integration editor 

Do the following to test the sample integration: 

  1. Click **Test** in the integration editor toolbar, and then select **OrderProcessAPITrigger**.

The **Test Integration** pane appears. 

  2. You are prompted to edit the `orders_request` input variable. For the purpose of this test, you can update the `quantity` value to `240`. The update `orders_request` input variable should look similar to the following: 
         
         {
               "order_no": "12345",
               "buyer_id": "raambo",
               "line_items": [
                 {
                   "line": 1,
                   "sku": "tr100",
                   "vendor": "Internal",
                   "quantity": 1,
                   "price_per_unit": 10
                 },
                 {
                   "line": 2,
                   "sku": "tbz",
                   "vendor": "External",
                   **"quantity" : 240,**
                   "price_per_unit": 1
                 }
               ]
             }
             

  3. Click **Test integration**.



Since the updated `orders_request` quantity is greater than **200** , the sample integration sends an approval request email to the email address specified in the **Recipients** field of the Approval task. The integration order operation will successfully complete once the approval is received. 

For more information about testing, see [Test and publish integrations](https://docs.cloud.google.com/application-integration/docs/test-publish-integrations).

Do the following to inspect the execution logs and to view the status and payload of the given integration: 

  1. In the integration editor, click **![image showing the icon for execution logs](https://docs.cloud.google.com/static/application-integration/images/logs-icon.png)View execution logs for this integration**. The **Execution Logs** page appears.
  2. On the **Execution Logs** page, you can view details about each attempt to run an integration. Each entry includes details for the execution attempt, including: 
     * Integration name
     * Execution ID
     * Status
     * Start time
     * Duration
     * Integration Version
     * Trigger ID
  3. Click the expander arrow (**>**) next to the executed integration to view an expanded list of tasks and variables in the integration, along with task status and variable payloads.



###  Test using a REST API call 

**Note:** The following test cases use `curl`, which typically comes pre-installed for Linux and macOS operating systems. If you don't have `curl`, you can download it from the `curl` [releases and downloads page](https://curl.haxx.se/download.html).

#### Test case 1: Send request with default inputs
    
    
      curl -X POST -H "Content-Type: application/json" -d '{"trigger_id":"api_trigger/ecom-order-processing_API_1"}' 'https://integrations.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/integrations/INTEGRATION_NAME:execute' -H "Authorization: Bearer $(gcloud auth print-access-token)"
    

#### Test case 2: Send request with custom inputs
    
    
      curl -X POST -H "Content-Type: application/json" -d '{ "triggerId": "api_trigger/ecom-order-processing_API_1", "inputParameters": { "orders_request": { "jsonValue": "{\n \"order_no\": \"12345\",\n \"buyer_id\": \"raambo\",\n \"line_items\": [{\n \"line\": 1.0,\n \"sku\": \"tr100\",\n \"vendor\": \"Internal\",\n \"quantity\": 1.0,\n \"price_per_unit\": 10.0\n }, {\n \"line\": 2.0,\n \"sku\": \"tbz\",\n \"vendor\": \"External\",\n \"quantity\": 24.0,\n \"price_per_unit\": 2.0\n }]\n}" } } }' 'https://integrations.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/integrations/INTEGRATION_NAME:execute' -H "Authorization: Bearer $(gcloud auth print-access-token)"
    

Replace the following: 

  * PROJECT_ID: The ID of your Google Cloud project.
  * LOCATION: The integration location. See [Application Integration locations](https://docs.cloud.google.com/application-integration/docs/locations).
  * INTEGRATION_NAME: Name of the integration.



#### Test output

The API returns the integration execution response containing all the integration output variable values. 

## Quotas and limits

For information about quotas and limits, see [Quotas and limits](https://docs.cloud.google.com/application-integration/docs/quotas).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
