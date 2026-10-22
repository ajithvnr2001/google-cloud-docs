---
url: https://docs.cloud.google.com/application-integration/docs/samples/ecom-order-processing/
title: E-commerce sample integration \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:19:51.511016+00:00
---

# E-commerce sample integration  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/samples/ecom-order-processing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Samples ](https://docs.cloud.google.com/application-integration/docs/samples)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# E-commerce sample integration

This sample integration illustrates an e-commerce back-end scenario use case. 

## Explore further

For detailed documentation that includes this code sample, see the following:

  * [Try the sample integration](https://docs.cloud.google.com/application-integration/docs/try-sample-integration-ecommerce)



## Code sample
    
    
    {
      "description": "The integration mimics the back office e-commerce order processing. The request is expected to contain order with one or more line items as json object with sku, quantity, price, vendor etc. If the total price of the order goes beyond $100 then there will be an email sent to approve the order else the order will be processed successfully. For all the items which have vendor as external, there will be an external order created by making a rest call to the external server. The response of the integration will be total order value, filtered list of external items and list of http response status received for each rest call made per external line_item.",
      "triggerConfigs": [{
        "label": "OrderProcessApiTrigger",
        "startTasks": [{
          "taskId": "1"
        }],
        "properties": {
          "Trigger name": "ecom-order-processing_API_1"
        },
        "triggerType": "API",
        "triggerNumber": "1",
        "triggerId": "api_trigger/ecom-order-processing_API_1",
        "position": {
          "x": -294,
          "y": -252
        }
      }, {
        "label": "ReportExternalOrders",
        "startTasks": [{
          "taskId": "6"
        }],
        "properties": {
          "Trigger name": "ecom-order-processing_API_2"
        },
        "triggerType": "API",
        "triggerNumber": "2",
        "triggerId": "api_trigger/ecom-order-processing_API_2",
        "position": {
          "x": 210,
          "y": -84
        }
      }],
      "taskConfigs": [{
        "task": "SuspensionTask",
        "taskId": "2",
        "parameters": {
          "customMessage": {
            "key": "customMessage",
            "value": {
              "stringValue": "Hello user, approval request from EcomOrderProcessing integration."
            }
          },
          "isApproved": {
            "key": "isApproved",
            "value": {
              "stringArray": {
                "stringValues": ["$`Task_2_isApproved`$"]
              }
            }
          },
          "suspensionExpiration": {
            "key": "suspensionExpiration",
            "value": {
              "jsonValue": "{\n  \"@type\": \"type.googleapis.com/enterprise.crm.eventbus.proto.SuspensionExpiration\",\n  \"remindAfterMs\": 86400000,\n  \"expireAfterMs\": 172800000\n}"
            }
          },
          "notifications": {
            "key": "notifications",
            "value": {
              "jsonValue": "{\n  \"protoValues\": [{\n    \"@type\": \"type.googleapis.com/enterprise.crm.eventbus.proto.Notification\",\n    \"emailAddress\": {\n      \"email\": \"\\u003cchange-this-to-email-id\\u003e\"\n    }\n  }]\n}"
            }
          }
        },
        "nextTasks": [{
          "taskId": "3",
          "condition": "$`Task_2_isApproved`$ \u003d true",
          "displayName": "Proceed if approved"
        }],
        "taskExecutionStrategy": "WHEN_ALL_SUCCEED",
        "displayName": "Approval",
        "successPolicy": {
          "finalState": "SUSPENDED"
        },
        "externalTaskType": "NORMAL_TASK",
        "position": {
          "x": -42
        }
      }, {
        "task": "FieldMappingTask",
        "taskId": "1",
        "parameters": {
          "FieldMappingConfigTaskParameterKey": {
            "key": "FieldMappingConfigTaskParameterKey",
            "value": {
              "jsonValue": "{\n  \"@type\": \"type.googleapis.com/enterprise.crm.eventbus.proto.FieldMappingConfig\",\n  \"mappedFields\": [{\n    \"inputField\": {\n      \"fieldType\": \"DOUBLE_VALUE\",\n      \"transformExpression\": {\n        \"initialValue\": {\n          \"referenceValue\": \"$orders_request$\"\n        },\n        \"transformationFunctions\": [{\n          \"functionType\": {\n            \"jsonFunction\": {\n              \"functionName\": \"GET_PROPERTY\"\n            }\n          },\n          \"parameters\": [{\n            \"initialValue\": {\n              \"literalValue\": {\n                \"stringValue\": \"line_items\"\n              }\n            }\n          }]\n        }, {\n          \"functionType\": {\n            \"jsonFunction\": {\n              \"functionName\": \"FOR_EACH\"\n            }\n          },\n          \"parameters\": [{\n            \"initialValue\": {\n              \"literalValue\": {\n                \"protoValue\": {\n                  \"@type\": \"type.googleapis.com/enterprise.crm.eventbus.proto.TransformExpression\",\n                  \"initialValue\": {\n                    \"referenceValue\": \"~x\"\n                  },\n                  \"transformationFunctions\": [{\n                    \"functionType\": {\n                      \"jsonFunction\": {\n                        \"functionName\": \"GET_PROPERTY\"\n                      }\n                    },\n                    \"parameters\": [{\n                      \"initialValue\": {\n                        \"literalValue\": {\n                          \"stringValue\": \"quantity\"\n                        }\n                      }\n                    }]\n                  }, {\n                    \"functionType\": {\n                      \"jsonFunction\": {\n                        \"functionName\": \"TO_DOUBLE\"\n                      }\n                    }\n                  }, {\n                    \"functionType\": {\n                      \"doubleFunction\": {\n                        \"functionName\": \"MULTIPLY\"\n                      }\n                    },\n                    \"parameters\": [{\n                      \"initialValue\": {\n                        \"referenceValue\": \"~x\"\n                      },\n                      \"transformationFunctions\": [{\n                        \"functionType\": {\n                          \"jsonFunction\": {\n                            \"functionName\": \"GET_PROPERTY\"\n                          }\n                        },\n                        \"parameters\": [{\n                          \"initialValue\": {\n                            \"literalValue\": {\n                              \"stringValue\": \"price_per_unit\"\n                            }\n                          }\n                        }]\n                      }, {\n                        \"functionType\": {\n                          \"jsonFunction\": {\n                            \"functionName\": \"TO_DOUBLE\"\n                          }\n                        }\n                      }]\n                    }]\n                  }]\n                }\n              }\n            }\n          }]\n        }, {\n          \"functionType\": {\n            \"jsonFunction\": {\n              \"functionName\": \"TO_DOUBLE_ARRAY\"\n            }\n          }\n        }, {\n          \"functionType\": {\n            \"doubleArrayFunction\": {\n              \"functionName\": \"SUM\"\n            }\n          }\n        }]\n      }\n    },\n    \"outputField\": {\n      \"referenceKey\": \"$total_order_value$\",\n      \"fieldType\": \"DOUBLE_VALUE\",\n      \"cardinality\": \"OPTIONAL\"\n    }\n  }]\n}"
            }
          }
        },
        "nextTasks": [{
          "taskId": "2",
          "condition": "$total_order_value$ \u003e\u003d $threshold_order_value$",
          "displayName": "TotalOrderValue Above Threshold ",
          "description": "Checks if the total order value is greater than or equal to $100"
        }, {
          "taskId": "3",
          "condition": "$total_order_value$ \u003c $threshold_order_value$",
          "displayName": "TotalOrderValue Below Threshold",
          "description": "Checks if the total order value is less than $100"
        }],
        "taskExecutionStrategy": "WHEN_ALL_SUCCEED",
        "displayName": "Find Total Order Price",
        "externalTaskType": "NORMAL_TASK",
        "position": {
          "x": -294,
          "y": -126
        }
      }, {
        "task": "FieldMappingTask",
        "taskId": "5",
        "parameters": {
          "FieldMappingConfigTaskParameterKey": {
            "key": "FieldMappingConfigTaskParameterKey",
            "value": {
              "jsonValue": "{\n  \"@type\": \"type.googleapis.com/enterprise.crm.eventbus.proto.FieldMappingConfig\",\n  \"mappedFields\": [{\n    \"inputField\": {\n      \"fieldType\": \"JSON_VALUE\",\n      \"transformExpression\": {\n        \"initialValue\": {\n          \"literalValue\": {\n            \"stringValue\": \"{\\\"STATUS\\\" : \\\"PROCESSING_COMPLETE\\\"}\"\n          }\n        },\n        \"transformationFunctions\": [{\n          \"functionType\": {\n            \"stringFunction\": {\n              \"functionName\": \"TO_JSON\"\n            }\n          }\n        }]\n      }\n    },\n    \"outputField\": {\n      \"referenceKey\": \"$orders_response$\",\n      \"fieldType\": \"JSON_VALUE\",\n      \"cardinality\": \"OPTIONAL\"\n    }\n  }]\n}"
            }
          }
        },
        "taskExecutionStrategy": "WHEN_ALL_SUCCEED",
        "displayName": "Build Response",
        "externalTaskType": "NORMAL_TASK",
        "position": {
          "x": -294,
          "y": 378
        }
      }, {
        "task": "SubWorkflowForEachLoopV2Task",
        "taskId": "4",
        "parameters": {
          "iterationElementMapping": {
            "key": "iterationElementMapping",
            "value": {
              "stringValue": "sub_integration_input"
            }
          },
          "aggregatorParameterMapping": {
            "key": "aggregatorParameterMapping",
            "value": {
              "jsonValue": "{\n  \"@type\": \"type.googleapis.com/enterprise.crm.eventbus.proto.ParameterMap\",\n  \"entries\": [{\n    \"key\": {\n      \"literalValue\": {\n        \"stringValue\": \"`Task_6_responseStatus`\"\n      }\n    },\n    \"value\": {\n      \"literalValue\": {\n        \"stringValue\": \"rest_call_response_status\"\n      }\n    }\n  }]\n}"
            }
          },
          "triggerId": {
            "key": "triggerId",
            "value": {
              "stringValue": "api_trigger/ecom-order-processing_API_2"
            }
          },
          "loopMetadata": {
            "key": "loopMetadata",
            "value": {
              "stringArray": {
                "stringValues": ["$`Task_4_loopMetadata`$"]
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
              "stringValue": "$filtered_external_items$"
            }
          },
          "workflowName": {
            "key": "workflowName",
            "value": {
              "stringValue": "ExampleIntegration-EcomOrderProcessing"
            }
          },
          "requestParameterMapping": {
            "key": "requestParameterMapping"
          },
          "overrideParameterMapping": {
            "key": "overrideParameterMapping"
          }
        },
        "nextTasks": [{
          "taskId": "5"
        }],
        "taskExecutionStrategy": "WHEN_ALL_SUCCEED",
        "displayName": "For Each Loop",
        "externalTaskType": "NORMAL_TASK",
        "position": {
          "x": -294,
          "y": 252
        }
      }, {
        "task": "FieldMappingTask",
        "taskId": "3",
        "parameters": {
          "FieldMappingConfigTaskParameterKey": {
            "key": "FieldMappingConfigTaskParameterKey",
            "value": {
              "jsonValue": "{\n  \"@type\": \"type.googleapis.com/enterprise.crm.eventbus.proto.FieldMappingConfig\",\n  \"mappedFields\": [{\n    \"inputField\": {\n      \"fieldType\": \"JSON_VALUE\",\n      \"transformExpression\": {\n        \"initialValue\": {\n          \"referenceValue\": \"$orders_request$\"\n        },\n        \"transformationFunctions\": [{\n          \"functionType\": {\n            \"jsonFunction\": {\n              \"functionName\": \"GET_PROPERTY\"\n            }\n          },\n          \"parameters\": [{\n            \"initialValue\": {\n              \"literalValue\": {\n                \"stringValue\": \"line_items\"\n              }\n            }\n          }]\n        }, {\n          \"functionType\": {\n            \"jsonFunction\": {\n              \"functionName\": \"FILTER_ELEMENTS\"\n            }\n          },\n          \"parameters\": [{\n            \"initialValue\": {\n              \"literalValue\": {\n                \"protoValue\": {\n                  \"@type\": \"type.googleapis.com/enterprise.crm.eventbus.proto.TransformExpression\",\n                  \"initialValue\": {\n                    \"referenceValue\": \"~x\"\n                  },\n                  \"transformationFunctions\": [{\n                    \"functionType\": {\n                      \"jsonFunction\": {\n                        \"functionName\": \"GET_PROPERTY\"\n                      }\n                    },\n                    \"parameters\": [{\n                      \"initialValue\": {\n                        \"literalValue\": {\n                          \"stringValue\": \"vendor\"\n                        }\n                      }\n                    }]\n                  }, {\n                    \"functionType\": {\n                      \"jsonFunction\": {\n                        \"functionName\": \"TO_STRING\"\n                      }\n                    }\n                  }, {\n                    \"functionType\": {\n                      \"stringFunction\": {\n                        \"functionName\": \"EQUALS\"\n                      }\n                    },\n                    \"parameters\": [{\n                      \"initialValue\": {\n                        \"literalValue\": {\n                          \"stringValue\": \"External\"\n                        }\n                      }\n                    }]\n                  }]\n                }\n              }\n            }\n          }]\n        }]\n      }\n    },\n    \"outputField\": {\n      \"referenceKey\": \"$filtered_external_items$\",\n      \"fieldType\": \"JSON_VALUE\",\n      \"cardinality\": \"OPTIONAL\"\n    }\n  }]\n}"
            }
          }
        },
        "nextTasks": [{
          "taskId": "4"
        }],
        "taskExecutionStrategy": "WHEN_ANY_SUCCEED",
        "displayName": "Filter External Items",
        "description": "Filtering out line_items which have vendor as \"External\" so that we can place order request to the vendor",
        "externalTaskType": "NORMAL_TASK",
        "position": {
          "x": -294,
          "y": 126
        }
      }, {
        "task": "GenericRestV2Task",
        "taskId": "6",
        "parameters": {
          "throwError": {
            "key": "throwError",
            "value": {
              "booleanValue": false
            }
          },
          "responseBody": {
            "key": "responseBody",
            "value": {
              "stringArray": {
                "stringValues": ["$`Task_6_responseBody`$"]
              }
            }
          },
          "disableSSLValidation": {
            "key": "disableSSLValidation",
            "value": {
              "booleanValue": false
            }
          },
          "httpParams": {
            "key": "httpParams"
          },
          "responseHeader": {
            "key": "responseHeader",
            "value": {
              "stringArray": {
                "stringValues": ["$`Task_6_responseHeader`$"]
              }
            }
          },
          "userAgent": {
            "key": "userAgent",
            "value": {
              "stringValue": ""
            }
          },
          "httpMethod": {
            "key": "httpMethod",
            "value": {
              "stringValue": "POST"
            }
          },
          "responseStatus": {
            "key": "responseStatus",
            "value": {
              "stringArray": {
                "stringValues": ["$`Task_6_responseStatus`$"]
              }
            }
          },
          "url": {
            "key": "url",
            "value": {
              "stringValue": "https://mocktarget.apigee.net/echo"
            }
          },
          "urlFetchingService": {
            "key": "urlFetchingService",
            "value": {
              "stringValue": "HARPOON"
            }
          },
          "useSSL": {
            "key": "useSSL",
            "value": {
              "booleanValue": false
            }
          },
          "requestorId": {
            "key": "requestorId",
            "value": {
              "stringValue": ""
            }
          },
          "urlQueryStrings": {
            "key": "urlQueryStrings"
          },
          "requestBody": {
            "key": "requestBody",
            "value": {
              "stringValue": "$sub_integration_input$"
            }
          },
          "followRedirects": {
            "key": "followRedirects",
            "value": {
              "booleanValue": true
            }
          },
          "additionalHeaders": {
            "key": "additionalHeaders"
          }
        },
        "taskExecutionStrategy": "WHEN_ALL_SUCCEED",
        "displayName": "Call REST Endpoint",
        "externalTaskType": "NORMAL_TASK",
        "position": {
          "x": 210,
          "y": 42
        }
      }],
      "integrationParameters": [{
        "key": "total_order_value",
        "dataType": "DOUBLE_VALUE",
        "displayName": "total_order_value",
        "inputOutputType": "OUT"
      }, {
        "key": "`Task_4_loopMetadata`",
        "dataType": "JSON_VALUE",
        "displayName": "`Task_4_loopMetadata`",
        "isTransient": true,
        "producer": "1_4"
      }, {
        "key": "threshold_order_value",
        "dataType": "DOUBLE_VALUE",
        "defaultValue": {
          "doubleValue": 100.0
        },
        "displayName": "threshold_order_value"
      }, {
        "key": "filtered_external_items",
        "dataType": "JSON_VALUE",
        "displayName": "filtered_external_items",
        "inputOutputType": "OUT"
      }, {
        "key": "orders_request",
        "dataType": "JSON_VALUE",
        "defaultValue": {
          "jsonValue": "{\n  \"order_no\": \"12345\",\n  \"buyer_id\": \"raambo\",\n  \"line_items\": [{\n    \"line\": 1.0,\n    \"sku\": \"tr100\",\n    \"vendor\": \"Internal\",\n    \"quantity\": 1.0,\n    \"price_per_unit\": 10.0\n  }, {\n    \"line\": 2.0,\n    \"sku\": \"tbz\",\n    \"vendor\": \"External\",\n    \"quantity\": 24.0,\n    \"price_per_unit\": 1.0\n  }]\n}"
        },
        "displayName": "orders_request",
        "inputOutputType": "IN",
        "jsonSchema": "{\n  \"properties\": {\n    \"buyer_id\": {\n      \"type\": \"string\"\n    },\n    \"line_items\": {\n      \"items\": {\n        \"properties\": {\n          \"price_per_unit\": {\n            \"type\": \"number\"\n          },\n          \"sku\": {\n            \"type\": \"string\"\n          },\n          \"vendor\": {\n            \"type\": \"string\"\n          },\n          \"line\": {\n            \"type\": \"number\"\n          },\n          \"quantity\": {\n            \"type\": \"number\"\n          }\n        },\n        \"type\": \"object\"\n      },\n      \"type\": \"array\"\n    },\n    \"order_no\": {\n      \"type\": \"string\"\n    }\n  },\n  \"type\": \"object\",\n  \"$schema\": \"http://json-schema.org/draft-04/schema#\"\n}"
      }, {
        "key": "rest_call_response_status",
        "dataType": "STRING_ARRAY",
        "displayName": "rest_call_response_status",
        "inputOutputType": "OUT"
      }, {
        "key": "`Task_2_isApproved`",
        "dataType": "BOOLEAN_VALUE",
        "displayName": "`Task_2_isApproved`",
        "isTransient": true,
        "producer": "1_2"
      }, {
        "key": "`Task_6_responseHeader`",
        "dataType": "STRING_VALUE",
        "displayName": "`Task_6_responseHeader`",
        "isTransient": true,
        "producer": "1_6"
      }, {
        "key": "`Task_6_responseBody`",
        "dataType": "STRING_VALUE",
        "displayName": "`Task_6_responseBody`",
        "isTransient": true,
        "producer": "1_6"
      }, {
        "key": "`Task_6_responseStatus`",
        "dataType": "STRING_VALUE",
        "defaultValue": {
          "stringValue": ""
        },
        "displayName": "`Task_6_responseStatus`",
        "inputOutputType": "OUT",
        "isTransient": true,
        "producer": "1_6"
      }, {
        "key": "orders_response",
        "dataType": "JSON_VALUE",
        "displayName": "orders_response",
        "inputOutputType": "OUT"
      }, {
        "key": "sub_integration_input",
        "dataType": "JSON_VALUE",
        "defaultValue": {
          "jsonValue": "{\n}"
        },
        "displayName": "sub_integration_input",
        "inputOutputType": "IN"
      }]
    }
    

### Sample integration flow

The following image shows a sample layout of the integration editor for this integration code sample.

![image showing the sample integration flow](https://raw.githubusercontent.com/GoogleCloudPlatform/application-integration-samples/HEAD/src/ecom-order-processing/ecom-order-processing-flow.png)![image showing the sample integration flow](https://raw.githubusercontent.com/GoogleCloudPlatform/application-integration-samples/HEAD/src/ecom-order-processing/ecom-order-processingflow.png)

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
