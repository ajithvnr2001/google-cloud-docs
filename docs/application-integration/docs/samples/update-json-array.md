---
url: https://docs.cloud.google.com/application-integration/docs/samples/update-json-array/
title: Update JSON array at a specified index \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:19:32.988051+00:00
---

# Update JSON array at a specified index  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/samples/update-json-array/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Samples ](https://docs.cloud.google.com/application-integration/docs/samples)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Update JSON array at a specified index

Using the Data Mapping task, update the value of a JSON array at a specified index using an input variable. Store the output in a new JSON variable. 

## Code sample
    
    
    {
      "triggerConfigs": [{
        "label": "API Trigger",
        "startTasks": [{
          "taskId": "1"
        }],
        "properties": {
          "Trigger name": "tkApplicationIntegrationSample1_API_1"
        },
        "triggerType": "API",
        "triggerNumber": "1",
        "triggerId": "api_trigger/tkApplicationIntegrationSample1_API_1"
      }],
      "taskConfigs": [{
        "task": "FieldMappingTask",
        "taskId": "1",
        "parameters": {
          "FieldMappingConfigTaskParameterKey": {
            "key": "FieldMappingConfigTaskParameterKey",
            "value": {
              "jsonValue": "{\n  \"@type\": \"type.googleapis.com/enterprise.crm.eventbus.proto.FieldMappingConfig\",\n  \"mappedFields\": [{\n    \"inputField\": {\n      \"fieldType\": \"JSON_VALUE\",\n      \"transformExpression\": {\n        \"initialValue\": {\n          \"referenceValue\": \"$jsonArray$\"\n        },\n        \"transformationFunctions\": [{\n          \"functionType\": {\n            \"jsonFunction\": {\n              \"functionName\": \"TO_STRING_ARRAY\"\n            }\n          }\n        }, {\n          \"functionType\": {\n            \"stringArrayFunction\": {\n              \"functionName\": \"SET\"\n            }\n          },\n          \"parameters\": [{\n            \"initialValue\": {\n              \"literalValue\": {\n                \"intValue\": \"2\"\n              }\n            }\n          }, {\n            \"initialValue\": {\n              \"referenceValue\": \"$jsonVar$\"\n            },\n            \"transformationFunctions\": [{\n              \"functionType\": {\n                \"jsonFunction\": {\n                  \"functionName\": \"TO_STRING\"\n                }\n              }\n            }]\n          }]\n        }, {\n          \"functionType\": {\n            \"stringArrayFunction\": {\n              \"functionName\": \"TO_JSON\"\n            }\n          }\n        }]\n      }\n    },\n    \"outputField\": {\n      \"referenceKey\": \"$outputJsonArray$\",\n      \"fieldType\": \"JSON_VALUE\",\n      \"cardinality\": \"OPTIONAL\"\n    }\n  }]\n}"
            }
          }
        },
        "taskExecutionStrategy": "WHEN_ALL_SUCCEED",
        "displayName": "Data Mapping"
      }],
      "integrationParameters": [{
        "key": "outputJsonArray",
        "dataType": "JSON_VALUE",
        "displayName": "outputJsonArray",
        "inputOutputType": "OUT",
        "jsonSchema": "{\n  \"$schema\": \"http://json-schema.org/draft-04/schema#\",\n  \"type\": \"array\",\n  \"items\": {\n    \"type\": \"object\",\n    \"properties\": {\n      \"prop1\": {\n        \"type\": \"string\"\n      }\n    }\n  }\n}"
      }, {
        "key": "jsonArray",
        "dataType": "JSON_VALUE",
        "defaultValue": {
          "jsonValue": "[{\n  \"prop1\": \"val11\"\n}, {\n  \"prop1\": \"val21\"\n}, {\n  \"prop1\": \"val31\"\n}, {\n  \"prop1\": \"val41\"\n}]"
        },
        "displayName": "jsonArray",
        "jsonSchema": "{\n  \"$schema\": \"http://json-schema.org/draft-04/schema#\",\n  \"type\": \"array\",\n  \"items\": {\n    \"type\": \"object\",\n    \"properties\": {\n      \"prop1\": {\n        \"type\": \"string\"\n      }\n    }\n  }\n}"
      }, {
        "key": "jsonVar",
        "dataType": "JSON_VALUE",
        "defaultValue": {
          "jsonValue": "{\n  \"prop1\": \"valUserDefined\"\n}"
        },
        "displayName": "jsonVar",
        "jsonSchema": "{\n  \"$schema\": \"http://json-schema.org/draft-04/schema#\",\n  \"type\": \"object\",\n  \"properties\": {\n    \"prop1\": {\n      \"type\": \"string\"\n    }\n  }\n}"
      }]
    }

### Sample integration flow

The following image shows a sample layout of the integration editor for this integration code sample.

![image showing the sample integration flow](https://raw.githubusercontent.com/GoogleCloudPlatform/application-integration-samples/HEAD/src/update-json-array/update-json-array-flow.png)![image showing the sample integration flow](https://raw.githubusercontent.com/GoogleCloudPlatform/application-integration-samples/HEAD/src/update-json-array/update-json-array-flow.png)

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

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
