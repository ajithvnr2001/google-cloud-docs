---
url: https://docs.cloud.google.com/api-gateway/docs/model-routing-configure/
title: Configure model routing \u00a0|\u00a0 API Gateway \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:18:49.783509+00:00
---

# Configure model routing  |  API Gateway  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/api-gateway/docs/model-routing-configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ API Gateway ](https://docs.cloud.google.com/api-gateway/docs)
  * [ Guides ](https://docs.cloud.google.com/api-gateway/docs/secure-traffic-gcloud)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure model routing

This page describes how to configure, deploy, and test model routing in API Gateway using OpenAPI 3.x specifications.

## Before you begin

Before configuring model routing, check that your environment meets the following prerequisites:

  1. **Check IAM permissions** : Check that you have access to the API Gateway Management Plane and Gemini Enterprise Agent Platform Model Garden. You must have the API Gateway Admin (`roles/apigateway.admin`) role to create API configs and gateways. In addition, the service account used by your gateway—either the default Compute Engine service account or a user-managed service account specified when creating the API config—must be granted the Agent Platform User (`roles/aiplatform.user`) role to access target models.
  2. **Check model availability and endpoint access** : Check that your routable models are pre-deployed [open models for Model as a Service (MaaS)](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/maas/use-open-models) in Agent Platform Model Garden. All models referenced by a single router must share the exact same hostname. Pick either the global endpoint (`aiplatform.googleapis.com`) or a single regional endpoint (for example, `us-central1-aiplatform.googleapis.com`) for every model referenced within that router.
  3. **Check gateway deployment eligibility** : You cannot update an existing gateway deployed without model routing to enable model routing, nor can you update a gateway deployed with model routing to disable or remove model routing. To switch routing modes, you must create and deploy a new API config and gateway instance.
  4. **Check VPC Service Controls and endpoint compatibility** : Model routing gateways do not support VPC Service Controls or Private Service Connect (PSC) endpoint configurations. Check that your target project and API Gateway instances are not restricted by VPC Service Controls perimeters, and that your models use public regional or global endpoints.



## Configuration validation

When you deploy an API config, the API Gateway management plane validates your OpenAPI specification. The management plane rejects invalid configurations during deployment with an informational validation error. The validation process enforces the following rules:

### Structural and location checks

  * The `x-google-api-management` extension and its associated blocks (`backends`, `ai.models.routing.routers`, individual routers, and `rules`) must be well-formed. Keys must match their expected data types (map, list, or string). The management plane rejects type mismatches with an `expected map/list/string` error.
  * The `x-google-api-management` extension must contain a valid `backends` block when model routing is enabled.
  * The `x-google-model-router` extension is supported only in OpenAPI 3.x specifications (it isn't supported in OpenAPI 2.0 / Swagger).
  * The `x-google-model-router` extension can only be specified at the operation level. The management plane explicitly rejects `x-google-model-router` definitions placed at the path level or root (top) level.
  * The `ai.models.routing.routers` block must be defined inside `x-google-api-management` whenever any operation references `x-google-model-router`.
  * You cannot specify both `x-google-model-router` and `x-google-backend` on the same API operation.
  * An OpenAPI specification cannot contain a mix of model routing and non-model routing operations. You cannot specify standard routing extensions (such as `x-google-backend`) on some operations while using `x-google-model-router` on other operations within the same API specification.



### HTTP method check

  * The `x-google-model-router` extension can only be applied to operations using the `POST` HTTP method. The management plane rejects model routing on any other HTTP method (such as `GET`, `PUT`, or `DELETE`).



### Backend validity

  * Every backend defined under `x-google-api-management.backends` must include a non-empty `address` field.
  * The backend `address` must be a valid URL using the `http` or `https` scheme. To protect prompt payloads and authentication credentials in transit across public or remote endpoints, always specify the `https` scheme when defining the `address` field.
  * Every backend defined under `x-google-api-management.backends` and referenced by a model router must use `pathTranslation: CONSTANT_ADDRESS`. The management plane rejects configurations using `pathTranslation: APPEND_PATH_TO_ADDRESS` for model routing backends because path translation is ignored in the model router's runtime path.
  * Model routing backends don't support VPC Service Controls or Private Service Connect (PSC) endpoint configurations. All backend `address` fields must point to public regional or global MaaS open model endpoints.

**Caution:** Because configuration validation doesn't enforce a domain allowlist, check that all backend `address` fields point only to trusted Agent Platform endpoints (for example, `aiplatform.googleapis.com`).

### Router reference resolution

  * The router name referenced by an operation's `x-google-model-router` must match a valid router key defined under `ai.models.routing.routers`.
  * The `backend` referenced by a router's `defaultModel` must match a valid backend defined under `x-google-api-management.backends`.
  * The `backend` referenced by each rule in a router must match a valid backend defined under `x-google-api-management.backends`.



### Router contents

  * Each router must define a `defaultModel`.
  * The `defaultModel` must include a valid `backend` field.
  * The `defaultModel` must include a non-empty `targetModel` field.
  * Each entry under `rules` must include a non-empty `model` field. The string value `default` is reserved and cannot be used as a rule's `model` value.
  * Each entry under `rules` must include a non-empty `targetModel` field.
  * The `model` values defined across all rules within a single router must be unique. The management plane rejects duplicate `model` values within the same router.



### Backend host and scheme consistency

  * All backends referenced by a single router (including `defaultModel.backend` and every rule's `backend`) must share the identical hostname and URL scheme. The management plane rejects configurations with differing hostnames or inconsistent schemes (`http` versus `https`) within the same router, ensuring the router dispatches all requests to a consistent upstream service endpoint.



### Target model validation

  * The `<provider>` portion of the `targetModel` string (`google`, `openai`, or `anthropic`) and the `<provider>/<model>` identifier format are both validated at config-create (deploy) time. The management plane rejects a `targetModel` that isn't formatted as `<provider>/<model>` or whose provider isn't `google`, `openai`, or `anthropic` with an `InvalidArgument: unsupported publisher` error during deployment.



## Step 1: Identify target models

Identify the target foundation models and their corresponding Agent Platform endpoint URLs. All routable models within a router must share a single hostname (for MaaS open models, this hostname is `aiplatform.googleapis.com`).

Endpoint URL paths vary based on the model provider:

  * **Google Gemini** : Uses the `:generateContent` method.
  * **Anthropic Claude** : Uses the `:rawPredict` method.
  * **OpenAI** : Uses the `/endpoints/openapi/chat/completions` endpoint path.



The following table lists the MaaS endpoints used in the OpenAPI specification example later in this section:

Model | Endpoint URL  
---|---  
`google/gemini-3.5-flash-lite` | `https://aiplatform.googleapis.com/v1/projects/YOUR_PROJECT_ID/locations/global/publishers/google/models/gemini-3.5-flash-lite:generateContent`  
`anthropic/claude-opus-4-7` | `https://aiplatform.googleapis.com/v1/projects/YOUR_PROJECT_ID/locations/global/publishers/anthropic/models/claude-opus-4-7:rawPredict`  
`openai/gpt-oss-120b-maas` | `https://aiplatform.googleapis.com/v1/projects/YOUR_PROJECT_ID/locations/global/endpoints/openapi/chat/completions`  
  
Replace `YOUR_PROJECT_ID` with your Google Cloud project ID.

## Step 2: Configure the OpenAPI 3.x specification

Create or update your OpenAPI 3.x specification to define your backend endpoints and model routing configurations.

The following example demonstrates an OpenAPI 3.0.3 specification defining two distinct model routers. To prevent horizontal scrolling, long backend address URLs use YAML double-quoted multi-line string continuation (``):
    
    
    openapi: 3.0.3
    
    info:
      title: OpenAPI 3.x spec using Model Routing
      description: Using Model Routing in an OAS 3.x spec
      version: 1.0.0
    
    x-google-api-management:
      backends:
        gemini-35-flashlite:
          address: "https://aiplatform.googleapis.com/v1/projects/\
            YOUR_PROJECT_ID/locations/global/publishers/google/\
            models/gemini-3.5-flash-lite:generateContent"
          deadline: 60.0
          pathTranslation: CONSTANT_ADDRESS
    
        anthropic-claude-opus-47:
          address: "https://aiplatform.googleapis.com/v1/projects/\
            YOUR_PROJECT_ID/locations/global/publishers/anthropic/\
            models/claude-opus-4-7:rawPredict"
          deadline: 60.0
          pathTranslation: CONSTANT_ADDRESS
    
        openai-gpt-oss-120b:
          address: "https://aiplatform.googleapis.com/v1/projects/\
            YOUR_PROJECT_ID/locations/global/endpoints/openapi/\
            chat/completions"
          deadline: 60.0
          pathTranslation: CONSTANT_ADDRESS
    
      ai:
        models:
          routing:
            routers:
              # Router 1: route between Gemini (default) and Claude.
              gemini-claude-router:
                defaultModel:
                  backend: gemini-35-flashlite
                  targetModel: google/gemini-3.5-flash-lite
                rules:
                  - model: "claude-opus-4-7"
                    backend: anthropic-claude-opus-47
                    targetModel: anthropic/claude-opus-4-7
    
              # Router 2: route between OpenAI GPT (default) and Gemini.
              openai-gemini-router:
                defaultModel:
                  backend: openai-gpt-oss-120b
                  targetModel: openai/gpt-oss-120b-maas
                rules:
                  - model: "gemini-3.5-flash-lite"
                    backend: gemini-35-flashlite
                    targetModel: google/gemini-3.5-flash-lite
    
    servers:
      - url: "https://my-gateway-url.com"
    
    paths:
      /v1/chat/gemini-claude:
        post:
          summary: "Endpoint:defaults to Gemini & Claude as an option."
          operationId: "chatGeminiClaude"
          x-google-model-router: gemini-claude-router
          responses:
            '200':
              description: "OK"
    
      /v1/chat/openai-gemini:
        post:
          summary: "Endpoint:defaults to OpenAI & Gemini as an option."
          operationId: "chatOpenAIGemini"
          x-google-model-router: openai-gemini-router
          responses:
            '200':
              description: "OK"
    

### Configuration properties

  1. **`backends`** : The `backends` object under `x-google-api-management` defines all routable model endpoints. Each backend name represents a symbolic model name (for example, `gemini-35-flashlite`) containing the destination `address`. The `backends` field is an existing Google OpenAPI extension.
  2. **`ai.models.routing`** : The model routing configuration resides under `x-google-api-management` as `ai.models.routing`, containing a map of named routers. Each map entry defines one model router, where the key represents the router's name (for example, `gemini-claude-router`) and the value contains: 
     * **`defaultModel`** : The required fallback model destination used when an incoming request payload doesn't match any explicit rule. It shares the exact structure of a rule entry but omits the `model` matching field. For OpenAI-compatible routes, when a request falls back to `defaultModel`, the value of `targetModel` is forwarded as the outgoing `model` attribute in the request body sent to Agent Platform.
     * **`rules`** : An optional array where each element maps a client-payload model string to a destination backend and target model.
  3. **Rule properties** : Each entry within `rules` (and the `defaultModel`) defines the following properties: 
     * **`model`** (_rules only_): The string value matched against the `model` attribute within the client's incoming JSON prompt payload. The router compares the incoming payload's `model` value to this string. If no rule matches, the router selects the `defaultModel`. For OpenAI-compatible routes (where the destination backend is `/openapi/chat/completions`), this string is forwarded directly as the outgoing `model` attribute in the request body sent to Agent Platform. Therefore, for OpenAI-compatible routes, the `model` selector must itself be a valid publisher model identifier (for example, `openai/gpt-oss-120b-maas`); using an alias such as `gpt-oss` results in a `400 Malformed publisher model` error from Agent Platform.
     * **`backend`** : The symbolic backend name defined under `x-google-api-management.backends` where the gateway sends the prompt.
     * **`targetModel`** : The target model identifier formatted as `<provider>/<model-id>`. The model router uses this string to translate requests and responses for the destination model. The `<provider>` prefix must be exactly `google`, `openai`, or `anthropic`. The `<model-id>` must be a valid Agent Platform Model Garden publisher model identifier. The gateway echoes this string back within the `model` field of the response returned to the client. Example values include: 
       * `google/gemini-3.5-flash-lite`
       * `google/gemini-2.5-pro`
       * `openai/gpt-oss-120b-maas`
       * `anthropic/claude-opus-4-7`
  4. **`x-google-model-router`** : To attach a model router to an API operation path, specify the router name using the `x-google-model-router` attribute. In the previous example, a `POST` request sent to `/v1/chat/gemini-claude` invokes `gemini-claude-router`, which routes the prompt based on the model name specified in the JSON payload.



## Step 3: Create and deploy the API config

Create an API config using your authored OpenAPI 3.x specification and deploy the config to your API Gateway instance as described in [Deploying an API to a gateway](https://docs.cloud.google.com/api-gateway/docs/deploying-api).

The API Gateway management plane processes your model routing configuration and activates the routing layer. When your gateway deployment completes, the gateway is ready to receive prompt requests formatted as OpenAI-compatible JSON payloads.

## Step 4: Test routing behavior

Before testing your gateway, wait for the gateway to reach the `ACTIVE` state, and then retrieve its URL:
    
    
    gcloud api-gateway gateways describe GATEWAY_ID \
      --location=GATEWAY_LOCATION \
      --project=PROJECT_ID \
      --format='value(defaultHostname)'
    

At the start of the Model Routing Public Preview, model routing gateways used a `run.app` hostname. Starting September 3, 2026, new model routing gateways might instead use a `gateway.dev` default hostname of the form `https://GATEWAY_ID-PROJECT_NUMBER.REGION.gateway.dev`, for example `https://my-gateway-123456789012.us-central1.gateway.dev`. The default hostname is immutable and assigned at creation. Whichever format is assigned—whether a `run.app` hostname or a `gateway.dev` hostname—the gateway retains that format permanently.

Test your gateway's routing behavior using `curl` to send OpenAI-compatible prompt requests to your gateway URL (`https://GATEWAY_URL`). In the following examples, `$TOKEN` represents a valid authentication token obtained using any of the methods described in [Choosing an Authentication Method](https://docs.cloud.google.com/api-gateway/docs/authentication-method).

### Test explicit rule routing

Send a prompt requesting the Claude model `anthropic/claude-opus-4-7`:
    
    
    curl https://GATEWAY_URL/v1/chat/gemini-claude \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $TOKEN" \
      -d '{
        "model": "claude-opus-4-7",
        "messages": [
          {
            "role": "system",
            "content": "You are a helpful assistant."
          },
          {
            "role": "user",
            "content": "Explain the concept of recursion in one sentence."
          }
        ]
      }'
    

Sending the request to `/v1/chat/gemini-claude` invokes `gemini-claude-router`. The attribute `"model": "claude-opus-4-7"` within the JSON payload matches the explicit rule in `gemini-claude-router`, directing the gateway to route the request to the `anthropic-claude-opus-47` backend.

### Test default model fallback

Send a prompt specifying an unmatched model name to test fallback routing:
    
    
    curl https://GATEWAY_URL/v1/chat/gemini-claude \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $TOKEN" \
      -d '{
        "model": "unrecognized-model",
        "messages": [
          {
            "role": "user",
            "content": "Write a short poem about the ocean."
          }
        ],
        "stream": true
      }'
    

Sending the request to `/v1/chat/gemini-claude` invokes `gemini-claude-router`. Because the attribute `"model": "unrecognized-model"` doesn't match any explicit rule, the gateway dispatches the request to the router's configured `defaultModel`—the `gemini-35-flashlite` backend.

### Test alternative router path

Send a prompt requesting Gemini through the secondary router endpoint:
    
    
    curl https://GATEWAY_URL/v1/chat/openai-gemini \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $TOKEN" \
      -d '{
        "model": "gemini-3.5-flash-lite",
        "messages": [
          {
            "role": "user",
            "content": "List the three largest cities in the world."
          }
        ]
      }'
    

Sending the request to `/v1/chat/openai-gemini` invokes `openai-gemini-router`. The attribute `"model": "gemini-3.5-flash-lite"` matches the explicit rule in that router, directing the gateway to route the request to the `gemini-35-flashlite` backend. A single backend can be referenced by multiple routers; in this configuration, `gemini-35-flashlite` serves as an explicit rule target in `openai-gemini-router` and as the fallback `defaultModel` in `gemini-claude-router`.

## Observability

The model router is instrumented so you can verify your gateway is serving traffic, inspect per-request metadata using [Cloud Logging](https://docs.cloud.google.com/logging/docs/overview), and diagnose failures using [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/overview).

### Cloud Logging

Every request routed through the gateway generates an entry in the standard API Gateway request log located in your Google Cloud project at:

`projects/YOUR_PROJECT_ID/logs/apigateway.googleapis.com%2Frequests`

Each log entry includes the following fields:

  * `httpRequest.requestUrl`, `httpRequest.status`, `httpRequest.latency`
  * `api`, `apiConfig`, `apiMethod`
  * `backendRequest.hostname`: The hostname of the Agent Platform backend to which the request was proxied.
  * `responseDetails`: Populated with a branded error category on model router failures (see Troubleshooting model router failures).



To find recent requests sent to a specific gateway, use the following Cloud Logging query filter:
    
    
    (resource.type="apigateway.googleapis.com/Gateway" OR resource.type="api")
    logName="projects/YOUR_PROJECT_ID/logs/apigateway.googleapis.com%2Frequests"
    

**Note:** Per-request attribution of the specific target model that handled a given request isn't available during Public Preview. Because all backends referenced by a single router share an identical hostname (such as `aiplatform.googleapis.com`), the `backendRequest.hostname` field alone doesn't identify the selected model. As a workaround, you can deploy a router with a single rule per test endpoint so the target is unambiguous from the router configuration itself, or you can inspect the response body since Gemini, Claude, and OpenAI model responses have distinguishable payload shapes and model-specific fields. Structured per-request routing decision logs will be added in a future release.

### Cloud Monitoring

The standard API Gateway metric `apigateway.googleapis.com/proxy/request_count` (BETA) reports gateway traffic volume broken down by:

  * `response_code_class`: One of `2xx`, `3xx`, `4xx`, or `5xx`.
  * `api_config`: The API config name the gateway is using.



This metric lets you verify overall traffic volume and error rates. Model-router-specific metrics (such as per-router or per-target-model breakdowns) will be added in a future release.

To track aggregated request latency, you can create a [log-based metric](https://docs.cloud.google.com/logging/docs/logs-based-metrics) from the `httpRequest.latency` field in the request log.

### Troubleshooting model router failures

When a request routed through the model router fails, the `responseDetails` field on the corresponding request log entry indicates whether the failure occurred within the model router layer. The model router surfaces four branded categories:

`responseDetails` value | Meaning | Typical fix  
---|---|---  
`model_router_application_error` | The request couldn't be routed. This usually indicates a missing rule, a payload containing a `model` value that doesn't match any rule (without a configured `defaultModel`), or a malformed request payload. | **Customer side** : Verify that your payload's `model` parameter matches one of the `rule.model` strings in your router configuration or that a `defaultModel` fallback is defined. Check that the request body is valid OpenAI-compatible JSON and explicitly includes a `model` attribute (during Public Preview, a missing `model` attribute in the request payload is incorrectly processed instead of being rejected).  
`model_router_timeout` | The model router exceeded the per-request timeout. The request might be unusually large or complex, or there might be a capacity bottleneck. | Check request complexity and timeout settings across backends. If the issue persists across normal payloads, contact [Google Cloud Support](https://docs.cloud.google.com/support) with the request timestamp and a log sample.  
`model_router_upstream_error` | The upstream target model returned an HTTP error to the gateway. | **Upstream service side** : Check the status code and payload from the target Agent Platform service endpoint. If this is unexpected for valid requests, open a support case.  
`model_router_unavailable` | The model router was unreachable from the gateway due to a transport or connectivity failure. | **Platform side** : Open a support case with [Google Cloud Support](https://docs.cloud.google.com/support).  
  
## What's next

  * Review [model routing architecture and concepts](https://docs.cloud.google.com/api-gateway/docs/model-routing-overview)
  * Explore [OpenAPI 3.x extensions](https://docs.cloud.google.com/api-gateway/docs/oasv3-extensions)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
