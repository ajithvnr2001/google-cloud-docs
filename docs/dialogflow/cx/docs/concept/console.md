---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/console/
title: Dialogflow CX console overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:43:14.340163+00:00
---

# Dialogflow CX console overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/console/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Dialogflow CX console overview Stay organized with collections  Save and categorize content based on your preferences. 

**Deprecated:** The Dialogflow CX console [has been replaced](https://docs.cloud.google.com/dialogflow/docs/release-notes#October_16_2025) by the [Conversational Agents console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents).

Dialogflow CX provides a web user interface called the Dialogflow CX console ([visit documentation](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console), [open console](https://dialogflow.cloud.google.com/cx/projects)). You use this console to create, build, and test agents. It graphs each flow as a conversational state machine diagram, which makes complex agents easy to design and understand.

The Dialogflow CX console is different from the [Google Cloud Console](https://support.google.com/cloud/answer/3465889?ref_topic=3340599), which is used to manage Google Cloud-specific Dialogflow CX settings (for example, billing) and other Google Cloud resources.

In most cases you should use the Dialogflow CX console to build agents, but you can also use the Dialogflow API to build agents for advanced scenarios.

## How the console is used

The console is used to create, build, manage, fine-tune, and test your projects and agents. With it, you can:

  * Create [projects](https://docs.cloud.google.com/dialogflow/cx/docs/quick/setup#project).
  * Create [agents](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent) that contain all settings and data that define the conversational experience.
  * Create [flows](https://docs.cloud.google.com/dialogflow/cx/docs/concept/flow) and [pages](https://docs.cloud.google.com/dialogflow/cx/docs/concept/page) that are the building blocks for conversation control.
  * Create [entities](https://docs.cloud.google.com/dialogflow/cx/docs/concept/entity) to extract useful data from end-user input.
  * Create [intents](https://docs.cloud.google.com/dialogflow/cx/docs/concept/intent) that categorize end-user input.
  * Test your agent via the simulator.
  * And more ...



## Project selector

When you initially load the console, you must select a [project](https://docs.cloud.google.com/dialogflow/cx/docs/quick/setup#project). The project selector interface is used to:

  * Select pre-existing projects
  * Create new projects



![Project selection screenshot](https://docs.cloud.google.com/static/dialogflow/cx/docs/images/project-selection.png)

## Agent selector

Once you select a project, you must select an agent. The agent selector interface is used to:

  * Select existing agents
  * [Create new agents](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent#create)
  * [Create prebuilt agents](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agents-prebuilt)
  * [Export and restore agents](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent#export)
  * [Delete agents](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent#del)
  * Configure [location settings](https://docs.cloud.google.com/dialogflow/cx/docs/concept/region#location-settings)
  * Filter agents by location



![Agent selection screenshot](https://docs.cloud.google.com/static/dialogflow/cx/docs/images/agent-selection.png)

## Agent builder

Once a project and agent has been selected, the agent builder loads. The builder is arranged in the following panels:

![Agent builder screenshot](https://docs.cloud.google.com/static/dialogflow/cx/docs/images/cx-console-layout.png)

### Console menu (1)

You can use this menu to switch between consoles.

### Project and agent selection (2)

You can use these menus to change the project, agent, or currently active language for [multilingual agents](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-multilingual).

### Search bar and task indicator (3)

Use the [search bar](https://docs.cloud.google.com/dialogflow/cx/docs/concept/search) _search_ to search, filter, and access the core resources within the agent. The task indicator _hourglass_full_ shows the status of tasks like training.

### Build and Manage tabs (4)

The **Build** tab contains sections for managing flows and pages. When you select a flow in the flow section, the pages contained within the flow are listed in the pages section.

The **Manage** tab contains resources and tools available to the agent: intents, entity types, webhooks, etc.

### Graph settings (5)

These buttons provide various controls for viewing and interacting with the agent graph.

### Agent settings and simulator buttons (6)

The _settings_ **Agent Settings** button opens the agent settings panel. The _forum_ **Test Agent** button opens the simulator panel.

### Graph (7)

The graph shows a visual representation of the selected flow, similar to a state machine diagram. Each node of the graph represents a page or flow start page. You can click a node to expand or contract it. When expanded, you can edit a nodes data.

The first node of the graph, called **Start** , is the start page of the flow.

Connecting lines from one node to another represent possible [transitions](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler). They are color-coded in the following way:

  * Blue represents transitions defined for intent requirements or for intent and condition requirements.
  * Orange represents transitions defined for condition requirements only.
  * Cyan represents transitions defined for [event handlers](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#event).
  * Grey represents transitions other than described above (for example, a mixture of the above mentioned transition types).



When a transition can lead to another flow, the target flow is shown as a node.

### Editing and simulator panels (8)

When editing agent content or testing the agent with the simulator, content-specific panels open on the right side of the console. These panels can be expanded to fill available console area, contracted to fill a portion of the right side of the console, or closed when you are finished.

## Simulator

The simulator is used to test your agent. You can have a conversation with your agent while monitoring changes in session state.

You can also use the simulator to create executable [test cases](https://docs.cloud.google.com/dialogflow/cx/docs/concept/test-case).

### Simulator settings

When you first open the simulator, you need to select an [agent environment or flow versions](https://docs.cloud.google.com/dialogflow/cx/docs/concept/version) and an active [flow](https://docs.cloud.google.com/dialogflow/cx/docs/concept/flow). In most cases, you should use the draft environment and default start flow.

From buttons above the simulator, you can also:

  * Enable or disable [webhook](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook) calls at any time with the webhook toggle button.
  * Enable or disable [partial responses](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#partial-response).
  * Enable or disable [sentiment analysis](https://docs.cloud.google.com/dialogflow/cx/docs/concept/sentiment).



### Simulator input

When interacting with the simulator, you provide end-user input as text, then press enter or click the send sendbutton. In addition to plain text, you can choose alternate input types with the input input selector:

  * **Parameter** : Inject a [parameter](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter) value. You can provide new parameters or provide preset values for existing parameters.
  * **Event** : Invoke an [event](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#event).
  * **DTMF** : Send dual-tone multi-frequency signaling (Touch-Tone) input for telephony interactions.



### Simulator session state

When using the simulator to have a conversation with your agent, session state is shown to the left of the conversation. The currently active flow, currently active page, populated parameter values, and [execution steps](https://docs.cloud.google.com/dialogflow/cx/docs/concept/page#visualization) are shown. This information may help you debug an agent or verify its behavior in certain conversation scenarios.

### Simulator limitations

For the simulator, the following limitations apply:

  * You cannot set a parameter value to null.
  * Conversations created using simulator are inaccessible using API methods.



[ Previous arrow_back  Conversational Agents console overview  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents)

[ Next Agents  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
