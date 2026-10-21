---
url: https://docs.cloud.google.com/api-gateway/docs/openapi-limitations/
title: OpenAPI 2.0 feature limitations \u00a0|\u00a0 API Gateway \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:22:57.145163+00:00
---

# OpenAPI 2.0 feature limitations  |  API Gateway  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/api-gateway/docs/openapi-limitations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ API Gateway ](https://docs.cloud.google.com/api-gateway/docs)
  * [ Guides ](https://docs.cloud.google.com/api-gateway/docs/secure-traffic-gcloud)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# OpenAPI 2.0 feature limitations

The following sections describe the limitations of OpenAPI 2.0 features on API Gateway.

### Scopes Ignored

Although API Gateway accepts OpenAPI documents with scopes defined in a security scheme object, these scopes are not checked or enforced.

### Multiple Security Requirements

  * **API Key Requirements** : API Gateway does not support alternative (logical OR) security requirements if one of the schemes is an API key. However, conjunctions (logical AND) are supported, allowing you to require both an API key and an OAuth2 token.
  * **OAuth2 Requirements** : Alternative (logical OR) security requirements are supported for different OAuth2 security schemes.
  * Conjunctions (logical AND) security requirements for different OAuth2 security schemes are not supported.
  * **Optional Security** : An empty security requirement (`- {}`) can be used to make security optional for an API key, but this is not supported for OAuth.



### Security Definition Validation

API Gateway will reject an OpenAPI 3.x specification that uses a security requirement without a corresponding definition in the `securityDefinitions` section.

### URL Path Templating

API Gateway only supports URL path template parameters that represent entire path segments (e.g., `/items/{itemId}`). Parameters corresponding to partial segments (such as `/items/prefix_{id}_suffix`) are not supported and will be rejected.

### Parameters, Schemas, and Types

API Gateway accepts OpenAPI documents with various parameter and type definitions (e.g., `required` parameters, array formats), but it does not enforce them. Incoming requests are forwarded to your API regardless of these definitions.

### External Type References

API Gateway does not support references to types outside of the provided OpenAPI document. For example, a `$ref` pointing to an external URL is not allowed and will be rejected.

### Custom Port in Host Address

API Gateway does not allow custom ports in the `host` field of an OpenAPI document.

### YAML Alias Limitations

An OpenAPI document submitted to API Gateway can have a maximum of 200 YAML alias nodes. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
