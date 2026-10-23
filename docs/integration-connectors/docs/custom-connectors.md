---
url: https://docs.cloud.google.com/integration-connectors/docs/custom-connectors/
title: Custom connectors \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:10:07.036615+00:00
---

# Custom connectors  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/custom-connectors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — BigQuery Connector**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

# Custom connectors

This page provides an overview of the custom connectors feature in Integration Connectors, and assumes that you are familiar with the following concepts:

  * [Integration Connectors](https://docs.cloud.google.com/integration-connectors/docs/overview)
  * [Connector versus connection](https://docs.cloud.google.com/integration-connectors/docs/connectorvsconnection)
  * [Open API specifications](https://swagger.io/specification/)



The custom connectors feature lets you use connectors that aren't a part of the standard connectors provided by Integration Connectors. For example, you might have an in-house Human Resource Management System (HRMS) with a proprietary connectivity protocol that you want to expose to [Application Integration](https://docs.cloud.google.com/application-integration/docs/overview) through a connector. The custom connector feature is useful in the following scenarios:

  * Built-in connectors aren't available in Integration Connectors for a data source or service that you want to connect.
  * Built-in connectors are available in Integration Connectors, but they don't meet your requirements.



## How Integration Connectors supports a custom connector?

Integration Connectors supports custom connectors through Open API specification (version 3.0.0 and all its minor versions). You can expose your backend as a public endpoint, and then use your endpoint's Open API specification to create a new connector that connects to your endpoint (backend).

An endpoint's Open API specification defines the contract between Integration Connectors and the endpoint. Integration Connectors uses the API specification to generate the connector's [actions and entities](https://docs.cloud.google.com/integration-connectors/docs/entities-operation-action). The API specification can be a JSON or a YAML. The following is an excerpt from a sample Open API specification of a backend service:
    
    
    {
      "openapi":"3.0.2",
      "info":{
        "title":"Swagger Petstore - OpenAPI 3.0",
        "description":"This is a sample Pet Store Server based on the OpenAPI 3.0 specification.
      You can find out more about\nSwagger at [
        http://swagger.io](http://swagger.io). In the third iteration of the pet store,
        we've switched to the design first approach! You can now help us improve the API whether
      it's by making changes to the definition itself or to the code.\nThat way,
        with time, we can improve the API in general, and expose some of the new
      features in OAS3.\n\nSome useful links:\n-
      [
           The Pet Store repository
      ]
      .....
      .....
        },
      "paths":{
        "/pet/{petId}/uploadImage":{
          "post":{
            "tags":[
            ]
          }
        },
        .....
        .....
        "/pet/findByStatus":{
          "get":{
            "tags":[
              "pet"
            ],
            .....
            .....
          }
        }
      },
      "components": {
        "securitySchemes": {
          "api_key":{
            "type":"apiKey",
            "name":"api_key",
            "in":"header"
          }
        }
      }
    }
    

To view the complete sample specification, see [Sample pet store repository](https://petstore3.swagger.io/api/v3/openapi.json). Suppose you use this sample specification to create a custom connector, Integration Connectors will generate a separate action for each element in `path`. For example, `uploadImage` and `findByStatus` would be listed as supported actions by the custom connector. 

## Backend connectivity scenarios

Integration Connectors supports custom connectors for the following backend connectivity scenarios:

  * Direct backend connectivity
  * Indirect backend connectivity

**Note:** Irrespective of any connectivity scenarios, Integration Connectors can only connect to endpoints that are Open API compliant.

### Scenario - Direct backend connectivity

In this scenario, the Integration Connectors runtime directly establishes connectivity to your Open API compliant backend. The following illustration shows the connector connectivity in this scenario: 

![direct backend connectivity](https://docs.cloud.google.com/static/integration-connectors/images/custom-connectors-scenario-1.png)

### Scenario - Indirect backend connectivity

In this scenario, the Integration Connectors runtime establishes connectivity to your backend through an intermediary (facade) service that is Open API compliant. The intermediary service in turn connects to your backend. The following illustration shows the connector connectivity in this scenario:

![indirect backend connectivity](https://docs.cloud.google.com/static/integration-connectors/images/custom-connectors-scenario-2.png)

  * Integration Connectors doesn't manage the connectivity between the intermediary service and your backend. Therefore, delays that occur because of connectivity issues between the intermediary service and the backend are outside the scope of Integration Connectors SLA.
  * Integration Connectors doesn't support OAuth 2.0 authentication type between the intermediary service and the backend.



## Custom connector versions

With the versioning feature, you can create multiple versions of a custom connector. Each version can have a different OpenAPI specification, authentication method, and backend variables. This provides the flexibility to create a connector with various configurations.

When you create a new connector, the first version of the connector is created automatically for you, and the version details are displayed in the **Versions** tab of the [custom connector's details page](https://console.cloud.google.com/connectors/custom-connectors). To understand how to create a new version of a connector, see [Manage custom connector versions](https://docs.cloud.google.com/integration-connectors/docs/manage-custom-connector-versions). 

## What's next

Understand how to [create a custom connector](https://docs.cloud.google.com/integration-connectors/docs/create-custom-connector).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
