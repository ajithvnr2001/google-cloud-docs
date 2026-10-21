---
url: https://docs.cloud.google.com/cloud-assist/reference/mcp/tools_list/ask_cloud_assist/
title: MCP Tools Reference: geminicloudassist.googleapis.com \u00a0|\u00a0 Gemini Cloud Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:40:55.388562+00:00
---

# MCP Tools Reference: geminicloudassist.googleapis.com  |  Gemini Cloud Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cloud-assist/reference/mcp/tools_list/ask_cloud_assist/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Cloud Assist ](https://docs.cloud.google.com/cloud-assist)
  * [ API and references ](https://docs.cloud.google.com/cloud-assist/api-and-reference)



Send feedback 

#  MCP Tools Reference: geminicloudassist.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

**Important** : The Gemini Cloud Assist MCP server is in private preview. Use of this Preview offering is subject to the Google Cloud Agreement, including the Pre-GA Offering Terms of the [Google Cloud Specific Service Terms](https://cloud.google.com/terms/services?e=48754805), as supplemented by the terms for the [Gemini for Google Cloud Trusted Tester Program](https://cloud.google.com/trusted-tester/gemini-for-google-cloud-preview?e=48754805). To request access to the private preview, contact your Google Cloud account manager.

## Tool: `ask_cloud_assist`

The primary interface for Google Cloud Platform assistance. Use this tool to interact with the GCA Root Agent for general troubleshooting, log analysis, or broad cloud inquiries. It acts as the central orchestration agent that directs user requests to expert sub-agents or handles them directly using general-purpose tools.

**Capabilities:**

  * **General Inquiries:** Answers broad questions about Google Cloud services, concepts, and documentation.
  * **Estate Queries:** Retrieves current resource state and inventory (e.g., "List my active VMs," "Show me the config for this pod").
  * **Directives:** Executes specific, low-complexity directives or status checks.
  * **Triage & Routing:** Handles complex or ambiguous intents (e.g., "Something is wrong with my app") to identify the problem scope before potentially handing off to specialized agents.
  * **Secure Execution:** Orchestrates mutative actions (e.g., "Restart this VM", "Scale this cluster") using a secure Human-in-the-Loop (HITL) workflow. It verifies user consent before executing `gcloud` commands.



**Usage Guidelines:**

  * **Default Choice:** Select this tool when the user's intent is broad, ambiguous, exploratory, purely informational, or involves planning.
  * **Triage:** Use this tool for initial issue reporting where the specific domain is not yet clear.
  * **Direct Execution:** Use this tool when the user requests a specific, intended change to their environment (e.g., "Restart instance X", "Scale this cluster", "Update the firewall rule").
  * **Exclusions:**
    * If the user explicitly asks to **design, architect, or deploy** infrastructure, use `design_infra`.
    * If the user explicitly asks for **deep root cause analysis, debugging, or remediation** of a known failure, use `investigate_issue`.
    * If the user explicitly asks about **costs, billing, or idle resources** , use `optimize_costs`.



**Session Management:**

  * This tool returns a `contextId` in its output.
  * To continue a conversation (multi-turn), you MUST include this `contextId`.
  * Omit `contextId` to start a new, independent task.



The following sample demonstrate how to use `curl` to invoke the `ask_cloud_assist` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://geminicloudassist.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "ask_cloud_assist",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

Request for AskCloudAssist

### AskCloudAssistRequest

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

Represents the response for AskCloudAssist. This message is only used as an output_schema_override.

### AskCloudAssistResponse

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

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
