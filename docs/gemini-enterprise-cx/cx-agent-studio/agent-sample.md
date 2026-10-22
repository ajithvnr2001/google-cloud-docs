---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/agent-sample/
title: Sample agent applications \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:36:34.460734+00:00
---

# Sample agent applications  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/agent-sample/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Sample agent applications Stay organized with collections  Save and categorize content based on your preferences. 

You can use the sample agent applications built into the console to understand how a completed agent application is built and to learn best practices for design.

## Import a sample agent application to your project

To import:

  1. Open the [CX Agent Studio console](https://ces.cloud.google.com).
  2. Select your project.
  3. Click the drop-down button next to the **New agent** button.
  4. Click **Try a sample agent**.



After a small delay, the sample agent application will be loaded in the console.

## Cymbal retail agent

**Note:** As of November 2025, this is the only sample agent application, but more samples will be added in the future.

This sample agent application is an assistant for a fictitious company called Cymbal Home & Garden. This assistant can help customers select products, identify plants, and manage their shopping cart.

Try having a conversation by entering input in the **Preview agent** [simulator](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/simulator). You can upload images of plants, ask the agent to identify them, and add them to your shopping cart.

The following features are demonstrated:

Feature | Description  
---|---  
Multi agent architecture | The root agent (cymbal_retail_agent) handles the majority of the conversation. The sub-agents handle upselling and out of scope questions.  
[Instructions](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/instruction) | Structured agent-specific and global instructions are defined for each agent. These instructions explicitly describe what the agent should do and how the agent should do it. These instructions also show how other agents, tools, and variables are referenced.  
[Tools](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool) | Python tools, a Google Search tool, and an OpenAPI tool are included. The OpenAPI tool provides an example for defining an API with 3 endpoints. The end_session system tool is used to complete a phone call (see the "Session Management" section of the root agent). Many of these tools have stubbed implementations, but a few have completed implementations.  
For example, look at the `greeting` Python tool, which is used to control greetings. This code shows how one tool can call another tool.  
[Variables](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/variable) | A custom schema variable is used to store customer profile. You can update this profile to suit your needs. A boolean variable is used to indicate whether a manager has approved a discount. A boolean variable is used to track whether images have been uploaded.  
[Guardrails](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/guardrail) | Guardrail settings have been customized. Prompt guard is enabled with a custom outcome, a blocklist is defined with a custom outcome, a safety outcome is defined, and a rule is configured with instructions.  
[Callbacks](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/callback) | Callbacks have been defined for before_model_callback, after_model_callback, and after_tool_callback.  
[Evaluations](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/evaluation) | When you first load the agent application, many golden and scenario based evaluations are defined and start execution. You can check on the results of these evaluations once the tests have completed.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
