---
url: https://docs.cloud.google.com/endpoints/docs/openapi/migrate-oasv3/
title: Modify Cloud Endpoints to use OpenAPI 3.x \u00a0|\u00a0 Cloud Endpoints with OpenAPI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:53:31.978349+00:00
---

# Modify Cloud Endpoints to use OpenAPI 3.x  |  Cloud Endpoints with OpenAPI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/openapi/migrate-oasv3/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ OpenAPI ](https://docs.cloud.google.com/endpoints/docs/openapi)



Send feedback 

#  Modify Cloud Endpoints to use OpenAPI 3.x Stay organized with collections  Save and categorize content based on your preferences. 

OpenAPI | gRPC

This page describes how to use an OpenAPI 3.x specification when configuring Endpoints.

## Before you begin

  * Confirm that you have an existing Endpoints instance configured with an OpenAPI 2.0 specification.
  * Install the `gcloud` CLI. For more information, see [Install the Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install).



## Modify your Endpoints configuration to use OpenAPI 3.x

Complete the following steps to modify an existing OpenAPI 2.0 Endpoints configuration to use OpenAPI 3.x.

### View the deployment history

To view the deployment history:

  1. In the Google Cloud console, go to the **Endpoints** > **Services** page.

[Go to the Endpoints Services page](https://console.cloud.google.com/endpoints)

  2. From the projects list, select your project.

  3. If you have more than one API, select an API from the list.

  4. To see a list of service configuration deployments, click the **Deployment history** tab. The list displays:

     * The configuration ID.
     * The date the service configuration was deployed.
     * Who deployed the service configuration.



### View the service configuration

On the **Deployment history** tab, select the most recent deployment from the list. The contents of the deployed service configuration file are displayed.

### Convert the OpenAPI document to OpenAPI 3.x

Convert your OpenAPI 2.0 document to OpenAPI 3.x. You can use a tool that supports this conversion to OpenAPI 3.x. For example, [Swagger Editor](https://editor-next.swagger.io/) provides a conversion utility.

After the initial conversion to OpenAPI 3.x, manually apply any additional changes to the document to align with OpenAPI 3.x and ensure compatibility with Endpoints extensions and features.

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
    
    
    # OpenAPI 3.x
    servers:
    - url: https://my-api.apigateway.my-project.cloud.goog/
      x-google-endpoint:
        allowCors: True  
  
API Names | `x-google-api-name` | `x-google-api-management` | In OpenAPI 2.0 extensions, you define API names in `x-google-api-name`. In OpenAPI 3.x extensions, you use an `apiName` field in `x-google-api-management`. Manually move this configuration to `x-google-api-management`.  
Allow all traffic | `x-google-allow` | NOT SUPPORTED | Remove this from the OpenAPI document. Endpoints does not support this in OpenAPI 3.x.  
  
### Redeploy your service configuration

Whenever you change something in your OpenAPI document, be sure to deploy it again so that Endpoints has the most recent version of your API's service configuration. You don't need to redeploy or restart ESP if you previously deployed ESP with the [`rollout` option set to `managed`](https://docs.cloud.google.com/endpoints/docs/openapi/deploy-api-backend#deploying_your_api_and_esp). This option configures ESP to use the latest deployed service configuration. When you specify this option, up to 5 minutes after you deploy a new service configuration, ESP detects the change and automatically begins using it. We recommend that you specify this option instead of a specific configuration ID for ESP to use. 

To deploy your OpenAPI document:

  1. Change directory to the location containing your OpenAPI document.

  2. Validate the project ID returned from the following command to make sure that the service isn't created in the wrong project.
         
         gcloud config list project
         

If you need to change the default project, run the following command and replace YOUR_PROJECT_ID with the Google Cloud project ID in which you want to create the service::
         
         gcloud config set project <var>YOUR_PROJECT_ID</var>
         

  3. Run the following command, and replace YOUR_OPENAPI_DOCUMENT with the name of the OpenAPI document that describes your API:
         
         gcloud endpoints services deploy <var>YOUR_OPENAPI_DOCUMENT</var>
         




The first time that you run the previous command, Service Management creates a new Endpoints service in the default project with a name that matches the text that you specified in the `host` field in your OpenAPI document and uploads your service configuration.

As it is creating and configuring the service, Service Management outputs information to the terminal. On successful completion, you see a line like the following that displays the service configuration ID and the service name:
    
    
    Service Configuration [2017-02-13r0] uploaded for service [echo-api.endpoints.example-project-12345.cloud.goog]
    

In the previous example, `2017-02-13r0` is the service configuration ID and `echo-api.endpoints.example-project-12345.cloud.goog` is the service name.

After a successful deployment, you can view the API on the [**Endpoints** > **Services**](https://console.cloud.google.com/endpoints) page in the Google Cloud console.

If you get an error message, see [Troubleshooting Endpoints configuration deployment](https://docs.cloud.google.com/endpoints/docs/openapi/troubleshoot-config-deployment).

## What's next

  * [Deploying the API backend](https://docs.cloud.google.com/endpoints/docs/openapi/deploy-api-backend)
  * [Deploying on Kubernetes](https://docs.cloud.google.com/endpoints/docs/openapi/kubernetes-concept)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
