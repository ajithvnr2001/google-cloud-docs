---
url: https://docs.cloud.google.com/dialogflow/es/docs/intents-responses/
title: Responses \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:25:48.596063+00:00
---

# Responses  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/intents-responses/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  Responses Stay organized with collections  Save and categorize content based on your preferences. 

Intents have a built-in response handler that can return responses after the intent is matched. This feature only supports static responses, though you can use [parameter references](https://docs.cloud.google.com/dialogflow/docs/intents-actions-parameters#values) in these responses to make them somewhat dynamic. This is helpful for recapping information provided by the end-user. For example, your intent response could look like: "Okay, I booked a room for you on $date".

In some cases, this is all you need. In cases where your code needs to take some action or build a more dynamic response, you should use one of the dynamic response options below. Agents typically use a combination of static and dynamic responses.

Multiple types of responses can be provided. The basic response type is a text response. Other types of responses are available (image, audio, synthesized speech, and so on), some of which are platform-specific.

If you define more than one response variation for an intent, your agent will select a response at random. You should add several response variations to make your agent more conversational.

When building an agent, you should provide response data for each intent. When you use the API or [fulfillment](https://docs.cloud.google.com/dialogflow/docs/fulfillment-overview) to interact with Dialogflow, you technically may not need to provide response data, because both of these methods can dynamically generate any response. However, if you want to use the [simulator](https://docs.cloud.google.com/dialogflow/docs/console#simulator) for testing or define intents that have a simple response, you should provide response data.

As a general rule, your intent responses should prompt the end-user to provide an expression that will match another intent. Your responses should also guide the end-user to provide specific data. For example, a question like "What city were you born in?" is better than a more open-ended question like "Where were you born?".

## Where to find this data

When building an agent, it is most common to use the Dialogflow ES console ([visit documentation](https://docs.cloud.google.com/dialogflow/docs/console), [open console](https://dialogflow.cloud.google.com)). The instructions below focus on using the console. To access intent response data:

  1. Go to the [Dialogflow ES console](https://dialogflow.cloud.google.com).
  2. Select an agent.
  3. Select **Intents** in the left sidebar menu.
  4. Select an intent.
  5. Scroll down to the **Responses** section.



If you are building an agent using the API instead of the console, see the [Intents reference](https://docs.cloud.google.com/dialogflow/docs/reference/common-types#intents). The API field names are similar to the console field names. The instructions below highlight any important differences between the console and the API.

## Response platforms

Each response is defined for either the **Default** platform (referred to as `PLATFORM_UNSPECIFIED` in the API) or a specific [integration](https://docs.cloud.google.com/dialogflow/docs/integrations) platform. If you are not using an integration, all of your responses can use the default platform. If you are using integrations, each integration can have a unique response, or it can be configured to use the default response.

For more information on platform-specific responses, see [Rich response messages](https://docs.cloud.google.com/dialogflow/docs/intents-rich-messages).

## Create built-in responses

To create built-in responses:

  1. Select **Default** or a specific platform.
  2. If the desired type of response (for example, **Text response**) is not already listed, click **Add Responses** and select the response type.
  3. Enter required information for the response.
  4. Click **Save**.



## Dynamic responses with fulfillment

Using fulfillment, you can create dynamic responses. See the [fulfillment documents](https://docs.cloud.google.com/dialogflow/docs/fulfillment-overview) for more information.

## Dynamic responses with the API

Using the API, you can create dynamic responses. See the [API overview](https://docs.cloud.google.com/dialogflow/docs/api-overview) for more information.

## Special characters

Some special characters require escaping in your response.

To use the dollar sign **`$`** or the number sign **`#`** in a response, add braces **`{}`** around the content that immediately follows the sign. For example:

  * `${100}` resolves to `$100`
  * `${$number}` resolves to `$100`, where `$number` is a parameter reference with a value of 100
  * `#{hello}` resolves to `#hello`



To use braces **`{}`** in a response, use double braces. For example:

  * `{{hello}}` resolves to `{hello}`



## Handling empty parameter values

If your intent has a parameter that can resolve to an empty value, you must provide at least one response variant that does not use that parameter.

For example, if your intent has 2 parameters (`p1` and `p2`), and either or both could be empty, you should provide at least four response variants:

  * Got it. You said $p1 and $p2.
  * Got it. You said $p1.
  * Got it. You said $p2.
  * Got it.



[ Previous arrow_back  Actions and parameters  ](https://docs.cloud.google.com/dialogflow/es/docs/intents-actions-parameters)

[ Next Rich response messages  arrow_forward  ](https://docs.cloud.google.com/dialogflow/es/docs/intents-rich-messages)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
