---
url: https://docs.cloud.google.com/api-gateway/docs/streaming-configure/
title: Configure streaming for LLM responses and other traffic \u00a0|\u00a0 API Gateway \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:09:44.281267+00:00
---

# Configure streaming for LLM responses and other traffic  |  API Gateway  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/api-gateway/docs/streaming-configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ API Gateway ](https://docs.cloud.google.com/api-gateway/docs)
  * [ Guides ](https://docs.cloud.google.com/api-gateway/docs/secure-traffic-gcloud)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure streaming for LLM responses and other traffic

**Preview — streaming**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how to configure streaming in API Gateway.

API Gateway supports streaming. Streaming allows gateways to serve long-running connections and transmit data in chunks for both request and response streaming.

A common use of streaming is serving a large language model (LLM). The model sends its answer one token at a time, so a client can show the text while the model is still generating it. For a complete example that streams responses from a Gemma model that [vLLM](https://docs.vllm.ai/) serves on Cloud Run, see Stream responses from an LLM.

## Supported streaming protocols

When enabled, API Gateway supports the following streaming methods:

  * **Incremental response delivery** : HTTP/2 DATA frames or HTTP/1.1 chunked transfer encoding, depending on what the client negotiates.
  * **Server-Sent Events (SSE)** : Unidirectional streaming from the server to the client.
  * **WebSockets** : Full-duplex communication channels over a single TCP connection.
  * **gRPC bidirectional streaming** : Full-duplex streaming using gRPC.



## Prerequisites

Before you can use streaming, ensure your backend service supports the required protocol (for example, HTTP/2 or WebSockets) and that your API configuration is set up correctly.

### Configure backend protocol

To support streaming traffic, you must configure the protocol for your backend based on the type of streaming:

  * **gRPC** : You must configure your backend to use HTTP/2 (`h2`).
  * **WebSockets** : You must use `http/1.1`. WebSockets require the HTTP/1.1 `Connection: Upgrade` handshake.
  * **Server-Sent Events (SSE) and incremental response delivery** : Your backend can use either HTTP/1.1 or HTTP/2 (`h2`). We recommend HTTP/2 (`h2`) for improved performance.



In your OpenAPI specification, configure the backend protocol as follows:

#### Example (OpenAPI 3.x)

Set the `protocol` field in the named backend definition within the `x-google-api-management.backends` object. You must also reference this backend using `x-google-backend` at the root or operation level.
    
    
    x-google-api-management:
      backends:
        gemma:
          address: https://my-gemma-service.run.app
          protocol: h2 # Use 'http/1.1' for WebSockets
    x-google-backend: gemma
    

#### Example (OpenAPI 2.0)

Set the `protocol` field in the `x-google-backend` extension.
    
    
    x-google-backend:
      address: https://my-gemma-service.run.app
      protocol: h2 # Use 'http/1.1' for WebSockets
    

### Set the stream deadline

The `deadline` field governs how long a request (unary or streaming) may run.

The following table shows how the timeouts apply to each kind of request:

Method | Idle timeout  
(maximum gap between messages) | Request timeout  
(maximum total request duration)  
---|---|---  
Non-streaming | N/A: the idle timeout only applies to streams | Default 15 seconds; set `deadline` to change it, up to 3,600 seconds for streaming-enabled gateways  
Streaming over HTTP  
(SSE, chunked transfer) | N/A: effectively infinite; only the request timeout ends the stream | Default 15 seconds; set `deadline` to change it, up to 3,600 seconds for streaming-enabled gateways  
Streaming over gRPC or WebSockets | Default 300 seconds; set `deadline` to change it, up to 3,600 seconds for streaming-enabled gateways. On WebSockets, a `deadline` of less than 300 seconds is ignored and a 300-second minimum applies | Always 3,600 seconds for streaming-enabled gateways, not configurable  
**Caution:** Outside gRPC streaming and WebSockets, the default is only 15 seconds, which is too short for most streams. A stream is cut once the request timeout elapses, even while it is still sending data, so set `deadline` explicitly on every streaming endpoint.**Note:** Your backend enforces its own request timeout, and that timeout ends the connection however much traffic it is carrying. `deadline` does not change it. A Cloud Run backend left on its 300-second default closes a stream five minutes after it opens. The Gemma guide deploys its service with `--timeout 600`, so its streams end after 10 minutes. To use the 3,600-second `deadline` in the two examples that follow, deploy the service with `--timeout 3600`. For more information, see [Configure request timeout for services](https://docs.cloud.google.com/run/docs/configuring/request-timeout).

#### Example (OpenAPI 3.x)

Set the `deadline` field in the named backend definition.
    
    
    x-google-api-management:
      backends:
        gemma:
          address: https://my-gemma-service.run.app
          protocol: h2
          deadline: 3600.0
    x-google-backend: gemma
    

#### Example (OpenAPI 2.0)

Set the `deadline` field in the `x-google-backend` extension.
    
    
    x-google-backend:
      address: https://my-gemma-service.run.app
      protocol: h2
      deadline: 3600.0
    

For the other limits that apply to streaming connections, see Limitations.

## Enable streaming on a gateway

Streaming is specified at gateway creation time. Note the following behavior:

  * **No explicit disable** : There is no flag to explicitly disable streaming. If you omit the `--enable-streaming` flag, API Gateway resolves the mode at creation from the API config and the platform default: an API config that configures a Model Router always produces a streaming gateway. Read the gateway's output-only `effectiveStreamingMode` field to see the mode it was created with.
  * **Immutability** : The streaming mode is fixed at creation and cannot be modified later.



To specify streaming on a gateway, use the `--enable-streaming` flag with the `gcloud api-gateway gateways create` command:
    
    
    gcloud api-gateway gateways create GATEWAY_ID \
        --api=API_ID \
        --api-config=CONFIG_ID \
        --location=GCP_REGION \
        --enable-streaming

For more information on gateway deployment options, see [Deploy an API to a gateway](https://docs.cloud.google.com/api-gateway/docs/deploying-api).

**Note:** Model Router Gateways automatically enable streaming.

### Gateway streaming properties

The following fields on the Gateway resource control streaming behavior:

Field | Attributes | Values  
---|---|---  
`streamingMode` | String (IMMUTABLE, OPTIONAL) | 

  * `STREAMING_MODE_UNSPECIFIED` (Default: Service selects mode)
  * `STREAMING_MODE_ENABLED`

  
`effectiveStreamingMode` | String (OUTPUT_ONLY) | 

  * `EFFECTIVE_STREAMING_MODE_DISABLED`
  * `EFFECTIVE_STREAMING_MODE_ENABLED`

  
  
When using the REST API to create a gateway, you can specify streaming in the request body:
    
    
    {
      "apiConfig": "projects/...",
      "streamingMode": "STREAMING_MODE_ENABLED"
    }
    

### Verify streaming is enabled

To confirm if streaming is active on your gateway, describe the gateway using the gcloud CLI:
    
    
    gcloud api-gateway gateways describe GATEWAY_ID \
        --location=GCP_REGION

Look for the `effectiveStreamingMode` field in the output. If streaming is enabled, the output includes:
    
    
    effectiveStreamingMode: EFFECTIVE_STREAMING_MODE_ENABLED
    

## Stream responses from an LLM

This example puts a streaming gateway in front of a Gemma model that vLLM serves on Cloud Run, and streams a chat completion through the gateway. vLLM serves an OpenAI-compatible API that streams responses as Server-Sent Events (SSE).

Before you begin, complete [Configure the development environment](https://docs.cloud.google.com/api-gateway/docs/configure-dev-env), including [Configure the service account used to create API configs](https://docs.cloud.google.com/api-gateway/docs/configure-dev-env#configure-service-account). The gateway uses that service account to call the Cloud Run service.

### Deploy the model

Deploy a Gemma model by following [Deploy a Gemma 4 model with a vLLM container](https://docs.cloud.google.com/run/docs/run-gemma-on-cloud-run#deploy-prebuilt-container). Note the service name, the service URL, the region, and the name of the model that you deploy, such as `google/gemma-4-E4B-it`.

**Note:** The guide's deploy command downloads the model weights from Hugging Face without authentication. If Hugging Face rate-limits the download, the service logs show `HTTP Error 429`, the container fails its startup probe, and the revision doesn't become ready. To avoid this, set a Hugging Face access token in the `HF_TOKEN` environment variable, as shown in the guide's table of deployment settings.

### Grant the gateway access to the service

The guide deploys the service with `--no-allow-unauthenticated`. The gateway calls the service with an ID token for its service account, which you pass as `--backend-auth-service-account` when you create the API config. Grant that service account the Cloud Run Invoker role (`roles/run.invoker`) on the service:
    
    
    gcloud run services add-iam-policy-binding SERVICE_NAME \
        --region=REGION \
        --member=serviceAccount:SERVICE_ACCOUNT_EMAIL \
        --role=roles/run.invoker

Replace the following:

  * `SERVICE_NAME`: the name of the Cloud Run service
  * `REGION`: the region where you deployed the service
  * `SERVICE_ACCOUNT_EMAIL`: the email address of the gateway's service account



### Create the API config

Save the following OpenAPI specification as `gemma-api.yaml`, replacing `https://my-gemma-service.run.app` with your service URL:
    
    
    openapi: 3.0.3
    info:
      title: Gemma API
      version: 1.0.0
    x-google-api-management:
      backends:
        gemma:
          address: https://my-gemma-service.run.app
          protocol: h2
          deadline: 570.0
    x-google-backend: gemma
    components:
      securitySchemes:
        google_id_token:
          type: oauth2
          flows:
            implicit:
              authorizationUrl: ""
              scopes: {}
          x-google-auth:
            issuer: https://accounts.google.com
            jwksUri: https://www.googleapis.com/oauth2/v3/certs
            audiences:
              - gemma-api
    security:
      - google_id_token: []
    paths:
      /v1/chat/completions:
        post:
          operationId: createChatCompletion
          responses:
            '200':
              description: A chat completion, streamed as SSE when the request sets "stream" to true.
    

The `deadline` of 570 seconds is 30 seconds shorter than the `--timeout 600` that the Gemma guide sets on the service. As a result, the gateway's `deadline`, not the service timeout, ends a stream that runs too long. A top-level `x-google-backend` defaults to `pathTranslation: APPEND_PATH_TO_ADDRESS`. The gateway appends the request path to the backend address, so a request to `/v1/chat/completions` reaches the vLLM chat completions endpoint.

The `security` requirement makes the gateway reject any request that doesn't carry a Google-signed ID token with the audience `gemma-api`. You can choose a different audience string, as long as callers request the same one when they mint a token. For more information, see [Using Google ID tokens to authenticate users](https://docs.cloud.google.com/api-gateway/docs/authenticating-users-googleid).

**Caution:** An ID token identifies the caller but doesn't limit which Google identity that is. Any identity that can mint a token for the `gemma-api` audience can send requests to your model. You pay for the GPU instances that their requests start. To also require an API key, see [Use API keys](https://docs.cloud.google.com/api-gateway/docs/authenticate-api-keys). To limit how many requests each consumer project can send per minute, see [About quotas](https://docs.cloud.google.com/api-gateway/docs/quotas-overview).

Create the API config:
    
    
    gcloud api-gateway api-configs create CONFIG_ID \
        --api=API_ID \
        --openapi-spec=gemma-api.yaml \
        --backend-auth-service-account=SERVICE_ACCOUNT_EMAIL

Replace the following:

  * `CONFIG_ID`: an ID for the API config
  * `API_ID`: the ID of the API. If the API doesn't exist, the command creates it.



### Create the gateway

Create a streaming gateway from the API config:
    
    
    gcloud api-gateway gateways create GATEWAY_ID \
        --api=API_ID \
        --api-config=CONFIG_ID \
        --location=GCP_REGION \
        --enable-streaming

Replace the following:

  * `GATEWAY_ID`: an ID for the gateway
  * `GCP_REGION`: the region for the gateway, which can differ from `REGION`. For allowed values, see [Deploy an API to a gateway](https://docs.cloud.google.com/api-gateway/docs/deploying-api).



When the gateway is ready, get its hostname:
    
    
    gcloud api-gateway gateways describe GATEWAY_ID \
        --location=GCP_REGION \
        --format="value(defaultHostname)"

### Get an ID token for the caller

A user account can't choose the audience of its ID token, so the example mints the token for a service account that you impersonate. For the caller, use an existing service account or create one. For more information, see [Create service accounts](https://docs.cloud.google.com/iam/docs/service-accounts-create). Grant yourself the Service Account Token Creator role (`roles/iam.serviceAccountTokenCreator`) on that service account, which the gcloud CLI needs to impersonate it:
    
    
    gcloud iam service-accounts add-iam-policy-binding CALLER_SERVICE_ACCOUNT_EMAIL \
        --member=user:USER_EMAIL \
        --role=roles/iam.serviceAccountTokenCreator

Replace the following:

  * `CALLER_SERVICE_ACCOUNT_EMAIL`: the email address of the service account that calls the gateway
  * `USER_EMAIL`: your email address



### Send a streaming request

Send a chat completion request that sets `"stream": true`, with an ID token for the caller's service account in the `Authorization` header. The `-N` flag turns off output buffering in `curl`, so each event prints when it arrives:
    
    
    curl -N https://DEFAULT_HOSTNAME/v1/chat/completions \
        -H "Authorization: Bearer $(gcloud auth print-identity-token \
            --impersonate-service-account=CALLER_SERVICE_ACCOUNT_EMAIL \
            --audiences=gemma-api)" \
        -H "Content-Type: application/json" \
        -d '{
          "model": "MODEL_NAME",
          "messages": [{"role": "user", "content": "Why is the sky blue?"}],
          "stream": true
        }'

Replace the following:

  * `DEFAULT_HOSTNAME`: the hostname of the gateway
  * `CALLER_SERVICE_ACCOUNT_EMAIL`: the service account from the previous step
  * `MODEL_NAME`: the model that you deployed, such as `google/gemma-4-E4B-it`

**Note:** The Gemma guide doesn't set minimum instances, so Cloud Run removes the service's instances when they're idle. A request that arrives when no instance is running waits while a new instance starts and loads the model. This can take several minutes, and the wait counts toward the gateway's `deadline`. To keep an instance running, see [Set minimum instances for services](https://docs.cloud.google.com/run/docs/configuring/min-instances). Instances kept running this way are billed.

The response is an SSE stream. The first event carries the `assistant` role, each later event carries the next part of the answer, and the last event before `data: [DONE]` sets `finish_reason`. The output is similar to the following:
    
    
    data: {"id":"chatcmpl-7bcd57ad-1c3c-4779-91be-2973b875e517","object":"chat.completion.chunk","created":1790099706,"model":"google/gemma-4-E4B-it","choices":[{"index":0,"delta":{"role":"assistant","content":""},"logprobs":null,"finish_reason":null}],"prompt_token_ids":null}
    
    data: {"id":"chatcmpl-7bcd57ad-1c3c-4779-91be-2973b875e517","object":"chat.completion.chunk","created":1790099706,"model":"google/gemma-4-E4B-it","choices":[{"index":0,"delta":{"content":"The"},"logprobs":null,"finish_reason":null,"token_ids":null}]}
    
    ...
    
    data: {"id":"chatcmpl-7bcd57ad-1c3c-4779-91be-2973b875e517","object":"chat.completion.chunk","created":1790099706,"model":"google/gemma-4-E4B-it","choices":[{"index":0,"delta":{"content":""},"logprobs":null,"finish_reason":"stop","stop_reason":106,"token_ids":null}]}
    
    data: [DONE]
    

### Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this example, delete the gateway and the API config:
    
    
    gcloud api-gateway gateways delete GATEWAY_ID \
        --location=GCP_REGION
    
    
    gcloud api-gateway api-configs delete CONFIG_ID \
        --api=API_ID

If you created the API for this example, delete it:
    
    
    gcloud api-gateway apis delete API_ID

Delete the Cloud Run service:
    
    
    gcloud run services delete SERVICE_NAME \
        --region=REGION

## Pricing

During the Public Preview of streaming, customers are not charged for network egress on streaming-enabled gateways. However, Service Control billing still applies at the API level regardless of the release phase.

## Limitations

The following limitations apply to streaming in API Gateway during the Public Preview:

  * **Immutability** : You cannot update an existing gateway to enable or disable streaming. You must create a new gateway. Note that a streaming-enabled gateway receives a different hostname _shape_ , requiring you to update your clients or DNS records. If you would like us to update your gateway record to use the new format, [contact support](https://cloud.google.com/support-hub). API Gateway uses the following hostname patterns:

    * **Non-streaming** : `{gateway_id}-{base36_project_number}.{shard_hash}.gateway.dev`, for example `test-gateway-4jcaz8x.uc.gateway.dev`
    * **Streaming** : `{gateway_id}-{project_number}.{region}.gateway.dev`, for example `test-gateway-9876654321.us-central1.gateway.dev`
    * **Streaming (legacy)** : `{service}-{tenant_project_number}.{region}.run.app`, for example `test-gateway-834512064953.us-central1.run.app`. Gateways created before regional `*.gateway.dev` hostnames were available keep this hostname permanently and are not migrated to the new pattern.

A new streaming-enabled gateway receives the **Streaming** pattern. The first two examples are the same gateway in the same project: in the **Streaming** pattern the project number appears in decimal rather than base36, so the first label has less room than on a non-streaming gateway. The first label is the combined `{gateway_id}-{project_number}` string, which must fit the 63-character DNS label limit. The [49-character gateway ID limit](https://docs.cloud.google.com/api-gateway/docs/deploying-api#gateway_id_requirements) keeps it within that limit for project numbers of up to 13 digits; a longer project number needs a shorter gateway ID.

  * **Terraform** : Enabling streaming using Terraform is not supported (planned for a future release).

  * **Load Balancing and Custom Domains** : Gateways with an `effectiveStreamingMode` of `EFFECTIVE_STREAMING_MODE_ENABLED` are not compatible with HTTP(S) Load Balancing for API Gateway or Serverless NEGs. You cannot place such a gateway behind a Serverless NEG or external Application Load Balancer. Consequently, custom domains (which rely on load balancing) are not supported for these gateways during Public Preview.

  * **Deadline behavior** : Enabling streaming on a gateway does not change how the `deadline` field behaves on an SSE or chunked-transfer path. The deadline remains a wall-clock bound on the complete response, so a stream is cut once the deadline elapses regardless of how much data it is sending. The default is 15 seconds and the maximum is 3,600 seconds. On a WebSocket, `deadline` bounds the gap between messages instead, and the connection terminates after 3,600 seconds. See Set the stream deadline.

  * **Model Context Protocol (MCP)** : Creating the gateway with `--enable-streaming` does not make an MCP endpoint stream. MCP responses remain a single `application/json` body regardless of the gateway's streaming mode. For more details, see [MCP Limitations](https://docs.cloud.google.com/api-gateway/docs/openapi-v3-limitations#mcp-limitations).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
