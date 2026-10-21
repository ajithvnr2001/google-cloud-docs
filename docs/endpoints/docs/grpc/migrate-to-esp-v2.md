---
url: https://docs.cloud.google.com/endpoints/docs/grpc/migrate-to-esp-v2/
title: Migrate to Extensible Service Proxy V2 \u00a0|\u00a0 Cloud Endpoints with gRPC \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:06:44.171499+00:00
---

# Migrate to Extensible Service Proxy V2  |  Cloud Endpoints with gRPC  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/grpc/migrate-to-esp-v2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ gRPC ](https://docs.cloud.google.com/endpoints/docs/grpc/about-grpc)



Send feedback 

#  Migrate to Extensible Service Proxy V2 Stay organized with collections  Save and categorize content based on your preferences. 

[OpenAPI](https://docs.cloud.google.com/endpoints/docs/openapi/migrate-to-esp-v2 "View this page for the Cloud Endpoints OpenAPI docs") | gRPC

The [Extensible Service Proxy V2 (ESPv2)](https://docs.cloud.google.com/endpoints/docs/openapi/glossary#extensible_service_proxy_v2) is an [Envoy](https://www.envoyproxy.io/docs/envoy/latest/)-based proxy that enables Cloud Endpoints to provide API management features. ESPv2 replaces the NGINX-based [Extensible Service Proxy (ESP)](https://docs.cloud.google.com/endpoints/docs/openapi/glossary#extensible_service_proxy).

This document describes how to migrate an existing Endpoints API deployment from ESP to ESPv2.

## Before you begin

Before you begin the migration, consider the unsupported use cases and breaking API changes described below.

### ESPv2 unsupported use cases

  * **App Engine flexible environment is not supported**

App Engine flexible environment has built-in Endpoints support that is enabled by setting `endpoints_api_service` in the application's `app.yaml` file. This built-in Endpoints implementation only supports ESP; it can not be migrated to ESPv2.

If you want to use ESPv2 with App Engine flexible environment, disable `endpoints_api_service` in `app.yaml`. You can deploy ESPv2 as a separate Cloud Run service used to manage your application in App Engine flexible environment. The deployment works in the same way that ESPv2 is used to support [App Engine standard environment](https://docs.cloud.google.com/endpoints/docs/openapi/set-up-app-engine-standard-environment-espv2).

  * **Custom NGINX Configuration is not supported**

ESPv2 is an [Envoy](https://www.envoyproxy.io/docs/envoy/latest/)-based proxy. It cannot support custom NGINX proxy configuration. If your ESP configuration uses the `-n` or `--nginx_config` flags, your implementation may rely on a custom NGINX configuration that can't easily be migrated to ESPv2.




### Breaking changes

  * The `X-Endpoint-API-UserInfo` header data format is changed. If your application uses this header, it must be changed to use the new format. See Handle JWTs in the backend service for more details.
  * If an API key is required for a request, ESP sends the `X-Endpoint-API-Project-ID` header with the consumer project ID to the backend application. ESPv2 uses two different headers,`X-Endpoint-API-Consumer-Type` and `X-Endpoint-API-Consumer-Number`, to send required details. See the [Service Infrastructure reference documentation](https://cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/check#consumerinfo) for more details about the `Consumer-Type` and `Consumer-Number` sent with these headers.

  * The HTTP error response body format is changed. When ESPv2 rejects an HTTP request, it generates an error response body in a new format. If your implementation uses client code to process the HTTP error JSON response body, the client code must be updated. See HTTP Error JSON response body for more details.

  * New startup flags are available and some ESP flags have been deprecated or replaced in ESPv2. See Startup flag changes between ESP and ESPv2.




## Migrating your Endpoints APIs to use ESPv2

The migration steps required to use ESPv2 with serverless platforms (Cloud Run, Cloud Run functions, App Engine) differ from the steps required for non-serverless platforms (Google Kubernetes Engine, Compute Engine, and Kubernetes).

The migration steps required for each platform type are described below:

### Non-serverless platforms: GKE, Compute Engine, Kubernetes

ESPv2 is a drop-in replacement for ESP. For most configurations, you only need to update to the docker image tag.

However, you may need to adjust your startup flags if you configured ESP with:

  * More than one port via the `--http_port`, `http2_port`, and/or `--ssl_port` flags.
  * The `SSL`, `DNS`, `Client IP`, or another rarely-used flag.



New startup flags are available for ESPv2 and some ESP flags have been deprecated or replaced. See Startup flag changes between ESP and ESPv2 for more details.

#### GKE and Kubernetes

To migrate Endpoints configurations for GKE and Kubernetes, change the ESP image tag from `:1` to `:2` in the deployment `yaml` file. For example:
    
    
    - name: esp
      image: gcr.io/endpoints-release/endpoints-runtime:2
      args: [
        "--http_port=8081",
        "--backend=127.0.0.1:8080",
        "--service=SERVICE_NAME",
        "--rollout_strategy=managed",
      ]
    

#### Compute Engine

Both ESP and ESPv2 are deployed to the docker container using the `docker run` command. To migrate Endpoints for Compute Engine toESPv2, update the docker image tag from `:1` to `:2` in the command. For example:
    
    
    sudo docker run \
        --detach \
        DOCKER_ARGUMENTS \
        gcr.io/endpoints-release/endpoints-runtime:2 \
        --service=SERVICE_NAME \
        --rollout_strategy=managed \
        --backend=YOUR_API_CONTAINER_NAME:8080
    

### Serverless platforms (Cloud Run, Cloud Functions, App Engine)

For serverless platforms, ESPv2 is deployed as a Cloud Run service to manage your application running on Cloud Run, Cloud Function or App Engine. To migrate Endpoints to ESPv2, you must build your existing Endpoints service configuration into a new ESPv2 docker image, then deploy the image to your ESPv2 Cloud Run service.

The deployment steps for ESP and ESPv2 are identical, except for the following details:

  * The image tag should be changed from `:1` to `:2` in the ESPv2 when you deploy ESPv2 to Cloud Run. For example:
        
        gcloud run deploy CLOUD_RUN_SERVICE_NAME \
        --image="gcr.io/endpoints-release/endpoints-runtime-serverless:2" \
        --allow-unauthenticated \
        --platform managed \
        --project=ESP_PROJECT_ID  

  * The `gcloud_build_image` [script](https://github.com/GoogleCloudPlatform/esp-v2/tree/master/docker/serverless/gcloud_build_image) is downloaded from a different location. It uses `gcr.io/endpoints-release/endpoints-runtime-serverless:2` as the base image.

  * An environment variable is used to specify startup flags. The variable name for ESP is `ESP_ARGS`. The name for ESPv2 is `ESPv2_ARGS`. See [Extensible Service Proxy V2 startup options](https://docs.cloud.google.com/endpoints/docs/grpc/specify-esp-v2-startup-options) for more information on setting `ESPv2_ARGS` and the available startup flags.




## Startup flag changes between ESP and ESPv2

As with Extensible Service Proxy, you can specify configuration flags when deploying ESPv2 services. With the change from the NGINX-based ESP to the Envoy-based ESPv2, some flags have been deprecated or replaced and new flags have been added. This section uses three tables to describe the changes:

  * Table 1 describes new flags that replace deprecated flags.
  * [Table 2](https://docs.cloud.google.com/endpoints/docs/grpc/new-flags) describes new flags.
  * [Table 3](https://docs.cloud.google.com/endpoints/docs/grpc/deprecated-flags) describes deprecated flags.



### Replaced Flags

New flags | Replaced flags | Description  
---|---|---  
`--listener_port` | `--http_port`, `--http2_port`, `--ssl_port` | A single Envoy listener port supports http, http2 and ssl in ESPv2. There is no need to specify separate ports.   
`--ssl_server_cert_path` | `--ssl_port` |  When `--ssl_server_cert_path` is used, ESPv2 uses certs from `server.key` and `server.crt` files. With ESPv2 you can specify server cert paths other than `/etc/nginx/ssl`. This flag replaces `--ssl_port` in ESP, which uses certs from the `/etc/nginx/ssl/nginx.key` and `/etc/nginx/ssl/nginx.crt` file paths.   
`--ssl_backend_client_cert_path` | `--tls_mutual_auth`, `--enable_grpc_backend_ssl`, `--grpc_backend_ssl_private_key_file`, `--grpc_backend_ssl_cert_chain_file` | When `--ssl_backend_client_cert_path` is used, ESPv2 uses certs from `client.key` and `client.crt` files. With ESPv2, you can specify client cert paths other than `/etc/nginx/ssl`. This flag replaces `--tls_mutual_auth` in ESP, which uses certs from the `/etc/nginx/ssl/backend.key` and `/etc/nginx/ssl/backend.crt` file paths.   
`--ssl_backend_client_root_certs_file` | `--grpc_backend_ssl_root_certs_file` | With ESPv2, `--ssl_backend_client_root_certs_file` works for all backends. This flag replaces `--grpc_backend_ssl_root_certs_file` in ESP, which only works for gRPC backends.   
`--ssl_minimum_protocol`,`--ssl_maximum_protocol` | `--ssl_protocols` | When using `--ssl_protocols` in ESP, you must list all desired ssl protocols. In ESPv2, you can specify a min and max protocol.   
`--envoy_use_remote_address`,`--envoy_xff_num_trusted_hops` | `--xff_trusted_proxy_list`,`--client_ip_header`,`--client_ip_position` | Envoy requires `use_remote_address` and `xff_num_trusted_hops` to configure [client ip extraction](https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_conn_man/headers#config-http-conn-man-headers-x-forwarded-for).   
`--dns_resolver_addresses` | `--dns` | The replacement flag has the same behavior, but a different default value. ESP uses 8.8.8.8 as a DNS resolver. ESPv2 uses the DNS resolver configured in `/etc/resolv.conf`.   
`--service_account_key` | `--non_gcp`, `--service_account_key` |  In ESP, the `--service_account_key` flag implicitly allows deployment to platforms other than GCP. It prevents ESP from calling [Instance Metadata Server](https://cloud.google.com/compute/docs/storing-retrieving-metadata).  |  In ESPv2, this implicit behavior is split into another flag. You may need to add `--non_gcp` when migrating, otherwise ESPv2 will fail to start on platforms other than GCP.   
  
### New Flags

New flags | Description  
---|---  
`--http_request_timeout_s` | Sets the timeout for all http/https remote calls, except for backend calls and [Google Service Control](https://cloud.google.com/service-infrastructure/docs/service-control/reference/rest) calls, in seconds.   
`--service_control_check_timeout_ms` | Sets the timeout for [Google Service Control Check](https://cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/check) calls, in milliseconds.   
`--service_control_report_timeout_ms` | Sets the timeout for [Google Service Control Report](https://cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/report) calls.   
`--service_control_quota_timeout_ms` | Sets the timeout for [Google Service Control Quota](https://cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/allocateQuota) calls.   
`--service_control_check_retries` | Specifies the retry number for [Google Service Control Check](https://cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/check) calls.   
`--service_control_report_retries` | Specifies the retry number for [Google Service Control Report](https://cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/report) calls.   
`--service_control_quota_retries` | Specifies the retry number for [Google Service Control Quota](https://cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/allocateQuota) calls.   
`--backend_dns_lookup_family` | Envoy specific config used to define the DNS lookup family for all backends.   
`--disable_tracing` | A overall flag used to disable all traces.   
`--tracing_project_id` | Used to set the id of the project that owns the trace data.   
`--tracing_incoming_context` | used to specify the incoming trace context.   
`--tracing_outgoing_context` | Used to specify the outgoingtrace context.   
  
### Deprecated Flags

Deprecated flags | Description  
---|---  
`--enable_websocket` | Websocket is enabled by default in Envoy.   
`--experimental_proxy_backend_host_header` | Not supported.   
`--allow_invalid_headers` | Not supported. This is a NGINX config: [`ignore_invalid_headers`](http://nginx.org/en/docs/http/ngx_http_core_module.html#ignore_invalid_headers). If a HTTP request has invalid header names, it will be rejected by ESPv2. Valid header names are composed of English letters, digits, hyphens, and possibly underscores. In ESPv2, the flag `--underscores_in_headers` determines whether underscores are allowed in headers.   
`--client_max_body_size` | NGINX config, not supported.   
`--client_body_buffer_size` | NGINX config, not supported.   
`--large_client_header_buffers` | NGINX config, not supported.   
`--keepalive_timeout` | NGINX config, not supported.   
`--client_body_timeout` | NGINX config, not supported.   
`--rewrite` | Not supported.   
`--experimental_enable_multiple_api_configs` | Not supported.   
`--enable_backend_routing` | Not needed. Backend routing is automatically enabled for serverless platforms.   
`--rollout_fetch_throttle_window_in_s` | Not needed.   
`--nginx_config` | Not supported.   
  
Please see [Extensible Service Proxy V2 startup options](https://docs.cloud.google.com/endpoints/docs/grpc/specify-esp-v2-startup-options) for more detail regarding ESPv2 startup flags. Additional generic examples and help text for flags can be found in the [GitHub repository](https://github.com/GoogleCloudPlatform/esp-v2/blob/master/docker/generic/start_proxy.py).

## Default JWT locations

By default, a JWT is passed either in the `Authorization` header (prefixed by "Bearer "), the `X-Goog-Iap-Jwt-Assertion` header, or the `access_token` query parameter. These locations are supported by both ESP and ESPv2. You can also pass a JWT in the `Authorization` header (no prefix) when using ESP. However, this location is not supported in ESPv2.

If you want to keep passing JWTs using the `Authorization` header (no prefix) after migrating to ESPv2, you can:

  * Set [x-google-jwt-locations](https://docs.cloud.google.com/endpoints/docs/openapi/openapi-extensions#x-google-jwt-locations) in your openAPI file (for HTTP backend users):


    
    
    x-google-jwt-locations:
    - header: "Authorization"

  * Set [Authentication.providers.jwt_locations](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.AuthProvider) in your gRPC yaml file (for gRPC backend users):


    
    
    jwt_locations:
    - header: Authorization

**Note:** * If you specify the custom JWT locations, Endpoints then ignores all default locations. * The custom JWT location feature is supported by ESPv2 only.

## Handle JWTs in the backend service

When using JWTs to perform authentication, ESPv2 and ESP send the authentication result in the `X-Endpoint-API-UserInfo` header to the backend API. We recommend using this header instead of the original `Authorization` header, as the original `Authorization` header may be modified in serverless platforms.

The `X-Endpoint-API-UserInfo` header contains a [Base64Url encoded](https://tools.ietf.org/html/rfc4648#section-5) JSON object. However, its format has been changed from ESP to ESPv2.

For ESPv2, the `X-Endpoint-API-UserInfo` header contains the **original** JWT payload, **without any modification**.

In ESP, the `X-Endpoint-API-UserInfo` header contains the JWT payload and a few specific fields added by ESP. ESP adds the `id`, `issuer`, `email`, and `audiences` fields to the JSON object. It also adds the `claims` field to include the original JWT payload.
    
    
    # ESPv1 X-Endpoint-API-UserInfo header value
    {
      "id": "extracted from 'sub' field",
      "issuer": "extracted from 'iss' field",
      "email": "extracted from 'email' field",
      # The following "audiences" is extracted from 'aud' field.
      # The 'aud' field may have multiple audiences delimited by coma. e.g. "aud: aud1,aud2".
      # but the following "audiences" is always a JSON array.
      "audiences": ["aud1", "aud2"],
      "claims": {
         Original JWT payload
       }
    }
    

The following example illustrates the differences, all of them have been base64url decoded.
    
    
    # This is an example of the original JWT payload:
    {
      &quotiss&quot: &quothttps://accounts.google.com&quot,
      &quotemail&quot: &quotabcdefg123456@gmail.com&quot,
      &quotsub&quot: &quot1234567890123456789&quot,
      &quotaud&quot: &quotxyz1.example.com,xyz2.example.com&quot,
      &quotfoo&quot: &quotfoo.foo.foo.foo&quot,
      &quotbar&quot: &quotbar.bar.bar.bar&quot,
      &quotazp&quot: &quot98765432109876543210&quot,
      &quotexp&quot: &quot1642809446&quot,
      &quotiat&quot: &quot1642805846&quot
    }
    
    # This is an example of the `X-Endpoint-API-UserInfo` header from ESPv2
    # extracted from above JWT payload.
    {
      &quotiss&quot: &quothttps://accounts.google.com&quot,
      &quotemail&quot: &quotabcdefg123456@gmail.com&quot,
      &quotsub&quot: &quot1234567890123456789&quot,
      &quotaud&quot: &quotxyz1.example.com,xyz2.example.com&quot,
      &quotfoo&quot: &quotfoo.foo.foo.foo&quot,
      &quotbar&quot: &quotbar.bar.bar.bar&quot,
      &quotazp&quot: &quot98765432109876543210&quot,
      &quotexp&quot: &quot1642809446&quot,
      &quotiat&quot: &quot1642805846&quot
    }
    
    # This is an example of the `X-Endpoint-API-UserInfo` header from ESP
    # extracted from above JWT payload.
    {
      &quotid&quot:&quot1234567890123456789&quot,
      &quotissuer&quot: &quothttps://accounts.google.com&quot,
      &quotemail&quot: &quotabcdefg123456@gmail.com&quot,
      &quotaudiences&quot: [
        &quotxyz1.example.com&quot
        &quotxyz2.example.com&quot
      ],
      &quotclaims&quot: {
        &quotiss&quot: &quothttps://accounts.google.com&quot,
        &quotemail&quot: &quotabcdefg123456@gmail.com&quot,
        &quotsub&quot: &quot1234567890123456789&quot,
        &quotaud&quot: &quotxyz1.example.com,xyz2.example.com&quot,
        &quotfoo&quot: &quotfoo.foo.foo.foo&quot,
        &quotbar&quot: &quotbar.bar.bar.bar&quot,
        &quotazp&quot: &quot98765432109876543210&quot,
        &quotexp&quot: &quot1642809446&quot,
        &quotiat&quot: &quot1642805846&quot
      }
    }

See [Using a custom method to authenticate users](https://docs.cloud.google.com/endpoints/docs/grpc/authenticating-users-custom) and [Authentication between services](https://docs.cloud.google.com/endpoints/docs/grpc/service-account-authentication) for more on using JWTs with authentication.

## Error JSON response body format

If an HTTP request is rejected by ESP or ESPv2, the response body contains a status code and an error message in [JSON format](https://docs.cloud.google.com/apis/design/errors#http_mapping). The response body format has changed in ESPv2, as shown in the examples below:

The error response body from ESP
    
    
    {
     "code": 5,
     "message": "Method does not exist.",
     "details": [
      {
       "@type": "type.googleapis.com/google.rpc.DebugInfo",
       "stackEntries": [],
       "detail": "service_control"
      }
     ]
    }

The error response body from ESPv2
    
    
    {
     "code": 400,
     "message": "Method does not exist.",
    }

There are two primary differences:

  * In ESPv2, the `code` field contains an http status code, rather than [RPC status code](https://grpc.github.io/grpc/core/md_doc_statuscodes.html) found in ESP.
  * The error response body in ESPv2 does not contain a `details` field.



## What's next

Learn about:

  * [Extensible Service Proxy V2 startup options](https://docs.cloud.google.com/endpoints/docs/grpc/specify-esp-v2-startup-options)
  * [OpenAPI extensions](https://docs.cloud.google.com/endpoints/docs/grpc/openapi-extensions)
  * [The ESPv2 repo on GitHub](https://github.com/GoogleCloudPlatform/esp-v2)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
