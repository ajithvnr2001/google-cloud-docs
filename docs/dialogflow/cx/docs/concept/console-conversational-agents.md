---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents/
title: Conversational Agents console overview \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:58.641876+00:00
---

# Conversational Agents console overview  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Conversational Agents console overview Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** The Conversational Agents console includes the features from both deprecated Dialogflow CX console and Vertex AI Agent Builder console.

The Dialogflow Console is an UI that lets you intuitively create interactive agents that use [generative playbooks](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook), [generative data stores](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store), and [deterministic flows](https://docs.cloud.google.com/dialogflow/cx/docs/basics).

## Console compatibility

Agents previously built with the Dialogflow CX console or the Vertex AI Agent Builder console can be seamlessly accessed by the Conversational Agents console. Agents created with any of these three consoles use the same Dialogflow API.

## Supported regions

The console supports all [regions](https://docs.cloud.google.com/dialogflow/cx/docs/concept/region) previously supported by the Dialogflow CX console or the Vertex AI Agent Builder console.

## Pricing

[Pricing](https://cloud.google.com/products/conversational-agents/pricing) for agents created with the Conversational Agents console is the same as it has been for agents created with the Dialogflow CX console. Agents that use generative features such as playbooks, data stores, generators, or generative fallback for a request are charged as generative requests.

## Create an agent

Prebuilt agents can be used to accelerate development for agents in common scenarios.

To create an agent with prebuilt agents:

  1. Open the [Conversational Agents console](https://conversational-agents.cloud.google.com).
  2. Select or create a project.
  3. Click **Create agent**.
  4. Click **Use a prebuilt agent**.
  5. Select a prebuilt agent and follow the installation instructions.



To create an agent with [playbooks](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook) or [flows](https://docs.cloud.google.com/dialogflow/cx/docs/basics):

  1. Open the [Conversational Agents console](https://conversational-agents.cloud.google.com).
  2. Select or create a project.
  3. Select **Create agent**.
  4. Select **Build your own**.
  5. Provide an agent name, [location](https://docs.cloud.google.com/dialogflow/cx/docs/concept/region), time zone, and [default language](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-multilingual).
  6. Select a **Conversation start** option. 
     * If you want your agent to begin the conversation using a generative playbook, select **Playbook**.
     * If you want your agent to begin the conversation using a deterministic flow, select **Flow**.
  7. Click **Create**.
  8. The console loads the editor page for the [default playbook](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook#default).



To create an agent with [data store handlers](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store/handler):

  1. Go to the [Conversational Agents console](https://conversational-agents.cloud.google.com).
  2. Select or create a project.
  3. Select **Create agent**.
  4. Select **Create a Q &A Agent**.
  5. You are redirected to the Builder console. Follow the instructions to [create an agent](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store/handler#create-agent).



## Top row navigation

The horizontal row at the top of the interface contains the following controls:

X | Item  
---|---  
Project | The selected [project](https://docs.cloud.google.com/dialogflow/cx/docs/quick/setup#project).  
Agent | The selected [agent](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent).  
Language | The selected [language](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-multilingual) to be used when entering language-specific data, and the **Manage Languages** option which brings you to [flow language settings](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-settings#flow-language).  
Search | Used to search, filter, and access core resources within the agent.  
Collaborators | [Collaborators](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-collaboration) that have access to the agent.  
Export/Import agent | Agent [export and import](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent#export).  
Change history | Agent [change history](https://docs.cloud.google.com/dialogflow/cx/docs/concept/change-history).  
Settings | Agent [settings](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-settings).  
Publish agent | A convenience button for setting up [Dialogflow CX Messenger](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/dialogflow-messenger).  
Simulator | The simulator used for testing the agent.  
Help | Links to documentation and other help content.  
Feedback | Used to provide product feedback.  
  
## Left navigation

X | Item  
---|---  
Playbooks | List, create, and edit generative [playbooks](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook).  
Flows | Visualize, create, and edit deterministic [flows](https://docs.cloud.google.com/dialogflow/cx/docs/basics).  
Tools | List, create, and edit [playbook tools](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/tool).  
Prebuilts | Import ready to use prebuilt agents for a variety of common use cases.  
Test Cases | List and define [test cases](https://docs.cloud.google.com/dialogflow/cx/docs/concept/test-case) to regularly verify agent behavior.  
Conversation History | View the [conversation history](https://docs.cloud.google.com/dialogflow/cx/docs/concept/conversation-history).  
Environments | Create and edit various deployment [environments](https://docs.cloud.google.com/dialogflow/cx/docs/concept/version).  
Versions | Snapshot flow and playbook [versions](https://docs.cloud.google.com/dialogflow/cx/docs/concept/version).  
Integrations | [Integrate your agent](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration) with ready to use user interfaces and other conversation platforms.  
Conversation Profiles | List, create, and edit [conversational profiles](https://docs.cloud.google.com/dialogflow/cx/docs/concept/conversation-profiles) for advanced telephony use cases.  
  
## Simulator

The simulator is used to test your agent. You can have a conversation with your agent while monitoring changes in session state.

### Simulator settings

When you first open the simulator, configure the following settings:

  * **Agent environment:** Select an [environment](https://docs.cloud.google.com/dialogflow/cx/docs/concept/version).
  * **Start resource:** Select a [playbook](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook) or [flow](https://docs.cloud.google.com/dialogflow/cx/docs/concept/flow) to receive the first input.
  * **Model or page:** Select the generative model if the start resource is a playbook, or select a page if the start resource is a flow.



When interacting with the simulator, you provide end-user input as text or audio from your microphone, then press Enter or tap the Send sendbutton.

In addition to plain text, you can choose alternate input types by typing `@` and then selecting an option:

  * **Channel:** Send a [channel](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#channel-specific) value as a query parameter.
  * **DTMF:** Send dual-tone multi-frequency signaling (Touch-Tone) input for telephony interactions.
  * **End-user metadata:** Provide a contextual hint in the form of a JSON object for generative AI to better answer an end-user query. For example, for data store fulfillment or tool input, you could use: `{"firstName": "John", "lastName": "Doe"}`.
  * **Event:** Invoke an [event](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#event).
  * **Cloud Storage uri** : Cloud Storage URI for a file to upload. Use this file for images and documents that provide context to the generative AI.
  * **Parameter:** Inject a [parameter](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter) value. Provide new parameters or preset values for existing parameters.
  * **Parameter scope:** Set the [parameter scope](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#scope).



### Simulator controls

Once the conversation starts, use the following controls at the top of the simulator panel:

  * **Debug trace**
  * **Original response**
  * **Show latency**
  * **Create test case**
  * **Undo**
  * **Replay conversation**
  * **Reset conversation**
  * **Options:**
    * Enable or disable [webhook](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook) calls at any time with the webhook toggle button.
    * Enable or disable [partial responses](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#partial-response).
    * Enable or disable [sentiment analysis](https://docs.cloud.google.com/dialogflow/cx/docs/concept/sentiment).
  * **Save as example:** [See instructions](https://docs.cloud.google.com/dialogflow/cx/docs/quick/build-agent-playbook#provide_examples).



### Simulator history

When you use the simulator to test your agent, the conversation history appears in the simulator panel. Select each turn to expand more details. For agent responses, you can also preview the audio response by tapping the play button for the turn.

[ Previous arrow_back  Important terms  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/important-terms)

[ Next Dialogflow CX console overview  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
