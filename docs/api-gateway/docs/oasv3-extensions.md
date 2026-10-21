---
url: https://docs.cloud.google.com/api-gateway/docs/oasv3-extensions/
title: OpenAPI 3.x Extensions in API Gateway \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:59:56.154426+00:00
---

# OpenAPI 3.x Extensions in API Gateway  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/api-gateway/docs/oasv3-extensions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ API Gateway ](https://docs.cloud.google.com/api-gateway/docs)
  * [ Guides ](https://docs.cloud.google.com/api-gateway/docs/secure-traffic-gcloud)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# OpenAPI 3.x Extensions in API Gateway

API Gateway accepts a set of Google-specific extensions to the OpenAPI specification that configure the behaviors of the gateway. These extensions allow you to specify API management settings, authentication methods, quota limits, and backend integrations directly within your OpenAPI document. Understanding these extensions helps you tailor your service behavior and integrate with API Gateway features.

This page describes Google-specific extensions to the [OpenAPI specification 3.x](https://docs.cloud.google.com/api-gateway/docs/openapi-overview).

Although the examples given are in YAML format, JSON is also supported.

## `x-google-api-management`

**Required.**

The `x-google-api-management` extension defines top-level API management settings for your service. Place this extension at the root of your OpenAPI document.

The following table describes the fields for `x-google-api-management`:

Field | Type | Required | Default | Description  
---|---|---|---|---  
`metrics` | `map[string]Metric` | No | Empty | Define metrics to enforce quota limits.  
`quota` | `map[string]Quota` | No | Empty | Specify quota limits for your service.  
`backends` | `map[string]Backend` | Yes | Empty | Configure backend services.  
`apiName` | `string` | No | Empty | Associate a name with the operations defined in the OpenAPI document.  
`ai` | `AI` | No | Empty | Configure artificial intelligence features, including model routing.  
`mcp` | `MCP` or `bool` | No | Empty | Enable or configure Model Context Protocol (MCP) features.  
**Caution:** Ensure that your quota metrics and limits remain consistent across all active API configs before you create a new one. API Gateway applies `metrics` and `quota` to the entire API rather than to an individual API config, so any metric or limit that a new API config declares replaces the definition for the whole API. If you rename or remove a metric, the quota-enforced methods of any gateway that still serves an earlier API config return an HTTP `500` error. For more information, see [Quotas apply to the whole API](https://docs.cloud.google.com/api-gateway/docs/quotas-overview#quotas_apply_to_the_whole_api).

### `Metric` object

The `Metric` object defines a metric used for quota enforcement.

The following table describes the fields for `Metric`:

Field | Type | Required | Default | Description  
---|---|---|---|---  
`displayName` | `string` | No | Empty | Display name of the metric.  
  
### `Quota` object

The `Quota` object defines quota limits.

The following table describes the fields for `Quota`:

Field | Type | Required | Default | Description  
---|---|---|---|---  
`limits` | `map[string]QuotaLimit` | No | Empty | Specify quota limits.  
  
### `QuotaLimit` object

The `QuotaLimit` object defines a specific quota limit.

The following table describes the fields for `QuotaLimit`:

Field | Type | Required | Description  
---|---|---|---  
`metric` | `string` | Yes | Reference a metric declared in this OpenAPI document.  
`values` | `int64` | Yes | Set the maximum value the metric can reach before client requests are denied.  
  
### `Backends` object

**Required.**

The `Backends` object configures a backend service. You must set either `jwtAudience` or `disableAuth`.

The following table describes the fields for `Backends`:

Field | Type | Required | Default | Description  
---|---|---|---|---  
`address` | `string` | Yes | Empty | Specify the URL of the backend.  
`jwtAudience` | `string` | No | Empty | By default, API Gateway will create the instance ID token with a JWT audience that matches the address field. Manually specifying `jwt_audience` is only required when the target backend uses JWT-based authentication and the expected audience is different than the value specified in the address field. For remote backends deployed on App Engine or with IAP, you must override the JWT audience. App Engine and IAP use their OAuth client ID as the expected audience.  
`disableAuth` | `bool` | No | `False` | Prevent the data plane proxy from obtaining an instance ID token and attaching it to the request.  
`pathTranslation` | `string` | No | `APPEND_PATH_TO_ADDRESS` or `CONSTANT_ADDRESS` | Set the path translation strategy when proxying requests to the target backend. When `x-google-backend` is set at the top level and no `path_translation` is specified, the default `pathTranslation` is `APPEND_PATH_TO_ADDRESS`. When `x-google-backend` is set on at the operation level and no `path_translation` is specified, the default is `CONSTANT_ADDRESS`.  
`deadline` | `double` | No | `15.0` | Specify the number of seconds to wait for a full response from a request. Responses that exceed this deadline time out. On an SSE or chunked-transfer endpoint, the deadline still bounds the entire stream's duration; on a gRPC or WebSocket endpoint it bounds the gap between messages instead. See [Set the stream deadline](https://docs.cloud.google.com/api-gateway/docs/streaming-configure#configure-deadline) for the timeouts that apply to each kind of request. Omit the field or set it to `0` to use the default. A negative value is rejected. The deadline is configurable up to 3600 seconds. A non-streaming gateway enforces a lower maximum of 600 seconds, rejecting a higher deadline at gateway create or update rather than at API config create.  
`protocol` | `string` | No | `http/1.1` | Set the protocol for sending a request to the backend. Supported values include `http/1.1` and `h2`. Protocol requirements depend on the streaming type:  
\- **gRPC** : You must set the protocol to `h2`.  
\- **WebSockets** : You must use `http/1.1`.  
\- **Server-Sent Events (SSE) and incremental response delivery** : You can use either `http/1.1` or `h2`. We recommend `h2` for improved performance.  
  
### `AI` object

The `AI` object configures artificial intelligence capabilities for your service, such as model routing.

The following table describes the fields for `AI`:

Field | Type | Required | Default | Description  
---|---|---|---|---  
`models` | `Models` | No | Empty | Configure AI model integrations.  
  
### `Models` object

The `Models` object defines model-specific configurations.

The following table describes the fields for `Models`:

Field | Type | Required | Default | Description  
---|---|---|---|---  
`routing` | `Routing` | No | Empty | Configure model routing settings.  
  
### `Routing` object

The `Routing` object defines model routing rules and routers.

The following table describes the fields for `Routing`:

Field | Type | Required | Default | Description  
---|---|---|---|---  
`routers` | `map[string]Router` | No | Empty | Define named model routers.  
  
### `Router` object

The `Router` object defines a named model router.

The following table describes the fields for `Router`:

Field | Type | Required | Default | Description  
---|---|---|---|---  
`defaultModel` | `DefaultModel` | Yes | Empty | The required fallback model destination used when an incoming request does not match any explicit rule.  
`rules` | `[Rule]` | No | Empty | List of explicit model routing rules.  
  
### `DefaultModel` object

The `DefaultModel` object specifies the fallback destination.

The following table describes the fields for `DefaultModel`:

Field | Type | Required | Default | Description  
---|---|---|---|---  
`backend` | `string` | Yes | Empty | Reference a backend declared in `x-google-api-management.backends`.  
`targetModel` | `string` | Yes | Empty | Specify the target model identifier in the form `<provider>/<model-id>`. For OpenAI-compatible routes, this value is forwarded as the outgoing `model` attribute in the request body when fallback occurs.  
  
### `Rule` object

The `Rule` object defines an explicit model routing rule.

The following table describes the fields for `Rule`:

Field | Type | Required | Default | Description  
---|---|---|---|---  
`model` | `string` | Yes | Empty | The incoming string matched against the `model` attribute in the client's JSON payload. For OpenAI-compatible routes, this string is forwarded as the outgoing `model` attribute in the request body and must be a valid `<provider>/<model-id>` string.  
`backend` | `string` | Yes | Empty | Reference a backend declared in `x-google-api-management.backends`.  
`targetModel` | `string` | Yes | Empty | Specify the target model identifier in the form `<provider>/<model-id>`. This value selects provider translation and is echoed back in the response `model` field.  
  
### `MCP` object

The `MCP` object configures Model Context Protocol (MCP) features for your service. You can set `mcp` to a boolean value or an object. Set to `true` to enable MCP globally for all eligible operations with default settings.

**Note:** You cannot use MCP and Model Routing together in the same API configuration. If `x-google-api-management.mcp` is set, you cannot define `x-google-model-router` on any operation.

The following table describes the fields for `MCP` object:

Field | Type | Required | Default | Description  
---|---|---|---|---  
`tools-list` | `ToolsList` | No | Empty | Configure settings for the `tools/list` MCP method.  
  
### `ToolsList` object

The `ToolsList` object configures settings for the `tools/list` MCP method.

The following table describes the fields for `ToolsList`:

Field | Type | Required | Default | Description  
---|---|---|---|---  
`security` | `map` | No | Empty | Enables authentication on `tools/list`. As a security best practice, it is strongly recommended to configure this option. Must name exactly one JWT or API key security scheme defined under `components.securitySchemes`.  
  
## `x-google-auth`

**Optional.**

The `x-google-auth` extension defines authentication settings within a Security Scheme Object.

The following table describes the fields for `x-google-auth`:

Field | Type | Required | Default | Description  
---|---|---|---|---  
`issuer` | `string` | No | Empty | Specify the issuer of a credential. Values can be a hostname or email address.  
`jwksUri` | `string` | No | Empty | Provide the URI of the provider's public key set to validate the signature of the JSON Web Token. API Gateway supports two asymmetric public key formats defined by this OpenAPI extension: 

  1. [JWK set format](https://tools.ietf.org/html/rfc7517#section-5). For example: `jwksUri: "https://YOUR_ACCOUNT_NAME.YOUR_AUTH_PROVIDER_URL/.well-known/jwks.json"`
  2. [X509](https://tools.ietf.org/html/rfc5280). For example: `jwksUri: "https://www.googleapis.com/service_accounts/v1/metadata/x509/securetoken@system.gserviceaccount.com"`

If you are using a symmetric key format, set the `jwksUri` to the URI of a file that contains the base64url-encoded key string.  
`audiences` | `[string]` | No | Empty | List audiences that the JWT `aud` field must match during JWT authentication.  
`jwtLocations` | `[JwtLocations]` | No | Empty | Customize locations for the JWT token. By default, a JWT passes in the `Authorization` header (prefixed by "Bearer "), `X-Goog-Iap-Jwt-Assertion` header, or the `access_token` query parameter.  
  
### `JwtLocations` object

The `JwtLocations` object provides customized locations for the JWT token.

The following table describes the fields for `JwtLocations`:

Field | Type | Required | Default | Description  
---|---|---|---|---  
`header` | `query` | `string` | Yes | N/A | Specify the name for the header containing the JWT, or the name for the query parameter containing the JWT.  
`valuePrefix` | `string` | No | Empty | For header only. When set, its value must match the prefix of the header value containing the JWT.  
  
## `x-google-quota`

**Optional.**

The `x-google-quota` extension is used on individual operations to specify which metrics defined in `x-google-api-management.metrics` are affected by requests to that operation.

`x-google-quota` is an object containing key-value pairs, where each key is a metric name and the value is the integer cost for each request to the operation. For example:
    
    
    x-google-api-management:
      metrics:
        read-requests:
          displayName: "Greeter requests"
        write-requests:
          displayName: "Greeter requests by name"
      quota:
        limits:
          read-requests-limit:
            metric: read-requests
            values: 1
    # Set at the top-level so this applies to all operations (unless overridden)
    x-google-quota:
        read-requests: 1
    paths:
      /v1/projects/projectId/pets:
        get:
          # Set at the path level, so it overrides the top level quota
          x-google-quota:
              write-requests: 1
    

## `x-google-backend`

**Required.**

The `x-google-backend` extension references a backend defined in `x-google-api-management.backends`. When used, its value must be a string that matches the name of a backend defined in `x-google-api-management.backends`. You must set this extension for API Gateway. You can define this extension at the top-level of your OpenAPI document or for an individual operation to override the top-level backend.

For example:
    
    
    x-google-api-management:
      backends:
        my-backend:
          address: myapp.run.app
    x-google-backend: my-backend
    

## `x-google-model-router`

**Optional.**

The `x-google-model-router` extension references a model router defined in `x-google-api-management.ai.models.routing.routers`. When used, its value must be a string that matches the name of a router defined in `x-google-api-management.ai.models.routing.routers`.

This extension is supported only in OpenAPI 3.x specifications; it cannot be used with OpenAPI 2.0 (Swagger) specifications. You can define this extension only at the individual operation level for operations using the `POST` HTTP method. You cannot specify both `x-google-model-router` and `x-google-backend` on the same operation, nor can you mix model routing and non-model routing operations across different paths within the same API specification. Furthermore, you cannot use Model Routing in conjunction with Model Context Protocol (MCP); enabling `x-google-api-management.mcp` makes this extension unavailable.

For example:
    
    
    x-google-api-management:
      backends:
        gemini-backend:
          address: https://aiplatform.googleapis.com/v1/...
      ai:
        models:
          routing:
            routers:
              my-router:
                defaultModel:
                  backend: gemini-backend
                  targetModel: google/gemini-3.5-flash-lite
    paths:
      /v1/chat:
        post:
          x-google-model-router: my-router
    

## `x-google-mcp-tool`

**Optional.**

The `x-google-mcp-tool` extension is used on individual operations to expose them as MCP tools and optionally override the generated tool name and description.

This extension is supported only in OpenAPI 3.x specifications; it cannot be used with OpenAPI 2.0 (Swagger) specifications. You can define this extension only at the individual operation level.

Accepts either a boolean or an object.

  * **Boolean form** : Set to `true` to opt this operation in. Set to `false` to opt it out, overriding a global enable.
  * **Object form** : Opt in and override the generated tool settings.



The following table describes the fields for `x-google-mcp-tool` when used as an object:

Field | Type | Required | Default | Description  
---|---|---|---|---  
`name` | `string` | No | The operation's `operationId` | The MCP tool name. Must match `[A-Za-z0-9_.-]{1,128}` and be unique across the specification.  
`description` | `string` | No | The operation's description, falling back to summary | The MCP tool description. This is the primary signal an LLM uses for tool selection.  
  
For example:
    
    
    paths:
      /v1/shelves/{shelf}:
        delete:
          operationId: deleteShelf
          summary: Delete a shelf.
          x-google-backend: bookstore-backend
          x-google-mcp-tool:
            name: delete_shelf
            description: "Permanently delete a shelf and every book on it."
    

## `x-google-endpoint`

**Optional.**

The `x-google-endpoint` extension is used to configure the properties of a server defined in the `servers` array of an OpenAPI 3.x document. Only one server entry in your OpenAPI document can use the `x-google-endpoint` extension.

The extension also defines other backend features, including:

  * CORS: You can enable Cross-Origin Resource Sharing (CORS) by setting the `allowCors` property to `true`.

  * Base path: The base path set on the server with `x-google-endpoint` is used for your API. For example, the following configuration sets `v1` as the base path:



    
    
    servers:
      - url: https://API_NAME.apigateway.PROJECT_ID.cloud.goog/v1
        x-google-endpoint: {}
    

The following table describes the fields for `x-google-endpoint`:

Field | Type | Required | Default | Description  
---|---|---|---|---  
`allowCors` | `bool` | No | `false` | Allow CORS requests.  
  
## `x-google-parameter`

**Optional.**

The `x-google-parameter` extension is defined on a `parameter` item. This can be used when the path uses [path templating](https://docs.cloud.google.com/api-gateway/docs/path-templating) to specify that double wildcard matching behavior should be used.

The following table describes the fields for `x-google-parameter`:

Field | Type | Required | Description  
---|---|---|---  
`pattern` | `string` | Yes | This must be set to `**`.  
  
## Understand OpenAPI extension limitations

These OpenAPI extensions have specific limitations. To learn more, see [OpenAPI 3.x feature limitations](https://docs.cloud.google.com/api-gateway/docs/openapi-v3-limitations).

## What's next

  * Explore the [OpenAPI Specification](https://swagger.io/specification/).
  * [Modify a gateway to use OpenAPI 3.0](https://docs.cloud.google.com/api-gateway/docs/migrate-oasv3).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
