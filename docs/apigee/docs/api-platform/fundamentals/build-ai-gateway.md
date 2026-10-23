---
url: https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/build-ai-gateway/
title: Build an AI gateway with routing, Model Armor, and semantic cache \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:14:20.959822+00:00
---

# Build an AI gateway with routing, Model Armor, and semantic cache  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/build-ai-gateway/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Build an AI gateway with routing, Model Armor, and semantic cache Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This tutorial shows you how to configure and use Apigee as an AI gateway that routes large language model (LLM) requests to different backend models based on flexible, policy-driven routing rules. An AI gateway helps you secure, govern, and optimize your model traffic to manage costs and prevent model sprawl.

Each stage of the tutorial builds on the previous configuration by adding a specific capability through reusable Apigee Feature Template (AFT) files:

  * **Stage 1** : Deploy a minimal API proxy that fronts a single LLM provider.
  * **Stage 2** : Add Model Armor prompt and response sanitization to filter malicious inputs and prevent sensitive data leakage.
  * **Stage 3** : Add cross-provider model routing and a semantic cache backed by Agent Platform Vector Search.
  * **Stage 4** : Configure cross-provider fallback to automatically retry requests against a secondary provider if the primary target returns a `4xx` or `5xx` HTTP status code.



To add a capability, you append a single line to the `features` block in your template. To view or download the complete set of example files, including the AFT files and helper scripts, see the [Apigee Template Repository on GitHub](https://github.com/gcp-samples/apigee-template-repository/tree/main/examples/ai-gateway-progressive).

## Before you begin

Before you complete this tutorial, ensure that you have the following:

  * An active Google Cloud project with billing enabled.
  * A **Comprehensive** environment available in your Apigee instance. You can deploy Model Armor, `SemanticCacheLookup`, and `SemanticCachePopulate` policies only in Comprehensive environments.
  * The Google Cloud CLI (`gcloud`) installed and configured with Application Default Credentials (ADC). To generate credentials, run `gcloud auth application-default login`.
  * A runtime service account with the following IAM roles: 
    * `roles/aiplatform.user`
    * `roles/modelarmor.user`
The service account also needs access to any provider-specific credentials. 
  * For stages 2, 3, and 4, specify a Model Armor template resource path. For example, `projects/YOUR_PROJECT/locations/us-central1/templates/apigee-aft-demo-ma`.
  * For stages 3 and 4: An [Apigee key-value map (KVM)](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps) named `openai-credentials` in your environment that contains an `api-key` entry with a valid OpenAI API key.
  * For stages 3 and 4: A deployed Vertex AI Vector Search index endpoint for the semantic cache. For step-by-step index setup, see the [Apigee Template Repository README on GitHub](https://github.com/gcp-samples/apigee-template-repository/tree/main/examples/ai-gateway-progressive).



## Overview

All four stages accept the OpenAI Chat Completions request shape at `/v1/chat/completions[-stageN]`, so the same client SDKs work across every stage. The `model` field prefix drives the routing decision: requests for `google/*` models route to Gemini on Agent Platform, and all other requests route to OpenAI. This inverted default ensures that new OpenAI model families, such as `o1-*`, `o3-*`, and `chatgpt-*`, are routed correctly instead of silently missing a `gpt-*` prefix match.

Stage | Capability added | Base path  
---|---|---  
1 | Hello LLM (OpenAI-format request to Gemini on Agent Platform) | `/v1/chat/completions`  
2 | Model Armor (prompt injection, responsible AI, and Sensitive Data Protection filters) | `/v1/chat/completions-stage2`  
3 | Cross-provider routing and a Agent Platform Vector Search semantic cache | `/v1/chat/completions-stage3`  
4 | Cross-provider fallback (the complete AI gateway) | `/v1/chat/completions-stage4`  
  
## Stage 1: Hello LLM

The minimal proxy fronts a single Gemini target through its OpenAI-compatible endpoint. Two small feature files provide the base proxy skeleton and a JSON extractor. The extractor copies `$.model` and `$.messages[-1].content` into the `llm.model` and `llm.prompt` flow variables so that later stages have consistent inputs.

`llm-base.yaml` defines the base proxy skeleton:
    
    
    gateway: apigee
    schemaVersion: 1.0.0
    name: llm-base
    type: feature
    parameters:
      - name: BASE_PATH
        default: /v1/chat/completions
    endpoints:
      - name: default
        basePath: "{BASE_PATH}"
        routes:
          - name: primary
            target: gemini-target

`llm-openai-format.yaml` extracts the OpenAI-shaped request fields:
    
    
    gateway: apigee
    schemaVersion: 1.0.0
    name: llm-openai-format
    type: feature
    defaultEndpoint:
      name: default
      flows:
        - name: PreFlow
          mode: Request
          steps:
            - name: EV-ExtractOpenAIRequest
    policies:
      - name: EV-ExtractOpenAIRequest
        type: ExtractVariables
        content:
          ExtractVariables:
            metadata:
              name: EV-ExtractOpenAIRequest
              continueOnError: "true"
            Source:
              _text: request
            JSONPayload:
              Variable:
                - metadata:
                    name: model
                  JSONPath:
                    _text: "$.model"
                - metadata:
                    name: prompt
                  JSONPath:
                    _text: "$.messages[-1].content"
            VariablePrefix:
              _text: llm

`target-vertex-gemini.yaml` defines a Agent Platform target that uses the OpenAI-compatible endpoint:
    
    
    gateway: apigee
    schemaVersion: 1.0.0
    name: target-vertex-gemini
    type: feature
    targets:
      - name: gemini-target
        httpTargetConnection:
          URL: https://aiplatform.googleapis.com/v1/projects/{organization.name}/locations/global/endpoints/openapi/chat/completions
          Authentication:
            GoogleAccessToken:
              Scopes:
                Scope: https://www.googleapis.com/auth/cloud-platform

Compose the feature files into the Stage 1 template, `01-hello-llm.yaml`:
    
    
    gateway: apigee
    schemaVersion: 1.0.0
    name: aft-demo-01-hello-llm
    features:
      - llm-base.yaml
      - llm-openai-format.yaml
      - target-vertex-gemini.yaml

Deploy the template:
    
    
    gcloud beta apigee apis import aft-demo-01-hello-llm \
      --from-template=01-hello-llm.yaml \
      --organization=APIGEE_ORG

Test the proxy:
    
    
    curl -X POST https://APIGEE_HOSTNAME/v1/chat/completions \
      -H "Content-Type: application/json" \
      -d '{"model":"google/gemini-2.5-flash",
           "messages":[{"role":"user","content":"Explain how AI works in a few words"}]}'

Replace the following:

  * `APIGEE_ORG`: your Apigee organization name.
  * `APIGEE_HOSTNAME`: the hostname of your Apigee environment group, typically a Google Cloud load balancer.



## Stage 2: Add Model Armor

[Model Armor](https://docs.cloud.google.com/apigee/docs/api-platform/tutorials/using-model-armor-policies) inspects the incoming prompt for prompt injection, disallowed content, and sensitive data before the target call. It then scans the model response before the response reaches the client.

Add one feature file to the template, `llm-model-armor.yaml`:
    
    
    gateway: apigee
    schemaVersion: 1.0.0
    name: llm-model-armor
    type: feature
    parameters:
      - name: MA_TEMPLATE_PATH
        default: projects/{organization.name}/locations/us-central1/templates/apigee-aft-demo-ma
    defaultEndpoint:
      name: default
      flows:
        - name: PreFlow
          mode: Request
          steps:
            - name: MA-SanitizeUserPrompt
        - name: PostFlow
          mode: Response
          steps:
            - name: MA-SanitizeModelResponse
    policies:
      - name: MA-SanitizeUserPrompt
        type: SanitizeUserPrompt
        content:
          SanitizeUserPrompt:
            metadata:
              name: MA-SanitizeUserPrompt
            ModelArmor:
              TemplateName:
                _text: "{MA_TEMPLATE_PATH}"
            UserPromptSource:
              _text: "{llm.prompt}"
      - name: MA-SanitizeModelResponse
        type: SanitizeModelResponse
        content:
          SanitizeModelResponse:
            metadata:
              name: MA-SanitizeModelResponse
            ModelArmor:
              TemplateName:
                _text: "{MA_TEMPLATE_PATH}"
            UserPromptSource:
              _text: "{llm.prompt}"
            LLMResponseSource:
              _text: "{jsonPath('$.choices[-1].message.content',response.content,true)}"

The Stage 2 template, `02-add-model-armor.yaml`, adds one line:
    
    
    gateway: apigee
    schemaVersion: 1.0.0
    name: aft-demo-02-add-model-armor
    features:
      - llm-base.yaml
      - llm-openai-format.yaml
      - target-vertex-gemini.yaml
      - llm-model-armor.yaml           # <-- the change from Stage 1
    parameters:
      - name: BASE_PATH
        default: /v1/chat/completions-stage2

The `MA_TEMPLATE_PATH` parameter defaults to a template named `apigee-aft-demo-ma` in `us-central1`. To use your own Model Armor template, override the parameter in the template's `parameters` block.

## Stage 3: Add cross-provider routing and semantic cache

In Stage 3, you add a second target (OpenAI), replace the single-route rule with model-based routing, and configure a semantic cache backed by Agent Platform Vector Search in front of both targets.

To configure Stage 3, append three feature files to the `features` block in your template:

  * `target-openai-gpt.yaml`: Adds OpenAI as a secondary target endpoint.
  * `llm-routing.yaml`: Routes requests dynamically based on the requested model name.
  * `llm-semantic-cache.yaml`: Adds a semantic cache in front of both providers.



The following example shows how the `llm-routing.yaml` feature file defines the routing logic:
    
    
    gateway: apigee
    schemaVersion: 1.0.0
    name: llm-routing
    type: feature
    parameters:
      - name: BASE_PATH
        default: /v1/chat/completions
    endpoints:
      - name: default
        basePath: "{BASE_PATH}"
        routes:
          - name: gemini
            condition: llm.model StartsWith "google/"
            target: gemini-target
          - name: openai
            target: openai-target      # default when the condition is false

The [semantic cache](https://docs.cloud.google.com/apigee/docs/api-platform/tutorials/using-semantic-caching-policies) runs `SemanticCacheLookup` in the request PreFlow and `SemanticCachePopulate` in the response PostFlow, on cache misses only. Both policies use a Agent Platform Vector Search index endpoint that you provision separately. The following excerpt shows the key parts of the policy definitions:
    
    
    policies:
      - name: SCLLookup
        type: SemanticCacheLookup
        content:
          SemanticCacheLookup:
            UserPromptSource:
              _text: "{llm.prompt}"
            Embeddings:
              VertexAI:
                URL:
                  _text: "https://{EMBEDDINGS_LOCATION}-aiplatform.googleapis.com/v1/projects/{organization.name}/locations/{EMBEDDINGS_LOCATION}/publishers/google/models/{EMBEDDINGS_MODEL}:predict"
            SimilaritySearch:
              VertexAI:
                URL:
                  _text: "https://{VECTOR_INDEX_ENDPOINT_SUBDOMAIN}.{EMBEDDINGS_LOCATION}-{PROJECT_NUMBER}.vdb.vertexai.goog/v1/projects/{organization.name}/locations/{EMBEDDINGS_LOCATION}/indexEndpoints/{VECTOR_INDEX_ENDPOINT_ID}:findNeighbors"
                DeployedIndexID:
                  _text: "{DEPLOYED_INDEX_ID}"
                Threshold:
                  _text: "{THRESHOLD}"
      - name: SCPPopulate
        type: SemanticCachePopulate
        # ... (see the GitHub repository for the full definition)

The Stage 3 template composes all of the feature files:
    
    
    gateway: apigee
    schemaVersion: 1.0.0
    name: aft-demo-03-add-routing-and-cache
    features:
      - llm-base.yaml
      - llm-openai-format.yaml
      - target-vertex-gemini.yaml
      - llm-model-armor.yaml
      - target-openai-gpt.yaml         # <-- add OpenAI target
      - llm-routing.yaml               # <-- add model-name routing
      - llm-semantic-cache.yaml        # <-- add semantic cache
    parameters:
      - name: BASE_PATH
        default: /v1/chat/completions-stage3
      - name: VECTOR_INDEX_ENDPOINT_ID
        default: "YOUR_INDEX_ENDPOINT_ID"
      - name: VECTOR_INDEX_ID
        default: "YOUR_INDEX_ID"
      - name: VECTOR_INDEX_ENDPOINT_SUBDOMAIN
        default: "YOUR_SUBDOMAIN"
      - name: PROJECT_NUMBER
        default: "YOUR_PROJECT_NUMBER"
      - name: DEPLOYED_INDEX_ID
        default: "YOUR_DEPLOYED_INDEX_ID"

Deploy the template by using the same `gcloud beta apigee apis import` command with the `--from-template` flag that you used in Stage 1.

## Stage 4: Add cross-provider fallback

Stage 4 attaches a `DefaultFaultRule` to both targets. When the primary target returns any `4xx` or `5xx` status, the fault rule sends a `ServiceCallout` with the same prompt to the other provider and returns that response to the client. The client receives a successful `200` response with a normal completion and doesn't need its own retry logic or error handling.

The `llm-fallback.yaml` feature file adds this behavior. The following example is abbreviated. For the full file, see the GitHub repository.
    
    
    gateway: apigee
    schemaVersion: 1.0.0
    name: llm-fallback
    type: feature
    targets:
      # Vertex primary; on 4xx/5xx, fall back to OpenAI.
      - name: gemini-target
        httpTargetConnection:
          Properties:
            Property:
              metadata:
                name: success.codes
              _text: "2XX"
          URL: https://aiplatform.googleapis.com/v1/projects/{organization.name}/locations/global/endpoints/openapi/chat/completions
          Authentication:
            GoogleAccessToken:
              Scopes:
                Scope: https://www.googleapis.com/auth/cloud-platform
        flows:
          - name: PostFlow
            mode: Response
            steps:
              - name: RF-TargetErrorToFault
                condition: response.status.code >= 400
        defaultFaultRule:
          name: FallbackToOpenAI
          steps:
            - name: KVM-GetOpenAIKey
            - name: AM-BuildOpenAIFallbackRequest
            - name: SC-FallbackToOpenAI
            - name: AM-CopyOpenAIFallbackResponse
      # OpenAI primary; on 4xx/5xx, fall back to Vertex.
      - name: openai-target
        httpTargetConnection:
          Properties:
            Property:
              metadata:
                name: success.codes
              _text: "2XX"
          URL: https://api.openai.com/v1/chat/completions
        flows:
          - name: PreFlow
            mode: Request
            steps:
              - name: JS-StripOpenAIModelPrefix
              - name: KVM-GetOpenAIKey
              - name: AM-SetOpenAIAuth
          - name: PostFlow
            mode: Response
            steps:
              - name: RF-TargetErrorToFault
                condition: response.status.code >= 400
        defaultFaultRule:
          name: FallbackToVertex
          steps:
            - name: AM-BuildVertexFallbackRequest
            - name: SC-FallbackToVertex
            - name: AM-CopyVertexFallbackResponse
    policies:
      # RaiseFault converts a target 4xx/5xx into a fault so DefaultFaultRule fires.
      - name: RF-TargetErrorToFault
        type: RaiseFault
        content:
          RaiseFault:
            IgnoreUnresolvedVariables: "true"
            # empty FaultResponse -- DefaultFaultRule builds the real response
      # ... AM-Build*, SC-Fallback*, AM-Copy* policies -- see GitHub repository

The fallback relies on two settings:

  * `success.codes: 2XX` on both `httpTargetConnection` blocks. Apigee treats any non-`2xx` target response as a target failure and transitions directly to the fault flow.
  * A `RaiseFault` policy in each target's response PostFlow, gated on `response.status.code >= 400`. This policy guarantees that the `DefaultFaultRule` runs for every error response.



Compose the Stage 4 template, which adds one line to the Stage 3 template:
    
    
    gateway: apigee
    schemaVersion: 1.0.0
    name: aft-demo-04-add-fallback
    features:
      - llm-base.yaml
      - llm-openai-format.yaml
      - target-vertex-gemini.yaml
      - llm-model-armor.yaml
      - target-openai-gpt.yaml
      - llm-routing.yaml
      - llm-semantic-cache.yaml
      - llm-fallback.yaml              # <-- the change from Stage 3
    parameters:
      - name: BASE_PATH
        default: /v1/chat/completions-stage4
      # ... Model Armor and Vector Search parameters as in Stage 3

Deploy the template:
    
    
    gcloud beta apigee apis import aft-demo-04-add-fallback \
      --from-template=04-add-fallback.yaml \
      --organization=APIGEE_ORG

## Verify end-to-end behavior

The GitHub repository includes a `routing-diagnostic.sh` script that exercises all of the routing and fallback paths with topically diverse prompts. Because the semantic cache short-circuits similar prompts, each test prompt must be worded distinctly.
    
    
    STAGE=4 ./routing-diagnostic.sh

The script sends five requests through the Stage 4 proxy:

  * A canonical OpenAI model
  * A Gemini model with the `google/` prefix
  * A Gemini model name without a prefix, which routes to OpenAI under the inverted default
  * An OpenAI reasoning model
  * A model name with the `openai/` prefix



For each request, the script reports which upstream provider served the response and whether fallback occurred.

To see every policy step, target call, and fault rule transition for a single request, create an [Apigee debug session](https://docs.cloud.google.com/apigee/docs/api-platform/debug/trace) against the deployed revision:
    
    
    DEBUG_URL="https://apigee.googleapis.com/v1/organizations/APIGEE_ORG/environments/APIGEE_ENV/apis/aft-demo-04-add-fallback/revisions/REVISION/debugsessions"
    curl -X POST -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
      -H "Content-Type: application/json" \
      -d '{"filter":"","count":10,"timeout":"600","validity":600}' \
      "$DEBUG_URL"

Replace the following:

  * `APIGEE_ORG`: your Apigee organization name.
  * `APIGEE_ENV`: the environment where you deployed the proxy.
  * `REVISION`: the deployed revision number of the `aft-demo-04-add-fallback` proxy.



Then send a request that exercises the fallback:
    
    
    curl -X POST https://APIGEE_HOSTNAME/v1/chat/completions-stage4 \
      -H "Content-Type: application/json" \
      -d '{"model":"gpt-4o-mini",
           "messages":[{"role":"user","content":"Describe nuclear fusion in stars in two sentences."}]}'

When you retrieve the captured debug session messages by using the Apigee API, the trace shows the following execution flow:

  1. **Extract request variables** : Apigee extracts the `llm.model` and `llm.prompt` variables from the incoming payload.
  2. **Evaluate safety policies** : The request passes Model Armor security filtering.
  3. **Check the semantic cache** : The lookup misses the semantic cache, so the request continues to a target.
  4. **Evaluate the routing condition** : The condition `llm.model StartsWith "google/"` evaluates to `false`.
  5. **Route to the primary target** : Apigee forwards the request to `openai-target`.
  6. **Handle the target error** : The OpenAI target returns a non-`2xx` HTTP status code, which causes Apigee to raise a target error.
  7. **Run the fault rule** : The `DefaultFaultRule` triggers the fallback sequence by running `AM-BuildVertexFallbackRequest`, `SC-FallbackToVertex`, and `AM-CopyVertexFallbackResponse`.
  8. **Return the response** : The client receives an HTTP `200` response that contains a payload generated by Gemini on Agent Platform.



## What's next

  * **Configure authentication** : Implement federated JWT, OpenID Connect (OIDC), or Apigee API keys in front of the proxy to enforce tenant-specific token quotas and provider access controls.
  * **Monitor cost and latency** : Attach Apigee analytics dashboards to your API proxy to track latency and operational costs on a per-model basis.
  * **Apply tenant-specific safety policies** : Configure per-tenant Model Armor templates by using the `MA_TEMPLATE_PATH` parameter to apply tailored sanitization rules across enterprise, developer, and public traffic.
  * **Explore sample configurations** : To download the complete example set, including the `llm-fallback.yaml` template, eight feature files, the `routing-diagnostic.sh` script, and provisioning scripts for KVM, Model Armor, and Agent Platform Vector Search, see the [Apigee progressive AI gateway repository on GitHub](https://github.com/gcp-samples/apigee-template-repository/tree/main/examples/ai-gateway-progressive).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
