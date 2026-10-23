---
url: https://docs.cloud.google.com/endpoints/docs/openapi/versioning-an-api/
title: Versioning an API \u00a0|\u00a0 Cloud Endpoints with OpenAPI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:02:04.661641+00:00
---

# Versioning an API  |  Cloud Endpoints with OpenAPI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/openapi/versioning-an-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ OpenAPI ](https://docs.cloud.google.com/endpoints/docs/openapi)



Send feedback 

#  Versioning an API Stay organized with collections  Save and categorize content based on your preferences. 

OpenAPI | gRPC

This page provides detailed configuration and deployment procedures for changing the version number of your API. The procedure that you use depends on whether the changes to your API are backwards compatible.

  * If your new API version has backwards-compatible changes, such as adding new fields or methods, see Backwards-compatible changes.
  * If your new API has changes to an existing method that breaks your customers' client code, see Backwards-incompatible changes.



For additional information and best practices, see [API lifecycle management](https://docs.cloud.google.com/endpoints/docs/openapi/lifecycle-management).

## Backwards-compatible changes

When you make changes to your API that are backwards compatible with existing client code, as a best practice, increment the minor version number of your API before you deploy the new version. Although Cloud Endpoints runs only one minor version of an API at a time, the graphs and logs in **Endpoints** > **Services** display the version number. By incrementing the minor version number before you deploy, the graphs and logs provide a labeled history of your deployments.

To increment the minor version number:

  1. In `openapi.yaml`, increment the minor version number of the `info.version` field. For example, if the current version is `1.1`, set `info.version` to `1.2`:
         
         info:
           description: "A simple Cloud Endpoints API example."
           title: "Endpoints Example"
           version: "1.2"
         host: "echo-api.endpoints.example-project-12345.cloud.goog"
         

  2. Use the Google Cloud CLI to deploy the API configuration:
         
         gcloud endpoints services deploy openapi.yaml
         

  3. Deploy the API backend by using the configuration ID returned from the previous step. For details, see [Deploying the API backend](https://docs.cloud.google.com/endpoints/docs/openapi/deploy-api-backend).




## Backwards-incompatible changes

When you make changes to your API that breaks your customers' client code, as a best practice, increment the major version number of your API. Endpoints can run more than one major version of an API concurrently. By providing both versions of the API, your customers can pick which version they want to use and control when they migrate to the new version.

To run the existing and new versions of an API concurrently:

  1. Create separate OpenAPI configuration files for each version you need to serve. This procedure uses the file names `openapi-v1.yaml` and `openapi-v2.yaml` for example purposes.

  2. Copy the contents of `openapi-v1.yaml` to `openapi-v2.yaml`.

  3. In `openapi-v1.yaml` configure the following:

     * Set the `info.version` field to the existing version number.
     * Leave the `basePath` field unchanged.

For example:
    
    info:
      description: "A simple Cloud Endpoints API example."
      title: "Endpoints Example"
      version: "1.1"
    host: "echo-api.endpoints.example-project-12345.cloud.goog"
    basePath: "/v1"
    

  4. In `openapi-v2.yaml` configure the following:

     * Make backwards-incompatible changes.
     * Set the `info.version` field to the new version number.
     * Set the `basePath` field to include the new major version number.
     * Remove the `x-google-endpoints` section. This section is needed if you want to specify DNS IP address or `allowCors` flag. When deploying two versions of the API with two yaml config files, only one of them can have `x-google-endpoints`, but its config will apply to both versions.

For example:
    
    info:
      description: "A simple Google Cloud Endpoints API example."
      title: "Endpoints Example"
      version: "2.0"
    host: "echo-api.endpoints.example-project-12345.cloud.goog"
    basePath: "/v2"
    

  5. Use the Google Cloud CLI to deploy both API configuration files:
         
         gcloud endpoints services deploy openapi-v1.yaml openapi-v2.yaml
         

**Note:** Cloud Endpoints internally converts your multiple OpenAPI configuration files into a single configuration, which is identified by one configuration ID.
  6. Deploy a single backend that serves both versions of the API by using the configuration ID returned from the previous step. For details, see [Deploying the API backend](https://docs.cloud.google.com/endpoints/docs/openapi/deploy-api-backend).




## What's next

  * [API lifecycle management](https://docs.cloud.google.com/endpoints/docs/openapi/lifecycle-management)
  * [Planning your Google Cloud projects](https://docs.cloud.google.com/endpoints/docs/openapi/planning-cloud-projects)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
