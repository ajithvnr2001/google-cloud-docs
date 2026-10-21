---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/instruction/
title: Instructions \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T22:59:01.759293+00:00
---

# Instructions  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/instruction/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Instructions Stay organized with collections  Save and categorize content based on your preferences. 

Agent _instructions_ provide detailed guidance for the model on what it should do. These instructions are provided in natural language.

## Write instructions

Instructions can contain any of the following:

  * Overall goal.
  * How to behave.
  * Persona to use.
  * References and dynamic conditions.



Example for a root agent:
    
    
    CURRENT CUSTOMER: {username}
    
    You are the main Weather Agent coordinating multiple agents.
    Your primary responsibility is to provide weather information.
    Use {@TOOL: get_weather} ONLY for specific weather requests
    (for example, 'weather in London').
    
    If you know the user's name, always greet them by their name.
    
    You have specialized sub-agents:
      1. Greeting Agent: Handles simple greetings like 'Hi', 'Hello'.
      2. Farewell Agent: Handles simple farewells like 'Bye', 'See you'.
    
    Analyze the user's query.
    If it's a greeting, call {@AGENT: Greeting Agent}
    If it's a farewell, call {@AGENT: Farewell Agent}
    If it's a weather request, handle it yourself using {@TOOL: get_weather}
    
    For anything else, respond appropriately or state you cannot handle it.
    

## Modular components

When providing instructions, you can create _modular components_ by using dynamic instructions. With modular components, you can create a single set of agent instructions that behave like multiple agents, where each agent is customized for a particular channel (API, telephony, web), modality (voice, text), or session variable using conditional blocks (`if`/`elif`/`else`), filters, loops (`for`), and reusable macros.

For the complete syntax reference and advanced examples, see [Modular components](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/modular-components).

## References and modular component syntax

This section provides a quick summary of references and modular component tags. For the full expression grammar, operator precedence, filters, loops, and macros, see [Modular components](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/modular-components).

### Basic references

You can explicitly reference variables, agents and tools in your instructions.

