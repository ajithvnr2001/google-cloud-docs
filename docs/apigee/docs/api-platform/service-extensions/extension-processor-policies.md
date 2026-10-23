---
url: https://docs.cloud.google.com/apigee/docs/api-platform/service-extensions/extension-processor-policies/
title: Configure Apigee policies with the extension processor \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:18:48.877819+00:00
---

# Configure Apigee policies with the extension processor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/service-extensions/extension-processor-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Configure Apigee policies with the extension processor Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

The Apigee extension processor lets you apply AI gateway capabilities from Apigee to traffic that doesn't flow through an Apigee proxy. For example, a service running on Google Kubernetes Engine, an API managed by another gateway, or a MCP server for an AI agent. Since the traffic path differs from a standard API proxy, some policy configuration is specific to the extension processor. This page describes those considerations and provides example configurations. Each policy section links to that policy's full tutorial.

**Important:** This page covers policy configuration only. It assumes you have already connected the extension processor to a load balancer or an Agent Gateway. For the setup steps—creating the Apigee environment and proxy, the service extension, and the networking resources—follow the guide for your deployment in the following list first.

The policies on this page apply the same way wherever the extension processor is attached:

  * To an [Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/application-load-balancer), as a [traffic extension](https://docs.cloud.google.com/service-extensions/docs/configure-traffic-extensions), governing traffic to the backends behind it. To set this up, see [Get started with the Apigee extension processor](https://docs.cloud.google.com/apigee/docs/api-platform/service-extensions/extension-processor-quickstart).
  * To an [Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview), as an [authorization extension](https://docs.cloud.google.com/service-extensions/docs/configure-authorization-extensions), governing an AI agent's outbound calls—to its model, and to the tools and MCP servers it uses—without changing the agent. To set this up, see [Connect the Apigee extension processor to an Agent Gateway](https://docs.cloud.google.com/apigee/docs/api-platform/service-extensions/extension-processor-agent-gateway).



## Key considerations

The following considerations apply when you attach any policy to an extension processor proxy. For where to attach them, see [Use policies with the extension processor](https://docs.cloud.google.com/apigee/docs/api-platform/service-extensions/extension-processor-quickstart#use-policies) in the quickstart.

### Match the examples to your model API

The examples on this page use the Gemini request and response shape. Other model providers work the same way: `UserPromptSource`, `LLMTokenUsageSource`, and `LLMModelSource` are message templates, so you set them to the equivalent location in that API's payload. The policies themselves are unchanged.

### Scope the traffic you process

With a standard API proxy, you assign a base path and clients call that specific URL, so the proxy only receives the traffic intended for it. The extension processor has no base path, so you scope its traffic in two places: at the extension, which decides what reaches Apigee at all, and in the proxy, which decides what runs on the traffic that arrives. Use both.

Filter at the extension first, so that traffic you don't intend to govern is never sent to Apigee:

  * On a traffic extension, set a [CEL match condition](https://docs.cloud.google.com/service-extensions/docs/cel-matcher-language-reference) on the extension chain, for example `matchCondition.celExpression: 'request.host == "example.com"'`.
  * On an authorization extension, match hosts and path prefixes under `httpRules.to.operations` in the [authorization policy](https://docs.cloud.google.com/service-extensions/docs/configure-authorization-extensions).



Then scope individual policies inside the proxy. A single extension processor proxy receives everything the extension selects, and that can still be a mix: an AI agent's model calls, session and state calls, and telemetry calls can share a host. A policy that inspects a model payload fails on a call that doesn't carry one, and a failed policy blocks the request. Attach each policy with a [condition](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/flow-variables-and-conditions) that scopes it to the intended traffic:
    
    
    <!-- Run only on the model (generateContent) call -->
    <Step>
      <Name>My-Policy</Name>
      <Condition>(request.uri Like "*generateContent*")</Condition>
    </Step>
    
    <!-- Or scope by backend host -->
    <Step>
      <Name>My-Policy</Name>
      <Condition>(request.header.host = "backend.example.com")</Condition>
    </Step>

### Use a no-target proxy

Extension processor proxies process intercepted traffic and do not have a target endpoint. Deploy them as **extensible** proxies. All proxies in an extension processor environment must be of the same proxy type.

### Read the body of the intercepted call

Policies that inspect the payload operate on the message as it appears on the wire. For a model call, this is the model's request and response. For example, the user prompt is at `$.contents[-1].parts[-1].text` and the model response is at `$.candidates[-1].content.parts[-1].text`.

### Grant a service account for policies that call Google services

Policies that call a Google service—for example, Model Armor, or the embeddings and index lookups used by semantic caching—require a deployment service account. Deploy the proxy with the `serviceAccount` parameter.

## AI safety with Model Armor

Attach the [SanitizeUserPrompt](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-user-prompt-policy) and [SanitizeModelResponse](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-llm-response-policy) policies, scoped to the model call. For template setup, see [Get started with Model Armor](https://docs.cloud.google.com/apigee/docs/api-platform/tutorials/using-model-armor-policies).
    
    
    <SanitizeUserPrompt name="SUP-sanitize" continueOnError="false">
      <ModelArmor>
        <TemplateName>projects/PROJECT/locations/LOCATION/templates/TEMPLATE</TemplateName>
      </ModelArmor>
      <UserPromptSource>{jsonPath('$.contents[-1].parts[-1].text',request.content,true)}</UserPromptSource>
    </SanitizeUserPrompt>

Attach `SUP-sanitize` in the request flow with the condition `(request.uri Like "*generateContent*")`. When the prompt matches the Model Armor template, the policy rejects the request, so the prompt never reaches the model.

## Semantic caching

Attach the [SemanticCacheLookup](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/semantic-cache-lookup-policy) policy in the request flow and the [SemanticCachePopulate](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/semantic-cache-populate-policy) policy in the response flow, both scoped to the model call. For index and embeddings setup, see [Get started with semantic caching](https://docs.cloud.google.com/apigee/docs/api-platform/tutorials/using-semantic-caching-policies). When a request matches a cached prompt, the response is served from the cache without calling the model.

## Token limits for model calls

Two policies limit large language model (LLM) token usage on the model call. Scope both to the model call with the condition `(request.uri Like "*generateContent*")`. For setup, see [Get started with LLM token policies](https://docs.cloud.google.com/apigee/docs/api-platform/tutorials/using-ai-token-policies).

### Limit prompt tokens

The [PromptTokenLimit](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/prompt-token-limit-policy) policy throttles tokens based on the user prompt—a spike arrest for prompts. Attach it in the request flow; it reads the prompt from the intercepted request and rejects the call when the rate is exceeded, so an oversized prompt never reaches the model. The following example limits prompts to 1,000 tokens per minute:
    
    
    <PromptTokenLimit continueOnError="false" enabled="true" name="PTL-limit-prompt">
      <Rate>1000pm</Rate>
      <UserPromptSource>{jsonPath('$.contents[-1].parts[-1].text',request.content,true)}</UserPromptSource>
    </PromptTokenLimit>

### Limit response token consumption

The [LLMTokenQuota](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/llm-token-quota-policy) policy enforces a token-consumption quota over a time interval, counting the tokens returned in the model response. Attach an `EnforceOnly` instance in the request flow to reject calls once the quota is exceeded, and a `CountOnly` instance in the response flow to count the tokens used, read from `$.usageMetadata.candidatesTokenCount`. Give both instances the same `SharedName` so they update a single counter. This policy requires an extensible proxy. The following pair enforces 15,000 tokens per 30 minutes:
    
    
    <!-- Request flow: reject when the token quota is exceeded -->
    <LLMTokenQuota name="LTQ-enforce" type="rollingwindow">
      <SharedName>llm-token-counter</SharedName>
      <EnforceOnly>true</EnforceOnly>
      <Allow count="15000"/>
      <Interval>30</Interval>
      <TimeUnit>minute</TimeUnit>
      <Distributed>true</Distributed>
    </LLMTokenQuota>
    
    <!-- Response flow: count the tokens used in the model response -->
    <LLMTokenQuota name="LTQ-count" type="rollingwindow">
      <SharedName>llm-token-counter</SharedName>
      <CountOnly>true</CountOnly>
      <Allow count="15000"/>
      <Interval>30</Interval>
      <TimeUnit>minute</TimeUnit>
      <Distributed>true</Distributed>
      <LLMTokenUsageSource>{jsonPath('$.usageMetadata.candidatesTokenCount',response.content,true)}</LLMTokenUsageSource>
    </LLMTokenQuota>

## Traffic governance: quota, authorization, and spike arrest

These policies enforce on traffic through the extension processor to any backend, including backends that aren't hosted on Apigee, such as a GKE-hosted API or a tool or MCP server that an AI agent calls. Scope each policy to the backend that you want to protect:
    
    
    <Step><Name>Verify-API-Key</Name><Condition>(request.header.host = "backend.example.com")</Condition></Step>
    <Step><Name>Quota-Limit</Name><Condition>(request.header.host = "backend.example.com")</Condition></Step>
    <Step><Name>Spike-Arrest</Name><Condition>(request.header.host = "backend.example.com")</Condition></Step>

  * **Authorization** : use the [VerifyAPIKey](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/verify-api-key-policy) or [OAuthV2](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/oauthv2-policy) policy. Unauthorized calls are rejected before they reach the backend.
  * **Quota** : use the [Quota](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/quota-policy) policy to enforce a precise call limit. Configure the policy as distributed and synchronous so the limit is enforced as a single shared count across the runtime.
  * **Spike arrest** : use the [SpikeArrest](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/spike-arrest-policy) policy to smooth traffic bursts. Spike arrest is enforced per message processor and doesn't guarantee an exact global rate; when you need a precise limit, use the Quota policy.



## Transform messages and extract variables

Use the [AssignMessage](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy) policy to add, change, or remove parts of a message—headers, query parameters, or the payload—and the [ExtractVariables](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/extract-variables-policy) policy to read values out of a message into variables that later policies can use. With the extension processor, both policies work in the request flow, operating on the intercepted request, and in the response flow, operating on the backend response. As with any extension processor policy, scope each attachment with a condition so it runs only on the intended traffic.

The following example uses ExtractVariables to read a field from the request body, and in the response flow to read a field from the response body:
    
    
    <!-- Request flow: read a field from the intercepted request -->
    <ExtractVariables name="EV-from-request">
      <Source>request</Source>
      <JSONPayload>
        <Variable name="user.prompt">
          <JSONPath>$.contents[-1].parts[-1].text</JSONPath>
        </Variable>
      </JSONPayload>
    </ExtractVariables>
    
    <!-- Response flow: read a field from the backend response -->
    <ExtractVariables name="EV-from-response">
      <Source>response</Source>
      <JSONPayload>
        <Variable name="model.answer">
          <JSONPath>$.candidates[-1].content.parts[-1].text</JSONPath>
        </Variable>
      </JSONPayload>
    </ExtractVariables>

The following example uses AssignMessage to set a header on the request before it reaches the backend, and on the response before it returns to the caller:
    
    
    <!-- Request flow: add a header to the intercepted request -->
    <AssignMessage name="AM-set-request-header">
      <Set>
        <Headers>
          <Header name="X-Apigee-Processed">true</Header>
        </Headers>
      </Set>
      <AssignTo createNew="false" type="request"/>
    </AssignMessage>
    
    <!-- Response flow: add a header to the backend response -->
    <AssignMessage name="AM-set-response-header">
      <Set>
        <Headers>
          <Header name="X-Apigee-Cache">miss</Header>
        </Headers>
      </Set>
      <AssignTo createNew="false" type="response"/>
    </AssignMessage>

## What's next

  * Read the [Apigee extension processor overview](https://docs.cloud.google.com/apigee/docs/api-platform/service-extensions/extension-processor-overview).
  * Learn how to [get started with the Apigee extension processor](https://docs.cloud.google.com/apigee/docs/api-platform/service-extensions/extension-processor-quickstart) on a load balancer.
  * Learn how to [connect the Apigee extension processor to an Agent Gateway](https://docs.cloud.google.com/apigee/docs/api-platform/service-extensions/extension-processor-agent-gateway).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
