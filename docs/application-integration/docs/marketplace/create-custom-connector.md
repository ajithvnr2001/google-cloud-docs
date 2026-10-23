---
url: https://docs.cloud.google.com/application-integration/docs/marketplace/create-custom-connector/
title: Create a custom connector and a connection \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:17:30.527662+00:00
---

# Create a custom connector and a connection  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/marketplace/create-custom-connector/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a custom connector and a connection

**Preview — BigQuery Connector**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to create an OpenAPI specification for a web service and then create a custom connector and a connection for this connector.

Before you create a custom connector, you must create an OpenAPI specification for the web service.

## Create an OpenAPI specification for the web service

Custom connectors support OpenAPI 3.0. You can also manually create the specification. For information about the OpenAPI specifications, see [OpenAPI specifications](https://swagger.io/specification/).

You can also autogenerate the OpenAPI 2.0 specification using gin swagger middleware. For information, see [Gin Swagger](https://github.com/swaggo/gin-swagger). You must convert the OpenAPI 2.0 specification to OpenAPI v3.0 specification by using [Swagger Converter](https://converter.swagger.io/).

Sample OpenAPI specification.
    
    
    {
      "openapi": "3.0.0",
      "info": {
        "title": "Go HTTPbin Proxy Service",
        "description": "A simple Go service that proxies requests to httpbin.org, adding custom headers.",
        "version": "1.0.0"
      },
      "servers": [
        {
          "url": "http://localhost:8080"
        }
      ],
      "paths": {
        "/getData": {
          "get": {
            "summary": "Fetch data from httpbin.org/get",
            "description": "Sends a GET request to httpbin.org/get, including any custom headers.",
            "responses": {
              "200": {
                "description": "Successful response from httpbin.org",
                "content": {
                  "application/json": {
                    "schema": {
                      "type": "object"
                    }
                  }
                }
              }
            }
          }
        },
        "/postData/{id}": {
          "post": {
            "summary": "Post data to httpbin.org/post",
            "description": "Sends a POST request to httpbin.org/post with data, including any custom headers.",
            "parameters": [
              {
                "in": "path",
                "name": "id",
                "required": true,
                "schema": {
                  "type": "string"
                }
              }
            ],
            "requestBody": {
              "content": {
                "application/json": {
                  "schema": {
                    "type": "object",
                    "properties": {
                      "name": {
                        "type": "string"   
    
                      },
                      "address": {
                        "type": "string"
                      },
                      "gender": {
                        "type": "string"   
                      }
                    },
                    "required": [
                      "name",
                      "address",
                      "gender"
                    ]
                  }
                }
              }
            },
            "responses": {
              "200": {
                "description": "Successful response from httpbin.org",
                "content": {
                  "application/json": {
                    "schema": {
                      "type": "object"
                    }
                  }
                }
              },
              "400": {
                "description": "Bad Request - Invalid request body"
              }
            }
          }
        }
      }
    }

## Create a custom connector and validate the service

You must create a custom connector and then validate the web service by using it in a connection in Application Integration.

### Before you begin

Set up [Private Service Connect](https://cloud.google.com/integration-connectors/docs/network-connectivity-private) (PSC) for this virtual machine and then create an endpoint attachment.

### Create a custom connector

  1. In the [Console](https://console.cloud.google.com/), go to the **Application Integration > Custom connectors** page, and then select or create a Google Cloud project. 

[ Go to the Custom connectors page](https://console.cloud.google.com/integrations/custom-connectors)

  2. Click **Create new** to open the **Create custom connector** page.
  3. In the **Connector details** section, specify the required fields, such as **Connector name** and **Display name**.Also, enter the use cases for the connector in the **Description** field.
  4. **Configure connector destination for backend access** : Enable this option. This shows the additional configuration sections in the page. 
  5. **Service account** : Select a service account that has the required roles.
  6. **Logo** : Upload an image to a Cloud Storage bucket to use it as the connector logo. **Note:** Ensure your Cloud Storage bucket has the [public access prevention](https://docs.cloud.google.com/storage/docs/using-public-access-prevention#console) disabled.
  7. In the **Connector Specification** section, either enter the public URL of your Open API specification or upload your specification file to a Cloud Storage bucket.
  8. In **Connector Destination** section, add the IP address of the endpoint attachment and the port on which service is running.
  9. In **Connector Authentication** section, select **No Authentication**. Authentication types are not supported for Marketplace connectors.
  10. In **Backend Variables** section, add the variables you want to take as input while creating the connection. These variables appear in the connection creation page and are sent on every API call made to the service. The values which will not change with APIs, such as third-party backend credentials must be added in this section.
  11. Create the custom connector. Ensure that you have specified a logo and described the use cases for the custom connector.



### Create a connection

After you create the custom connector, create the connection for this connector.

  1. Click **Create new** to open the **Create connection** page.
  2. Select the custom connector that you created.
  3. Add values for the connection fields that you had defined.
  4. Create the connection.



### Validate the service

To validate the service, create a new integration.

  1. In the Google Cloud console, go to the **Application Integration** page and then create an integration. 
  2. Add API trigger and the connector task.
  3. Configure the connector task to use the connection created in the earlier step. Add Data Mapper if required.
  4. Set up the connectorInputPayload for the connector as per the schema. 
  5. Run the integration to verify that the connection is working.



If the Integration runs successfully and returns expected response, the web service is validated.

## What's next

  * Learn how to [create a startup script for the web service](https://docs.cloud.google.com/integration-connectors/docs/marketplace/create-startup-script).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
