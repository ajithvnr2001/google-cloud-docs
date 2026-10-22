---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/mcp/
title: MCP tools \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:07.417231+00:00
---

# MCP tools  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/mcp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  MCP tools Stay organized with collections  Save and categorize content based on your preferences. 

[Model Context Protocol (MCP)](https://modelcontextprotocol.io/) is an open-source standard for connecting AI applications to external systems. It establishes a specific set of entities and a defined structure, which acts as a standard way to connect various data sources and tools with AI models.

You can use MCP tools to connect your agent application with an existing MCP server.

## Limitations

The following limitations apply:

  * CX Agent Studio only supports StreamableHttpTransport-based servers; SSE transport servers are not supported.



## Build or select a MCP server

To build your own MCP server, we recommend using the official MCP SDKs or other reliable third-party SDKs such as [FastMCP](https://github.com/jlowin/fastmcp). Once the MCP server is created, deploy it to a hosting service. You can use [Cloud Run](https://docs.cloud.google.com/run) or [Compute Engine](https://docs.cloud.google.com/compute) to host the MCP server. Consider following this guide to understand the process end-to-end: [Build and Deploy a Remote MCP Server to Google Cloud Run in Under 10 Minutes](https://cloud.google.com/blog/topics/developers-practitioners/build-and-deploy-a-remote-mcp-server-to-google-cloud-run-in-under-10-minutes).

Instead of building an MCP server from scratch, you can also use a prebuilt MCP server, such as a [Google Cloud MCP server](https://docs.cloud.google.com/mcp/overview).

## Authentication

MCP tools have the same [authentication options as OpenAPI tools](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/open-api#openapi-authentication).

## Custom headers

You can provide custom HTTP headers to be sent in requests to the MCP server. You can also inject variables from the session context into these headers. For more information, see [Session context variables](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/variable#session-context).

## Test the MCP server independently

Before connecting your agents to the MCP server, we recommend testing the MCP server independently. Servers built using StreamableHttpTransport end with the suffix (`/mcp` or `/mcp/`). For example, if the server is hosted at `https://example.com`, the correct URL to send requests to the server would be `https://example.com/mcp`.

To test the server locally, consider using curl or Postman ([which natively supports MCP connections](https://learning.postman.com/docs/postman-ai/mcp-requests/interact/)). This ensures the server is up and running and that the authentication information required to communicate with the server is understood.

## Custom headers

You can define custom headers that are included when sending HTTP requests to the MCP server (tool list requests as well as tool execution). The values of these headers must be supplied by [variables](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/variable), so to define a custom header, you must first define a variable that will contain the header value. If a variable does not contain a value and there is no default value at runtime, the header won't be included in requests.

## Create the MCP Tool

To create an MCP tool from the console:

  1. Click the tool icon on the right side of the agent builder.
  2. Select **MCP tool**.
  3. Provide a tool name.
  4. Provide a tool description.
  5. Provide the server address for the MCP server.
  6. Select an authentication type.
  7. Optionally define custom headers by providing header names and variables that are used as header values.
  8. Click **Create**.



For servers hosted on Cloud Run, the recommended authentication option is **Service Agent ID Token**. This method uses the CX Agent Studio service account (of the format: `service-{PROJECT_NUMBER}@gcp-sa-ces.iam.gserviceaccount.com`) to send requests to the Cloud Run job. Grant the [Cloud Run Invoker role](https://docs.cloud.google.com/run/docs/reference/iam/roles#run.invoker) to the CX Agent Studio service account , so it can send requests to the server using its own identity.

Before adding additional tools to the agent, we recommend testing at least one tool to ensure the authentication information is set up correctly.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
