---
url: https://docs.cloud.google.com/cloud-assist/reference/mcp/tools_list/optimize_costs/
title: MCP Tools Reference: geminicloudassist.googleapis.com \u00a0|\u00a0 Gemini Cloud Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:30:35.947598+00:00
---

# MCP Tools Reference: geminicloudassist.googleapis.com  |  Gemini Cloud Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cloud-assist/reference/mcp/tools_list/optimize_costs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Cloud Assist ](https://docs.cloud.google.com/cloud-assist)
  * [ API and references ](https://docs.cloud.google.com/cloud-assist/api-and-reference)



Send feedback 

#  MCP Tools Reference: geminicloudassist.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

**Important** : The Gemini Cloud Assist MCP server is in private preview. Use of this Preview offering is subject to the Google Cloud Agreement, including the Pre-GA Offering Terms of the [Google Cloud Specific Service Terms](https://cloud.google.com/terms/services?e=48754805), as supplemented by the terms for the [Gemini for Google Cloud Trusted Tester Program](https://cloud.google.com/trusted-tester/gemini-for-google-cloud-preview?e=48754805). To request access to the private preview, contact your Google Cloud account manager.

## Tool: `optimize_costs`

The Optimize Agent helps users analyze, track, and optimize their Google Cloud costs. It provides detailed breakdowns of spend and identifies opportunities for cost efficiency by finding idle or underutilized resources.

**Core Features:**

  * **Cost Analysis:** Breaks down spend by project, application, product, resource, or location to answer "how much did I spend" questions.
  * **Top Cost Drivers:** Identifies the most expensive resources or services driving the bill.
  * **Cost Trends:** Analyzes how costs have changed over time (e.g., month-over-month increases).
  * **Efficiency & Rightsizing:** Identifies idle, overprovisioned, or underutilized resources _specifically_ to highlight cost-saving opportunities.



**Important Routing Constraints:**

  * **DO** route questions about "underutilized" or "idle" resources if the context is saving money (e.g., "Show me the cost of my most underutilized resources").
  * **DO NOT** route general utilization questions unrelated to cost (e.g., "How much vCPU did resource X use?").
  * This agent **does not** predict future costs.
  * This agent **does not** take any action to reduce costs (read-only analysis).



**When to route to this agent:**

  * User asks "How much did I spend on Compute Engine last month?"
  * User asks "What are my most expensive resources?"
  * User asks "Which resources are idle and costing me money?"
  * User asks "Why did my bill go up compared to last month?"



**Session Management:**

  * This tool returns a `contextId` in its output.
  * To continue a conversation (multi-turn), you MUST include this `contextId`.
  * Omit `contextId` to start a new, independent task.



The following sample demonstrate how to use `curl` to invoke the `optimize_costs` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://geminicloudassist.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "optimize_costs",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

Request for OptimizeCosts

### OptimizeCostsRequest

JSON representation  
---  
      
    
    {
      "project": string,
      "userQuery": string,
      "contextId": string
    }  
  
Fields  
---  
`project` |  `string` Required. The project resource name in the format `projects/{project}`.  
`userQuery` |  `string` Required. The natural language prompt provided by the user.  
`contextId` |  `string` Optional. This is an optional session ID to continue a conversation.  
  
## Output Schema

Represents the response for OptimizeCosts. This message is only used as an output_schema_override.

### OptimizeCostsResponse

JSON representation  
---  
      
    
    {
      "content": string,
      "contextId": string
    }  
  
Fields  
---  
`content` |  `string` Contains the textual response received from the agent.  
`contextId` |  `string` Represents the session ID; clients must persist this.  
  
### Tool Annotations

Destructive Hint: ✅ | Idempotent Hint: ✅ | Read Only Hint: ❌ | Open World Hint: ✅

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
