---
url: https://docs.cloud.google.com/api-gateway/docs/migrate-oasv3/
title: Modify a gateway to use OpenAPI 3.x \u00a0|\u00a0 API Gateway \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:24:38.252578+00:00
---

# Modify a gateway to use OpenAPI 3.x  |  API Gateway  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/api-gateway/docs/migrate-oasv3/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ API Gateway ](https://docs.cloud.google.com/api-gateway/docs)
  * [ Guides ](https://docs.cloud.google.com/api-gateway/docs/secure-traffic-gcloud)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Modify a gateway to use OpenAPI 3.x

This page describes how to modify an existing API gateway to use an OpenAPI 3.x specification for its API configuration.

## Before you begin

  * Confirm that you have an existing API Gateway instance configured with an OpenAPI 2.0 specification.
  * Install the `gcloud` CLI. For more information, see [Install the Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install).



## Modify an API configuration to use OpenAPI 3.x

To modify an existing OpenAPI 2.0 API Gateway configuration to use OpenAPI 3.x complete the following steps:

### Find the current API configuration

Find the API config associated with your gateway.

  1. Describe your API Gateway instance:
         
         gcloud api-gateway gateways describe GATEWAY_ID --project=PROJECT_ID --location=GATEWAY_LOCATION
         

Replace the following:

     * GATEWAY_ID: The ID of your gateway.
     * PROJECT_ID: Your Google Cloud project ID.
     * GATEWAY_LOCATION: The location of your gateway.

The output displays the `apiConfig` path, for example:
    
    apiConfig: projects/my-project/locations/global/apis/my-api/configs/my-gateway-config
    createTime: '2025-03-25T02:49:58.641650649Z'
    defaultHostname: my-gateway-a1b2c3d4.uc.gateway.dev
    displayName: My gateway
    name: projects/my-project/locations/us-west1/gateways/my-new-gateway
    state: ACTIVE
    updateTime: '2025-03-25T02:51:52.674308428Z'
    




### Get the OpenAPI document

To get the OpenAPI document for the API configuration you identified:

  1. Describe the API configuration:
         
         gcloud api-gateway api-configs describe CONFIG_ID --api=API_ID --project=PROJECT_ID --view=FULL
         

Replace the following:

     * CONFIG_ID: The ID of your API configuration.
     * API_ID: The ID of your API.
     * PROJECT_ID: Your Google Cloud project ID.

The output displays the `openapiDocuments` section, which contains the base64-encoded content of your OpenAPI document:
    
    createTime: '2024-02-16T21:11:36.293169474Z'
    displayName: my-api-config
    gatewayServiceAccount: projects/-/serviceAccounts/api-gateway-sa@my-sandbox.iam.gserviceaccount.com
    name: projects/my-project-id/locations/global/apis/my-api/configs/my-gateway-config
    openapiDocuments:
    -   document:
        contents: IyBvc...
        path: apigateway-config.yaml
    serviceConfigId: my-api-config-0a1fjkfeb7t8z
    state: ACTIVE
    updateTime: '2024-02-16T21:13:45.626771120Z'
    




### Decode the OpenAPI document

To decode the base64-encoded OpenAPI document content:

  1. Decode the `contents` value:
         
         echo 'IyBvc...' | base64 -d
         

Replace `IyBvc...` with the actual `contents` value from the previous step.

The output displays your OpenAPI 2.0 document, for example:
         
         swagger: '2.0'
         info:
           title: API_ID
           description: Sample API on API Gateway with a Google Cloud Functions backend
           version: 1.0.0
         




### Convert the OpenAPI document to OpenAPI 3.x

You can use a tool to convert your OpenAPI 2.0 document to OpenAPI 3.x. For example, [Swagger Editor](https://editor-next.swagger.io/) provides a conversion utility.

After the initial conversion to OpenAPI 3.x, manually apply any additional changes to the document to align with OpenAPI 3.x and ensure compatibility with API Gateway extensions and features. For more details on supported OpenAPI 3.x extension in API Gateway, see [OpenAPI 3.x Extensions in API Gateway](https://docs.cloud.google.com/api-gateway/docs/oasv3-extensions).

The following table describes the required changes:

Feature | OpenAPI 2.0 | OpenAPI 3.x | Description of change  
---|---|---|---  
API key | `securityDefinitions` | `securitySchemes` | API keys use out-of-the-box OpenAPI API key support. Conversion tools typically handle this automatically. No manual changes are required.  
JWT Authentication | `x-google-audiences`, etc. | `x-google-auth` | In OpenAPI 2.0 extensions, you define OAuth configuration with individual extensions on a `securityDefinition` instance. Conversion tools convert the security scheme instance to `#/components/securitySchemes` and leave the extensions. Manually modify these extensions to be children of `x-google-auth` and remove the `x-google-` prefix. The values remain the same.  
Quota | `x-google-management`, `x-google-quota` | `x-google-api-management`, `x-google-quota` | In OpenAPI 2.0 extensions, you define metrics and quota in `x-google-management` and attach them with `x-google-quota`. Conversion tools leave these extensions in place. Manually move metrics and quota configuration from `x-google-management` to `x-google-api-management`. Change the configuration to use YAML keys, and remove `valueType`, `metricKind`, and `unit`. Remove `metricCosts` from instances of `x-google-quota`.  
Backends | `x-google-backend` | `x-google-api-management`, `x-google-backend` | In OpenAPI 2.0 extensions, you define backends in `x-google-backend`, and the configuration applies where defined. In OpenAPI 3.x extensions, you define the backend in `x-google-api-management` and then apply it with `x-google-backend`. Conversion tools leave this extension in place. Manually move the configuration to `x-google-api-management`. Modify instances of `x-google-backend` to reference that configuration.  
Endpoints | `x-google-endpoints` | `x-google-endpoint`, `servers` | In OpenAPI 2.0 extensions, you define endpoints configuration in `x-google-endpoints`. In OpenAPI 3.x extensions, you use `x-google-endpoint`, but it is an extension on `servers` rather than at the root. Conversion tools leave this extension in place. Manually move this to `servers` and remove the `name` field. For example: 
    
    
    # OpenAPI 2.0
    x-google-endpoints:
    - name: "my-api.apigateway.my-project.cloud.goog"
      allowCors: True
    
    
    # OpenAPI 3.0.x
    servers:
    - url: https://my-api.apigateway.my-project.cloud.goog/
      x-google-endpoint:
        allowCors: True  
  
API Names | `x-google-api-name` | `x-google-api-management` | In OpenAPI 2.0 extensions, you define API names in `x-google-api-name`. In OpenAPI 3.x extensions, you use an `apiName` field in `x-google-api-management`. Manually move this configuration to `x-google-api-management`.  
Allow all traffic | `x-google-allow` | NOT SUPPORTED | Remove this from the OpenAPI document. API Gateway does not support this in OpenAPI 3.x.  
  
### Create a new API configuration

Create a new API configuration using your modified OpenAPI 3.x document.

  1. Create the API configuration:
         
         gcloud api-gateway api-configs create NEW_CONFIG_ID --api=API_ID --project=PROJECT_ID --openapi-spec=NEW_API_DEFINITION
         

Replace the following:

     * NEW_CONFIG_ID: A new ID for your API configuration.
     * API_ID: The ID of your API.
     * PROJECT_ID: Your Google Cloud project ID.
     * NEW_API_DEFINITION: The path to your OpenAPI 3.x specification file.



### Update the gateway

Update your gateway instance to reference the new API configuration from your modified OpenAPI 3.x document.

  1. Update the gateway:
         
         gcloud api-gateway gateways update GATEWAY_ID --api-config=API_CONFIG --project=PROJECT_ID --location=GATEWAY_LOCATION
         

Replace the following:

     * GATEWAY_ID: The ID of your gateway.
     * API_CONFIG: The full resource path of your new API configuration, for example: `projects/PROJECT_ID/locations/global/apis/API_ID/configs/NEW_CONFIG_ID`
     * PROJECT_ID: Your Google Cloud project ID.
     * GATEWAY_LOCATION: The location of your gateway.



## What's next

  * Learn more about [API Gateway](https://docs.cloud.google.com/api-gateway/docs/overview).
  * Explore the [OpenAPI Specification](https://swagger.io/specification/).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
