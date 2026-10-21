---
url: https://docs.cloud.google.com/data-catalog/docs/api-libraries-overview/
title: Overview of APIs and Client Libraries \u00a0|\u00a0 Data Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:45:55.005662+00:00
---

# Overview of APIs and Client Libraries  |  Data Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-catalog/docs/api-libraries-overview/

Data Catalog is deprecated and will be discontinued on June 1, 2026. For steps to transition your Data Catalog users, workloads, and content to Knowledge Catalog (formerly Dataplex Universal Catalog), see [Transition from Data Catalog to Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/transition-to-dataplex-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Catalog ](https://docs.cloud.google.com/data-catalog/docs)
  * [ Reference ](https://docs.cloud.google.com/data-catalog/docs/reference)



Send feedback 

#  Overview of APIs and Client Libraries Stay organized with collections  Save and categorize content based on your preferences. 

Data Catalog offers several programmatic interfaces for interaction, and we recommend using them in the following order:

  * [Google Cloud Client Libraries](https://docs.cloud.google.com/apis/docs/client-libraries-explained#google_cloud_client_libraries): Data Catalog client libraries are available in multiple languages and are built on [gRPC](https://grpc.io/). These client libraries provide a layer of abstraction on top of gRPC and handle the details of operation polling and retries. For more information, see [Data Catalog client libraries](https://docs.cloud.google.com/data-catalog/docs/reference/libraries).

**Note:** While the Cloud Client Libraries are the preferred library choice, you can also use the [Google API Client Libraries](https://docs.cloud.google.com/apis/docs/client-libraries-explained#google-api-client-libraries) for Data Catalog. The "legacy" Google API Client Libraries provide access to the REST interface, but not the gRPC APIs.
  * [gRPC](https://docs.cloud.google.com/data-catalog/docs/reference/rpc): If your preferred programming language lacks a dedicated client library, you can still generate gRPC client libraries for Data Catalog using any gRPC-supported language. This requires the [protocol buffers](https://developers.google.com/protocol-buffers/) service definition, which is available in the [GitHub repository](https://github.com/googleapis/googleapis).

To generate and use your client, refer to the instructions on [grpc.io](https://grpc.io/) for your chosen language.

  * [REST API](https://docs.cloud.google.com/data-catalog/docs/reference/rest): if you're unable to use Data Catalog's client libraries or the gRPC API, use the REST API.




For more information, see the following:

  * [Google Cloud APIs](https://docs.cloud.google.com/apis/docs/overview)
  * [Client libraries explained](https://docs.cloud.google.com/apis/docs/client-libraries-explained)
  * [API errors](https://docs.cloud.google.com/apis/design/errors)
  * [HTTP response status codes](https://docs.cloud.google.com/apis/design/errors#handling_errors)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
