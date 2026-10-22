---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai-api-overview/
title: Vertex AI API overview \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:15:05.910376+00:00
---

# Vertex AI API overview  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai-api-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  Vertex AI API overview Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of using the APIs installed with Vertex AI on Google Distributed Cloud (GDC) air-gapped and its reference documentation.

## Service endpoint and discovery document

A service endpoint is required to interact programmatically with the Vertex AI APIs.

### Get the Vertex AI Workbench endpoint and discovery document

The API endpoint for the Vertex AI Workbench KRM API is:

`https://ENDPOINT/apis/aiplatform.gdc.goog/v1`

Replace `ENDPOINT` with the API endpoint of the Management API server.

To access the Vertex AI Workbench discovery document, perform one of the following actions:

  * Enter the endpoint URL in a browser.

  * Run the `kubectl proxy` command in a tool such as curl to open a proxy to the Management API server on your local machine. After that command is running, enter the following URL in your browser:

`http://127.0.0.1:8001/apis/aiplatform.gdc.goog/v1`.




### Get the pre-trained APIs endpoints

To get the endpoints for the pre-trained APIs, [view service status and endpoints](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-api-status).

## REST, gRPC, KRM, and client libraries

You can access the pre-trained APIs using gRPC or one of the provided client libraries. The client libraries are built on gRPC.

Alternatively, you access some pre-trained APIs using REST.

You can manage Vertex AI Workbench using its Kubernetes Resource Model (KRM) API.

### Client libraries

Vertex AI provides Python client libraries for pre-trained APIs. The following table shows a comparison of advantages and disadvantages of using client libraries:

Advantages | Disadvantages  
---|---  
Maintained by Google.   
Built-in authentication.   
Built-in retries.   
Efficient protocol buffer HTTP request body.  |  Not available for all programming languages.   
  
### REST

The OCR and Translation APIs support REST. For more information, see the REST API references for these services:

  * [OCR REST API reference](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/overview)

  * [Translation REST API reference](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest)


**Note:** The Speech-to-Text and Vertex AI Workbench APIs don't support REST.

The following table shows a comparison of advantages and disadvantages of using REST:

Advantages | Disadvantages  
---|---  
Simple JSON interface.   
Well supported by many Google and third-party tools and libraries.  |  You must build your own client.   
You must implement authentication.   
You must implement retries.   
Less efficient JSON HTTP request body.   
REST streaming is not supported by these APIs.   
  
### gRPC

Pre-trained APIs support gRPC. For more information about the generic descriptions of the types, methods, and fields generated for a gRPC library, see the following gRPC reference:

  * [OCR gRPC reference](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rpc)
  * [Speech-to-Text gRPC reference](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/speech-to-text/rpc)
  * [Translation gRPC reference](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc)

**Note:** The Vertex AI Workbench API doesn't support gRPC.

The following table shows a comparison of advantages and disadvantages of using gRPC:

Advantages | Disadvantage  
---|---  
Supports many programming languages.   
Efficient protocol buffer HTTP request body.  |  You must generate your own client from Google-supplied protocol buffers.   
You must implement authentication.   
You must implement retries.   
  
### KRM

The Vertex AI Workbench API supports KRM. For more information, see the [Vertex AI Workbench KRM API reference](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/workbench/krm/vertex-ai-workbench-krm-ref).

## Type, method, and field names

Depending on whether you are using client libraries, REST, gRPC, or KRM, the type, method, and field names for the API vary in the following ways:

  * REST is arranged by resource hierarchies and their methods.
  * Client libraries and gRPC are arranged by services and their methods.
  * KRM field names use camelCase, but the API service accepts either camelCase or snake_case.
  * REST and gRPC field names use snake_case.
  * Client library field names use either title case, camelCase, or snake_case, depending on which name is idiomatic for the language.



## REST and protocol buffers

When calling the REST API, the default value behavior for protocol buffers might result in missing fields in a JSON response. These fields are set to the default value, so they are not included in the response.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
