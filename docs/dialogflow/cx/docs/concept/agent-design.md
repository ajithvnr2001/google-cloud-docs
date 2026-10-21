---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-design/
title: General agent design best practices \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:37:51.455101+00:00
---

# General agent design best practices  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-design/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  General agent design best practices Stay organized with collections  Save and categorize content based on your preferences. 

This guide provides general best practices for designing all types of agents.

You should also see the [voice agent design](https://docs.cloud.google.com/dialogflow/cx/docs/concept/voice-agent-design) guide specifically for designing voice agents, and the [best practices](https://docs.cloud.google.com/dialogflow/cx/docs/concept/best-practices) guide for using the Dialogflow CX service.

## General advice

### Build agents iteratively

If your agent will be large or complex, start by building a dialog that only addresses the top level requests. Once the basic structure is established, iterate on the conversation paths to ensure you're covering all of the possible routes an end-user may take.

While your agent evolves, consider using the test cases feature for test driven development.

### Prebuilt agents

Dialogflow CX offers agent templates to help you get started. [Prebuilt agents](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agents-prebuilt) cover common use-cases like financial services, telecommunications, and travel. These agents come with intents and entities to cover the most common user queries. Add routes and fulfillment specific to your business, and you'll quickly build a functioning agent.

## Integrations and connecting your services

There are multiple ways to integrate with Dialogflow CX agents. This section provides best practices for choosing how to integrate.

### Integrations

Dialogflow CX [integrations](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration) provide a ready-to-use user interface for your agent. If you use an integration, you do not need to directly call the Dialogflow CX API, as integrations handle this for you. These integrations can provide a text agent that you can embed on your website, connect with other messaging platforms, or provide a telephony interface.

### Dialogflow CX API

If none of the ready-to-use integrations are suitable, or you would like to customize the interface for your system, you can [use the Dialogflow CX API directly](https://docs.cloud.google.com/dialogflow/cx/docs/reference/api-overview). With this approach, you will need to implement the user interface for your agent, or make use of an existing user interface.

### Webhooks

Unless your agent can be completely defined with static data, you need to use [webhooks](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook) to connect your service and provide an agent that can handle dynamic scenarios. This applies whether you are using integrations or the Dialogflow CX API.

## Agent resources

Dialogflow CX agent resources can be used in many ways to achieve a desired result. This section provides advice for choosing the right resources for the right scenarios.

### Flows and pages

[Flows](https://docs.cloud.google.com/dialogflow/cx/docs/concept/flow) and [pages](https://docs.cloud.google.com/dialogflow/cx/docs/concept/page) provide structure to your agent. You can think of pages as nodes in a state machine, and flows as groups of related pages. You control transitions between nodes with [state handlers](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler), which are called when an intent is matched, a condition is met, or an event is invoked.

A simple agent may work fine with a single flow, but complex agents are almost always better designed with multiple flows. Each flow should represent a high level topic for your agent, where each page associated with the flow helps to handle the topic. In addition, each flow can have some of its own settings, and it can be [owned](https://docs.cloud.google.com/dialogflow/cx/docs/concept/access-control) by a subset of team members, which helps to divide the work when designing large agents.

When designing a large, complex agent, you need to consider the ["flows per agent" and "pages per flow" limits](https://docs.cloud.google.com/dialogflow/quotas#count_limits). These limits help to keep your agent performant.

If your agent design has too many flows per agent, combine related topics in a single flow. For example, you could combine the following topics to a single "Get balance" flow:

  * Get checking balance
  * Get savings balance
  * Get mortgage balance
  * Get credit balance



If your agent design has too many pages per flow, combine related pages and make use of many [routes](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#route) per page.

If you are still having difficulty with flow and page limits, it may be because you have too much business logic built into the agent itself. Consider moving this logic to webhooks.

The following lists the conversation control granularity of agent resources in increasing granularity order:

  1. Agents (one agent handles all conversations)
  2. Flows (one flow handles one or more related conversation topics)
  3. Pages (one page handles one or more related conversation turns)
  4. Routes (one route handles a user intent or condition check)



### Intent parameters versus form parameters

The main way in which your system gets structured data from the end-user is with [parameters](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter). You can use parameters for either [intents](https://docs.cloud.google.com/dialogflow/cx/docs/concept/intent) ([intent parameters](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter#intent)) or [pages](https://docs.cloud.google.com/dialogflow/cx/docs/concept/page) ([form parameters](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter#form)).

The main purpose of some pages is to collect specific information from the end-user. For example, a page may be designed to collect the end-user's contact information. In this case, you should always use form parameters to collect this information.

In some cases, you may want to capture end-user information while transitioning from one page to another. For example, if the end-user requests a particular product at the beginning of the conversation, you want to capture the desired product while transitioning to the appropriate order page. In this case, use intent parameters as part of [intent routes](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#route).

There are also situations in which using both intent parameters and form parameters is ideal. For example, if the end-user requests a small shirt at the beginning of the conversation, you want to capture the desired size parameter (small) while transitioning to the shirt order page. The shirt order page may ask for additional information, like the desired color. The shirt order page should have form parameters for size and color. In this example, the size parameter has already been provided and is [propagated](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter#prop), so the agent will only request the color. However, other conversations may follow a different path, where the end-user has not provided the desired size when the shirt order page becomes active. By defining this parameter in both ways, your agent is more flexible with how it extracts the information.

**Note:** When you define parameters with the same ID or display name in different intents or forms, make sure that the entity type and other settings are the same for all definitions. If the entity type or other parameter settings differ, use unique parameter ID or display name for each definition.

### Routes and route groups

If you want to transition to another page, queue a response message, or call a webhook when an [intent](https://docs.cloud.google.com/dialogflow/cx/docs/concept/intent) is matched or a [condition](https://docs.cloud.google.com/dialogflow/cx/docs/reference/condition) is met, use [routes](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#route).

If you find yourself using the same set of routes on multiple pages, use [route groups](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#route-group). This will avoid unnecessary duplication in your agent design.

### Intent reuse

If you find yourself defining multiple intents with similar training phrases, consider reusing intents across multiple pages. Ideally, you should define some general purpose intents that are used in many pages, and some specific intents that are only used in a single page. This will avoid unnecessary duplication in your agent design.

For example, confirmation intents are typically best defined as reusable intents. A `confirmation.yes` intent could have training phrases like:

  * yes
  * yeah
  * yep
  * okay
  * yes I do
  * you bet
  * absolutely
  * yes please



A `confirmation.no` intent could have training phrases like:

  * no
  * nah
  * nope
  * no way
  * not for me
  * absolutely not
  * no thank you



These reusable confirmation intents can be used in many scenarios for your agent.

In some cases, you should also consider creating specialized confirmation intents. For example, when confirming an order, you may want to have a specialized `order.confirmation.yes` intent with training phrases like:

  * the order looks good to me
  * I accept this order



And, a specialized `order.confirmation.no` intent with training phrases like:

  * I do not want this order
  * I do not accept this order



When your order confirmation page is active, intent routes for all four of these intents should be in scope. This ensures that any generic or specific confirmation from the end-user will get handled appropriately.

### Default negative intent

You should populate the [default negative intent](https://docs.cloud.google.com/dialogflow/cx/docs/concept/intent#negative) with phrases that your end-users might say, but should not match any intent in your agent.

### Fulfillment

There are many options for using [fulfillment](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment) to respond to the end-user. During a conversation turn, the agent can append multiple messages to the response queue, and the concatenated queue is sent to the end-user at the end of the conversation turn. This section describes each option for creating the individual messages.

  * [Page entry fulfillment](https://docs.cloud.google.com/dialogflow/cx/docs/concept/page#use): This fulfillment is called when the page initially becomes active. It is useful when you want a message that describes the purpose of the page, and it should only be said once while the page is active. For example: 
    * What do you want to know about your checking account?
    * What type of product would you like to purchase?
    * I need to collect some information about the shirt you want to order.
  * [Routes](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#route): This fulfillment is called when either an intent route or a condition route with fulfillment is called. This is useful when you want a message that responds to the end-user about the intent match, the satisfied condition (which may be a [form filling completion condition](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter#form-ref)), or the transition. For example: 
    * Yes, your international plan includes Japan. (intent match)
    * Are you sure you would like to purchase 300 shirts? ([comparison condition](https://docs.cloud.google.com/dialogflow/cx/docs/reference/condition#comp) met)
    * Okay, your appointment is for 7 AM tomorrow morning. (form filling completion)
    * Okay, let's talk about aardvarks now. (transition)
  * [Event handlers](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#event): This fulfillment is called when an event is invoked. It is useful when you want a message that responds to the event. For example: 
    * The stock you are considering for purchase has just increased in value by 10%. (custom event)
    * Can you rephrase that? ([no-match event](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#event-built-in))
  * [Initial prompts for forms](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter#form): This fulfillment is called when the agent performs form filling. These messages should ask the end-user a specific question. Each form parameter has its own initial prompt fulfillment. For example: 
    * What size shirt would you like?
    * What color shirt would you like?
  * [Reprompt handlers for forms](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter#form-reprompt): This fulfillment is called when the agent is performing form filling, and it does not understand the end-user selection for the current parameter. This fulfillment is only necessary if you would like a reprompt message to be different than the initial prompt message. If no reprompt handlers exist, the agent will just use the initial prompt as the reprompt message. For example: 
    * I do not understand. Can you please supply a valid color for the shirt?



## Naming

This section provides advice for naming agent resources.

### Intent naming

If your agent has many [intents](https://docs.cloud.google.com/dialogflow/cx/docs/concept/intent), you should consider a naming scheme that helps you keep them organized. It is common to segment intent names with punctuation, where the specificity increases from left to right. In addition, an intent name should reflect the end-user's intention for a conversational turn.

There are many good naming schemes, but here is one example:

  * phone-service.order.cancel
  * phone-service.order.create
  * phone-service.order.change
  * tv-service.order.cancel
  * tv-service.order.create
  * tv-service.order.change
  * account.balance.get
  * account.balance.pay
  * account.address.get
  * account.address.update



## Transitions

[Transitions defined in state handlers](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler) provide control over the conversation by changing the active page. This section provides advice for organizing your agent transitions.

### Complimentary transitions

When defining a route that triggers a transition, consider that there may be a complementary or inverse route.

For example:

  * If you have an intent route for **confirmation.yes** , consider defining another route for **confirmation.no**.
  * If you define a condition route with a boolean `=` operator, consider defining another route that uses `!=`.



## Handling end-user input

This section provides guidelines for intents and training phrases, so your agent can optimally handle and process end-user input.

### Define at least 20 training phrases

You should have at least 20 [training phrases](https://docs.cloud.google.com/dialogflow/cx/docs/concept/intent#tp) for every intent. Otherwise, the NLU model may not have enough information to appropriately match your intent. This is a bare minimum guideline. Ideally, you should define more, especially for [head intents](https://docs.cloud.google.com/dialogflow/cx/docs/concept/intent#head) of large agents, where roughly 50 is desirable.

### Be aware of intent bias

When one or more intents have significantly more training phrases than other intents, this causes the NLU model to bias in favor of the larger intents due to [imbalanced data](https://developers.google.com/machine-learning/data-prep/construct/sampling-splitting/imbalanced-data). This intent bias can happen when the quantity of training phrases differs by an order of magnitude or more.

In some cases, this is desired behavior, because you might define some intents that should be matched more often than others, because they correspond to end-user inputs more frequently observed in live traffic.

In other cases, this behavior may be undesirable, because you do not want a bias in favor of these larger intents. If this is the case, reduce the number of training phrases for these larger intents to be of the same order of magnitude as other intents. For example:

Intent A training phrases | Intent B training phrases | Bias for intent B  
---|---|---  
20 | 50 | No  
20 | 200 | Borderline  
20 | 2000 | Yes  
  
### Entity use and training phrase quantity

For all entity types used in an intent:

  * Annotate every example of the entity types.
  * For each of the entity types, provide at least five training phrases containing annotated examples.
  * Provide at least three times as many training phrases as entity types. For example, if you use 10 different entity types for annotations in an intent, you should have at least 30 training phrases.



### Training phrases should be natural

Training phrases should be conversational and natural; they should match what people actually say. Whenever possible, use end-user inputs that have occurred in production as your training data, paying special attention to those that are most common.

### Necessary training phrase variety

Include variations of questions, commands, verbs, and synonyms for common nouns to ensure your phrases cover a broad spectrum of possible requests.

It is best to include some shorter phrases like "pay my bill", as well as longer phrases and sentences like "I just got something in the mail that says I need to pay my statement balance". There is no recommended proportion of short to long phrases, but you should base this on actual end-user inputs sent to your agent in production.

Defining training phrases that vary in length, phrasing, and sentence structure is important to ensure good training for your agent. It is not necessary to add variety for variety's sake, but it is necessary to provide enough variety that the NLU model can successfully detect the end-user's intent from a wide range of end-user inputs. If you don't have sufficient variety, there is a danger of overfitting. In other words, there is a danger that the model will be too closely tied to the particular examples you provide and won't generalize sufficiently to other examples.

### Capitalization variety

Capitalization sensitivity varies according which [NLU model](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-settings#settings-ml) your agent is using.

#### Standard NLU

The standard NLU model is not case-sensitive. In rare cases, you may need to add training phrases that vary only in capitalization. This usually applies to situations when you expect end-users to provide all-uppercase text inputs.

Alternative approaches could be:

  * Lowering the [ML classification threshold](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-settings#settings-ml)
  * Lowercasing end-user inputs before sending them to Dialogflow CX.



#### Advanced NLU

Unlike the standard NLU model, the advanced NLU model is case-sensitive. We recommend testing and adding the relevant capitalized training data to increase intent match rates.

### Unnecessary training phrase variety

Avoid trivial variation in training phrases, as they provide duplicate information to the NLU model. For example, do not include variants that differ only by:

  * **Capitalization** : If you are using the standard NLU model, avoid duplicate phrases such as except "Order a ticket" and "order a ticket" except in rare cases. However, the advanced NLU model is case-sensitive and requires more training phrases to increase intent matches. See the capitalization variety section for details. 
  * **Filler words** : For example, "okay, order a ticket" and "order a ticket".
  * **Punctuation** : For example, "can you please help?" and "can you please help!?"



### Annotation consistency

The training phrase part selected for an annotation should include all of, and no more than, the text that is necessary to match an entity. Also, ensure that similar parts of training phrases are annotated for the entire intent.

For example, the following table shows good and bad ways to annotate with the `@sys.date` system entity:

Good | Bad  
---|---  
September 7th departure | September 7th departure  
Leaving on July 4 | Leaving on July 4  
  
### Use semantically meaningful annotations for system entities

The semantic meaning of a training phrase part selected for an annotation can be affected by the rest of the text in a training phrase. For example:

Annotated training phrase | Semantic meaning of annotated text  
---|---  
I am 7 years old | A person's age  
The contract is valid for 7 years | A time duration  
  
Dialogflow CX's machine learning models consider semantic meaning when matching system entities. The semantic meaning of the training phrase part must match the intended semantic meaning of the system entity.

For example, do not use the `@sys.duration` system entity for annotation of the first "7 years" example above. The semantic meaning of "7 years" does not match a simple time duration. Instead, you should select "7" for the annotation and use the `@sys.number` system entity.

### Define intents to handle non-compliant form filling answers

Consider defining intents to handle non-compliant form filling answers. For example, your agent may ask "what's your travel dates?", followed by the end-user answer of "I don't know yet". This answer does not satisfy the form parameter prompt, but if your agent has an intent route in scope that can match this answer, your agent can handle the situation well.

### Avoid @sys.any

Avoid using the `@sys.any` system entity type. It should only be used if you have completely exhausted all avenues, including building custom entities. This entity type is very broad and can cause undesired behavior.

If you do use this entity type, avoid annotating multiple parts of a single training phrase with this entity type, as this creates an ambiguity, and the agent behavior will be undefined.

It is less dangerous to use `@sys.any` with form parameters, because the agent is expecting specific information when prompting for form parameters.

**Note:** Some system entities are not available when you regionalize your agent deployment, and `@sys.any` is sometimes recommended as a workaround.

### Annotations should include a variety of entity values

When defining annotated training phrases, you should use a variety of entity value examples in the phrases. You should not consistently use the same entity example for the annotations. The following example shows good and bad annotations for a product entity type:

Good | Bad  
---|---  
I want to buy a shirt | I want to buy a shirt  
Order a new hat | Order a new shirt  
Add a watch to my cart | Add a shirt to my cart  
  
### Custom entities should include variety

Custom entities should cover a broad range of examples. The NLU model will provide variety for grammatical forms, but you must include all possible items.

### Avoid entities that match aggressively

Do not define entities that match virtually anything. This degrades the performance and quality of ML. Nearly everything in every training phrase will be evaluated as a possible match.

### Map and list entities should focus on distinct values

Map and list entity types should have a limited scope that captures distinct values of one type of information. Keep your entities focused, short, and simple.

If your entity values are complicated, it may be because intent training phrases are better suited to your situation. For example, consider end-user input like:

  * "How can I make an international call with Plan A?"
  * "Using international data roaming with Plan B."



Do not create entity types for both the actions and the plans, like the following:

Actions entity type | Plans entity type  
---|---  
"How can I make an international call" | "Plan A"  
"Using international data roaming" | "Plan B"  
  
Instead, you should use training phrases and intent matching to capture the actions and entities to capture the plans.

### Use regexp entities to capture non-word identifiers

When capturing end-user input that involves non-word identifiers, you should use [regexp entities](https://docs.cloud.google.com/dialogflow/cx/docs/concept/entity-regexp). For example, to capture product IDs like "AA-256" or "AC-436", use a regexp entity like "[A-Z]{2}-\d{3}".

### Avoid nesting composite entities

Do not use more than one level of nesting in composite entities. Each level of nesting significantly degrades quality.

### Avoid similar intents

Each intent should capture the end-user intention. If you define different intents with similar training phrases, matching may be unreliable, because the NLU model cannot determine with sufficient confidence, which intent to match.

If two training phrases represent the same intention, they should belong to the same intent. For example, "change current bill due date" and "more time to pay" should both belong to the same intent, because they are both requesting a due date change. However, "Can I make an international call with Plan A?" and "Can I use international data roaming with Plan A?" could belong to different intents, because the end-user wants a different thing in each case.

### Avoid similar entity types

You should avoid defining multiple entity types that have similar entity entries, because this can lead to ambiguity for the NLU model.

### Use no-match events in production to improve your intents

When running your agent in production, it is inevitable that some end-user inputs will result in [no-matches events](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#event-built-in). You can use these opportunities to improve your agent in one of three ways:

  * Add the end-user input as a training phrase to the desired intent. However, this is not always the best option. If you do this many times for the intent, it might lead to intent bias. 
  * Cleanup the training phrases for the desired intent, so that they all accurately reflect the intention. In some cases, intents with training phrases that are divergent can prevent matching for the intent.
  * If intents that should not be matched for the end-user input have training phrases that could match the end-user input, delete these training phrases.



### Avoid special characters

Special characters in training phrases (`{`, `_`, `#`, `[`, and so on) are ignored. An exception to this is for emoticons, where they work as expected.

### Avoid filler words

Filler words are words that you can ignore and still be able to understand the text. For example:

  * please
  * can you please
  * hmmm
  * how about



It is unnecessary but harmless to use filler words in training phrases, because these are ignored by the NLU model. However, you should not define training phrases that vary only by filler words.

Never define entities that are composed of filler words.

### Experiment with ML settings

The [ML settings](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-settings#settings-ml) can be used to adjust how end-user input is processed. In most cases, the default settings work well. However, you may want to fine-tune the settings to improve your agent performance.

## Responding to the end-user

This section provides guidelines for using fulfillment to respond to the end-user.

### Welcome the end-user

A newly created agent has an automatically created intent route for the [welcome intent](https://docs.cloud.google.com/dialogflow/cx/docs/concept/intent#welcome). You should edit this route to include a fulfillment message that welcomes the end-user. This message should describe the agent and give the end-user a sense for what it is capable of.

### Acknowledge end-user information

It is often best to repeat information provided by the end-user in responses. This lets the end-user know that the agent is understanding their request.

When an intent is matched, and a transition occurs, let the end-user know that the conversation is progressing based on their request. For example:

Dialogue | Description  
---|---  
**End-user** : I have questions about my checking account.  
**Agent** : Okay, what would you like to know about your checking account? | The end-user input resulted in an intent match, and a route was followed which included a fulfillment message and a transition to a page that handles checking account questions. Note that the agent confirms that the end-user wants to know about their checking account.  
  
When form filling has completed, repeat the data provided by the end-user. For example:

Dialogue | Description  
---|---  
**End-user** : Tomorrow  
**Agent** : Okay, your haircut is scheduled for tomorrow at 7 PM. Can I help you with anything else? | The end-user provided the date form parameter, which was the last form parameter on the active page. The agent confirmed the time and date of a scheduled haircut.  
  
### Guide the conversation

The agent should always guide the conversation with the end-user. This is easily accomplished by ending each response with a question like:

  * Can I help you with anything else?
  * What do you want to know about beagles?
  * Would you like to cancel or submit that order?
  * What can I help you with today?
  * Are you traveling alone or with somebody?



When defining these questions, be careful to avoid asking multiple questions like:

  * Are you still here? What service are you inquiring about?
  * Do you still want this order? Do you want to add anything?



The end-user may respond to just one of the questions, and your agent may not handle that situation correctly.

## Handling errors and unexpected end-user input

This section provides advice on handling errors and unexpected end-user input.

### Create event handlers for built-in events

You should create event handlers for the [built-in events](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#event-built-in) as applicable. Handling these events is similar to catching exceptions in software programming. Depending on the situation, you may want to handle the events with parameter-specific event handlers, page-specific event handlers, or flow-specific event handlers.

### Handle webhook errors

When your webhook service fails, it is important that your agent can gracefully handle the failure. You achieve this by defining event handlers for the webhook-specific [built-in events](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#event-built-in). Here is a recommended approach to handling webhook errors:

  * Do not supply a transition target from the [state handler](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler) that triggers the [webhook call](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#webhook), otherwise, the webhook error event handler will not be invoked. Instead, set the transition target in the webhook response from the webhook service.
  * Choose a page where an error counter can be initialized to zero. This page should be active before the page that triggers a webhook call. The entry fulfillment for this page should initialize the error counter to `0` using a [fulfillment parameter preset](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#param-preset). For example:

Parameter | Value  
---|---  
`webhook-error-count` | `0`  
  * Create a webhook error page that handles webhook error events:

    * The entry fulfillment should acknowledge the failure for the end-user, and it should increment an error counter session parameter using a [fulfillment parameter preset](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#param-preset). For example:

Parameter | Value  
---|---  
`webhook-error-count` | `$sys.func.ADD($session.params.webhook-error-count, 1)`  
    * Define a [condition route](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#route) that has a condition that the error count is less than the maximum allowed. (for example, `$session.params.webhook-error-count <= 3`). This route should have fulfillment that notifies the end-user that the agent will retry. This route should have a transition target set to [PREVIOUS_PAGE](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#symbolic), or to any page that can make another attempt to call the webhook.

    * Define a condition route that has a condition that the error count is greater than the maximum allowed (for example, `$session.params.webhook-error-count > 3`). This route should have fulfillment that notifies the end-user that the agent will no longer retry. This route should have a transition target set to a page that will not trigger webhook retries.

  * The webhook event handler should have a transition target that transitions to the webhook error page.




## Tools

This section provides advice on using tools to improve agent design.

### Use the validation tool

You should always use the [validation tool](https://docs.cloud.google.com/dialogflow/cx/docs/concept/validation) to check your agent. This tool finds some of the issues described in this guide.

### Use the test cases feature

You should always define [test cases](https://docs.cloud.google.com/dialogflow/cx/docs/concept/test-case) for your agent. These test cases can help prevent regressions while your agent evolves to handle more scenarios.

[ Previous arrow_back  Service use best practices  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/best-practices)

[ Next Voice agent design best practices  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/voice-agent-design)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
