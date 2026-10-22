---
url: https://docs.cloud.google.com/cloud-assist/reference/mcp/tools_list/investigate_issue/
title: MCP Tools Reference: geminicloudassist.googleapis.com \u00a0|\u00a0 Gemini Cloud Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:46:14.032217+00:00
---

# MCP Tools Reference: geminicloudassist.googleapis.com  |  Gemini Cloud Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cloud-assist/reference/mcp/tools_list/investigate_issue/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Cloud Assist ](https://docs.cloud.google.com/cloud-assist)
  * [ API and references ](https://docs.cloud.google.com/cloud-assist/api-and-reference)



Send feedback 

#  MCP Tools Reference: geminicloudassist.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

**Important** : The Gemini Cloud Assist MCP server is in private preview. Use of this Preview offering is subject to the Google Cloud Agreement, including the Pre-GA Offering Terms of the [Google Cloud Specific Service Terms](https://cloud.google.com/terms/services?e=48754805), as supplemented by the terms for the [Gemini for Google Cloud Trusted Tester Program](https://cloud.google.com/trusted-tester/gemini-for-google-cloud-preview?e=48754805). To request access to the private preview, contact your Google Cloud account manager.

## Tool: `investigate_issue`

The Investigation Orchestrator Agent is the **Principal Troubleshooting & Diagnostics Agent** for Google Cloud. It acts as a specialized "SRE in a box" capable of navigating complex infrastructure, application code, and observability data to resolve incidents.

**Core Features & Architecture:**

  * **Advanced Reasoning & Interactive Investigations:** Uses sophisticated planning algorithms to execute **parallelized hypothesis evaluation** , allowing it to check multiple failure scenarios simultaneously rather than sequentially.
  * **Quick vs. Deep Investigation Strategy:**
    * **Express Mode:** For rapid insights, log/metric anomaly detection, and real-time status checks.
    * **Deep Research Mode:** For complex Root Cause Analysis (RCA). It leverages **domain expertise** by integrating with specialized Database & Analytics Agents via the Cloud Assist Planner Agent.
  * **Diagnostic Runbooks:** Can automatically select and execute pre-defined diagnostic playbooks for standardized troubleshooting.
  * **Trace-Based Topology:** Generates dynamic architecture maps derived from real traffic traces, not just static configuration.
  * **Source Code Insights:** Analyzes application logic to find root causes within the code itself (e.g., connection pools, queries).
  * **AI-Powered Explanation:** Provides plain-language explanations for obscure error logs and metric anomalies.



**When to route to this agent:**

  * User requests **Root Cause Analysis (RCA)** or help with an outage/crash.
  * User asks to analyze **logs, metrics, or traces** for anomalies.
  * User needs to **understand dependencies** or reason about topology graph.
  * User asks about **source code** issues causing infrastructure failures.
  * User wants to run specific **diagnostics** or health checks.



**Detailed Capabilities & Skills:**

  * **Deep Research & Root Cause Analysis (RCA):** Initiates a comprehensive, multi-step investigation using advanced reasoning and planning. It executes parallelized hypothesis evaluation, leveraging domain-specific agents (Database, Analytics) to find definitive root causes. Use this for complex, open-ended problems.

    * Examples: "My application latency has spiked to 5s, find the root cause.", "Investigate why the chatter-service is throwing 503 errors during the load test.", "Why are the pods on ClusterABC unschedulable?", "Analyze the bottlenecks in my checkout flow.", "Perform a deep analysis of the database lock contention."
  * **Diagnostic Runbooks & Playbooks:** Executes deterministic diagnostic runbooks and standard operating procedures (SOPs). This skill integrates with the Cloud Assist Planner Agent to run validated checks for known issues and common failure modes.

    * Examples: "Run the connectivity diagnostic for the frontend service.", "Execute the standard health check runbook.", "Check for known configuration issues using the diagnostic playbook.", "Is there a runbook to verify network reachability?"
  * **Express Diagnostics & Anomaly Detection:** Performs rapid 'Quick Checks' and automated anomaly detection on logs and metrics. Use this to instantly identify outliers, spikes, or error patterns without waiting for a full investigation.

    * Examples: "Detect any metric anomalies for the checkout-service.", "Show me the traffic level and latency for the chatter-frontend service.", "Are there any outliers in the CPU usage?", "What are the top errors for the store-processing service right now?", "Scan the logs for recent error spikes."
  * **AI-Powered Log & Error Reasoning:** Uses AI to **reason about** and interpret complex error logs, stack traces, and metric patterns. Beyond simple explanation, it deduces the technical meaning and potential impact of observability data.

    * Examples: "Analyze this stack trace and explain why the crash is happening.", "Reason about this 'Connection Reset' error in the context of high load.", "Interpret this obscure database error code.", "Why am I seeing this specific error log repeatedly?"
  * **Trace-Based Topology Graph:** Generates a dynamic topology graph derived from real application traces (OneGraph). It visualizes and reasons actual traffic paths and dependencies, overlaying latency and error signals on the graph nodes.

    * Examples: "Show me the trace-based topology for the payment service.", "Visualize the actual traffic flow between microservices.", "Map out the dependencies based on recent request traces.", "Generate a graph showing where the latency is introduced in the stack."
  * **Source Code Insights:** Deeply analyzes application source code and configuration files (via DevConnect). It connects infrastructure symptoms to specific lines of code, identifying issues like bad queries, aggressive timeouts, or logic bugs.

    * Examples: "Analyze the source code for inefficient database queries.", "Did a recent commit change the connection pool settings?", "Check the app logic for potential race conditions.", "Review the configuration files in the repo for errors."
  * **Root Cause Resolution & Remediation:** Synthesizes investigation findings to **identify the definitive root cause** and generates a corresponding actionable remediation plan (e.g., CLI commands, code patches) to resolve the issue.

    * Examples: "Find the root cause of the database timeout and generate a plan to fix it.", "Identify why the instance is crashing and create a gcloud command to resize it.", "Determine the cause of the connection errors and suggest code changes.", "What is the recommended fix for this error?"
  * **Multi-Turn Interactive Troubleshooting:** Supports stateful, multi-turn interactivity. Allows the user to guide the investigation, ask follow-up questions, refine the scope, and iterate on findings in a conversational manner.

    * Examples: "That didn't fix it, what should we check next?", "Can you look at the database logs instead?", "Let's focus on the frontend service now.", "Go deeper into that second hypothesis."



**Session Management:**

  * This tool returns a `contextId` in its output.
  * To continue a conversation (multi-turn), you MUST include this `contextId`.
  * Omit `contextId` to start a new, independent task.



The following sample demonstrate how to use `curl` to invoke the `investigate_issue` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://geminicloudassist.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "investigate_issue",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

Request for InvestigateIssue

### InvestigateIssueRequest

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

Represents the response for InvestigateIssue. This message is only used as an output_schema_override.

### InvestigateIssueResponse

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
