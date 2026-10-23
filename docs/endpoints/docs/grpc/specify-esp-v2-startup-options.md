---
url: https://docs.cloud.google.com/endpoints/docs/grpc/specify-esp-v2-startup-options/
title: Extensible Service Proxy V2 startup options \u00a0|\u00a0 Cloud Endpoints with gRPC \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:00:49.723209+00:00
---

# Extensible Service Proxy V2 startup options  |  Cloud Endpoints with gRPC  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/grpc/specify-esp-v2-startup-options/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ gRPC ](https://docs.cloud.google.com/endpoints/docs/grpc/about-grpc)
  * [ Reference ](https://docs.cloud.google.com/endpoints/docs/grpc/specify-proxy-startup-options)



Send feedback 

#  Extensible Service Proxy V2 startup options Stay organized with collections  Save and categorize content based on your preferences. 

[OpenAPI](https://docs.cloud.google.com/endpoints/docs/openapi/specify-esp-v2-startup-options "View this page for the Cloud Endpoints OpenAPI docs") | gRPC

The [Extensible Service Proxy V2 (ESPv2)](https://docs.cloud.google.com/endpoints/docs/openapi/glossary#extensible_service_proxy_v2) is an [Envoy](https://www.envoyproxy.io/docs/envoy/latest/)-based proxy that enables Cloud Endpoints to provide API management features. To configure ESPv2, you can specify configuration flags when deploying the ESPv2 service.

## Setting configuration flags

The method for setting ESPv2 configuration flags varies based on deployment platform, as outlined in the following sections.

### Compute Engine VM

ESPv2 configuration flags for Compute Engine are specified in the `docker run` command. For example:
    
    
    sudo docker run \
        --detach \
        DOCKER_ARGUMENTS \
        gcr.io/endpoints-release/endpoints-runtime:2 \
        **--service= SERVICE_NAME** \
        **--rollout_strategy=managed** \
        **--backend= YOUR_API_CONTAINER_NAME:8080**

In this example, `--service`, `--rollout_strategy` and `--backend` are the ESPv2 configuration flags.

### GKE and Kubernetes

You can specify configuration flags for GKE and Kubernetes in the `args` field of your deployment manifest file. For example:
    
    
    containers:
    - name: esp
      image: gcr.io/endpoints-release/endpoints-runtime:2
      **args: [
        "--listener_port=8081",
        "--backend=127.0.0.1:8080",
        "--service= SERVICE_NAME",
        "--rollout_strategy=managed"
      ]**
    

In this example, `--listener_port`, `--backend`, `--service`, and `--rollout_strategy` are the ESPv2 configuration flags.

### Cloud Run for serverless platforms

To specify startup options for Cloud Run for serverless, use the ESPv2_ARGS environment variable. The variable can be set in the `gcloud run deploy` command by using the `--set-env-vars` option.

For example:
    
    
    gcloud run deploy CLOUD_RUN_SERVICE_NAME \
      --image="gcr.io/ESP_PROJECT_ID/endpoints-runtime-serverless:CLOUD_RUN_HOSTNAME-CONFIG_ID" \
      **-- set-env-vars=ESPv2_ARGS=--enable_debug**

In this example, `--enable_debug` is the ESPv2 configuration flag.

See [Cloud Functions for OpenAPI](https://docs.cloud.google.com/endpoints/docs/openapi/set-up-cloud-functions-espv2), [Cloud Run for OpenAPI](https://docs.cloud.google.com/endpoints/docs/openapi/set-up-cloud-run-espv2), or [Cloud Run for gRPC](https://docs.cloud.google.com/endpoints/docs/grpc/set-up-cloud-run-espv2) for more information on the `gcloud run deploy` command.

To set multiple arguments in the ESPv2_ARGS environment variable, specify a custom delimiter and use that delimiter to separate multiple arguments. Do not use a comma as a delimiter. Place the custom delimiter at the start of the ESPv2_ARGS environment variable, surrounded by carets.

The following example uses `++` as the delimiter: 
    
    
    gcloud run deploy CLOUD_RUN_SERVICE_NAME \
      --image="gcr.io/ESP_PROJECT_ID/endpoints-runtime-serverless:CLOUD_RUN_HOSTNAME-CONFIG_ID" \
      **-- set-env-vars=ESPv2_ARGS=^++^--cors_preset=basic++--cors_allow_origin=your_host.com**

If the flag you are setting contains commas, you must set the ESPv2_ARGS environment variable in the [gcloud_build_image](https://github.com/GoogleCloudPlatform/esp-v2/tree/master/docker/serverless/gcloud_build_image) script.

For example, to add the flag `--cors_allow_methods=PUT,POST,GET`:

  * Download the [gcloud_build_image](https://github.com/GoogleCloudPlatform/esp-v2/tree/master/docker/serverless/gcloud_build_image) script.
  * Edit the `gcloud_build_image` as shown below: 
        
        cat <<EOF > Dockerfile
          FROM BASE_IMAGE
        
          ENV ENDPOINTS_SERVICE_PATH /etc/endpoints/service.json
          COPY service.json \ENDPOINTS_SERVICE_PATH
        
          **ENV ESPv2_ARGS ^++^--cors_preset=basic++--cors_allow_method="GET,PUT,POST"++--cors_allow_credentials**
        
          ENTRYPOINT ["/env_start_proxy.py"]
          EOF

**Note** : A custom delimiter is used to separate multiple arguments.
  * Run the `gcloud_build_image` script to build the image.



## ESPv2 configuration flags

ESPv2 configuration flags can be grouped into the following categories:

  * Non-serverless configuration
  * Logging
  * Tracing
  * Health Check
  * Debugging
  * Local Testing
  * Non-Google Cloud Deployment
  * Client IP extraction
  * CORS support
  * TLS support
  * Timeout and retries
  * gRPC transcoding
  * Request and response modification
  * Security options
  * JWT authentication



Additional generic examples and help text for ESPv2 flags can be found found in the [GitHub repository.](https://github.com/GoogleCloudPlatform/esp-v2/blob/master/docker/generic/start_proxy.py)

### Non-Serverless Configuration

These flags are required to run ESPv2 in non-serverless platforms, such as GKE, Compute Engine, and Kubernetes. They can not be set when deployed in Cloud Run for serverless platforms.

**Note** : For Kubernetes users, **DO NOT** surround field values with quotes in config files. For example, `--cors_allow_origin="http://example.com"` will assign string value `\"http://example.com\"` to field `cor_allow_origin` instead of the intended string value `http://example.com`. ``

Flag | Description  
---|---  
`--service` | Sets the name of the Endpoints service.   
`--version` | Sets the service config ID of the Endpoints service.   
`--rollout_strategy` | Specifies the service config rollout strategy, [**fixed** |**managed**]. Default is **fixed**.   
`--listener_port` | Identifies the port to accept downstream connections. It supports HTTP/1.x, HTTP/2, and gRPC connections. Default is **8080**.   
`--backend` | Specifies the local backend application server address. Valid schemes are **http** , **https** , **grpc** , and **grpcs** if included. Default scheme is **> http**.   
  
### Logging

Use these flags to configure ESPv2 to write additional information to the Stackdriver log.

Flag | Description  
---|---  
`--log_request_headers` | Log the values of the specified request headers, separated by commas with no spaces. For example, set this flag as: `--log_request_headers=foo,bar` If values for the "foo" and "bar" header are available in the request, then the Endpoints log contains: `request_headers: foo=**_foo_value_** ;bar=**_bar_value_**`  
`--log_response_headers` | Log the values of the specified response headers, separated by commas with no spaces. For example, set this flag as: `--log_response_headers=baz,bing` If values for the "baz" and "bing" header are available in the response, then the Endpoints log contains: `response_headers: baz=**_baz_value_** ;bing=**_bing_value_**`  
`--log_jwt_payloads` | Log the values of the specified JWT payload primitive fields, separated by commas with no spaces. For example, set this flag as: `--log_jwt_payloads=sub,project_id,foo.foo_name ` If the values are available in the JWT payload, then the Endpoints log contains: `jwt_payloads: sub=**_sub_value_** ;project_id=**_project_id_value_** ; foo.foo_name=**_foo.foo_name_value_**` The values in the JWT payload must be primitive fields (string, integer). JSON objects and arrays are not logged.  
`--access_log` | If specified, the path to the local file where access log entries will be written.  
`--access_log_format` | String format to specify the format of access log. If unset, the [>default format string](https://www.envoyproxy.io/docs/envoy/latest/configuration/observability/access_log/usage#default-format-string) is used. For detailed format grammar, see the [format strings reference](https://www.envoyproxy.io/docs/envoy/latest/configuration/observability/access_log#format-strings).  
  
### Tracing

Use these flags to configure the ESPv2 tracing data sent to Stackdriver. These flags only apply when tracing is enabled. 

Flag | Description  
---|---  
`--disable_tracing` | Disable tracing. By default, tracing is enabled.  When enabled, ESPv2 samples a small number of requests to your API every second to get traces that it sends to Stackdriver Trace. By default, 1 out of 1000 requests are sampled. Use the `--tracing_sample_rate` flag to change the sampling rate.   
`--tracing_project_id` | The Google project ID for Stackdriver tracing. Tracing is a paid service. The specified project will be billed for tracing. By default, the project ID of the deployed ESPv2 service is billed. The project ID is determined by calling the Google Cloud Instance Metadata Server on startup. If ESPv2 is deployed outside of Google Cloud (using the `--non_gcp` flag), then tracing will be automatically disabled unless this flag is explicitly set.   
`--tracing_sample_rate` | Set the trace sampling rate to a value from 0.0 to 1.0. This value specifies the fraction of requests that are sampled. The default value is 0.001, which equates to 1 out of 1000 requests.   
`--tracing_incoming_context` |  This flag specifies which HTTP headers to check for the trace context, with flag values separated by commas with no spaces. Note that order matters: trace context will be derived from the first header that matches. Possible values include `traceparent`, `x-cloud-trace-context`, and `grpc-trace-bin`. If omitted, the `traceparent` and `x-cloud-trace-context` headers will be checked (in order). See [Tracing Your API](https://docs.cloud.google.com/endpoints/docs/openapi/tracing#trace-context-propagation) for more details.  
`--tracing_outgoing_context` |  Sets the trace context header in the request sent to the backend service. This flag specifies which HTTP header to set, with flag values separated by commas with no spaces. Possible values include `traceparent`, `x-cloud-trace-context`, and `grpc-trace-bin`. If omitted, the `traceparent` and `x-cloud-trace-context` headers will be sent. See [Tracing Your API](https://docs.cloud.google.com/endpoints/docs/openapi/tracing#trace-context-propagation) for more details.  
  
### Health Check

Use these flags to configure health checks for ESPv2. The first flag can be used to set up a health handler to respond to the health checking calls. The other flags can be used to enable health checking for the gRPC backend.

Flag | Description  
---|---  
`-z, --healthz` | Define a health checking endpoint. For example, `-z healthz` makes ESPv2 returns code 200 for path `/healthz`.   
`--health_check_grpc_backend` | Enable ESPv2 to periodically check gRPC Health service for a backend specified by the flag `--backend`. The backend must use gRPC protocol and implement the [gRPC Health Checking Protocol](https://github.com/grpc/grpc/blob/master/doc/health-checking.md). The health check endpoint enabled by the flag `--healthz` will reflect the backend health check result.   
`--health_check_grpc_backend_service` | Specify the service name when calling the backend gRPC Health Checking Protocol. The value of this flag is only applied when the flag `--health_check_grpc_backend` is used. It is optional, if not set, default is empty. An empty service name is to query the gRPC server overall health status.   
`--health_check_grpc_backend_interval` | Specify the checking interval and the request timeout when calling the backend gRPC Health service. The value of this flag is only applied when the flag `--health_check_grpc_backend` is used. Default is 1 second. The accepted format is a sequence of decimal numbers, each with optional fraction and a unit suffix, such as "5s", "100ms" or "2m". Valid time units are "m" for minutes, "s" for seconds, and "ms" for milliseconds.   
/tbody>

### Debugging

Use these flags to configure debugging for ESPv2. These flags can be used to set up an Envoy admin port to fetch configuration and statistics or run Envoy in debug mode to write debug level information to the log.

Flag | Description  
---|---  
`--status_port`, `--admin_port` | Enable ESPv2 Envoy admin on this port. Refer to the [Envoy administration interface reference](https://www.envoyproxy.io/docs/envoy/latest/operations/admin) for more details. The admin port is disabled by default.   
`--enable_debug` | Enable debug level logs and add debug headers.   
  
### Non-Google Cloud Deployment

If ESPv2 is deployed in a non Google Cloud environment, the following flags may be required.

Flag | Description  
---|---  
`--service_account_key` | Specifies the service account key JSON file to access Google services. If the option is omitted, the proxy contacts the Google Cloud metadata server to fetch an access token.   
`--dns_resolver_addresses` | The addresses of DNS resolvers. Each address should be in format of IP_ADDR or IP_ADDR:PORT and separated with a semi-colon (**;**). For IP_ADDR, the default DNS port 52 will be used. For example: `--dns_resolver_addresses=127.0.0.1;127.0.0.2;127.0.0.3:8000`) If unset, ESPv2 will use the default resolver configured in `/etc/resolv.conf`  
`--backend_dns_lookup_family` | Define the DNS lookup family for all backends. The options are **auto** , **v4only** , **v6only** , **v4preferred** and **all**. The default is **v4preferred**. Note that **auto** is a legacy value. Setting the flag to **auto** will result in behavior equivalent to **v6preferred**.   
`--non_gcp` | By default, the proxy attempts to connect to the [Google Cloud Metadata Server](https://cloud.google.com/appengine/docs/standard/java/accessing-instance-metadata) to get VM location in the first few requests. To skip this step, set this flag to **true**.   
  
### Local Testing

ESPv2 can be deployed locally on your workstation for testing. See [ Running ESP locally or on another platform](https://docs.cloud.google.com/endpoints/docs/openapi/running-esp-localdev) for more details. 

Use these flags along with the Non-Google Cloud Deployment flags for easier local deployment and testing in continuous integration. 

Flag | Description  
---|---  
`--service_json_path` |  Specify a path for ESPv2 to load the endpoint service config. With this flag, ESPv2 will use a "fixed" rollout strategy and the following flags will be ignored: 

  * `--service`
  * `--version`
  * `--rollout_strategy`

This flag will prevent ESPv2 from using the [Service Management API quota](https://docs.cloud.google.com/service-infrastructure/docs/quotas#management).   
`--enable_backend_address_override` |  Backend addresses can be specified using either the `--backend` flag or the `backend.rule.address` field in the service configuration. For OpenAPI users, note the `backend.rule.address` field is set by the `address` field in the `x-google-backend` extension.  The service configuration per-operation `backend.rule.address` is usually specified for serverless routing. By default, the `backend.rule.address` will take priority over the `--backend` flag for each individual operation.  Enable this flag if you want the `--backend` flag to take priority instead. This is useful if you are developing on a local workstation. Then you can use the same production service config but override the backend address via the `--backend` flag for local testing.  **Note** : Only the address will be overridden. All other components of `backend.rule` will still apply (deadlines, backend auth, path translation, etc).   
  
### Client IP Extraction

Use these flags to configure client IP extraction for ESPv2.

Flag | Description  
---|---  
`--envoy_use_remote_address` | Envoy HttpConnectionManager configuration, refer to Envoy [reference](https://www.envoyproxy.io/docs/envoy/latest/api-v3/extensions/filters/network/http_connection_manager/v3/http_connection_manager.proto.html) for detailed information. Default is **off**.   
`--envoy_xff_num_trusted_hops` | Envoy HttpConnectionManager configuration, refer to Envoy [reference](https://www.envoyproxy.io/docs/envoy/latest/api-v3/extensions/filters/network/http_connection_manager/v3/http_connection_manager.proto.html) for detailed information. The default value is 2.   
  
### CORS Support

Please refer to [Support CORS](https://docs.cloud.google.com/endpoints/docs/openapi/support-cors) for a description of available CORS support options. This section describes using ESPv2 startup flags to support CORS.

To enable CORS support in ESPv2, include the `--cors_preset` option and set it one of the following flags:

  * `--cors_preset=basic`
  * `--cors_preset=cors_with_regex`



When you include `--cors_preset=basic` or `--cors_preset=cors_with_regex`, ESPv2:

  * Assumes all location paths have the same CORS policy.
  * Responds to both [simple requests](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS#simple_requests) and [preflight](https://developer.mozilla.org/docs/Web/HTTP/CORS#Preflighted_requests) `HTTP OPTIONS` requests.
  * Caches the result of the preflight `OPTIONS` request for up to 20 days (1728000 seconds).
  * Sets the response headers to the following values:
        
        Access-Control-Allow-Origin: *
        Access-Control-Allow-Methods: GET, POST, PUT, PATCH, DELETE, OPTIONS
        Access-Control-Allow-Headers: DNT,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Range,Authorization
        Access-Control-Expose-Headers: Content-Length,Content-Range
        Access-Control-Max-Age: 1728000




To override the default value of [`Access-Control-Allow-Origin`](https://developer.mozilla.org/docs/Web/HTTP/Headers/Access-Control-Allow-Origin), specify one of the following options:

**Option** | **Description**  
---|---  
`--cors_allow_origin` | Use with `--cors_preset=basic` to set `Access-Control-Allow-Origin` to a specific origin.  
**Example:**  
` --cors_preset=basic  
--cors_allow_origin=http://example.com `  
`--cors_allow_origin_regex` | Use with `--cors_preset=cors_with_regex`. Allows you to use a regular expression to set `Access-Control-Allow-Origin`.  
**Example:**  
` --cors_preset=cors_with_regex  
--cors_allow_origin_regex=^https?://.+\.example\.com$ ` The regular expression in the preceding example allows an origin with either **http** or **https** and any subdomain of `example.com`. When you set this option in a Kubernetes configuration file, you need to add an additional backslash character to escape both instances of **\**. in the string, for example:  ` "--cors_preset","cors_with_regex",  
"--cors_allow_origin_regex","^https?://.+\\.example\\.com$" ` When you set this option in the gcloud_build_image script for Cloud Run, try to avoid using escaped characters and backslashes, they may not be passed correctly from the bash script to the proxy on startup. Use character classes instead of meta sequences. For example: ` Original: \d Recommended: [0-9] `  
  
After setting `--cors_preset=basic` or `--cors_preset=cors_with_regex` to enable CORS, you can override the default values of the other response headers by specifying one or more of the following options:

**Option** | **Description**  
---|---  
`--cors_allow_methods` | Sets [`Access-Control-Allow-Methods`](https://developer.mozilla.org/docs/Web/HTTP/Headers/Access-Control-Allow-Methods) to the specified HTTP methods. Specify the HTTP methods as a string with each HTTP method separated by a comma.  
**Example:**  
` --cors_preset=basic  
--cors_allow_methods=GET,POST,PUT,OPTIONS `  
`--cors_allow_headers` | Sets [`Access-Control-Allow-Headers`](https://developer.mozilla.org/docs/Web/HTTP/Headers/Access-Control-Allow-Headers) to the specified HTTP headers. Specify the HTTP headers as a string with each HTTP header separated by a comma.  
**Example:**  
` --cors_preset=basic  
--cors_allow_headers=Origin,Content-Type,Accept `  
`--cors_allow_credentials` | Includes the [`Access-Control-Allow-Credentials`](https://developer.mozilla.org/docs/Web/HTTP/Headers/Access-Control-Allow-Credentials) header with the value **true** in responses. By default, the `Access-Control-Allow-Credentials` header isn't included in responses.  
**Example:**  
` --cors_preset=basic  
--cors_allow_credentials `  
`--cors_expose_headers` | Sets [`Access-Control-Expose-Headers`](https://developer.mozilla.org/docs/Web/HTTP/Headers/Access-Control-Expose-Headers) to the specified headers. Specify which headers can be exposed as part of the response as a string with each header separated by a comma.  
**Example:**  
` --cors_preset=basic  
--cors_expose_headers=Content-Length `  
`--cors_max_age` | Sets [`Access-Control-Max-Age`](https://developer.mozilla.org/docs/Web/HTTP/Headers/Access-Control-Max-Age) to the specified time duration. The acceptable format is a sequence of decimal numbers, each with an optional fractional value and a unit suffix, such as "300m", "1.5h" or "2h45m". Valid time units are "m" for minutes, "h" for hours. The default value is "480h" if not set.  
**Example:**  
` --cors_preset=basic  
--cors_max_age=24h `  
  
### TLS Support

Use these flags to configure ESPv2 to use TLS connections.

Flag | Description  
---|---  
`--ssl_server_cert_path` | Proxy's server cert path. When configured, ESPv2 only accepts HTTP/1.x and HTTP/2 secure connections on listener_port. Requires the certificate and key files "server.crt" and "server.key" within this path.   
`--ssl_server_cipher_suites` |  Cipher suites to use for downstream connections, specified as a comma-separated list. Please refer to [ Cipher suite configuration](https://commondatastorage.googleapis.com/chromium-boringssl-docs/ssl.h.html#Cipher-suite-configuration).   
`--ssl_backend_client_cert_path` | Proxy's client cert path. When configured, ESPv2 enables TLS mutual authentication for HTTPS backends. Requires the certificate and key files "client.crt" and "client.key" within this path.   
`--ssl_backend_client_root_certs_file` | The file path of root certificates that ESPv2 uses to verify backend server certificate. If not specified, ESPv2 uses "/etc/ssl/certs/ca-certificates.crt" by default.   
`--ssl_backend_client_cipher_suites` |  Cipher suites to use for HTTPS backends, specified as a comma-separated list. Please refer to [ Cipher suite configuration](https://commondatastorage.googleapis.com/chromium-boringssl-docs/ssl.h.html#Cipher-suite-configuration).   
`--ssl_minimum_protocol` | Minimum TLS protocol version for client side connection. Please refer to [this](https://www.envoyproxy.io/docs/envoy/latest/api-v3/extensions/transport_sockets/tls/v3/common.proto.html?highlight=common%20tls%20configuration)  
`--ssl_maximum_protocol` | Maximum TLS protocol version for client side connection. Please refer to [this](https://www.envoyproxy.io/docs/envoy/latest/api-v3/extensions/transport_sockets/tls/v3/common.proto.html?highlight=common%20tls%20configuration)  
`--enable_strict_transport_security` | Enable HSTS (HTTP Strict Transport Security). "Strict-Transport-Security" response header with value "max-age=31536000; includeSubdomains;" is added for all responses.   
`--generate_self_signed_cert` | Generate a self-signed certificate and key at start, then store them in "/tmp/ssl/endpoints/server.crt" and "/tmp/ssl/endpoints/server.key". This is useful when only a random self-sign cert is needed to serve HTTPS requests. Generated certificate will have Common Name "localhost" and valid for 10 years.   
  
### Timeout and Retries

Use these flags to configure remote HTTP call timeout and retries for ESPv2.

Flag | Description  
---|---  
`--http_request_timeout_s` | Set the timeout in seconds for requests made to external services except Backend and Google Service Control. It includes Google ServiceManagement, Metadata server, and Google IAM server. Must be **> 0** and the default is **30** seconds if not set.   
`--service_control_network_fail_policy` | In case of network failures when connecting to Google service control, the requests will be allowed if this flag is **open**. The default is **open**.   
`--service_control_check_timeout_ms` | Set the timeout in millisecond for service control Check request. Must be **> 0** and the default is **1000** if not set.   
`--service_control_report_timeout_ms` | Set the timeout in millisecond for service control Report request. Must be **> 0** and the default is **1000** if not set.   
`--service_control_quota_timeout_ms` | Set the timeout in millisecond for service control Quota request. Must be **> 0 ** and the default is **1000** if not set.   
`--service_control_check_retries` | Set the retry times for service control Check request. Must be **> = 0** and the default is **3** if not set   
`--service_control_report_retries` | Set the retry times for service control Report request. Must be **> = 0** and the default is **5** if not set   
`--service_control_quota_retries` | Set the retry times for service control Quota request. Must be **> = 0** and the default is **1** if not set   
`--backend_retry_ons` |  The conditions under which ESPv2 does retry on the backends. One or more `retryOn` conditions can be specified using a comma-separated list. The default is `reset,connect-failure,refused-stream`. Disable retry by setting this flag to empty.  Refer to the following links for the accepted conditions: 

  * [x-envoy-retry-on](https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_filters/router_filter#x-envoy-retry-on)
  * [x-envoy-retry-grpc-on](https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_filters/router_filter#x-envoy-retry-grpc-on)

  
`--backend_retry_num` |  The allowed number of retries. Must be >= 0 and defaults to 1.   
  
### gRPC Transcoding

Use these flags to configure ESPv2 for HTTP/JSON to gRPC transcoding.

Flag | Description  
---|---  
`--transcoding_always_print_primitive_fields` | Specifies whether to print primitive fields for grpc-json transcoding. By default, primitive fields with default values will be omitted in JSON output. For example, an int32 field set to 0 will be omitted. Setting this flag to **true** will override the default behavior and print primitive fields regardless of their values. Defaults to **false**.   
`--transcoding_always_print_enums_as_ints` | Specifies whether to print enums as ints for grpc-json transcoding. By default they are rendered as strings. Defaults to **false**.   
`--transcoding_stream_newline_delimited` | If true, use new line delimiter to separate response streaming messages. If false, all response streaming messages are transcoded into a JSON array.   
`--transcoding_case_insensitive_enum_parsing` | Normally, proto enum values should be in upper cases when used in JSON. Set this flag to true if your JSON request uses non uppercase enum values.   
`--transcoding_preserve_proto_field_names` | Specifies whether to preserve proto field names for grpc-json transcoding. By default, protobuf will generate JSON field names using the json_name option, or lower camel case, in that order. Setting this flag will preserve the original field names. Defaults to **false**.   
`--transcoding_ignore_query_parameters` | A list of comma-separated query parameters to be ignored for transcoding method mapping in grpc-json transcoding. By default, the transcoder filter will not transcode a request with unknown/invalid query parameters.   
`--transcoding_ignore_unknown_query_parameters` | Specifies whether to ignore query parameters that cannot be mapped to a corresponding protobuf field in grpc-json transcoding. Use this if you cannot control the query parameters and do not know them beforehand. Otherwise, use `--transcoding_ignore_query_parameters`. Defaults to **false**.   
`--transcoding_query_parameters_disable_unescape_plus` | By default, plus signs `"+"` in the query parameters are unescaped into space `" "` in grpc-json transcoding. This is to support [HTML 2.0.](https://tools.ietf.org/html/rfc1866#section-8.2.1) If it is not desired, set this flag to true to disable this feature.   
  
### Request and Response Modification

Use these flags to configure ESPv2 to partially modify requests and responses.

Flag | Description  
---|---  
`--add_request_header` |  Add an HTTP header to the request before sending it to the upstream backend. If the header is already in the request, its value will be replaced with the new one.  It supports [Envoy custom variables](https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_conn_man/headers#custom-request-response-headers).  This argument can be repeated multiple times to specify multiple headers. For example: `--add_request_header=key1=value1 --add_request_header=key2=value2`.   
`--append_request_header` |  Append an HTTP header to the request before sending it to the upstream backend. If the header is already in the request, the new value will be appended.  It supports [Envoy custom variables](https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_conn_man/headers#custom-request-response-headers).  This argument can be repeated multiple times to specify multiple headers. For example: `--append_request_header=key1=value1 --append_request_header=key2=value2`.   
`--add_response_header` |  Add an HTTP header to the response before sending it to the downstream client. If the header is already in the response, it will be replaced with the new one.  It supports [Envoy custom variables](https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_conn_man/headers#custom-request-response-headers).  This argument can be repeated multiple times to specify multiple headers. For example: `--add_response_header=key1=value1 --add_response_header=key2=value2`.   
`--append_response_header` |  Append an HTTP header to the response before sending it to the downstream client. If the header is already in the response, the new one will be appended.  It supports [Envoy custom variables](https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_conn_man/headers#custom-request-response-headers).  This argument can be repeated multiple times to specify multiple headers. For example: `--append_response_header=key1=value1 --append_response_header=key2=value2`.   
  
### Security Options

Use these flags to further refine the requests ESPv2 allows.

Flag | Description  
---|---  
`--underscores_in_headers` |  Allow header names that contain underscores to pass through. Defaults to **false**.  The underscore character is allowed in header names by [RFC-7230](https://tools.ietf.org/html/rfc7230#section-3.2.6). However, this behavior is implemented as a security measure because some systems treat `_` and `-` as interchangeable.   
`--envoy_connection_buffer_limit_bytes` |  Configure the maximum amount of data that is buffered for each request/response body, in bytes. If not set, default is decided by Envoy. See [Envoy's listener configuration](https://www.envoyproxy.io/docs/envoy/latest/api-v3/config/listener/v3/listener.proto).   
`--disable_normalize_path` |  Disable normalization of the `path` HTTP header according to [RFC 3986](https://datatracker.ietf.org/doc/html/rfc3986#section-6). We recommend keeping this option enabled if your backend performs path normalization by default.  The following table provides examples of the request `path` the backend will receive from ESPv2 based on the configuration of this flag. 
    
    
            -----------------------------------------------------------------
            | Request Path     | Without Normalization | With Normalization |
            -----------------------------------------------------------------
            | /hello/../world  | Rejected              | /world             |
            | /%4A             | /%4A                  | /J                 |
            | /%4a             | /%4a                  | /J                 |
            -----------------------------------------------------------------
         

By default, ESPv2 will normalize paths. Disable the feature only if your traffic is affected by the behavior.  **Note** : Following RFC 3986, this option does not unescape percent-encoded slash characters. See flag `--disallow_escaped_slashes_in_path` to enable this non-compliant behavior.  **Note** : [Case normalization](https://datatracker.ietf.org/doc/html/rfc3986#section-6.2.2.1) from RFC 3986 is not supported, even if this option is enabled.  For more details, see [Understanding Path Templating](https://docs.cloud.google.com/api-gateway/docs/path-templating).   
`--disable_merge_slashes_in_path` |  Disable merging of adjacent slashes in the `path` HTTP header. We recommend keeping this option enabled if your backend performs merging by default.  The following table provides examples of the request `path` the backend will receive from ESPv2 based on the configuration of this flag. 
    
    
            -----------------------------------------------------------------
            | Request Path     | Without Normalization | With Normalization |
            -----------------------------------------------------------------
            | /hello//world    | Rejected              | /hello/world       |
            | /hello///        | Rejected              | /hello             |
            -----------------------------------------------------------------
         

By default, ESPv2 will merge slashes. Disable the feature only if your traffic is affected by the behavior.  For more details, see [Understanding Path Templating](https://docs.cloud.google.com/api-gateway/docs/path-templating).   
`--disallow_escaped_slashes_in_path` |  Disallows requests with escaped percent-encoded slash characters: 

  * `%2F` or `%2f` is treated as a `/`
  * `%5C` or `%5c` is treated as a `\`

When enabled, the behavior depends on the protocol used: 

  * For OpenAPI backends, request paths with escaped percent-encoded slashes will be automatically unescaped via a redirect.
  * For gRPC backends, request paths with escaped percent-encoded slashes will be rejected (gRPC does not support redirects).

This option is **not** [RFC 3986](https://datatracker.ietf.org/doc/html/rfc3986#section-6) compliant, so it is turned off by default. If your backend is **not** RFC 3986 compliant and escapes slashes, you **must** enable this option in ESPv2. This will prevent path confusion attacks that result in security requirements not being enforced.  For more details, see [Understanding Path Templating](https://docs.cloud.google.com/api-gateway/docs/path-templating).   
  
### JWT Authentication

Use these flags to configure ESPv2 to fetch remote Jwks with retries.

Flag | Description  
---|---  
`--jwks_fetch_num_retries` |  Specify the number of retries in the remote JWKS fetch retry policy. The default is 0, not retry.   
`--jwks_fetch_retry_back_off_base_interval_ms` |  Specify the JWKS fetch retry exponential back off base interval, in milliseconds. The default is 200ms, if not set.   
`--jwks_fetch_retry_back_off_max_interval_ms` |  Specify the JWKS fetch retry exponential back off maximum interval, in milliseconds. The default is 32s, if not set.   
`--jwks_cache_duration_in_s` |  Specify JWT public key cache duration in seconds. The default is 5 minutes, if not set.   
`--jwks_async_fetch_fast_listener` |  Only apply when `--disable_jwks_async_fetch` flag is not set. This flag determines if ESPv2 will wait for the initial `jwks` fetch to complete before binding the listener port. If false, it will wait. Default is false.   
`--jwt_cache_size` |  Specify the number of unique JWT tokens as the maximum JWT cache size. The cache only stores verified tokens. If 0, JWT cache is disabled. This flag limits the memory usage for the JWT cache. The cache used memory is roughly (token size + 64 bytes) per token. If not specified, the default is 100000.   
`--disable_jwt_audience_service_name_check` |  Normally JWT `aud` field is checked against audiences specified in OpenAPI `x-google-audiences` field. This flag changes the behavior when the `x-google-audiences` field is not specified. When the `x-google-audiences` field is not specified, and this flag is not used, the service name is used to check the JWT `aud` field. If this flag is used, JWT `aud` field will not be checked.   
  
## What's next

Learn about:

  * [Migrate to Extensible Service Proxy V2](https://docs.cloud.google.com/endpoints/docs/grpc/migrate-to-esp-v2)
  * [OpenAPI extensions](https://docs.cloud.google.com/endpoints/docs/grpc/openapi-extensions)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
