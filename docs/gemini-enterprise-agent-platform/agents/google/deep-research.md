---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents/google/deep-research/
title: Gemini Deep Research Agent \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:25:10.386890+00:00
---

# Gemini Deep Research Agent  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents/google/deep-research/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Agents ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents)



Send feedback 

#  Gemini Deep Research Agent Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The Gemini Deep Research Agent is a managed AI agent designed to plan, execute, and synthesize complex, multi-step research workflows. Powered by Gemini, the agent navigates diverse information landscapes including the public web and private enterprise data to generate comprehensive, cited reports that accelerate informed decision-making.

For more information on how to get started using Deep Research, see [Use the Gemini Deep Research Agent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents/use-deep-research).

Agent ID | `deep-research-preview-04-2026`  
---|---  
Supported APIs | 

  * Interactions API

  
Supported inputs & outputs | 

  * Inputs: Text, PDF
  * Outputs: Text, Images

  
Token limits | 

  * Maximum input tokens: 1,048,576
  * Maximum output tokens: 65,536

  
Capabilities | 

  * Supported
    * [Grounding with Google Search](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/grounding/grounding-with-google-search)
    * [Grounding with Enterprise Web Search](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/grounding/web-grounding-enterprise)
    * [Grounding with Agent Search](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/grounding/grounding-with-vertex-ai-search)
    * [Grounding on remote MCP servers](https://ai.google.dev/gemini-api/docs/interactions/deep-research#mcp-servers) previewPreview feature
    * [Thought summaries](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/thinking)
    * [Implicit context caching](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/context-cache/context-cache-overview)
    * [Citations](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/grounding/grounding-with-google-search#inline-citations)
  * Not supported
    * [Structured output](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/control-generated-output)
    * [Function calling](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tools/function-calling)
    * [Gemini Live API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/live-api)
    * [Thinking level](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/thinking)
    * [Explicit context caching](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/context-cache/context-cache-overview)
    * [Content Credentials (C2PA)](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/content-credentials)

  
Consumption options | 

  * Supported
    * [Provisioned Throughput](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/provisioned-throughput)
    * [Standard PayGo](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/standard-paygo)
  * Not supported

  
See [Consumption options](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/deploy/consumption-options) for more information.   
Technical specifications  
**Documents** description | 

  * Maximum number of files per prompt: 3,000 
  * Maximum number of pages per file: 3,000 
  * Maximum file size per file for the API or Cloud Storage imports: 50 MB (application/pdf) or 7 MB (text/plain) 
  * Maximum file size per file for direct uploads through the console: 7 MB 
  * Default resolution tokens: 560 
  * OCR for scanned PDFs: Not used by default 
  * Supported MIME types: `application/pdf`, `text/plain`

  
Supported regions |  Agent availability | 

  * Global
    * global

  
See [Agent locations](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/agent-locations) for more information.  
Knowledge cutoff date | January 2025  
Quota name | Stateful Gen AI Interaction Creation requests per minute  
Billing label | `is_deep_research`  
Supported languages | See [Supported languages](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models#expandable-1).  
Pricing | See [Pricing](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
