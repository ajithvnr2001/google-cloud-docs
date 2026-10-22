---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/custom-events/
title: Custom events and custom UI module connectors \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:54:55.447702+00:00
---

# Custom events and custom UI module connectors  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/custom-events/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Custom events and custom UI module connectors Stay organized with collections  Save and categorize content based on your preferences. 

All communication between an [Agent Assist UI module](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/ui-modules) and its connector happens through **custom events**. The **UI module connector** facilitates events between the agent desktop and the UI modules.

For example, when an Agent Assist suggestion is received, a UI module connector service will dispatch an `analyze-content-received` event to the UI modules, and the modules are subscribed to such events.

## Custom event details

For the full list of UI module events and their payloads, see the [UI module events API documentation](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/ui-modules-events-documentation).

To manually dispatch a custom event, use the following syntax:
    
    
        dispatchAgentAssistEvent('event_name', {
          detail: event_payload,
        });
    

The following example shows how to dispatch the `analyze-content-received` event:
    
    
    if (newMessageFromHumanAgent) {
      dispatchAgentAssistEvent('analyze-content-received', {
        detail: {
          participantRole: 'HUMAN_AGENT',
          request: {
            textInput: {text: newMessageFromHumanAgent},
            messageSendTime: new Date().toISOString()
          }
        }
      });
    }
    

After you dispatch a custom event, you see the following in the UI module connector service:
    
    
        this.api.analyzeContent(...).then(function (response) {
          dispatchAgentAssistEvent('analyze-content-response-received', {
           detail: {response: response}});
        });
    

And you will see the following in the module:
    
    
        addAgentAssistEventListener('analyze-content-response-received', function (event) {
          // Use the AnalyzeContent response to render suggestions in the UI.
        });
    

To manually subscribe to a custom event, use the following syntax:
    
    
        addAgentAssistEventListener('event_name', function (event) {
          // `event.detail` contains the event payload.
        });
    

The following example shows a custom event subscription:
    
    
    addAgentAssistEventListener('smart-reply-selected', function (event) {
      var chipContent = event.details;
      // Populate the agent chat box with the selected Smart Reply chip.
    });
    

## Custom UI module connectors

You can also use custom events to create your own custom UI module connectors, which allow you to integrate the UI modules into an agent desktop that isn't supported by Agent Assist. For more information about implementing modules and connectors, see the [implementation documentation](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/ui-modules).

If you're integrating Agent Assist UI modules into any agent desktop without a prebuilt UI module connector, you will need to write a custom one. Once you have created a custom UI module connector, return to the [UI module implementation](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/ui-modules#implement_the_ui_module_connector) documentation for details about configuring your connectors and implementing the modules. You can use a custom UI module connector with any UI module client.

A custom UI module connector must be responsible for the following operations:

  1. Dispatching an event to select the active conversation. This will initialize the conversation along with its participants. Event name: `active-conversation-selected`
  2. For chat conversations, dispatching an event whenever a new utterance is registered from the agent or customer. Event name: `analyze-content-requested`
  3. Notifying the module system when 'dark mode' has been toggled in the primary application. Event name: `dark-mode-toggled`
  4. Dispatching an event to request that the conversation is marked as complete on the backend. Event name: `complete-conversation-requested`



In addition, a custom UI module connector must subscribe to the following events to update the agent desktop UI where applicable:

  1. For Smart Reply, update the agent's input field whenever a Smart Reply chip is selected. Event name: `smart-reply-selected`.
  2. For Generative Knowledge Assist, update the agent's input field whenever a knowledge assist answer is pasted into the input box. Event name: `knowledge-assist-v2-answer-pasted`.



## Initialize multiple UI modules instances with `namespace`

To load multiple instances of the UI modules on the same page, agent desktops need multiple initialization instances. To keep them separate, at initialization, pass a `namespace` configuration option to the [UI modules](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/ui-modules-companion-agent#attributes) and the [`UIModulesConnector`](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/ui-modules#implement_the_ui_module_connector).

Use this option if you notice messages and suggestions shared between distinct conversations in your agent desktop. For example:
    
    
    const connector = new UiModulesConnector();
    const config = {};
    // ...other UI module connector config options
    config.uiModuleEventOptions = { namespace: this.recordId }
    
    const companionAgentElement = document.createElement("agent-assist-companion-agent");
    // ...other UI modules HTML attributes
    companionAgentElement.setAttribute("namespace", this.recordId);
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
