---
url: https://docs.cloud.google.com/endpoints/docs/grpc/grpc-service-config/
title: Configuring a gRPC service \u00a0|\u00a0 Cloud Endpoints with gRPC \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:53:19.866335+00:00
---

# Configuring a gRPC service  |  Cloud Endpoints with gRPC  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/grpc/grpc-service-config/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ gRPC ](https://docs.cloud.google.com/endpoints/docs/grpc/about-grpc)
  * [ Reference ](https://docs.cloud.google.com/endpoints/docs/grpc/specify-proxy-startup-options)



Send feedback 

#  Configuring a gRPC service Stay organized with collections  Save and categorize content based on your preferences. 

OpenAPI | gRPC

To create a gRPC service—whether or not you are using Cloud Endpoints—you specify the _interface definition_ in one or more _`proto` files_, which are text files with the `.proto` extension. In a `proto` file, you define the surface of your API, including the data structures, methods, method parameters, and return types. Then, you compile your `proto` file by using the language-specific protocol buffer compiler, `protoc`. For more information, see [What is gRPC?](https://grpc.io/docs/guides/index.html) and [gRPC concepts](https://grpc.io/docs/guides/concepts.html).

To have your gRPC service managed by Endpoints, in addition to the compiled proto file, you have to specify a _service configuration_ in one or more YAML files. A service configuration is a specification that lets you define the behavior of a gRPC service, including authentication, quotas, and more.

## Service configuration overview

At the top of the YAML file, you specify basic information about the [service](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#service), such as its name and title. You configure other aspects of the service in subsections of the YAML file, for example:

  * Which APIs are served.
  * How the [callers are authenticated](https://docs.cloud.google.com/endpoints/docs/grpc/authenticating-users).
  * How to [restrict or grant API access with API keys](https://docs.cloud.google.com/endpoints/docs/grpc/restricting-api-access-with-api-keys).
  * How the APIs are accessed by using [HTTP REST](https://docs.cloud.google.com/endpoints/docs/grpc/transcoding).
  * For APIs using the `cloud.goog` domain, [the DNS configuration](https://docs.cloud.google.com/endpoints/docs/grpc/cloud-goog-dns-configure).



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

The [Bookstore sample](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/endpoints/bookstore-grpc), which is used in the [gRPC tutorials](https://docs.cloud.google.com/endpoints/docs/grpc/tutorials), includes a basic interface definition file and a service configuration file.

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
    
    name: bookstore.endpoints.MY_PROJECT_ID.cloud.goog
    
    title: Bookstore gRPC API
    apis:
    - name: endpoints.examples.bookstore.Bookstore

The previous code sample is the simplest service configuration as it:

  * Defines a service named `bookstore.endpoints.MY_PROJECT_ID.cloud.goog`, where `MY_PROJECT_ID` represents your Google Cloud project ID.
  * Specifies that the service exposes the API `endpoints.examples.bookstore.Bookstore`, as defined in the `bookstore.proto` file.
  * Provides a descriptive title that appears on the **Endpoints** > **Services** page in the Google Cloud console after you deploy the configuration. Review the complete GitHub versions of each file for more detailed comments.



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

## Using multiple YAML files

You might find it useful to use more than one YAML file to configure different features for the same service. Using multiple YAML files makes it easier to reuse files and modify them for different environments. For example, in the Bookstore sample, the basic configuration is specified in the [`api_config.yaml`](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/endpoints/bookstore-grpc/api_config.yaml) file and its HTTP rules are specified in the [`api_config_http.yaml`](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/endpoints/bookstore-grpc/api_config_http.yaml) file. This lets you deploy the HTTP rules only if you want to turn on JSON/HTTP to gRPC transcoding for the Bookstore.

If you use multiple YAML files for your service configuration, when the configuration is [deployed](https://docs.cloud.google.com/endpoints/docs/grpc/deploy-endpoints-config) each file is converted to [`google.api.Service`](https://github.com/googleapis/googleapis/blob/master/google/api/service.proto) proto messages, and then all messages are merged using proto merging semantics. That is, all singular scalar fields in the latter instance replace those in the former. So if you provide different singular values for the same rule in two files, the value in the second file you specify when deploying the configuration is used. Singular embedded messages are merged, and repeated fields are concatenated.

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

## Configuration validation

You [deploy your service configuration and compiled `proto` files](https://docs.cloud.google.com/endpoints/docs/grpc/deploy-endpoints-config) by using the [`gcloud endpoints services deploy`](https://docs.cloud.google.com/sdk/gcloud/reference/endpoints/services/deploy) to create your service’s runtime configuration. The `gcloud endpoints services deploy` command validates the service configuration and flags any errors and warnings.

Warnings are divided into regular and linter warnings. Linter warnings use an identifier of the form `<group>-<rule>`, where `<group>` indicates the configuration group, and `<rule>` the particular linter rule. For example, below the group is `versioning` and the rule is `http-version-prefix`:
    
    
    WARNING: bookstore.proto:51:3: (lint) versioning-http-version-prefix: method
    'endpoints.examples.bookstore.BookStore.ListShelves' has a different version
    prefix in HTTP path ('v2') than api version 'v1'.
    

You can suppress linter warnings by adding a directive to the documentation of an API element. You can add the directive in your `proto` file or in the service configuration YAML file. For example, the following suppresses the previous warning:
    
    
    service Bookstore {
      // Returns an object.
      // (== suppress_warning versioning-http-version-prefix ==)
      rpc ListShelves(google.protobuf.Empty) returns (ListShelvesResponse) {
          option (google.api.http) = { get: "/v1/shelves" };
      }
    }
    

To suppress warnings for an entire group, you can use a wildcard (`*`) instead of rule names. For example, `versioning-*` suppresses all warnings related to the `versioning` group.

Suppression directives attached to parent elements also apply to all children. For example, the following example suppresses all `versioning` group warnings on all methods within the service:
    
    
    // (== suppress_warning versioning-* ==)
    service Bookstore {
      // Returns an object.
      rpc ListShelves(google.protobuf.Empty) returns (ListShelvesResponse) {
          option (google.api.http) = { get: "/v1/shelves" };
      }
    }
    

To globally suppress a warning, attach it to the overview documentation of the service configuration:
    
    
    type: google.api.Service
    name: your_api.endpoints.<producer-project-id>.cloud.goog
    title: Bookstore gRPC API
    apis:
    - name: endpoints.examples.bookstore.BookStore
    documentation:
        overview: |
          A simple Bookstore gRPC API.
          (== suppress_warning documentation-presence ==)
    

Note that directives in documentation such as `suppress_warning` must appear on their own line, otherwise they won't be recognized. YAML block literal markers such as `>` remove all newlines, so if you use `overview: >` in the previous example, the suppression doesn't work. For more information on block literals in YAML, see [Indented delimiting](http://en.wikipedia.org/wiki/YAML#Indented_delimiting).

## What's next

  * [Configuring Endpoints](https://docs.cloud.google.com/endpoints/docs/grpc/configure-endpoints)
  * [Deploying the Endpoints configuration](https://docs.cloud.google.com/endpoints/docs/grpc/deploy-endpoints-config)
  * [gRPC service configuration reference](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
