---
url: https://docs.cloud.google.com/application-integration/docs/samples/use-vertex-ai-embedded-genai/
title: Use the Vertex AI task to embed GenAI \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:19:50.713754+00:00
---

# Use the Vertex AI task to embed GenAI  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/samples/use-vertex-ai-embedded-genai/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Samples ](https://docs.cloud.google.com/application-integration/docs/samples)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Use the Vertex AI task to embed GenAI

This sample integration contains a flow to be used as a sub-integration for interacting with Google Cloud Vertex AI models. Before using the following code sample, ensure that all [prerequisites](https://github.com/GoogleCloudPlatform/application-integration-samples/tree/1391362afa2dbcd35d1de6805ebf940107fa6dc9/src/vertex-ai-task#prerequisites) are met. 

## Code sample
    
    
    {
      "triggerConfigs": [
        {
          "label": "API Trigger",
          "startTasks": [
            {
              "taskId": "1"
            }
          ],
          "properties": {
            "Trigger name": "vertex-ai-task_API_1"
          },
          "triggerType": "API",
          "triggerNumber": "1",
          "triggerId": "api_trigger/vertex-ai-task_API_1",
          "description": "As inputs, we are only adding TextPrompt and ModelId. You can set Model ID for different Google models, such as text-bison, chat-bison, etc.",
          "position": {
            "x": -210
          }
        }
      ],
      "taskConfigs": [
        {
          "task": "Vertex AI - Predict",
          "taskId": "4",
          "parameters": {
            "request": {
              "key": "request",
              "value": {
                "stringValue": "$`Task_4_request`$"
              }
            },
            "projectsId": {
              "key": "projectsId",
              "value": {
                "stringValue": "$ProjectId$"
              }
            },
            "endpoint": {
              "key": "endpoint",
              "value": {
                "stringValue": "$endpoint$"
              }
            },
            "locationsId": {
              "key": "locationsId",
              "value": {
                "stringValue": "$Region$"
              }
            },
            "response": {
              "key": "response",
              "value": {
                "stringArray": {
                  "stringValues": [
                    "$`Task_4_response`$"
                  ]
                }
              }
            },
            "taskTemplateId": {
              "key": "taskTemplateId",
              "value": {
                "stringValue": "2b5513a2-f3f4-4ac6-918e-8ea55b53cbb8"
              }
            }
          },
          "nextTasks": [
            {
              "taskId": "3"
            }
          ],
          "taskExecutionStrategy": "WHEN_ALL_SUCCEED",
          "displayName": "Vertex AI - Predict (Preview)",
          "description": "This is the actual Vertex AI API call with the variables we\u0027ve previously setup. Notice that under authentication, you need to have a Service Account with Vertex AI Predict IAM permissions.",
          "taskTemplate": "Vertex AI - Predict",
          "externalTaskType": "NORMAL_TASK",
          "position": {
            "x": -208,
            "y": 256
          }
        },
        {
          "task": "FieldMappingTask",
          "taskId": "1",
          "parameters": {
            "FieldMappingConfigTaskParameterKey": {
              "key": "FieldMappingConfigTaskParameterKey",
              "value": {
                "jsonValue": "{\n  \"@type\": \"type.googleapis.com/enterprise.crm.eventbus.proto.FieldMappingConfig\",\n  \"mappedFields\": [{\n    \"inputField\": {\n      \"fieldType\": \"STRING_VALUE\",\n      \"transformExpression\": {\n        \"initialValue\": {\n          \"baseFunction\": {\n            \"functionType\": {\n              \"baseFunction\": {\n                \"functionName\": \"GET_PROJECT_ID\"\n              }\n            }\n          }\n        }\n      }\n    },\n    \"outputField\": {\n      \"referenceKey\": \"$ProjectId$\",\n      \"fieldType\": \"STRING_VALUE\",\n      \"cardinality\": \"OPTIONAL\"\n    }\n  }, {\n    \"inputField\": {\n      \"fieldType\": \"STRING_VALUE\",\n      \"transformExpression\": {\n        \"initialValue\": {\n          \"baseFunction\": {\n            \"functionType\": {\n              \"baseFunction\": {\n                \"functionName\": \"GET_REGION\"\n              }\n            }\n          }\n        }\n      }\n    },\n    \"outputField\": {\n      \"referenceKey\": \"$Region$\",\n      \"fieldType\": \"STRING_VALUE\",\n      \"cardinality\": \"OPTIONAL\"\n    }\n  }, {\n    \"inputField\": {\n      \"fieldType\": \"STRING_VALUE\",\n      \"transformExpression\": {\n        \"initialValue\": {\n          \"referenceValue\": \"$endpoint$\"\n        },\n        \"transformationFunctions\": [{\n          \"functionType\": {\n            \"stringFunction\": {\n              \"functionName\": \"CONCAT\"\n            }\n          },\n          \"parameters\": [{\n            \"initialValue\": {\n              \"referenceValue\": \"$ModelId$\"\n            }\n          }]\n        }]\n      }\n    },\n    \"outputField\": {\n      \"referenceKey\": \"$endpoint$\",\n      \"fieldType\": \"STRING_VALUE\",\n      \"cardinality\": \"OPTIONAL\"\n    }\n  }, {\n    \"inputField\": {\n      \"fieldType\": \"JSON_VALUE\",\n      \"transformExpression\": {\n        \"initialValue\": {\n          \"referenceValue\": \"$PalmPromptRequest$\"\n        },\n        \"transformationFunctions\": [{\n          \"functionType\": {\n            \"jsonFunction\": {\n              \"functionName\": \"RESOLVE_TEMPLATE\"\n            }\n          }\n        }]\n      }\n    },\n    \"outputField\": {\n      \"referenceKey\": \"$`Task_4_request`$\",\n      \"fieldType\": \"JSON_VALUE\",\n      \"cardinality\": \"OPTIONAL\"\n    }\n  }]\n}"
              }
            }
          },
          "nextTasks": [
            {
              "taskId": "4"
            }
          ],
          "taskExecutionStrategy": "WHEN_ALL_SUCCEED",
          "displayName": "Set Prompt Parameters",
          "description": "In here, we are setting the required variables for the Vertex AI task. The actual payload is set using the resolve_template function from a pre-defined Local Variable called PalmPromptRequest.",
          "externalTaskType": "NORMAL_TASK",
          "position": {
            "x": -210,
            "y": 126
          }
        },
        {
          "task": "FieldMappingTask",
          "taskId": "3",
          "parameters": {
            "FieldMappingConfigTaskParameterKey": {
              "key": "FieldMappingConfigTaskParameterKey",
              "value": {
                "jsonValue": "{\n  \"@type\": \"type.googleapis.com/enterprise.crm.eventbus.proto.FieldMappingConfig\",\n  \"mappedFields\": [{\n    \"inputField\": {\n      \"fieldType\": \"JSON_VALUE\",\n      \"transformExpression\": {\n        \"initialValue\": {\n          \"referenceValue\": \"$`Task_4_response`.predictions$\"\n        },\n        \"transformationFunctions\": [{\n          \"functionType\": {\n            \"jsonFunction\": {\n              \"functionName\": \"GET_ELEMENT\"\n            }\n          },\n          \"parameters\": [{\n            \"initialValue\": {\n              \"literalValue\": {\n                \"intValue\": \"0\"\n              }\n            }\n          }]\n        }, {\n          \"functionType\": {\n            \"jsonFunction\": {\n              \"functionName\": \"GET_PROPERTY\"\n            }\n          },\n          \"parameters\": [{\n            \"initialValue\": {\n              \"literalValue\": {\n                \"stringValue\": \"content\"\n              }\n            }\n          }]\n        }]\n      }\n    },\n    \"outputField\": {\n      \"referenceKey\": \"$Content$\",\n      \"fieldType\": \"STRING_VALUE\",\n      \"cardinality\": \"OPTIONAL\"\n    }\n  }]\n}"
              }
            }
          },
          "taskExecutionStrategy": "WHEN_ALL_SUCCEED",
          "displayName": "Map Prompt Response",
          "description": "Finally, we are mapping just the content of the Vertex AI task output as the final integration Output. ",
          "externalTaskType": "NORMAL_TASK",
          "position": {
            "x": -210,
            "y": 378
          }
        }
      ],
      "integrationParameters": [
        {
          "key": "TextPrompt",
          "dataType": "STRING_VALUE",
          "displayName": "TextPrompt",
          "inputOutputType": "IN"
        },
        {
          "key": "Region",
          "dataType": "STRING_VALUE",
          "defaultValue": {
            "stringValue": "us-central1"
          },
          "displayName": "Region"
        },
        {
          "key": "ProjectId",
          "dataType": "STRING_VALUE",
          "displayName": "ProjectId"
        },
        {
          "key": "`Task_4_request`",
          "dataType": "JSON_VALUE",
          "defaultValue": {
            "jsonValue": "{\n}"
          },
          "displayName": "`Task_4_request`",
          "isTransient": true,
          "producer": "1_4",
          "jsonSchema": "{\n  \"$schema\": \"http://json-schema.org/draft-07/schema#\",\n  \"type\": \"object\",\n  \"properties\": {\n    \"instances\": {\n      \"type\": \"array\"\n    },\n    \"parameters\": {\n      \"type\": \"object\"\n    }\n  }\n}"
        },
        {
          "key": "`Task_4_response`",
          "dataType": "JSON_VALUE",
          "displayName": "`Task_4_response`",
          "isTransient": true,
          "producer": "1_4",
          "jsonSchema": "{\n  \"$schema\": \"http://json-schema.org/draft-07/schema#\",\n  \"type\": \"object\",\n  \"properties\": {\n    \"deployedModelId\": {\n      \"type\": \"string\"\n    },\n    \"modelVersionId\": {\n      \"type\": \"string\"\n    },\n    \"model\": {\n      \"type\": \"string\"\n    },\n    \"predictions\": {\n      \"type\": \"array\"\n    },\n    \"modelDisplayName\": {\n      \"type\": \"string\"\n    }\n  }\n}"
        },
        {
          "key": "ModelId",
          "dataType": "STRING_VALUE",
          "defaultValue": {
            "stringValue": "text-bison@001"
          },
          "displayName": "ModelId",
          "inputOutputType": "IN"
        },
        {
          "key": "endpoint",
          "dataType": "STRING_VALUE",
          "defaultValue": {
            "stringValue": "publishers/google/models/"
          },
          "displayName": "endpoint"
        },
        {
          "key": "PalmPromptRequest",
          "dataType": "JSON_VALUE",
          "defaultValue": {
            "jsonValue": "{\n  \"instances\": [{\n    \"prompt\": \"$TextPrompt$\"\n  }],\n  \"parameters\": {\n    \"temperature\": 0.2,\n    \"maxOutputTokens\": 768.0,\n    \"topP\": 0.8,\n    \"topK\": 40.0\n  }\n}"
          },
          "displayName": "PalmPromptRequest",
          "jsonSchema": "{\n  \"$schema\": \"http://json-schema.org/draft-04/schema#\",\n  \"type\": \"object\",\n  \"properties\": {\n    \"instances\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"prompt\": {\n            \"type\": \"string\"\n          }\n        }\n      }\n    },\n    \"parameters\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"topK\": {\n          \"type\": \"number\"\n        },\n        \"temperature\": {\n          \"type\": \"number\"\n        },\n        \"maxOutputTokens\": {\n          \"type\": \"number\"\n        },\n        \"topP\": {\n          \"type\": \"number\"\n        }\n      }\n    }\n  }\n}"
        },
        {
          "key": "Content",
          "dataType": "STRING_VALUE",
          "displayName": "Content",
          "inputOutputType": "OUT"
        }
      ]
    }

### Sample integration flow

The following image shows a sample layout of the integration editor for this integration code sample.

![image showing the sample integration flow](https://raw.githubusercontent.com/GoogleCloudPlatform/application-integration-samples/HEAD/src/vertex-ai-task/vertex-ai-task.png)![image showing the sample integration flow](https://raw.githubusercontent.com/GoogleCloudPlatform/application-integration-samples/HEAD/src/vertex-ai-task/vertex-ai-task.png)

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
