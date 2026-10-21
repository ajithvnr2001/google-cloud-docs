---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/companion-agent-tools/
title: Companion agent tool support \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:44:15.078558+00:00
---

# Companion agent tool support  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/companion-agent-tools/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Companion agent tool support Stay organized with collections  Save and categorize content based on your preferences. 

Companion agent improves customer service with external tools that fetch verified information during live customer service conversations. Companion agent tools provide the following benefits:

  * Faster customer resolutions
  * Human-in-the-loop
  * Single configuration surface



### Faster customer resolutions

Human agents save time because the companion agent automatically adds relevant account, billing, and shipping details into their active view.

### Human-in-the-loop

Important or sensitive actions prompt human agents to review and approve changes before completion to maintain the safety and accuracy of information. The following stages outline how human agents can verify the companion agent's actions during live conversations:

  1. The companion agent suggests an action and gathers all the initial required information
  2. The companion agent displays an action card showing the tool name, a description of the action, and fields where the human agent can edit the parameters
  3. Human agent review: A human agent reviews the suggested actions and selects one of the following options to proceed: 
     * Click **Confirm** to carry out the action as suggested by the companion agent.
     * Make necessary changes in the details and click **Run** to complete the process.



#### Tool confirmation and operation

Confirmation settings help manage tool safety by requiring explicit user approval before performing sensitive or state-modifying actions during a conversation. Following are key details on how tool confirmations and operations function:

  * Confirmation defaults: By default safe read-only operations run without confirmation. State-modifying operations require human approval before running. You can customize this setting for each tool.

  * Background processing : You can configure tools for background processing, allowing the companion agent to handle background tasks and deliver results when finished. Once a human agent confirms a tool call that requires approval, it always runs independently so the companion agent can resume with the result.




### Single configuration surface

Set up [tools](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool) in [Customer Experience Agent Studio](http://ces.cloud.google.com/) and reuse them for both proactive rules and reactive human agent queries.

## Set up and use tools

See the [set up guide](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/companion-agent-set-up-guide#set_up_a_companion_agent) to add tool support and guidance rules in companion agent.

### Supported tools and use cases

  * [Data store tool](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store/handler): Powered by Agent Search and Dialogflow datastore to query enterprise FAQs, policy manuals, and product specifications.
  * [OpenAPI toolsets](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/tools#openapi_tools): Integrates with REST APIs to handle actions like checking order statuses, looking up CRM account details, and reviewing billing information.
  * [Custom Gemini Enterprise for Customer Experience tools](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/tool-integration-for-ai-coach#create_a_tool): Connects to internal microservices, runs custom Python code, and performs complex mathematical calculations or custom integrations.
  * Google Search tool: Uses Grounding with Google Search to retrieve live web results for real-time info like courier schedules, weather delays, and public information.



## Grounding with Google Search

Grounding with Google Search (GWGS) is an AI feature on the [Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform) that generates suggestions grounded in real time Google Search results. Companion agent generates these grounded results based on end user prompts, customer provided context, Google Search data, and recommended search suggestions. GWGS keeps conversations rooted in factual, up-to-date content because the companion agent can use real time web information.

**Note:** The use of the companion agent Google Search tool is subject to Section 20(k) (Grounding with Google Search) of the [Google Cloud Platform Service Specific Terms](https://cloud.google.com/terms/service-terms).**Caution:** Grounding with Google Search doesn't support Customer-Managed Encryption Keys (CMEK), Data Residency (DRZ), VPC Service Controls (VPC-SC), or Access Transparency (AXT). When you enable this tool, these controls won't apply to search requests. For more details, see [Vertex AI Security Controls](https://cloud.google.com/vertex-ai/generative-ai/docs/security-controls).

## Companion agent modes

Companion agent operates in two modes during live conversations. Tools work behind the scenes to power both modes. They empower proactive mode to automate tasks and reactive mode to fetch verified answers.

Proactive mode offers instructions and runs actions based on preset rules.

  * **Trigger** : An end user sends a chat message that matches configured conversation events, such as `CUSTOMER_MESSAGE`, `AGENT_MESSAGE`, or `END_OF_UTTERANCE`.
  * **Tool activation** : If an instruction condition matches, the guidance agent extracts parameters from the conversation context and activates the tool.
  * **Delivery** : The companion agent displays a recommended action card or relevant information directly on the human agent's screen.



Reactive mode answers specific questions instantly when a human agent searches for information.

  * **Trigger** : A human agent types a question directly into the companion agent's interactive panel.
  * **Tool activation** : The companion agent searches resources or Google Search to find verified details.
  * **Delivery** : The companion agent displays answers with source citations inside the interactive panel.



## Live updates and tool activity

As the companion agent processes a request, it sends continuous updates back to your agent desktop application before delivering the final answer. These intermediate updates let the human agent know that the companion agent is actively working on their query. These live updates include the following two main types of information:

  * **Status updates (tool calls)** : When the companion agent searches for information with Google Search or other tools like a datastore, it immediately sends a brief status message so the user interface can display what the companion agent is doing.


    
    
    {
      "intermediateToolCallEvents": {
        "toolCallSuggestions": [
          {
            "toolCallInfo": {
              "toolCall": {
                "tool": "projects/.../locations/.../apps/.../tools/search-tool",
                "state": "TRIGGERED"
              }
            }
          }
        ]
      },
      "isFinal": false
    }
    

  * **Live response streaming** : As the companion agent starts formulating its response, words and sentences appear in the interactive panel progressively. The human agent can read the answer in real time as it is generated rather than waiting for the entire response to complete.


    
    
    {
      "responseChunk": "For SKU-104 laptops, the standard return window is ",
      "isFinal": false
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
