---
url: https://docs.cloud.google.com/dialogflow/cx/docs/quick/build-agent/
title: Build an agent using flows \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:08:57.476726+00:00
---

# Build an agent using flows  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/quick/build-agent/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Build an agent using flows Stay organized with collections  Save and categorize content based on your preferences. 

This guide shows how to use the Dialogflow CX console to build and test a shirt ordering agent using flows. When interacting with this agent, ask for the store location, get store hours, or order a shirt.

The following diagram shows the completed agent for this guide:

![Agent graph screenshot](https://docs.cloud.google.com/static/dialogflow/cx/docs/images/shirt-1-flow-graph.png)

## Before you begin

Complete the following tasks before you read this guide:

  * Read [flow basics](https://docs.cloud.google.com/dialogflow/cx/docs/basics).
  * Perform [setup steps](https://docs.cloud.google.com/dialogflow/cx/docs/quick/setup).



## Create an agent

Create an agent for this guide:

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects).
  2. Create or choose a project.
  3. Click **Create agent**.
  4. Select **Build your own**.
  5. Complete the form for basic agent settings: 
     1. Enter a display name.
     2. Select a [location](https://docs.cloud.google.com/dialogflow/cx/docs/how/region#avail). Click the **Edit** button if you want to change advanced [location settings](https://docs.cloud.google.com/dialogflow/cx/docs/how/region#location-settings).
     3. Select a time zone.
     4. Select the default language.
     5. Optionally, enable Cloud Logging.
  6. Click **Save**.



## Optional agent import

This guide walks you through the steps to build a shirt ordering agent.

To skip the console steps, download the [agent](https://docs.cloud.google.com/static/dialogflow/cx/docs/data/agent-shirts-1-flow.zip) and [import it](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent#export).

## Default flow and intents

The following flow and intents are created automatically for a new agent.

You can find the intents by clicking **Manage** and then **Intents** , and you can find the flow by clicking **Build**.

X | Item  
---|---  
Default Welcome Intent | The [Default Welcome Intent](https://docs.cloud.google.com/dialogflow/cx/docs/concept/intent#welcome) has training phrases like "Hi" or "Hello" that are meant to match initial end-user input. You can edit this intent as needed.  
Default Negative Intent | The [Default Negative Intent](https://docs.cloud.google.com/dialogflow/cx/docs/concept/intent#negative) can be used to add training phrases to this intent that act as negative examples.  
Default Start Flow | The [Default Start Flow](https://docs.cloud.google.com/dialogflow/cx/docs/concept/flow#start) can be used as your only flow. It is the only flow that will be used in this guide. For more complex agents, you can add more flows. This flow has a default [intent route](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#route) with the **Default Welcome Intent** as an intent requirement.  
  
### Test default welcome response message

The default flow and intents can handle a basic conversation with only a welcome message.

To test your new agent:

  1. Click the **Test Agent** button to open the simulator.
  2. Enter `hello` in the text field and press Enter.
  3. The agent responds with a default welcome message.
  4. Close the simulator.



![Simulator screenshot](https://docs.cloud.google.com/static/dialogflow/cx/docs/images/quick-hello-default-response.png)

The agent performs the following steps for this end-user input:

  1. When you provide input, the agent evaluates the state handlers in scope for the active [Default Start Flow](https://docs.cloud.google.com/dialogflow/cx/docs/concept/flow#start) and [flow start page](https://docs.cloud.google.com/dialogflow/cx/docs/concept/flow#start-page).
  2. The agent identifies a route that matches the **Default Welcome Intent** and executes it.
  3. The agent selects one of the fulfillment response messages at random and adds it to the [response queue](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#queue).
  4. Because the route has no transition target, the active flow and page remain unchanged.
  5. The agent sends the contents of the response queue to you.



### Edit the welcome response message

To edit the welcome response message:

  1. Click the **Build** tab.
  2. Select the **Default Start Flow** in the **Flows** section.
  3. Click the **Start Page** node in the graph.
  4. Find the route with the **Default Welcome Intent** as an intent requirement and click it to open the route editing panel.
  5. In the fulfillment section, under the agent responses subsection, delete all existing response messages.
  6. Add `Hello, this is a shirt ordering virtual agent. How can I help you?` as the only response.
  7. Click **Save**.
  8. Close the route editing panel.



![Agent response screenshot](https://docs.cloud.google.com/static/dialogflow/cx/docs/images/quick-hello-edited-response.png)

### Test the updated welcome response message

To test your updated response:

  1. Click the **Test Agent** button to open the simulator.
  2. Enter `hello` in the text field and press Enter.
  3. The agent responds with your new message.
  4. Close the simulator.



## Store location page

A Dialogflow CX conversation (session) can be described and visualized as a [state machine](https://en.wikipedia.org/wiki/Finite-state_machine). The states of a CX session are represented by [pages](https://docs.cloud.google.com/dialogflow/cx/docs/concept/page). Because you only have one page, the agent is not very useful. In this section, create another page that handles questions about the store's location.

### Create the location intent

An [intent](https://docs.cloud.google.com/dialogflow/cx/docs/concept/intent) categorizes an end-user's intention for one conversation turn.

To create an intent that is matched when end-user input requests the store's location:

  1. Select the **Manage** tab.
  2. Click **Intents**.
  3. Click **Create**.
  4. Enter `store.location` for the intent display name.
  5. Enter the following training phrases: 
     * `Where is the store?`
     * `Directions`
     * `Tell me the address`
     * `Where do I pick up my order?`
     * `How do I get there?`
     * `Where is the store located?`
     * `What street are you on?`
     * `What is your address?`
     * `How do I get to your store?`
     * `Where are you located?`
  6. Click **Save**.



![intent screenshot](https://docs.cloud.google.com/static/dialogflow/cx/docs/images/quick-store-location-intent.png)

### Create the location page

Create a new page. You can add an _entry fulfillment_ to this page that runs whenever the page becomes active. This entry fulfillment should have a response message that provides the store's location.

To create the store location page:

  1. Click the **Build** tab.
  2. Select the **Default Start Flow** in the **Flows** section.
  3. Click the **add** _add_ button in the **Pages** section. A text entry for the page display name appears.
  4. Enter `Store Location` for the display name of the page and press Enter.
  5. Click the **more_vert** _more_vert_ button next to the page display name.
  6. Select **Edit** to open the page editing panel.
  7. Find **Entry fulfillment** and click **Edit fulfillment**.
  8. Click **+Add dialogue response** to enter `Our store is located at 1007 Mountain Drive, Gotham City, NJ.` in the **Agent dialogue** field of the **Agent responses** section.
  9. Click **Save**.
  10. Close the page editing panel.



![page screenshot](https://docs.cloud.google.com/static/dialogflow/cx/docs/images/quick-store-location-page.png)

### Add a location intent route to the flow

Now, create a route that has the Store Location page as a transition target. When this route is called, the session transitions to the Store Location page. This route is applied to the **Default Start Flow** , so it is in scope as long as the flow is active.

For a single-flow agent, this means that the route is always in scope. At any point in the conversation, an end-user can ask for the store location, and this route will be called.

To create the route:

  1. Click the **Build** tab.
  2. Select the **Default Start Flow** in the **Flows** section.
  3. Click the **Start Page** node in the graph. This is the start page for the **Default Start Flow**.
  4. Add the following intent route: 
     * **Intent:** `store.location`
     * **Transition Page:** `Store Location`
  5. Click **Save**.
  6. Close the intent route editing panel.



![intent route screenshot](https://docs.cloud.google.com/static/dialogflow/cx/docs/images/quick-store-location-intent-route.png)

After you close the editing panel, a node for your new page appears on the graph. The arrow from the **Start** node to the **Store Location** node shows how the session transitions between nodes.

### Test the store location page

To test your page:

  1. Click the **Test Agent** button to open the simulator.
  2. Enter `What is the store location?` and press the Enter key.
  3. The agent provides the address.
  4. Close the simulator.



The agent performs the following steps for this end-user input:

  1. When you provide input, the agent evaluates the state handlers in scope for the active [Default Start Flow](https://docs.cloud.google.com/dialogflow/cx/docs/concept/flow#start) and [flow start page](https://docs.cloud.google.com/dialogflow/cx/docs/concept/flow#start-page).
  2. The agent identifies a route that matches the **store.location** intent and executes it.
  3. Because the route has no fulfillment response messages, the agent adds nothing to the response queue.
  4. The agent transitions the session to the **Store Location** page.
  5. The agent adds the entry fulfillment response message from the **Store Location** page to the response queue.
  6. The agent sends the contents of the response queue to you.



## Store hours page using inline creation

In this section, you create a **Store Hours** page that handles end-user questions about store hours. Previously, you created pages and intents from the **Build** and **Manage** tabs. This section shows you a faster way of creating these components with inline creation.

To inline create an intent route, intent, and page:

  1. Click the **Start Page** node in the graph.
  2. Next to **Routes** , click _add_ **Add**. The intent route editing panel opens.
  3. In the **Intent** section, select **New intent**. The intent editing panel opens.
  4. Create a `store.hours` intent with the following training phrases:

     * `What are your store hours?`
     * `What time do you close?`
**Note:** Production agents must have at least 10 training phrases per intent.
  5. Click **Save**. The intent editing panel closes.

  6. Go to the **Transition** section in the route editing panel.

  7. For **Page** transition, select **New page**.

  8. Enter `Store Hours` in the text entry that appears.

  9. Click **Save**. The new page appears on the graph because there is now a transition that leads to it.

  10. Close the route editing panel.

  11. Add an entry fulfillment that provides the store hours, as you did for **Store Location**.

  12. Close any open editing panels.




## Order item page

Next, create a page that uses [form parameters](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter#form). When you request a new shirt order, the session transitions to this page, which collects the size and color for the shirt order.

### Create a custom entity type for shirt size

[Entity types](https://docs.cloud.google.com/dialogflow/cx/docs/concept/entity) control how data from end-user input is extracted. Dialogflow CX provides predefined system entities that match common data types, such as dates, times, colors, and email addresses. You can also create custom entities for specific data.

For this agent, you can use a system entity for the shirt color, but you need to create a custom entity for the shirt size.

The size entity type should have the following entity entries:

Entity | Synonyms  
---|---  
Small | small, tiny, little  
Medium | medium, regular, average  
Large | large, big, giant  
  
To create the entity:

  1. Select the **Manage** tab.
  2. Click **Entity Types**.
  3. Click **Create**.
  4. Set the display name to `size`.
  5. Add the entity entries listed in the table.
  6. Click **Save**.



### Create an order intent with intent parameters

You need an intent that is matched when the end-user requests a new shirt order. This intent should also optionally capture the chosen shirt color or size if the end-user provides that information initially.

[Parameters](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter) are used to capture and reference values supplied by the end-user during a session. Each parameter has a display name and an entity type. Unlike raw end-user input, parameters are structured data that you can use to perform logic or generate responses.

You control how end-user data is extracted with intent matching by [annotating](https://cloud.google.com/dialogflow/cx/docs/concept/intent#annot) parts of your training phrases and configuring the associated [intent parameters](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter#intent).

For example, consider a training phrase like "What is the forecast tomorrow for Tokyo?" You can annotate "tomorrow" with a `date` parameter and "Tokyo" with a `location` parameter. When you annotate parts of a training phrase, Dialogflow CX recognizes that these parts are just examples of actual values that can be provided by end-users at runtime.

For an end-user input like "What is the forecast on Friday for Sydney?", Dialogflow CX can extract the `date` parameter from "Friday" and the `location` parameter from "Sydney".

To annotate a training phrase in the console:

  1. Highlight the part of the training phrase you want to annotate.
  2. Select the needed entity type from the list.
  3. Dialogflow creates a parameter in the following parameter table.



Create an intent named `order.new` by following these steps:

  1. For each phrase that contains a color, annotate the color with a `color` parameter and the `@sys.color` system entity type.
  2. For each phrase that contains a shirt size, annotate the size with a `size` parameter and the `@size` custom entity type that you created earlier.



Your training phrases and parameters should look similar to the following:

![Intent screenshot](https://docs.cloud.google.com/static/dialogflow/cx/docs/images/shirt-order-training-phrases.png)

### Create an order page

Create a new order page:

  * **Display name:** `New Order`
  * **Entry fulfillment:** `Ok, let's start a new order.`



### Add a form to the order page

For each page, you can define a [form](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter#form), which is a list of parameters that should be collected from the end-user for the page. The agent interacts with the end-user for multiple conversation turns, until it has collected all of the required _form parameters_ , also called _page parameters_. For each form parameter, you also provide _prompts_ that the agent uses to request that information from the end-user. This process is called _form filling_.

When an end-user supplies intent parameters for an intent match, the intent parameters become [session parameters](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter#session). When a page initially becomes active, all of its form parameters are pre-filled with any session parameters that have the same name. So, if the end-user supplies size or color when the **order.new** intent is matched, these values are automatically filled for the form.

Define two required form parameters for the _New Order_ page:

Required | Display name | Entity type | Is list | Prompt  
---|---|---|---|---  
check_box | color | @sys.color | check_box_outline_blank | What color would you like?  
check_box | size | @size | check_box_outline_blank | What size do you want?  
  
To add this form:

  1. Click the **New Order** page in the graph.
  2. Click the **Parameters** add button _add_ to open the parameters editing panel.
  3. Add the parameters as described in the table above.
  4. Click **Save**.
  5. Close the parameters editing panel.



### Add a order intent route to the flow

Add a route to the **Default Start Flow** that transitions to the **New Order** page when the end-user wants to make a new order:

  * Intent: **order.new**
  * Transition target page: **New Order**



## Confirmation page

The final page confirms the order and ends the session.

### Create the confirmation page

Create a confirmation page with a response that uses the session parameters to confirm the order:

  * Display name: `Order Confirmation`
  * Entry fulfillment: `You can pick up your order for a $session.params.size, $session.params.color shirt in 7 to 10 business days. Goodbye.`



### Add condition routes to the order page

You can use [conditions](https://docs.cloud.google.com/dialogflow/cx/docs/reference/condition) to determine whether a route is called. Conditions are commonly used to check whether a form is complete, or they are configured to always be called when evaluated.

To set conditions in the console, see the [Set conditions](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#cond) documentation.

Add the following route to the order page, which is called when the order page form is filled. This condition route uses parameter references in its response to the end-user and transitions the session to the **Order Confirmation** page.

  * **Condition:** `$page.params.status = "FINAL"`
  * **Agent Says:** `You have selected a $session.params.size, $session.params.color shirt.`
  * **Transition Page:** `Order Confirmation`



Add the following route to the order page. This route runs for each conversational turn while the page is active and the condition route is evaluated. When the aforementioned condition is evaluated and called, the page becomes inactive, so this _true_ condition route is not evaluated:

  * **Condition:** `true`
  * **Agent Says:** `I'd like to collect a bit more information from you.`



### Create a condition route to end the session

Add the following condition route to the **Order Confirmation** page to end the session after the page becomes active and its entry fulfillment is processed:

  * **Condition:** `true`
  * **Transition Target Page:** `End Session`



### Test the completed agent

Test the agent with the following dialogue:

Dialogue | Explanation  
---|---  
**End-user:** Hi  
**Agent:** Hello, this is a shirt ordering virtual agent. How can I help you?  | 

  1. The **Default Welcome Intent** route in the **Default Start Flow** is called. 
  2. The fulfillment for this state handler ("Hello, this...") is added to the response queue. 
  3. The agent sends the response queue to the end-user. 

  
**End-user:** I want to buy a blue shirt  
**Agent:** Ok, let's start a new order.  
**Agent:** I'd like to collect a bit more information from you.  
**Agent:** What size do you want?  | 

  1. The **order.new** intent route in the **Default Start Flow** is evaluated. 
  2. The **order.new** intent is matched, and the **color** intent parameter is set to "blue". 
  3. The session transitions to the **New Order** page, and the **color** intent parameter becomes a session parameter. 
  4. The **New Order** page has an entry fulfillment ("Ok, let's start..."), so this is added to the response queue. 
  5. The **color** session parameter is used to fill the like-named form parameter. 
  6. The true condition route in the **New Order** page is evaluated and called. It has a response message ("I'd like to collect..."), so this is added to the response queue. 
  7. The pages's form is not filled, so the agent uses the size prompt ("What size...") and adds this to the response queue. 
  8. The agent sends the response queue to the end-user. 

  
**End-user:** large  
**Agent:** You have selected a large, blue shirt.  
**Agent:** You can pick up your order for a large blue shirt in 7 to 10 business days. Goodbye.  | 

  1. The end-user input fills the **size** parameter requested by the agent in the previous conversation turn. 
  2. The form completion route in the **New Order** page is evaluated and called. It has a fulfillment ("You have selected..."), which is added to the response queue with its parameter references resolved to actual values supplied by the end-user. 
  3. The session transitions to the **Order Confirmation** page. 
  4. The **Order Confirmation** page has an entry fulfillment ("You can pick up..."), which is added to the response queue. 
  5. The agent sends the response queue to the end-user. 
  6. The session transitions to **End Session**. 

  
  
## Prepare for production

Before you run your agent in production, implement the [Best practices for production](https://docs.cloud.google.com/dialogflow/cx/docs/concept/best-practices#prod).

[ Previous arrow_back  Build an agent using playbooks  ](https://docs.cloud.google.com/dialogflow/cx/docs/quick/build-agent-playbook)

[ Next Create a webhook  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/quick/webhook)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
