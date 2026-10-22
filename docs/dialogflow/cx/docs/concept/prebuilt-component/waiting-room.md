---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/waiting-room/
title: Waiting room prebuilt component \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:45:06.607295+00:00
---

# Waiting room prebuilt component  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/waiting-room/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Waiting room prebuilt component Stay organized with collections  Save and categorize content based on your preferences. 

The waiting room [prebuilt component](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component) allows you to configure your agent so that end-users may ask the agent to hold, for example in scenarios where the end-user may need some time to retrieve requested information. [Waiting room functionality](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#waiting-room-functionality) is implemented in several prebuilt components and can be added additionally to non-prebuilt agents and components.

## Limitations

In addition to the [common prebuilt component limitations](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#limits), this prebuilt component has the following limitations:

  * Waiting room does not extend the session's timeout, see [Sessions](https://docs.cloud.google.com/dialogflow/cx/docs/concept/session) for default behavior.
  * By default, the waiting room component will exit after three no-matches or three no-input [built-in events](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#event-built-in), timing out according to the no-speech timeout configured in [Advanced speech settings](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-settings#settings-speech). To increase this limit, configure the no-match and no-input event handlers in the `Main` page.
  * Waiting room will exit after the session times out or after it has exhausted the event handlers on the `Main` page, whichever occurs first.



## Sample dialogs

The following sample dialogs demonstrate common scenarios handled by this prebuilt component.

### Successful hold

End-user asks the agent to hold. Once the user says "I'm ready", the agent returns to the conversation. 

User input | Agent response  
---|---  
| Please say or enter the first part of your credit card number. You can say "play back" at any time to hear the current collected numbers.  
I need a minute |   
| No worries. Let me know when you're ready.  
Okay I'm ready now |   
| Let's get you back to where you were.  
  
Please say or enter the first part of your credit card number. You can say "play back" at any time to hear the current collected numbers.  
  
### Unrecognized input

User input | Agent response  
---|---  
| Please say or enter the first part of your credit card number. You can say "play back" at any time to hear the current collected numbers.  
I need a minute |   
| No worries. Let me know when you're ready.  
Nice |   
| Sorry, I didn't get that. I'm waiting till you're ready to proceed. You can say "I'm ready" and we'll continue where we left off.  
That's fine |   
| Hmm, I still wasn't able to get that. Please make sure you're saying "ready"  
I'm not sure |   
| Sorry, I'm having difficulty understanding your response.  
  
## Naming conventions

This prebuilt component uses the following naming conventions:

Feature | Format | Example  
---|---|---  
Flow | [Component Name] | Waiting Room  
Component Specific Intent | prebuilt_components_[component_name]_[intent_name] | prebuilt_components_waiting_room  
  
## Basic setup

To set up this prebuilt component:

  1. [Import the prebuilt component](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#import).
  2. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects).
  3. Choose your Google Cloud project.
  4. Select your agent.
  5. Select the **Build** tab.
  6. Click the Start Page in the **Pages** section.
  7. Add a new route using the `prebuilt_components_waiting_room` intent, which will make this intent accessible from any page in the flow. For more detail, see [Flow-level routes](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#route-flow).
  8. Click **Save**.
  9. On pages where you want to enable the waiting room, add two new routes. 
     1. The first route allows the conversation to return to the page where the end-user originally asked the agent to hold: 
        1. [Condition](https://docs.cloud.google.com/dialogflow/cx/docs/reference/condition): `$session.params.from_waiting_room_reusable_flow = true`
        2. [Parameter presets](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#param-preset): 
           * Parameter: `from_waiting_room_reusable_flow`
           * Value: `false`
        3. [Transition page](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#symbolic): Current page
     2. The second route determines what happens after an end-user has exceeded their retry limit for no-match or no-input in the waiting room flow: 
        1. [Condition](https://docs.cloud.google.com/dialogflow/cx/docs/reference/condition): `$session.params.waiting_room_event_handler = true`
        2. [Parameter presets](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#param-preset): 
           * Parameter: `waiting_room_event_handler`
           * Value: `null`
        3. [Transition page](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#symbolic): should be set according to what should happen after the end-user has used all their retry attempts for the waiting room flow, for example routing to another page, ending the flow, or ending the session.



### Complete

Your agent should now be set up and ready to test.

[ Previous arrow_back  Transaction history  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/transaction-history)

[ Next Zip code collection  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/zip-code-collection)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
