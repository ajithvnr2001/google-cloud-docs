---
url: https://docs.cloud.google.com/endpoints/docs/openapi/configure-endpoints/
title: Configuring Cloud Endpoints \u00a0|\u00a0 Cloud Endpoints with OpenAPI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:00:39.343003+00:00
---

# Configuring Cloud Endpoints  |  Cloud Endpoints with OpenAPI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/openapi/configure-endpoints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ OpenAPI ](https://docs.cloud.google.com/endpoints/docs/openapi)



Send feedback 

#  Configuring Cloud Endpoints Stay organized with collections  Save and categorize content based on your preferences. 

OpenAPI | [gRPC](https://docs.cloud.google.com/endpoints/docs/grpc/configure-endpoints "View this page for the Cloud Endpoints gRPC docs")

Cloud Endpoints supports APIs that are described using version 2.0 of the [OpenAPI specification](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md). You describe the API [surface](https://docs.cloud.google.com/endpoints/docs/openapi/glossary#surface) and configure Endpoints features such as [authentication rules](https://docs.cloud.google.com/endpoints/docs/openapi/authentication-method) or [quotas](https://docs.cloud.google.com/endpoints/docs/openapi/quotas-overview) in an [OpenAPI document](https://docs.cloud.google.com/endpoints/docs/openapi/glossary#open_api_doc).

Endpoints makes special use of the following required fields in your OpenAPI document:

  * `host`
  * `info.title`
  * `info.version`
  * `operationId`



This page provides information about how Endpoints uses the preceding fields. With this information, you can finish preparing your OpenAPI document for [deployment](https://docs.cloud.google.com/endpoints/docs/openapi/deploy-endpoints-config).

## Prerequisites

As a starting point, this page assumes that you have:

  * A [Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).
  * Basic knowledge of [OpenAPI](https://docs.cloud.google.com/endpoints/docs/openapi/openapi-overview).
  * An OpenAPI document in the format described in the [Swagger basic structure](https://swagger.io/docs/specification/2-0/basic-structure/) documentation.



## `host`

Cloud Endpoints uses the name you configure in the `host` field of your OpenAPI document as the name of your service. 

The name of your API service must be unique on Google Cloud. Because Endpoints uses DNS-compatible names to identify services, we recommend that you use your API's domain name or subdomain name as the service name. With this approach, the service name that appears on the **Endpoints Services** page matches the name used in requests to your API. Endpoints has the following requirements for the service name:

  * The maximum length of the domain name is 253 characters. 
  * The domain name must start with a lowercase letter. 
  * Each section in the domain name, which is delimited by dots, has the following requirements: 
    * Must start with a lowercase letter. 
    * Must not end with a dash. 
    * The remaining characters can be lowercase letters, numbers, or dashes. 
    * The maximum length is 63 characters. 



You can either register your own custom domain (such as `example.com`), or you can use a domain managed by Google.

### Use a domain managed by Google

Google owns and manages the `cloud.goog` and the `appspot.com` domains. If you want to use a domain managed by Google, you must use your Google Cloud project ID as part of the service name. Because Google Cloud projects have a globally unique project ID, this requirement ensures that you have a unique service name. 

The domain name that you use depends on the backend that hosts your API:

  * For APIs that are hosted on the App Engine flexible environment, you must use the `appspot.com` domain, and the service name must be in the following format, where `YOUR_PROJECT_ID` is your Google Cloud project ID:
        
        YOUR_PROJECT_ID.appspot.com
        

When you deploy your API to App Engine, a DNS entry with a name in the format `YOUR_PROJECT_ID.appspot.com` is created automatically.

  * For APIs that are hosted on Compute Engine, Google Kubernetes Engine, or Kubernetes, you must use the `cloud.goog` domain, and the service name must be in the following format, where `YOUR_API_NAME` is the name of your API:
        
        YOUR_API_NAME.endpoints.YOUR_PROJECT_ID.cloud.goog
        

To use this domain as the API's domain name, read [Configuring DNS on the `cloud.goog` domain](https://docs.cloud.google.com/endpoints/docs/openapi/cloud-goog-dns-configure).




### Use a custom domain

If you don't want to use a domain managed by Google, you can use a custom domain (for example, `myapi.mycompany.com`) that you are authorized to use. Before you deploy the API configuration, follow the steps in [Verify ownership of the domain](https://docs.cloud.google.com/endpoints/docs/openapi/verify-domain-name).

## `info.title`

The `info.title` field is a user-friendly name for your API. The **Endpoints** > **Services** page in the Google Cloud console displays the text that you configure in the `info.title` field. If you have more than one API per Google Cloud project, the API name is displayed in a list when you first open the page. You can click on the API name to open another page that displays the API's metrics, deployment history, and other information.

## `info.version`

The **Endpoints** > **Services** page in the Google Cloud console displays the version number for your API. Before deploying your API configuration for the first time:

  * Set the version number in the `info.version` field to the applicable API version,for example, `1.0`.

  * Set the `basePath` field to the major version number, for example, `/v1`.




For additional information on versioning your API, see [API lifecycle management](https://docs.cloud.google.com/endpoints/docs/openapi/lifecycle-management).

## `operationId`

Although the `operationId` is an optional field in the OpenAPI Specification, Endpoints requires this field because it is used for internal identification of the operation. The string that you use for the `operationId` must be unique within your API. See the description for [`operationId`](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md#operation-object) in the OpenAPI Specification for guidance on naming.

## What's next

  * [Deploying the Endpoints configuration](https://docs.cloud.google.com/endpoints/docs/openapi/deploy-endpoints-config)
  * [Deploying the API backend](https://docs.cloud.google.com/endpoints/docs/openapi/deploy-api-backend)
  * [Configuring authentication](https://docs.cloud.google.com/endpoints/docs/openapi/authentication-method)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
