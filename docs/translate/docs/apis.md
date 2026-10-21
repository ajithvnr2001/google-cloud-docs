---
url: https://docs.cloud.google.com/translate/docs/apis/
title: API usage overview \u00a0|\u00a0 Cloud Translation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:56:06.019032+00:00
---

# API usage overview  |  Cloud Translation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/translate/docs/apis/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Translation ](https://docs.cloud.google.com/translate/docs)
  * [ API and references ](https://docs.cloud.google.com/translate/docs/reference/api-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# API usage overview

This guide provides an overview of using the Cloud Translation API and its reference documentation.

## Client libraries, REST, and gRPC

You can access the API through client libraries, REST, or gRPC (Cloud Translation - Advanced only).

### Client libraries

Google provides client libraries for many popular languages to access the APIs. If your desired programming language is supported by the client libraries, we recommend that you use this option.

  * Cloud Translation - Basic [client libraries](https://docs.cloud.google.com/translate/docs/reference/libraries/v2/overview-v2)
  * Cloud Translation - Advanced [client libraries](https://docs.cloud.google.com/translate/docs/reference/libraries/v3/overview-v3)

Pros | Cons  
---|---  
Maintained by Google.   
Built-in [authentication](https://docs.cloud.google.com/docs/authentication).   
Built-in retries.   
Idiomatic for each language.   
Efficient [protocol buffer](https://developers.google.com/protocol-buffers) HTTP request body.  |  Not available for all programming languages.   
  
### REST

The Cloud Translation API supports [REST](https://wikipedia.org/wiki/Representational_state_transfer).

  * Cloud Translation - Basic [translate text method](https://docs.cloud.google.com/translate/docs/reference/rest/v2/translate)
  * Cloud Translation - Advanced [overview](https://docs.cloud.google.com/translate/docs/reference/rest).

Pros | Cons  
---|---  
Simple JSON interface.   
Well supported by many Google and third-party tools and libraries.  |  You must build your own client.   
You must [implement authentication](https://developers.google.com/identity/protocols/OAuth2).   
You must implement retries.   
Less efficient JSON HTTP request body.   
  
### gRPC

Cloud Translation - Advanced supports [gRPC](https://grpc.io/). For more information, see the [RPC reference](https://docs.cloud.google.com/translate/docs/reference/rpc), which provides a generic description of the types, methods, and fields generated for a gRPC library.

Pros | Cons  
---|---  
Supports [many programming languages](https://grpc.io/docs/reference/).   
Efficient [protocol buffer](https://developers.google.com/protocol-buffers) HTTP request body.  |  You must generate your own client from Google-supplied protocol buffers.   
You must [implement authentication](https://grpc.io/docs/guides/auth.html).   
You must implement retries.   
  
## Type, method, and field names

Depending on whether you are using client libraries, REST, or gRPC, the type, method, and field names for the API vary:

  * REST is arranged by resource hierarchies and their methods.
  * Client libraries and gRPC are arranged by services and their methods.
  * REST field names use camel case, though the API service will accept either camel case or snake case.
  * gRPC field names use snake case.
  * Client library field names use either title case, camel case or snake case, depending on which name is idiomatic for the language.



## API editions

Cloud Translation offers two editions: Basic (v2) and Advanced (v3). Each edition has its own set of APIs and capabilities. For more information, see the [Editions](https://docs.cloud.google.com/translate/docs/editions) page.

## What's next

  * For more information about using client libraries or REST, see get started translating text with [v3](https://docs.cloud.google.com/translate/docs/advanced/translate-text-advance) or [v2](https://docs.cloud.google.com/translate/docs/basic/translate-text-basic).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
