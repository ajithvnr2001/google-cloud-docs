---
url: https://docs.cloud.google.com/endpoints/docs/grpc/about-grpc/
title: Cloud Endpoints for gRPC \u00a0|\u00a0 Cloud Endpoints with gRPC \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:36:05.353561+00:00
---

# Cloud Endpoints for gRPC  |  Cloud Endpoints with gRPC  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/grpc/about-grpc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ gRPC ](https://docs.cloud.google.com/endpoints/docs/grpc/about-grpc)



Send feedback 

#  Cloud Endpoints for gRPC Stay organized with collections  Save and categorize content based on your preferences. 

[gRPC](http://www.grpc.io) is a high performance, open-source universal RPC framework, developed by Google. In gRPC, a client application can directly call methods on a server application on a different machine as if it was a local object, making it easier to create distributed applications and services.

## API management

Endpoints works with either the [Extensible Service Proxy (ESP)](https://docs.cloud.google.com/endpoints/docs/grpc/glossary#extensible_service_proxy) or the [Extensible Service Proxy V2](https://docs.cloud.google.com/endpoints/docs/openapi/glossary#extensible_service_proxy_v2) (ESPv2) to provide API management.

With Endpoints for gRPC, you can use the API management capabilities of Endpoints to add an API console, monitoring, hosting, tracing, authentication, and more to your gRPC services. In addition, once you specify special mapping rules, ESP and ESPv2 translate RESTful JSON over HTTP into gRPC requests. This means that you can deploy a gRPC server managed by Endpoints and call its API using a gRPC or JSON/HTTP client, giving you much more flexibility and ease of integration with other systems.

![gRPC Endpoints Service](https://docs.cloud.google.com/static/endpoints/docs/images/grpc-endpoints.png)

You can create gRPC services for Endpoints in any gRPC-supported language. You can find out much more about gRPC, including quickstarts and tutorials for creating servers and clients, on the [gRPC site](http://www.grpc.io/docs/).

## Supported compute platforms

ESP and ESPv2 are Open Source projects and are available to you in the following ways:

  * A container in Artifact Registry. 
    * See the [ESP release notes](https://github.com/cloudendpoints/esp/releases) for the current ESP Docker image.
    * See the [ESPv2 release notes](https://github.com/GoogleCloudPlatform/esp-v2/releases) for the current ESPv2 Docker image.
  * Source code in GitHub. 
    * See the [ESP README](https://github.com/cloudendpoints/esp/blob/master/README.md) for details on building ESP.
    * See the [ESPv2 README](https://github.com/GoogleCloudPlatform/esp-v2/blob/master/README.md) for details on building ESPv2.



You can run the ESP container on the following:

  * Compute Engine with Docker
  * Kubernetes, including Google Kubernetes Engine
  * A [Linux or macOS computer or another cloud provider](https://docs.cloud.google.com/endpoints/docs/grpc/running-esp-localdev)



You can run the ESPv2 container on the following:

  * Cloud Run
  * Knative serving
  * GKE
  * Compute Engine
  * Kubernetes



See [About Cloud Endpoints](https://docs.cloud.google.com/endpoints/docs/grpc/about-cloud-endpoints) for more.

See [Deploying the API Backend](https://docs.cloud.google.com/endpoints/docs/grpc/deploy-api-backend) for information on deploying your API and Extensible Service Proxy on Google Cloud compute platforms.

## Service definition and configuration

gRPC is based around the idea of defining a **service** , specifying the methods that can be called remotely with their parameters and return types. By default, gRPC uses [protocol buffers](https://developers.google.com/protocol-buffers/docs/overview) as the Interface Definition Language (IDL) for describing both the service interface and the structure of the payload messages.
    
    
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
    

To use gRPC with Endpoints, you must provide a [service configuration](https://docs.cloud.google.com/endpoints/docs/grpc/grpc-service-config) along with the service definition. This configures the runtime behavior of your service, including authentication, the API(s) included in the service, mappings from HTTP requests to gRPC methods, and special Cloud Endpoints settings.

## Transcoding

Endpoints provides protocol translation for your gRPC services allowing clients to use HTTP/JSON to communicate with a gRPC service through the ESP or ESPv2.

The most common use case is allowing browser clients to talk to gRPC servers without special support from gRPC client libraries. Endpoints provides a mechanism for mapping HTTP requests to gRPC methods as part of [service configuration](https://docs.cloud.google.com/endpoints/docs/grpc/grpc-service-config).

You can find out more about this in [Transcoding HTTP/JSON to gRPC](https://docs.cloud.google.com/endpoints/docs/grpc/transcoding).

## Limitations

The following gRPC features are not yet supported in Endpoints:

  * Payload compression
  * Any IDL other than protocol buffers



In addition, Endpoints only supports gRPC services for GKE, Compute Engine, and Cloud Run (Beta). Endpoints does **not** support gRPC services for App Engine environments.

## What's next?

  * Follow one of our [tutorials](https://docs.cloud.google.com/endpoints/docs/grpc/tutorials) to get a simple gRPC service up and running with Cloud Endpoints in your environment of choice
  * Find out how to [configure a gRPC service](https://docs.cloud.google.com/endpoints/docs/grpc/grpc-service-config) for Cloud Endpoints
  * Explore samples. The getting-started-grpc sample is available on GitHub in the following languages: 
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
