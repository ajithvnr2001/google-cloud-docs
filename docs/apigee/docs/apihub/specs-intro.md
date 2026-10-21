---
url: https://docs.cloud.google.com/apigee/docs/apihub/specs-intro/
title: API specifications overview \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:39:55.032826+00:00
---

# API specifications overview  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/apihub/specs-intro/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  API specifications overview Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

API specifications use standard formats to describe APIs. They are machine readable, but also easy for humans to read and understand. Specifications typically describe elements of an API such as its base path, paths and verbs, headers, query parameters, operations, content types, response descriptions.

An [API version](https://docs.cloud.google.com/apigee/docs/apihub/versions-intro) can contain multiple API specifications of the same or different type. API hub supports several specification formats, including: 

  * [OpenAPI specifications](https://swagger.io/specification/) for REST APIs
  * Protocol Buffers for RPC APIs
  * Web Service Definition Language (WSDL) for SOAP APIs
  * MCP schema files for Model Context Protocol (MCP) APIs



## Using API specifications with API hub

You can create an API version in API hub with or without an API specification. You can upload a specification at the time you create a version, or you can attach one to an existing version. When you view the details of an API in the user interface, you will see a list of any specs that are associated with the versions of that API resource

For more information, see [Manage API specifications](https://docs.cloud.google.com/apigee/docs/apihub/manage-specifications). 

## Specification parsing

Where supported, API hub can parse an API specification to extract information about the API and store it with an API version. This parsing process is what populates the version with its specific operations or tools. 

API hub supports specification parsing for the following formats:

  * **OpenAPI specifications:** For versions with the `REST` API style, API hub parses the OpenAPI file to extract the API's operations. **Note:** API specification parsing is only supported for OpenAPI specifications (v.2.0, v3.0 and v3.1) in JSON and YAML formats. 
  * **MCP schema:** For versions with the `MCP` API style, API hub parses the MCP schema file to extract the API's tools.



API hub also supports specification validation. For more information, see [Validate an API specification](https://docs.cloud.google.com/apigee/docs/apihub/validate-spec). 

## What's next

  * Learn more about [API versions](https://docs.cloud.google.com/apigee/docs/apihub/versions-intro).
  * Learn more about [Manage API specifications](https://docs.cloud.google.com/apigee/docs/apihub/manage-specifications).
  * Learn more about [API operations and MCP tools](https://docs.cloud.google.com/apigee/docs/apihub/operations-intro).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
