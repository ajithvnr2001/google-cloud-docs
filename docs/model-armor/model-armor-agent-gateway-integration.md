---
url: https://docs.cloud.google.com/model-armor/model-armor-agent-gateway-integration/
title: Integrate Model Armor with Agent Gateway \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:40.156411+00:00
---

# Integrate Model Armor with Agent Gateway  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/model-armor/model-armor-agent-gateway-integration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Model Armor ](https://docs.cloud.google.com/model-armor)
  * [ Guides ](https://docs.cloud.google.com/model-armor/overview)



Send feedback 

#  Integrate Model Armor with Agent Gateway Stay organized with collections  Save and categorize content based on your preferences. 

Gemini Enterprise Agent Platform is a platform for building and managing enterprise-grade AI agents. [Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview) serves as a control plane that manages, secures, and governs how AI agents connect and interact within the Google Cloud environment and with external agents, AI applications, and LLMs. The integration of Model Armor and Agent Gateway embeds Model Armor's screening capabilities directly into the communication pathways Gemini Enterprise Agent Platform manages. When content passes through Agent Gateway, it invokes Model Armor to enforce your predefined security templates. You can configure your template to either block and redact content that violates policies, or to only inspect content and log any violations that are detected. This mitigates risks such as prompt injection, jailbreaks, exposure to harmful content, and sensitive data leakage.

When Model Armor detects policy violations in content passing through Agent Gateway, it can be configured to log these events. You can view these findings on the **Model Armor** page in the Google Cloud console ([Go to Model Armor](https://console.cloud.google.com/security/model-armor)). These findings are also surfaced in Security Command Center. For more information, see [Review findings in the Google Cloud console](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#review-ma-findings).

When using the real-time streaming mode, Model Armor supports unlimited tokens in the stream, making it suitable for long-running interactions and model responses.

## Limitations

Consider the following limitations when integrating Model Armor with Agent Gateway:

  * **Streaming support for agents** : Model Armor only supports streaming sanitization using the `streamQuery` method for agents built with the Agent Development Kit.
  * **Cross-project template usage** : When using a Model Armor template in one project to sanitize requests for a service, like Agent Gateway, in a different project, the API quota for Model Armor needs to be sufficient in both the project hosting the template and the project hosting the calling service. For more information, see [Manage quota](https://docs.cloud.google.com/model-armor/integrations#manage-quota).
  * **Regional alignment** : Model Armor and the services it integrates with must be deployed within the same Google Cloud region. Cross-region calls to Model Armor are not supported.
  * **Egress integration compatibility** : Model Armor's inline protection on egress traffic is limited to integrations with MCP servers, services following the [OpenAI format](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/start/openai), and A2A through Agent Gateway.
  * **Ingress integration compatibility** : Inline ingress protection with Model Armor is only supported for agents built using ADK.
  * **No document support** : Sanitizing prompts and responses that contain documents or file uploads (such as PDFs) isn't supported in this integration. To screen documents, call the [Model Armor REST API](https://docs.cloud.google.com/model-armor/sanitize-prompts-responses#file-prompts) directly.
  * **Supported payloads** : For a list of supported payloads, see Supported and unsupported payloads in this document.



## Configure Model Armor on a gateway

To configure Model Armor on a gateway, follow these steps:

  1. [Enable the Model Armor API](https://docs.cloud.google.com/model-armor/manage-templates#enable-apis) in the project where you want to create the Model Armor templates.
  2. [Create one or more Model Armor templates](https://docs.cloud.google.com/model-armor/manage-templates#create-ma-template) in the same region where you plan to add the gateway. You can use the same template for both ingress and egress traffic.

Take note of the template names. To copy the name of a template in the Google Cloud console, [view the template's details](https://docs.cloud.google.com/model-armor/manage-templates#view-ma-template) and click content_copy **Copy to clipboard** next to the template name.

  3. Set up Agent Gateway in the same region where the Model Armor templates are stored. For the [Client-to-Agent (ingress) gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/set-up-agent-gateway#config-client-to-agent), specify the Model Armor templates that you created for ingress traffic. For the [Agent-to-Anywhere (egress) gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/set-up-agent-gateway#config-agent-to-anywhere), specify the Model Armor templates that you created for egress traffic. You can use the same template for both traffic flows.

  4. Grant the required IAM roles to the appropriate service agents:

     * **Client-to-Agent (ingress)** : Grant the [AI Platform Reasoning Engine Service Agent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/manage-agent-access#service-agent) service agent the following roles:

       * The Model Armor Callout User (`roles/modelarmor.calloutUser`) role in the project that contains the AI agent.

       * The Model Armor User (`roles/modelarmor.user`) role in the project that contains the Model Armor template.
    
    gcloud projects add-iam-policy-binding AGENT_RUNTIME_PROJECT_ID \
        --member=serviceAccount:service-AGENT_RUNTIME_PROJECT_NUMBER@gcp-sa-aiplatform-re.iam.gserviceaccount.com \
        --role=roles/modelarmor.calloutUser
    gcloud projects add-iam-policy-binding MODEL_ARMOR_PROJECT_ID \
        --member=serviceAccount:service-AGENT_RUNTIME_PROJECT_NUMBER@gcp-sa-aiplatform-re.iam.gserviceaccount.com \
        --role=roles/modelarmor.user
    

Replace the following:

       * `AGENT_RUNTIME_PROJECT_ID`: The project ID of the project where you created the agent.
       * `AGENT_RUNTIME_PROJECT_NUMBER`: The project number of the project where you created the agent.
       * `MODEL_ARMOR_PROJECT_ID`: The project ID of the project that contains the Model Armor template.
     * **Agent-to-Anywhere (egress)** : Grant the Service Extensions service agent the following roles:

       * The Model Armor Callout User (`roles/modelarmor.calloutUser`) and Service Usage Consumer (`roles/serviceusage.serviceUsageConsumer`) roles in the project that contains the gateway.
       * The Model Armor User (`roles/modelarmor.user`) role in the project that contains the Model Armor template.
    
    gcloud projects add-iam-policy-binding GATEWAY_PROJECT_ID \
        --member=serviceAccount:service-GATEWAY_PROJECT_NUMBER@gcp-sa-dep.iam.gserviceaccount.com \
        --role=roles/modelarmor.calloutUser
    gcloud projects add-iam-policy-binding GATEWAY_PROJECT_ID \
        --member=serviceAccount:service-GATEWAY_PROJECT_NUMBER@gcp-sa-dep.iam.gserviceaccount.com \
        --role=roles/serviceusage.serviceUsageConsumer
    gcloud projects add-iam-policy-binding MODEL_ARMOR_PROJECT_ID \
        --member=serviceAccount:service-GATEWAY_PROJECT_NUMBER@gcp-sa-dep.iam.gserviceaccount.com \
        --role=roles/modelarmor.user
    

Replace the following:

       * `GATEWAY_PROJECT_ID`: The project ID of the project where you created the gateway.
       * `GATEWAY_PROJECT_NUMBER`: The project number of the project where you created the gateway.
       * `MODEL_ARMOR_PROJECT_ID`: The project ID of the project that contains the Model Armor template.

For instructions, see [Delegate authorization to Model Armor](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/delegate-authorization#configure-authz-ma).

For general information about how to grant a role, see [Grant a single IAM role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role).




## Ingress and egress traffic

In the context of Agent Gateway and Model Armor integration, the terms _ingress_ and _egress_ are used from the perspective of the AI agent's interactions:

  * **Ingress Traffic (Client-to-Agent):** Refers to the communication flow between a client and the agent. Model Armor can protect both the incoming requests from the client to the agent and the outgoing responses from the agent back to the client.
  * **Egress Traffic (Agent-to-Anywhere):** Refers to the communication flow between the agent and an external system. Model Armor can protect both the outgoing requests from the agent to the external system and the incoming responses from the external system back to the agent.



### Client-to-Agent (ingress) protection

You define templates that Model Armor uses to evaluate:

  * Incoming requests from the _client_ (end users or calling applications) to your AI agent.
  * Outgoing responses from the AI agent back to the client.



You can apply a single template to both directions or configure different templates for each.

#### Traffic flow for Client-to-Agent

  1. A client sends a prompt to the agent. Agent Gateway intercepts the request and sends the payload to Model Armor.
  2. Model Armor screens the request. If blocked, the client receives an error.
  3. If allowed, the request reaches the AI agent.
  4. The AI agent generates a response. Agent Gateway intercepts this response before it reaches the client.
  5. Model Armor screens the response, and Agent Gateway either allows or blocks it based on the verdict.



### Agent-to-Anywhere (egress) protection

You define templates that Model Armor uses to evaluate:

  * Outgoing requests from your AI agent to external systems.
  * Incoming responses from external systems back to your AI agent.



This protection applies to communications with systems including:

  * External LLMs and third-party AI agents
  * Model Context Protocol (MCP) servers
  * Other AI agents



#### Traffic flow for Agent-to-Anywhere

  1. The AI agent initiates a request to an external system. Agent Gateway intercepts the outgoing traffic.
  2. Model Armor screens the outgoing payload. If blocked, the connection is terminated.
  3. If allowed, the request is sent to the external system.
  4. The external system sends a response back. Agent Gateway intercepts this incoming response.
  5. Model Armor screens the response payload, and Agent Gateway either allows it to reach the agent or blocks it.



For more information, see [Configure Model Armor on a gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/configure-model-armor).

## Track and debug streaming requests

To facilitate tracking and debugging of streaming requests, Model Armor uses a correlation ID and a trace ID.

### Use a trace ID

A trace ID connects all events for a single request as it travels across multiple services in a distributed system. This includes the security enforcements that Model Armor applies within the request path of the Agent Gateway resource.

Each trace contains one or more spans, where each span ID represents a specific operation or unit of work within the trace. Logs generated during the execution of a request are associated with the specific span ID of the operation performing the work.

A trace ID is handled in two ways:

  * **Automatic** : When Google Cloud Observability is enabled, Agent Gateway automatically generates a trace ID and propagates it through the system.
  * **User-provided** : You can override the system-generated trace ID by providing your own using the traceparent HTTP header in your requests.

The following code sample shows how to pass a custom trace ID in a request to the `streamQuery` method:
        
        curl -X POST \
          -H "Authorization: Bearer $(gcloud auth print-access-token)" \
          -H "Content-Type: application/json" \
          -H "traceparent: 00-98adffecc8dd095968a06c44216190f6-5b565a8342378cd7-01" \
          "https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/reasoningEngines/REASONING_ENGINE_ID:streamQuery?alt=sse"
        

Replace the following:

    * `LOCATION`: the region where the reasoning engine is located.
    * `PROJECT_ID`: the ID of your Google Cloud project.
    * `REASONING_ENGINE_ID`: the ID of your reasoning engine.



Using a trace ID is the recommended method to correlate logs and traces end-to-end from the caller through Agent Gateway to Model Armor and any downstream agents. This is essential for debugging, understanding security actions, and monitoring performance. For more information, see [View Model Armor trace spans](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/view-model-armor-spans).

To view sanitization operation logs for a specific trace ID, use the following query in the Logs Explorer:
    
    
    jsonPayload.@type="type.googleapis.com/google.cloud.modelarmor.logging.v1.SanitizeOperationLogEntry"
    trace:TRACE_ID
    

Replace `TRACE_ID` with the trace ID of your request.

### Use a correlation ID

A correlation ID links together all log entries in Cloud Logging that pertain to a single streaming sanitization session, from the initial request to the final response. It is an internal identifier primarily used within Model Armor logs, specifically for ingress streaming sessions. For more information, see [Correlate logs and related events](https://docs.cloud.google.com/model-armor/configure-logging#correlate-logs-and-events).

## Supported and unsupported payloads

This section lists the types of payloads that Model Armor sanitizes.

### Client-to-Agent (ingress) traffic

For Client-to-Agent (ingress) traffic using the ADK protocol, Model Armor sanitizes only [`reasoningEngines.streamQuery`](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/reference/rest/v1/projects.locations.reasoningEngines/streamQuery) requests and responses for agents that were built using Agent Development Kit (ADK) and are running on Agent Runtime.

All other [`ReasoningEngine`](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/reference/rest/v1/projects.locations.reasoningEngines) payloads and `ReasoningEngine` error responses aren't sent to Model Armor. Non-ADK payloads (such as Langchain payloads) are also not sent to Model Armor.

### Agent-to-Anywhere (egress) traffic

For Agent-to-Anywhere (egress) traffic, the following payloads are supported.

#### A2A payloads

Model Armor sanitizes only the following payloads of the [A2A v1 protocol](https://a2a-protocol.org/latest/):

  * [Send Message](https://a2a-protocol.org/latest/specification/#311-send-message) operations
  * [Agent Card](https://a2a-protocol.org/latest/specification/#441-agentcard)
  * [Get Extended Agent Card](https://a2a-protocol.org/latest/specification/#3111-get-extended-agent-card) operations
  * [JSON-RPC](https://a2a-protocol.org/latest/specification/#9-json-rpc-protocol-binding) protocol bindings
  * [HTTP+JSON/REST](https://a2a-protocol.org/latest/specification/#11-httpjsonrest-protocol-binding) protocol bindings



Model Armor allows the following A2A payloads without sanitization:

  * Payloads from A2A versions earlier than v1
  * [`SendStreamingMessage`](https://a2a-protocol.org/latest/specification/#942-sendstreamingmessage)
  * [`GetTask`](https://a2a-protocol.org/latest/specification/#943-gettask)
  * [`ListTasks`](https://a2a-protocol.org/latest/specification/#944-listtasks)
  * [`CancelTask`](https://a2a-protocol.org/latest/specification/#945-canceltask)
  * [`SubscribeToTask`](https://a2a-protocol.org/latest/specification/#946-subscribetotask)
  * [CRUD methods](https://a2a-protocol.org/latest/specification/#1047-createtaskpushnotificationconfig) on `TaskPushNotificationConfig`
  * Payloads using A2A [gRPC](https://a2a-protocol.org/latest/specification/#10-grpc-protocol-binding) protocol binding (protobuf on the wire)
  * A2A error payloads



#### MCP payloads

Model Armor sanitizes only the following MCP payloads:

  * `tools/call` request and response
  * `prompts/get` request and response
  * [MCP tool execution errors](https://modelcontextprotocol.io/specification/2025-11-25/server/tools#error-handling) (target for prompt injection by malicious MCP tools authors)



Model Armor allows the following payloads without sanitization:

  * `tools/list`
  * `resources/*`
  * `notifications/*`
  * Streamable HTTP/SSE for MCP
  * MCP protocol errors (for example, all errors other than tool execution errors)



#### External LLM payloads

Model Armor sanitizes only the following payloads of the OpenAI API protocol (egress), which includes GPT models on `openai.com` as well as any other models through OpenAI API-compatible LLM servers (such as [vLLM](https://docs.vllm.ai/en/latest/serving/openai_compatible_server/#supported-apis)). Payloads that aren't listed here are allowed without sanitization.

  * [Chat completions](https://developers.openai.com/api/reference/resources/chat/subresources/completions): Create, Delete, Get, List, and Update (non-streaming variants only)
  * [Get chat messages](https://developers.openai.com/api/reference/resources/chat/subresources/completions/subresources/messages)
  * [Responses](https://developers.openai.com/api/reference/resources/responses): Create, Get, and Delete (non-streaming variants only)
  * [OpenAI API errors](https://community.openai.com/t/error-code-for-openai-chat-completion/1102402) (including [vLLM's variant](https://github.com/vllm-project/vllm/issues/12886))
  * [Legacy Completions](https://developers.openai.com/api/reference/resources/beta/subresources/assistants)
  * [Legacy Assistants](https://developers.openai.com/api/reference/resources/beta/subresources/assistants/methods/create): Create, Delete, List, Modify, and Retrieve
  * [Legacy Messages](https://developers.openai.com/api/reference/resources/beta/subresources/threads/subresources/messages): Create, Delete, List, Modify, and Retrieve
  * [Legacy Threads](https://developers.openai.com/api/reference/resources/beta/subresources/threads/methods/create): Create, Delete, Modify, and Retrieve
  * [Embeddings](https://developers.openai.com/api/reference/resources/embeddings/methods/create): Create



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
