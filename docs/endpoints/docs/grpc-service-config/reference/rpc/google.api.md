---
url: https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api
title: Package google.api \u00a0|\u00a0 Cloud Endpoints with gRPC \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:39:53.818910+00:00
---

# Package google.api  |  Cloud Endpoints with gRPC  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ gRPC ](https://docs.cloud.google.com/endpoints/docs/grpc/about-grpc)
  * [ Reference ](https://docs.cloud.google.com/endpoints/docs/grpc/specify-proxy-startup-options)



Send feedback 

#  Package google.api Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[JwtLocation](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.JwtLocation)` (message)
  * `[AuthRequirement](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.AuthRequirement)` (message)
  * `[Authentication](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.Authentication)` (message)
  * `[AuthenticationRule](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.AuthenticationRule)` (message)
  * `[Backend](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.Backend)` (message)
  * `[BackendRule](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.BackendRule)` (message)
  * `[BackendRule.PathTranslation](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.BackendRule.PathTranslation)` (enum)
  * `[CustomHttpPattern](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.CustomHttpPattern)` (message)
  * `[Documentation](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.Documentation)` (message)
  * `[DocumentationRule](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.DocumentationRule)` (message)
  * `[Endpoint](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.Endpoint)` (message)
  * `[Http](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.Http)` (message)
  * `[HttpRule](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.HttpRule)` (message)
  * `[LabelDescriptor](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.LabelDescriptor)` (message)
  * `[LabelDescriptor.ValueType](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.LabelDescriptor.ValueType)` (enum)
  * `[LaunchStage](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.LaunchStage)` (enum)
  * `[MetricDescriptor](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.MetricDescriptor)` (message)
  * `[MetricDescriptor.MetricDescriptorMetadata](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.MetricDescriptor.MetricDescriptorMetadata)` (message)
  * `[MetricDescriptor.MetricKind](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.MetricDescriptor.MetricKind)` (enum)
  * `[MetricDescriptor.ValueType](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.MetricDescriptor.ValueType)` (enum)
  * `[MetricRule](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.MetricRule)` (message)
  * `[Page](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.Page)` (message)
  * `[Quota](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.Quota)` (message)
  * `[QuotaLimit](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.QuotaLimit)` (message)
  * `[Service](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.Service)` (message)
  * `[SystemParameter](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.SystemParameter)` (message)
  * `[SystemParameterRule](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.SystemParameterRule)` (message)
  * `[SystemParameters](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.SystemParameters)` (message)
  * `[Usage](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.Usage)` (message)
  * `[UsageRule](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.UsageRule)` (message)



## JwtLocation

Defines the locations to extract the [JSON Web Token (JWT)](https://tools.ietf.org/html/draft-ietf-oauth-json-web-token-32).

Fields  
---  
`value_prefix` |  `string` The value prefix. The value format is "value_prefix{token}". Only applies to `in` header type. Must be empty for `in` query type. If not empty, the header value has to match (case sensitive) this prefix. If not matched, JWT will not be extracted. If matched, JWT will be extracted after the prefix is removed. For example, for "Authorization: Bearer {JWT}", value_prefix="Bearer " with a space at the end.  
Union field `in`. `in` can be only one of the following:  
`header` |  `string` Specifies HTTP header name to extract JWT token.  
`query` |  `bool` Specifies URL query parameter name to extract JWT token.  
  
## AuthProvider

Configuration for an authentication provider, including support for [JSON Web Token (JWT)](https://tools.ietf.org/html/draft-ietf-oauth-json-web-token-32).

Fields  
---  
`id` |  `string` The unique identifier of the auth provider. It will be referred to by `AuthRequirement.provider_id`.Example: "bookstore_auth".  
`issuer` |  `string` Identifies the principal that issued the JWT. See <https://tools.ietf.org/html/draft-ietf-oauth-json-web-token-32#section-4.1.1> Usually a URL or an email address. Example: `https://securetoken.google.com` Example: `1234567-compute@developer.gserviceaccount.com`  
`jwks_uri` |  `string` URL of the provider's public key set to validate signature of the JWT. See [OpenID Discovery](https://openid.net/specs/openid-connect-discovery-1_0.html#ProviderMetadata). Optional if the key set document: - can be retrieved from [OpenID Discovery](<https://openid.net/specs/openid-connect-discovery-1_0.html> of the issuer. - can be inferred from the email domain of the issuer (e.g. a Google service account).Example: <https://www.googleapis.com/oauth2/v1/certs>  
`audiences` |  `string` The list of JWT [audiences](https://tools.ietf.org/html/draft-ietf-oauth-json-web-token-32#section-4.1.3). that are allowed to access. A JWT containing any of these audiences will be accepted. When this setting is absent, only JWTs with audience "https://`[Service_name](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.Service.FIELDS.string.google.api.Service.name)`/`[API_name](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Api)`" will be accepted. For example, if no audiences are in the setting, LibraryService API will only accept JWTs with the following audience "https://library-example.googleapis.com/google.example.library.v1.LibraryService".Example:
    
    
    audiences: bookstore_android.apps.googleusercontent.com,
               bookstore_web.apps.googleusercontent.com
      
  
`authorization_url` |  `string` Redirect URL if JWT token is required but not present or is expired. Implement authorizationUrl of securityDefinitions in OpenAPI spec.  
`jwt_locations` |  `JwtLocation` Defines the locations to extract the JWT. JWT locations can be either from HTTP headers or URL query parameters. The rule is that the first match wins. The checking order is: checking all headers first, then URL query parameters. If not specified, default to use following 3 locations:

  * 1) `Authorization: Bearer` header
  * 2) `x-goog-iap-jwt-assertion` header
  * 3) `access_token` query parameter

Default locations can be specified as followings:
    
    
    jwt_locations:
    - header: Authorization
      value_prefix: "Bearer "
    - header: x-goog-iap-jwt-assertion
    - query: access_token
                        
  
## AuthRequirement

User-defined authentication requirements, including support for [JSON Web Token (JWT)](https://tools.ietf.org/html/draft-ietf-oauth-json-web-token-32).

Fields  
---  
`provider_id` |  `string` `[id](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.AuthProvider.FIELDS.string.google.api.AuthProvider.id)` from authentication provider.Example:
    
    
    provider_id: bookstore_auth
      
  
`audiences` |  `string` NOTE: This will be deprecated soon, once AuthProvider.audiences is implemented and accepted in all the runtime components.The list of JWT [audiences](https://tools.ietf.org/html/draft-ietf-oauth-json-web-token-32#section-4.1.3). that are allowed to access. A JWT containing any of these audiences will be accepted. When this setting is absent, only JWTs with audience "https://`[Service_name](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.Service.FIELDS.string.google.api.Service.name)`/`[API_name](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Api)`" will be accepted. For example, if no audiences are in the setting, LibraryService API will only accept JWTs with the following audience "https://library-example.googleapis.com/google.example.library.v1.LibraryService".Example:
    
    
    audiences: bookstore_android.apps.googleusercontent.com,
               bookstore_web.apps.googleusercontent.com
      
  
## Authentication

`Authentication` defines the authentication configuration for an API.

Example for an API targeted for external use:
    
    
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
    

Fields  
---  
`rules[]` |  ``[AuthenticationRule](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.AuthenticationRule)`` A list of authentication rules that apply to individual API methods.**NOTE:** All service configuration rules follow "last one wins" order.  
`providers[]` |  ``[AuthProvider](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.AuthProvider)`` Defines a set of authentication providers that a service supports.  
  
## AuthenticationRule

Authentication rules for the service.

By default, if a method has any authentication requirements, every request must include a valid credential matching one of the requirements. It's an error to include more than one kind of credential in a single request.

If a method doesn't have any auth requirements, request credentials will be ignored.

Fields  
---  
`selector` |  `string` Selects the methods to which this rule applies.Refer to `[selector](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.DocumentationRule.FIELDS.string.google.api.DocumentationRule.selector)` for syntax details.  
`requirements[]` |  ``[AuthRequirement](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.AuthRequirement)`` Requirements for additional authentication providers.  
  
## Backend

`Backend` defines the backend configuration for a service.

Fields  
---  
`rules[]` |  ``[BackendRule](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.BackendRule)`` A list of API backend rules that apply to individual API methods.**NOTE:** All service configuration rules follow "last one wins" order.  
  
## BackendRule

A backend rule provides configuration for an individual API element.

Fields  
---  
`selector` |  `string` Selects the methods to which this rule applies.Refer to `[selector](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.DocumentationRule.FIELDS.string.google.api.DocumentationRule.selector)` for syntax details.  
`address` |  `string` The address of the API backend.The scheme is used to determine the backend protocol and security. The following schemes are accepted:
    
    
    SCHEME        PROTOCOL        SECURITY
    http://       HTTP            None
    https://      HTTP            TLS
    grpc://       gRPC            None
    grpcs://      gRPC            TLS

It is recommended to explicitly include a scheme. Leaving out the scheme might cause constrasting behaviors across platforms.If the port is unspecified, the default is: 80 for schemes without TLS, and 443 for schemes with TLSFor HTTP backends, use `[protocol](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.BackendRule.FIELDS.string.google.api.BackendRule.protocol)` to specify the protocol version.  
`deadline` |  `double` The number of seconds to wait for a response from a request. The default varies based on the request protocol and deployment environment.  
`min_deadline` |  `double` Minimum deadline in seconds needed for this method. Calls having deadline value lower than this will be rejected.  
`operation_deadline` |  `double` The number of seconds to wait for the completion of a long running operation. The default is no deadline.  
`path_translation` |  ``[PathTranslation](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.BackendRule.PathTranslation)``  
`protocol` |  `string` The protocol used for sending a request to the backend. The supported values are "http/1.1" and "h2".The default value is inferred from the scheme in the `[address](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.BackendRule.FIELDS.string.google.api.BackendRule.address)` field:
    
    
    SCHEME        PROTOCOL
    http://       http/1.1
    https://      http/1.1
    grpc://       h2
    grpcs://      h2

For secure HTTP backends (https://) that support HTTP/2, set this field to "h2" for improved performance.Setting this field to non-default values is only supported for secure HTTP backends. This field will be ignored for all other backends.See <https://www.iana.org/assignments/tls-extensiontype-values/tls-extensiontype-values.xhtml#alpn-protocol-ids> for more details on the supported values.  
Union field `authentication`. Authentication settings used by the backend.These are typically used to provide service management functionality to a backend served on a publicly-routable URL. The `authentication` details should match the authentication behavior used by the backend.For example, specifying `jwt_audience` implies that the backend expects authentication via a JWT.When authentication is unspecified, the resulting behavior is the same as `disable_auth` set to `true`.Refer to <https://developers.google.com/identity/protocols/OpenIDConnect> for JWT ID token. `authentication` can be only one of the following:  
`jwt_audience` |  `string` The JWT audience is used when generating a JWT ID token for the backend. This ID token will be added in the HTTP "authorization" header, and sent to the backend.  
`disable_auth` |  `bool` When disable_auth is true, a JWT ID token won't be generated and the original "Authorization" HTTP header will be preserved. If the header is used to carry the original token and is expected by the backend, this field must be set to true to preserve the header.  
  
## PathTranslation

Path Translation specifies how to combine the backend address with the request path in order to produce the appropriate forwarding URL for the request.

Path Translation is applicable only to HTTP-based backends. Backends which do not accept requests over HTTP/HTTPS should leave `path_translation` unspecified.

Enums  
---  
`PATH_TRANSLATION_UNSPECIFIED` |   
`CONSTANT_ADDRESS` | Use the backend address as-is, with no modification to the path. If the URL pattern contains variables, the variable names and values will be appended to the query string. If a query string parameter and a URL pattern variable have the same name, this may result in duplicate keys in the query string.Given the following operation config:
    
    
    Method path:        /api/company/{cid}/user/{uid}
    Backend address:    https://example.cloudfunctions.net/getUser
    

Requests to the following request paths will call the backend at the translated path:
    
    
    Request path: /api/company/widgetworks/user/johndoe
    Translated:
    https://example.cloudfunctions.net/getUser?cid=widgetworks&uid=johndoe
    
    Request path: /api/company/widgetworks/user/johndoe?timezone=EST
    Translated:
    https://example.cloudfunctions.net/getUser?timezone=EST&cid=widgetworks&uid=johndoe
      
  
`APPEND_PATH_TO_ADDRESS` | The request path will be appended to the backend address.Given the following operation config:
    
    
    Method path:        /api/company/{cid}/user/{uid}
    Backend address:    https://example.appspot.com
    

Requests to the following request paths will call the backend at the translated path:
    
    
    Request path: /api/company/widgetworks/user/johndoe
    Translated:
    https://example.appspot.com/api/company/widgetworks/user/johndoe
    
    Request path: /api/company/widgetworks/user/johndoe?timezone=EST
    Translated:
    https://example.appspot.com/api/company/widgetworks/user/johndoe?timezone=EST
      
  
## CustomHttpPattern

A custom pattern is used for defining custom HTTP verb.

Fields  
---  
`kind` |  `string` The name of this custom HTTP verb.  
`path` |  `string` The path matched by this custom verb.  
  
## Documentation

`Documentation` provides the information for describing a service.

Example:
    
    
    documentation:
      summary: >
        The Google Calendar API gives access
        to most calendar features.
      pages:
      - name: Overview
        content: (== include google/foo/overview.md ==)
      - name: Tutorial
        content: (== include google/foo/tutorial.md ==)
        subpages;
        - name: Java
          content: (== include google/foo/tutorial_java.md ==)
      rules:
      - selector: google.calendar.Calendar.Get
        description: >
          ...
      - selector: google.calendar.Calendar.Put
        description: >
          ...
    

Documentation is provided in markdown syntax. In addition to standard markdown features, definition lists, tables and fenced code blocks are supported. Section headers can be provided and are interpreted relative to the section nesting of the context where a documentation fragment is embedded.

Documentation from the IDL is merged with documentation defined via the config at normalization time, where documentation provided by config rules overrides IDL provided.

A number of constructs specific to the API platform are supported in documentation text.

In order to reference a proto element, the following notation can be used:
    
    
    [fully.qualified.proto.name][]

To override the display text used for the link, this can be used:
    
    
    [display text][fully.qualified.proto.name]

Text can be excluded from doc using the following notation:
    
    
    (-- internal comment --)

A few directives are available in documentation. Note that directives must appear on a single line to be properly identified. The `include` directive includes a markdown file from an external source:
    
    
    (== include path/to/file ==)

The `resource_for` directive marks a message to be the resource of a collection in REST view. If it is not specified, tools attempt to infer the resource from the operations in a collection:
    
    
    (== resource_for v1.shelves.books ==)

The directive `suppress_warning` does not directly affect documentation and is documented together with service config validation.

Fields  
---  
`summary` |  `string` A short summary of what the service does. Can only be provided by plain text.  
`pages[]` |  ``[Page](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.Page)`` The top level pages for the documentation set.  
`rules[]` |  ``[DocumentationRule](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.DocumentationRule)`` A list of documentation rules that apply to individual API elements.**NOTE:** All service configuration rules follow "last one wins" order.  
`documentation_root_url` |  `string` The URL to the root of documentation.  
`service_root_url` |  `string` Specifies the service root url if the default one (the service name from the yaml file) is not suitable. This can be seen in any fully specified service urls as well as sections that show a base that other urls are relative to.  
`overview` |  `string` Declares a single overview page. For example:
    
    
    documentation:
      summary: ...
      overview: (== include overview.md ==)
    

This is a shortcut for the following declaration (using pages style):
    
    
    documentation:
      summary: ...
      pages:
      - name: Overview
        content: (== include overview.md ==)
    

Note: you cannot specify both `overview` field and `pages` field.  
  
## DocumentationRule

A documentation rule provides information about individual API elements.

Fields  
---  
`selector` |  `string` The selector is a comma-separated list of patterns. Each pattern is a qualified name of the element which may end in "*", indicating a wildcard. Wildcards are only allowed at the end and for a whole component of the qualified name, i.e. "foo.*" is ok, but not "foo.b*" or "foo.*.bar". A wildcard will match one or more components. To specify a default for all applicable elements, the whole pattern "*" is used.  
`description` |  `string` Description of the selected API(s).  
`deprecation_description` |  `string` Deprecation description of the selected element(s). It can be provided if an element is marked as `deprecated`.  
  
## Endpoint

`Endpoint` describes a network endpoint that serves a set of APIs. A service may expose any number of endpoints, and all endpoints share the same service configuration, such as quota configuration and monitoring configuration.

Example service configuration:
    
    
    name: library-example.googleapis.com
    endpoints:
      # Below entry makes 'google.example.library.v1.Library'
      # API be served from endpoint address library-example.googleapis.com.
      # It also allows HTTP OPTIONS calls to be passed to the backend, for
      # it to decide whether the subsequent cross-origin request is
      # allowed to proceed.
    - name: library-example.googleapis.com
      allow_cors: true
    

Fields  
---  
`name` |  `string` The canonical name of this endpoint.  
`allow_cors` |  `bool` Allowing [CORS](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing), aka cross-domain traffic, would allow the backends served from this endpoint to receive and respond to HTTP OPTIONS requests. The response will be used by the browser to determine whether the subsequent cross-origin request is allowed to proceed.  
  
## Http

Defines the HTTP configuration for an API service. It contains a list of `[HttpRule](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.HttpRule)`, each specifying the mapping of an RPC method to one or more HTTP REST API methods.

Fields  
---  
`rules[]` |  ``[HttpRule](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.HttpRule)`` A list of HTTP configuration rules that apply to individual API methods.**NOTE:** All service configuration rules follow "last one wins" order.  
`fully_decode_reserved_expansion` |  `bool` When set to true, URL path parameters will be fully URI-decoded except in cases of single segment matches in reserved expansion, where "%2F" will be left encoded.The default behavior is to not decode RFC 6570 reserved characters in multi segment matches.  
  
## HttpRule

#### gRPC Transcoding

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

HTTP  | gRPC  
---|---  
`GET /v1/messages/123456` | `GetMessage(name: "messages/123456")`  
  
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

HTTP  | gRPC  
---|---  
`GET /v1/messages/123456?revision=2&sub.subfield=foo` | `GetMessage(message_id: "123456" revision: 2 sub: SubMessage(subfield: "foo"))`  
  
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

HTTP  | gRPC  
---|---  
`PATCH /v1/messages/123456 { "text": "Hi!" }` | `UpdateMessage(message_id: "123456" message { text: "Hi!" })`  
  
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

HTTP  | gRPC  
---|---  
`PATCH /v1/messages/123456 { "text": "Hi!" }` | `UpdateMessage(message_id: "123456" text: "Hi!")`  
  
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

HTTP  | gRPC  
---|---  
`GET /v1/messages/123456` | `GetMessage(message_id: "123456")`  
`GET /v1/users/me/messages/123456` | `GetMessage(user_id: "me" message_id: "123456")`  
  
##### Rules for HTTP mapping

  1. Leaf request fields (recursive expansion nested messages in the request message) are classified into three categories:


  * Fields referred by the path template. They are passed via the URL path.
  * Fields referred by the `[HttpRule.body](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.HttpRule.FIELDS.string.google.api.HttpRule.body)`. They are passed via the HTTP request body.
  * All other fields are passed via the URL query parameters, and the parameter name is the field path in the request message. A repeated field can be represented as multiple query parameters under the same name.


  1. If `[HttpRule.body](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.HttpRule.FIELDS.string.google.api.HttpRule.body)` is "*", there is no URL query parameter, all fields are passed via URL path and HTTP request body.
  2. If `[HttpRule.body](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.HttpRule.FIELDS.string.google.api.HttpRule.body)` is omitted, there is no HTTP request body, all fields are passed via URL path and URL query parameters.



###### Path template syntax
    
    
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

##### Using gRPC API Service Configuration

gRPC API Service Configuration (service config) is a configuration language for configuring a gRPC service to become a user-facing product. The service config is simply the YAML representation of the `google.api.Service` proto message.

As an alternative to annotating your proto file, you can configure gRPC transcoding in your service config YAML files. You do this by specifying a `HttpRule` that maps the gRPC method to a REST endpoint, achieving the same effect as the proto annotation. This can be particularly useful if you have a proto that is reused in multiple services. Note that any transcoding specified in the service config will override any matching transcoding configuration in the proto.

Example:
    
    
    http:
      rules:
        # Selects a gRPC method and applies HttpRule to it.
        - selector: example.v1.Messaging.GetMessage
          get: /v1/messages/{message_id}/{sub.subfield}
    

##### Special notes

When gRPC Transcoding is used to map a gRPC to JSON REST endpoints, the proto to JSON conversion must follow the [proto3 specification](https://developers.google.com/protocol-buffers/docs/proto3#json).

While the single segment variable follows the semantics of [RFC 6570](https://tools.ietf.org/html/rfc6570) Section 3.2.2 Simple String Expansion, the multi segment variable **does not** follow RFC 6570 Section 3.2.3 Reserved Expansion. The reason is that the Reserved Expansion does not expand special characters like `?` and `#`, which would lead to invalid URLs. As the result, gRPC Transcoding uses a custom encoding for multi segment variables.

The path variables **must not** refer to any repeated or mapped field, because client libraries are not capable of handling such variable expansion.

The path variables **must not** capture the leading "/" character. The reason is that the most common use case "{var}" does not capture the leading "/" character. For consistency, all path variables must share the same behavior.

Repeated message fields must not be mapped to URL query parameters, because no client library can support such complicated mapping.

If an API needs to use a JSON array for request or response body, it can map the request or response body to a repeated field. However, some gRPC Transcoding implementations may not support this feature.

Fields  
---  
`selector` |  `string` Selects a method to which this rule applies.Refer to `[selector](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.DocumentationRule.FIELDS.string.google.api.DocumentationRule.selector)` for syntax details.  
`body` |  `string` The name of the request field whose value is mapped to the HTTP request body, or `*` for mapping all request fields not captured by the path pattern to the HTTP body, or omitted for not having any HTTP request body.NOTE: the referred field must be present at the top-level of the request message type.  
`response_body` |  `string` Optional. The name of the response field whose value is mapped to the HTTP response body. When omitted, the entire response message will be used as the HTTP response body.NOTE: The referred field must be present at the top-level of the response message type.  
`additional_bindings[]` |  ``[HttpRule](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.HttpRule)`` Additional HTTP bindings for the selector. Nested bindings must not contain an `additional_bindings` field themselves (that is, the nesting may only be one level deep).  
`allow_half_duplex` |  `bool` When this flag is set to true, HTTP requests will be allowed to invoke a half-duplex streaming method.  
Union field `pattern`. Determines the URL pattern is matched by this rules. This pattern can be used with any of the {get|put|post|delete|patch} methods. A custom method can be defined using the 'custom' field. `pattern` can be only one of the following:  
`get` |  `string` Maps to HTTP GET. Used for listing and getting information about resources.  
`put` |  `string` Maps to HTTP PUT. Used for replacing a resource.  
`post` |  `string` Maps to HTTP POST. Used for creating a resource or performing an action.  
`delete` |  `string` Maps to HTTP DELETE. Used for deleting a resource.  
`patch` |  `string` Maps to HTTP PATCH. Used for updating a resource.  
`custom` |  ``[CustomHttpPattern](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.CustomHttpPattern)`` The custom pattern is used for specifying an HTTP method that is not included in the `pattern` field, such as HEAD, or "*" to leave the HTTP method unspecified for this rule. The wild-card rule is useful for services that provide content to Web (HTML) clients.  
  
## LabelDescriptor

A description of a label.

Fields  
---  
`key` |  `string` The label key.  
`value_type` |  ``[ValueType](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.LabelDescriptor.ValueType)`` The type of data that can be assigned to the label.  
`description` |  `string` A human-readable description for the label.  
  
## ValueType

Value types that can be used as label values.

Enums  
---  
`STRING` | A variable-length string. This is the default.  
`BOOL` | Boolean; true or false.  
`INT64` | A 64-bit signed integer.  
  
## LaunchStage

The launch stage as defined by [Google Cloud Platform Launch Stages](http://cloud.google.com/terms/launch-stages).

Enums  
---  
`LAUNCH_STAGE_UNSPECIFIED` | Do not use this default value.  
`EARLY_ACCESS` | Early Access features are limited to a closed group of testers. To use these features, you must sign up in advance and sign a Trusted Tester agreement (which includes confidentiality provisions). These features may be unstable, changed in backward-incompatible ways, and are not guaranteed to be released.  
`ALPHA` | Alpha is a limited availability test for releases before they are cleared for widespread use. By Alpha, all significant design issues are resolved and we are in the process of verifying functionality. Alpha customers need to apply for access, agree to applicable terms, and have their projects whitelisted. Alpha releases don't have to be feature complete, no SLAs are provided, and there are no technical support obligations, but they will be far enough along that customers can actually use them in test environments or for limited-use tests -- just like they would in normal production cases.  
`BETA` | Beta is the point at which we are ready to open a release for any customer to use. There are no SLA or technical support obligations in a Beta release. Products will be complete from a feature perspective, but may have some open outstanding issues. Beta releases are suitable for limited production use cases.  
`GA` | GA features are open to all developers and are considered stable and fully qualified for production use.  
`DEPRECATED` | Deprecated features are scheduled to be shut down and removed. For more information, see the "Deprecation Policy" section of our [Terms of Service](https://cloud.google.com/terms/) and the [Google Cloud Platform Subject to the Deprecation Policy](https://cloud.google.com/terms/deprecation) documentation.  
  
## MetricDescriptor

Defines a metric type and its schema. Once a metric descriptor is created, deleting or altering it stops data collection and makes the metric type's existing data unusable.

Fields  
---  
`name` |  `string` The resource name of the metric descriptor.  
`type` |  `string` The metric type, including its DNS name prefix. The type is not URL-encoded. All user-defined metric types have the DNS name `custom.googleapis.com` or `external.googleapis.com`. Metric types should use a natural hierarchical grouping. For example:
    
    
    "custom.googleapis.com/invoice/paid/amount"
    "external.googleapis.com/prometheus/up"
    "appengine.googleapis.com/http/server/response_latencies"
      
  
`labels[]` |  ``[LabelDescriptor](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.LabelDescriptor)`` The set of labels that can be used to describe a specific instance of this metric type. For example, the `appengine.googleapis.com/http/server/response_latencies` metric type has a label for the HTTP response code, `response_code`, so you can look at latencies for successful responses or just for responses that failed.  
`metric_kind` |  ``[MetricKind](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.MetricDescriptor.MetricKind)`` Whether the metric records instantaneous values, changes to a value, etc. Some combinations of `metric_kind` and `value_type` might not be supported.  
`value_type` |  ``[ValueType](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.MetricDescriptor.ValueType)`` Whether the measurement is an integer, a floating-point number, etc. Some combinations of `metric_kind` and `value_type` might not be supported.  
`unit` |  `string` The units in which the metric value is reported. It is only applicable if the `value_type` is `INT64`, `DOUBLE`, or `DISTRIBUTION`. The `unit` defines the representation of the stored metric values.Different systems may scale the values to be more easily displayed (so a value of `0.02KBy` _might_ be displayed as `20By`, and a value of `3523KBy` _might_ be displayed as `3.5MBy`). However, if the `unit` is `KBy`, then the value of the metric is always in thousands of bytes, no matter how it may be displayed..If you want a custom metric to record the exact number of CPU-seconds used by a job, you can create an `INT64 CUMULATIVE` metric whose `unit` is `s{CPU}` (or equivalently `1s{CPU}` or just `s`). If the job uses 12,005 CPU-seconds, then the value is written as `12005`.Alternatively, if you want a custom metric to record data in a more granular way, you can create a `DOUBLE CUMULATIVE` metric whose `unit` is `ks{CPU}`, and then write the value `12.005` (which is `12005/1000`), or use `Kis{CPU}` and write `11.723` (which is `12005/1024`).The supported units are a subset of [The Unified Code for Units of Measure](http://unitsofmeasure.org/ucum.html) standard:**Basic units (UNIT)**

  * `bit` bit
  * `By` byte
  * `s` second
  * `min` minute
  * `h` hour
  * `d` day

**Prefixes (PREFIX)**

  * `k` kilo (10^3)
  * `M` mega (10^6)
  * `G` giga (10^9)
  * `T` tera (10^12)
  * `P` peta (10^15)
  * `E` exa (10^18)
  * `Z` zetta (10^21)
  * `Y` yotta (10^24)
  * `m` milli (10^-3)
  * `u` micro (10^-6)
  * `n` nano (10^-9)
  * `p` pico (10^-12)
  * `f` femto (10^-15)
  * `a` atto (10^-18)
  * `z` zepto (10^-21)
  * `y` yocto (10^-24)
  * `Ki` kibi (2^10)
  * `Mi` mebi (2^20)
  * `Gi` gibi (2^30)
  * `Ti` tebi (2^40)
  * `Pi` pebi (2^50)

**Grammar** The grammar also includes these connectors:

  * `/` division or ratio (as an infix operator). For examples, `kBy/{email}` or `MiBy/10ms` (although you should almost never have `/s` in a metric `unit`; rates should always be computed at query time from the underlying cumulative or delta value).
  * `.` multiplication or composition (as an infix operator). For examples, `GBy.d` or `k{watt}.h`.

The grammar for a unit is as follows:
    
    
    Expression = Component { "." Component } { "/" Component } ;
    
    Component = ( [ PREFIX ] UNIT | "%" ) [ Annotation ]
              | Annotation
              | "1"
              ;
    
    Annotation = "{" NAME "}" ;
    

Notes:

  * `Annotation` is just a comment if it follows a `UNIT`. If the annotation is used alone, then the unit is equivalent to `1`. For examples, `{request}/s == 1/s`, `By{transmitted}/s == By/s`.
  * `NAME` is a sequence of non-blank printable ASCII characters not containing `{` or `}`.
  * `1` represents a unitary [dimensionless unit](https://en.wikipedia.org/wiki/Dimensionless_quantity) of 1, such as in `1/s`. It is typically used when none of the basic units are appropriate. For example, "new users per day" can be represented as `1/d` or `{new-users}/d` (and a metric value `5` would mean "5 new users). Alternatively, "thousands of page views per day" would be represented as `1000/d` or `k1/d` or `k{page_views}/d` (and a metric value of `5.3` would mean "5300 page views per day").
  * `%` represents dimensionless value of 1/100, and annotates values giving a percentage (so the metric values are typically in the range of 0..100, and a metric value `3` means "3 percent").
  * `10^2.%` indicates a metric contains a ratio, typically in the range 0..1, that will be multiplied by 100 and displayed as a percentage (so a metric value `0.03` means "3 percent").

  
`description` |  `string` A detailed description of the metric, which can be used in documentation.  
`display_name` |  `string` A concise name for the metric, which can be displayed in user interfaces. Use sentence case without an ending period, for example "Request count". This field is optional but it is recommended to be set for any metrics associated with user-visible concepts, such as Quota.  
`metadata` |  ``[MetricDescriptorMetadata](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.MetricDescriptor.MetricDescriptorMetadata)`` Optional. Metadata which can be used to guide usage of the metric.  
`launch_stage` |  ``[LaunchStage](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.LaunchStage)`` Optional. The launch stage of the metric definition.  
`monitored_resource_types[]` |  `string` Read-only. If present, then a [time series][google.monitoring.v3.TimeSeries], which is identified partially by a metric type and a `MonitoredResourceDescriptor`, that is associated with this metric type can only be associated with one of the monitored resource types listed here.  
  
## MetricDescriptorMetadata

Additional annotations that can be used to guide the usage of a metric.

Fields  
---  
`launch_stage  
**(deprecated)**` |  ``[LaunchStage](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.LaunchStage)`` This item is deprecated!Deprecated. Must use the `[MetricDescriptor.launch_stage](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.MetricDescriptor.FIELDS.google.api.LaunchStage.google.api.MetricDescriptor.launch_stage)` instead.  
`sample_period` |  ``[Duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration)`` The sampling period of metric data points. For metrics which are written periodically, consecutive data points are stored at this time interval, excluding data loss due to errors. Metrics with a higher granularity have a smaller sampling period.  
`ingest_delay` |  ``[Duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration)`` The delay of data points caused by ingestion. Data points older than this age are guaranteed to be ingested and available to be read, excluding data loss due to errors.  
  
## MetricKind

The kind of measurement. It describes how the data is reported.

Enums  
---  
`METRIC_KIND_UNSPECIFIED` | Do not use this default value.  
`GAUGE` | An instantaneous measurement of a value.  
`DELTA` | The change in a value during a time interval.  
`CUMULATIVE` | A value accumulated over a time interval. Cumulative measurements in a time series should have the same start time and increasing end times, until an event resets the cumulative value to zero and sets a new start time for the following points.  
  
## ValueType

The value type of a metric.

Enums  
---  
`VALUE_TYPE_UNSPECIFIED` | Do not use this default value.  
`BOOL` | The value is a boolean. This value type can be used only if the metric kind is `GAUGE`.  
`INT64` | The value is a signed 64-bit integer.  
`DOUBLE` | The value is a double precision floating point number.  
`STRING` | The value is a text string. This value type can be used only if the metric kind is `GAUGE`.  
`DISTRIBUTION` | The value is a [`Distribution`][google.api.Distribution].  
`MONEY` | The value is money.  
  
## MetricRule

Bind API methods to metrics. Binding a method to a metric causes that metric's configured quota behaviors to apply to the method call.

Fields  
---  
`selector` |  `string` Selects the methods to which this rule applies.Refer to `[selector](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.DocumentationRule.FIELDS.string.google.api.DocumentationRule.selector)` for syntax details.  
`metric_costs` |  `map<string, int64>` Metrics to update when the selected methods are called, and the associated cost applied to each metric.The key of the map is the metric name, and the values are the amount increased for the metric against which the quota limits are defined. The value must not be negative.  
  
## Page

Represents a documentation page. A page can contain subpages to represent nested documentation set structure.

Fields  
---  
`name` |  `string` The name of the page. It will be used as an identity of the page to generate URI of the page, text of the link to this page in navigation, etc. The full page name (start from the root page name to this page concatenated with `.`) can be used as reference to the page in your documentation. For example:
    
    
    pages:
    - name: Tutorial
      content: (== include tutorial.md ==)
      subpages:
      - name: Java
        content: (== include tutorial_java.md ==)
    

You can reference `Java` page using Markdown reference link syntax: `[Java][Tutorial.Java]`.  
`content` |  `string` The Markdown content of the page. You can use  `(== include {path} ==)` to include content from a Markdown file.  
`subpages[]` |  ``[Page](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.Page)`` Subpages of this page. The order of subpages specified here will be honored in the generated docset.  
  
## Quota

Quota configuration helps to achieve fairness and budgeting in service usage.

The metric based quota configuration works this way: - The service configuration defines a set of metrics. - For API calls, the quota.metric_rules maps methods to metrics with corresponding costs. - The quota.limits defines limits on the metrics, which will be used for quota checks at runtime.

An example quota configuration in yaml format:

quota: limits:
    
    
     - name: apiWriteQpsPerProject
       metric: library.googleapis.com/write_calls
       unit: "1/min/{project}"  # rate limit for consumer projects
       values:
         STANDARD: 10000
    
    
     # The metric rules bind all methods to the read_calls metric,
     # except for the UpdateBook and DeleteBook methods. These two methods
     # are mapped to the write_calls metric, with the UpdateBook method
     # consuming at twice rate as the DeleteBook method.
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
    

Fields  
---  
`limits[]` |  ``[QuotaLimit](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.QuotaLimit)`` List of `QuotaLimit` definitions for the service.  
`metric_rules[]` |  ``[MetricRule](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.MetricRule)`` List of `MetricRule` definitions, each one mapping a selected method to one or more metrics.  
  
## QuotaLimit

`QuotaLimit` defines a specific limit that applies over a specified duration for a limit type. There can be at most one limit for a duration and limit type combination defined within a `QuotaGroup`.

Fields  
---  
`name` |  `string` Name of the quota limit.The name must be provided, and it must be unique within the service. The name can only include alphanumeric characters as well as '-'.The maximum length of the limit name is 64 characters.  
`description` |  `string` Optional. User-visible, extended description for this quota limit. Should be used only when more context is needed to understand this limit than provided by the limit's display name (see: `display_name`).  
`metric` |  `string` The name of the metric this quota limit applies to. The quota limits with the same metric will be checked together during runtime. The metric must be defined within the service config.  
`unit` |  `string` Specify the unit of the quota limit. It uses the same syntax as [Metric.unit][]. The supported unit kinds are determined by the quota backend system.Here are some examples: * "1/min/{project}" for quota per minute per project.Note: the order of unit components is insignificant. The "1" at the beginning is required to follow the metric unit syntax.  
`values` |  `map<string, int64>` Tiered limit values. You must specify this as a key:value pair, with an integer value that is the maximum number of requests allowed for the specified unit. Currently only STANDARD is supported.  
  
## Service

`Service` is the root object of Google service configuration schema. It describes basic information about a service, such as the name and the title, and delegates other aspects to sub-sections. Each sub-section is either a proto message or a repeated proto message that configures a specific aspect, such as auth. See each proto message definition for details.

Example:
    
    
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
    

Fields  
---  
`config_version` |  ``[UInt32Value](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.UInt32Value)`` The semantic version of the service configuration. The config version affects the interpretation of the service configuration. For example, certain features are enabled by default for certain config versions. The latest config version is `3`.  
`name` |  `string` The service name, which is a DNS-like logical identifier for the service, such as `calendar.googleapis.com`. The service name typically goes through DNS verification to make sure the owner of the service also owns the DNS name.  
`id` |  `string` A unique ID for a specific instance of this message, typically assigned by the client for tracking purpose. Must be no longer than 63 characters and only lower case letters, digits, '.', '_' and '-' are allowed. If empty, the server may choose to generate one instead.  
`title` |  `string` The product title for this service.  
`apis[]` |  ``[Api](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Api)`` A list of API interfaces exported by this service. Only the `name` field of the `[google.protobuf.Api](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Api)` needs to be provided by the configuration author, as the remaining fields will be derived from the IDL during the normalization process. It is an error to specify an API interface here which cannot be resolved against the associated IDL files.  
`types[]` |  ``[Type](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Type)`` A list of all proto message types included in this API service. Types referenced directly or indirectly by the `apis` are automatically included. Messages which are not referenced but shall be included, such as types used by the `google.protobuf.Any` type, should be listed here by name. Example:
    
    
    types:
    - name: google.protobuf.Int32
      
  
`enums[]` |  ``[Enum](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Enum)`` A list of all enum types included in this API service. Enums referenced directly or indirectly by the `apis` are automatically included. Enums which are not referenced but shall be included should be listed here by name. Example:
    
    
    enums:
    - name: google.someapi.v1.SomeEnum
      
  
`backend` |  ``[Backend](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.Backend)`` API backend configuration.  
`http` |  ``[Http](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.Http)`` HTTP configuration.  
`quota` |  ``[Quota](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.Quota)`` Quota configuration.  
`authentication` |  ``[Authentication](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.Authentication)`` Auth configuration.  
`usage` |  ``[Usage](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.Usage)`` Configuration controlling usage of this service.  
`endpoints[]` |  ``[Endpoint](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.Endpoint)`` Configuration for network endpoints. If this is empty, then an endpoint with the same name as the service is automatically generated to service all defined APIs.  
`metrics[]` |  ``[MetricDescriptor](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.MetricDescriptor)`` Defines the metrics used by this service.  
`system_parameters` |  ``[SystemParameters](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.SystemParameters)`` System parameter configuration.  
  
## SystemParameter

Define a parameter's name and location. The parameter may be passed as either an HTTP header or a URL query parameter, and if both are passed the behavior is implementation-dependent.

Fields  
---  
`name` |  `string` Define the name of the parameter, such as "api_key" . It is case sensitive.  
`http_header` |  `string` Define the HTTP header name to use for the parameter. It is case insensitive.  
`url_query_parameter` |  `string` Define the URL query parameter name to use for the parameter. It is case sensitive.  
  
## SystemParameterRule

Define a system parameter rule mapping system parameter definitions to methods.

Fields  
---  
`selector` |  `string` Selects the methods to which this rule applies. Use '*' to indicate all methods in all APIs.Refer to `[selector](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.DocumentationRule.FIELDS.string.google.api.DocumentationRule.selector)` for syntax details.  
`parameters[]` |  ``[SystemParameter](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.SystemParameter)`` Define parameters. Multiple names may be defined for a parameter. For a given method call, only one of them should be used. If multiple names are used the behavior is implementation-dependent. If none of the specified names are present the behavior is parameter-dependent.  
  
## SystemParameters

###### System parameter configuration

A system parameter is a special kind of parameter defined by the API system, not by an individual API. It is typically mapped to an HTTP header and/or a URL query parameter. This configuration specifies which methods change the names of the system parameters.

Fields  
---  
`rules[]` |  ``[SystemParameterRule](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.SystemParameterRule)`` Define system parameters.The parameters defined here will override the default parameters implemented by the system. If this field is missing from the service config, default system parameters will be used. Default system parameters and names is implementation-dependent.Example: define api key for all methods
    
    
    system_parameters
      rules:
        - selector: "*"
          parameters:
            - name: api_key
              url_query_parameter: api_key
    

Example: define 2 api key names for a specific method.
    
    
    system_parameters
      rules:
        - selector: "/ListShelves"
          parameters:
            - name: api_key
              http_header: Api-Key1
            - name: api_key
              http_header: Api-Key2
    

**NOTE:** All service configuration rules follow "last one wins" order.  
  
## Usage

Configuration controlling usage of a service.

Fields  
---  
`rules[]` |  ``[UsageRule](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.UsageRule)`` A list of usage rules that apply to individual API methods.**NOTE:** All service configuration rules follow "last one wins" order.  
  
## UsageRule

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
    

Fields  
---  
`selector` |  `string` Selects the methods to which this rule applies. Use '*' to indicate all methods in all APIs.Refer to `[selector](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.DocumentationRule.FIELDS.string.google.api.DocumentationRule.selector)` for syntax details.  
`allow_unregistered_calls` |  `bool` If true, the selected method allows unregistered calls, e.g. calls that don't identify any user or application.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
