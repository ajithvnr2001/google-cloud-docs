---
url: https://docs.cloud.google.com/dataflow/docs/guides/templates/create-template-udf/
title: Create user-defined functions for Dataflow templates \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:23:06.218377+00:00
---

# Create user-defined functions for Dataflow templates  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/templates/create-template-udf/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Create user-defined functions for Dataflow templates Stay organized with collections  Save and categorize content based on your preferences. 

Some [Google-provided Dataflow templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates) support user-defined functions (UDFs). UDFs let you extend the functionality of a template without modifying the template code.

## Overview

To create a UDF, you write a JavaScript function or Python function, depending on the template. You store the UDF code file in Cloud Storage and specify the location as a template parameter. For each input element, the template calls your function. The function transforms the element or performs other custom logic and returns the result back to the template.

For example, you might use a UDF to:

  * Reformat the input data to match a target schema.
  * Redact sensitive data.
  * Filter some elements from the output.



The input to the UDF function is a single data element, serialized as a JSON string. The function returns a serialized JSON string as output. The data format depends on the template. For example, in the [Pub/Sub Subscription to BigQuery](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/pubsub-subscription-to-bigquery) template, the input is the Pub/Sub message data serialized as a JSON object, and the output is a serialized JSON object representing a BigQuery table row. For more information, see the [documentation](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates) for each template.

## Run a template with a UDF

To run a template with a UDF, you specify the Cloud Storage location of the JavaScript file and the name of the function as template parameters.

**Note:** The relevant template parameter names depend on the template. See the documentation for each template.

With some Google-provided templates, you can also create the UDF directly in the Google Cloud console, as follows:

  1. Go to the Dataflow page in the Google Cloud console.

