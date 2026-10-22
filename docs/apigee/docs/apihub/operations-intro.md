---
url: https://docs.cloud.google.com/apigee/docs/apihub/operations-intro/
title: API operations and MCP tools overview \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:55:12.622439+00:00
---

# API operations and MCP tools overview  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/apihub/operations-intro/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  API operations and MCP tools overview Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

API hub helps you understand the specific capabilities of your APIs by representing their individual functions as distinct entities. For most APIs, these are called operations, which represent the fundamental actions performed on an API. For agentic APIs built using the Model Context Protocol (MCP), these are called tools. By exposing operations and tools as individual entities, API hub facilitates granular search and discovery, helping developers quickly find APIs that offer the required functionality. 

## How operations and tools are created

Operations and tools for an API version are created in the following ways: 

  * **Using specification files** : When you upload an API specification file, API hub automatically parses it to extract the defined operations or tools. 
    * Operations are extracted from OpenAPI specifications. 
    * Tools are extracted from MCP schema files.
**Note:** While specifications from multiple revisions can be stored for API proxies in Apigee and Apigee hybrid organizations, only the OpenAPI specification from the latest deployed revision is used to generate the API operations list in API hub. 
  * **Using the UI** : You can create operations using the Google Cloud console. **Note:** Creating MCP tools using the Google Cloud console is currently not supported. 
  * **Using the API** : You can create operations and tools using the [Operations API](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.apis.versions.operations) or the [Specifications API](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.apis.versions.specs). This gives you the flexibility to supplement or override what was automatically extracted from a specification.



## How operations and tools are used in API hub

Both operations and tools are used in similar ways within API hub to improve discovery and analysis:

  * **Semantic Search** : Operations and tools are indexed for [Semantic Search](https://docs.cloud.google.com/apigee/docs/apihub/search-apis) allowing you to find APIs based on the functionality they provide.
  * **API exploration** : Exposing operations and tools as individual entities makes it easier for developers to explore an API's capabilities at a granular level.
  * **Dependency analysis** : You can analyze the dependencies between APIs at the function level. For example, you can identify which APIs are calling a specific operation and which are being called by it. This is visible in the [Supply chain](https://docs.cloud.google.com/apigee/docs/apihub/api-supply-chain) page. **Note:** Dependency analysis is currently not supported for MCP tools. 



## What's next

  * Learn about how to [manage API operations](https://docs.cloud.google.com/apigee/docs/apihub/manage-operations).
  * Learn about how to [manage MCP tools](https://docs.cloud.google.com/apigee/docs/apihub/manage-mcp-tools).
  * Learn more about [Operations API](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.apis.versions.operations).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
