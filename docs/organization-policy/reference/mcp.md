---
url: https://docs.cloud.google.com/organization-policy/reference/mcp/
title: MCP Reference: orgpolicy.googleapis.com \u00a0|\u00a0 Organization Policy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:00:43.627564+00:00
---

# MCP Reference: orgpolicy.googleapis.com  |  Organization Policy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/organization-policy/reference/mcp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Organization Policy ](https://docs.cloud.google.com/organization-policy)
  * [ Reference ](https://docs.cloud.google.com/organization-policy/apis)



Send feedback 

#  MCP Reference: orgpolicy.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

Organization Policy MCP Server provides tools to discover, manage, and audit organization policies and custom constraints across Google Cloud resources.

A [Model Context Protocol (MCP) server](https://modelcontextprotocol.io/docs/learn/server-concepts) acts as a proxy between an external service that provides context, data, or capabilities to a Large Language Model (LLM) or AI application. MCP servers connect AI applications to external systems such as databases and web services, translating their responses into a format that the AI application can understand.

### Server Setup

You must [enable MCP servers](https://docs.cloud.google.com/mcp/enable-disable-mcp-servers) and [set up authentication](https://docs.cloud.google.com/mcp/authenticate-mcp) before use. For more information about using Google and Google Cloud remote MCP servers, see [Google Cloud MCP servers overview](https://docs.cloud.google.com/mcp/overview). 

### Server Endpoints

An MCP service endpoint is the network address and communication interface (usually a URL) of the MCP server that an AI application (the Host for the MCP client) uses to establish a secure, standardized connection. It is the point of contact for the LLM to request context, call a tool, or access a resource. Google MCP endpoints can be global or regional.

The Organization Policy API MCP server has the following global MCP endpoint:

  * https://orgpolicy.googleapis.com/mcp



## MCP Tools

An [MCP tool](https://modelcontextprotocol.io/legacy/concepts/tools) is a function or executable capability that an MCP server exposes to a LLM or AI application to perform an action in the real world.

### Tools

The orgpolicy.googleapis.com MCP server has the following tools:

MCP Tools  
---  
`[ListConstraints](https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/ListConstraints)` |  Lists constraints that can be applied to a specific resource (project, folder, or organization). Use this to discover what constraints are available to enforce.   
`[ListPolicies](https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/ListPolicies)` |  Retrieves all explicit policies set on a particular resource. Useful for auditing what policies are directly applied.   
`[GetPolicy](https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/GetPolicy)` |  Gets a specific policy on a resource by name. Returns the policy details if set.   
`[GetEffectivePolicy](https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/GetEffectivePolicy)` |  Gets the final, evaluated policy on a resource, taking into account inheritance from parent resources and conditions. Use this to see the actual enforcement state.   
`[CreatePolicy](https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/CreatePolicy)` |  Creates a new policy on a resource to enforce specific constraints.   
`[UpdatePolicy](https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/UpdatePolicy)` |  Updates an existing policy on a resource. Note that this performs a full overwrite of the policy.   
`[DeletePolicy](https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/DeletePolicy)` |  Deletes a policy from a resource, causing it to inherit policies from its parent or revert to the default constraint behavior.   
`[CreateCustomConstraint](https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/CreateCustomConstraint)` |  Creates a new custom constraint for an organization, allowing for fine-grained resource restriction using CEL.   
`[UpdateCustomConstraint](https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/UpdateCustomConstraint)` |  Updates an existing custom constraint. Note that this performs a full overwrite.   
`[GetCustomConstraint](https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/GetCustomConstraint)` |  Gets the definition of a custom or managed constraint by name.   
`[ListCustomConstraints](https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/ListCustomConstraints)` |  Lists all custom constraints defined for an organization.   
`[DeleteCustomConstraint](https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/DeleteCustomConstraint)` |  Deletes a custom constraint from an organization.   
  
### Get MCP tool specifications

To get the MCP tool specifications for all tools in an MCP server, use the `tools/list` method. The following example demonstrates how to use `curl` to list all tools and their specifications currently available within the MCP server. 

Curl Request  
---  
      
    
    curl --location 'https://orgpolicy.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
        "method": "tools/list",
        "jsonrpc": "2.0",
        "id": 1
    }'  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-18 UTC."],[],[]] 