[Go to the Dataflow page](https://console.cloud.google.com/dataflow)

  2. Click _add_box_**Create job from template**.

  3. Select the Google-provided template that you want to run.

  4. Expand **Optional parameters**. If the template supports UDFs, it has a parameter for the Cloud Storage location of the UDF and another parameter for the function name.

  5. Next to the template parameter, click **Create UDF**.

**Note:** This button is not available for all templates. If this button is not visible, then create the UDF in a local file and upload the file to Cloud Storage.
  6. In the **Select or Create a User-Defined Function (UDF)** panel:

     1. Enter a filename. Example: `my_udf.js`.
     2. Select a Cloud Storage folder. Example: `gs://your-bucket/your-folder`.
     3. Use the inline code editor to write the function. The editor is pre-populated with boilerplate code that you can use as a starting point.
     4. Click **Create UDF**.

The Google Cloud console saves the UDF file and populates the Cloud Storage location.

     5. Enter your function's name in the corresponding field.




## Write a JavaScript UDF

The following code shows a no-op JavaScript UDF that you can start from:
    
    
    /*
     * @param {string} inJson input JSON message (stringified)
     * @return {?string} outJson output JSON message (stringified)
     */
    function process(inJson) {
      const obj = JSON.parse(inJson);
    
      // Example data transformations:
      // Add a field: obj.newField = 1;
      // Modify a field: obj.existingField = '';
      // Filter a record: return null;
    
      return JSON.stringify(obj);
    }
    

The JavaScript code runs on the [Nashorn JavaScript engine](https://github.com/openjdk/nashorn). We recommend testing your UDF on the Nashorn engine before deploying it. The Nashorn engine does not exactly match the Node.js implementation of JavaScript. A common problem is using `console.log()` or `Number.isNaN()`, neither of which is defined in the Nashorn engine.

You can test your UDF on Nashorn engine by using Cloud Shell, which has JDK 11 pre-installed. Launch Nashorn in interactive mode as follows:
    
    
    jjs --language=es6
    

In the Nashorn interactive shell, perform the following steps:

  1. Call `load` to load your UDF JavaScript file.
  2. Define an input JSON object depending on your pipeline's expected messages.
  3. Use the `JSON.stringify` function to serialize the input to a JSON string.
  4. Call your UDF function to process the JSON string.
  5. Call `JSON.parse` to deserialize the output.
  6. Verify the result.



Example:
    
    
    > load('my_udf.js')
    > var input = {"name":"user1"}
    > var output = process(JSON.stringify(input))
    > print(output)
    

## Write a Python UDF

The following code shows a no-op Python UDF that you can start from:
    
    
    import json
    def process(value):
      # Load the JSON string into a dictionary.
      data = json.loads(value)
    
      # Transform the data in some way.
      data['new_field'] = 'new_value'
    
      # Serialize the data back to JSON.
      return json.dumps(data)
    

Python UDFs support dependency packages that are standard to Python and Apache Beam. They can't use third-party packages.

## Error handling

Typically, when an error occurs during UDF execution, the error is written to a dead-letter location. The details depend on the template. For example, the [Pub/Sub Subscription to BigQuery](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/pubsub-subscription-to-bigquery) template creates an `_error_records` table and writes errors there. Runtime UDF errors can occur because of syntax errors or uncaught exceptions. To check for syntax errors, test your UDF locally.

You can programmatically throw an exception for an element that shouldn't be processed. In the case, the element is written to the dead-letter location, if the template supports one. For an example that shows this approach, see Route events.

## Example use cases

This section describes some common patterns for UDFs, based on real-world use cases.

### Enrich events

Use a UDF to enrich events with new fields for more contextual information.

Example:
    
    
     function process(inJson) {
      const data = JSON.parse(inJson);
    
      // Add new field to track data source
      data.source = "source1";
      return JSON.stringify(data);
    }
    

### Transform events

Use a UDF to transform the entire event format depending on what your destination expects.

The following example reverts a Cloud Logging log entry ([`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry)) to the original log string when available. (Depending on the log source, the original log string is sometimes populated in the `textPayload` field.) You might use this pattern to send the raw logs in their original format, instead of sending the entire `LogEntry` from Cloud Logging.
    
    
     function process(inJson) {
      const data = JSON.parse(inJson);
    
      if (data.textPayload) {
        return data.textPayload; // Return string value, and skip JSON.stringify
      }
     return JSON.stringify(obj);
    }
    

### Redact or remove event data

Use a UDF to redact or remove a part of the event.

The following example redacts the field name `sensitiveField` by replacing its value, and removes the field named `redundantField` entirely.
    
    
     function process(inJson) {
      const data = JSON.parse(inJson);
    
      // Normalize existing field values
      data.source = (data.source && data.source.toLowerCase()) || "unknown";
    
      // Redact existing field values
      if (data.sensitiveField) {
        data.sensitiveField = "REDACTED";
      }
    
      // Remove existing fields
      if (data.redundantField) {
        delete(data.redundantField);
      }
    
      return JSON.stringify(data);
    }
    

### Route events

Use a UDF to route events to separate destinations in the downstream sink.

The following example, based on the [Pub/Sub to Splunk](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/pubsub-to-splunk) template, routes each event to the correct Splunk index. It calls a user-defined local function to map events to indexes.
    
    
    function process(inJson) {
      const obj = JSON.parse(inJson);
      
      // Set index programmatically for data segregation in Splunk
      obj._metadata = {
        index: splunkIndexLookup(obj)
      }
      return JSON.stringify(obj);
    }  
    

The next example routes unrecognized events to the dead-letter queue, assuming the template supports a dead-letter queue. (For example, see the [Pub/Sub to JDBC](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/pubsub-to-jdbc) template.) You might use this pattern to filter out unexpected entries before writing to the destination.
    
    
     function process(inJson) {
      const data = JSON.parse(inJson);
    
      // Route unrecognized events to the deadletter topic
      if (!data.hasOwnProperty('severity')) {
        throw new Error("Unrecognized event. eventId='" + data.Id + "'");
      }
    
      return JSON.stringify(data);
    

### Filter events

Use a UDF to filter undesired or unrecognized events from the output.

The following example drops events where `data.severity` equals `"DEBUG"`.
    
    
     function process(inJson) {
      const data = JSON.parse(inJson);
    
      // Drop events with certain field values
      if (data.severity == "DEBUG") {
        return null;
      }
    
      return JSON.stringify(data);
    }
    

## What's next

  * [Google-provided templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates)
  * [Extend your Dataflow template with UDFs](https://cloud.google.com/blog/topics/developers-practitioners/extend-your-dataflow-template-with-udfs) (blog post)
  * [Example UDFs](https://github.com/GoogleCloudPlatform/DataflowTemplates/tree/main/v2/common/src/main/resources/udf-samples) (GitHub)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
