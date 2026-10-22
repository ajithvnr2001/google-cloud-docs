---
url: https://docs.cloud.google.com/food-ai/concepts/
title: Food Ordering AI Agent concepts \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:15.065925+00:00
---

# Food Ordering AI Agent concepts  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/food-ai/concepts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Food AI ](https://docs.cloud.google.com/food-ai)
  * [ Guides ](https://docs.cloud.google.com/food-ai/concepts)



Send feedback 

#  Food Ordering AI Agent concepts Stay organized with collections  Save and categorize content based on your preferences. 

This document provides a high-level overview of the key concepts in the Food Ordering AI Agent API.

## Agent configuration

The behavior of the Food Ordering AI Agent is influenced by the configuration of several API resources: [`Brand`](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#brand), [`Store`](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#store), and [`Menu`](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#menu). These resources define the restaurant's identity, its physical locations, and the products it offers, providing the necessary context for the AI agent to handle orders.

### Brand

A [`Brand`](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#brand) is the top-level resource, representing a restaurant brand corresponding to one or more locations of that restaurant brand. It contains configuration which is shared across all locations of that restaurant. `Brand` can include configuration of many features of the agent persona, such as greeting behavior and voice characteristics. Many of those features can be overridden by values configured in the Store resource or even in per-session configuration (see Session lifecycle)

### Store

A [`Store`](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#store) resource represents a single physical restaurant location belonging to a [`Brand`](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#brand). It defines configuration specific to that location, such as its time zone, status (e.g., `ACTIVE`, `DISABLED`), operating hours, and _dayparts_ (e.g., periods like "Breakfast" or "Lunch" during which certain menu items are available).

### Menu

A [`Menu`](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#menu) resource defines all the products offered by a restaurant, including all possible choices and customizations for every sellable product. A [`Menu`](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#menu) must be associated with a [`Store`](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#store). Menu is designed to be flexible and accommodate various menu structures, from small lists of standalone items to complex trees of combination meals with nested modifiers.

Key components of a [`Menu`](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#menu) include:

  * **Items** : Sellable top-level products like a-la-carte entrees, drinks, sides, or combination meals.
  * **ModifierGroups** : Collections of choices applicable to an [`Item`](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#item) or another [`Modifier`](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#modifier), such as "Choose a Side" or "Add Toppings".
  * **Modifiers** : Individual options within a [`ModifierGroup`](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#modifiergroup), like "Fries", "Extra Cheese", or "Cola". Modifiers can adjust the item price and can contain nested [`ModifierGroup`](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#modifiergroup)s for further customization.
  * **MenuCategories** : Organizational units like "Appetizers" or "Drinks".



A [`Menu`](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#menu) resource is identified by a name in the following format: `projects/{project}/locations/{location}/menus/{menu}`.

For more details on structuring menu data, see [Integrating menu data](https://docs.cloud.google.com/food-ai/menu-integration).

## Food ordering sessions

Food ordering sessions are at the core of Food Ordering AI Agent, enabling conversational interactions between a customer and the AI agent. Each session represents a single food ordering conversation and is managed using either the real-time bidirectional streaming method ([`FoodOrderingService.BidiProcessOrder`](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.FoodOrderingService.BidiProcessOrder)) or the turn-based unary request-response method ([`FoodOrderingService.ProcessOrder`](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#google.cloud.foodorderingaiagent.v1beta.FoodOrderingService.ProcessOrder)).

### BidiProcessOrder RPC method

This is a bidirectional streaming RPC: the client application streams input to the agent, and the agent concurrently streams responses back to the client. This allows for low-latency, real-time multimodal (voice and text) interactions.

  * **Client-to-Agent Stream** : The client sends a stream of [`BidiProcessOrderRequest`](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#bidiprocessorderrequest) messages containing audio input (customer speech), text input, or event inputs (such as a client-side cart update performed by a customer using a tap interface, or a hardware-detected drive-off event from drive-thru restaurant hardware).
  * **Agent-to-Client Stream** : The agent returns a stream of [`BidiProcessOrderResponse`](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#bidiprocessorderresponse) messages containing audio output (synthesized agent speech), text output, transcripts of recognized speech, updates to the customer's order state, or other signals such as detected interruptions.



### ProcessOrder RPC and REST method

`ProcessOrder` is a unary request-response method designed for text-based, turn-by-turn food ordering integrations (such as chat widgets, web forms, and REST clients). It is accessible over gRPC and REST (`POST /v1/{config.session=projects/*/locations/*/sessions/*}:processOrder`).

Unlike `BidiProcessOrder`, `ProcessOrder` operates on discrete request-response turns and is text-only:

  * **Mode Requirement** : `config.mode` must be explicitly set to `TEXT` (or `2` in JSON).
  * **Turn Lifecycle** : `turn_type` should be set to `INITIALIZE` on the initial turn to inject session variables (such as menu and store metadata), and `SUBSEQUENT` on follow-up turns.



### Session lifecycle

Every Session in Food Ordering AI Agent must begin with client-provided configuration specified using a [`Config`](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#config) message. The `Config` specifies:

  * `store`: The full resource name of the `Store` for which the order is being placed (e.g. `projects/PROJECT/locations/LOCATION/brands/BRAND/stores/STORE`). The session takes on configuration specified in the referenced `Store` resource and that store's parent `Brand` resource. Where configuration conflicts across the `Brand` and `Store`, the `Store` configuration takes precedence.
  * `session`: A unique session identifier in the format `projects/PROJECT/locations/LOCATION/sessions/SESSION`. The `session_id` is a client-generated ID that uniquely identifies one customer interaction or conversation.
  * `mode`: The mode of the session (`HYBRID` or `TEXT`). For `BidiProcessOrder`, `mode` is optional and defaults to `HYBRID` (voice and text). For `ProcessOrder` (unary / REST), `mode` **must** be explicitly set to `TEXT`.

**Tip:** If a client disconnects (e.g., due to network issues) and reconnects to `BidiProcessOrder` using the same `session` identifier in the initial `Config` message, the agent resumes the session from its previous state. If a new `session` identifier is provided, the API initiates a new ordering session.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
