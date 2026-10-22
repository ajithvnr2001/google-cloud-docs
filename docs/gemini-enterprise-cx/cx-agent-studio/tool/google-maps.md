---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/google-maps/
title: Google Maps tools \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:31.716495+00:00
---

# Google Maps tools  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/google-maps/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Google Maps tools Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This tool is used to connect an agent to Google Maps using a [Model Context Protocol (MCP)](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/mcp) server.

When you first create the tool, you provide:

  * **Name** : Tool name
  * **Description** : Tool description
  * **Server** : Prefilled with Google's MCP server for Google Maps.
  * **Authentication** : See [MCP tool authentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/mcp#authentication). To communicate with the Google Maps MCP server, it's recommended to create a service account, grant it the **MCP Tool User (Beta)** permission, and use **Service Account Auth** with that account. This account's access token will be used for authentication with the Google Maps MCP server.



Once you have provided that information, you can provide advanced settings:

  * **Asynchronous execution** : When enabled, the agent will continue the session while the tool runs in the background.
  * **Custom headers** : Provide custom HTTP headers and optionally inject [session context variables](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/variable#session-context).
  * **Custom TLS certificate authorities** : Optionally upload a custom certificate.
  * **Service Directory** : Optionally provide the name of a service directory.



When you add the MCP tool to an agent, you can select which subtools from the server the agent is allowed to invoke.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
