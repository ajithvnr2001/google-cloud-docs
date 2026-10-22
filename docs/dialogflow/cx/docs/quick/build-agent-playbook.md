---
url: https://docs.cloud.google.com/dialogflow/cx/docs/quick/build-agent-playbook/
title: Build an agent using playbooks \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:44:37.682546+00:00
---

# Build an agent using playbooks  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/quick/build-agent-playbook/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Build an agent using playbooks Stay organized with collections  Save and categorize content based on your preferences. 

Build and test a shirt ordering agent using playbooks. Use the agent to ask for the store location, get store hours, or place a shirt order.

## Before you begin

If you haven't already, follow the [setup](https://docs.cloud.google.com/dialogflow/cx/docs/quick/setup) instructions.

## About playbooks

An agent consists of one or more playbooks. Each playbook has a clearly defined and limited scope. The following table describes the data in a playbook:

X | Item  
---|---  
Name | A name used to identify the playbook.  
Goal | [Goals](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/goal) are high-level descriptions of what the playbook should accomplish.  
Instructions | [Instructions](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/instruction) are high-level steps that should be taken to accomplish the playbook's goal.  
Examples | [Examples](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/example) are sample conversations between an end-user and the agent. These examples are effectively few-shot prompt examples for the LLM.  
  
## Create an agent

To create an agent:

  1. Go to the https://conversational-agents.cloud.google.com.
  2. If you haven't already, select or create a project.
  3. Click **Create agent**.
  4. Click **Build your own**.
  5. Enter "Shirt Ordering - Playbooks" for the agent name.
  6. Enter a [location](https://docs.cloud.google.com/dialogflow/cx/docs/concept/region).
  7. Enter a time zone.
  8. Enter a [default language](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-multilingual).
  9. Select **Playbook** for the **Conversation start** option.
  10. Click **Create**.
  11. The user interface takes you to the default playbook named **Default Generative Playbook**.
  12. Click **Back** to return to the playbook list.



## Create the order playbook

The **Order** playbook handles shirt orders.

To create the playbook:

  1. Click **Create**.
  2. Select the **Task playbook** option.
  3. Enter the playbook name: `Order`.
  4. Enter the following goal:
         
         You are a shirt store ordering assistant. Help customers purchase shirts.
         Help the customer choose a size and color.
         The shirts come in small, medium, and large.
         The shirts can be red, green, or blue.
         

  5. Enter the following instructions:
         
         - If the customer has not provided a size, ask them to choose a size.
         - If the customer has not provided a color, ask them to choose a color.
         - Once the customer has selected a size and color for the shirt,
           repeat the selection to the customer, and ask them to confirm the selection.
         - Once the customer has confirmed their selection,
           let them know that the shirt is now ordered.
         - Do not provide prices or collect payment.
         - Do not collect the customer's name or address.
         

  6. Click **Save**.

  7. Click **Back** to return to the playbook list.




## Create the information playbook

The **Information** playbook handles questions about the store.

To create the playbook:

  1. Click **Create**.
  2. Select the **Task playbook** option.
  3. Enter the playbook name: `Information`.
  4. Enter the following goal:
         
         You provide information about a shirt store.
         The store is open between 8 AM and 6 PM every day.
         The store is located at 1007 Mountain Drive, Gotham City, NJ.
         

  5. Enter the following instructions:
         
         - If the customer asks for the store location, provide them with the address.
         - If the customer asks for the store hours, provide them with the hours.
         

  6. Click **Save**.

  7. Click **Back** to return to the playbook list.




## Update the default playbook

When you first create the agent, a default playbook is created for you. This playbook steers the conversation to the appropriate playbooks with specific goals. You can see how the default playbook references the other playbooks in the following instructions.

To update the playbook:

  1. Click the default playbook, which is marked with a star.
  2. Enter the following goal:
         
         You are an assistant for a shirt store.
         Your name is "Samantha".
         Your job is to direct customers to other playbooks based on the customer's questions.
         

  3. Enter the following instructions:
         
         - If the customer hasn't been greeted yet, greet the customer,
           introduce yourself, and ask how you can help.
         - If the customer wants information about the store,
           route them to ${PLAYBOOK: Information}
         - If the customer wants to purchase a shirt,
           route them to ${PLAYBOOK: Order}
         

  4. Click **Save**.

  5. Observe that the playbook references are highlighted because there are no examples yet; you will add these in the next section.

  6. Click **Back** to return to the playbook list.




## Provide examples

The playbook is functional, but providing [examples](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/example) ensures quality responses.

You can provide examples from the **Examples** tab when a playbook is open; however, it's often easier to have a conversation with the agent and save the conversation as an example.

A default playbook conversation is short. This playbook needs to direct the conversation to another playbook.

To have a conversation with the default playbook:

  1. Close or cancel any panel that might be present on the right side of the screen.
  2. Tap the simulator question_answer button in the top row navigation.
  3. For resource, select the default playbook.
  4. Use the default model or select an alternative.
  5. In the **Enter user input** field, enter `Hello`, and then press Enter.
  6. The playbook responds with a greeting.



To save this conversation as an example:

  1. Select the default playbook in the **Invocations** list.
  2. Click **Save as example**.
  3. In the example editor panel, add, edit, delete, or reorder actions.
  4. Enter `Greeting` as the example name.
  5. Update the playbook responses as needed.
  6. In the **End example with output information** section, enter `The user is greeted.` in the **Summary** field.
  7. Click **Save**.



Add a location example for the information playbook:

  1. Close or cancel any panel on the right side of the screen.
  2. If necessary, reset the conversation with the **reset** restart_alt button.
  3. Select the information playbook in the simulator **Start Resource** menu.
  4. Type `Where are you located?` and press Enter.
  5. Select the information playbook in the **Invocations** menu.
  6. Click **Save as example**.
  7. Enter `Location` as the example name.
  8. Delete the action that contains `Where are you located?` because only default playbook examples can start with a user action.
  9. Expand the **Summary of the preceding conversation** section and enter `The customer asked "Where are you located?"` in the **Starts example with input information** field.
  10. Expand the **Summary of the playbook execution** section and enter `The store is located at 1007 Mountain Drive, Gotham City, NJ.` in the **End example with output information** field.
  11. Click **Save**.



Add an hours example for the information playbook:

  1. Select the information playbook in the simulator.
  2. Enter the message `What are your hours?`.
  3. Save the conversation as an example named `Hours`.



Add a selection example for the order playbook by following these steps:

  1. Name the example `Selection`.
  2. Select the order playbook.
  3. Send the following messages: 
     * `I want to buy a shirt`
     * `Large`
     * `Green`
     * `Yes`



## Test the agent

Your agent is now ready to be tested. Open the simulator panel and have a conversation with the agent. You can have conversations different from those described earlier. For example, you can ask this agent which colors are available for shirts. If you are not achieving the needed results, refining or adding examples will improve responses.

## Interact with the agent using the API

For more information about interacting with the API, see [Interactions with the API](https://docs.cloud.google.com/dialogflow/cx/docs/quick/api).

[ Previous arrow_back  Setup and cleanup  ](https://docs.cloud.google.com/dialogflow/cx/docs/quick/setup)

[ Next Build an agent using flows  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/quick/build-agent)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
