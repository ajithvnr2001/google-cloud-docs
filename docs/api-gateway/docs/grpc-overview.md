---
url: https://docs.cloud.google.com/api-gateway/docs/grpc-overview/
title: gRPC overview \u00a0|\u00a0 API Gateway \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:14:08.397961+00:00
---

# gRPC overview  |  API Gateway  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/api-gateway/docs/grpc-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ API Gateway ](https://docs.cloud.google.com/api-gateway/docs)
  * [ Guides ](https://docs.cloud.google.com/api-gateway/docs/secure-traffic-gcloud)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# gRPC overview

[gRPC](http://www.grpc.io) is a high performance, open-source universal RPC framework, developed by Google. In gRPC, a client application can directly call methods on a server application on a different machine as if it was a local object, making it easier to create distributed applications and services.

One of the primary benefits of using gRPC is for documentation; you can use your service configuration and API interface definition files to generate reference documentation for your API.

## API management

With API Gateway for gRPC, you can use the API management capabilities of API Gateway to add monitoring, hosting, tracing, authentication, and more to your gRPC services on Cloud Run. In addition, once you specify special mapping rules, API Gateway translates RESTful JSON over HTTP into gRPC requests. This means that you can deploy a gRPC server managed by API Gateway and call its API using a gRPC or JSON/HTTP client, giving you much more flexibility and ease of integration with other systems.

You can create gRPC services for API Gateway in any gRPC-supported language. You can find out much more about gRPC, including quickstarts and tutorials for creating servers and clients, on the [gRPC site](http://www.grpc.io/docs/).

## Service definition and configuration

gRPC is based on the idea of defining a **service** , specifying the methods that can be called remotely with their parameters and return types. By default, gRPC uses [protocol buffers](https://developers.google.com/protocol-buffers/docs/overview) as the Interface Definition Language (IDL) for describing both the service interface and the structure of the payload messages.
    
    
    // The greeting service definition.
    service Greeter {
      // Sends a greeting
      rpc SayHello (HelloRequest) returns (HelloReply) {}
    }
    
    // The request message containing the user's name.
    message HelloRequest {
      string name = 1;
    }
    
    // The response message containing the greetings
    message HelloReply {
      string message = 1;
    }
    

To use gRPC with API Gateway, you must provide a [service configuration](https://docs.cloud.google.com/api-gateway/docs/grpc-service-config) along with the service definition. This configures the runtime behavior of your service, including authentication, the API(s) included in the service, mappings from HTTP requests to gRPC methods, and special API Gateway settings.

## Transcoding

API Gateway provides protocol translation for your gRPC services on Cloud Run allowing clients to use HTTP/JSON to communicate with a gRPC service through the API Gateway.

The most common use case is allowing browser clients to talk to gRPC servers without special support from gRPC client libraries. API Gateway provides a mechanism for mapping HTTP requests to gRPC methods as part of [service configuration](https://docs.cloud.google.com/api-gateway/docs/grpc-service-config).

You can find out more about this in [Transcoding HTTP/JSON to gRPC](https://docs.cloud.google.com/endpoints/docs/grpc/transcoding).

**Note** : When using gRPC transcoding, request and response body sizes exceeding **one megabyte** may result in `500 Internal Server Error` responses. 

If this size is exceeded, request logs for API Gateway will show _grpc_json_transcode_failure{request_buffer_size_limit_reached}_ or _grpc_json_transcode_failure{response_buffer_size_limit_reached}_ in the _responseDetails_ field.

## Limitations

The following gRPC features are not yet supported in API Gateway:

  * Payload compression
  * Any IDL other than protocol buffers



API Gateway only supports Cloud Run gRPC services at this time.

## What's next

  * Explore samples. The `getting-started-grpc` sample is available on GitHub in the following languages: 
    * [Java](https://github.com/GoogleCloudPlatform/java-docs-samples/tree/master/endpoints/getting-started-grpc)
    * [Python](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/endpoints/getting-started-grpc)
    * [Ruby](https://github.com/GoogleCloudPlatform/ruby-docs-samples/tree/master/endpoints/getting-started-grpc)
    * [Go](https://github.com/GoogleCloudPlatform/golang-samples/tree/master/endpoints/getting-started-grpc)
    * [Node.js](https://github.com/GoogleCloudPlatform/nodejs-docs-samples/tree/master/endpoints/getting-started-grpc)
  * The Bookstore sample is available in the following languages: 
    * [Python](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/endpoints/bookstore-grpc)
    * [Java](https://github.com/GoogleCloudPlatform/java-docs-samples/tree/master/endpoints)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
