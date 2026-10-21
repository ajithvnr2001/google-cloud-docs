---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1
title: Package lf.a2a.v1 \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:25:09.363637+00:00
---

# Package lf.a2a.v1  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Package lf.a2a.v1 Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[A2AService](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.A2AService)` (interface)
  * `[APIKeySecurityScheme](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.APIKeySecurityScheme)` (message)
  * `[AgentCapabilities](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.AgentCapabilities)` (message)
  * `[AgentCard](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.AgentCard)` (message)
  * `[AgentCardSignature](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.AgentCardSignature)` (message)
  * `[AgentExtension](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.AgentExtension)` (message)
  * `[AgentInterface](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.AgentInterface)` (message)
  * `[AgentProvider](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.AgentProvider)` (message)
  * `[AgentSkill](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.AgentSkill)` (message)
  * `[Artifact](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.Artifact)` (message)
  * `[AuthenticationInfo](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.AuthenticationInfo)` (message)
  * `[AuthorizationCodeOAuthFlow](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.AuthorizationCodeOAuthFlow)` (message)
  * `[CancelTaskRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.CancelTaskRequest)` (message)
  * `[ClientCredentialsOAuthFlow](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.ClientCredentialsOAuthFlow)` (message)
  * `[DeleteTaskPushNotificationConfigRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.DeleteTaskPushNotificationConfigRequest)` (message)
  * `[DeviceCodeOAuthFlow](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.DeviceCodeOAuthFlow)` (message)
  * `[GetExtendedAgentCardRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.GetExtendedAgentCardRequest)` (message)
  * `[GetTaskPushNotificationConfigRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.GetTaskPushNotificationConfigRequest)` (message)
  * `[GetTaskRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.GetTaskRequest)` (message)
  * `[HTTPAuthSecurityScheme](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.HTTPAuthSecurityScheme)` (message)
  * `[ImplicitOAuthFlow](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.ImplicitOAuthFlow)` (message)
  * `[ListTaskPushNotificationConfigsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.ListTaskPushNotificationConfigsRequest)` (message)
  * `[ListTaskPushNotificationConfigsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.ListTaskPushNotificationConfigsResponse)` (message)
  * `[ListTasksRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.ListTasksRequest)` (message)
  * `[ListTasksResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.ListTasksResponse)` (message)
  * `[Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.Message)` (message)
  * `[MutualTlsSecurityScheme](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.MutualTlsSecurityScheme)` (message)
  * `[OAuth2SecurityScheme](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.OAuth2SecurityScheme)` (message)
  * `[OAuthFlows](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.OAuthFlows)` (message)
  * `[OpenIdConnectSecurityScheme](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.OpenIdConnectSecurityScheme)` (message)
  * `[Part](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.Part)` (message)
  * `[PasswordOAuthFlow](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.PasswordOAuthFlow)` (message)
  * `[Role](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.Role)` (enum)
  * `[SecurityRequirement](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.SecurityRequirement)` (message)
  * `[SecurityScheme](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.SecurityScheme)` (message)
  * `[SendMessageConfiguration](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.SendMessageConfiguration)` (message)
  * `[SendMessageRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.SendMessageRequest)` (message)
  * `[SendMessageResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.SendMessageResponse)` (message)
  * `[StreamResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.StreamResponse)` (message)
  * `[StringList](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.StringList)` (message)
  * `[SubscribeToTaskRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.SubscribeToTaskRequest)` (message)
  * `[Task](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.Task)` (message)
  * `[TaskArtifactUpdateEvent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.TaskArtifactUpdateEvent)` (message)
  * `[TaskPushNotificationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.TaskPushNotificationConfig)` (message)
  * `[TaskState](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.TaskState)` (enum)
  * `[TaskStatus](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.TaskStatus)` (message)
  * `[TaskStatusUpdateEvent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.TaskStatusUpdateEvent)` (message)



## A2AService

Provides operations for interacting with agents using the A2A protocol.

