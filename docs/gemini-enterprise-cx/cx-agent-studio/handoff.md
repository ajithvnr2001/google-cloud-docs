---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/handoff/
title: Handoff rules \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:13:43.838130+00:00
---

# Handoff rules  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/handoff/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Handoff rules Stay organized with collections  Save and categorize content based on your preferences. 

You can use handoff rules to deterministically control transfers between parent and child agents in a multi-agent application. You can control these transfers by defining conditions for the transfers. You can either force a transfer immediately when a condition is met, or block transfers until a condition is met.

For example, Agent A transfers to Agent B when a user is authenticated or to Agent C when the user is unauthenticated.

You can achieve similar control over agent transfers using instructions, but that control is not deterministic. You could also use callbacks, but callbacks require writing code.

Example use cases:

  * Forward handoffs (agent to subagent) 
    * Route authenticated or unauthenticated users to different agents
    * Understand user's intent and steer to the right agent
    * Directing high-stakes requests (for example, financial transfers, PII handling) to specific agents
  * Backward handoffs (subagent to agent) 
    * Retry failed authentication attempts
    * Loop back for additional information gathering
    * Re-qualification after changes in user requirements
    * Iterative troubleshooting processes



## Configuration

To configure handoff rules from the agent builder:

  1. Click the **+** button under an agent node.
  2. Select **Add handoff rules**. The Handoff rules configuration pane is opened, and child agents are listed.
  3. Select a child agent. The rule configuration pane opens.
  4. Select the direction of the transfer (to parent or to child).
  5. You can use the interface to define conditions based on variables, or you can use the advanced code option.
  6. Click **Save**.



If you choose the advanced code option, here is a sample:
    
    
    def should_trigger_transfer_callback(callback_context: CallbackContext) -> bool:
      # Access session variables using callback_context:
      # callback_context.variables['variable_name]
      return True
    

## Limitations

The following limitations apply.

When creating a rule that uses a variable check, you can specify multiple conditions (one per variable). These can be linked together using AND or OR logical operators. Only **one** (AND/OR) operator can be selected for all conditions listed. If you want to mix logical operators and group conditions together, you can use the Python code option or specify the condition using the API.

Only text, number, and boolean variable types are supported for variable checks (list and custom object types are not supported).

When defining a rule that **blocks** handoffs, the condition can only be specified using variables (not code).

If you create a complex condition using the API (using multiple ANDs/ORs, grouping, etc.) then the handoff rule appears as read-only in the UI, and can only be modified using the API.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
