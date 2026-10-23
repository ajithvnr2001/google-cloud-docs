---
url: https://docs.cloud.google.com/application-integration/docs/view-openapi-spec/
title: View OpenAPI Specification for your integration \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:17:54.328621+00:00
---

# View OpenAPI Specification for your integration  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/view-openapi-spec/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# View OpenAPI Specification for your integration

**Preview — OpenAPI Specification**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Application Integration provides the ability to dynamically generate and view the OpenAPI Specifications of your published integrations that are configured with one or more [API triggers](https://docs.cloud.google.com/application-integration/docs/configure-api-trigger). Accessing the OpenAPI Specification of your integration allows you to: 

  * Gain a comprehensive understanding of your integration's API endpoints, methods, and data structures.
  * Enable more efficient development and troubleshooting by providing a detailed and centralized view of your integration's API.
  * Expose your integration APIs and seamlessly integrate with conversational agents, see [Build conversational agents with Application Integration](https://docs.cloud.google.com/application-integration/docs/conversational-agents).



## What is the OpenAPI Specification? 

![OpenAPI Specification logo](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/OpenAPI_Pantone.png)

The OpenAPI Specification (OAS) is a standard, language-independent format to describe RESTful APIs. Commonly written in either YAML or JSON formats, the OpenAPI Specification presents a formal description of the API elements such as its base URL, paths and verbs, headers, query parameters, content types, request and response models, and more. For more information about the OpenAPI Specification, see [OpenAPI Specification](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.0.md). 

**Note:** Application Integration only supports OpenAPI Specification **version 3.0.1**.

## Generate and view the OpenAPI Specification

You can dynamically generate and view the OpenAPI Specification for your integrations from the Integration editor in the Google Cloud console or using an API call.

### Before you begin

  * Confirm that your integration is configured with one or more API triggers. For information about configuring API triggers, see [API triggers](https://docs.cloud.google.com/application-integration/docs/configure-api-trigger).
  * Publish your integration. For information about how to publish an integration, see [Test and publish integrations](https://docs.cloud.google.com/application-integration/docs/test-publish-integrations).



### View OpenAPI Specification

To view the OpenAPI Specification for your integration, select one of the options: 

### Console

To view the OpenAPI Specification for a specific integration, do the following steps:

  1. Go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. In the navigation menu, click **Integrations**. 

The **Integrations** page appears, listing all the integrations available in the Google Cloud project. 

  3. Click the integration for which you want to view the OpenAPI Specification. This opens the integration in the Integration editor.
  4. Click the more_vert (Actions menu) in the Integration editor toolbar, and select **View OpenAPI spec**. 

The **View OpenAPI spec** pane appears displaying the OpenAPI Specification of the integration. The generated OpenAPI Specification, by default, contains all the API triggers configured in the integration. 

     * To view the OpenAPI Specification for a specific API trigger, select the API trigger from the **APIs** drop-down list.
     * To download the OpenAPI Specification as a YAML file, click  download  (Download).

**Note:** You can only view and download the OpenAPI Specification, in YAML format, for a single integration from the Integration editor at a time. To view and download the OpenAPI Specification, in YAML or JSON formats, follow the instructions in the **API** section.

### API

The `generateOpenApiSpec` method of the Application Integration API allows you to view the OpenAPI Specification for your integration using an API call. 

Use the following `curl` command to view the OpenAPI Specification for one or more integrations in the same region:

**Tip:** `curl` typically comes pre-installed for Linux and macOS operating systems. If you don't have `curl`, you can download it from the `curl` [releases and downloads page](https://curl.haxx.se/download.html).
    
    
    curl -X POST \
        -H "authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        -d '{
        "apiTriggerResources": [{
        "integrationResource": "INTEGRATION_NAME",
        "triggerId": ["api_trigger/TRIGGER_NAME", "api_trigger/TRIGGER_NAME_2", "api_trigger/TRIGGER_NAME_n"]
        },
        {
        "integrationResource": "INTEGRATION_NAME",
          "triggerId": ["api_trigger/TRIGGER_NAME"]
        }],
        "fileFormat": "DOC_TYPE"
        }' \
        "https://LOCATION-integrations.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION:generateOpenApiSpec"
              

Replace the following: 

  * `TRIGGER_NAME, TRIGGER_NAME_2, TRIGGER_NAME_n`: The names of the API trigger in your integration which you want to view the OpenAPI Specification for.
  * `INTEGRATION_NAME`: The name of your integration.
  * `DOC_TYPE`: The type of document to generate. The following values are supported: `YAML` or `JSON`.
  * `PROJECT_ID`: The ID of your Google Cloud project.
  * `LOCATION`: The location of your Google Cloud project. **Note:** You can only view the OpenAPI Specification for multiple integrations in the same region.



## Understanding the OpenAPI Specification

Application Integration generates the OpenAPI Specification for your published integrations following the [OpenAPI Specification 3.0](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.0.md) standard. The following table describes the elements of the OpenAPI Specification generated in Application Integration: 

Element | Description  
---|---  
`openapi` | The OpenAPI Specification version used.  
`info` | Information about the integration, such as its name (title), description, and published version.  
`servers` | The server URLs that host the integration.  
`paths` | Paths are created for each selected API trigger in the integration. The server URL combined with the path constitutes the API endpoint for making API calls. `Request` and `Response` fields are populated based on the input and output variables configured for the corresponding API trigger.  **Note:** Application Integration currently supports only a limited set of JSON schema keywords. For information on the supported keywords, see Considerations.  
`components` | The `schemas` field contains the JSON schema for the input and output variables of the API trigger.  The `securitySchemes` field contains the authentication information for the API triggers.   
  
## Considerations

The following considerations apply when viewing the OpenAPI Specification for your integration: 

  * The OpenAPI Specification is generated only for published integrations.
  * The OpenAPI Specification is generated only for integrations configured with one or more API triggers.
  * The OpenAPI Specification is generated only for integrations in the same region.
  * The OpenAPI Specification is generated in YAML format by default. To generate and view the OpenAPI Specification in JSON format, set the `fileFormat` parameter to `JSON` in the API call.
  * Application Integration currently supports only the following limited set of JSON schema keywords: 
    * `type`
    * `items`
    * `properties`
    * `description`
    * `required`
    * `array`
    * `object`
    * `oneOf`
    * `allOf`
    * `anyOf`
    * `not`
    * `null`
    * `enum`
    * `additionalProperties`
    * `default`
  * When validating the OpenAPI specification using the [Swagger Editor](https://editor.swagger.io/), you may encounter semantic errors related to the API paths similar to the following image: 

![Swagger Editor](https://docs.cloud.google.com/static/application-integration/images/swagger_editor.png)![Swagger Editor](https://docs.cloud.google.com/static/application-integration/images/swagger_editor.png)

These errors can be safely ignored. The OpenAPI Specification is still valid.




## What's next

  * [Build conversational agents with Application Integration](https://docs.cloud.google.com/application-integration/docs/conversational-agents).
  * Learn about [API triggers](https://docs.cloud.google.com/application-integration/docs/configure-api-trigger).
  * Learn about [Test and publish integrations](https://docs.cloud.google.com/application-integration/docs/test-publish-integrations).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
