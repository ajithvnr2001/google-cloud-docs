---
url: https://docs.cloud.google.com/api-gateway/docs/openapi-overview/
title: OpenAPI overview \u00a0|\u00a0 API Gateway \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:14:08.252701+00:00
---

# OpenAPI overview  |  API Gateway  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/api-gateway/docs/openapi-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ API Gateway ](https://docs.cloud.google.com/api-gateway/docs)
  * [ Guides ](https://docs.cloud.google.com/api-gateway/docs/secure-traffic-gcloud)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# OpenAPI overview

API Gateway supports APIs that are described using supported versions of the OpenAPI specification.

Your API can be implemented using any publicly available REST framework such as [Django](https://www.djangoproject.com/) or [Jersey](https://jersey.github.io/).

You describe your API in a `YAML` file referred to as an _OpenAPI document_. This page describes some of the benefits to using OpenAPI, shows a basic OpenAPI document, and provides additional information to help you get started with OpenAPI.

## Supported OpenAPI Versions

API Gateway supports the following OpenAPI versions:

  1. OpenAPI 2.0 (formerly Swagger)
  2. OpenAPI 3.0.x
  3. OpenAPI 3.1.x



Official specifications for each version are available from the [OpenAPI Initiative](https://spec.openapis.org/oas/).

### Patch Version Support

The OpenAPI Specification indicates that patch versions (e.g., 3.0.1, 3.0.2) only introduce fixes or clarifications and don't add new features. As a result, API Gateway supports all patch versions of 3.0 and 3.1.

### Terminology

Throughout the API Gateway documentation, _OpenAPI 3.x_ refers to all OpenAPI 3 supported versions, as described in Supported OpenAPI versions.

## Benefits

One of the primary benefits to using OpenAPI is for documentation; once you have an OpenAPI document that describes your API, you can generate reference documentation for your API.

There are other benefits to using OpenAPI. For example, you can:

  * Generate client libraries in dozens of languages
  * Generate server stubs
  * Use projects to verify your conformance and to generate samples



## Basic structure of an OpenAPI document

An OpenAPI document describes the surface of your REST API, and defines information such as:

  * The name and description of the API
  * The individual endpoints (paths) in the API
  * How the callers are authenticated



The structure of your OpenAPI document depends upon the OpenAPI version you use. The following examples describe the structure of OpenAPI 2.0 and OpenAPI 3.x.

**Note:** If you want to use OpenAPI 3.x, make sure to update your `Google Cloud CLI` before you begin [Create an API config](https://docs.cloud.google.com/api-gateway/docs/creating-api-config) to avoid errors when uploading your API definition.

### OpenAPI 2.0

If you are new to OpenAPI, take a look at the [Swagger basic structure](https://swagger.io/docs/specification/2-0/basic-structure/), which provides a sample OpenAPI document (also referred to as a Swagger specification) and briefly explains each section of the file. The following example illustrates this basic structure:
    
    
    swagger: "2.0"
    info:
      title: API_ID optional-string
      description: "Get the name of an airport from its three-letter IATA code."
      version: "1.0.0"
    host: DNS_NAME_OF_DEPLOYED_API
    schemes:
      - "https"
    paths:
      "/airportName":
        get:
          description: "Get the airport name for a given IATA code."
          operationId: "airportName"
          parameters:
            -
              name: iataCode
              in: query
              required: true
              type: string
          responses:
            200:
              description: "Success."
              schema:
                type: string
            400:
              description: "The IATA code is invalid or missing."

### OpenAPI 3.x

If you are new to OpenAPI, take a look at the [Swagger basic structure](https://swagger.io/docs/specification/v3_0/basic-structure/) which provides a sample OpenAPI document and explains each section of the file. The following example illustrates this basic structure:
    
    
    openapi: 3.0.4
    info:
      title: **API_ID optional-string**
      description: Get the name of an airport from its three-letter IATA code
      version: 1.0.0
    x-google-api-management:
      backends:
        BACKEND_NAME
          address: **https ://BACKEND_URL/airportNameGET**
          pathTranslation: APPEND_PATH_TO_ADDRESS
          protocol: "http/1.1"
    x-google-backend: BACKEND_NAME
    paths:
      /airportName:
        get:
          summary: Get the airport name for a given IATA code
          operationId: airportName
          responses:
            '200':
              description: A successful response
              content:
                application/json:
                  schema:
                    type: string
          parameters:
            - name: iataCode
              in: query
              required: true
              schema:
                type: string

**Note:** For API Gateway, the use of `host` or `servers.url` in your API definition is optional. You can either omit this from the OpenAPI 2.0 or OpenAPI 3.x definition or set it to the DNS name of the deployed API. API providers often set it to the DNS name when sharing the OpenAPI description with their API consumers. Don't set the `host` or `servers.url` property to **null** or an empty value, as this will result in an error. 

For more information, see [Servers](https://docs.cloud.google.com/api-gateway/docs/openapi-v3-limitations#servers).

In addition to the basic structure, use the `openapi.yaml` file to configure:

  * The `title` field with the name of your API and an optional-string with a brief description.
  * A path to use an [API key](https://docs.cloud.google.com/api-gateway/docs/authentication-method).
  * Various security schemes for [OpenAPI 2.0](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/2.0.md#security-scheme-object) or [OpenAPI 3.x](https://spec.openapis.org/oas/v3.0.4.html#security-scheme-object-0) for authentication.
  * Extensions for [OpenAPI 2.0](https://docs.cloud.google.com/api-gateway/docs/oasv2-extensions) and [OpenAPI 3.x](https://docs.cloud.google.com/api-gateway/docs/oasv3-extensions).



## Generate an OpenAPI document

Depending on what language you are using, you might be able to generate an OpenAPI document. In Java, there are open source projects for both [Jersey](https://jersey.github.io/) and [Spring](https://github.com/springfox/springfox) that can generate an OpenAPI document from annotations. There is also a [Maven plugin](http://kongchen.github.io/swagger-maven-plugin/). For Python and Node developers, [OpenAPI.Tools](https://openapi.tools/) might be an interesting project.

The OpenAPI community is continually developing tools to help in the composition (and, for some languages, automatic generation) of OpenAPI documents. See the [The OpenAPI Specification](https://github.com/OAI/OpenAPI-Specification) for more.

## What's next

  * [OpenAPI 2.0 extensions](https://docs.cloud.google.com/api-gateway/docs/oasv2-extensions)
  * [OpenAPI 3.x extensions](https://docs.cloud.google.com/api-gateway/docs/oasv3-extensions)
  * [Unsupported OpenAPI features](https://docs.cloud.google.com/endpoints/docs/openapi/openapi-limitations)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
