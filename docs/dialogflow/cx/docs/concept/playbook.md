---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/
title: Playbooks \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:44:19.688529+00:00
---

# Playbooks  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Playbooks Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** The _Playbook_ feature is excluded from the [Dialogflow CX SLA](https://cloud.google.com/dialogflow/sla).

A playbook is the basic building block of generative agents. A generative agent typically has many playbooks, where each playbook is defined to handle specific tasks. The playbook data is provided to the LLM to ensure that it has the information it needs to answer questions and execute tasks. Each playbook can provide information, send queries to external services, or defer conversation handling to a [flow](https://docs.cloud.google.com/dialogflow/cx/docs/concept/flow) or another playbook to handle sub-tasks.

## Limitations

The following limitations apply:

  * Agents that use playbooks don't support sending a [call companion](https://docs.cloud.google.com/dialogflow/cx/docs/concept/call-companion) SMS from the Default Welcome Intent route in the Default Start Flow, but you can enable the call companion SMS option in standard flows.
  * Playbooks don't support DTMF input from telephone systems.



## Language support

See the **Playbooks** column in the [language reference](https://docs.cloud.google.com/dialogflow/cx/docs/reference/language#table). The languages marked for playbooks have been tested for quality with `gemini-2.5-flash` models.

When using languages other than English:

  * In most cases, use English for playbook instructions. For certain languages and use cases, you can get slightly better responses if you additionally supply instructions in the target language.
  * Declare your language support in the playbook instructions, for example, "Always answer using the French language".
  * Define your examples in the target language.



## Model support

You can select the LLM model used in playbook in the following places:

  * Select the LLM model at the agent level.

    * In the [Conversational Agents console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents) Agent setting -> Generative AI -> Playbook, select a model by its display name from the list of available models.
    * Specify the model name in the GenerativeSettings.llm_model_settings.model field if you use the API to update agent settings (see [GenerativeSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3beta1#generativesettings)).
  * Override the model selection at the request level.

    * In the Conversational Agents console simulator, select a model by its display name from the list when testing a playbook.
    * Specify the model name in the DetectIntentRequest.query_params.llm_model_settings.model field if you are testing the agent using the API (see [DetectIntentRequest](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3beta1#detectintentrequest)).

Model Name | Model Spec | Launch Stage  
---|---|---  
gemini-2.5-flash | [Gemini 2.5 flash](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-5-flash) | GA  
gemini-2.5-flash-lite | [Gemini 2.5 flash lite](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-5-flash-lite) | GA  
gemini-3.1-flash-lite | [Gemini 3.1 flash lite](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/3-1-flash-lite) | GA  
gemini-3.5-flash-lite | [Gemini 3.5 flash lite](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/3-5-flash-lite) | GA  
  
## Region support

Playbooks are supported in the following [regions](https://cloud.google.com/about/locations):

  * `global`
  * `asia-south1`
  * `asia-southeast1`
  * `asia-southeast2`
  * `asia-northeast1`
  * `australia-southeast1`
  * `eu` (multi-region)
  * `europe-west1`
  * `europe-west2`
  * `europe-west3`
  * `europe-west4`
  * `europe-west6`
  * `northamerica-northeast1`
  * `us` (multi-region)
  * `us-central1`
  * `us-east1`
  * `us-west1`



## Playbook data

A playbook is composed of the following data:

  * Playbook name: a concise name in natural language that helps developers and the LLM understand what tasks the playbook handles.
  * [Goals](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/goal): a high-level description of what the playbook should accomplish.
  * [Instructions](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/instruction): the process steps that the agent must take to accomplish the goal.
  * [Examples](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/example): sample conversations that are effectively few-shot prompt examples for the LLM.
  * [Parameters](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/parameter): variables that store information about a conversation, such as user input, user system information, and action results.



## LLM prompt

For each conversational turn, Dialogflow CX uses your design-time playbook data and runtime conversation data to create an LLM prompt within the [token limits](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-settings#generative-input-token-limit). The contents of this prompt are summarized as follows, where headers are meant to be illustrative and not necessarily part of the prompt.
    
    
    # INTERNAL_SYSTEM_PROMPT
    <you cannot see or edit this>
    
    # INTERNAL_SYSTEM_EXAMPLES
    <you cannot see or edit this>
    
    # AVAILABLE_TOOLS_TO_CURRENT_PLAYBOOK
    <tool names and schemas, for example...>
    
    ## Tool: my_datastore
       description: blah
       input: blah
       output: blah
    
    ## Tool: some_other_custom_tool
       description: blah
       input: blah
       output: blah
    
    # PLAYBOOK
    <verbatim Goal and Instructions that you provide in the console>
    
    # PLAYBOOK_EXAMPLES
    <as many Examples for the current Playbook as can fit in the prompt>
    
    ## Example 1
    
    ## Example 2
    ..
    ..
    ..
    ## Example N (up to the input token limit)
    
    # CURRENT_CONVERSATION
    <the conversation up to this point w/ some caveats...>
    
    * Caveat 1: If there was a transition from Playbook A -> Playbook B, the
      Conversation that happened in Playbook A is summarized and provided as context
    * Caveat 2: If there was a transition from Flow A -> Playbook A, the
      Conversation that happened prior to the entry of Playbook A is summarized and
      provided to the Playbook
    

## Playbook types

When you create a playbook, you select the type of playbook you want: task playbook or routine playbook.

### Task playbooks

_Task playbooks_ are the original type of playbook. You can use them to break down complex tasks into smaller, reusable sub-tasks and model _compositional_ conversation stages, where each stage communicates through input and output parameters.

A task playbook (caller) calls another task playbook (callee):

![One task playbook calling another task playbook](https://docs.cloud.google.com/static/dialogflow/cx/docs/images/task-playbook-calls-task-playbook.png)

  1. The caller starts the callee.
  2. The caller provides necessary input parameters to the callee.
  3. The callee processes this information, performs its designated function, and returns output parameters.
  4. The caller receives parameters from the callee.



Any routine or task playbook can call another task playbook, but a task playbook can't call another routine playbook.

### Routine playbooks

_Routine playbooks_ are a new type of playbook. They are used for modeling _sequential_ conversation stages, where each stage is complete and independent. They can call task playbooks to decompose larger tasks into smaller sub-tasks, and they can transition to other routine playbooks or flows.

The following shows a routine playbook (A), transitioning to another routine playbook (B), transitioning to a flow (C):

![One routine playbook calling another routine playbook](https://docs.cloud.google.com/static/dialogflow/cx/docs/images/routine-playbook-calls-routine-playbook.png)

  1. Routine playbook A can read session parameters when it starts and write session parameters just before exiting.
  2. Routine playbook A exits and transitions to routine playbook B.
  3. Routine playbook B can read session parameters when it starts and write session parameters just before exiting.
  4. Routine playbook B exits and transitions to flow C.
  5. Flow C can read and write session parameters.



If a routine playbook doesn't transition to another routine playbook or flow, the session returns to the last active flow or ends if there isn't one.

Routine playbooks have the following parameter management behavior:

  * When a routine playbook is entered, its input parameters are assigned values that are equivalent to session parameters with the same name.
  * When a routine playbook exits, it generates values for its output parameters and assigns them to session parameters with the same name.



### Compare playbook types

Category | Task Playbook | Routine Playbook  
---|---|---  
Latency | Each time a task playbook calls another task playbook, there is a LLM call. For a long chain of task playbooks in one conversational turn, this can increase latency. | Each routine playbook in a series of transitions occurs within a single conversational turn, so there is only a single LLM call and improved latency.  
Parameter regeneration | When a task playbook calls another task playbook, parameter values need to be regenerated. If there is a long chain of task playbooks, this regeneration can lead to context loss. | Routine playbooks use session storage for parameters, which creates a more reliable context.  
Session parameter integration | Task playbooks do not interface well with session parameters and instead require input and return parameters to be defined. | Routine playbooks interface well with session parameters.  
Reusability | Since every task playbook has a fixed parent/child relationship, tasks are tightly coupled. | Routine playbooks can be defined independently from each other.  
  
## Default playbook

When you create a generative agent using Conversational Agents console, Dialogflow automatically creates a **Default Generative Playbook**.

The default playbook is the starting point for conversations, so it has some important distinctions from other playbooks:

  * The default playbook doesn't receive a summary of preceding conversation turns.
  * The default playbook can't define or receive input parameters.



## Create a playbook

To create a playbook:

  1. Select the playbook icon in the navigation menu of the console.
  2. Click the **Create** button.
  3. Select either a **Routine** or **Task** playbook type.
  4. Provide playbook data.



### Use AI generation to create a playbook

When creating a playbook, a generative AI panel opens. This lets you generate playbook data.

## Import and export playbooks

After you create playbooks using the Conversational Agents console, you can export these playbooks for use in another agent.

To export a playbook:

  1. Go to the playbooks list.
  2. Click the export button for the playbook you want to export.
  3. Select exporting options.
  4. Click **Export**.



To import a playbook you have previously exported:

  1. Go to the playbooks list.
  2. Click **Import**.
  3. Select import options.
  4. Click **Import**.



[ Previous arrow_back  Flow-based prebuilt agents  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agents-prebuilt)

[ Next Playbook goals  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/goal)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
