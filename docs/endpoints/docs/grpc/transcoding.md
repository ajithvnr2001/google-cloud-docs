---
url: https://docs.cloud.google.com/endpoints/docs/grpc/transcoding/
title: Transcoding HTTP/JSON to gRPC \u00a0|\u00a0 Cloud Endpoints with gRPC \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:42:49.108790+00:00
---

# Transcoding HTTP/JSON to gRPC  |  Cloud Endpoints with gRPC  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/grpc/transcoding/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ gRPC ](https://docs.cloud.google.com/endpoints/docs/grpc/about-grpc)



Send feedback 

#  Transcoding HTTP/JSON to gRPC Stay organized with collections  Save and categorize content based on your preferences. 

OpenAPI | gRPC

Cloud Endpoints supports protocol transcoding so that clients can access your gRPC API by using HTTP/JSON. The Extensible Service Proxy (ESP) transcodes HTTP/JSON to gRPC.

This guide describes:

  * How to use annotations in your `.proto` file to specify data conversion from HTTP/JSON to gRPC
  * How to deploy your service in Endpoints to use this feature
  * Where to find more reference information about designing and implementing transcoding for gRPC services



It assumes that you have already completed our gRPC [Tutorials](https://docs.cloud.google.com/endpoints/docs/grpc/tutorials) and are familiar with basic [Endpoints for gRPC APIs](https://docs.cloud.google.com/endpoints/docs/grpc/about-grpc) concepts.

## Designing a transcoding-friendly API

Transcoding involves mapping HTTP/JSON requests and their parameters to gRPC methods and _their_ parameters and return types. Because of this, while it's possible to map an HTTP/JSON request to any arbitrary API method, it helps to do so if the gRPC API is structured in a **resource-oriented way** , just like a traditional HTTP [REST](https://wikipedia.org/wiki/Representational_state_transfer) API. In other words, you design the API service so that it uses a small number of **standard methods** , corresponding to **HTTP verbs** such as `GET` and `PUT`, that operate on the service's **resources** and **collections** of resources, which are themselves a type of resource. These standard methods are `List`, `Get`, `Create`, `Update`, and `Delete`.

If necessary, the API can also have some non-standard **custom methods** , though these aren't quite as straightforward to map.

You can find out much more about resource-oriented design and standard transcoding mappings in the [API design guide](https://docs.cloud.google.com/apis/design). This design guide is the design standard that's followed in Google when designing public APIs like [Cloud APIs](https://docs.cloud.google.com/apis/docs/overview). While you don't need to follow this guide to use gRPC transcoding, we strongly recommend it. In particular, the following pages can help you understand these design principles and add useful transcoding mappings to your methods:

  * [Resource oriented design](https://docs.cloud.google.com/apis/design/resources)
  * [Standard methods](https://docs.cloud.google.com/apis/design/standard_methods)
  * [Custom methods](https://docs.cloud.google.com/apis/design/custom_methods)
  * [HTTP verbs](https://docs.cloud.google.com/apis/design/http_verbs): this page provides additional guidelines for your method implementations if they're going to be accessed over HTTP.



The following reference page might also be useful:

  * [Http rule reference](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.HttpRule): a comprehensive reference for HTTP mapping rules,



In the rest of this document, you use the Bookstore example you used in our [Tutorials](https://docs.cloud.google.com/endpoints/docs/grpc/tutorials), which already uses these principles. The Bookstore has "shelf" collections of "book" resources, which users can `List`, `Get`, `Create`, or `Delete`.

## Where to configure transcoding

gRPC transcoding is enabled by default, and you _can_ use it without any configuration at all. Follow the instructions for deploying a service using transcoding. After, when you send an HTTP `POST` request to the URL path `GRPC_SERVICE_FULL_NAME/METHOD_NAME>` with the method's request message field values (if any) as JSON in the HTTP request body, ESP sends the request message to the appropriate gRPC method. In the preceding example, `GRPC_SERVICE_FULL_NAME` is the full name of your gRPC service and `METHOD_NAME` is the name of the method.

For example, if you send a `POST` to the Bookstore's `ListShelves` URL as follows:
    
    
    curl -XPOST http://mydomain/endpoints.examples.bookstore.Bookstore/ListShelves
    

You get a current list of shelves back in JSON form.

**Warning:** Using http method `POST` with the URL path `GRPC_SERVICE_FULL_NAME/METHOD_NAME>` is supported by default. Do not add additional mapping for this method in the proto file's `google.api.http` annotation or in the `http.rules` section of the service config yaml file. This will result in a "duplicate http pattern" error.

However, it's **strongly preferable** in terms of HTTP interface design to explicitly configure mappings, as described in the rest of this document.

The gRPC API configuration standard for service configuration lets you specify exactly how data should be translated from HTTP/JSON to gRPC. Two mechanisms are supported for doing this: direct annotations in your `.proto` file, and in YAML as part of your [gRPC API configuration](https://docs.cloud.google.com/endpoints/docs/grpc/grpc-service-config) file. We recommend using `proto` annotations for ease of reading and maintenance. For more information on YAML configuration and when you might need to use it, see [Configuring transcoding in YAML](https://docs.cloud.google.com/endpoints/docs/grpc/transcoding#configuring_transcoding_in_yaml).

Here's an example using the recommended approach from the [Bookstore](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/endpoints/bookstore-grpc/http_bookstore.proto):
    
    
    // Returns a specific bookstore shelf.
    rpc GetShelf(GetShelfRequest) returns (Shelf) {
      // Client example - returns the first shelf:
      //   curl http://DOMAIN_NAME/v1/shelves/1
      option (google.api.http) = { get: "/v1/shelves/{shelf}" };
    }
    
    ...
    // Request message for GetShelf method.
    message GetShelfRequest {
      // The ID of the shelf resource to retrieve.
      int64 shelf = 1;
    }
    

The annotation tells ESP that making an HTTP `GET` request with the URL `http://mydomain/v1/shelves/1` calls the gRPC server's `GetShelf()` method, with a `GetShelfRequest` containing the requested shelf ID `shelf` (in this case, `1`).

## Adding transcoding mappings

This section describes some additional mapping annotations from the Bookstore sample. There are two sample `proto` files in the Bookstore sample so that you can deploy it both with or without the transcoding mappings, and compare the differences in the `proto` files:

  * [`bookstore.proto`](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/endpoints/bookstore-grpc/bookstore.proto): used in the Endpoints [Tutorials](https://docs.cloud.google.com/endpoints/docs/grpc/tutorials) and doesn't have transcoding mappings.
  * [`http_bookstore.proto`](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/endpoints/bookstore-grpc/http_bookstore.proto): transcoding bindings added.



For a more comprehensive guide to specifying transcoding mappings, see [Standard methods](https://docs.cloud.google.com/apis/design/standard_methods), [Custom methods](https://docs.cloud.google.com/apis/design/custom_methods), and the [HTTP rule reference](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.HttpRule).

### Map a `List` method

The `List` method is defined in the `.proto` file with its response type:
    
    
      // Returns a list of all shelves in the bookstore.
      rpc ListShelves(google.protobuf.Empty) returns (ListShelvesResponse) {
        // Define HTTP mapping.
        // Client example (Assuming your service is hosted at the given 'DOMAIN_NAME'):
        //   curl http://DOMAIN_NAME/v1/shelves
        **option (google.api.http) = { get: "/v1/shelves" };**
      }
    ...
    message ListShelvesResponse {
      // Shelves in the bookstore.
      repeated Shelf shelves = 1;
    }

The annotation in bold specifies the HTTP mapping for this method.

  * `option (google.api.http)` specifies that this method is a gRPC HTTP mapping annotation.
  * `get` specifies that this method is mapped to an HTTP `GET` request.
  * `"/v1/shelves"` is the URL path template (appended to your service's domain) that the `GET` request uses to call this method. The URL path is also known as the resource path because it typically specifies the "thing" or resource you want to use. In this case, all our Bookstore's shelf resources.



For example, if a client calls this method by sending a `GET` to the URL `http://mydomain/v1/shelves`, ESP calls the gRPC method `ListShelves()`. The gRPC backend then returns the shelves, which ESP converts to JSON format and returns to the client.

### Map a `Get` method

The Bookstore's `GetShelf` method is defined in the `.proto` file with its request and response types:
    
    
    // Returns a specific bookstore shelf.
    rpc GetShelf(GetShelfRequest) returns (Shelf) {
      // Client example - returns the first shelf:
      //   curl http://DOMAIN_NAME/v1/shelves/1
      **option (google.api.http) = { get: "/v1/shelves/{shelf}" };**
    }
    
    ...
    // Request message for GetShelf method.
    message GetShelfRequest {
      // The ID of the shelf resource to retrieve.
      int64 shelf = 1;
    }
    ...
    // A shelf resource.
    message Shelf {
      // A unique shelf id.
      int64 id = 1;
      // A theme of the shelf (fiction, poetry, etc).
      string theme = 2;
    }

The annotation in bold specifies the HTTP mapping for this method.

  * `option (google.api.http)` specifies that this method is a gRPC HTTP mapping annotation.
  * `get` specifies that this method is mapped to an HTTP `GET` request.
  * `"/v1/shelves/{shelf}"`is the URL path for the request, as before, but it specifies `/v1/shelves/` and then `{shelf}`. This curly-brace notation tells ESP that whatever is in `{shelf}` is the value it should provide for `shelf` in the method's `GetShelfRequest` parameter.



If a client calls this method by sending a `GET` to the URL `http://mydomain/v1/shelves/4`, ESP creates a `GetShelfRequest` with a `shelf` value of `4` and then calls the gRPC method `GetShelf()` with it. The gRPC backend then returns the requested `Shelf` with the ID `4`, which ESP converts to JSON format and returns to the client.

This method only requires a single request field value to be provided by the client, `shelf`, which you specify in the URL path template with the curly-brace "capture" notation. You can also capture multiple parts of the URL if necessary to identify the requested resource. For example, the `GetBook` method needs the client to specify both the shelf ID and the book ID in the URL:
    
    
    // Returns a specific book.
    rpc GetBook(GetBookRequest) returns (Book) {
      // Client example - get the first book from the second shelf:
      //   curl http://DOMAIN_NAME/v1/shelves/2/books/1
      option (google.api.http) = { get: "/v1/shelves/{shelf}/books/{book}" };
    }
    ...
    // Request message for GetBook method.
    message GetBookRequest {
      // The ID of the shelf from which to retrieve a book.
      int64 shelf = 1;
      // The ID of the book to retrieve.
      int64 book = 2;
    }
    

As well as literals and capture braces for field values, URL path templates can use wildcards to indicate that anything in this part of the URL should be captured. The `{shelf}` notation used in the preceding example is actually a shortcut for `{shelf=*}`. You can find out more about the rules for path templates in the [HTTP rule reference](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.HttpRule).

In the case of this method type, there's no specified HTTP request body. You can find more guidelines for mapping `Get` methods, including using query parameters, in [Standard methods](https://docs.cloud.google.com/apis/design/standard_methods#get).

### Map a `Create` method

The Bookstore's `CreateShelf` method maps to HTTP `POST`.
    
    
      // Creates a new shelf in the bookstore.
      rpc CreateShelf(CreateShelfRequest) returns (Shelf) {
        // Client example:
        //   curl -d '{"theme":"Music"}' http://DOMAIN_NAME/v1/shelves
        **option (google.api.http) = {
          post: "/v1/shelves"
          body: "shelf"
        };**
      }
    ...
    // Request message for CreateShelf method.
    message CreateShelfRequest {
      // The shelf resource to create.
      Shelf shelf = 1;
    }
    ...
    // A shelf resource.
    message Shelf {
      // A unique shelf id.
      int64 id = 1;
      // A theme of the shelf (fiction, poetry, etc).
      string theme = 2;
    }

  * `option (google.api.http)` specifies that this method is a gRPC HTTP mapping annotation.
  * `post` specifies that this method is mapped to an HTTP `POST` request.
  * `"/v1/shelves"` is the URL path for the request, as before.
  * `body: "shelf"`is used in the HTTP request body to specify the resource you want to add, in JSON format.



So, for example, if a client called this method like this:
    
    
    curl -d '{"theme":"Music"}' http://DOMAIN_NAME/v1/shelves
    

ESP uses the JSON body to create a `Shelf` value with the theme `"Music"` for the `CreateShelfRequest`, and then calls the gRPC `CreateShelf()` method. Note that the client _doesn't_ provide the `id` value for the `Shelf`. The Bookstore's shelf IDs are provided by the service when creating a new shelf. You provide this type of information to users of your service in API documentation.

### Use wildcard in body

The special name `*` can be used in the body mapping to indicate that every field not bound by the path template should be mapped to the request body. This enables the following alternative definition of the `CreateShelf` method.
    
    
      // Creates a new shelf in the bookstore.
      rpc CreateShelf(CreateShelfRequest) returns (Shelf) {
        // Client example:
        //   curl -d '{"shelf_theme":"Music", "shelf_size": 20}' http://DOMAIN_NAME/v1/shelves/123
        **option (google.api.http) = {
          post: "/v1/shelves/{shelf_id}"
          body: "*"
        };**
      }
    ...
    // Request message for CreateShelf method.
    message CreateShelfRequest {
      // A unique shelf id.
      int64 shelf_id = 1;
      // A theme of the shelf (fiction, poetry, etc).
      string shelf_theme = 2;
      // The size of the shelf
      int64 shelf_size = 3;
    }

  * `option (google.api.http)` specifies that this method is a gRPC HTTP mapping annotation.
  * `post` specifies that this method is mapped to an HTTP `POST` request.
  * `"/v1/shelves/{shelf_id}"` is the URL path for the request. Whatever is in `{shelf_id}` is the value of the `shelf_id` field in `CreateShelfRequest`.
  * `body: "*"`is used in the HTTP request body to specify all remaining request fields except `shelf_id` in this example, and they are `shelf_theme` and `shelf_size`. For any fields in JSON body with these two names, their values will be used in the corresponding fields of `CreateShelfRequest`.



For example, if a client called this method like this:
    
    
    curl -d '{"shelf_theme":"Music", "shelf_size": 20}' http://DOMAIN_NAME/v1/shelves/123
    

ESP uses the JSON body and the path template to create a `CreateShelfRequest{shelf_id: 123 shelf_theme: "Music" shelf_size: 20}`, and then uses it to call the gRPC `CreateShelf()` method. For details, see the [HttpRule](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.HttpRule).

## Configuring transcoding in YAML

**Note:** [(ESPv2)](https://docs.cloud.google.com/endpoints/docs/grpc/glossary#extensible_service_proxy_v2) doesn't support this approach.

An alternative approach is where you specify your HTTP to gRPC mappings in your [gRPC API configuration](https://docs.cloud.google.com/endpoints/docs/grpc/grpc-service-config) YAML file rather than in your `.proto` file. You might need to configure transcoding in a YAML file if you have a single `proto` API definition that's used in multiple services, with different mappings specified for each service.

The `rules` in the `http` section of your YAML file specify how to map HTTP/JSON requests to gRPC methods:
    
    
    http:
      rules:
      ...
      #
      # 'GetShelf' is available via the GET HTTP verb and '/shelves/{shelf}' URL
      # path, where {shelf} is the value of the 'shelf' field of 'GetShelfRequest'
      # protobuf message.
      #
      # Client example - returns the first shelf:
      #   curl http://DOMAIN_NAME/v1/shelves/1
      #
      - selector: endpoints.examples.bookstore.Bookstore.GetShelf
        get: /v1/shelves/{shelf}
      ...
    

A more complete example of using this approach for the example Bookstore service is in [`api_config_http.yaml`](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/endpoints/bookstore-grpc/api_config_http.yaml).

## Deploying a service that uses transcoding

Deploying a gRPC service that uses transcoding is much the same as deploying any other gRPC service, with one major difference. In the [Tutorials](https://docs.cloud.google.com/endpoints/docs/grpc/tutorials), the example needed to accept gRPC requests from the sample client. However, if you want the Bookstore to accept HTTP requests as well, you need to do some extra configuration for ESP. Clients use the `HTTP1.1` protocol to send JSON/HTTP requests to ESP, so ESP either needs to be configured to use SSL (the SSL port can support both request types) or needs to have a special port enabled to accept these calls. Deployment is otherwise largely the same as in the tutorial for your chosen environment.

### Ensure HTTP rules are deployed

If you've already downloaded the Bookstore example for the [Tutorials](https://docs.cloud.google.com/endpoints/docs/grpc/tutorials), note that you need to download a slightly different version of the `.proto` file with annotations, [`http_bookstore.proto`](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/endpoints/bookstore-grpc/http_bookstore.proto). You also need to clone the [`googleapis`](https://github.com/googleapis/googleapis) repository from GitHub before running `protoc`, as you need [`annotations.proto`](https://github.com/googleapis/googleapis/blob/master/google/api/annotations.proto) in your include path.
    
    
        git clone https://github.com/googleapis/googleapis
    
        GOOGLEAPIS_DIR=<your-local-googleapis-folder>
    

Then you create a new `.pb` descriptor from `http_bookstore.proto` when [deploying](https://docs.cloud.google.com/endpoints/docs/grpc/deploy-endpoints-config) your configuration to Endpoints:
    
    
        protoc \
            --include_imports \
            --include_source_info \
            --proto_path=${GOOGLEAPIS_DIR} \
            --proto_path=. \
            --descriptor_set_out=api_descriptor.pb \
            http_bookstore.proto
    

If you are using the alternative method of configuring HTTP mappings in your [gRPC API configuration](https://docs.cloud.google.com/endpoints/docs/grpc/grpc-service-config) YAML file, you also need to ensure that the relevant rules are deployed when [deploying](https://docs.cloud.google.com/endpoints/docs/grpc/deploy-endpoints-config) your configuration to Endpoints. To try this with the Bookstore service, its basic rules are in the [`api_config.yaml`](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/endpoints/bookstore-grpc/api_config.yaml) file and its HTTP rules are in the [`api_config_http.yaml`](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/endpoints/bookstore-grpc/api_config_http.yaml) file:
    
    
        gcloud endpoints services deploy api_descriptor.pb api_config.yaml api_config_http.yaml
    

The above gcloud command only supports one proto descriptor file and it has to be the first file in the gcloud command arguments. If you have multiple gRPC services in different proto files, please use the `protoc` command-line tool to combine them into one descriptor file.

### Using SSL

**Note:** this is only needed for ESPv1. [(ESPv2)](https://docs.cloud.google.com/endpoints/docs/grpc/glossary#extensible_service_proxy_v2) `--listener_port` works for both http and grpc.

If SSL is enabled for communication between your clients and ESP, then clients can use the same port to make gRPC or `HTTP1.1` calls. You can find out how to set up SSL for a Endpoints service in [Enabling SSL](https://docs.cloud.google.com/endpoints/docs/grpc/enabling-ssl).

Specify a port for ESP to accept SSL calls using the `--ssl_port` flag in the Google Kubernetes Engine configuration file (GKE) or the `docker run` command (Compute Engine/Docker).
    
    
        args: [
          "--http_port", "8080",
          "--ssl_port", "443",  # enable SSL port at 443 to serve https requests
          "--backend",  "grpc://127.0.0.1:8081",  # gRPC backend.
          "--service", "SERVICE_NAME",
          "--rollout_strategy", "managed",
        ]
    

### Setting up an `HTTP1.1` port

**Note:** this is only needed for ESPv1. [(ESPv2)](https://docs.cloud.google.com/endpoints/docs/grpc/glossary#extensible_service_proxy_v2) `--listener_port` works for both http and grpc.

If you are't using SSL, you need to set up a separate port for `HTTP1.1` requests because gRPC and `HTTP1.1` can't share the same port without SSL. Use the `--http_port` flag in the GKE configuration file or `docker run` command to specify a port to accept `HTTP1.1` calls. If you also want ESP to accept gRPC calls, you need to use the `--http2_port` flag as well to specify a gRPC port.
    
    
        args: [
          "--http_port", "8080",  # for HTTP 1.1
          "--http2_port", "8090",  # for gRPC
          "--backend", "grpc://127.0.0.1:8081",  # gRPC backend.
          "--service", "SERVICE_NAME",
          "--rollout_strategy", "managed",
        ]
    

## Calling a service using transcoding

This section describes the service setup and how to make HTTP calls to the service.

### Service setup

This assumes that you've already completed the basic gRPC service [Tutorials](https://docs.cloud.google.com/endpoints/docs/grpc/tutorials) for your chosen environment and have a GKE cluster or Compute Engine instance to run the example.

  1. First ensure that you've deployed the HTTP-enabled Bookstore service configuration to Endpoints, as described in [Ensure HTTP rules are deployed](https://docs.cloud.google.com/endpoints/docs/grpc/transcoding#ensure_http_rules_are_deployed).
  2. Deploy the backend and ESP as described in the tutorial for your chosen platform, using the `--http_port` flag to enable a port for `HTTP1.1` requests:

     * GKE deployment: Follow the instructions in [Deploying the sample API and ESP to the cluster](https://docs.cloud.google.com/endpoints/docs/grpc/get-started-kubernetes-engine#deploying_the_sample_api_and_esp_to_the_cluster), making sure the `"--http_port"` flag is specified in the GKE configuration file.
     * Compute Engine deployment: Follow the instructions in [Running the sample API and ESP in a Docker container](https://docs.cloud.google.com/endpoints/docs/grpc/get-started-compute-engine-docker#running_the_sample_api_and_esp_in_a_docker_container). Ensure the `--http_port` flag is specified in the `docker run` command when running the pre-packaged ESP Docker container.



### Make HTTP calls to the service

**Note:** Every field provided in a request message must contain a valid value. For example, if a proto request message includes the field `int64 book_id`, you must either specify a valid integer value or remove the field entirely. For example, `mygateway.dev?book_id=0` contains a valid value but `mygateway.dev?book_id=` does not and should be removed or provide a valid integer value.

  1. Get the ESP's external IP address and set it to `$ESP_IP`.
  2. Make the following HTTP request with `curl`
         
         curl http://$ESP_IP/v1/shelves
         

(or use the same URL with `https://` if you're using SSL). The server responds with:
         
         {"shelves":[{"id":"1","theme":"Fiction"},{"id":"2","theme":"Fantasy"}]}
         

If the output displays a binary response, check your port configuration because you might be hitting your HTTP2 port instead of your HTTP port.

  3. Try a `Create` method. `CreateShelf` requires an [API key](https://docs.cloud.google.com/endpoints/docs/grpc/restricting-api-access-with-api-keys), so you need to [create a key](https://docs.cloud.google.com/docs/authentication/api-keys#creating_an_api_key) for your project and set it as `$KEY`. Now call:
         
         curl -d '{"theme":"Music"}' http://$ESP_IP/v1/shelves?key=$KEY
         

If you call `GetShelves` again you should see your new shelf.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
