---
url: https://docs.cloud.google.com/mcp/mcp-gcp-stability-commitment/
title: Google Cloud MCP servers stability commitment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:07:35.351732+00:00
---

# Google Cloud MCP servers stability commitment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/mcp/mcp-gcp-stability-commitment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud APIs ](https://docs.cloud.google.com/apis/docs/overview)
  * [ Google Cloud MCP servers ](https://docs.cloud.google.com/mcp)
  * [ Resources ](https://docs.cloud.google.com/mcp/resources)



Send feedback 

#  Google Cloud MCP servers stability commitment Stay organized with collections  Save and categorize content based on your preferences. 

This policy outlines the Google Cloud stability commitments for Google and Google Cloud remote Model Context Protocol (MCP) servers.

When you use a local MCP server, the set of MCP tools doesn't change unless you explicitly update the local MCP server. When you use a remote MCP server, the producers of the remote MCP server can update prompts, resources, or tools at any time. The MCP client can discover new tools or added functionality, which can result in different behavior for similar prompts.

## Stability commitments and user responsibility

The following table explains the stability commitments Google Cloud makes and the assumptions and responsibilities you should adhere to when integrating with Google and Google Cloud remote MCP servers.

Additional terms may apply to the data generated or used by a specific MCP server.

Google and Google Cloud remote MCP server component | Policy  
---|---  
MCP endpoint | The URL used to access a Google or Google Cloud remote MCP server, for example, `bigquery.googleapis.com/mcp`, follows the [Google Cloud terms of service](https://cloud.google.com/terms). The Google Cloud terms of service includes policies for mandatory notice to users for changes or discontinuation of services.  
MCP server objects and capabilities | Google or Google Cloud remote MCP server objects, for example, tools, prompts, and resources, can be added or removed from MCP servers at any time and without warning.  
Tools, parameters, descriptions, or outputs | The names, structure, descriptions, and required parameters of available Google or Google Cloud remote MCP server tools and functions can be altered, refined, or removed at any time and without warning.  
Non-deterministic output | Some Google or Google Cloud remote MCP server tools, prompts, or other MCP objects can change content and formatting of the output between invocations. You shouldn't assume strict repeatability of results.  
  
## Understand how changes can impact AI applications

Remote MCP servers can be dynamically updated by their producers. Google and Google Cloud remote MCP servers keep the same MCP endpoint URL, but might update tools, tool names, parameters, or tool descriptions without warning. The following list contains some examples of how these dynamic changes can impact AI applications:

  * **Tool additions or removals** : When remote MCP server producers add or remove tools, it can change how an agent performs.
  * **Tool renaming** : When remote MCP server producers change tool names, it can cause issues with client-side allowlists or denylists that rely on tool names.
  * **Parameter changes** : If a required parameter is added to a tool by the remote MCP server producer after an agent is prompted to use it, the tool's invocation can fail.
  * **Description changes** : If the remote MCP server producer changes a tool's description, it can cause an agent to use a different context or behave differently.



You shouldn't build AI applications or dependencies that rely on specific, non-versioned elements, for example, tool names, parameter names, or descriptions when working with remote MCP servers.

## Intended use of remote MCP servers

We recommend Google and Google Cloud remote MCP servers for enterprise and production deployments with Google Cloud controls for security and governance. For information about features you can use to secure and govern the usage of Google and Google Cloud remote MCP servers, see [MCP on Google Cloud overview](https://docs.cloud.google.com/mcp/overview).

Agents that use Google and Google Cloud remote MCP tools should be designed for dynamic MCP tool and object change. If your agent requires that MCP objects have static names, then we recommend that you build your own MCP server based on versioned and static APIs.

## What's next

  * [Explore supported products](https://docs.cloud.google.com/mcp/supported-products).
  * [Read the Google Cloud MCP servers overview](https://docs.cloud.google.com/mcp/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