Syntax | Description  
---|---  
`{variable_name}` | References a particular [dynamic variable](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/variable#dynamic).  
`{{variable_name}}` | References a particular [static variable](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/variable#static).  
`{@AGENT: Agent Name}` | References a particular agent.  
`{@TOOL: tool_name}` | References a particular tool.  
  
Sample:
    
    
    If it's a greeting, call {@AGENT: Greeting Agent}
    If it's a farewell, call {@AGENT: Farewell Agent}
    If it's a weather request, handle it yourself using {@TOOL: get_weather}
    
    Please follow these business rules: {{business_rules}}.
    

### Channel conditions

You can optimize your instructions for individual channel types. For the full list of supported channel tags (`Twilio`, `Five9`, `AudioCodes`, `GoogleCCaaSVoice`, `GoogleCCaaSChat`, `WhatsApp`, `Instagram`), see [Channel block tags](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/modular-components#channel-tags).

Syntax | Description  
---|---  
`{@startChannel_API}` (or `{@startChannelAPI}`) | Marks the beginning of instructions that only apply to API driven interactions.  
`{@endChannel_API}` (or `{@endChannelAPI}`) | Marks the end of instructions that only apply to API driven interactions.  
`{@startChannel_GoogleTelephonyPlatform}` | Marks the beginning of instructions that only apply to [Google Telephony Platform](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/deploy/google-telephony-platform) driven interactions.  
`{@endChannel_GoogleTelephonyPlatform}` | Marks the end of instructions that only apply to [Google Telephony Platform](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/deploy/google-telephony-platform) driven interactions.  
`{@startChannel_WEB_UI}` (or `{@startChannelWEB_UI}`) | Marks the beginning of instructions that only apply to [web widget](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/deploy/web-widget) driven interactions.  
`{@endChannel_WEB_UI}` (or `{@endChannelWEB_UI}`) | Marks the end of instructions that only apply to [web widget](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/deploy/web-widget) driven interactions.  
  
Sample:
    
    
    {@startChannel_GoogleTelephonyPlatform}
    Telephony instructions here.
    {@endChannel_GoogleTelephonyPlatform}
    

### Modality conditions

You can optimize your instructions for specific modalities (text versus voice). Be sure to select the correct **Modality** setting in the deployment settings.

Syntax | Description  
---|---  
`{@startModality_Text}` (or `{@startModalityTEXT}`) | Marks the beginning of instructions that only apply to text driven interactions.  
`{@endModality_Text}` (or `{@endModalityTEXT}`) | Marks the end of instructions that only apply to text driven interactions.  
`{@startModality_Voice}` (or `{@startModalityVOICE}`) | Marks the beginning of instructions that only apply to voice driven interactions.  
`{@endModality_Voice}` (or `{@endModalityVOICE}`) | Marks the end of instructions that only apply to voice driven interactions.  
  
Sample:
    
    
    {@startModality_Text}
    Text instructions here.
    {@endModality_Text}
    

### Flexible conditions

You can build flexible conditions, loops, filters, and macros based on variable values, channel, or modality. For all supported operators (`!=`, `<`, `>`, `<=`, `>=`, `in`, `is defined`), filters (`| default`, `| length`, `| upper`), loops (`{% for %}`), and macros (`{% macro %}`), see [Conditional logic and expressions](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/modular-components#conditional-logic).

Syntax | Description  
---|---  
`{% if variable_name == 'A' %}` | Marks the beginning of instructions that only apply when the variable is equal to the given value.  
`{% if _session.modality == 'MODALITY' %}` | Marks the beginning of instructions that only apply to the given MODALITY value, which can be one of:  
`TEXT`  
`VOICE`  
`{% if _session.channel == 'CHANNEL' %}` | Marks the beginning of instructions that only apply to the given CHANNEL value, which can be one of:  
`API`  
`WEB_UI`  
`TWILIO`  
`GOOGLE_TELEPHONY_PLATFORM`  
`CONTACT_CENTER_AS_A_SERVICE`  
`CONTACT_CENTER_AS_A_SERVICE_CHAT`  
`FIVE9`  
`WHATSAPP`  
`INSTAGRAM`  
`CONTACT_CENTER_INTEGRATION`  
`and` | Logical AND used within a condition.  
`or` | Logical OR used within a condition.  
`not` | Logical NOT used within a condition.  
`{% else %}` | Start else block of condition.  
`{% elif ... %}` | Start else-if block of condition.  
`{% endif %}` | Complete the condition.  
  
Sample:
    
    
    {% if _session.modality == 'TEXT' %}
    Say exactly: "Welcome to Customer Support! I am your virtual assistant."
    {% else %}
    Say exactly: "Hi there! Thank you for calling customer support."
    {% endif %}
    
    {% if brand_name == 'Cymbal Retail' or brand_name == 'Cymbal Wholesale' %}
    Say exactly: "Welcome to Cymbal support".
    {% elif brand_name == 'Acme Corp' %}
    Say exactly: "Welcome to Acme Corp support".
    {% else %}
    Say exactly: "Welcome to support".
    {% endif %}
    

### Testing modular components

When interacting with an agent that uses dynamic instructions with the [simulator](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/simulator), the tracing information will show the value of the `_session` variable used for the conversation.

When testing agents that use dynamic instructions using modality or channel with evaluations, you should set the `_session` [scenario variable](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/evaluation#scenario_variables). For example, if the scenario involves the `TEXT` modality and `API` channel, you should set the `_session` variable to
    
    
    {
      "modality": "TEXT",
      "channel": "API"
    }
    

It is also helpful to set custom variables that are used in dynamic instructions using either the simulator or the scenario editor. For example, you might have a `brand_name` variable with different behavior depending on its value.

### Syntax highlighting

When using the special syntax in the console, text will be highlighted with a colored "chip", indicating that the syntax is recognized.

To make inserting these references easier, the instructions editor provides two shortcuts:

  * Typing `@` opens a context menu. You can navigate this menu with arrow keys and **Tab** , or by clicking. Selecting an option will show further options until the reference is complete, at which point it will become a chip.
  * Typing `{` opens a context menu showing available variables for quick insertion.

**Note:** For the **Tool** option, only tools that have been added to the current agent appear in the context menu.

## Language support

When designing agent prompts and instructions, always use English for the highest quality understanding by the agent. When your agents interact with your users, they are able to detect the language of the end-user input and automatically respond using the same language, unless specifically instructed otherwise.

If you want your agent to only speak (or not speak) in certain languages, you should include an instruction describing the support. For example, if your agent should only respond in Italian, you can include "you only speak Italian and no other languages" in your instructions.

For the list of supported languages, see the [languages reference](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/language).

## Restructure instructions

You can enter instructions in natural language, but your agent may perform better if you format instructions using an XML structure, which can help the model better follow instructions. We provide a standard XML structure with tags that you can use to structure your instructions. Once you have entered natural language instructions, you can click the **Restructure instructions** button above the instructions panel to format the instructions into our recommended XML structure.

The following table describes recommended XML tags and how they can be used:

Tag | Description  
---|---  
`role` | Defines the agent's core function or responsibility.  
`persona` | Describes the agent's personality, tone, and behavioral guidelines.  
`primary_goal` | Within `<persona>`, specifies the agent's main objective.  
`constraints` | Lists rules or limitations the agent must follow.  
`taskflow` | Outlines conversational flows as a series of subtasks.  
`subtask` | Within `<taskflow>`, a specific part of the conversation flow, containing one or more steps.  
`step` | Within `<subtask>`, an individual step that includes a trigger and an action.  
`trigger` | Within `<step>`, the condition or user input that initiates a step.  
`action` | Within `<step>`, the action the agent should take when a step is triggered.  
`examples` | Contains few-shot examples to guide agent behavior for specific scenarios.  
  
Here's a sample of the same instructions using our recommended XML structure:
    
    
    CURRENT CUSTOMER: {username}
    
    <role>The main Weather Agent coordinating multiple agents.</role>
    
    <persona>
        <primary_goal>To provide weather information.</primary_goal>
        How to handle prohibited topics and violations: Respond appropriately or
        state inability to handle the request.
        General guidelines: Follow the constraints and task flow precisely.
    </persona>
    
    <constraints>
        1. Use {@TOOL: get_weather} ONLY for specific weather requests 
          (for example, 'weather in London').
        2. If the user's name is known (from the 'CURRENT CUSTOMER' context), always
          greet them by their name.
    </constraints>
    
    <taskflow>
        These define the conversational subtasks that you can take. Each subtask
        has a sequence of steps that should be taken in order.
        <subtask name="Initial Greeting">
            <step name="Check for Username and Greet">
                <trigger>Start of conversation or new user interaction.</trigger>
                <action>If a username is provided in the 'CURRENT CUSTOMER' context,
                  greet the user by their name. Otherwise, proceed without a 
                  personalized greeting.
                </action>
            </step>
        </subtask>
        <subtask name="Query Analysis and Routing">
            <step name="Analyze User Query">
                <trigger>User provides a query.</trigger>
                <action>Determine the intent of the user's query 
                  (greeting, farewell, weather request, or other).
                </action>
            </step>
            <step name="Handle Greeting">
                <trigger>User query is identified as a simple greeting
                  (e.g., 'Hi', 'Hello').
                </trigger>
                <action>Call {@AGENT: Greeting Agent}.</action>
            </step>
            <step name="Handle Farewell">
                <trigger>User query is identified as a simple farewell
                  (e.g., 'Bye', 'See you').
                </trigger>
                <action>Call {@AGENT: Farewell Agent}.</action>
            </step>
            <step name="Handle Weather Request">
                <trigger>User query is identified as a specific weather request
                  (e.g., 'weather in London').
                </trigger>
                <action>Use {@TOOL: get_weather} to retrieve weather information and
                  provide it to the user.
                </action>
            </step>
            <step name="Handle Other Queries">
                <trigger>User query does not fall into greeting, farewell, or
                  specific weather request categories.
                </trigger>
                <action>Respond appropriately to the query or state that the request
                  cannot be handled.
                </action>
            </step>
        </subtask>
    </taskflow>
    <examples>
    </examples>
    

## Inline few-shot examples

Few-shot prompting is a technique where a Large Language Model (LLM) is provided with a small set of examples to guide its behavior, tone, or logic. In the context of Agents, "Inline Few-Shot Examples" refer to placing these examples directly within the agent's instructions rather than in a separate UI pane. This method helps the model understand complex requirements by showing rather than just telling, essentially bridging the gap between abstract instructions and concrete execution.

### When to use few-shot examples

Few-shot examples are a powerful tool for calibration but should be used strategically. Consider adding them in the following scenarios:

  * **Resolving quality issues** : Use examples primarily to fix specific failures where the model consistently misunderstands instructions.
  * **Complex formatting** : When the agent needs to output data in a very specific, non-standard format.
  * **Nuanced logic** : When "if-then" instructions are insufficient to capture the subtlety of a decision-making process.



### Best practices and warnings

While effective, few-shot examples should be curated carefully to avoid degrading agent performance.

  * **Use sparingly** : Adding too many examples can cause the agent to "overfit," meaning it may rigidly follow the examples and lose its ability to generalize to new, unseen user queries.
  * **Descriptive, not exhaustive** : You do not need to enumerate every possible user query. Examples are meant to serve as guidance for the model's reasoning pattern, not as a lookup database.
  * **Start with instructions** : Always attempt to solve behavior issues with clear, descriptive instructions first. Only add few-shots if instructions alone fail to achieve the desired result.



### Components of a few-shot example

A standard few-shot example for agents consists of four distinct components that simulate a conversation turn.

Component | Tag / Syntax | Description  
---|---|---  
User | `[user]` | Represents the end-user's input or query.  
Model | `[model]` | Represents the agent's textual response or thought process.  
Tool Input | `tool_code` | Demonstrates how the agent should structure the input or "call" to an external tool or function (e.g., specific arguments/syntax).  
Tool Output | `tool_outputs` | Simulates the data returned by the tool, teaching the agent how to interpret and utilize that data in its final response.  
  
The following format should be used for few-shot examples:
    
    
    <examples>
      EXAMPLE 1:
      Begin example
      [user]
      What's the weather in London?
      [model]
      ```tool_code
      get_weather(location="London")
      ```
      ```tool_outputs
      {"temperature": "15 C", "condition": "Cloudy"}
      ```
      [model]
      The weather in London is 15 C and Cloudy.
      End example
    </examples>

## Refine instructions

You can select a portion of your instructions content, then a **Refine** button appears. You can click this button to use AI to improve the selected content. In the **Requirements** field, enter information about how you want to improve the selected content.

## Format agent responses

You can instruct the agent on how to format its textual responses for better readability. The following are best practices for instruction on formatting:

### Chunking and whitespace

  * **Never** write dense paragraphs. Users scan; they do not read.
  * Limit text blocks to 1-2 sentences maximum.
  * Insert a line break between every distinct idea to create whitespace.



### Strategic bolding

  * You must **bold** the most important data points so they stand out instantly.
  * **Always bold** : **Product Names** , **Prices** , **Dates** , **Order Numbers** , and **Deadlines**.
  * _Example_ : "The **Classic Tee** is **$25.00**."



### Lists over text

  * If you mention more than two items or steps, **automatically** convert them into a bulleted or numbered list.
  * Use standard bullets (`-`) for options and numbered lists (`1.`) for instructions.



## Global instructions

In addition to defining agent-specific instructions, you can define global instructions in the [advanced agent application settings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/agent#agent-application-settings).

Every agent in the agent application inherits the global instructions, and they are sent to the model for every conversational turn on top of the agent-specific instructions.

Global instructions are well suited for generic information that every agent needs to know about. For example: brand tone, general "DOs and DON'TS", globally shared variables, and customer profiles.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
