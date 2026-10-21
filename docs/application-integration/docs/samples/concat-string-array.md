---
url: https://docs.cloud.google.com/application-integration/docs/samples/concat-string-array/
title: Concat a string to a string array \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:41:59.180833+00:00
---

# Concat a string to a string array  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/samples/concat-string-array/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Samples ](https://docs.cloud.google.com/application-integration/docs/samples)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Concat a string to a string array

Using the Data Mapping task, iterate through the elements of a string array and apply transformation functions to concat a string value to all the array elements. 

## Code sample
    
    
    {
      "triggerConfigs": [{
        "label": "API Trigger",
        "startTasks": [{
          "taskId": "1"
        }],
        "properties": {
          "Trigger name": "tkApplicationIntegrationSample2_API_1"
        },
        "triggerType": "API",
        "triggerNumber": "1",
        "triggerId": "api_trigger/tkApplicationIntegrationSample2_API_1"
      }],
      "taskConfigs": [{
        "task": "FieldMappingTask",
        "taskId": "1",
        "parameters": {
          "FieldMappingConfigTaskParameterKey": {
            "key": "FieldMappingConfigTaskParameterKey",
            "value": {
              "jsonValue": "{\n  \"@type\": \"type.googleapis.com/enterprise.crm.eventbus.proto.FieldMappingConfig\",\n  \"mappedFields\": [{\n    \"inputField\": {\n      \"fieldType\": \"STRING_ARRAY\",\n      \"transformExpression\": {\n        \"initialValue\": {\n          \"referenceValue\": \"$stringArray$\"\n        },\n        \"transformationFunctions\": [{\n          \"functionType\": {\n            \"stringArrayFunction\": {\n              \"functionName\": \"FOR_EACH\"\n            }\n          },\n          \"parameters\": [{\n            \"initialValue\": {\n              \"literalValue\": {\n                \"protoValue\": {\n                  \"@type\": \"type.googleapis.com/enterprise.crm.eventbus.proto.TransformExpression\",\n                  \"initialValue\": {\n                    \"referenceValue\": \"~x\"\n                  },\n                  \"transformationFunctions\": [{\n                    \"functionType\": {\n                      \"stringFunction\": {\n                        \"functionName\": \"CONCAT\"\n                      }\n                    },\n                    \"parameters\": [{\n                      \"initialValue\": {\n                        \"referenceValue\": \"$textToAppend$\"\n                      }\n                    }]\n                  }]\n                }\n              }\n            }\n          }]\n        }, {\n          \"functionType\": {\n            \"jsonFunction\": {\n              \"functionName\": \"TO_STRING_ARRAY\"\n            }\n          }\n        }]\n      }\n    },\n    \"outputField\": {\n      \"referenceKey\": \"$stringArray$\",\n      \"fieldType\": \"STRING_ARRAY\",\n      \"cardinality\": \"OPTIONAL\"\n    }\n  }]\n}"
            }
          }
        },
        "taskExecutionStrategy": "WHEN_ALL_SUCCEED",
        "displayName": "Data Mapping"
      }],
      "integrationParameters": [{
        "key": "stringArray",
        "dataType": "STRING_ARRAY",
        "defaultValue": {
          "stringArray": {
            "stringValues": ["oranges", "apples", "bananas", "mangos"]
          }
        },
        "displayName": "stringArray",
        "inputOutputType": "OUT"
      }, {
        "key": "textToAppend",
        "dataType": "STRING_VALUE",
        "defaultValue": {
          "stringValue": "AreGreatFruits"
        },
        "displayName": "textToAppend"
      }]
    }

### Sample integration flow

The following image shows a sample layout of the integration editor for this integration code sample.

![image showing the sample integration flow](https://raw.githubusercontent.com/GoogleCloudPlatform/application-integration-samples/HEAD/src/concat-string-array/concat-string-array-flow.png)![image showing the sample integration flow](https://raw.githubusercontent.com/GoogleCloudPlatform/application-integration-samples/HEAD/src/concat-string-array/concat-string-array-flow.png)

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
