---
url: https://docs.cloud.google.com/endpoints/docs/openapi/oasv3-extensions/
title: OpenAPI 3.x extensions \u00a0|\u00a0 Cloud Endpoints with OpenAPI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:46:17.927168+00:00
---

# OpenAPI 3.x extensions  |  Cloud Endpoints with OpenAPI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/openapi/oasv3-extensions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ OpenAPI ](https://docs.cloud.google.com/endpoints/docs/openapi)



Send feedback 

#  OpenAPI 3.x extensions Stay organized with collections  Save and categorize content based on your preferences. 

OpenAPI | gRPC

Endpoints accepts a set of Google-specific extensions to the OpenAPI specification that configure the behaviors of the gateway. These extensions allow you to specify API management settings, authentication methods, quota limits, and backend integrations directly within your OpenAPI document. Understanding these extensions helps you tailor your service behavior and integrate with Endpoints features.

This page describes Google-specific extensions to the [OpenAPI specification 3.x](https://docs.cloud.google.com/endpoints/docs/openapi/openapi-overview).

Although the examples given are in YAML format, JSON is also supported.

## `x-google-api-management`

**Required.**

The `x-google-api-management` extension defines top-level API management settings for your service. Place this extension at the root of your OpenAPI document.

The following table describes the fields for `x-google-api-management`:

Field | Type | Required | Default | Description  
---|---|---|---|---  
`metrics` | `map[string]Metric` | No | Empty | Define metrics to enforce quota limits.  
`quota` | `map[string]Quota` | No | Empty | Specify quota limits for your service.  
`backends` | `map[string]Backend` | No | Empty | Configure backend services.  
`apiName` | `string` | No | Empty | Associate a name with the operations defined in the OpenAPI document.  
  
### `Metric` Object

The `Metric` object defines a metric used for quota enforcement.

The following table describes the fields for `Metric`:

Field | Type | Required | Default | Description  
---|---|---|---|---  
`displayName` | `string` | No | Empty | Display name of the metric.  
  
### `Quota` Object

The `Quota` object defines quota limits.

The following table describes the fields for `Quota`:

Field | Type | Required | Default | Description  
---|---|---|---|---  
`limits` | `map[string]QuotaLimit` | No | Empty | Specify quota limits.  
  
### `Quota Limit` Object

The `QuotaLimit` object defines a specific quota limit.

The following table describes the fields for `QuotaLimit`:

Field | Type | Required | Description  
---|---|---|---  
`metric` | `string` | Yes | Reference a metric declared in this OpenAPI document.  
`values` | `int64` | Yes | Set the maximum value the metric can reach before client requests are denied.  
  
### `Backend` Object

The `Backend` object configures a backend service. You must set either `jwtAudience` or `disableAuth`.

The following table describes the fields for `Backend`:

Field | Type | Required | Default | Description  
---|---|---|---|---  
`address` | `string` | No | Empty | Specify the URL of the backend.  
`jwtAudience` | `string` | No | Empty | By default, Endpoints will create the instance ID token with a JWT audience that matches the address field. Manually specifying `jwt_audience` is only required when the target backend uses JWT-based authentication and the expected audience is different than the value specified in the address field. For remote backends deployed on App Engine or with IAP, you must override the JWT audience. App Engine and IAP use their OAuth client ID as the expected audience.  
`disableAuth` | `bool` | No | `False` | Prevent the data plane proxy from obtaining an instance ID token and attaching it to the request.  
`pathTranslation` | `string` | No | `APPEND_PATH_TO_ADDRESS` or `CONSTANT_ADDRESS` | Set the path translation strategy when proxying requests to the target backend. When `x-google-backend` is set at the top level, the default `pathTranslation` is `APPEND_PATH_TO_ADDRESS`. When `x-google-backend` is set on an operation, the default is `CONSTANT_ADDRESS`.  
`deadline` | `double` | No | `15.0` | Specify the number of seconds to wait for a full response from a request. Responses that exceed this deadline time out.  
`protocol` | `string` | No | `http/1.1` | Set the protocol for sending a request to the backend. Supported values include `http/1.1` and `h2`.  
  
## `x-google-auth`

**Optional.**

The `x-google-auth` extension defines authentication settings within a Security Scheme Object.

The following table describes the fields for `x-google-auth`:

Field | Type | Required | Default | Description  
---|---|---|---|---  
`issuer` | `string` | No | Empty | Specify the issuer of a credential. Values can be a hostname or email address.  
`jwksUri` | `string` | No | Empty | Provide the URI of the provider's public key set to validate the JSON Web Token signature.  
`audiences` | `[string]` | No | Empty | List audiences that the JWT `aud` field must match during JWT authentication.  
`jwtLocations` | `[JwtLocations]` | No | Empty | Customize locations for the JWT token. By default, a JWT passes in the `Authorization` header (prefixed by "Bearer "), `X-Goog-Iap-Jwt-Assertion` header, or the `access_token` query parameter.  
  
### `JwtLocations` Object

The `JwtLocations` object provides customized locations for the JWT token.

The following table describes the fields for `JwtLocations`:

Field | Type | Required | Default | Description  
---|---|---|---|---  
`header` | `query` | `string` | Yes | N/A | Specify the name for the header containing the JWT, or the name for the query parameter containing the JWT.  
`valuePrefix` | `string` | No | Empty | For header only. When set, its value must match the prefix of the header value containing the JWT.  
  
## `x-google-quota`

**Optional.**

The `x-google-quota` extension defines quota limits. You can define this extension at the top-level of your OpenAPI document or for an individual operation.

The following table describes the fields for `x-google-quota`:

Field | Type | Required | Description  
---|---|---|---  
`self` | `map[string]int64` | Yes | The `quota` object (`self`) references any metrics defined within the object. In this case, map a metric (such as `read-requests`) to an amount to increment the metric. Requests are rejected when the metric value meets the quota limit.  
  
## `x-google-backend`

**Required.**

The `x-google-backend` extension references a backend defined in `x-google-api-management`. You must set this extension for Endpoints. You can define this extension at the top-level of your OpenAPI document or for an individual operation.

The following table describes the fields for `x-google-backend`:

Field | Type | Required | Description  
---|---|---|---  
`self` | `string` | Yes | Reference the ID of a backend defined in `x-google-api-management`.  
  
## `x-google-endpoint`

**Required.**

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
`target` | `string` | No |  | Specify the IP address that the host resolves to.  
`allowCors` | `bool` | No | `false` | Allow CORS requests.  
  
## Understand OpenAPI Extension Limitations

These OpenAPI extensions have specific limitations. To learn more, see [OpenAPI 3.x feature limitations](https://docs.cloud.google.com/endpoints/docs/openapi/openapi-v3-limitations).

## What's next

  * Explore the [OpenAPI Specification](https://swagger.io/specification/).
  * Review Endpoints documentation for specific Endpoints or ESPv2 configurations.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
