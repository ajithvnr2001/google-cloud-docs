---
url: https://docs.cloud.google.com/application-integration/docs/samples/resolve-json/
title: Resolve a JSON reference \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:31:59.138900+00:00
---

# Resolve a JSON reference  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/samples/resolve-json/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Samples ](https://docs.cloud.google.com/application-integration/docs/samples)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Resolve a JSON reference

Using the Data Mapping task, resolve a JSON reference in a template JSON that contains a $variable$ reference. Store the output in a new JSON variable. 

## Code sample
    
    
    {
      "triggerConfigs": [{
        "label": "API Trigger",
        "startTasks": [{
          "taskId": "1"
        }],
        "properties": {
          "Trigger name": "json_structure_mapping_API_1"
        },
        "triggerType": "API",
        "triggerNumber": "1",
        "triggerId": "api_trigger/json_structure_mapping_API_1"
      }],
      "taskConfigs": [{
        "task": "FieldMappingTask",
        "taskId": "1",
        "parameters": {
          "FieldMappingConfigTaskParameterKey": {
            "key": "FieldMappingConfigTaskParameterKey",
            "value": {
              "jsonValue": "{\n  \"@type\": \"type.googleapis.com/enterprise.crm.eventbus.proto.FieldMappingConfig\",\n  \"mappedFields\": [{\n    \"inputField\": {\n      \"fieldType\": \"JSON_VALUE\",\n      \"transformExpression\": {\n        \"initialValue\": {\n          \"referenceValue\": \"$new_structure_json_template$\"\n        },\n        \"transformationFunctions\": [{\n          \"functionType\": {\n            \"stringFunction\": {\n              \"functionName\": \"RESOLVE_TEMPLATE\"\n            }\n          }\n        }, {\n          \"functionType\": {\n            \"stringFunction\": {\n              \"functionName\": \"TO_JSON\"\n            }\n          }\n        }]\n      }\n    },\n    \"outputField\": {\n      \"referenceKey\": \"$output_order_json$\",\n      \"fieldType\": \"JSON_VALUE\",\n      \"cardinality\": \"OPTIONAL\"\n    }\n  }]\n}"
            }
          }
        },
        "taskExecutionStrategy": "WHEN_ALL_SUCCEED",
        "displayName": "Data Mapping"
      }],
      "integrationParameters": [{
        "key": "output_order_json",
        "dataType": "JSON_VALUE",
        "displayName": "output_order_json",
        "inputOutputType": "OUT"
      }, {
        "key": "new_structure_json_template",
        "dataType": "STRING_VALUE",
        "defaultValue": {
          "stringValue": "{\n\t\"order\": {\n\t\t\"ordDate\": \"$input_order_json.orderDate$\",\n\t\t\"orderID\": \"$input_order_json.orderNum$\",\n\t\t\"btAddr\": {\n\t\t\t\"btAddr\": \"$input_order_json.billTo.street$ $input_order_json.billTo.city$ $input_order_json.billTo.state$ $input_order_json.billTo.zipCode$\",\n\t\t\t\"btCode\": \"$input_order_json.billTo.billToCode$\"\n\t\t},\n\"stAddr\": {\n\t\t\t\"stAddress\": \"$input_order_json.shipTo.street$ $input_order_json.shipTo.city$ $input_order_json.shipTo.state$ $input_order_json.shipTo.zipCode$\",\n\t\t\t\"stCode\": \"$input_order_json.shipTo.shipToCode$\"\n\t\t}\n\t}\n}"
        },
        "displayName": "new_structure_json_template"
      }, {
        "key": "input_order_json",
        "dataType": "JSON_VALUE",
        "defaultValue": {
          "jsonValue": "{\n  \"orderNum\": \"123\",\n  \"orderDate\": \"29/5/2022\",\n  \"shipTo\": {\n    \"shipToCode\": \"CX3H-XC Sunnyvale, California\",\n    \"street\": \"1155 Borregas Ave\",\n    \"city\": \"Sunnyvale\",\n    \"state\": \"CA\",\n    \"zipCode\": \"94089\"\n  },\n  \"billTo\": {\n    \"billToCode\": \"CX3H+XC Sunnyvale, California\",\n    \"street\": \"1155 Borregas Ave\",\n    \"city\": \"Sunnyvale\",\n    \"state\": \"CA\",\n    \"zipCode\": \"94089\"\n  }\n}"
        },
        "displayName": "input_order_json",
        "jsonSchema": "{\n  \"$schema\": \"http://json-schema.org/draft-04/schema#\",\n  \"type\": \"object\",\n  \"properties\": {\n    \"billTo\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"zipCode\": {\n          \"type\": \"string\"\n        },\n        \"city\": {\n          \"type\": \"string\"\n        },\n        \"street\": {\n          \"type\": \"string\"\n        },\n        \"state\": {\n          \"type\": \"string\"\n        },\n        \"billToCode\": {\n          \"type\": \"string\"\n        }\n      }\n    },\n    \"orderNum\": {\n      \"type\": \"string\"\n    },\n    \"orderDate\": {\n      \"type\": \"string\"\n    },\n    \"shipTo\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"zipCode\": {\n          \"type\": \"string\"\n        },\n        \"city\": {\n          \"type\": \"string\"\n        },\n        \"street\": {\n          \"type\": \"string\"\n        },\n        \"shipToCode\": {\n          \"type\": \"string\"\n        },\n        \"state\": {\n          \"type\": \"string\"\n        }\n      }\n    }\n  }\n}"
      }]
    }

### Sample integration flow

The following image shows a sample layout of the integration editor for this integration code sample.

![image showing the sample integration flow](https://raw.githubusercontent.com/GoogleCloudPlatform/application-integration-samples/HEAD/src/resolve-json/resolve-json-flow.png)![image showing the sample integration flow](https://raw.githubusercontent.com/GoogleCloudPlatform/application-integration-samples/HEAD/src/resolve-json/resolve-json-flow.png)

## Upload and run the sample integration

To upload and run the sample integration, do the following steps:

  1. Save the integration sample as a .json file on your system.
  2. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  3. Click **Integrations** from the left navigation menu to open the **Integrations** page. 
  4. Select an existing integration or create a new integration by clicking **Create integration**.

If you are creating a new integration: 

     1. Enter a name and description in the **Create Integration** dialog.
     2. Select a region for the integration. **Note:** The **Regions** dropdown only lists the regions provisioned in your Google Cloud project. To provision a new region, Click **Enable Region**. See [Enable new region](https://docs.cloud.google.com/application-integration/docs/enable-new-region) for more information. 
     3. Select a service account for the integration. You can change or update the service account details of an integration any time from the info **Integration summary** pane in the integration toolbar. **Note:** The option to select a service account is displayed only if you have enabled integration governance for the selected region. 
     4. Click **Create**.

This opens the integration in the _integration editor_.

  5. In the _integration editor_ , click publish**Upload/download menu** and then select **Upload integration**.
  6. In the file browser dialog, select the file that you saved in step 1, and then click **Open**. 

A new version of the integration is created using the uploaded file.

  7. In the _integration editor_ , click **Test**. 
  8. Click **Test integration**. This runs the integration and displays the execution result in the **Test Integration** pane.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
