---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api
title: Namespace Google.Api (2.17.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:57:32.680329+00:00
---

# Namespace Google.Api (2.17.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Namespace Google.Api (2.17.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.17.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api)
  * [ 2.15.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/2.15.0/Google.Api)
  * [ 2.10.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/2.10.0/Google.Api)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/2.2.0/Google.Api)



## Classes 

### [Advice](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Advice)

Generated advice about this change, used for providing more information about how a change will affect the existing service.

### [AnnotationsExtensions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.AnnotationsExtensions)

Holder for extension identifiers generated from the top level of google/api/annotations.proto

### [AnnotationsReflection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.AnnotationsReflection)

Holder for reflection information generated from google/api/annotations.proto

### [AuthProvider](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.AuthProvider)

Configuration for an authentication provider, including support for [JSON Web Token (JWT)](https://tools.ietf.org/html/draft-ietf-oauth-json-web-token-32).

### [AuthReflection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.AuthReflection)

Holder for reflection information generated from google/api/auth.proto

### [AuthRequirement](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.AuthRequirement)

User-defined authentication requirements, including support for [JSON Web Token (JWT)](https://tools.ietf.org/html/draft-ietf-oauth-json-web-token-32).

### [Authentication](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Authentication)

`Authentication` defines the authentication configuration for API methods provided by an API service.

Example:
    
    
    name: calendar.googleapis.com
    authentication:
      providers:
      - id: google_calendar_auth
        jwks_uri: https://www.googleapis.com/oauth2/v1/certs
        issuer: https://securetoken.google.com
      rules:
      - selector: "*"
        requirements:
          provider_id: google_calendar_auth
      - selector: google.calendar.Delegate
        oauth:
          canonical_scopes: https://www.googleapis.com/auth/calendar.read
    

### [AuthenticationRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.AuthenticationRule)

Authentication rules for the service.

By default, if a method has any authentication requirements, every request must include a valid credential matching one of the requirements. It's an error to include more than one kind of credential in a single request.

If a method doesn't have any auth requirements, request credentials will be ignored.

### [Backend](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Backend)

`Backend` defines the backend configuration for a service.

### [BackendReflection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.BackendReflection)

Holder for reflection information generated from google/api/backend.proto

### [BackendRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.BackendRule)

A backend rule provides configuration for an individual API element.

### [BackendRule.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.BackendRule.Types)

Container for nested types declared in the BackendRule message type.

### [Billing](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Billing)

Billing related configuration of the service.

The following example shows how to configure monitored resources and metrics for billing, `consumer_destinations` is the only supported destination and the monitored resources need at least one label key `cloud.googleapis.com/location` to indicate the location of the billing usage, using different monitored resources between monitoring and billing is recommended so they can be evolved independently:
    
    
    monitored_resources:
    - type: library.googleapis.com/billing_branch
      labels:
      - key: cloud.googleapis.com/location
        description: |
          Predefined label to support billing location restriction.
      - key: city
        description: |
          Custom label to define the city where the library branch is located
          in.
      - key: name
        description: Custom label to define the name of the library branch.
    metrics:
    - name: library.googleapis.com/book/borrowed_count
      metric_kind: DELTA
      value_type: INT64
      unit: "1"
    billing:
      consumer_destinations:
      - monitored_resource: library.googleapis.com/billing_branch
        metrics:
        - library.googleapis.com/book/borrowed_count
    

### [Billing.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Billing.Types)

Container for nested types declared in the Billing message type.

### [Billing.Types.BillingDestination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Billing.Types.BillingDestination)

Configuration of a specific billing destination (Currently only support bill against consumer project).

### [BillingReflection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.BillingReflection)

Holder for reflection information generated from google/api/billing.proto

### [ClientExtensions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ClientExtensions)

Holder for extension identifiers generated from the top level of google/api/client.proto

### [ClientLibrarySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ClientLibrarySettings)

Details about how and where to publish client libraries.

### [ClientReflection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ClientReflection)

Holder for reflection information generated from google/api/client.proto

### [CommonLanguageSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.CommonLanguageSettings)

Required information for every language.

### [ConfigChange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ConfigChange)

Output generated from semantically comparing two versions of a service configuration.

Includes detailed information about a field that have changed with applicable advice about potential consequences for the change, such as backwards-incompatibility.

### [ConfigChangeReflection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ConfigChangeReflection)

Holder for reflection information generated from google/api/config_change.proto

### [ConsumerReflection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ConsumerReflection)

Holder for reflection information generated from google/api/consumer.proto

### [Context](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Context)

`Context` defines which contexts an API requests.

Example:
    
    
    context:
      rules:
      - selector: "*"
        requested:
        - google.rpc.context.ProjectContext
        - google.rpc.context.OriginContext
    

The above specifies that all methods in the API request `google.rpc.context.ProjectContext` and `google.rpc.context.OriginContext`.

Available context types are defined in package `google.rpc.context`.

This also provides mechanism to allowlist any protobuf message extension that can be sent in grpc metadata using “x-goog-ext-<extension_id>-bin” and “x-goog-ext-<extension_id>-jspb” format. For example, list any service specific protobuf types that can appear in grpc metadata as follows in your yaml file:

Example:
    
    
    context:
      rules:
       - selector: "google.example.library.v1.LibraryService.CreateBook"
         allowed_request_extensions:
         - google.foo.v1.NewExtension
         allowed_response_extensions:
         - google.foo.v1.NewExtension
    

You can also specify extension ID instead of fully qualified extension name here.

### [ContextReflection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ContextReflection)

Holder for reflection information generated from google/api/context.proto

### [ContextRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ContextRule)

A context rule provides information about the context for an individual API element.

### [Control](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Control)

Selects and configures the service controller used by the service.

Example:
    
    
    control:
      environment: servicecontrol.googleapis.com
    

### [ControlReflection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ControlReflection)

Holder for reflection information generated from google/api/control.proto

### [CppSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.CppSettings)

Settings for C++ client libraries.

### [CustomHttpPattern](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.CustomHttpPattern)

A custom pattern is used for defining custom HTTP verb.

### [Distribution](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Distribution)

`Distribution` contains summary statistics for a population of values. It optionally contains a histogram representing the distribution of those values across a set of buckets.

The summary statistics are the count, mean, sum of the squared deviation from the mean, the minimum, and the maximum of the set of population of values. The histogram is based on a sequence of buckets and gives a count of values that fall into each bucket. The boundaries of the buckets are given either explicitly or by formulas for buckets of fixed or exponentially increasing widths.

Although it is not forbidden, it is generally a bad idea to include non-finite values (infinities or NaNs) in the population of values, as this will render the `mean` and `sum_of_squared_deviation` fields meaningless.

### [Distribution.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Distribution.Types)

Container for nested types declared in the Distribution message type.

### [Distribution.Types.BucketOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Distribution.Types.BucketOptions)

`BucketOptions` describes the bucket boundaries used to create a histogram for the distribution. The buckets can be in a linear sequence, an exponential sequence, or each bucket can be specified explicitly. `BucketOptions` does not include the number of values in each bucket.

A bucket has an inclusive lower bound and exclusive upper bound for the values that are counted for that bucket. The upper bound of a bucket must be strictly greater than the lower bound. The sequence of N buckets for a distribution consists of an underflow bucket (number 0), zero or more finite buckets (number 1 through N - 2) and an overflow bucket (number N - 1). The buckets are contiguous: the lower bound of bucket i (i > 0) is the same as the upper bound of bucket i - 1. The buckets span the whole range of finite values: lower bound of the underflow bucket is -infinity and the upper bound of the overflow bucket is +infinity. The finite buckets are so-called because both bounds are finite.

### [Distribution.Types.BucketOptions.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Distribution.Types.BucketOptions.Types)

Container for nested types declared in the BucketOptions message type.

### [Distribution.Types.BucketOptions.Types.Explicit](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Distribution.Types.BucketOptions.Types.Explicit)

Specifies a set of buckets with arbitrary widths.

There are `size(bounds) + 1` (= N) buckets. Bucket `i` has the following boundaries:

Upper bound (0 <= i < N-1): bounds[i] Lower bound (1 <= i < N); bounds[i - 1]

The `bounds` field must contain at least one element. If `bounds` has only one element, then there are no finite buckets, and that single element is the common boundary of the overflow and underflow buckets.

### [Distribution.Types.BucketOptions.Types.Exponential](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Distribution.Types.BucketOptions.Types.Exponential)

Specifies an exponential sequence of buckets that have a width that is proportional to the value of the lower bound. Each bucket represents a constant relative uncertainty on a specific value in the bucket.

There are `num_finite_buckets + 2` (= N) buckets. Bucket `i` has the following boundaries:

Upper bound (0 <= i < N-1): scale * (growth_factor ^ i).

Lower bound (1 <= i < N): scale * (growth_factor ^ (i - 1)).

### [Distribution.Types.BucketOptions.Types.Linear](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Distribution.Types.BucketOptions.Types.Linear)

Specifies a linear sequence of buckets that all have the same width (except overflow and underflow). Each bucket represents a constant absolute uncertainty on the specific value in the bucket.

There are `num_finite_buckets + 2` (= N) buckets. Bucket `i` has the following boundaries:

Upper bound (0 <= i < N-1): offset + (width * i).

Lower bound (1 <= i < N): offset + (width * (i - 1)).

### [Distribution.Types.Exemplar](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Distribution.Types.Exemplar)

Exemplars are example points that may be used to annotate aggregated distribution values. They are metadata that gives information about a particular value added to a Distribution bucket, such as a trace ID that was active when a value was added. They may contain further information, such as a example values and timestamps, origin, etc.

### [Distribution.Types.Range](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Distribution.Types.Range)

The range of the population values.

### [DistributionReflection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.DistributionReflection)

Holder for reflection information generated from google/api/distribution.proto

### [Documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Documentation)

`Documentation` provides the information for describing a service.

Example: <pre><code>documentation: summary: > The Google Calendar API gives access to most calendar features. pages:

  * name: Overview content: &#40;== include google/foo/overview.md ==&#41;
  * name: Tutorial content: &#40;== include google/foo/tutorial.md ==&#41; subpages:
    * name: Java content: &#40;== include google/foo/tutorial_java.md ==&#41; rules:
  * selector: google.calendar.Calendar.Get description: > ...
  * selector: google.calendar.Calendar.Put description: > ... </code></pre> Documentation is provided in markdown syntax. In addition to standard markdown features, definition lists, tables and fenced code blocks are supported. Section headers can be provided and are interpreted relative to the section nesting of the context where a documentation fragment is embedded.



Documentation from the IDL is merged with documentation defined via the config at normalization time, where documentation provided by config rules overrides IDL provided.

A number of constructs specific to the API platform are supported in documentation text.

In order to reference a proto element, the following notation can be used: <pre><code>&#91;fully.qualified.proto.name]&#91;]</code></pre> To override the display text used for the link, this can be used: <pre><code>&#91;display text]&#91;fully.qualified.proto.name]</code></pre> Text can be excluded from doc using the following notation: <pre><code>&#40;-- internal comment --&#41;</code></pre>

A few directives are available in documentation. Note that directives must appear on a single line to be properly identified. The `include` directive includes a markdown file from an external source: <pre><code>&#40;== include path/to/file ==&#41;</code></pre> The `resource_for` directive marks a message to be the resource of a collection in REST view. If it is not specified, tools attempt to infer the resource from the operations in a collection: <pre><code>&#40;== resource_for v1.shelves.books ==&#41;</code></pre> The directive `suppress_warning` does not directly affect documentation and is documented together with service config validation.

### [DocumentationReflection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.DocumentationReflection)

Holder for reflection information generated from google/api/documentation.proto

### [DocumentationRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.DocumentationRule)

A documentation rule provides information about individual API elements.

### [DotnetSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.DotnetSettings)

Settings for Dotnet client libraries.

### [Endpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Endpoint)

`Endpoint` describes a network address of a service that serves a set of APIs. It is commonly known as a service endpoint. A service may expose any number of service endpoints, and all service endpoints share the same service definition, such as quota limits and monitoring metrics.

Example:
    
    
    type: google.api.Service
    name: library-example.googleapis.com
    endpoints:
      # Declares network address `https://library-example.googleapis.com`
      # for service `library-example.googleapis.com`. The `https` scheme
      # is implicit for all service endpoints. Other schemes may be
      # supported in the future.
    - name: library-example.googleapis.com
      allow_cors: false
    - name: content-staging-library-example.googleapis.com
      # Allows HTTP OPTIONS calls to be passed to the API frontend, for it
      # to decide whether the subsequent cross-origin request is allowed
      # to proceed.
      allow_cors: true
    

### [EndpointReflection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.EndpointReflection)

Holder for reflection information generated from google/api/endpoint.proto

### [ErrorReasonReflection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ErrorReasonReflection)

Holder for reflection information generated from google/api/error_reason.proto

### [FieldBehaviorExtensions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.FieldBehaviorExtensions)

Holder for extension identifiers generated from the top level of google/api/field_behavior.proto

### [FieldBehaviorReflection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.FieldBehaviorReflection)

Holder for reflection information generated from google/api/field_behavior.proto

### [FieldInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.FieldInfo)

Rich semantic information of an API field beyond basic typing.

### [FieldInfo.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.FieldInfo.Types)

Container for nested types declared in the FieldInfo message type.

### [FieldInfoExtensions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.FieldInfoExtensions)

Holder for extension identifiers generated from the top level of google/api/field_info.proto

### [FieldInfoReflection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.FieldInfoReflection)

Holder for reflection information generated from google/api/field_info.proto

### [FieldPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.FieldPolicy)

Google API Policy Annotation

This message defines a simple API policy annotation that can be used to annotate API request and response message fields with applicable policies. One field may have multiple applicable policies that must all be satisfied before a request can be processed. This policy annotation is used to generate the overall policy that will be used for automatic runtime policy enforcement and documentation generation.

### [GoSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.GoSettings)

Settings for Go client libraries.

### [Http](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Http)

Defines the HTTP configuration for an API service. It contains a list of [HttpRule][google.api.HttpRule], each specifying the mapping of an RPC method to one or more HTTP REST API methods.

### [HttpBody](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.HttpBody)

Message that represents an arbitrary HTTP body. It should only be used for payload formats that can't be represented as JSON, such as raw binary or an HTML page.

This message can be used both in streaming and non-streaming API methods in the request as well as the response.

It can be used as a top-level request field, which is convenient if one wants to extract parameters from either the URL or HTTP template into the request fields and also want access to the raw HTTP body.

Example:
    
    
    message GetResourceRequest {
      // A unique request id.
      string request_id = 1;
    
      // The raw HTTP body is bound to this field.
      google.api.HttpBody http_body = 2;
    
    }
    
    service ResourceService {
      rpc GetResource(GetResourceRequest)
        returns (google.api.HttpBody);
      rpc UpdateResource(google.api.HttpBody)
        returns (google.protobuf.Empty);
    
    }
    

Example with streaming methods:
    
    
    service CaldavService {
      rpc GetCalendar(stream google.api.HttpBody)
        returns (stream google.api.HttpBody);
      rpc UpdateCalendar(stream google.api.HttpBody)
        returns (stream google.api.HttpBody);
    
    }
    

Use of this type only changes how the request and response bodies are handled, all other features will continue to work unchanged.

### [HttpReflection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.HttpReflection)

Holder for reflection information generated from google/api/http.proto

### [HttpRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.HttpRule)

gRPC Transcoding

gRPC Transcoding is a feature for mapping between a gRPC method and one or more HTTP REST endpoints. It allows developers to build a single API service that supports both gRPC APIs and REST APIs. Many systems, including [Google APIs](https://github.com/googleapis/googleapis), [Cloud Endpoints](https://cloud.google.com/endpoints), [gRPC Gateway](https://github.com/grpc-ecosystem/grpc-gateway), and [Envoy](https://github.com/envoyproxy/envoy) proxy support this feature and use it for large scale production services.

`HttpRule` defines the schema of the gRPC/REST mapping. The mapping specifies how different portions of the gRPC request message are mapped to the URL path, URL query parameters, and HTTP request body. It also controls how the gRPC response message is mapped to the HTTP response body. `HttpRule` is typically specified as an `google.api.http` annotation on the gRPC method.

Each mapping specifies a URL path template and an HTTP method. The path template may refer to one or more fields in the gRPC request message, as long as each field is a non-repeated field with a primitive (non-message) type. The path template controls how fields of the request message are mapped to the URL path.

Example:
    
    
    service Messaging {
      rpc GetMessage(GetMessageRequest) returns (Message) {
        option (google.api.http) = {
            get: "/v1/{name=messages/*}"
        };
      }
    }
    message GetMessageRequest {
      string name = 1; // Mapped to URL path.
    }
    message Message {
      string text = 1; // The resource content.
    }
    

This enables an HTTP REST to gRPC mapping as below:

  * HTTP: `GET /v1/messages/123456`
  * gRPC: `GetMessage(name: "messages/123456")`



Any fields in the request message which are not bound by the path template automatically become HTTP query parameters if there is no HTTP request body. For example:
    
    
    service Messaging {
      rpc GetMessage(GetMessageRequest) returns (Message) {
        option (google.api.http) = {
            get:"/v1/messages/{message_id}"
        };
      }
    }
    message GetMessageRequest {
      message SubMessage {
        string subfield = 1;
      }
      string message_id = 1; // Mapped to URL path.
      int64 revision = 2;    // Mapped to URL query parameter `revision`.
      SubMessage sub = 3;    // Mapped to URL query parameter `sub.subfield`.
    }
    

This enables a HTTP JSON to RPC mapping as below:

  * HTTP: `GET /v1/messages/123456?revision=2&sub.subfield=foo`
  * gRPC: `GetMessage(message_id: "123456" revision: 2 sub: SubMessage(subfield: "foo"))`



Note that fields which are mapped to URL query parameters must have a primitive type or a repeated primitive type or a non-repeated message type. In the case of a repeated type, the parameter can be repeated in the URL as `...?param=A&param=B`. In the case of a message type, each field of the message is mapped to a separate parameter, such as `...?foo.a=A&foo.b=B&foo.c=C`.

For HTTP methods that allow a request body, the `body` field specifies the mapping. Consider a REST update method on the message resource collection:
    
    
    service Messaging {
      rpc UpdateMessage(UpdateMessageRequest) returns (Message) {
        option (google.api.http) = {
          patch: "/v1/messages/{message_id}"
          body: "message"
        };
      }
    }
    message UpdateMessageRequest {
      string message_id = 1; // mapped to the URL
      Message message = 2;   // mapped to the body
    }
    

The following HTTP JSON to RPC mapping is enabled, where the representation of the JSON in the request body is determined by protos JSON encoding:

  * HTTP: `PATCH /v1/messages/123456 { "text": "Hi!" }`
  * gRPC: `UpdateMessage(message_id: "123456" message { text: "Hi!" })`



The special name `*` can be used in the body mapping to define that every field not bound by the path template should be mapped to the request body. This enables the following alternative definition of the update method:
    
    
    service Messaging {
      rpc UpdateMessage(Message) returns (Message) {
        option (google.api.http) = {
          patch: "/v1/messages/{message_id}"
          body: "*"
        };
      }
    }
    message Message {
      string message_id = 1;
      string text = 2;
    }
    

The following HTTP JSON to RPC mapping is enabled:

  * HTTP: `PATCH /v1/messages/123456 { "text": "Hi!" }`
  * gRPC: `UpdateMessage(message_id: "123456" text: "Hi!")`



Note that when using `*` in the body mapping, it is not possible to have HTTP parameters, as all fields not bound by the path end in the body. This makes this option more rarely used in practice when defining REST APIs. The common usage of `*` is in custom methods which don't use the URL at all for transferring data.

It is possible to define multiple HTTP methods for one RPC by using the `additional_bindings` option. Example:
    
    
    service Messaging {
      rpc GetMessage(GetMessageRequest) returns (Message) {
        option (google.api.http) = {
          get: "/v1/messages/{message_id}"
          additional_bindings {
            get: "/v1/users/{user_id}/messages/{message_id}"
          }
        };
      }
    }
    message GetMessageRequest {
      string message_id = 1;
      string user_id = 2;
    }
    

This enables the following two alternative HTTP JSON to RPC mappings:

  * HTTP: `GET /v1/messages/123456`
  * gRPC: `GetMessage(message_id: "123456")`

  * HTTP: `GET /v1/users/me/messages/123456`

  * gRPC: `GetMessage(user_id: "me" message_id: "123456")`



Rules for HTTP mapping

  1. Leaf request fields (recursive expansion nested messages in the request message) are classified into three categories:
     * Fields referred by the path template. They are passed via the URL path.
     * Fields referred by the [HttpRule.body][google.api.HttpRule.body]. They are passed via the HTTP request body.
     * All other fields are passed via the URL query parameters, and the parameter name is the field path in the request message. A repeated field can be represented as multiple query parameters under the same name.
     * If [HttpRule.body][google.api.HttpRule.body] is "*", there is no URL query parameter, all fields are passed via URL path and HTTP request body.
     * If [HttpRule.body][google.api.HttpRule.body] is omitted, there is no HTTP request body, all fields are passed via URL path and URL query parameters.



Path template syntax
    
    
    Template = "/" Segments [ Verb ] ;
    Segments = Segment { "/" Segment } ;
    Segment  = "*" | "**" | LITERAL | Variable ;
    Variable = "{" FieldPath [ "=" Segments ] "}" ;
    FieldPath = IDENT { "." IDENT } ;
    Verb     = ":" LITERAL ;
    

The syntax `*` matches a single URL path segment. The syntax `**` matches zero or more URL path segments, which must be the last part of the URL path except the `Verb`.

The syntax `Variable` matches part of the URL path as specified by its template. A variable template must not contain other variables. If a variable matches a single path segment, its template may be omitted, e.g. `{var}` is equivalent to `{var=*}`.

The syntax `LITERAL` matches literal text in the URL path. If the `LITERAL` contains any reserved character, such characters should be percent-encoded before the matching.

If a variable contains exactly one path segment, such as `"{var}"` or `"{var=*}"`, when such a variable is expanded into a URL path on the client side, all characters except `[-_.~0-9a-zA-Z]` are percent-encoded. The server side does the reverse decoding. Such variables show up in the [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) as `{var}`.

If a variable contains multiple path segments, such as `"{var=foo/*}"` or `"{var=**}"`, when such a variable is expanded into a URL path on the client side, all characters except `[-_.~/0-9a-zA-Z]` are percent-encoded. The server side does the reverse decoding, except "%2F" and "%2f" are left unchanged. Such variables show up in the [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) as `{+var}`.

Using gRPC API Service Configuration

gRPC API Service Configuration (service config) is a configuration language for configuring a gRPC service to become a user-facing product. The service config is simply the YAML representation of the `google.api.Service` proto message.

As an alternative to annotating your proto file, you can configure gRPC transcoding in your service config YAML files. You do this by specifying a `HttpRule` that maps the gRPC method to a REST endpoint, achieving the same effect as the proto annotation. This can be particularly useful if you have a proto that is reused in multiple services. Note that any transcoding specified in the service config will override any matching transcoding configuration in the proto.

The following example selects a gRPC method and applies an `HttpRule` to it:
    
    
    http:
      rules:
        - selector: example.v1.Messaging.GetMessage
          get: /v1/messages/{message_id}/{sub.subfield}
    

Special notes

When gRPC Transcoding is used to map a gRPC to JSON REST endpoints, the proto to JSON conversion must follow the [proto3 specification](https://developers.google.com/protocol-buffers/docs/proto3#json).

While the single segment variable follows the semantics of [RFC 6570](https://tools.ietf.org/html/rfc6570) Section 3.2.2 Simple String Expansion, the multi segment variable **does not** follow RFC 6570 Section 3.2.3 Reserved Expansion. The reason is that the Reserved Expansion does not expand special characters like `?` and `#`, which would lead to invalid URLs. As the result, gRPC Transcoding uses a custom encoding for multi segment variables.

The path variables **must not** refer to any repeated or mapped field, because client libraries are not capable of handling such variable expansion.

The path variables **must not** capture the leading "/" character. The reason is that the most common use case "{var}" does not capture the leading "/" character. For consistency, all path variables must share the same behavior.

Repeated message fields must not be mapped to URL query parameters, because no client library can support such complicated mapping.

If an API needs to use a JSON array for request or response body, it can map the request or response body to a repeated field. However, some gRPC Transcoding implementations may not support this feature.

### [HttpbodyReflection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.HttpbodyReflection)

Holder for reflection information generated from google/api/httpbody.proto

### [JavaSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.JavaSettings)

Settings for Java client libraries.

### [JwtLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.JwtLocation)

Specifies a location to extract JWT from an API request.

### [LabelDescriptor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.LabelDescriptor)

A description of a label.

### [LabelDescriptor.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.LabelDescriptor.Types)

Container for nested types declared in the LabelDescriptor message type.

### [LabelReflection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.LabelReflection)

Holder for reflection information generated from google/api/label.proto

### [LaunchStageReflection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.LaunchStageReflection)

Holder for reflection information generated from google/api/launch_stage.proto

### [LogDescriptor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.LogDescriptor)

A description of a log type. Example in YAML format:
    
    
    - name: library.googleapis.com/activity_history
      description: The history of borrowing and returning library items.
      display_name: Activity
      labels:
      - key: /customer_id
        description: Identifier of a library customer
    

### [LogReflection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.LogReflection)

Holder for reflection information generated from google/api/log.proto

### [Logging](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Logging)

Logging configuration of the service.

The following example shows how to configure logs to be sent to the producer and consumer projects. In the example, the `activity_history` log is sent to both the producer and consumer projects, whereas the `purchase_history` log is only sent to the producer project.
    
    
    monitored_resources:
    - type: library.googleapis.com/branch
      labels:
      - key: /city
        description: The city where the library branch is located in.
      - key: /name
        description: The name of the branch.
    logs:
    - name: activity_history
      labels:
      - key: /customer_id
    - name: purchase_history
    logging:
      producer_destinations:
      - monitored_resource: library.googleapis.com/branch
        logs:
        - activity_history
        - purchase_history
      consumer_destinations:
      - monitored_resource: library.googleapis.com/branch
        logs:
        - activity_history
    

### [Logging.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Logging.Types)

Container for nested types declared in the Logging message type.

### [Logging.Types.LoggingDestination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Logging.Types.LoggingDestination)

Configuration of a specific logging destination (the producer project or the consumer project).

### [LoggingReflection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.LoggingReflection)

Holder for reflection information generated from google/api/logging.proto

### [MethodPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.MethodPolicy)

Defines policies applying to an RPC method.

### [MethodSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.MethodSettings)

Describes the generator configuration for a method.

### [MethodSettings.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.MethodSettings.Types)

Container for nested types declared in the MethodSettings message type.

### [MethodSettings.Types.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.MethodSettings.Types.LongRunning)

Describes settings to use when generating API methods that use the long-running operation pattern. All default values below are from those used in the client library generators (e.g. [Java](https://github.com/googleapis/gapic-generator-java/blob/04c2faa191a9b5a10b92392fe8482279c4404803/src/main/java/com/google/api/generator/gapic/composer/common/RetrySettingsComposer.java)).

### [Metric](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Metric)

A specific metric, identified by specifying values for all of the labels of a [`MetricDescriptor`][google.api.MetricDescriptor].

### [MetricDescriptor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.MetricDescriptor)

Defines a metric type and its schema. Once a metric descriptor is created, deleting or altering it stops data collection and makes the metric type's existing data unusable.

### [MetricDescriptor.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.MetricDescriptor.Types)

Container for nested types declared in the MetricDescriptor message type.

### [MetricDescriptor.Types.MetricDescriptorMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.MetricDescriptor.Types.MetricDescriptorMetadata)

Additional annotations that can be used to guide the usage of a metric.

### [MetricDescriptor.Types.MetricDescriptorMetadata.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.MetricDescriptor.Types.MetricDescriptorMetadata.Types)

Container for nested types declared in the MetricDescriptorMetadata message type.

### [MetricReflection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.MetricReflection)

Holder for reflection information generated from google/api/metric.proto

### [MetricRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.MetricRule)

Bind API methods to metrics. Binding a method to a metric causes that metric's configured quota behaviors to apply to the method call.

### [MonitoredResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.MonitoredResource)

An object representing a resource that can be used for monitoring, logging, billing, or other purposes. Examples include virtual machine instances, databases, and storage devices such as disks. The `type` field identifies a [MonitoredResourceDescriptor][google.api.MonitoredResourceDescriptor] object that describes the resource's schema. Information in the `labels` field identifies the actual resource and its attributes according to the schema. For example, a particular Compute Engine VM instance could be represented by the following object, because the [MonitoredResourceDescriptor][google.api.MonitoredResourceDescriptor] for `"gce_instance"` has labels `"project_id"`, `"instance_id"` and `"zone"`:
    
    
    { "type": "gce_instance",
      "labels": { "project_id": "my-project",
                  "instance_id": "12345678901234",
                  "zone": "us-central1-a" }}
    

### [MonitoredResourceDescriptor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.MonitoredResourceDescriptor)

An object that describes the schema of a [MonitoredResource][google.api.MonitoredResource] object using a type name and a set of labels. For example, the monitored resource descriptor for Google Compute Engine VM instances has a type of `"gce_instance"` and specifies the use of the labels `"instance_id"` and `"zone"` to identify particular VM instances.

Different APIs can support different monitored resource types. APIs generally provide a `list` method that returns the monitored resource descriptors used by the API.

### [MonitoredResourceMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.MonitoredResourceMetadata)

Auxiliary metadata for a [MonitoredResource][google.api.MonitoredResource] object. [MonitoredResource][google.api.MonitoredResource] objects contain the minimum set of information to uniquely identify a monitored resource instance. There is some other useful auxiliary metadata. Monitoring and Logging use an ingestion pipeline to extract metadata for cloud resources of all types, and store the metadata in this message.

### [MonitoredResourceReflection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.MonitoredResourceReflection)

Holder for reflection information generated from google/api/monitored_resource.proto

### [Monitoring](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Monitoring)

Monitoring configuration of the service.

The example below shows how to configure monitored resources and metrics for monitoring. In the example, a monitored resource and two metrics are defined. The `library.googleapis.com/book/returned_count` metric is sent to both producer and consumer projects, whereas the `library.googleapis.com/book/num_overdue` metric is only sent to the consumer project.
    
    
    monitored_resources:
    - type: library.googleapis.com/Branch
      display_name: "Library Branch"
      description: "A branch of a library."
      launch_stage: GA
      labels:
      - key: resource_container
        description: "The Cloud container (ie. project id) for the Branch."
      - key: location
        description: "The location of the library branch."
      - key: branch_id
        description: "The id of the branch."
    metrics:
    - name: library.googleapis.com/book/returned_count
      display_name: "Books Returned"
      description: "The count of books that have been returned."
      launch_stage: GA
      metric_kind: DELTA
      value_type: INT64
      unit: "1"
      labels:
      - key: customer_id
        description: "The id of the customer."
    - name: library.googleapis.com/book/num_overdue
      display_name: "Books Overdue"
      description: "The current number of overdue books."
      launch_stage: GA
      metric_kind: GAUGE
      value_type: INT64
      unit: "1"
      labels:
      - key: customer_id
        description: "The id of the customer."
    monitoring:
      producer_destinations:
      - monitored_resource: library.googleapis.com/Branch
        metrics:
        - library.googleapis.com/book/returned_count
      consumer_destinations:
      - monitored_resource: library.googleapis.com/Branch
        metrics:
        - library.googleapis.com/book/returned_count
        - library.googleapis.com/book/num_overdue
    

### [Monitoring.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Monitoring.Types)

Container for nested types declared in the Monitoring message type.

### [Monitoring.Types.MonitoringDestination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Monitoring.Types.MonitoringDestination)

Configuration of a specific monitoring destination (the producer project or the consumer project).

### [MonitoringReflection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.MonitoringReflection)

Holder for reflection information generated from google/api/monitoring.proto

### [NodeSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.NodeSettings)

Settings for Node client libraries.

### [OAuthRequirements](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.OAuthRequirements)

OAuth scopes are a way to define data and permissions on data. For example, there are scopes defined for "Read-only access to Google Calendar" and "Access to Cloud Platform". Users can consent to a scope for an application, giving it permission to access that data on their behalf.

OAuth scope specifications should be fairly coarse grained; a user will need to see and understand the text description of what your scope means.

In most cases: use one or at most two OAuth scopes for an entire family of products. If your product has multiple APIs, you should probably be sharing the OAuth scope across all of those APIs.

When you need finer grained OAuth consent screens: talk with your product management about how developers will use them in practice.

Please note that even though each of the canonical scopes is enough for a request to be accepted and passed to the backend, a request can still fail due to the backend requiring additional scopes or permissions.

### [Page](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Page)

Represents a documentation page. A page can contain subpages to represent nested documentation set structure.

### [PhpSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.PhpSettings)

Settings for Php client libraries.

### [PolicyExtensions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.PolicyExtensions)

Holder for extension identifiers generated from the top level of google/api/policy.proto

### [PolicyReflection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.PolicyReflection)

Holder for reflection information generated from google/api/policy.proto

### [ProjectProperties](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ProjectProperties)

A descriptor for defining project properties for a service. One service may have many consumer projects, and the service may want to behave differently depending on some properties on the project. For example, a project may be associated with a school, or a business, or a government agency, a business type property on the project may affect how a service responds to the client. This descriptor defines which properties are allowed to be set on a project.

Example:

project_properties: properties:

  * name: NO_WATERMARK type: BOOL description: Allows usage of the API without watermarks.
  * name: EXTENDED_TILE_CACHE_PERIOD type: INT64



### [Property](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Property)

Defines project properties.

API services can define properties that can be assigned to consumer projects so that backends can perform response customization without having to make additional calls or maintain additional storage. For example, Maps API defines properties that controls map tile cache period, or whether to embed a watermark in a result.

These values can be set via API producer console. Only API providers can define and set these properties.

### [Property.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Property.Types)

Container for nested types declared in the Property message type.

### [Publishing](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Publishing)

This message configures the settings for publishing [Google Cloud Client libraries](https://cloud.google.com/apis/docs/cloud-client-libraries) generated from the service config.

### [PythonSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.PythonSettings)

Settings for Python client libraries.

### [PythonSettings.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.PythonSettings.Types)

Container for nested types declared in the PythonSettings message type.

### [PythonSettings.Types.ExperimentalFeatures](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.PythonSettings.Types.ExperimentalFeatures)

Experimental features to be included during client library generation. These fields will be deprecated once the feature graduates and is enabled by default.

### [Quota](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Quota)

Quota configuration helps to achieve fairness and budgeting in service usage.

The metric based quota configuration works this way:

  * The service configuration defines a set of metrics.
  * For API calls, the quota.metric_rules maps methods to metrics with corresponding costs.
  * The quota.limits defines limits on the metrics, which will be used for quota checks at runtime.



An example quota configuration in yaml format:

quota: limits:
    
    
     - name: apiWriteQpsPerProject
       metric: library.googleapis.com/write_calls
       unit: "1/min/{project}"  # rate limit for consumer projects
       values:
         STANDARD: 10000
    
     (The metric rules bind all methods to the read_calls metric,
      except for the UpdateBook and DeleteBook methods. These two methods
      are mapped to the write_calls metric, with the UpdateBook method
      consuming at twice rate as the DeleteBook method.)
     metric_rules:
     - selector: "*"
       metric_costs:
         library.googleapis.com/read_calls: 1
     - selector: google.example.library.v1.LibraryService.UpdateBook
       metric_costs:
         library.googleapis.com/write_calls: 2
     - selector: google.example.library.v1.LibraryService.DeleteBook
       metric_costs:
         library.googleapis.com/write_calls: 1
    

Corresponding Metric definition:
    
    
     metrics:
     - name: library.googleapis.com/read_calls
       display_name: Read requests
       metric_kind: DELTA
       value_type: INT64
    
     - name: library.googleapis.com/write_calls
       display_name: Write requests
       metric_kind: DELTA
       value_type: INT64
    

### [QuotaLimit](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.QuotaLimit)

`QuotaLimit` defines a specific limit that applies over a specified duration for a limit type. There can be at most one limit for a duration and limit type combination defined within a `QuotaGroup`.

### [QuotaReflection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.QuotaReflection)

Holder for reflection information generated from google/api/quota.proto

### [ResourceDescriptor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ResourceDescriptor)

A simple descriptor of a resource type.

ResourceDescriptor annotates a resource message (either by means of a protobuf annotation or use in the service config), and associates the resource's schema, the resource type, and the pattern of the resource name.

Example:
    
    
    message Topic {
      // Indicates this message defines a resource schema.
      // Declares the resource type in the format of {service}/{kind}.
      // For Kubernetes resources, the format is {api group}/{kind}.
      option (google.api.resource) = {
        type: "pubsub.googleapis.com/Topic"
        pattern: "projects/{project}/topics/{topic}"
      };
    }
    

The ResourceDescriptor Yaml config will look like:
    
    
    resources:
    - type: "pubsub.googleapis.com/Topic"
      pattern: "projects/{project}/topics/{topic}"
    

Sometimes, resources have multiple patterns, typically because they can live under multiple parents.

Example:
    
    
    message LogEntry {
      option (google.api.resource) = {
        type: "logging.googleapis.com/LogEntry"
        pattern: "projects/{project}/logs/{log}"
        pattern: "folders/{folder}/logs/{log}"
        pattern: "organizations/{organization}/logs/{log}"
        pattern: "billingAccounts/{billing_account}/logs/{log}"
      };
    }
    

The ResourceDescriptor Yaml config will look like:
    
    
    resources:
    - type: 'logging.googleapis.com/LogEntry'
      pattern: "projects/{project}/logs/{log}"
      pattern: "folders/{folder}/logs/{log}"
      pattern: "organizations/{organization}/logs/{log}"
      pattern: "billingAccounts/{billing_account}/logs/{log}"
    

### [ResourceDescriptor.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ResourceDescriptor.Types)

Container for nested types declared in the ResourceDescriptor message type.

### [ResourceExtensions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ResourceExtensions)

Holder for extension identifiers generated from the top level of google/api/resource.proto

### [ResourceReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ResourceReference)

Defines a proto annotation that describes a string field that refers to an API resource.

### [ResourceReflection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ResourceReflection)

Holder for reflection information generated from google/api/resource.proto

### [RoutingExtensions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.RoutingExtensions)

Holder for extension identifiers generated from the top level of google/api/routing.proto

### [RoutingParameter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.RoutingParameter)

A projection from an input message to the GRPC or REST header.

### [RoutingReflection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.RoutingReflection)

Holder for reflection information generated from google/api/routing.proto

### [RoutingRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.RoutingRule)

Specifies the routing information that should be sent along with the request in the form of routing header. **NOTE:** All service configuration rules follow the "last one wins" order.

The examples below will apply to an RPC which has the following request type:

Message Definition:
    
    
    message Request {
      // The name of the Table
      // Values can be of the following formats:
      // - `projects/<project>/tables/<table>`
      // - `projects/<project>/instances/<instance>/tables/<table>`
      // - `region/<region>/zones/<zone>/tables/<table>`
      string table_name = 1;
    
      // This value specifies routing for replication.
      // It can be in the following formats:
      // - `profiles/<profile_id>`
      // - a legacy `profile_id` that can be any string
      string app_profile_id = 2;
    }
    

Example message:
    
    
    {
      table_name: projects/proj_foo/instances/instance_bar/table/table_baz,
      app_profile_id: profiles/prof_qux
    }
    

The routing header consists of one or multiple key-value pairs. Every key and value must be percent-encoded, and joined together in the format of `key1=value1&key2=value2`. The examples below skip the percent-encoding for readability.

Example 1

Extracting a field from the request to put into the routing header unchanged, with the key equal to the field name.

annotation:
    
    
    option (google.api.routing) = {
      // Take the `app_profile_id`.
      routing_parameters {
        field: "app_profile_id"
      }
    };
    

result:
    
    
    x-goog-request-params: app_profile_id=profiles/prof_qux
    

Example 2

Extracting a field from the request to put into the routing header unchanged, with the key different from the field name.

annotation:
    
    
    option (google.api.routing) = {
      // Take the `app_profile_id`, but name it `routing_id` in the header.
      routing_parameters {
        field: "app_profile_id"
        path_template: "{routing_id=**}"
      }
    };
    

result:
    
    
    x-goog-request-params: routing_id=profiles/prof_qux
    

Example 3

Extracting a field from the request to put into the routing header, while matching a path template syntax on the field's value.

NB: it is more useful to send nothing than to send garbage for the purpose of dynamic routing, since garbage pollutes cache. Thus the matching.

Sub-example 3a

The field matches the template.

annotation:
    
    
    option (google.api.routing) = {
      // Take the `table_name`, if it's well-formed (with project-based
      // syntax).
      routing_parameters {
        field: "table_name"
        path_template: "{table_name=projects/*/instances/*/**}"
      }
    };
    

result:
    
    
    x-goog-request-params:
    table_name=projects/proj_foo/instances/instance_bar/table/table_baz
    

Sub-example 3b

The field does not match the template.

annotation:
    
    
    option (google.api.routing) = {
      // Take the `table_name`, if it's well-formed (with region-based
      // syntax).
      routing_parameters {
        field: "table_name"
        path_template: "{table_name=regions/*/zones/*/**}"
      }
    };
    

result:
    
    
    <no routing header will be sent>
    

Sub-example 3c

Multiple alternative conflictingly named path templates are specified. The one that matches is used to construct the header.

annotation:
    
    
    option (google.api.routing) = {
      // Take the `table_name`, if it's well-formed, whether
      // using the region- or projects-based syntax.
    
      routing_parameters {
        field: "table_name"
        path_template: "{table_name=regions/*/zones/*/**}"
      }
      routing_parameters {
        field: "table_name"
        path_template: "{table_name=projects/*/instances/*/**}"
      }
    };
    

result:
    
    
    x-goog-request-params:
    table_name=projects/proj_foo/instances/instance_bar/table/table_baz
    

Example 4

Extracting a single routing header key-value pair by matching a template syntax on (a part of) a single request field.

annotation:
    
    
    option (google.api.routing) = {
      // Take just the project id from the `table_name` field.
      routing_parameters {
        field: "table_name"
        path_template: "{routing_id=projects/*}/**"
      }
    };
    

result:
    
    
    x-goog-request-params: routing_id=projects/proj_foo
    

Example 5

Extracting a single routing header key-value pair by matching several conflictingly named path templates on (parts of) a single request field. The last template to match "wins" the conflict.

annotation:
    
    
    option (google.api.routing) = {
      // If the `table_name` does not have instances information,
      // take just the project id for routing.
      // Otherwise take project + instance.
    
      routing_parameters {
        field: "table_name"
        path_template: "{routing_id=projects/*}/**"
      }
      routing_parameters {
        field: "table_name"
        path_template: "{routing_id=projects/*/instances/*}/**"
      }
    };
    

result:
    
    
    x-goog-request-params:
    routing_id=projects/proj_foo/instances/instance_bar
    

Example 6

Extracting multiple routing header key-value pairs by matching several non-conflicting path templates on (parts of) a single request field.

Sub-example 6a

Make the templates strict, so that if the `table_name` does not have an instance information, nothing is sent.

annotation:
    
    
    option (google.api.routing) = {
      // The routing code needs two keys instead of one composite
      // but works only for the tables with the "project-instance" name
      // syntax.
    
      routing_parameters {
        field: "table_name"
        path_template: "{project_id=projects/*}/instances/*/**"
      }
      routing_parameters {
        field: "table_name"
        path_template: "projects/*/{instance_id=instances/*}/**"
      }
    };
    

result:
    
    
    x-goog-request-params:
    project_id=projects/proj_foo&instance_id=instances/instance_bar
    

Sub-example 6b

Make the templates loose, so that if the `table_name` does not have an instance information, just the project id part is sent.

annotation:
    
    
    option (google.api.routing) = {
      // The routing code wants two keys instead of one composite
      // but will work with just the `project_id` for tables without
      // an instance in the `table_name`.
    
      routing_parameters {
        field: "table_name"
        path_template: "{project_id=projects/*}/**"
      }
      routing_parameters {
        field: "table_name"
        path_template: "projects/*/{instance_id=instances/*}/**"
      }
    };
    

result (is the same as 6a for our example message because it has the instance information):
    
    
    x-goog-request-params:
    project_id=projects/proj_foo&instance_id=instances/instance_bar
    

Example 7

Extracting multiple routing header key-value pairs by matching several path templates on multiple request fields.

NB: note that here there is no way to specify sending nothing if one of the fields does not match its template. E.g. if the `table_name` is in the wrong format, the `project_id` will not be sent, but the `routing_id` will be. The backend routing code has to be aware of that and be prepared to not receive a full complement of keys if it expects multiple.

annotation:
    
    
    option (google.api.routing) = {
      // The routing needs both `project_id` and `routing_id`
      // (from the `app_profile_id` field) for routing.
    
      routing_parameters {
        field: "table_name"
        path_template: "{project_id=projects/*}/**"
      }
      routing_parameters {
        field: "app_profile_id"
        path_template: "{routing_id=**}"
      }
    };
    

result:
    
    
    x-goog-request-params:
    project_id=projects/proj_foo&routing_id=profiles/prof_qux
    

Example 8

Extracting a single routing header key-value pair by matching several conflictingly named path templates on several request fields. The last template to match "wins" the conflict.

annotation:
    
    
    option (google.api.routing) = {
      // The `routing_id` can be a project id or a region id depending on
      // the table name format, but only if the `app_profile_id` is not set.
      // If `app_profile_id` is set it should be used instead.
    
      routing_parameters {
        field: "table_name"
        path_template: "{routing_id=projects/*}/**"
      }
      routing_parameters {
         field: "table_name"
         path_template: "{routing_id=regions/*}/**"
      }
      routing_parameters {
        field: "app_profile_id"
        path_template: "{routing_id=**}"
      }
    };
    

result:
    
    
    x-goog-request-params: routing_id=profiles/prof_qux
    

Example 9

Bringing it all together.

annotation:
    
    
    option (google.api.routing) = {
      // For routing both `table_location` and a `routing_id` are needed.
      //
      // table_location can be either an instance id or a region+zone id.
      //
      // For `routing_id`, take the value of `app_profile_id`
      // - If it's in the format `profiles/<profile_id>`, send
      // just the `<profile_id>` part.
      // - If it's any other literal, send it as is.
      // If the `app_profile_id` is empty, and the `table_name` starts with
      // the project_id, send that instead.
    
      routing_parameters {
        field: "table_name"
        path_template: "projects/*/{table_location=instances/*}/tables/*"
      }
      routing_parameters {
        field: "table_name"
        path_template: "{table_location=regions/*/zones/*}/tables/*"
      }
      routing_parameters {
        field: "table_name"
        path_template: "{routing_id=projects/*}/**"
      }
      routing_parameters {
        field: "app_profile_id"
        path_template: "{routing_id=**}"
      }
      routing_parameters {
        field: "app_profile_id"
        path_template: "profiles/{routing_id=*}"
      }
    };
    

result:
    
    
    x-goog-request-params:
    table_location=instances/instance_bar&routing_id=prof_qux
    

### [RubySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.RubySettings)

Settings for Ruby client libraries.

### [SelectiveGapicGeneration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.SelectiveGapicGeneration)

This message is used to configure the generation of a subset of the RPCs in a service for client libraries.

### [Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Service)

`Service` is the root object of Google API service configuration (service config). It describes the basic information about a logical service, such as the service name and the user-facing title, and delegates other aspects to sub-sections. Each sub-section is either a proto message or a repeated proto message that configures a specific aspect, such as auth. For more information, see each proto message definition.

Example:
    
    
    type: google.api.Service
    name: calendar.googleapis.com
    title: Google Calendar API
    apis:
    - name: google.calendar.v3.Calendar
    
    visibility:
      rules:
      - selector: "google.calendar.v3.*"
        restriction: PREVIEW
    backend:
      rules:
      - selector: "google.calendar.v3.*"
        address: calendar.example.com
    
    authentication:
      providers:
      - id: google_calendar_auth
        jwks_uri: https://www.googleapis.com/oauth2/v1/certs
        issuer: https://securetoken.google.com
      rules:
      - selector: "*"
        requirements:
          provider_id: google_calendar_auth
    

### [ServiceReflection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ServiceReflection)

Holder for reflection information generated from google/api/service.proto

### [SourceInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.SourceInfo)

Source information used to create a Service Config

### [SourceInfoReflection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.SourceInfoReflection)

Holder for reflection information generated from google/api/source_info.proto

### [SystemParameter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.SystemParameter)

Define a parameter's name and location. The parameter may be passed as either an HTTP header or a URL query parameter, and if both are passed the behavior is implementation-dependent.

### [SystemParameterReflection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.SystemParameterReflection)

Holder for reflection information generated from google/api/system_parameter.proto

### [SystemParameterRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.SystemParameterRule)

Define a system parameter rule mapping system parameter definitions to methods.

### [SystemParameters](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.SystemParameters)

### System parameter configuration

A system parameter is a special kind of parameter defined by the API system, not by an individual API. It is typically mapped to an HTTP header and/or a URL query parameter. This configuration specifies which methods change the names of the system parameters.

### [TypeReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.TypeReference)

A reference to a message type, for use in [FieldInfo][google.api.FieldInfo].

### [Usage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Usage)

Configuration controlling usage of a service.

### [UsageReflection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.UsageReflection)

Holder for reflection information generated from google/api/usage.proto

### [UsageRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.UsageRule)

Usage configuration rules for the service.

NOTE: Under development.

Use this rule to configure unregistered calls for the service. Unregistered calls are calls that do not contain consumer project identity. (Example: calls that do not contain an API key). By default, API methods do not allow unregistered calls, and each method call must be identified by a consumer project identity. Use this rule to allow/disallow unregistered calls.

Example of an API that wants to allow unregistered calls for entire service.
    
    
    usage:
      rules:
      - selector: "*"
        allow_unregistered_calls: true
    

Example of a method that wants to allow unregistered calls.
    
    
    usage:
      rules:
      - selector: "google.example.library.v1.LibraryService.CreateBook"
        allow_unregistered_calls: true
    

### [Visibility](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Visibility)

`Visibility` restricts service consumer's access to service elements, such as whether an application can call a visibility-restricted method. The restriction is expressed by applying visibility labels on service elements. The visibility labels are elsewhere linked to service consumers.

A service can define multiple visibility labels, but a service consumer should be granted at most one visibility label. Multiple visibility labels for a single service consumer are not supported.

If an element and all its parents have no visibility label, its visibility is unconditionally granted.

Example:
    
    
    visibility:
      rules:
      - selector: google.calendar.Calendar.EnhancedSearch
        restriction: PREVIEW
      - selector: google.calendar.Calendar.Delegate
        restriction: INTERNAL
    

Here, all methods are publicly visible except for the restricted methods EnhancedSearch and Delegate.

### [VisibilityExtensions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.VisibilityExtensions)

Holder for extension identifiers generated from the top level of google/api/visibility.proto

### [VisibilityReflection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.VisibilityReflection)

Holder for reflection information generated from google/api/visibility.proto

### [VisibilityRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.VisibilityRule)

A visibility rule provides visibility configuration for an individual API element.

## Enums 

### [BackendRule.AuthenticationOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.BackendRule.AuthenticationOneofCase)

Enum of possible cases for the "authentication" oneof.

### [BackendRule.Types.PathTranslation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.BackendRule.Types.PathTranslation)

Path Translation specifies how to combine the backend address with the request path in order to produce the appropriate forwarding URL for the request.

Path Translation is applicable only to HTTP-based backends. Backends which do not accept requests over HTTP/HTTPS should leave `path_translation` unspecified.

### [ChangeType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ChangeType)

Classifies set of possible modifications to an object in the service configuration.

### [ClientLibraryDestination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ClientLibraryDestination)

To where should client libraries be published?

### [ClientLibraryOrganization](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ClientLibraryOrganization)

The organization for which the client libraries are being published. Affects the url where generated docs are published, etc.

### [Distribution.Types.BucketOptions.OptionsOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Distribution.Types.BucketOptions.OptionsOneofCase)

Enum of possible cases for the "options" oneof.

### [ErrorReason](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ErrorReason)

Defines the supported values for `google.rpc.ErrorInfo.reason` for the `googleapis.com` error domain. This error domain is reserved for [Service Infrastructure](https://cloud.google.com/service-infrastructure/docs/overview). For each error info of this domain, the metadata key "service" refers to the logical identifier of an API service, such as "pubsub.googleapis.com". The "consumer" refers to the entity that consumes an API Service. It typically is a Google project that owns the client application or the server resource, such as "projects/123". Other metadata keys are specific to each error reason. For more information, see the definition of the specific error reason.

### [FieldBehavior](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.FieldBehavior)

An indicator of the behavior of a given field (for example, that a field is required in requests, or given as output but ignored as input). This **does not** change the behavior in protocol buffers itself; it only denotes the behavior and may affect how API tooling handles the field.

Note: This enum **may** receive new values in the future.

### [FieldInfo.Types.Format](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.FieldInfo.Types.Format)

The standard format of a field value. The supported formats are all backed by either an RFC defined by the IETF or a Google-defined AIP.

### [HttpRule.PatternOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.HttpRule.PatternOneofCase)

Enum of possible cases for the "pattern" oneof.

### [JwtLocation.InOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.JwtLocation.InOneofCase)

Enum of possible cases for the "in" oneof.

### [LabelDescriptor.Types.ValueType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.LabelDescriptor.Types.ValueType)

Value types that can be used as label values.

### [LaunchStage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.LaunchStage)

The launch stage as defined by [Google Cloud Platform Launch Stages](https://cloud.google.com/terms/launch-stages).

### [MetricDescriptor.Types.MetricDescriptorMetadata.Types.TimeSeriesResourceHierarchyLevel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.MetricDescriptor.Types.MetricDescriptorMetadata.Types.TimeSeriesResourceHierarchyLevel)

The resource hierarchy level of the timeseries data of a metric.

### [MetricDescriptor.Types.MetricKind](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.MetricDescriptor.Types.MetricKind)

The kind of measurement. It describes how the data is reported. For information on setting the start time and end time based on the MetricKind, see [TimeInterval][google.monitoring.v3.TimeInterval].

### [MetricDescriptor.Types.ValueType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.MetricDescriptor.Types.ValueType)

The value type of a metric.

### [Property.Types.PropertyType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Property.Types.PropertyType)

Supported data type of the property values

### [ResourceDescriptor.Types.History](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ResourceDescriptor.Types.History)

A description of the historical or future-looking state of the resource pattern.

### [ResourceDescriptor.Types.Style](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ResourceDescriptor.Types.Style)

A flag representing a specific style that a resource claims to conform to.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
