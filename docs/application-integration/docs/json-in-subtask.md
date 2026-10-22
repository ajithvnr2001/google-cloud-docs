---
url: https://docs.cloud.google.com/application-integration/docs/json-in-subtask/
title: Handle JSON payloads as strings in HTTP Connectors task \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:57.962372+00:00
---

# Handle JSON payloads as strings in HTTP Connectors task  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/json-in-subtask/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Handle JSON payloads as strings in HTTP Connectors task

In this tutorial, you learn how to handle JSON payloads when you use an **HTTP Connectors** task in Application Integration.

Incorrectly treating the payload can cause APIs to misinterpret it, resulting in `400 Bad Request` errors. To ensure APIs receive and parse your JSON payload correctly, treat the JSON payload as a string and explicitly set the `Content-Type` header to `application/json`.

## Before you begin

  * Verify you can access [Application Integration](https://docs.cloud.google.com/application-integration/docs/setup-application-integration).
  * Select your Google Cloud project and complete the following tasks:

    * Grant the following roles to the service account that you want to use to create the connection: 
      * `roles/secretmanager.viewer`
      * `roles/secretmanager.secretAccessor`
    * Enable the following services: 
      * `secretmanager.googleapis.com` (Secret Manager API)
      * `connectors.googleapis.com` (Connectors API)

If you haven't enabled these services for your project, the **Create Connection** page prompts you to enable them when you create the connection.

  * Add and configure an [HTTP Connectors](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task) task.
  * Add and configure the [Data Transformer task](https://docs.cloud.google.com/application-integration/docs/configure-data-transformer-script-task) to prepare the JSON payload and headers.



## Handle JSON payloads as strings

To handle JSON payloads that contain special characters when you use an **HTTP Connectors** task, complete the following steps:

  * Create a string variable for the JSON payload
  * Map the string variable to the connector input body
  * Add a custom Content-Type header
  * Execute the HTTP Connectors task



### Create a string variable for the JSON payload

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. In the navigation menu, click **Integrations**.
  3. Select an existing integration or [create a new one](https://docs.cloud.google.com/application-integration/docs/setup-application-integration). Ensure your integration includes the configured **HTTP Connectors** and **Data Transformer** tasks as detailed in the Before you begin section.
  4. In the _integration editor_ , click add **Create** to open the **Create variable** dialog.
  5. In the **Create variable** dialog: 
     1. Enter the following information: 
        1. **Name:** Enter a name, for example, `jsonPayloadString`.
        2. **Data Type:** Select **String**.
        3. **Default Value:**
           * If the JSON payload is populated by a preceding task in the integration flow, for example, another [Data Transformer](https://docs.cloud.google.com/application-integration/docs/configure-data-transformer-script-task) task, leave this field empty. The variable will be populated dynamically based on the output of previous tasks in the integration.
           * If the JSON payload is not populated by a preceding task, you must provide a static default JSON payload. Enter the JSON structure as a single string in this field. 

Here are two examples of how to enter JSON strings in the **Default Value** field:

**Without special characters** : To represent the JSON `{"name": "Developer", "key": "test"}`, enter exactly: `{ "name": "Developer", "key": "test" }`.

**With special characters** : When your JSON contains special characters like newline (`\n`), you must escape them. For example, to represent the JSON `{"key": "value1\nvalue2"}`, enter `{"key": "value1\\nvalue2"}` in the field.

     2. Click **Create**. 
![Create a string variable for the JSON payload](https://docs.cloud.google.com/static/application-integration/images/string.png)
For more information on creating and using variables, see [Variables](https://docs.cloud.google.com/application-integration/docs/variables). 


### Map the string variable to the connector input body

In the **Data Transformer Editor** , map the `jsonPayloadString` variable to the **connectorInputPayload.Body** field.

  1. In your integration, add a [Data Transformer task](https://docs.cloud.google.com/application-integration/docs/configure-data-transformer-script-task).
  2. Open the **Data Transformer Editor**. You can use either the **Diagram mode** or the **Script mode**.
  3. To map the variable: 
     * **Diagram mode:** Add `jsonPayloadString` as an input and map it to the **connectorInputPayload.Body** output field.
     * **Script mode:** Write Jsonnet code to assign the value: `connectorInputPayload.Body = vars.jsonPayloadString;`.



### Add a custom Content-Type header

  1. In the **Data Transformer Editor** , add a mapping for custom headers to the **connectorInputPayload.Headers** field. 
     * **Diagram mode:** Add a constant input with the value `{"Content-Type": "application/json"}` and map it to **connectorInputPayload.Headers**.
     * **Script mode:** Add the following Jsonnet to set the header: 
           
           connectorInputPayload.Headers = {
             "Content-Type": "application/json"
           };
                   




### Execute the HTTP Connectors task

Before executing your integration, verify that `connectorInputPayload.Body` is populated by the `jsonPayloadString` variable and that `connectorInputPayload.Headers` includes the `Content-Type: application/json` header. This setup ensures the **HTTP Connectors** task sends the JSON payload as a string with the correct `Content-Type` in the **Data Transformer** task.

Run your integration to test the API request. If the API returns a `400 Bad Request` error, verify the mappings for `connectorInputPayload.Body` and `connectorInputPayload.Headers` again in the **Data Transformer** task.

## What's next

Try building integrations with other connectors. For a list of all supported connectors, see [ Connector reference](https://docs.cloud.google.com/integration-connectors/docs/connector-reference-overview).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
