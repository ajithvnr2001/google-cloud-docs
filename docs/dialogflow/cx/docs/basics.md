---
url: https://docs.cloud.google.com/dialogflow/cx/docs/basics/
title: Flow-based agent basics \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:37:37.265212+00:00
---

# Flow-based agent basics  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/basics/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Flow-based agent basics Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the basics of using Dialogflow CX flows to build an agent. It provides an overview of the most important concepts.

## Agents

A [Dialogflow CX agent](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent) is a virtual agent that handles concurrent conversations with your end-users. It is a natural language understanding module that understands the nuances of human language. Dialogflow CX translates end-user text or audio during a conversation to structured data that your apps and services can understand. You design and build a Dialogflow CX agent to handle the types of conversations required for your system.

A Dialogflow CX agent is similar to a human call center agent. You train them both to handle expected conversation scenarios, and your training does not need to be overly explicit.

## Flows

Complex dialogs often involve multiple conversation topics. For example, a pizza delivery agent may have _food order_ , _customer information_ , and _confirmation_ as distinct topics. Each topic requires multiple conversational turns for an agent to acquire the relevant information from the end-user.

[Flows](https://docs.cloud.google.com/dialogflow/cx/docs/concept/flow) are used to define these topics and the associated conversational paths. Every agent has one flow called the [Default Start Flow](https://docs.cloud.google.com/dialogflow/cx/docs/concept/flow#start). This single flow may be all you need for a simple agent. More complicated agents may require additional flows, and different development team members can be responsible for building and maintaining these flows. For example, the flows of a pizza delivery agent may look like the following: 

![Example multi-flow diagram.](https://docs.cloud.google.com/static/dialogflow/cx/docs/images/cx-flow.svg)

## Pages

A Dialogflow CX conversation (session) can be described and visualized as a [state machine](https://en.wikipedia.org/wiki/Finite-state_machine). The states of a session are represented by [pages](https://docs.cloud.google.com/dialogflow/cx/docs/concept/page). 

For each [flow](https://docs.cloud.google.com/dialogflow/cx/docs/concept/flow), you define many pages, where your combined pages can handle a complete conversation on the topics the flow is designed for. At any given moment, exactly one page is the _current page_ , the current page is considered _active_ , and the flow associated with that page is considered _active_. Every flow has a special [start page](https://docs.cloud.google.com/dialogflow/cx/docs/concept/flow#start-page). When a flow initially becomes active, the start page becomes the current page. For each conversational turn, the current page will either stay the same or transition to another page.

You configure each page to collect information from the end-user that is relevant for the conversational state represented by the page. For example, you might create the pages (in blue) in the diagram below for a _Food Order_ flow of a pizza delivery agent. The _Start_ node of the diagram represents the start page of the _Food Order_ flow. When the flow is complete, it transitions to the _Confirmation_ flow.

![Example multi-flow diagram.](https://docs.cloud.google.com/static/dialogflow/cx/docs/images/cx-page.svg)

## Entity types

[Entity types](https://docs.cloud.google.com/dialogflow/cx/docs/concept/entity) are used to control how data from end-user input is extracted. 

Dialogflow CX provides predefined [system entities](https://docs.cloud.google.com/dialogflow/cx/docs/concept/entity-system) that can match many common types of data. For example, there are system entities for matching dates, times, colors, email addresses, and so on. You can also create your own [custom entities](https://docs.cloud.google.com/dialogflow/cx/docs/concept/entity-custom) for matching custom data. For example, you could define a vegetable entity that can match the types of vegetables available for purchase with a grocery store agent.

## Parameters

[Parameters](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter) are used to capture and reference values that have been supplied by the end-user during a session. Each parameter has a name and an [entity type](https://docs.cloud.google.com/dialogflow/cx/docs/concept/entity). Unlike raw end-user input, parameters are structured data that can easily be used to perform some logic or generate responses. 

## Forms

For each page, you can define a [form](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter#form), which is a list of parameters that should be collected from the end-user for the page. The agent interacts with the end-user for multiple conversation turns, until it has collected all of the required _form parameters_ , which are also known as _page parameters_. The agent collects these parameters in the order defined on the page. For each required form parameter, you also provide _prompts_ that the agent uses to request that information from the end-user. This process is called _form filling_.

For example, you might create a form that collects the end-user's name and telephone number for a `Collect Customer Info` page.

## Intents

An [intent](https://docs.cloud.google.com/dialogflow/cx/docs/concept/intent) categorizes an end-user's intention for one conversation turn.

An intent contains the following data:

Term | Definition  
---|---  
Display name | Name displayed on the console for the intent.  
Labels | Labels that help categorize intents. For example: [head intent](https://docs.cloud.google.com/dialogflow/cx/docs/concept/intent#head).  
Training phrases  | [Training phrases](https://docs.cloud.google.com/dialogflow/cx/docs/concept/intent#tp) are example phrases for what end-users might type or say, known as _end-user input_. When end-user input resembles one of these phrases, Dialogflow CX matches the intent. You don't have to define every possible example, because Dialogflow CX's built-in machine learning expands on your list with other, similar phrases.  
Parameters  | You define your training phrases to use [parameters](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter#intent) to extract values from specific parts of the end-user input.  
DTMF patterns | See [DTMF for telephony integrations](https://docs.cloud.google.com/dialogflow/cx/docs/concept/dtmf).  
  
## Webhook

[Webhooks](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook) are services that host your business logic or call other services. During a session, webhooks allow you to use the data extracted by Dialogflow CX's natural language processing to generate dynamic responses, validate collected data, or trigger actions on the backend. 

A webhook can either be a _standard webhook_ or a _flexible webhook_. With a standard webhook, the request and response fields are defined by Dialogflow CX. With a flexible webhook, you define the request and response fields.

## Fulfillment

For an agent's conversational turn, the agent must respond to the end-user with an answer to a question, a query for information, or session termination. Your agent may also need to contact your service to generate dynamic responses or take actions for a turn. [Fulfillment](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment) is used to accomplish all of this.

A fulfillment may contain any of the following:

  * Static response messages.
  * Webhook calls for dynamic responses and/or to take actions.
  * Parameter presets to set or override parameter values.



During an agent's turn, it is possible (and sometimes desirable) to call multiple fulfillments, each of which may generate a response message. Dialogflow CX maintains these responses in a _response queue_. Once the agent's turn is over, Dialogflow CX sends the ordered responses to the end-user.

## State handlers

[State handlers](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler), also simply called _handlers_ , are used to control the conversation by creating responses for end-users and/or by transitioning the current page. For each conversational turn, handlers are evaluated and may affect the session. Handlers have three general types of data: Term | Definition  
---|---  
Handler requirements  | These are the requirements that must be satisfied for the handler to have any effect on the session. A handler is said to be _called_ when it satisfies its requirements and affects the session in some way.  
Handler fulfillment  | If a handler is called, an optional [fulfillment](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment) is used to create responses for end-users. These responses are either defined in static agent data or retrieved dynamically from your [webhook service](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook).  
Handler transition target  | If a handler is called, an optional transition target is used to change the current page. The next page can only be a [flow start page](https://docs.cloud.google.com/dialogflow/cx/docs/concept/flow#start-page) or a page within the currently active flow.  
  
There are two types of state handlers with differing handler requirements:

Term | Definition  
---|---  
Routes  | [Routes](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#route) are called when an end-user input matches an [intent](https://docs.cloud.google.com/dialogflow/cx/docs/concept/intent) and/or some [condition](https://docs.cloud.google.com/dialogflow/cx/docs/reference/condition) on the session status is met. A route with an intent requirement is also called an _intent route_. A route with only a condition requirement is also called a _condition route_.  
Event handlers  | [Event handlers](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#event) are called when an _event_ is invoked. Some [built-in events](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#event-built-in) are triggered when unexpected end-user input is received, or when a webhook error occurs. You can also define [custom events](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#event-custom) that you invoke when something happens outside the conversation.  
  
There are three steps to processing a state handler:

Term | Definition  
---|---  
1\. Scope | A handler must be in [scope](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#scope) to have any effect on the session. The scope is determined by whether a handler is applied to a flow, a page, or a form parameter; and by whether the associated flow is active, the associated page is active, or the agent is currently attempting to fill the associated form parameter.  
2\. Evaluation | Each handler in scope is [evaluated in order](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#eval). If a handler's requirements are met, it passes evaluation.  
3\. Call | If a handler is in scope and passes evaluation, it is called. Any associated fulfillment is called, and any associated transition target is applied to the session.  
  
## Regionalization and location settings

When you create an agent, you must specify a [region](https://docs.cloud.google.com/dialogflow/cx/docs/concept/region#avail) as the agent's location. Requests sent to your agent are handled by Google services in this region and Dialogflow CX keeps [data-at-rest](https://en.wikipedia.org/wiki/Data_at_rest) physically within the geographical [region or location](https://cloud.google.com/about/locations). For the best performance, you should choose a region that is near your services and end-users.

Once an agent is created, its location cannot change. In order to change an agent's location, you must [export and restore](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent#export) to a new agent with a different location.

Each location has associated settings that apply across your project. In most cases, you do not need to edit these location settings, and the default settings will work well. If your system requires [customer-managed encryption keys](https://docs.cloud.google.com/dialogflow/cx/docs/concept/cmek) (often required by government entities or regulated industries), read more about [location settings](https://docs.cloud.google.com/dialogflow/cx/docs/concept/region#location-settings).

## Console

**Note:** The Conversational Agents console includes the features from both deprecated Dialogflow CX console and Vertex AI Agent Builder console.

The Dialogflow Console is an UI that lets you intuitively create interactive agents that use [generative playbooks](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook), [generative data stores](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store), and [deterministic flows](https://docs.cloud.google.com/dialogflow/cx/docs/basics).

## Integrations

Dialogflow CX provides several built-in [integrations](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration) with other conversation platforms. These integrations provide a user interface to the end-user, and they call the API for you. All you need to do is build your agent and optionally implement a [webhook](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook) service. Each integration handles interactions in a platform-specific way, so see the specific integration documentation for details.

## Interactions

For each conversational turn, an _interaction_ takes place. During an interaction, an end-user sends input to Dialogflow CX, and Dialogflow CX sends a response. You have two options when implementing your system to handle interactions: using the API or using an integration.

When [using the API](https://docs.cloud.google.com/dialogflow/cx/docs/quick/api), your system needs to handle the following:

  * Build an agent.
  * Provide a user interface for end-users.
  * Call the Dialogflow API for each conversational turn to send end-user input to the API.
  * Unless your agent responses are purely static (uncommon), you need to host a [webhook service](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook) to handle webhook-enabled [fulfillment](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment).



When using an [integration](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration), your system only needs to handle the following:

  * Build an agent.
  * Optionally implement a webhook service.



The following diagram shows the steps that take place for one conversational turn of a session.

**Note:** Communications between your systems and integrations, and Dialogflow CX are [encrypted in transit](https://docs.cloud.google.com/docs/security/encryption-in-transit). Also, Google internal component communications are encrypted using [Application Layer Transport Security (ALTS)](https://docs.cloud.google.com/docs/security/encryption-in-transit/application-layer-transport-security).

![API flow diagram.](https://docs.cloud.google.com/static/dialogflow/cx/docs/images/cx-interaction-sequence.svg)

  1. The end-user types or says something, known as _end-user input_.
  2. Your user interface or integration system receives the input and forwards it to the Dialogflow API in a detect intent request.
  3. The Dialogflow API receives the detect intent request. It matches the input to an intent or form parameter, sets parameters as needed, and updates session state. If it needs to call a webhook-enabled fulfillment, it sends a webhook request to your webhook service, otherwise, go to step 6.
  4. Your webhook service receives the webhook request. Your service takes any actions necessary, like calling external APIs, querying or updating a database, etc.
  5. Your webhook service builds a response and sends a webhook response back to Dialogflow CX.
  6. Dialogflow CX creates a detect intent response. If a webhook was called, it uses the response provided in the webhook response. If no webhook was called, it uses the static response defined in the agent. Dialogflow CX sends a detect intent response to your user interface or integration system.
  7. Your user interface or integration system receives the detect intent response and forwards the text or audio response to the end-user.
  8. The end-user sees or hears the response.



[ Previous arrow_back  Data store search configuration  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store/search-configure)

[ Next Flows  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/flow)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
