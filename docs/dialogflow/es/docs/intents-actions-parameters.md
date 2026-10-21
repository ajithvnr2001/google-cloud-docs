---
url: https://docs.cloud.google.com/dialogflow/es/docs/intents-actions-parameters/
title: Actions and parameters \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:45:37.033700+00:00
---

# Actions and parameters  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/intents-actions-parameters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  Actions and parameters Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the _actions_ and _parameters_ settings for intents and how they are used when intents are matched at runtime.

## Where to find this data

When building an agent, it is most common to use the Dialogflow ES console ([visit documentation](https://docs.cloud.google.com/dialogflow/docs/console), [open console](https://dialogflow.cloud.google.com)). The instructions below focus on using the console. To access actions and parameters data:

  1. Go to the [Dialogflow ES console](https://dialogflow.cloud.google.com).
  2. Select an agent.
  3. Select **Intents** in the left sidebar menu.
  4. Select an intent.
  5. Scroll down to the **Action and parameters** section.



![Screenshot of action and parameters fields](https://docs.cloud.google.com/static/dialogflow/es/docs/images/intent-action-and-parameters.png)

If you are building an agent using the API instead of the console, see the [Intents reference](https://docs.cloud.google.com/dialogflow/docs/reference/common-types#intents). The API field names are similar to the console field names. The instructions below highlight any important differences between the console and the API.

## Actions

The _action_ field is a simple convenience field that assists in executing logic in your service.

When building an agent, you can set this field to any text you find useful.

When an intent is matched at runtime, Dialogflow provides the action value to your fulfillment webhook request or the API interaction response. It can be used to trigger specific logic in your service.

## Parameters

When an intent is matched at runtime, Dialogflow provides the extracted values from the end-user expression as _parameters_. Each parameter has a type, called the [entity type](https://docs.cloud.google.com/dialogflow/docs/entities-overview), which dictates exactly how the data is extracted. Unlike raw end-user input, parameters are structured data that can easily be used to perform some logic or generate responses. 

When building an agent, you control how data is extracted by [annotating](https://docs.cloud.google.com/dialogflow/docs/intents-training-phrases#annotation) parts of your training phrases and configuring the associated parameters.

The following list shows the fields of a parameter configuration. Examples are shown for the training phrase "book a room on Tuesday", where "Tuesday" is annotated.

  * **Required** : Check this box if the parameter is required for the intent to be complete. See the Slot filling with required parameters section below.
  * **Parameter Name** : A name that identifies the parameter. Example: `date`.
  * **Entity** : The [entity type](https://docs.cloud.google.com/dialogflow/docs/entities-overview) associated with the parameter. Example: `@sys.date`.
  * **Value** : In most cases, this is set to a parameter reference like `$parameter-name`, which is used as a placeholder for the extracted value at runtime. However, this field can be used to select alternate values as well. See the Parameter values and parameter references section below. Example: `$date`.
  * **Is List** : Check this box if the values should be returned as a list. See the List parameters section below.
  * **Prompts** : Questions that the agent will ask the end-user if this parameter was not supplied. This field is only used if the **Required** field is checked. See the Slot filling with required parameters section below.
  * **Default value** : This is the default value for the parameter when the end-user does not supply one. To change the default value with the console, you must hover over the parameter row and click the menu on the right.



When an intent is matched at runtime, Dialogflow provides parameter data to your fulfillment webhook request or the API interaction response. These are provided as a mapping from parameter names to parameter values.

When building an agent, your responses can include parameter values. See Parameter values and parameter references below.

## List parameters

When building an agent with the console, checking the **Is List** option configures the parameter as a list. Lists can contain multiple elements. For example, a produce-ordering agent may expect the following end-user expressions:

  * "I want apples"
  * "I want apples and oranges"
  * "I want apples, oranges, and bananas"



When annotating training phrases with list parameters, your phrases can contain one or more parameter examples, and you annotate each one separately:

![Screenshot of list parameter annotation.](https://docs.cloud.google.com/static/dialogflow/es/docs/images/parameter-is-list.png)

Once you annotate at least two words or phrases with the same parameter in a single training phrase, the **Is List** option is automatically enabled. If you disable this option but keep the same annotation, **Is List** will be automatically checked again once you open the page with this annotation.

In [multilingual agents](https://docs.cloud.google.com/dialogflow/es/docs/agents-multilingual), the **Is List** option is not [language-specific](https://docs.cloud.google.com/dialogflow/es/docs/agents-multilingual#lang-specific).

## Parameter values and parameter references

Parameter references are variables that hold parameter values extracted at runtime. When building an agent, you can use parameter references in intent responses, parameter prompts, and the parameter **Value** field.

For example, you can use `$parameter-name` in an intent response. When Dialogflow responds to the user, it will replace that parameter reference with the parameter value extracted at runtime. This is helpful for recapping information provided by the end-user. For example, your intent response could look like: "Okay, I booked a room for you on $date".

### Basic parameter reference

To reference a parameter value extracted by the associated entity, use the following format:
    
    
    $parameter-name

For example, if the parameter name is `date`, you can reference it as `$date`.

### Parameter reference for an original value

When text is matched to a particular entity, it is often converted to text that is more convenient for processing. For example, the word "apples" in an end-user expression may be extracted as "apple" for a fruit entity. To reference a parameter value exactly as it was written or spoken by the end-user, use the following format:
    
    
    $parameter-name.original

For example, if the parameter name is `date`, you can reference the original value as `$date.original`.

### Parameter reference for ambiguous dates

When a parameter is associated with the `@sys.date` system entity, and the end-user supplies a partial date (not specifying month, day, and year), Dialogflow will match to the nearest date in the future. However, you can also retrieve variations of this date.

You can retrieve the explicit partial match, where Dialogflow substitutes the unknown part with `U`s using the following format:
    
    
    $parameter-name.partial

You can retrieve the nearest date in the past using the following format:
    
    
    $parameter-name.recent

For example, if today's date is August 11, 2021, your parameter name is `date`, and the user says "August 13":

Parameter reference | Resolved value  
---|---  
$date | 2021-08-13  
$date.partial | UUUU-08-13  
$date.recent | 2020-08-13  
  
### Parameter reference for a composite entity

[Composite entities](https://docs.cloud.google.com/dialogflow/docs/entities-options#comp) are entities that contain other sub-entities. To reference the value of a parameter's sub-entity, use the following format:
    
    
    $parameter-name.sub-entity-name

For example, if the parameter name is `move`, and the sub-entity name is `direction`, you can reference the sub-entity value as `$move.direction`.

### Parameter reference for an active context

[Contexts](https://docs.cloud.google.com/dialogflow/docs/contexts-overview) can serve as temporary storage for parameter values. To reference a parameter value obtained from an active context, use the following format:
    
    
    #context-name.parameter-name

For example, if the parameter name is `room`, and `reservation` is an active context, you can reference the parameter value as `#reservation.room`.

### Parameter reference for an event parameter

To reference an [event](https://docs.cloud.google.com/dialogflow/docs/events-overview) parameter, use the following format:
    
    
    #event-name.parameter-name

For example, if the parameter name is `duration`, and the event name is `alarm`, you can reference the event parameter as `#alarm.duration`.

### Parameter Value field

Parameter references in the parameter **Value** field have a special significance. The content in this field determines the resolved value for`$parameter-name` in intent responses and parameter prompts. Dialogflow processes parameter data in the following order:

  1. Extract the parameter value from the end-user expression using the associated entity.
  2. Resolve content for the parameter **Value** field.
  3. Set`$parameter-name` to the resolved content of the parameter **Value** field. If the **Value** field is not set to `$parameter-name`, this resets the value of `$parameter-name` to something else. 
  4. Resolve content for intent responses and parameter prompts.



Here are a few examples to illustrate the effects of this ordering for an end-user expression of "I want to buy a _small_ shirt".

Parameter reference location | Configured content | Resolved content  
---|---|---  
Parameter **Value** field | $size | S  
Intent response | You chose size: $size | You chose size: S  
Parameter reference location | Configured content | Resolved content  
---|---|---  
Parameter **Value** field | $size.original | small  
Intent response | You chose size: $size | You chose size: small  
Parameter reference location | Configured content | Resolved content  
---|---|---  
Parameter **Value** field | $size | S  
Intent response | You chose size: $size.original | You chose size: small  
  
## Slot filling with required parameters

When building an agent, you can mark parameters as required. An intent is not complete until the end-user has supplied data for each of these required parameters.

![Screenshot of required parameters fields](https://docs.cloud.google.com/static/dialogflow/es/docs/images/intent-parameters-required.png)

When an intent is matched at runtime, the Dialogflow agent continues collecting information from the end-user until the end-user has provided data for each of the required parameters. This process is called _slot filling_.

Dialogflow does not send a fulfillment webhook request until it has collected all required data from the end-user, unless [webhook for slot filling](https://docs.cloud.google.com/dialogflow/docs/fulfillment-webhook-slot-filling) is enabled.

Dialogflow sends an API interaction response for each step of slot filling. For each of these slot filling responses, the intent and action will be the same, and the parameters collected so far will be provided.

When building an agent, you provide prompts that the agent will use to get parameter data from the end-user. You can also provide prompt variations, so the agent doesn't always ask the same question.

![Screenshot of parameter prompts](https://docs.cloud.google.com/static/dialogflow/es/docs/images/intent-parameters-prompts.png)

For example, consider that your clothing store agent has an intent with required parameters for:

  * clothing type
  * quantity
  * size
  * color



Completing an intent may look like the following:

**User** : I'd like to buy a t-shirt.  
**Agent** : How many do you want?  
**User** : 3  
**Agent** : What color would you like?  
**User** : Black  
**Agent** : What size?  
**User** : Medium  
**Agent** : Got it, that was three black t-shirts in medium  


If the end-user supplies data for more than one parameter in a single expression, Dialogflow collects the data provided and continues asking for the missing data. For example, the end-user may say "I'd like to buy three black t-shirts". Dialogflow would ask the user for the size.

### Ordering parameters

When building an agent, you can order the parameters, which determines the order in which the agent will prompt the end-user for missing data.

When building an agent from the console, hovering over a parameter will reveal a reorder icon on the right. You can drag this icon to change the position of the parameter in the list.

### Parameter references in prompts

When building an agent, you can use parameter references in prompts, but only for required parameters before the prompt. For example, if the `color` parameter is before the `quantity` parameter, you can use the following prompt for the `quantity` parameter: `How many $color t-shirts would you like to buy?`

### Cancel slot filling

When the end-user says an exit phrase like "Cancel", "Stop it", "That's enough", etc., the agent replies with "Okay, canceled" and clears slot filling contexts.

If you are using the API, the `DetectIntentResponse.queryResult.cancelsSlotFilling` field is set to `true` when slot filling is canceled. For more information, see the `detectIntent` documentation of the [`Sessions`](https://docs.cloud.google.com/dialogflow/es/docs/reference/common-types#sessions) type.

[ Previous arrow_back  Training phrases  ](https://docs.cloud.google.com/dialogflow/es/docs/intents-training-phrases)

[ Next Responses  arrow_forward  ](https://docs.cloud.google.com/dialogflow/es/docs/intents-responses)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
