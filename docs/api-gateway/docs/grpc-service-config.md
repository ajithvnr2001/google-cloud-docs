---
url: https://docs.cloud.google.com/api-gateway/docs/grpc-service-config/
title: Configure a gRPC Service \u00a0|\u00a0 API Gateway \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:27:00.752538+00:00
---

# Configure a gRPC Service  |  API Gateway  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/api-gateway/docs/grpc-service-config/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ API Gateway ](https://docs.cloud.google.com/api-gateway/docs)
  * [ Guides ](https://docs.cloud.google.com/api-gateway/docs/secure-traffic-gcloud)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure a gRPC Service 

To create a gRPC service—whether or not you are using API Gateway—you specify the _interface definition_ in one or more _`proto` files_, which are text files with the `.proto` extension. In a `proto` file, you define the surface of your API, including the data structures, methods, method parameters, and return types. Then, you compile your `proto` file by using the language-specific protocol buffer compiler, `protoc`. For more information, see [What is gRPC?](https://grpc.io/docs/guides/index.html) and [gRPC concepts](https://grpc.io/docs/guides/concepts.html).

To have your gRPC service managed by API Gateway, in addition to the compiled proto file, you have to specify a _service configuration_ in one or more YAML files. A service configuration is a specification that lets you define the behavior of a gRPC service, including authentication, quotas, and more.

## Service configuration overview

At the top of the YAML file, you can specify basic information about the service, such as its name and title. Other aspects of the service are configured in subsections of the YAML file, for example:

  * Which APIs are served.
  * How [callers are authenticated](https://docs.cloud.google.com/api-gateway/docs/authentication-method).
  * How to [restrict or grant API access with API keys](https://docs.cloud.google.com/api-gateway/docs/authentication-method#api_keys).
  * How the APIs are accessed by using HTTP REST.



For example:
    
    
    type: google.api.Service
    config_version: 3
    name: calendar.googleapis.com
    title: Google Calendar API
    apis:
    - name: google.calendar.v3.Calendar
    authentication:
      providers:
      - id: google_calendar_auth
        jwks_uri: https://www.googleapis.com/oauth2/v1/certs
        issuer: https://securetoken.google.com
      rules:
      - selector: "*"
        requirements:
          provider_id: google_calendar_auth
    backend:
      rules:
        - selector: "*"
          address: grpcs://my-service-98sdf8sd0-uc.a.run.app
    

Each subsection typically corresponds to a [`.proto` message](https://developers.google.com/protocol-buffers/docs/overview) where you configure various aspects of the service. For example:

  * [`authentication`](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#authentication): specifies how callers are authenticated.
  * [`backend`](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#backend): controls remote backend routing.
  * [`http`](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#http): defines the rules for mapping an RPC method to one or more HTTP REST API methods.
  * [`usage`](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#usage): lets you selectively enable and disable API key validation.



The official schema for the service configuration is defined by the `.proto` message [`google.api.Service`](https://github.com/googleapis/googleapis/blob/master/google/api/service.proto).

### Basic configuration

The [Bookstore sample](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/endpoints/bookstore-grpc), which is used in the [Get started with API Gateway and Cloud Run for gRPC](https://docs.cloud.google.com/api-gateway/docs/get-started-cloud-run-grpc) tutorial, includes a basic interface definition file and a service configuration file.

**The Bookstore interface definition** , [`bookstore.proto`](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/endpoints/bookstore-grpc/bookstore.proto):
    
    
    syntax = "proto3";
    
    package endpoints.examples.bookstore;
    
    option java_multiple_files = true;
    option java_outer_classname = "BookstoreProto";
    option java_package = "com.google.endpoints.examples.bookstore";
    
    import "google/protobuf/empty.proto";
    
    service Bookstore {
      rpc ListShelves(google.protobuf.Empty) returns (ListShelvesResponse) {}
      rpc CreateShelf(CreateShelfRequest) returns (Shelf) {}
      rpc GetShelf(GetShelfRequest) returns (Shelf) {}
      rpc DeleteShelf(DeleteShelfRequest) returns (google.protobuf.Empty) {}
      rpc ListBooks(ListBooksRequest) returns (ListBooksResponse) {}
      rpc CreateBook(CreateBookRequest) returns (Book) {}
      rpc GetBook(GetBookRequest) returns (Book) {}
      rpc DeleteBook(DeleteBookRequest) returns (google.protobuf.Empty) {}
    }
    
    message Shelf {
      int64 id = 1;
      string theme = 2;
    }
    
    message Book {
      int64 id = 1;
      string author = 2;
      string title = 3;
    }

**The Bookstore service configuration** , [`api_config.yaml`](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/endpoints/bookstore-grpc/api_config.yaml):
    
    
    type: google.api.Service
    config_version: 3
    
    name: *.apigateway.PROJECT_ID.cloud.goog
    
    title: Bookstore gRPC API
    apis:
    - name: endpoints.examples.bookstore.Bookstore

The previous code sample is the simplest service configuration as it:

  * Defines a service named `*.apigateway.PROJECT_ID.cloud.goog` where PROJECT_ID is the name of your Google Cloud project ID.
  * Specifies that the service exposes the API `endpoints.examples.bookstore.Bookstore`, as defined in the `bookstore.proto` file.



### Rules and selectors

In some cases, you might need the ability to associate configuration with individual elements of a service—for example, to enforce authentication on certain methods but not others. To configure this in your service configuration, some parts of the service configuration, such as [`authentication`](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#authentication) and [`http`](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#http), let you specify _rules_ and _selectors_. A selector identifies the elements of the service, such as a method name that the configuration associated with the rule applies to.

A selector is a comma-separated list of qualified names defined in the service: method, message, field, enum, or enum values. The last segment of the name can be the wildcard `*`, which matches any suffix. Wildcards are allowed only at the end of a name and only for a whole segment of the name. For example: `foo.*` is okay, but not `foo.b*` or `foo.*.bar`. To configure a default for all applicable elements, you specify `*` by itself.

Example 1 (affecting entire service):
    
    
    usage:
      rules:
      # Allow unregistered calls for all methods.
      - selector: "*"
        allow_unregistered_calls: true
    

Example 2 (affecting a single method):
    
    
    usage:
      rules: # IMPORTANT: ONLY LAST MATCHING RULE IS APPLIED
      # Disable API key validation on just the ListShelves method
      # while requiring an API key for the rest of the API.
      - selector: "*"
        allow_unregistered_calls: false
      - selector: "endpoints.examples.bookstore.BookStore.ListShelves"
        allow_unregistered_calls: true
    

The previous example shows how to require API key validation for all methods except the `ListShelves` method.

Rules are evaluated sequentially, the last matching one in the declaration order is applied.

## Quotas

To apply a [quota](https://docs.cloud.google.com/api-gateway/docs/quotas-overview) to your gRPC service, define the metrics in the top-level `metrics` section of your service configuration, the limits in `quota.limits`, and the cost that each method incurs in `quota.metric_rules`. For example:
    
    
    metrics:
      - name: "read-requests"
        display_name: "Read requests"
        value_type: INT64
        metric_kind: DELTA
    quota:
      limits:
        - name: "read-limit"
          metric: "read-requests"
          unit: "1/min/{project}"
          values:
            STANDARD: 1000
      metric_rules:
        - selector: "endpoints.examples.bookstore.Bookstore.ListShelves"
          metric_costs:
            "read-requests": 1

For detailed instructions on each of these fields, see the Cloud Endpoints doc at [Configuring quotas](https://docs.cloud.google.com/endpoints/docs/grpc/quotas-configure).

**Caution:** Ensure that your quota metrics and limits remain consistent across all active API configs before you create a new one. API Gateway applies `metrics` and `quota` to the entire API rather than to an individual API config, so any metric or limit that a new API config declares replaces the definition for the whole API. If you rename or remove a metric, any gateway that still serves an earlier API config rejects calls to its quota-enforced methods with the gRPC status code `Internal`. For more information, see [Quotas apply to the whole API](https://docs.cloud.google.com/api-gateway/docs/quotas-overview#quotas_apply_to_the_whole_api).

## Use multiple YAML files

You might find it useful to use more than one YAML file to configure different features for the same service. Using multiple YAML files makes it easier to reuse files and modify them for different environments. For example, in the Bookstore sample, the basic configuration is specified in the [`api_config.yaml`](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/endpoints/bookstore-grpc/api_config.yaml) file and its HTTP rules are specified in the [`api_config_http.yaml`](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/endpoints/bookstore-grpc/api_config_http.yaml) file. This lets you deploy the HTTP rules only if you want to turn on JSON/HTTP to gRPC transcoding for the Bookstore.

If you use multiple YAML files for your service configuration, when the configuration is [deployed](https://docs.cloud.google.com/api-gateway/docs/get-started-cloud-run-grpc#deploying_an_api_gateway) each file is converted to [`google.api.Service`](https://github.com/googleapis/googleapis/blob/master/google/api/service.proto) proto messages, and then all messages are merged using proto merging semantics. That is, all singular scalar fields in the latter instance replace those in the former. So if you provide different singular values for the same rule in two files, the value in the second file you specify when deploying the configuration is used. Singular embedded messages are merged, and repeated fields are concatenated.

Like rules, merging is order sensitive. If there are two service configurations, the second service configuration overrides the first one.

## Annotations (HTTP rules only)

As an alternative to using a YAML file for configuring HTTP options, you can configure them directly in your `proto` file, using the [options mechanism](https://developers.google.com/protocol-buffers/docs/proto?csw=1#options). API annotations are defined in [annotations.proto](https://github.com/googleapis/googleapis/blob/master/google/api/annotations.proto).

Use annotations if the configuration option is intended to be invariant over all usages of the protocol buffer interface definition. For example, if an API has one single implementation, or all implementations are required to have the same HTTP interface, you can annotate the HTTP configuration in the `proto` file.

If a configuration option is provided, both in the `proto` file and the service configuration YAML file, the service configuration overrides the annotation.

Example annotation in a `proto` file:
    
    
    rpc ListShelves(google.protobuf.Empty) returns (ListShelvesResponse) {
        option (google.api.http) = { get: "/v1/shelves" };
    }
    
    
    # The preceding annotation is equivalent to the following service configuration:
    
    http:
      rules:
      - selector: endpoints.examples.bookstore.BookStore.ListShelves
        get: '/v1/shelves'
    

For more information, see [Transcoding HTTP/JSON to gRPC](https://docs.cloud.google.com/endpoints/docs/grpc/transcoding).

## What's next

  * [Get started with API Gateway and Cloud Run for gRPC ](https://docs.cloud.google.com/api-gateway/docs/get-started-cloud-run-grpc)
  * [Deploy an API to a gateway](https://docs.cloud.google.com/api-gateway/docs/deploying-api)
  * [gRPC service configuration reference](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
