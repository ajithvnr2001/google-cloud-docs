---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/policies/iam-overview-uap/
title: IAM Unified Access Policies overview \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:42:53.658138+00:00
---

# IAM Unified Access Policies overview  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/policies/iam-overview-uap/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Agents ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents)



Send feedback 

#  IAM Unified Access Policies overview Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This feature does not support VPC Service Controls.

You can create Identity and Access Management (IAM) Unified Access Policies (UAPs) to help securely govern communication between _agent principals_ and _destination resources_ , such as destination agents, MCP servers, and endpoints. These policies are bound to the project that contains your Agent Gateway instances.

Agent Gateway uses Identity-Aware Proxy (IAP) to evaluate and enforce the UAPs.

IAP also integrates with Context-Aware Access to provide end-to-end agent identity authentication and authorization.

To set up UAPs for Agent Gateway, see [Configure IAM UAPs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/policies/configure-iam-policies-uap).

You can also create a Principal Access Boundary (PAB) on the agent identity. Agent Gateway can use IAP to enforce Principal Access Boundary policies.

## Enable Agent Gateway

To use agentic communication policies, you must [set up Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/set-up-agent-gateway).

We recommend that you configure Agent Gateway in dry-run mode (`DRY_RUN`) in a staging environment to verify that your policies are working as expected.

**Important:** In dry-run mode, IAP logs disallowed agentic communications to Cloud Audit Logs but doesn't block them.

When you are satisfied that the policies are functioning correctly, you can update the Agent Gateway configuration to set enforcement mode to `ENFORCE`. In this mode, agentic communications that violate the policy are disallowed and communication to the resource is blocked.

## UAPs overview