CancelTask  
---  
` rpc CancelTask(`[CancelTaskRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.CancelTaskRequest)`) returns (`[Task](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.Task)`) ` Cancels a task in progress.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
CreateTaskPushNotificationConfig  
---  
` rpc CreateTaskPushNotificationConfig(`[TaskPushNotificationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.TaskPushNotificationConfig)`) returns (`[TaskPushNotificationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.TaskPushNotificationConfig)`) ` Creates a push notification config for a task.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
DeleteTaskPushNotificationConfig  
---  
` rpc DeleteTaskPushNotificationConfig(`[DeleteTaskPushNotificationConfigRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.DeleteTaskPushNotificationConfigRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes a push notification config for a task.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetExtendedAgentCard  
---  
` rpc GetExtendedAgentCard(`[GetExtendedAgentCardRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.GetExtendedAgentCardRequest)`) returns (`[AgentCard](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.AgentCard)`) ` Gets the extended agent card for the authenticated agent.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetTask  
---  
` rpc GetTask(`[GetTaskRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.GetTaskRequest)`) returns (`[Task](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.Task)`) ` Gets the latest state of a task.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetTaskPushNotificationConfig  
---  
` rpc GetTaskPushNotificationConfig(`[GetTaskPushNotificationConfigRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.GetTaskPushNotificationConfigRequest)`) returns (`[TaskPushNotificationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.TaskPushNotificationConfig)`) ` Gets a push notification config for a task.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListTaskPushNotificationConfigs  
---  
` rpc ListTaskPushNotificationConfigs(`[ListTaskPushNotificationConfigsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.ListTaskPushNotificationConfigsRequest)`) returns (`[ListTaskPushNotificationConfigsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.ListTaskPushNotificationConfigsResponse)`) ` Get a list of push notifications configured for a task.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListTasks  
---  
` rpc ListTasks(`[ListTasksRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.ListTasksRequest)`) returns (`[ListTasksResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.ListTasksResponse)`) ` Lists tasks that match the specified filter.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
SendMessage  
---  
` rpc SendMessage(`[SendMessageRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.SendMessageRequest)`) returns (`[SendMessageResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.SendMessageResponse)`) ` Sends a message to an agent.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
SendStreamingMessage  
---  
` rpc SendStreamingMessage(`[SendMessageRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.SendMessageRequest)`) returns (`[StreamResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.StreamResponse)`) ` Sends a streaming message to an agent, allowing for real-time interaction and status updates. Streaming version of `SendMessage`

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
SubscribeToTask  
---  
` rpc SubscribeToTask(`[SubscribeToTaskRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.SubscribeToTaskRequest)`) returns (`[StreamResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.StreamResponse)`) ` Subscribes to task updates for tasks not in a terminal state. Returns `UnsupportedOperationError` if the task is already in a terminal state (completed, failed, canceled, rejected).

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
  
## APIKeySecurityScheme

Defines a security scheme using an API key.

Fields  
---  
`description` |  `string` An optional description for the security scheme.  
`location` |  `string` Required. The location of the API key. Valid values are "query", "header", or "cookie".  
`name` |  `string` Required. The name of the header, query, or cookie parameter to be used.  
  
## AgentCapabilities

Defines optional capabilities supported by an agent.

Fields  
---  
`extensions[]` |  `[AgentExtension](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.AgentExtension)` A list of protocol extensions supported by the agent.  
`streaming` |  `bool` Indicates if the agent supports streaming responses.  
`push_notifications` |  `bool` Indicates if the agent supports sending push notifications for asynchronous task updates.  
`extended_agent_card` |  `bool` Indicates if the agent supports providing an extended agent card when authenticated.  
  
## AgentCard

A self-describing manifest for an agent. It provides essential metadata including the agent's identity, capabilities, skills, supported communication methods, and security requirements. Next ID: 20

Fields  
---  
`name` |  `string` Required. A human readable name for the agent. Example: "Recipe Agent"  
`description` |  `string` Required. A human-readable description of the agent, assisting users and other agents in understanding its purpose. Example: "Agent that helps users with recipes and cooking."  
`supported_interfaces[]` |  `[AgentInterface](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.AgentInterface)` Required. Ordered list of supported interfaces. The first entry is preferred.  
`provider` |  `[AgentProvider](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.AgentProvider)` The service provider of the agent.  
`version` |  `string` Required. The version of the agent. Example: "1.0.0"  
`capabilities` |  `[AgentCapabilities](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.AgentCapabilities)` Required. A2A Capability set supported by the agent.  
`security_schemes` |  `map<string, `[SecurityScheme](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.SecurityScheme)`>` The security scheme details used for authenticating with this agent.  
`security_requirements[]` |  `[SecurityRequirement](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.SecurityRequirement)` Security requirements for contacting the agent.  
`default_input_modes[]` |  `string` Required. protolint:enable REPEATED_FIELD_NAMES_PLURALIZED The set of interaction modes that the agent supports across all skills. This can be overridden per skill. Defined as media types.  
`default_output_modes[]` |  `string` Required. The media types supported as outputs from this agent.  
`skills[]` |  `[AgentSkill](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.AgentSkill)` Required. Skills represent the abilities of an agent. It is largely a descriptive concept but represents a more focused set of behaviors that the agent is likely to succeed at.  
`signatures[]` |  `[AgentCardSignature](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.AgentCardSignature)` JSON Web Signatures computed for this `AgentCard`.  
`documentation_url` |  `string` A URL providing additional documentation about the agent.  
`icon_url` |  `string` Optional. A URL to an icon for the agent.  
  
## AgentCardSignature

AgentCardSignature represents a JWS signature of an AgentCard. This follows the JSON format of an RFC 7515 JSON Web Signature (JWS).

Fields  
---  
`protected` |  `string` Required. Required. The protected JWS header for the signature. This is always a base64url-encoded JSON object.  
`signature` |  `string` Required. The computed signature, base64url-encoded.  
`header` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` The unprotected JWS header values.  
  
## AgentExtension

A declaration of a protocol extension supported by an Agent.

Fields  
---  
`uri` |  `string` The unique URI identifying the extension.  
`description` |  `string` A human-readable description of how this agent uses the extension.  
`required` |  `bool` If true, the client must understand and comply with the extension's requirements.  
`params` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Optional. Extension-specific configuration parameters.  
  
## AgentInterface

Declares a combination of a target URL, transport and protocol version for interacting with the agent. This allows agents to expose the same functionality over multiple protocol binding mechanisms.

Fields  
---  
`url` |  `string` Required. The URL where this interface is available. Must be a valid absolute HTTPS URL in production. Example: "https://api.example.com/a2a/v1", "https://grpc.example.com/a2a"  
`protocol_binding` |  `string` Required. The protocol binding supported at this URL. This is an open form string, to be easily extended for other protocol bindings. The core ones officially supported are `JSONRPC`, `GRPC` and `HTTP+JSON`.  
`tenant` |  `string` Optional. An opaque string used for routing requests to a specific agent or tenant when multiple agents are served behind a single A2A endpoint. When set, clients MUST include this value in the `tenant` field of all request messages sent to this interface. The server is responsible for interpreting the value and routing requests accordingly; the protocol does not define its format or semantics.  
`protocol_version` |  `string` Required. The version of the A2A protocol this interface exposes. Use the latest supported minor version per major version. Examples: "0.3", "1.0"  
  
## AgentProvider

Represents the service provider of an agent.

Fields  
---  
`url` |  `string` Required. A URL for the agent provider's website or relevant documentation. Example: "https://ai.google.dev"  
`organization` |  `string` Required. The name of the agent provider's organization. Example: "Google"  
  
## AgentSkill

Represents a distinct capability or function that an agent can perform.

Fields  
---  
`id` |  `string` Required. A unique identifier for the agent's skill.  
`name` |  `string` Required. A human-readable name for the skill.  
`description` |  `string` Required. A detailed description of the skill.  
`tags[]` |  `string` Required. A set of keywords describing the skill's capabilities.  
`examples[]` |  `string` Example prompts or scenarios that this skill can handle.  
`input_modes[]` |  `string` The set of supported input media types for this skill, overriding the agent's defaults.  
`output_modes[]` |  `string` The set of supported output media types for this skill, overriding the agent's defaults.  
`security_requirements[]` |  `[SecurityRequirement](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.SecurityRequirement)` Security schemes necessary for this skill.  
  
## Artifact

Artifacts represent task outputs.

Fields  
---  
`artifact_id` |  `string` Required. Unique identifier (e.g. UUID) for the artifact. It must be unique within a task.  
`name` |  `string` A human readable name for the artifact.  
`description` |  `string` Optional. A human readable description of the artifact.  
`parts[]` |  `[Part](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.Part)` Required. The content of the artifact. Must contain at least one part.  
`metadata` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Optional. Metadata included with the artifact.  
`extensions[]` |  `string` The URIs of extensions that are present or contributed to this Artifact.  
  
## AuthenticationInfo

Defines authentication details, used for push notifications.

Fields  
---  
`scheme` |  `string` Required. HTTP Authentication Scheme from the [IANA registry](https://www.iana.org/assignments/http-authschemes/). Examples: `Bearer`, `Basic`, `Digest`. Scheme names are case-insensitive per [RFC 9110 Section 11.1](https://www.rfc-editor.org/rfc/rfc9110#section-11.1).  
`credentials` |  `string` Push Notification credentials. Format depends on the scheme (e.g., token for Bearer).  
  
## AuthorizationCodeOAuthFlow

Defines configuration details for the OAuth 2.0 Authorization Code flow.

Fields  
---  
`authorization_url` |  `string` Required. The authorization URL to be used for this flow.  
`token_url` |  `string` Required. The token URL to be used for this flow.  
`refresh_url` |  `string` The URL to be used for obtaining refresh tokens.  
`scopes` |  `map<string, string>` Required. The available scopes for the OAuth2 security scheme.  
`pkce_required` |  `bool` Indicates if PKCE (RFC 7636) is required for this flow. PKCE should always be used for public clients and is recommended for all clients.  
  
## CancelTaskRequest

Represents a request for the `CancelTask` method.

Fields  
---  
`tenant` |  `string` Optional. Opaque routing identifier. Must match the `tenant` value from the selected `AgentInterface` in the Agent Card when that field is set.  
`id` |  `string` Required. The resource ID of the task to cancel.  
`metadata` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` A flexible key-value map for passing additional context or parameters.  
  
## ClientCredentialsOAuthFlow

Defines configuration details for the OAuth 2.0 Client Credentials flow.

Fields  
---  
`token_url` |  `string` Required. The token URL to be used for this flow.  
`refresh_url` |  `string` The URL to be used for obtaining refresh tokens.  
`scopes` |  `map<string, string>` Required. The available scopes for the OAuth2 security scheme.  
  
## DeleteTaskPushNotificationConfigRequest

Represents a request for the `DeleteTaskPushNotificationConfig` method.

Fields  
---  
`tenant` |  `string` Optional. Opaque routing identifier. Must match the `tenant` value from the selected `AgentInterface` in the Agent Card when that field is set.  
`task_id` |  `string` Required. The parent task resource ID.  
`id` |  `string` Required. The resource ID of the configuration to delete.  
  
## DeviceCodeOAuthFlow

Defines configuration details for the OAuth 2.0 Device Code flow (RFC 8628). This flow is designed for input-constrained devices such as IoT devices, and CLI tools where the user authenticates on a separate device.

Fields  
---  
`device_authorization_url` |  `string` Required. The device authorization endpoint URL.  
`token_url` |  `string` Required. The token URL to be used for this flow.  
`refresh_url` |  `string` The URL to be used for obtaining refresh tokens.  
`scopes` |  `map<string, string>` Required. The available scopes for the OAuth2 security scheme.  
  
## GetExtendedAgentCardRequest

Represents a request for the `GetExtendedAgentCard` method.

Fields  
---  
`tenant` |  `string` Optional. Opaque routing identifier. Must match the `tenant` value from the selected `AgentInterface` in the Agent Card when that field is set.  
  
## GetTaskPushNotificationConfigRequest

Represents a request for the `GetTaskPushNotificationConfig` method.

Fields  
---  
`tenant` |  `string` Optional. Opaque routing identifier. Must match the `tenant` value from the selected `AgentInterface` in the Agent Card when that field is set.  
`task_id` |  `string` Required. The parent task resource ID.  
`id` |  `string` Required. The resource ID of the configuration to retrieve.  
  
## GetTaskRequest

Represents a request for the `GetTask` method.

Fields  
---  
`tenant` |  `string` Optional. Opaque routing identifier. Must match the `tenant` value from the selected `AgentInterface` in the Agent Card when that field is set.  
`id` |  `string` Required. The resource ID of the task to retrieve.  
`history_length` |  `int32` The maximum number of most recent messages from the task's history to retrieve. An unset value means the client does not impose any limit. A value of zero is a request to not include any messages. The server MUST NOT return more messages than the provided value, but MAY apply a lower limit.  
  
## HTTPAuthSecurityScheme

Defines a security scheme using HTTP authentication.

Fields  
---  
`description` |  `string` An optional description for the security scheme.  
`scheme` |  `string` Required. The name of the HTTP Authentication scheme to be used in the Authorization header, as defined in RFC7235 (e.g., "Bearer"). This value should be registered in the IANA Authentication Scheme registry.  
`bearer_format` |  `string` A hint to the client to identify how the bearer token is formatted (e.g., "JWT"). Primarily for documentation purposes.  
  
## ImplicitOAuthFlow

Deprecated: Use Authorization Code + PKCE instead.

Fields  
---  
`authorization_url` |  `string` The authorization URL to be used for this flow. This MUST be in the form of a URL. The OAuth2 standard requires the use of TLS  
`refresh_url` |  `string` The URL to be used for obtaining refresh tokens. This MUST be in the form of a URL. The OAuth2 standard requires the use of TLS.  
`scopes` |  `map<string, string>` The available scopes for the OAuth2 security scheme. A map between the scope name and a short description for it. The map MAY be empty.  
  
## ListTaskPushNotificationConfigsRequest

Represents a request for the `ListTaskPushNotificationConfigs` method.

Fields  
---  
`tenant` |  `string` Optional. Opaque routing identifier. Must match the `tenant` value from the selected `AgentInterface` in the Agent Card when that field is set.  
`task_id` |  `string` Required. The parent task resource ID.  
`page_size` |  `int32` The maximum number of configurations to return.  
`page_token` |  `string` A page token received from a previous `ListTaskPushNotificationConfigsRequest` call.  
  
## ListTaskPushNotificationConfigsResponse

Represents a successful response for the `ListTaskPushNotificationConfigs` method.

Fields  
---  
`configs[]` |  `[TaskPushNotificationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.TaskPushNotificationConfig)` The list of push notification configurations.  
`next_page_token` |  `string` A token to retrieve the next page of results, or empty if there are no more results in the list.  
  
## ListTasksRequest

Parameters for listing tasks with optional filtering criteria.

Fields  
---  
`tenant` |  `string` Optional. Opaque routing identifier. Must match the `tenant` value from the selected `AgentInterface` in the Agent Card when that field is set.  
`context_id` |  `string` Filter tasks by context ID to get tasks from a specific conversation or session.  
`status` |  `[TaskState](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.TaskState)` Filter tasks by their current status state.  
`page_token` |  `string` A page token, received from a previous `ListTasks` call. `ListTasksResponse.next_page_token`. Provide this to retrieve the subsequent page.  
`status_timestamp_after` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Filter tasks which have a status updated after the provided timestamp in ISO 8601 format (e.g., "2023-10-27T10:00:00Z"). Only tasks with a status timestamp time greater than or equal to this value will be returned.  
`page_size` |  `int32` The maximum number of tasks to return. The service may return fewer than this value. If unspecified, at most 50 tasks will be returned. The minimum value is 1. The maximum value is 100.  
`history_length` |  `int32` The maximum number of messages to include in each task's history.  
`include_artifacts` |  `bool` Whether to include artifacts in the returned tasks. Defaults to false to reduce payload size.  
  
## ListTasksResponse

Result object for `ListTasks` method containing an array of tasks and pagination information.

Fields  
---  
`tasks[]` |  `[Task](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.Task)` Required. Array of tasks matching the specified criteria.  
`next_page_token` |  `string` Required. A token to retrieve the next page of results, or empty if there are no more results in the list.  
`page_size` |  `int32` Required. The page size used for this response.  
`total_size` |  `int32` Required. Total number of tasks available (before pagination).  
  
## Message

`Message` is one unit of communication between client and server. It can be associated with a context and/or a task. For server messages, `context_id` must be provided, and `task_id` only if a task was created. For client messages, both fields are optional, with the caveat that if both are provided, they have to match (the `context_id` has to be the one that is set on the task). If only `task_id` is provided, the server will infer `context_id` from it.

Fields  
---  
`message_id` |  `string` Required. The unique identifier (e.g. UUID) of the message. This is created by the message creator.  
`context_id` |  `string` Optional. The context id of the message. If set, the message will be associated with the given context.  
`task_id` |  `string` Optional. The task id of the message. If set, the message will be associated with the given task.  
`role` |  `[Role](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.Role)` Required. Identifies the sender of the message.  
`parts[]` |  `[Part](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.Part)` Required. Parts is the container of the message content.  
`metadata` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Optional. Any metadata to provide along with the message.  
`extensions[]` |  `string` The URIs of extensions that are present or contributed to this Message.  
`reference_task_ids[]` |  `string` A list of task IDs that this message references for additional context.  
  
## MutualTlsSecurityScheme

Defines a security scheme using mTLS authentication.

Fields  
---  
`description` |  `string` An optional description for the security scheme.  
  
## OAuth2SecurityScheme

Defines a security scheme using OAuth 2.0.

Fields  
---  
`description` |  `string` An optional description for the security scheme.  
`flows` |  `[OAuthFlows](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.OAuthFlows)` Required. An object containing configuration information for the supported OAuth 2.0 flows.  
`oauth2_metadata_url` |  `string` URL to the OAuth2 authorization server metadata [RFC 8414](https://datatracker.ietf.org/doc/html/rfc8414). TLS is required.  
  
## OAuthFlows

Defines the configuration for the supported OAuth 2.0 flows.

Fields  
---  
Union field `flow`.`flow` can be only one of the following:  
`authorization_code` |  `[AuthorizationCodeOAuthFlow](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.AuthorizationCodeOAuthFlow)` Configuration for the OAuth Authorization Code flow.  
`client_credentials` |  `[ClientCredentialsOAuthFlow](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.ClientCredentialsOAuthFlow)` Configuration for the OAuth Client Credentials flow.  
`implicit  
**(deprecated)**` |  `[ImplicitOAuthFlow](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.ImplicitOAuthFlow)` This item is deprecated!Deprecated: Use Authorization Code + PKCE instead.  
`password  
**(deprecated)**` |  `[PasswordOAuthFlow](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.PasswordOAuthFlow)` This item is deprecated!Deprecated: Use Authorization Code + PKCE or Device Code.  
`device_code` |  `[DeviceCodeOAuthFlow](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.DeviceCodeOAuthFlow)` Configuration for the OAuth Device Code flow.  
  
## OpenIdConnectSecurityScheme

Defines a security scheme using OpenID Connect.

Fields  
---  
`description` |  `string` An optional description for the security scheme.  
`open_id_connect_url` |  `string` Required. The [OpenID Connect Discovery URL](https://openid.net/specs/openid-connect-discovery-1_0.html) for the OIDC provider's metadata.  
  
## Part

`Part` represents a container for a section of communication content. Parts can be purely textual, some sort of file (image, video, etc) or a structured data blob (i.e. JSON).

Fields  
---  
`metadata` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Optional. metadata associated with this part.  
`filename` |  `string` An optional `filename` for the file (e.g., "document.pdf").  
`media_type` |  `string` The `media_type` (MIME type) of the part content (e.g., "text/plain", "application/json", "image/png"). This field is available for all part types.  
Union field `content`.`content` can be only one of the following:  
`text` |  `string` The string content of the `text` part.  
`raw` |  `bytes` The `raw` byte content of a file. In JSON serialization, this is encoded as a base64 string.  
`url` |  `string` A `url` pointing to the file's content.  
`data` |  `[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` Arbitrary structured `data` as a JSON value (object, array, string, number, boolean, or null).  
  
## PasswordOAuthFlow

Deprecated: Use Authorization Code + PKCE or Device Code.

Fields  
---  
`token_url` |  `string` The token URL to be used for this flow. This MUST be in the form of a URL. The OAuth2 standard requires the use of TLS.  
`refresh_url` |  `string` The URL to be used for obtaining refresh tokens. This MUST be in the form of a URL. The OAuth2 standard requires the use of TLS.  
`scopes` |  `map<string, string>` The available scopes for the OAuth2 security scheme. A map between the scope name and a short description for it. The map MAY be empty.  
  
## Role

Defines the sender of a message in A2A protocol communication.

Enums  
---  
`ROLE_UNSPECIFIED` | The role is unspecified.  
`ROLE_USER` | The message is from the client to the server.  
`ROLE_AGENT` | The message is from the server to the client.  
  
## SecurityRequirement

Defines the security requirements for an agent.

Fields  
---  
`schemes` |  `map<string, `[StringList](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.StringList)`>` A map of security schemes to the required scopes.  
  
## SecurityScheme

Defines a security scheme that can be used to secure an agent's endpoints. This is a discriminated union type based on the OpenAPI 3.2 Security Scheme Object. See: <https://spec.openapis.org/oas/v3.2.0.html#security-scheme-object>

Fields  
---  
Union field `scheme`.`scheme` can be only one of the following:  
`api_key_security_scheme` |  `[APIKeySecurityScheme](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.APIKeySecurityScheme)` API key-based authentication.  
`http_auth_security_scheme` |  `[HTTPAuthSecurityScheme](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.HTTPAuthSecurityScheme)` HTTP authentication (Basic, Bearer, etc.).  
`oauth2_security_scheme` |  `[OAuth2SecurityScheme](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.OAuth2SecurityScheme)` OAuth 2.0 authentication.  
`open_id_connect_security_scheme` |  `[OpenIdConnectSecurityScheme](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.OpenIdConnectSecurityScheme)` OpenID Connect authentication.  
`mtls_security_scheme` |  `[MutualTlsSecurityScheme](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.MutualTlsSecurityScheme)` Mutual TLS authentication.  
  
## SendMessageConfiguration

Configuration of a send message request.

Fields  
---  
`accepted_output_modes[]` |  `string` A list of media types the client is prepared to accept for response parts. Agents SHOULD use this to tailor their output.  
`task_push_notification_config` |  `[TaskPushNotificationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.TaskPushNotificationConfig)` Configuration for the agent to send push notifications for task updates. Task id should be empty when sending this configuration in a `SendMessage` request.  
`return_immediately` |  `bool` If `true`, the operation returns immediately after creating the task, even if processing is still in progress. If `false` (default), the operation MUST wait until the task reaches a terminal (`COMPLETED`, `FAILED`, `CANCELED`, `REJECTED`) or interrupted (`INPUT_REQUIRED`, `AUTH_REQUIRED`) state before returning.  
`history_length` |  `int32` The maximum number of most recent messages from the task's history to retrieve in the response. An unset value means the client does not impose any limit. A value of zero is a request to not include any messages. The server MUST NOT return more messages than the provided value, but MAY apply a lower limit.  
  
## SendMessageRequest

Represents a request for the `SendMessage` method.

Fields  
---  
`tenant` |  `string` Optional. Opaque routing identifier. Must match the `tenant` value from the selected `AgentInterface` in the Agent Card when that field is set.  
`message` |  `[Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.Message)` Required. The message to send to the agent.  
`configuration` |  `[SendMessageConfiguration](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.SendMessageConfiguration)` Configuration for the send request.  
`metadata` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` A flexible key-value map for passing additional context or parameters.  
  
## SendMessageResponse

Represents the response for the `SendMessage` method.

Fields  
---  
Union field `payload`. The payload of the response. `payload` can be only one of the following:  
`task` |  `[Task](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.Task)` The task created or updated by the message.  
`message` |  `[Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.Message)` A message from the agent.  
  
## StreamResponse

A wrapper object used in streaming operations to encapsulate different types of response data.

Fields  
---  
Union field `payload`. The payload of the stream response. `payload` can be only one of the following:  
`task` |  `[Task](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.Task)` A Task object containing the current state of the task.  
`message` |  `[Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.Message)` A Message object containing a message from the agent.  
`status_update` |  `[TaskStatusUpdateEvent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.TaskStatusUpdateEvent)` An event indicating a task status update.  
`artifact_update` |  `[TaskArtifactUpdateEvent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.TaskArtifactUpdateEvent)` An event indicating a task artifact update.  
  
## StringList

protolint:disable REPEATED_FIELD_NAMES_PLURALIZED A list of strings.

Fields  
---  
`list[]` |  `string` The individual string values.  
  
## SubscribeToTaskRequest

Represents a request for the `SubscribeToTask` method.

Fields  
---  
`tenant` |  `string` Optional. Opaque routing identifier. Must match the `tenant` value from the selected `AgentInterface` in the Agent Card when that field is set.  
`id` |  `string` Required. The resource ID of the task to subscribe to.  
  
## Task

`Task` is the core unit of action for A2A. It has a current status and when results are created for the task they are stored in the artifact. If there are multiple turns for a task, these are stored in history.

Fields  
---  
`id` |  `string` Required. Unique identifier (e.g. UUID) for the task, generated by the server for a new task.  
`context_id` |  `string` Unique identifier (e.g. UUID) for the contextual collection of interactions (tasks and messages).  
`status` |  `[TaskStatus](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.TaskStatus)` Required. The current status of a `Task`, including `state` and a `message`.  
`artifacts[]` |  `[Artifact](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.Artifact)` A set of output artifacts for a `Task`.  
`history[]` |  `[Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.Message)` protolint:disable REPEATED_FIELD_NAMES_PLURALIZED The history of interactions from a `Task`.  
`metadata` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` protolint:enable REPEATED_FIELD_NAMES_PLURALIZED A key/value object to store custom metadata about a task.  
  
## TaskArtifactUpdateEvent

A task delta where an artifact has been generated.

Fields  
---  
`task_id` |  `string` Required. The ID of the task for this artifact.  
`context_id` |  `string` Required. The ID of the context that this task belongs to.  
`artifact` |  `[Artifact](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.Artifact)` Required. The artifact that was generated or updated.  
`append` |  `bool` If true, the content of this artifact should be appended to a previously sent artifact with the same ID.  
`last_chunk` |  `bool` If true, this is the final chunk of the artifact.  
`metadata` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Optional. Metadata associated with the artifact update.  
  
## TaskPushNotificationConfig

A container associating a push notification configuration with a specific task.

Fields  
---  
`tenant` |  `string` Optional. Opaque routing identifier. Must match the `tenant` value from the selected `AgentInterface` in the Agent Card when that field is set.  
`id` |  `string` The push notification configuration details. A unique identifier (e.g. UUID) for this push notification configuration.  
`task_id` |  `string` The ID of the task this configuration is associated with.  
`url` |  `string` Required. The URL where the notification should be sent.  
`token` |  `string` A token unique for this task or session.  
`authentication` |  `[AuthenticationInfo](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.AuthenticationInfo)` Authentication information required to send the notification.  
  
## TaskState

Defines the possible lifecycle states of a `Task`.

Enums  
---  
`TASK_STATE_UNSPECIFIED` | The task is in an unknown or indeterminate state.  
`TASK_STATE_SUBMITTED` | Indicates that a task has been successfully submitted and acknowledged.  
`TASK_STATE_WORKING` | Indicates that a task is actively being processed by the agent.  
`TASK_STATE_COMPLETED` | Indicates that a task has finished successfully. This is a terminal state.  
`TASK_STATE_FAILED` | Indicates that a task has finished with an error. This is a terminal state.  
`TASK_STATE_CANCELED` | Indicates that a task was canceled before completion. This is a terminal state.  
`TASK_STATE_INPUT_REQUIRED` | Indicates that the agent requires additional user input to proceed. This is an interrupted state.  
`TASK_STATE_REJECTED` | Indicates that the agent has decided to not perform the task. This may be done during initial task creation or later once an agent has determined it can't or won't proceed. This is a terminal state.  
`TASK_STATE_AUTH_REQUIRED` | Indicates that authentication is required to proceed. This is an interrupted state.  
  
## TaskStatus

A container for the status of a task

Fields  
---  
`state` |  `[TaskState](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.TaskState)` Required. The current state of this task.  
`message` |  `[Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.Message)` A message associated with the status.  
`timestamp` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` ISO 8601 Timestamp when the status was recorded. Example: "2023-10-27T10:00:00Z"  
  
## TaskStatusUpdateEvent

An event sent by the agent to notify the client of a change in a task's status.

Fields  
---  
`task_id` |  `string` Required. The ID of the task that has changed.  
`context_id` |  `string` Required. The ID of the context that the task belongs to.  
`status` |  `[TaskStatus](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/lf.a2a.v1#lf.a2a.v1.TaskStatus)` Required. The new status of the task.  
`metadata` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Optional. Metadata associated with the task update.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-25 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-25 UTC."],[],[]] 
