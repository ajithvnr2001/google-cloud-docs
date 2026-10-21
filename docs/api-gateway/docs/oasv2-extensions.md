---
url: https://docs.cloud.google.com/api-gateway/docs/oasv2-extensions/
title: OpenAPI 2.0 extensions in API Gateway \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:59:57.436070+00:00
---

# OpenAPI 2.0 extensions in API Gateway  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/api-gateway/docs/oasv2-extensions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ API Gateway ](https://docs.cloud.google.com/api-gateway/docs)
  * [ Guides ](https://docs.cloud.google.com/api-gateway/docs/secure-traffic-gcloud)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# OpenAPI 2.0 extensions in API Gateway

API Gateway accepts a set of Google-specific extensions to the OpenAPI specification that configure the behaviors of the gateway. This page describes custom Google- specific extensions to the [OpenAPI specification 2.0](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md) used to configure API Gateway behaviors such as backend routing, authentication, and API management features.

Although the examples given are in YAML format, JSON is also supported.

## Naming convention

Google OpenAPI extensions have names that begin with the `x-google-` prefix.

## `x-google-allow`

`x-google-allow: [configured | all]`

This extension is used at the top level of an OpenAPI specification to indicate what URL paths should be allowed through API Gateway.

Possible values are `configured` and `all`.

The default value is `configured`, which means that only the API methods that you have listed in your OpenAPI specification are served through API Gateway.

When `all` is used, unconfigured calls —with or without an API key or user authentication—pass through API Gateway to your API.

**Note:** When the [`basePath`](https://swagger.io/docs/specification/2-0/api-host-and-base-path/) property is configured in the service configuration as well, this header applies only to URL paths that are prefixed by the `basePath` property value. URLs that aren't part of the `basePath` aren't passed through regardless of the `x-google-allow` property.

API Gateway processes calls to your API in a case-sensitive manner. For example, API Gateway considers `/widgets` and `/Widgets` as different API methods.

When `all` is used, you need to take extra care in two areas:

  * Any API key or authentication rules.
  * The backend path routing in your service.



As a best practice, we recommend that you configure your API to use case-sensitive path routing. By using case-sensitive routing, your API returns an HTTP status code of `404` when the method requested in the URL doesn't match the API method name listed in your OpenAPI specification. Note that web application frameworks such as Node.js Express have a setting to enable or disable case-sensitive routing. The default behavior depends on the framework that you are using. We recommend that you review the settings in your framework to make sure that case-sensitive routing is enabled. This recommendation agrees with the [OpenAPI Specification v2.0](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md#specification) that says: "All field names in the specification are case sensitive."

### Example

Assume that:

  * `x-google-allow` is set to `all`.
  * The API method `widgets` is listed in your OpenAPI specification but not `Widgets`.
  * You have configured your OpenAPI specification to require an API key.



Because `widgets` is listed in your OpenAPI specification, API Gateway blocks the following request because it doesn't have an API key:

`https://my-project-id.appspot.com/widgets`

Because `Widgets` isn't listed in your OpenAPI specification, API Gateway passes the following request through to your service without an API key:

`https://my-project-id.appspot.com/Widgets/`

If your API uses case-sensitive routing (and you haven't routed calls to "Widgets" to any code), your API backend returns a `404`. If, however, you are using case-insensitive routing, your API backend routes this call to "widgets."

Different languages and frameworks have different methods for controlling case sensitivity and routing. Consult the documentation for your framework for details.

## `x-google-backend`

The `x-google-backend` extension specifies how to route requests to remote backends. The extension can be specified at the top level, the operation level, or both levels of an OpenAPI specification.

The `x-google-backend` extension can also configure other settings for remote backends, such as authentication and timeouts. All these configurations can be applied on a per-operation basis.

The `x-google-backend` extension contains the following fields:

### `address`

`address: URL`

Required. The URL of the target backend. The address's scheme must be either `http` or `https`.

When routing to remote backends (Serverless), the address should be set and the scheme portion should be `https`.

### `jwt_audience | disable_auth`

Only one of these two properties should be set.

If an operation uses `x-google-backend` but does not specify either `jwt_audience` or `disable_auth`, API Gateway will automatically default the `jwt_audience` to match the `address`. If `address` is not set, API Gateway will automatically set `disable_auth` to `true`.

#### `jwt_audience`

`jwt_audience: string`

Optional. The JWT audience specified when API Gateway [obtains an instance ID token](https://docs.cloud.google.com/compute/docs/instances/verifying-instance-identity#request_signature), which is then used when making the target backend request.

When configuring API Gateway for Serverless, the remote backend should be secured to only allow traffic from API Gateway. API Gateway will attach an instance ID token to the `Authorization` header when proxying requests. The instance ID token represents the runtime service account that was used to deploy API Gateway. The remote backend can then verify the request is from API Gateway based on this attached token.

For example, a remote backend deployed on Cloud Run can use Identity and Access Management (IAM) to:

  1. Restrict unauthenticated invocations by revoking `roles/run.invoker` from the special `allUsers` principal.
  2. Allow only API Gateway to invoke the backend by granting the `roles/run.invoker` role to the API Gateway runtime service account.



By default, API Gateway will create the instance ID token with a JWT audience that matches the `address` field. Manually specifying `jwt_audience` is only required when the target backend uses JWT-based authentication and the expected audience is different than the value specified in the `address` field. For remote backends deployed on App Engine or with Identity-Aware Proxy (IAP), you must override the JWT audience. App Engine and IAP use their OAuth client ID as the expected audience.

When this feature is enabled, API Gateway will mutate headers in requests. If a request has the `Authorization` header already set, API Gateway will:

  1. Copy the original value to a new header `X-Forwarded-Authorization`.
  2. Override the `Authorization` header with the instance ID token.



Therefore, if an API client sets the `Authorization` header, a backend running behind API Gateway should use the `X-Forwarded-Authorization` header to retrieve the entire JWT. The backend **must** verify the JWT in this header, as API Gateway won't perform verification when [authentication methods](https://docs.cloud.google.com/endpoints/docs/openapi/authentication-method) are not configured.

For configuration examples, see [Create an API config](https://docs.cloud.google.com/api-gateway/docs/get-started-app-engine).

**Note:** If API Gateway is configured with authentication, prefer to use the `X-Endpoint-API-UserInfo` header to retrieve the verified JWT payload. See [Receive authenticated results in your API](https://docs.cloud.google.com/endpoints/docs/openapi/authenticating-users-custom#receiving_authenticated_results_in_your_api) for more details.

#### `disable_auth`

`disable_auth: bool`

Optional. This property determines whether API Gateway should prevent obtaining an instance ID token and prevent attaching it to the request.

When configuring your target backend, you may not want to use IAP or IAM to authenticate requests from API Gateway if either of these conditions apply:

  1. The backend should allow unauthenticated invocations.
  2. The backend requires the original `Authorization` header from the API client and cannot use `X-Forwarded-Authorization` (described in the `jwt_audience` section).



In this case, set this field to `true`.

### `path_translation`

`path_translation: [ APPEND_PATH_TO_ADDRESS | CONSTANT_ADDRESS ]`

Optional. Sets the path translation strategy used by API Gateway when proxying requests to the target backend.

For more details on path translation, see the Understand path translation section.

When `x-google-backend` is used at the top level of the OpenAPI specification, `path_translation` defaults to `APPEND_PATH_TO_ADDRESS`, and when `x-google-backend` is used at the operation level of the OpenAPI specification, `path_translation` defaults to `CONSTANT_ADDRESS`. If the `address` field is missing, `path_translation` will remain unspecified and it won't occur.

### `deadline`

`deadline: double`

Optional. The number of seconds to wait for a full response from a request. Responses that take longer than the configured deadline will time out. On an SSE or chunked-transfer endpoint, the deadline still bounds the entire stream's duration; on a gRPC or WebSocket endpoint it bounds the gap between messages instead. See [Set the stream deadline](https://docs.cloud.google.com/api-gateway/docs/streaming-configure#configure-deadline) for the timeouts that apply to each kind of request. The default deadline is `15.0` seconds.

Omit the field or set it to `0` to use the default. A negative value also uses the default, but is deprecated: creating an API config with one returns a warning in the operation metadata, and it will be rejected in a future release.

The deadline is configurable up to `3600` seconds. A non-streaming gateway enforces a lower maximum of `600` seconds, rejecting a higher deadline at gateway create or update rather than at API config create.

**Warning:** Long deadlines can result in the proxy being overloaded with too many tcp connections if the backend response is slow. Short deadlines can cause some more expensive requests to fail consistently. Balance these constraints to pick a good deadline.

### `protocol`

`protocol: [ http/1.1 | h2 ]`

Optional. The protocol used for sending a request to the backend. The supported values are `http/1.1` and `h2`.

The default value is `http/1.1` for HTTP and HTTPS backends.

For secure HTTP backends (https://) that support HTTP/2, set this field to `h2` for improved performance. This is the recommended option for Google Cloud Serverless backends.

Protocol requirements depend on the streaming type:

  * **gRPC** : You must set the protocol to `h2`.
  * **WebSockets** : You must use `http/1.1`.
  * **Server-Sent Events (SSE) and incremental response delivery** : You can use either `http/1.1` or `h2`. We recommend `h2` for improved performance.



### Understand path translation

As API Gateway handles requests, it will take the original request path and translate it prior to making a request to the target backend. Exactly how this translation occurs depends on which path translation strategy you are using. There are two path translation strategies:

  * `APPEND_PATH_TO_ADDRESS`: The target backend request path is computed by appending the original request path to the `address` URL of the `x-google-backend` extension.
  * `CONSTANT_ADDRESS`: The target request path is constant, as defined by the `address` URL of the `x-google-backend` extension. If the corresponding OpenAPI path contains parameters, the parameter name and its value become query parameters.



Examples:

  * `APPEND_PATH_TO_ADDRESS`
    * `address: https://my-project-id.appspot.com/BASE_PATH`
    * With OpenAPI path parameters 
      * OpenAPI path: `/hello/{name}`
      * Request path: `/hello/world`
      * Target request URL: `https://my-project-id.appspot.com/BASE_PATH/hello/world`
    * Without OpenAPI path parameters 
      * OpenAPI path: `/hello`
      * Request path: `/hello`
      * Target request URL: `https://my-project-id.appspot.com/BASE_PATH/hello`
  * `CONSTANT_ADDRESS`
    * `address`: `https://us-central1-my-project-id.cloudfunctions.net/helloGET`
    * With OpenAPI path parameters 
      * OpenAPI path: `/hello/{name}`
      * Request path: `/hello/world`
      * Target request URL: `https://us-central1-my-project-id.cloudfunctions.net/helloGET?name=world`
    * Without OpenAPI path parameters 
      * OpenAPI path: `/hello`
      * Request path: `/hello`
      * Target request URL: `https://us-central1-my-project-id.cloudfunctions.net/helloGET`



## `x-google-endpoints`

This section describes the uses of the `x-google-endpoints` extension.

### Configure API Gateway to allow CORS requests

If your API is called from a web application on a different origin, your API must support Cross-Origin Resource Sharing [(CORS)](https://docs.cloud.google.com/endpoints/docs/openapi/glossary#cors). See [Adding CORS support to API Gateway](https://docs.cloud.google.com/endpoints/docs/openapi/specify-proxy-startup-options#adding_cors_support_to_esp) for information on configuring API Gateway to support CORS.

If you need to implement custom CORS support in your backend code, set `allowCors: True` so that API Gateway passes all CORS requests through to your backend code:
    
    
    x-google-endpoints:
    - name: "API_NAME.endpoints.PROJECT_ID.cloud.goog"
      allowCors: True
    

Add the `x-google-endpoints` extension at the top level of your OpenAPI document (not indented or nested), for example:
    
    
    swagger: "2.0"
    host: "my-cool-api.endpoints.my-project-id.cloud.goog"
    x-google-endpoints:
    - name: "my-cool-api.endpoints.my-project-id.cloud.goog"
      allowCors: True
    

## `x-google-issuer`

`x-google-issuer: URI | EMAIL_ADDRESS`

This extension is used in the OpenAPI `securityDefinitions` section to specify the issuer of a credential. Values can take the form of a hostname or email address.

## `x-google-jwks_uri`

`x-google-jwks_uri: URI`

URI of the provider's public key set to validate the signature of the JSON Web Token.

The `x-google-jwks_uri` (OpenAPI 2.0) or `jwksUri` (OpenAPI 3.x) field _is_ required. API Gateway supports two asymmetric public key formats defined by this OpenAPI extension: 

  * [JWK set format](https://tools.ietf.org/html/rfc7517#section-5). For example: 

### OpenAPI 2.0
        
        x-google-jwks_uri: "https://YOUR_ACCOUNT_NAME.YOUR_AUTH_PROVIDER_URL/.well-known/jwks.json"
        

### OpenAPI 3.x
        
        jwksUri: "https://YOUR_ACCOUNT_NAME.YOUR_AUTH_PROVIDER_URL/.well-known/jwks.json"
        

  * [X509](https://tools.ietf.org/html/rfc5280). For example: 

### OpenAPI 2.0
        
        x-google-jwks_uri: "https://www.googleapis.com/service_accounts/v1/metadata/x509/securetoken@system.gserviceaccount.com"
        

### OpenAPI 3.x
        
        jwksUri: "https://www.googleapis.com/service_accounts/v1/metadata/x509/securetoken@system.gserviceaccount.com"
        

If you are using a symmetric key format, set the `x-google-jwks_uri` (OpenAPI 2.0) or `jwksUri` (OpenAPI 3.x) to the URI of a file that contains the base64url-encoded key string. 

**Note** : When API Gateway sends requests to the `x-google-jwks_uri` or `jwksUri`, the request will contain the `x-forwarded-proto` header.

## `x-google-jwt-locations`

By default, a JWT is passed either in the `Authorization` header (prefixed by `"Bearer "`), `X-Goog-Iap-Jwt-Assertion` header, or in the `access_token` query parameter.

Alternatively, use the `x-google-jwt-locations` extension in the OpenAPI securityDefinitions section to provide the customized locations from where to extract the JWT token.

**Note:** If you specify the `x-google-jwt-locations` extension, API Gateway then ignores all default locations.

The `x-google-jwt-locations` extension accepts a list of JWT locations. Each JWT location contains the following fields:

**Element** | **Description**  
---|---  
`header/query` | Required. The name for the header containing the JWT, or the name for the query parameter containing the JWT.  
`value_prefix` | Optional. For header only. When the `value_prefix` is set, its value must match the prefix of the header value containing the JWT.  
  
For example:
        
        x-google-jwt-locations:
          # Expect header "Authorization": "MyBearerToken <TOKEN>"
          - header: "Authorization"
            value_prefix: "MyBearerToken "
          # expect header "jwt-header-foo": "jwt-prefix-foo<TOKEN>"
          - header: "jwt-header-foo"
            value_prefix: "jwt-prefix-foo"
          # expect header "jwt-header-bar": "<TOKEN>"
          - header: "jwt-header-bar"
          # expect query parameter "jwt_query_bar=<TOKEN>"
          - query: "jwt_query_bar"
        

If you want to support only a subset of the default JWT locations, list them out explicitly in the `x-google-jwt-locations` extension. For example, to include support for only the `Authorization` header with the `"Bearer "` prefix:
        
        x-google-jwt-locations:
            # Support the default header "Authorization": "Bearer <TOKEN>"
            - header: "Authorization"
              value_prefix: "Bearer "
        

## `x-google-audiences`

`x-google-audiences: STRING`

This extension is used in the OpenAPI `securityDefinitions` section to provide a list of audiences that JWT `aud` field should match during JWT authentication. This extension accepts a single string with values separated by a comma. Spaces aren't allowed between the audiences. When it is not specified, JWT `aud` field should match the `host` field in the OpenAPI document.
        
        securityDefinitions:
          google_id_token:
            type: oauth2
            authorizationUrl: ""
            flow: implicit
            x-google-issuer: "https://accounts.google.com"
            x-google-jwks_uri: "https://www.googleapis.com/oauth2/v1/certs"
            x-google-audiences: "848149964201.apps.googleusercontent.com,841077041629.apps.googleusercontent.com"
        

**Beta**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

## `x-google-management`

The `x-google-management` extension controls different aspects of API management and contains the fields described in this section.

**Caution:** Ensure that your quota metrics and limits remain consistent across all active API configs before you create a new one. API Gateway applies the `metrics` and `quota` that you define here to the entire API rather than to an individual API config, so any metric or limit that a new API config declares replaces the definition for the whole API. If you rename or remove a metric, the quota-enforced methods of any gateway that still serves an earlier API config return an HTTP `500` error. For more information, see [Quotas apply to the whole API](https://docs.cloud.google.com/api-gateway/docs/quotas-overview#quotas_apply_to_the_whole_api).

### `metrics`

You use `metrics` in conjunction with quota and `x-google-quota` to configure a quota for your API. A quota lets you control the rate at which applications can call the methods in your API. For example:
        
        x-google-management:
          metrics:
            - name: read-requests
              displayName: Read requests
              valueType: INT64
              metricKind: DELTA
        

The `metrics` field contains a list with the following key-value pairs:

**Element** | **Description**  
---|---  
name | Required. The name for this metric. Typically, this is the type of request (for example, "read-requests" or "write-requests") that uniquely identifies the metric.  
displayName | Optional, but recommended. The text displayed to identify the metric on the **Quotas** tab on the **Endpoints** > **Services** page in the Google Cloud console. This text is also displayed to consumers of your API on the **Quotas** pages under **IAM & admin** and **APIs & Services**. The display name must be a maximum of 40 characters. For readability purposes, the unit from the associated quota limit is automatically appended to the display name in the Google Cloud console. For example, if you specify "Read requests" for the display name, then "Read requests per minute per project" is displayed in the Google Cloud console. If not specified, "unlabeled quota" is displayed to the consumers of your API on the **Quotas** pages under **IAM & admin** and **APIs & Services**.  To maintain consistency with the display names of Google services listed on the **Quotas** page that consumers of your API see, we recommend the following for the display name:
    * Use "Requests" when you have only one metric.
    * When you have multiple metrics, each should describe the type of request and contain the word "requests" (for example "Read requests" or "Write requests").
    * Use "quota units" instead of "requests" when any of the costs associated with the metric is greater than 1.  
valueType | Required. Must be INT64  
metricKind | Required. Must be DELTA  
  
### `quota`

You specify the [quota](https://docs.cloud.google.com/endpoints/docs/openapi/quotas-overview) limit for a defined metric in the `quota` section. For example:
    
    quota:
      limits:
        - name: read-requests-limit
          metric: read-requests
          unit: 1/min/{project}
          values:
            STANDARD: 5000
    

The `quota.limits` field contains a list with the following key:value pairs:

**Element** | **Description**  
---|---  
name | Required. Name of the limit, which must be unique within the service The name can contain lower and upper case letters, numbers and `-` (the dash character), and it must have a maximum length of 64 characters.  
metric | Required. The name of the metric this limit applies to. This name must match the text specified in the name of a metric. If the specified text doesn't match a metric name, you get an error when you deploy your OpenAPI document.   
unit | Required. The unit of the limit. Only "1/min/{project}" is supported, which means that the limit is enforced per-project and the usage is reset every minute.  
  
values | Required. The limit for the metric. You must specify this as a key:value pair, in the following format:   

    
    STANDARD: YOUR-LIMIT-FOR-THE-METRIC
    

You replace `YOUR-LIMIT-FOR-THE-METRIC` with an integer value that is the maximum number of requests allowed for the specified unit (which is only per-minute, per-project). For example:  

    
    values:
      STANDARD: 5000  
  
### `x-google-quota`

The `x-google-quota` extension is used in the OpenAPI `paths` section to associate a method in your API with a metric. Methods that don't have `x-google-quota` defined don't have quota limits applied to them. For example:
    
    x-google-quota:
      metricCosts:
        read-requests: 1
    

The `x-google-quota` extension contains the following item:

**Element** | **Description**  
---|---  
metricCosts | A user-defined key:value pair: `"YOUR-METRIC-NAME": METRIC-COST`.  

    * `"YOUR-METRIC-NAME":` The text for `"YOUR-METRIC-NAME"` must match a defined metric name. 
    * `METRIC-COST:` An integer value that defines the cost for each request. When a request is made, the associated metric is incremented by the specified cost. The cost allows methods to consume at different rates from the same metric. For example, if a metric has a quota limit of 1000 and a cost of 1, the calling application can make 1000 requests per minute before going over the limit. With a cost of 2 for the same metric, a calling application can make only 500 requests per minute before going over the limit.   
  
### Quota examples

The following example shows adding a metric and limit for read requests and write requests.
    
    x-google-management:
      metrics:
        # Define a metric for read requests.
        - name: "read-requests"
          displayName: "Read requests"
          valueType: INT64
          metricKind: DELTA
        # Define a metric for write requests.
        - name: "write-requests"
          displayName: "Write requests"
          valueType: INT64
          metricKind: DELTA
      quota:
        limits:
          # Rate limit for read requests.
          - name: "read-requests-limit"
            metric: "read-requests"
            unit: "1/min/{project}"
            values:
              STANDARD: 5000
          # Rate limit for write requests.
          - name: "write-request-limit"
            metric: "write-requests"
            unit: "1/min/{project}"
            values:
              STANDARD: 5000
    
    paths:
      "/echo":
        post:
          description: "Echo back a given message."
          operationId: "echo"
          produces:
          - "application/json"
          responses:
            200:
              description: "Echo"
              schema:
                $ref: "#/definitions/echoMessage"
          parameters:
          - description: "Message to echo"
            in: body
            name: message
            required: true
            schema:
              $ref: "#/definitions/echoMessage"
          x-google-quota:
            metricCosts:
              read-requests: 1
          security:
          - api_key: []
    

## `x-google-api-name`

When your service contains only one API, the API name is the same as the API Gateway service name. (API Gateway uses the name you specify in the `host` field of your OpenAPI document as the name of your service.) When your service contains more than one API, you specify the API names by adding the `x-google-api-name` extension to your OpenAPI document. The `x-google-api-name` extension lets you explicitly name individual APIs and establish independent versioning for each API.

For example, you can configure a service named `api.example.com` with two APIs, _producer_ and _consumer_ , with the OpenAPI document fragments shown here:

    * Producer API in `producer.yaml`: 
          
          swagger: 2.0
          host: api.example.com
          x-google-api-name: producer
          info:
            version: 1.0.3
          

    * Consumer API in `consumer.yaml`: 
          
          swagger: 2.0
          host: api.example.com
          x-google-api-name: consumer
          info:
            version: 1.1.0
          

You can deploy the two OpenAPI documents jointly with:
    
    gcloud api-gateway api-configs create API_CONFIG_ID \
      --api=my-api \
      --openapi-spec="producer.yaml,consumer.yaml" \
      --project=my-project-id

**Note:** API names must conform to the regular expression `[a-z][a-z0-9]{0,39}` (40 characters max, lowercase, no symbols)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 

    * ### Products and pricing

      * [ See all products ](https://cloud.google.com/products/)
      * [ Google Cloud pricing ](https://cloud.google.com/pricing/)
      * [ Google Cloud Marketplace ](https://cloud.google.com/marketplace/)
      * [ Contact sales ](https://cloud.google.com/contact/)
    * ### Support

      * [ Community forums ](https://discuss.google.dev/c/google-cloud/14/)
      * [ Support ](https://cloud.google.com/support-hub/)
      * [ Release Notes ](https://docs.cloud.google.com/release-notes)
      * [ System status ](https://status.cloud.google.com)
    * ### Resources

      * [ GitHub ](https://github.com/googlecloudPlatform/)
      * [ Getting Started with Google Cloud ](https://docs.cloud.google.com/docs/get-started/)
      * [ Code samples ](https://docs.cloud.google.com/docs/samples)
      * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture/)
      * [ Training and Certification ](https://cloud.google.com/learn/training/)
      * [ Builders Hub ](https://me.developers.google.com/)
    * ### Engage

      * [ Blog ](https://cloud.google.com/blog/)
      * [ Events ](https://cloud.google.com/events/)
      * [ X (Twitter) ](https://x.com/googlecloud)
      * [ Google Cloud on YouTube ](https://www.youtube.com/googlecloud)
      * [ Google Cloud Tech on YouTube ](https://www.youtube.com/googlecloudplatform)

[ ![Google Developers](https://www.gstatic.com/devrel-devsite/prod/v9ce9cb5b22b62a465ff52c45061a0a6a2d86a80b685e9aa8a182b203fdfbf420/clouddocs/images/lockup-google-for-developers.svg)](https://developers.google.com/)
    * [ Android ](https://developer.android.com/)
    * [ Chrome ](https://developer.chrome.com/)
    * [ Firebase ](https://firebase.google.com/)
    * [ Google AI ](https://ai.google.com/)
    * [ About Google ](https://about.google/)
    * [ Privacy ](https://policies.google.com/privacy)
    * [ Site terms ](https://policies.google.com/terms?hl=en)
    * [ Google Cloud terms ](https://cloud.google.com/product-terms)
    * Manage cookies 
    * [ Our third decade of climate action: join us ](https://cloud.google.com/sustainability)
    * Sign up for the Google Cloud newsletter [ Subscribe ](https://cloud.google.com/newsletter/)
    * English
    * Deutsch
    * Español
    * Español – América Latina
    * Français
    * Indonesia
    * Italiano
    * Português
    * Português – Brasil
    * עברית
    * 中文 – 简体
    * 中文 – 繁體
    * 日本語
    * 한국어