UAPs control whether one or more agent principals can access one or more destination resources. UAPs extend the IAM policy model by supporting multiple _rules_ in a single policy. Unlike IAM allow policies and deny policies, each rule in a UAP can have both an allow effect and a deny effect. Learn more about [IAM policy types](https://docs.cloud.google.com/iam/docs/policy-types).

Rules also contain _conditions_ that are expressed in Common Expression Language (CEL). Conditions act as the primary mechanism to control access to post-gateway resources. Enforcing UAPs with Agent Gateway and IAP delivers strict behavioral control over agents deployed across your enterprise. You can represent real-world, fine-grained agent governance use cases in a single policy.

A typical policy contains at least two distinct rules:

  * **Allow rule:** Allow rules have an allow effect that lets agent principals access specific, safe operations, such as performing a read operation on a tool to fetch tracking data or view registry entries.
  * **Deny rule:** Deny rules have a deny effect that disallows the agent from executing unwanted actions, such as performing an uncommanded delete or update operation on a critical resource.



For example, consider an automated customer support agent that needs to interact with internal tools that have privileged access to a customer database. The administrator configures an Agent Gateway with IAP to enforce IAM UAPs. The administrator can configure a UAP with an allow rule that authorizes the agent principal to read support tickets, and a deny rule that disallows the agent principal from deleting or updating database records.

By using UAPs that contain both allow and deny rules, organizations can deploy a single corporate compliance policy directly onto underlying cloud infrastructure to constrain agent behavior.

## Best practices

Follow these best practices when you configure agent egress policies:

  * **Use dry-run mode:** Deploy new or modified policies in dry-run mode first to make sure that your policy works as expected, without blocking active agent traffic.
  * **Apply the principle of least privilege:** Grant only necessary permissions. Use specific tool names or paths in CEL conditions rather than wildcards.
  * **Use deny rules for guardrails:** Use explicit deny rules to implement critical guardrails, such as blocking destructive tools on production endpoints. Using deny rules for guardrails is effective because deny rules override allow rules.
  * **Perform regular audits:** Periodically review Cloud Audit Logs logs and policy configurations to verify that they comply with your organization's security policies.



## UAP components

UAPs contain one or more rules. Rules have the following components:

### Agent principals

In your IAM UAPs, you define one or more agent principals. Agent principals are the members that you grant access to. You specify agents by their agent identity, the identity of the agent initiating communication with a resource. For more information about how different types of agents receive identities, see [Agent identity](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/agent-identity). Agent identities are represented by [principal identifiers](https://docs.cloud.google.com/iam/docs/principal-identifiers) that contain the SPIFFE-formatted identity of the agent (for example, `principal://agents.global.org-...`).

**Important:** Agent identifiers in URN format, such as `urn:agent:...`, are used solely for inventory and catalog lookup and are not used in IAM policy bindings.

You can specify an array of individual agent identities or an array of principal sets.

Built-in agent identities are provisioned across Google Cloud services such as Agent Runtime (Reasoning Engine), Gemini Enterprise (Discovery Engine), and Cloud Run services configured with agent identity. These agent principals take the form `principal://TRUST_DOMAIN/AGENT_UNIQUE_IDENTIFIER`, where the identifier represents the resource path of the agent on its hosting service. You can also specify agents using Workload Identity Federation principal identifiers.

### Rule effect

The rule effect defines whether the rule allows or disallows agent principals from accessing a resource.

### Destination resources

IAM UAPs manage access from agent principals to destination resources. Destination resources are the resources that agent principals are trying to access. Destination resources are specified in the rule conditions. Destination resources can be either registered resources or unregistered resources.

#### Registered resources

Registered resources are resources that are registered in an Agent Registry registry.

Registered resources include the following:

  * Registries: Entire agent registries within a project.
  * MCP servers: MCP servers that are registered in an agent registry.
  * Agents: Agents that are registered in an agent registry. Individual agents can be specified individually by their agent identity. A group of agents can be specified by a principal set identifier.
  * Endpoints: Endpoints that are registered in an agent registry.



Individual services can be registered in Agent Registry. If you regionalize your agent registries and your rule manages access to registered resources, then your UAPs applies only to the resources that are in the registry's region.

#### Unregistered resources

Unregistered resources are resources that are not registered in an agent registry. To grant or deny access to unregistered resources in your UAP rules, you must specify unregistered resources in your rule conditions by using Common Expression Language (CEL) expressions that contain [unregistered host and path attributes](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/policies/cel-attributes-uap#unregistered-destination).

### Conditions

In UAPs rules, you use Common Expression Language (CEL) expressions in the `conditions` block to define both **target resource scope** and **fine-grained access criteria** :

  * **Target resource scope** : Identifies _which_ destination resources the rule governs. In JSON-formatted policy files, you specify destination attributes, such as `destination.agent_registry.mcp_server.name` or `destination.unregistered.host`. In the Google Cloud console, selecting destinations under **Target resources** automatically adds these resource criteria to the rule's condition expression.

  * **Access criteria** : Use a Boolean expression to determine _when_ and _under what constraints_ the rule effect applies. For example, you can restrict access based on tool names, read-only status, HTTP methods, or path prefixes using UAP CEL attributes. The rule effect (allow or deny) takes effect only when the entire CEL expression evaluates to `true`.




In the gcloud CLI and REST API, you specify these CEL expressions in the `conditions` field of the rule definition.

In the Google Cloud console, you can configure standard rules by using the **Condition builder** , or write custom CEL expressions directly in the **Condition editor**.

### Permissions

In IAP V2 with IAM UAPs, the `iap.googleapis.com/resources.egressViaIAP` permission is always granted on the destination resource. In the gcloud CLI and REST API, you specify the permission in the `operation.permissions` field of your policy file.

## Policy creation options

In the **Policies** page in the Google Cloud console, you can create IAM UAPs. We recommend that you create only [UAPs (IAM v3 policies)](https://docs.cloud.google.com/iam/docs/policy-types).

In both the gcloud CLI and the REST API, you can configure IAM UAPs by first creating a JSON-formatted file. We recommend that you create only UAPs.

## End-to-end authentication and authorization

IAP and Context-Aware Access provide default end-to-end agent identity authentication and authorization by using the following protocols:

  * Mutual TLS (mTLS)
  * Demonstrating Proof of Possession (DPoP)



Agent identities are provisioned with an X.509 certificate and a certificate-bound token. IAP enforces that agent identities use mutual TLS (mTLS) to authenticate to Agent Gateway. When the gateway allows the agent to egress and access Google Cloud APIs, MCP servers, other agents, and endpoints, the agent attempts access outside of the mTLS boundary. To help protect communication, Context-Aware Access enforces a Google-managed Context-Aware Access policy. The policy requires DPoP to validate the certificate-bound token that is bound to the agent identity. For more information about how Context-Aware Access uses mTLS and DPoP, see [Context-Aware Access agent security](https://docs.cloud.google.com/access-context-manager/docs/caa-agent-security).

## UAP CEL attributes

In your UAPs, you can define conditions with conditional expressions. The expressions can contain multiple sub-expressions. The destination resource type that you use in each relational sub-condition determines which attributes you can use.

For example, in the following condition, in the sub-expression `destination.unregistered.path.startsWith('/v1/statements')`, the resource type is an unregistered destination, the attribute is `destination.unregistered.path`, and `startsWith()` is the CEL function.
    
    
    destination.unregistered.host == 'finance.example.com' &&
    destination.unregistered.path.startsWith('/v1/statements')
    

The attributes described in the following table are available for each resource type:

Destination resource type | Attribute | Details  
---|---|---  
  
### Agent Registry

| `destination.is_registered` |  | Value type | Boolean  
---|---  
Supported values | `true`, `false`  
Supported operations | `==`, `!=`  
`destination.agent_registry.resource_type` |  | Value type | String  
---|---  
Supported values |  `'AGENT'`, `'ENDPOINT'`, `'MCP_SERVER'`, `'SKILL'`  
Supported operations |  `==`, `!=`, `in`  
`destination.agent_registry.location` |  | Value type | String  
---|---  
Supported values |  Google Cloud location ID (for example, `'global'`, `'us-central1'`)   
Supported operations |  `==`, `!=`, `in`  
`destination.agent_registry.project_id` |  | Value type | String  
---|---  
Supported values | Google Cloud project ID  
Supported operations |  `==`, `!=`, `in`  
  
### Agent

| `destination.agent_registry.agent.name` |  | Value type | String  
---|---  
Supported values |  Agent resource name (`projects/PROJECT_ID/locations/LOCATION/agents/AGENT_NAME`)   
Supported operations |  `==`, `!=`, `in`  
  
### MCP Server

| `destination.agent_registry.mcp_server.name` |  | Value type | String  
---|---  
Supported values |  MCP server resource name (`projects/PROJECT_ID/locations/LOCATION/mcpServers/MCP_SERVER_NAME`)   
Supported operations |  `==`, `!=`, `in`  
`destination.agent_registry.mcp_server.method` |  | Value type | String  
---|---  
Supported values |  MCP method name (for example, `'tools'`, `'prompts'`, `'resources'`)   
Supported operations |  `==`, `!=`, `in`  
`destination.agent_registry.mcp_server.tool.name` |  | Value type | String  
---|---  
Supported values |  Tool name (for example, `'search_code'`, `'execute'`)   
Supported operations |  `==`, `!=`, `in`  
`destination.agent_registry.mcp_server.tool.annotations.read_only_hint` |  | Value type | Boolean  
---|---  
Supported values | `true`, `false`  
Supported operations | `==`, `!=`  
`destination.agent_registry.mcp_server.tool.annotations.destructive_hint` |  | Value type | Boolean  
---|---  
Supported values | `true`, `false`  
Supported operations | `==`, `!=`  
`destination.agent_registry.mcp_server.tool.annotations.idempotent_hint` |  | Value type | Boolean  
---|---  
Supported values | `true`, `false`  
Supported operations | `==`, `!=`  
`destination.agent_registry.mcp_server.tool.annotations.open_world_hint` |  | Value type | Boolean  
---|---  
Supported values | `true`, `false`  
Supported operations | `==`, `!=`  
`destination.agent_registry.mcp_server.prompt.name` |  | Value type | String  
---|---  
Supported values | Prompt name  
Supported operations |  `==`, `!=`, `in`  
`destination.agent_registry.mcp_server.resource.name` |  | Value type | String  
---|---  
Supported values | Resource name  
Supported operations |  `==`, `!=`, `in`  
  
### Endpoint

| `destination.agent_registry.endpoint.name` |  | Value type | String  
---|---  
Supported values |  Endpoint resource name (`projects/PROJECT_ID/locations/LOCATION/endpoints/ENDPOINT_NAME`)   
Supported operations |  `==`, `!=`, `in`  
  
### Unregistered Destination

| `destination.unregistered.host` |  | Value type | String  
---|---  
Supported values |  Hostname (for example, `'google.com'`, `'example.com'`)   
Supported operations |  `==`, `!=`, `in`, `.startsWith()`, `.endsWith()`, `.contains()`  
`destination.unregistered.path` |  | Value type | String  
---|---  
Supported values |  Request path (for example, `'/admin'`, `'/api/v1'`)   
Supported operations |  `==`, `!=`, `in`, `.startsWith()`, `.endsWith()`, `.contains()`  
`destination.unregistered.method` |  | Value type | String  
---|---  
Supported values |  HTTP method (for example, `'get'`, `'post'`, `'put'`, `'delete'`)   
Supported operations |  `==`, `!=`, `in`  
  
**Note:** The `startsWith()`, `endsWith()`, and `contains()` functions (or `STARTS_WITH`, `ENDS_WITH`, and `CONTAINS`) are supported only for the `destination.unregistered.host` and `destination.unregistered.path` attributes. Other attributes don't support these string functions.

## What's next

  * [CEL attributes for UAPs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/policies/cel-attributes-uap)
  * [Create IAM UAPs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/policies/configure-iam-policies-uap)
  * [Manage IAM UAPs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/policies/manage-iam-policies-uap)
  * [Troubleshoot IAM UAPs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/troubleshooting/troubleshoot-iam-policies-uap)



Codelab 

###  [ Codelab: Secure cross-cloud agentic AI applications ](https://codelabs.developers.google.com/next26/aiinfra-learning-pod/screen1-securing-cross-cloud-agentic)

Learn how to secure your agentic applications in the Securing Cross-Cloud Agentic AI Applications codelab. 

Overview 

###  [ Agent Gateway overview ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview)

Get an overview of Agent Gateway. 

Guide 

###  [ Security controls ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/security-controls)

Learn about security controls for Google Agent Platform. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
