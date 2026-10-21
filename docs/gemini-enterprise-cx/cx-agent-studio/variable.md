---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/variable/
title: Variables \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T22:59:00.489813+00:00
---

# Variables  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/variable/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Variables Stay organized with collections  Save and categorize content based on your preferences. 

Variables are used to store and retrieve data across conversational turns. They enable agents to remember information and maintain context. When you write prompt instructions for your agent, you can include references to these variables.

## Variable types

The agent builder supports two distinct types of variables in instructions: _static variables_ and _dynamic variables_.

Choosing the right type depends on whether the variable's value needs to change during the user's session, and how much you need to optimize for latency.

### Static variables

Static variables are compiled directly into the agent prompt _before_ the model call happens. They act as a direct 1:1 text substitution and are updated infrequently.

Static variables maximize instruction following quality and are suitable for conditional instructions for many scenarios. Use static variables for configuration data, rigid business rules, or large contextual payloads that don't change over the life of a single conversation.

To reference a static variable by name in your instructions, use double curly braces: `{{variable_name}}`.

For example, if you are creating a retail agent with a large, static product catalog, you could use an instruction like:
    
    
    You are a helpful shopping assistant.
    Please follow these business rules: {{business_rules}}.
    

**Warning:** Updating static variable values invalidates prompt caching, which can potentially lead to higher model call latency.

### Dynamic variables

Dynamic variables can be updated at any point during a conversation by tools, callbacks, or API requests. They are _not_ directly substituted into your prompt's text. Instead, when they are updated, their new values are appended as `state update` events to the conversation history. For example: `<state_update>var_name: value</state_update>`.

Use dynamic variables for information extracted from the user during the session, outputs retrieved from external APIs (tools), or any state that mutates as the conversation progresses.

The following disadvantages apply to dynamic variables:

  * Dynamic variables are appended to conversation history, so if a long session exceeds the context window limit, the agent may forget variable values that get lost when trimming the history.
  * Dynamic variables could lead to slightly lower instruction adherence compared to static variables. This is due to the variable values being defined further away from instructions. This can also add latency, as model thinking needs to find the value further away from the instruction.



To reference a dynamic variable by name in your instructions, use single curly braces: `{variable_name}`.

For example, if you're creating an agent that needs to authenticate a user and then look up their specific account details using a tool, you could use an instruction like:
    
    
    If the user asks for their balance, call the {@TOOL: LookupBalance}.
    The tool will update the {current_account_balance} variable.
    Always share the {current_account_balance} with the user.
    

## Variable data

Variables have the following data:

  * **Name** : Variable name using snake case
  * **Type** : Underlying data type: 
    * **Text** : String values
    * **Number** : Numeric values
    * **Yes/No** : Boolean values
    * **Custom Object** : You provide a schema for the object
    * **List** : List of variables. Provide values as a comma delimited list.
  * **Default value** : Default value for the variable
  * **Description** : Optional description of the variable



## Updating variable values

The agent itself cannot update the value of a variable, but tools and callbacks can update variable values.

Agent variables use the [ADK context state](https://google.github.io/adk-docs/context/#managing-state), which can be used to update variables. A global variable called `context` is available to use in your Python tool code. For example, you can use the following statement in a Python tool to update a variable using ADK features:
    
    
    context.state["variable_name"] = value
    

**Warning:** Instruction templates are rendered _between_ the `before_agent` callback and the `before_model` callback. Variable updates made in a `before_agent` callback take effect immediately on the current turn, whereas variable updates made in a `before_model` callback aren't visible in rendered instructions until the following conversational turn. Reference variables updated by `before_model` callbacks as static `{{variable_name}}` variables rather than dynamic `{variable_name}` variables, because `before_model` callbacks don't append `<state_update>` events to the conversation history.

## Built-in session context variables

Beyond custom variables, OpenAPI and MCP tools can reference built-in session context variables. These are available by default and can be passed within HTTP headers or request parameters. These variables cannot be referenced in instructions, and cannot be manually overwritten. The following built-in variables are available:

  * `$context.project_id`, `$context.project_number`, `$context.location`, `$context.app_id`, `$context.session_id`, `$context.turn_index` for app-level/session-level resource IDs.
  * `$context.variables.variable_name` for a specific agent variable value.
  * `$context.variables` for all agent variable values as an object.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
