---
url: https://docs.cloud.google.com/endpoints/docs/grpc/configure-endpoints/
title: Configuring Cloud Endpoints \u00a0|\u00a0 Cloud Endpoints with gRPC \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:46:18.496402+00:00
---

# Configuring Cloud Endpoints  |  Cloud Endpoints with gRPC  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/grpc/configure-endpoints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ gRPC ](https://docs.cloud.google.com/endpoints/docs/grpc/about-grpc)



Send feedback 

#  Configuring Cloud Endpoints Stay organized with collections  Save and categorize content based on your preferences. 

[OpenAPI](https://docs.cloud.google.com/endpoints/docs/openapi/configure-endpoints "View this page for the Cloud Endpoints OpenAPI docs") | gRPC

This page describes the configuration files needed to create a gRPC service that is managed by Endpoints.

## Prerequisites

As a starting point, this page assumes that you have:

  * A [Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).
  * Basic knowledge of [configuring a gRPC API service](https://docs.cloud.google.com/endpoints/docs/grpc/grpc-service-config).
  * Installed gRPC and the gRPC tools. Read [Get started with gRPC](https://grpc.io/docs/quickstart/) for details.



## Choosing the service name

Cloud Endpoints uses the name you configure in your gRPC API configuration YAML file as the name of your service. 

The name of your API service must be unique on Google Cloud. Because Endpoints uses DNS-compatible names to identify services, we recommend that you use your API's domain name or subdomain name as the service name. With this approach, the service name that appears on the **Endpoints Services** page matches the name used in requests to your API. Endpoints has the following requirements for the service name:

  * The maximum length of the domain name is 253 characters. 
  * The domain name must start with a lowercase letter. 
  * Each section in the domain name, which is delimited by dots, has the following requirements: 
    * Must start with a lowercase letter. 
    * Must not end with a dash. 
    * The remaining characters can be lowercase letters, numbers, or dashes. 
    * The maximum length is 63 characters. 



You can either register your own custom domain (such as `example.com`), or you can use a domain managed by Google.

### Use a domain managed by Google

Google owns and manages the `cloud.goog` domain. If you want to use a domain managed by Google, you must use your Google Cloud project ID as part of the service name. Because Google Cloud projects have a globally unique project ID, this requirement ensures that you have a unique service name. If you want to use the `cloud.goog` domain, the service name must be in the format, where `YOUR_API_NAME` is the name of your API and `YOUR_PROJECT_ID` is your Google Cloud project ID: 
    
    
    YOUR_API_NAME.endpoints.YOUR_PROJECT_ID.cloud.goog`
    

To use this domain as the API's domain name, read [Configuring DNS on the `cloud.goog` domain](https://docs.cloud.google.com/endpoints/docs/grpc/cloud-goog-dns-configure). 

### Use a custom domain

If you don't want to use a domain managed by Google, you can use a custom domain (for example, `myapi.mycompany.com`) that you are authorized to use. Before you deploy the API configuration, follow the steps in [Verify ownership of the domain](https://docs.cloud.google.com/endpoints/docs/grpc/verify-domain-name).

## Configuring the protocol buffer

  1. Create a `.proto` file for your service. Read the [Developer guide](https://developers.google.com/protocol-buffers/docs/overview)  
for details.

  2. Compile your protocol buffers by using the [`protoc` compiler](https://developers.google.com/protocol-buffers/docs/pythontutorial#compiling-your-protocol-buffers) for your language. For example:
         
         protoc
           --proto_path=. \
           --include_imports \
           --include_source_info \
           --descriptor_set_out=api_descriptor.pb \
           bookstore.proto
         

In the preceding command, `--proto_path` is set to the current working directory. In your gRPC build environment, if you use a different directory for `.proto` input files, change `--proto_path` so the compiler searches the directory where you saved your `.proto` file.

If the `protoc` command to generate your descriptor file fails, make sure that:

     * Your `protoc` version is up-to-date.
     * You specified the `--proto_path` or its short form `-I` for the root directories for imported `.proto` files. You can find out more in the [protocol buffers documentation](https://developers.google.com/protocol-buffers/docs/proto3#generating).
     * You specified `--include_imports`.

If you want your clients to access your gRPC service by using HTTP with JSON, you need to specify how data is translated from HTTP with JSON to gRPC. We recommend that you annotate the APIs defined in your `.proto` file. Read [Transcoding HTTP/JSON to gRPC](https://docs.cloud.google.com/endpoints/docs/grpc/transcoding) for more information.




## Configuring the gRPC service configuration file

You need to create a gRPC service configuration YAML file. You specify the name of the service and usage restrictions, such as requiring an API key in this file. You can use the `api_config.yaml` file from the Bookstore sample as a model.

  1. Save a copy of [ `api_config.yaml`](https://raw.githubusercontent.com/GoogleCloudPlatform/python-docs-samples/master/endpoints/bookstore-grpc/api_config.yaml).

  2. Enter the name of your service in the `name` field. For example:
         
         name: bookstore.endpoints.example-project-12345.cloud.goog
         

  3. Enter the title that is displayed on the **Endpoints** > **Services** page in the Google Cloud console. For example:
         
         title: Bookstore gRPC API
         

  4. Enter the API name in the `apis:name` field. The text that you enter must exactly match the fully-qualified API name from your `.proto` file. For example:
         
         apis:
           - name: endpoints.examples.bookstore.Bookstore
         

  5. Configure the rest of the file. For example:
         
         #
         # API usage restrictions.
         #
         usage:
           rules:
           # ListShelves methods can be called without an API Key.
           - selector: endpoints.examples.bookstore.Bookstore.ListShelves
             allow_unregistered_calls: true
         

Read [Rules and selectors](https://docs.cloud.google.com/endpoints/docs/grpc/grpc-service-config#rules_and_selectors) for more information.




## What's next

  * [Deploying the Endpoints configuration](https://docs.cloud.google.com/endpoints/docs/grpc/deploy-endpoints-config)
  * [Deploying the API backend](https://docs.cloud.google.com/endpoints/docs/grpc/deploy-api-backend)
  * [Configuring authentication](https://docs.cloud.google.com/endpoints/docs/grpc/authentication-method)



## Additional gRPC samples

  * [Java version of the Bookstore sample](https://github.com/GoogleCloudPlatform/java-docs-samples/tree/master/endpoints/bookstore-grpc).
  * The `getting-started-grpc` sample is available on GitHub in the following languages:

    * [Java](https://github.com/GoogleCloudPlatform/java-docs-samples/tree/master/endpoints/getting-started-grpc)
    * [Python](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/endpoints/getting-started-grpc)
    * [Ruby](https://github.com/GoogleCloudPlatform/ruby-docs-samples/tree/master/endpoints/getting-started-grpc)
    * [Go](https://github.com/GoogleCloudPlatform/golang-samples/tree/master/endpoints/getting-started-grpc)
    * [Node.js](https://github.com/GoogleCloudPlatform/nodejs-docs-samples/tree/master/endpoints/getting-started-grpc)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
