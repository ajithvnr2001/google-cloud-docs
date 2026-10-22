---
url: https://docs.cloud.google.com/api-gateway/docs/model-routing-overview/
title: Overview of model routing \u00a0|\u00a0 API Gateway \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:18:50.932359+00:00
---

# Overview of model routing  |  API Gateway  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/api-gateway/docs/model-routing-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ API Gateway ](https://docs.cloud.google.com/api-gateway/docs)
  * [ Guides ](https://docs.cloud.google.com/api-gateway/docs/secure-traffic-gcloud)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Overview of model routing

Model routing for API Gateway is a managed traffic management layer that accepts OpenAI-compatible prompt requests, transcodes them in-flight, and routes them to specific Gemini Enterprise Agent Platform models. Model routing acts as a managed alternative to client-side proxies such as LiteLLM, providing centralized infrastructure to manage the lifecycle of AI agents.

Model routing moves routing logic to the network edge and integrates with Agent Platform Model Garden for same-host optimizations. This architecture removes the requirement to host, scale, and maintain unmanaged proxy servers, reducing operational overhead and infrastructure costs.

## Scope and user journeys

Model routing supports the following core user journeys:

  * **Model selection** : An AI developer uses [open models from Model as a Service (MaaS)](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/maas/use-open-models) in Agent Platform Model Garden. These are Gemini, Anthropic Claude, or OpenAI GPT family models.
  * **Specification authoring** : An AI developer creates or updates a model router configuration within an OpenAPI 3.x specification to reference the deployed models.
  * **Gateway deployment** : An AI developer deploys an API config and an API Gateway instance using the authored OpenAPI specification.
  * **Prompt routing** : Client applications send OpenAI-compatible prompt requests to the gateway, which routes requests and translates payloads based on the model name specified in the JSON payload.



Future versions of API Gateway are planned to support additional user journeys.

## Benefits of model routing

Implementing model routing in API Gateway provides the following advantages:

  * **Centralized management** : Consolidate AI traffic management within a single managed gateway, replacing fragmented client-side routing configurations.
  * **Reduced operational overhead** : Eliminate the infrastructure costs and maintenance burden associated with deploying standalone proxy servers.
  * **Edge-optimized performance** : Inspect prompts and route traffic at the network edge, leveraging direct integration with Agent Platform Model Garden endpoints.
  * **Standardized client interface** : Enable client applications to interact with a uniform OpenAI-compatible REST interface while dynamically dispatching requests to diverse underlying foundation models.



## Personas and use cases

Model routing addresses the requirements of the following personas:

  * **Platform Engineers** : Provision a managed infrastructure solution to replace client-side routing logic across enterprise AI deployments.
  * **AI Developers** : Expose a standardized API endpoint that dynamically routes requests between different foundation models (such as Gemini Pro, Gemini Flash, or Anthropic Claude) based on request payload parameters.
  * **Governance Admins** : Enforce centralized access policies (such as authentication and quotas) and monitor overall AI traffic volume across an organization.



### Supported use cases

During Public Preview, model routing supports routing based exclusively on the model tag or name (for example, `"model": "gemini-3.5-flash-lite"`) specified within the JSON payload of OpenAI-compatible client requests.

## Architecture and request flow

Model routing operates as a managed routing layer within the API Gateway data plane. When a client application sends an OpenAI-compatible prompt request to the gateway, the following sequence occurs:

  1. **Request interception** : The gateway intercepts the incoming `POST` request (for example, `POST /chat/completions`).
  2. **Payload inspection** : The model router inspects the `model` attribute within the incoming JSON payload (for example, `{"model": "claude-opus-4-7", "messages": [...]}`).
  3. **Rule evaluation** : The router matches the `model` string against the routing rules defined in your OpenAPI specification. If no rule matches, the router selects the configured default model.
  4. **In-flight transcoding** : The gateway transcodes the OpenAI-compatible request into the destination Agent Platform prediction schema.
  5. **Backend dispatch** : The gateway dispatches the transcoded request to the designated Agent Platform Model Garden endpoint and returns the model response to the client.



## Performance and limitations

Before implementing model routing, review the following technical constraints:

  * **Host constraints** : Model routing supports routing only to pre-deployed MaaS models hosted on Agent Platform Model Garden where all models referenced by a single router share the same hostname (for example, the global endpoint `aiplatform.googleapis.com` or a single regional endpoint such as `us-central1-aiplatform.googleapis.com`).
  * **Specification requirements** : Model routing requires an OpenAPI 3.x specification and the corresponding API Gateway OpenAPI 3.x extensions. OpenAPI 2.0 (Swagger) specifications aren't supported.
  * **Gateway updates** : You cannot update an existing gateway that was deployed without model routing to enable model routing, nor can you update a gateway deployed with model routing to disable or remove model routing. To switch routing modes, you must create and deploy a new API config and gateway instance.
  * **Mixed configurations** : An OpenAPI specification cannot contain a mix of model routing and non-model routing operations. All operations in the specification must either use model routing or use standard gateway routing.
  * **VPC Service Controls** : Model routing gateways do not support VPC Service Controls. You cannot use VPC Service Controls perimeters with API Gateway instances that enable model routing.
  * **Streaming and unsupported protocols** : Model routing supports response streaming (server-sent events), but doesn't support request-side streaming, gRPC, WebSockets, or Gemini Live.
  * **Supported modalities** : During Public Preview, model routing assumes text-based prompt requests formatted as OpenAI-compatible JSON payloads and routes based exclusively on the `model` tag or name in the payload.
  * **Required payload fields** : The incoming JSON request payload must include a `model` attribute. During Public Preview, if the `model` field is missing from the client request payload, the gateway incorrectly processes the request instead of rejecting it with an error. Always ensure client requests specify a `model` field in the JSON payload.
  * **Runtime limitations** : Standard gateway hosting infrastructure service limits and behaviors apply to your model routing endpoints: 
    * **Maximum timeout** : The gateway enforces a maximum request timeout of 3,600 seconds (1 hour), which applies to long-running streaming requests.
    * **Cold-start latency** : If your gateway instance scales to zero during periods of inactivity, the initial request might experience cold-start latency, which can impact latency-sensitive AI inference paths.
    * **Reserved URL paths** : You cannot use reserved URL paths starting with `/_ah/` or certain paths ending in `z` (to prevent conflicts, avoid using path names that end in `z`).
    * **URL character decoding** : The gateway automatically decodes certain encoded characters in request URLs before processing the request (for example, `%41` is decoded to `A`).



## What's next

  * [Configure model routing](https://docs.cloud.google.com/api-gateway/docs/model-routing-configure)
  * Learn about [OpenAPI 3.x extensions](https://docs.cloud.google.com/api-gateway/docs/oasv3-extensions)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
