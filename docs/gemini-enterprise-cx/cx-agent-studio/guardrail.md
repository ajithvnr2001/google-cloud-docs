---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/guardrail/
title: Guardrails \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:36:30.662517+00:00
---

# Guardrails  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/guardrail/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Guardrails Stay organized with collections  Save and categorize content based on your preferences. 

Guardrails are a collection of checks and balances that help protect and keep agent applications safe and secure. They provide content restrictions for both model input and model output. Each agent application is provided with default guardrails, which you can modify to suit your needs. To access the guardrails for your agent application, click the guardrails button on the right side of the agent builder.

## Outcome

Each type of guardrail contains an outcome setting. This controls what happens if the guard is triggered. You can select from the following types of actions:

  * **Say exactly** : Provide the exact agent response.

  * **Handoff to an agent** : Transition control to a specific agent.

  * **Generate a response** : Provide instructions to generate a response. A default is supplied for you, which you can override to customize.




## Prompt guard

Prompt guard provides basic protection against prompt-based attacks like "ignore your instructions and ...". The following settings are available:

  * **Enable prompt guard** : Enable or disable prompt card.
  * **Outcomes** : See Outcome
  * **Custom** : Provide a custom security prompt for screening queries.



## Blocklist

Blocklists prevent users and your agent from using certain words and phrases. When you create a list, the following settings are available:

  * **How should your agent match blocked content?** : This lets you pick the matching method: 
    * **Whole words** : Matches for whole words.
    * **Any mention** : Matches content that contains words and phrases.
    * **Regex pattern** : Matches regular expressions.
  * **Block words and phrases** : The list of blocked words and phrases, where each entry is separated with a comma.
  * **Blocked content from** : Block content from one or both: 
    * **On user input**
    * **On agent response**
  * **Outcomes** : See Outcome
  * **Details** : Provide an optional name and description for this blocklist.



## Safety

These are guardrails that enforce Responsible AI practices. The following settings are available:

  * **Safety level** : Select the level of safety: 
    * **Relaxed** : Prioritize flexible generation and low latency. Never engage with illicit or harmful prompts. Always block explicitly harmful content.
    * **Balanced** : Prioritize safe and natural interactions with customers. Always stop unsafe content. Never engage with harmful prompts.
    * **Strict** : Prioritize deep harm filtering. Never allow generated content with sensitive elements. Always push back against harmful prompts.
  * **Outcomes** : See Outcome
  * **Custom** : Individually adjust or disable specific safety guardrail safety levels.



## Rules

Build your own guardrails using rules. The following settings are available:

  * **Behavior** : Select one of the following to define your rule: 
    * **Natural** : Provide natural language instructions.
    * **Code** : Provide the code for a `after_model_callback` [callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/callback).
  * **Outcomes** : See Outcome
  * **Details** : Provide an optional name and description for this rule.



## Supervisor agents

You can configure supervisor agents that monitor the performance of the active agent currently interacting with the end-user. Supervisor agents ensure that the active agent properly calls tools and maintains good audio quality. If a supervisor agent detects an issue, it can trigger an outcome, similar to other guardrails.

You can also see supervisor agent trigger events on the [monitoring dashboard](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/monitor).

You can configure the following supervisor agents:

  * **Audio quality supervisor** : This monitors audio quality and contains the following settings:

    * **Name** : Supervisor agent name.
    * **Notes** : Optional notes.
    * **Detection mode** : Blocking (active agent response is blocked until supervisor agent finishes assessment) or Non-Blocking (active agent proceeds while supervisor agent continues assessing).
    * **Issue type** : Select one of the following issue types:

      * **Audio mismatch** : Generated audio and generated text do not match.
      * **Speaker shift** : Synthesised voice sounds different over time.
      * **Missing tool call** : Model is supposed to make a tool call in the given context of the conversation, but it failed to do that.
    * **Outcomes** : See Outcome

  * **Missed tool call supervisor** : This monitors for missed tool calls and contains the following settings:

    * **Name** : Supervisor agent name.
    * **Notes** : Optional notes.
    * **Detection mode** : Blocking (active agent response is blocked until supervisor agent finishes assessment) or Non-Blocking (active agent proceeds while supervisor agent continues assessing).
    * **Outcomes** : See Outcome



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
