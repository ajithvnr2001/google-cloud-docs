---
url: https://docs.cloud.google.com/mcp/known-issues/
title: Known issues \u00a0|\u00a0 Google Cloud MCP servers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:39:38.328955+00:00
---

# Known issues  |  Google Cloud MCP servers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/mcp/known-issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud APIs ](https://docs.cloud.google.com/apis/docs/overview)
  * [ Google Cloud MCP servers ](https://docs.cloud.google.com/mcp)
  * [ Guides ](https://docs.cloud.google.com/mcp/overview)



Send feedback 

#  Known issues Stay organized with collections  Save and categorize content based on your preferences. 

This document provides details and workarounds for known issues with Google and Google Cloud remote Model Context Protocol (MCP) servers.

## Tool issues

The following known issues affect specific Google or Google Cloud MCP tools.

### Compute Engine `list_images` tool returns permission denied

The Compute Engine [`list_images` tool](https://docs.cloud.google.com/compute/docs/reference/mcp/list_images) fails with a permission error when querying public images like `fedora-cloud`.

## Client-specific issues

The following issues involve problems with specific MCP clients.

### Gemini CLI gives API error

The following issue occurs when the name of the MCP server is longer than 64 characters or contains characters other than alphanumeric characters, underscores, dots, colons, or dashes:
    
    
    [API Error: {"error":{"message":"{\"error\": {\"code\": 400, \"status\": 400, \"message\": \"* GenerateContentRequest.tools[0].function_declarations[14].name: Invalid
    function name. Must start with a letter or an underscore. Must be alphanumeric (a-z, A-Z, 0-9), underscores (_), dots (.), colons (:), or dashes (-), with a maximum length
      of 64.\\n*
    

To resolve this issue, change the name of the MCP server in your Gemini extension file to comply with the required naming conventions. Gemini CLI extension files are typically located in: `~/.gemini/extensions/EXT_NAME/gemini-extension.json` where `~/` is your home directory and `EXT_NAME` is the name you gave the extension. For more information, see [Configure MCP in an AI application](https://docs.cloud.google.com/mcp/configure-mcp-ai-application#gemini-cli)

## What's next

  * [Configure Google and Google Cloud remote MCP servers in your AI applications](https://docs.cloud.google.com/mcp/configure-mcp-ai-application).
  * [Explore supported products](https://docs.cloud.google.com/mcp/supported-products).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
