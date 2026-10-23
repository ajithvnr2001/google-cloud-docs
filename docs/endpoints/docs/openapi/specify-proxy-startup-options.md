---
url: https://docs.cloud.google.com/endpoints/docs/openapi/specify-proxy-startup-options/
title: Extensible Service Proxy startup options \u00a0|\u00a0 Cloud Endpoints with OpenAPI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:01:25.463391+00:00
---

# Extensible Service Proxy startup options  |  Cloud Endpoints with OpenAPI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/openapi/specify-proxy-startup-options/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ OpenAPI ](https://docs.cloud.google.com/endpoints/docs/openapi)
  * [ Reference ](https://docs.cloud.google.com/endpoints/docs/openapi/specify-proxy-startup-options)



Send feedback 

#  Extensible Service Proxy startup options Stay organized with collections  Save and categorize content based on your preferences. 

OpenAPI | [gRPC](https://docs.cloud.google.com/endpoints/docs/grpc/specify-proxy-startup-options "View this page for the Cloud Endpoints gRPC docs")

The [Extensible Service Proxy (ESP)](https://docs.cloud.google.com/endpoints/docs/openapi/glossary#extensible_service_proxy) is an [NGINX-based](https://docs.cloud.google.com/endpoints/docs/openapi/glossary#nginx) proxy that enables Cloud Endpoints to provide API management features. You configure ESP by specifying options when you start the ESP Docker container. When the ESP container starts, it runs a script called `start_esp`, which writes the NGINX configuration file by using the options that you specified and launches ESP.

You specify ESP startup options in the `docker run` command, for example:
    
    
    sudo docker run \
        --detach \
        DOCKER_ARGUMENTS \
        gcr.io/endpoints-release/endpoints-runtime:1 \
        --service=SERVICE_NAME \
        --rollout_strategy=managed \
        --backend=YOUR_API_CONTAINER_NAME:8080
    

If you are deploying ESP to Kubernetes, you specify the startup options in your deployment manifest file in the `args` field, for example:
    
    
    containers:
    - name: esp
      image: gcr.io/endpoints-release/endpoints-runtime:1
      args: [
        "--http_port=8081",
        "--backend=127.0.0.1:8080",
        "--service=SERVICE_NAME",
        "--rollout_strategy=managed"
      ]
    

The following table describes ESP's startup options.

**Short option** | **Long option** | **Description**  
---|---|---  
`-s SERVICE_NAME` | `--service SERVICE_NAME` | Sets the name of the Endpoints service.   
`-R ROLLOUT_STRATEGY` | `--rollout_strategy ROLLOUT_STRATEGY` | Available in ESP version 1.7.0 and later. Specify either `managed` or `fixed`. The `--rollout_strategy=managed` option configures ESP to use the latest deployed service configuration. When you specify this option, up to 5 minutes after you deploy a new service configuration, ESP detects the change and automatically begins using it. We recommend that you specify this option instead of a specific configuration ID for ESP to use. You don't need to specify the `--version` option when you set `--rollout_strategy` to `managed`.  
`-v CONFIG_ID` | `--version CONFIG_ID` | Sets the service configuration ID to be used by ESP. See [Getting the service name and configuration ID](https://docs.cloud.google.com/endpoints/docs/openapi/get-service-name-config-id) for the information you need to set this option. When you specify `--rollout_strategy=fixed` or when you don't include the `--rollout_strategy` option, you must include the `--version` option and specify a configuration ID. In this case, every time you deploy a new Endpoints configuration, you must restart ESP with the new configuration ID.   
`-p HTTP1_PORT` | `--http_port HTTP1_PORT` | Sets the ports that ESP exposes for HTTP/1.x connections.1  
`-P HTTP2_PORT` | `--http2_port HTTP2_PORT` | Sets the ports that ESP exposes for HTTP/2 connections.1  
`-S SSL_PORT` | `--ssl_port SSL_PORT` | Sets the ports that ESP exposes for HTTPS connections.1  
`-a BACKEND` | `--backend BACKEND` | Sets the address for the HTTP/1.x application backend server. The default value for the backend address is `http://127.0.0.1:8081`.  
You can specify a protocol prefix, for example:  
`--backend=https://127.0.0.1:8000`  
If you don't specify a protocol prefix, the default is `http`.  
If your backend server is running on Compute Engine in a container, you can specify the container name and the port, for example:  
`--backend=my-api-container:8000`  
  
`-N STATUS_PORT` | `--status_port STATUS_PORT` | Sets the status port (default: `8090`).   
none | `--disable_cloud_trace_auto_sampling` | By default, ESP samples 1 request out of every 1000 or 1 request out of every 10 seconds is enabled with Cloud Trace. Set this flag to disable such auto sampling. Cloud Trace can still be enabled from request HTTP headers with trace context regardless of this flag value. See [Tracing your API](https://docs.cloud.google.com/endpoints/docs/openapi/tracing) for more information.   
`-n NGINX_CONFIG` | `--nginx_config NGINX_CONFIG` | Sets the location for the custom NGINX configuration file. If you specify this option, ESP fetches the specified configuration file and then immediately launches NGINX with the provided custom configuration file. See [Using a custom nginx config for GKE](https://docs.cloud.google.com/endpoints/docs/openapi/custom-nginx) for more information.   
`-k SERVICE_ACCOUNT_KEY` | `--service_account_key SERVICE_ACCOUNT_KEY` | Sets the service account credentials JSON file. If provided, ESP uses the service account to generate an access token to call [Service Infrastructure APIs](https://docs.cloud.google.com/service-infrastructure/docs/overview). The only time you need to specify this option is when ESP is running on platforms other than Google Cloud, such as your local desktop, Kubernetes, or another cloud provider. See [ Creating a service account](https://docs.cloud.google.com/endpoints/docs/openapi/running-esp-localdev#create_service_account) for more information.   
`-z HEALTHZ_PATH` | `--healthz HEALTHZ_PATH` | Define a health checking endpoint on the same ports as the application backend. For example, `-z healthz` makes ESP return code `200` for location `/healthz`, instead of forwarding the request to the backend. Default: not used.   
none | `--dns DNS_RESOLVER` | Specify a dns resolver. For example, `--dns 169.254.169.254` uses the GCP Metadata server as the DNS resolver. If not specified, default is `8.8.8.8`.   
  
1 These ports are optional and must be distinct from each other. If you don't specify any port option, ESP accepts HTTP/1.x connections on port `8080`. For HTTPS connections, ESP expects the TLS secrets to be located at `/etc/nginx/ssl/nginx.crt` and `/etc/nginx/ssl/nginx.key`.

## Sample command-line invocations

The following examples show how to use some of the command-line arguments:

To start ESP to handle requests coming in at HTTP/1.x port `80` and HTTPS port `443` and send the requests to your API backend at `127.0.0.1:8000`:
    
    
    sudo docker run \
        --detach \
        DOCKER_ARGUMENTS \
        gcr.io/endpoints-release/endpoints-runtime:1
         --service=echo-api.endpoints.example-project-12345.cloud.goog \
            --rollout_strategy=managed \
            --http_port=80 \
            --ssl_port=443 \
            --backend=127.0.0.1:8000
    

To start ESP with a custom NGINX configuration by using the service account credentials file to fetch the service config and connect to the service control:
    
    
    sudo docker run \
        --detach \
        --volume=$HOME/Downloads:/esp \
        DOCKER_ARGUMENTS \
        gcr.io/endpoints-release/endpoints-runtime:1 \
        --service=echo-api.endpoints.example-project-12345.cloud.goog \
        --rollout_strategy=managed \
        --service_account_key=/esp/serviceaccount.json \
        --nginx_config=/esp/nginx.conf
        

Note that you must use the Docker flags `--volume` or `--mount` to mount the JSON file containing the private key for the service account and the custom NGINX config file as volumes inside ESP's Docker container. The preceding example maps the `$HOME/Downloads` directory on the local computer to the `esp` directory in the container. When you save the private key file for the service account, it is typically downloaded to the `Downloads` directory. You can copy the private key file to another directory if you want to. See [Manage data in Docker](https://docs.docker.com/storage/) for more information.

## Adding CORS support to ESP

Please refer to [Support CORS](https://docs.cloud.google.com/endpoints/docs/openapi/support-cors) for a description of available CORS support options. This section describes using ESP startup flags to support CORS.

To enable CORS support in ESP, include the `--cors_preset` option and set it to either `basic` or `cors_with_regex`. When you include `--cors_preset=basic` or `--cors_preset=cors_with_regex`, ESP:

  * Assumes all location paths have the same CORS policy.
  * Responds to both [simple requests](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS#simple_requests) and [preflight](https://developer.mozilla.org/docs/Web/HTTP/CORS#Preflighted_requests) `HTTP OPTIONS` requests.
  * Caches the result of the preflight `OPTIONS` request for up to 20 days (1728000 seconds).
  * Sets the response headers to the following values:
        
        Access-Control-Allow-Origin: *
        Access-Control-Allow-Methods: GET, POST, PUT, PATCH, DELETE, OPTIONS
        Access-Control-Allow-Headers: DNT,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Range,Authorization
        Access-Control-Expose-Headers: Content-Length,Content-Range




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
--cors_allow_origin_regex=^https?://.+\.example\.com$ ` The regular expression in the preceding example allows an origin with either `http` or `https` and any subdomain of `example.com`.  
  
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
`--cors_allow_credentials` | Includes the [`Access-Control-Allow-Credentials`](https://developer.mozilla.org/docs/Web/HTTP/Headers/Access-Control-Allow-Credentials) header with the value `true` in responses. By default, the `Access-Control-Allow-Credentials` header isn't included in responses.  
**Example:**  
` --cors_preset=basic  
--cors_allow_credentials `  
`--cors_expose_headers` | Sets [`Access-Control-Expose-Headers`](https://developer.mozilla.org/docs/Web/HTTP/Headers/Access-Control-Expose-Headers) to the specified headers. Specify which headers can be exposed as part of the response as a string with each header separated by a comma.  
**Example:**  
` --cors_preset=basic  
--cors_expose_headers=Content-Length `  
  
If the ESP CORS startup options don't suit the needs of your application, you can create a custom `nginx.conf` file with the CORS support that your application requires. For more information, see [Creating a custom `nginx.conf` to support CORS](https://docs.cloud.google.com/endpoints/docs/openapi/custom-cors-nginx).

## What's next

Learn about:

  * [Deploying ESP and your API backend to Google Cloud](https://docs.cloud.google.com/endpoints/docs/openapi/deploy-api-backend)
  * [Running ESP locally or on another platform](https://docs.cloud.google.com/endpoints/docs/openapi/running-esp-localdev)
  * The [`start_esp`](https://github.com/cloudendpoints/esp/tree/master/start_esp) script on GitHub



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
