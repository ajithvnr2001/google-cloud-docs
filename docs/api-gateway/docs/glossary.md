---
url: https://docs.cloud.google.com/api-gateway/docs/glossary/
title: Glossary \u00a0|\u00a0 API Gateway \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:10:28.797699+00:00
---

# Glossary  |  API Gateway  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/api-gateway/docs/glossary/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ API Gateway ](https://docs.cloud.google.com/api-gateway/docs)
  * [ Guides ](https://docs.cloud.google.com/api-gateway/docs/secure-traffic-gcloud)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Glossary

This page provides brief definitions and links to more information of terms that are used in the API Gateway documentation.

API
    A REST interface that makes it easy for one application to consume capabilities or data from another application. By defining stable, simple, and well-documented entry points, APIs enable developers to easily access and reuse application logic built by other developers.
API config
    Created when you upload an API definition to API Gateway. Each time you upload an API definition, API Gateway creates a new API config. That is, you can create an API config but you cannot later modify it. If you later edit the API definition, and then upload the edited API definition, you create a new API config.
API definition
    An [Open API 2.0](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md) spec or [gRPC](http://www.grpc.io) configuration used to create an API config. An API definition specifies: the URL of the backend service, the data format of data passed on a request, the data format of any data returned by the service, the authentication mechanism used to control access to the service, and many more options.
API key
    A code passed in by a client application when it calls an API. API keys identify the application or the Google Cloud project making the call to the API. See [Why and when to use API keys](https://docs.cloud.google.com/endpoints/docs/openapi/when-why-api-key) for more information on using an API key with your API Gateway API.
Auth0
    A service that lets you define how users authenticate to applications. See [Auth0](https://auth0.com) for more information.
CORS
    Cross-Origin Resource Sharing (CORS) is a specification that provides a way for web applications to access resources on a server in another domain (technically, in another origin). To learn more about CORS, see the [Mozilla Developer Network (MDN) web docs](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) and the [Fetch Living Standard](https://fetch.spec.whatwg.org/).
Firebase authentication
    Google's authentication service that supports end user sign-in for client applications by using credentials from popular federated identity providers such as Google, Facebook, or Twitter. See [Firebase authentication](https://firebase.google.com/docs/auth/) for more information.
Gateway
    An [Envoy](https://www.envoyproxy.io/docs/envoy/latest/)-based, high-performance, scalable proxy that hosts the deployed API config. Creating a gateway creates the external facing URL that your API clients use to access the API. A gateway only host a single API config. You cannot deploy multiple API configs to the same gateway.
Google ID token
    A JSON Web Token (JWT) that contains the [OpenID Connect](https://developers.google.com/identity/protocols/OpenIDConnect) fields needed to identify a Google user account or service account, and that is signed by Google's authentication service, `https://accounts.google.com`.
gRPC
    A high performance, open source universal RPC framework developed by Google. In gRPC, a client application can directly call methods on a server application on a different machine as if it was a local object. See [gRPC Overview](https://docs.cloud.google.com/api-gateway/docs/grpc-overview) for information on using gRPC with API Gateway and the [gRPC](http://www.grpc.io) website for general information.
JWT
    JSON Web Token is an open standard access token format for use in HTTP Authorization headers and URI query parameters. See [Introduction to JSON Web Tokens](https://jwt.io/introduction/) for general information.
OpenAPI
    The [Open API Initiative](http://openapis.org) is an industry-wide effort to standardize the description of REST APIs. APIs that are described with the [OpenAPI Specification](https://github.com/OAI/OpenAPI-Specification) (formerly the [Swagger Specification](http://swagger.io)) can be supported with common tools that create documentation, automate testing, and generate code for clients and servers. See [OpenAPI overview](https://docs.cloud.google.com/api-gateway/docs/openapi-overview) for more information.
OpenAPI document
    A file in either YAML or JSON format that you use to describe your API. This file is also referred to as an API definition. When uploaded to API Gateway, the OpenAPI document is converted to an API config.
Surface
    The public interface of an API. An API's surface consists of the methods as well as the parameters and return types used in the methods.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
