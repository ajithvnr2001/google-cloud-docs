---
url: https://docs.cloud.google.com/application-integration/docs/samples/foreach-loop-send-email/
title: Invoke a sub-integration to send an email \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:26:03.330520+00:00
---

# Invoke a sub-integration to send an email  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/samples/foreach-loop-send-email/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Samples ](https://docs.cloud.google.com/application-integration/docs/samples)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Invoke a sub-integration to send an email

Using the For Each Loop task, invoke a sub-integration that takes input from the main integration to send email notifications. 

## Code sample: Sub-integration
    
    
    {
      "triggerConfigs": [{
        "label": "API Trigger",
        "startTasks": [{
          "taskId": "1"
        }],
        "properties": {
          "Trigger name": "SubIntegrationSendEmailDemo_API_1"
        },
        "triggerType": "API",
        "triggerNumber": "1",
        "triggerId": "api_trigger/SubIntegrationSendEmailDemo_API_1"
      }],
      "taskConfigs": [{
        "task": "EmailTask",
        "taskId": "1",
        "parameters": {
          "Cc": {
            "key": "Cc",
            "value": {
              "stringArray": {
              }
            }
          },
          "TextBody": {
            "key": "TextBody",
            "value": {
              "stringValue": "$EmailContent$"
            }
          },
          "Bcc": {
            "key": "Bcc",
            "value": {
              "stringArray": {
              }
            }
          },
          "AttachmentPath": {
            "key": "AttachmentPath",
            "value": {
              "stringArray": {
              }
            }
          },
          "To": {
            "key": "To",
            "value": {
              "stringArray": {
                "stringValues": ["$Recipients$"]
              }
            }
          },
          "BodyFormat": {
            "key": "BodyFormat",
            "value": {
              "stringValue": "text"
            }
          },
          "EmailConfigInput": {
            "key": "EmailConfigInput",
            "value": {
              "jsonValue": "{\n  \"@type\": \"type.googleapis.com/enterprise.crm.eventbus.proto.EmailConfig\"\n}"
            }
          },
          "Subject": {
            "key": "Subject",
            "value": {
              "stringValue": "$Email_Subject$"
            }
          }
        },
        "taskExecutionStrategy": "WHEN_ALL_SUCCEED",
        "displayName": "Send Email"
      }],
      "integrationParameters": [{
        "key": "EmailContent",
        "dataType": "STRING_VALUE",
        "defaultValue": {
          "stringValue": ""
        },
        "displayName": "EmailContent",
        "inputOutputType": "IN"
      }, {
        "key": "Recipients",
        "dataType": "STRING_VALUE",
        "defaultValue": {
          "stringValue": ""
        },
        "displayName": "Recipients",
        "inputOutputType": "IN"
      }, {
        "key": "Email_Subject",
        "dataType": "STRING_VALUE",
        "defaultValue": {
          "stringValue": ""
        },
        "displayName": "Email_Subject",
        "inputOutputType": "IN"
      }]
    }

## Code sample: Main Integration
    
    
    {
      "triggerConfigs": [{
        "label": "API Trigger",
        "startTasks": [{
          "taskId": "1"
        }],
        "properties": {
          "Trigger name": "ForEachLoopDemo_API_1"
        },
        "triggerType": "API",
        "triggerNumber": "1",
        "triggerId": "api_trigger/ForEachLoopDemo_API_1"
      }],
      "taskConfigs": [{
        "task": "SubWorkflowForEachLoopV2Task",
        "taskId": "1",
        "parameters": {
          "iterationElementMapping": {
            "key": "iterationElementMapping",
            "value": {
              "stringValue": "EmailContent"
            }
          },
          "aggregatorParameterMapping": {
            "key": "aggregatorParameterMapping"
          },
          "triggerId": {
            "key": "triggerId",
            "value": {
              "stringValue": "api_trigger/SubIntegrationSendEmailDemo_API_1"
            }
          },
          "loopMetadata": {
            "key": "loopMetadata",
            "value": {
              "stringArray": {
                "stringValues": ["$`Task_1_loopMetadata`$"]
              }
            }
          },
          "disableEucPropagation": {
            "key": "disableEucPropagation",
            "value": {
              "booleanValue": false
            }
          },
          "listToIterate": {
            "key": "listToIterate",
            "value": {
              "stringValue": "$ListOfEmailContent$"
            }
          },
          "workflowName": {
            "key": "workflowName",
            "value": {
              "stringValue": "SubIntegrationSendEmailDemo"
            }
          },
          "requestParameterMapping": {
            "key": "requestParameterMapping",
            "value": {
              "jsonValue": "{\n  \"@type\": \"type.googleapis.com/enterprise.crm.eventbus.proto.ParameterMap\",\n  \"entries\": [{\n    \"key\": {\n      \"literalValue\": {\n        \"stringValue\": \"Recipients\"\n      }\n    },\n    \"value\": {\n      \"literalValue\": {\n        \"stringValue\": \"Recipients\"\n      }\n    }\n  }, {\n    \"key\": {\n      \"literalValue\": {\n        \"stringValue\": \"Email_Subject\"\n      }\n    },\n    \"value\": {\n      \"literalValue\": {\n        \"stringValue\": \"Email_Subject\"\n      }\n    }\n  }]\n}"
            }
          },
          "overrideParameterMapping": {
            "key": "overrideParameterMapping"
          }
        },
        "taskExecutionStrategy": "WHEN_ALL_SUCCEED",
        "displayName": "For Each Loop"
      }],
      "integrationParameters": [{
        "key": "`Task_1_loopMetadata`",
        "dataType": "JSON_VALUE",
        "displayName": "`Task_1_loopMetadata`",
        "isTransient": true,
        "producer": "1_1"
      }, {
        "key": "Recipients",
        "dataType": "STRING_VALUE",
        "defaultValue": {
          "stringValue": ""
        },
        "displayName": "Recipients",
        "inputOutputType": "IN"
      }, {
        "key": "Email_Subject",
        "dataType": "STRING_VALUE",
        "defaultValue": {
          "stringValue": ""
        },
        "displayName": "Email_Subject",
        "inputOutputType": "IN"
      }, {
        "key": "ListOfEmailContent",
        "dataType": "STRING_ARRAY",
        "defaultValue": {
          "stringArray": {
            "stringValues": ["\"Content 1\"", "\"Content 2\"", "\"Content 3\"", "\"Content 4\""]
          }
        },
        "displayName": "ListOfEmailContent",
        "inputOutputType": "IN"
      }]
    }

### Sample integration flow

The following images shows a sample layout of the integration editor for this integration code sample.

### Sub-integration

![image showing the sample sub-integration flow](https://raw.githubusercontent.com/GoogleCloudPlatform/application-integration-samples/HEAD/src/foreach-loop-send-email/foreach-loop-send-email-sub-flow.png)![image showing the sample sub-integration flow](https://raw.githubusercontent.com/GoogleCloudPlatform/application-integration-samples/HEAD/src/foreach-loop-send-email/foreach-loop-send-email-sub-flow.png)

### Main Integration

![image showing the sample main-integration flow](https://raw.githubusercontent.com/GoogleCloudPlatform/application-integration-samples/HEAD/src/foreach-loop-send-email/foreach-loop-send-email-flow.png)![image showing the sample main-integration flow](https://raw.githubusercontent.com/GoogleCloudPlatform/application-integration-samples/HEAD/src/foreach-loop-send-email/foreach-loop-send-email-flow.png)

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
