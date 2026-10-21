---
url: https://docs.cloud.google.com/dialogflow/es/docs/intents-default/
title: Default intents \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:45:37.600603+00:00
---

# Default intents  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/intents-default/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  Default intents Stay organized with collections  Save and categorize content based on your preferences. 

Two intents are created automatically when you create an agent:

  * **Default welcome intent** : matched when an end-user begins a conversation with your agent.
  * **Default fallback intent** : matched when your agent doesn't match an end-user input to any other intents.

**Note:** You can delete the default intents, but it is normally best to keep them and customize them for your agent.

## Default welcome intent

The default welcome intent is matched when an end-user begins a conversation with your agent. It should return a response that lets end-users know what your agent does or what end-users can say to begin a conversation. You should customize the pre-populated intent responses for your agent.

The default welcome intent is matched in one of two ways:

  * One of its training phrases are matched, which are pre-populated with common greetings, like "hello".
  * This intent has a [welcome event](https://docs.cloud.google.com/dialogflow/docs/events-platform#welcome_events) attached to it, which is triggered when the end-user begins a conversation with your agent via a supported [integration](https://docs.cloud.google.com/dialogflow/docs/integrations).

**Note:** The default welcome intent includes various greeting training phrases in all languages, however these training phrases are not used for invocation by Google Assistant. See the Google Assistant [invocation](https://developers.google.com/assistant/discovery) documentation for more information.

## Default fallback intent

The default fallback intent is matched when your agent doesn't match an end-user input to any other intents.

This intent is not matched if an audio input doesn't contain any transcribed speech.

This intent is automatically configured with a variety of static text responses, like "I didn't get that. Can you say it again?".

You can customize fallback intents by changing the pre-populated text responses or by adding negative examples.

You can also create additional fallback intents:

  1. Go to the [Dialogflow ES console](https://dialogflow.cloud.google.com).
  2. Select an agent.
  3. Select **Intents** in the left sidebar menu.
  4. Click the option _more_vert_ button at the top of the intents page.
  5. Select **Create Fallback Intent**.



### Fallback intent responses

You can change the pre-populated text responses, but they should communicate to the end-user that their input was not recognized.

**Note:** You can have multiple fallback intents with [contexts](https://docs.cloud.google.com/dialogflow/docs/contexts-overview) to customize fallback responses.

### Negative examples

You can add training phrases to fallback intents that act as _negative examples_. There may be cases where end-user expressions have a slight resemblance to your training phrases, but you do not want these expressions to match any normal intents.

For example, a room booking service may have a training phrase like "I'd like to book a room". If the end-user wants to purchase a book about rooms, they may say "I'd like to buy a book about rooms." To ensure that the end-user expression does not match your intent, you can add that phrase as a negative example.

[ Previous arrow_back  Rich response messages  ](https://docs.cloud.google.com/dialogflow/es/docs/intents-rich-messages)

[ Next Intent matching  arrow_forward  ](https://docs.cloud.google.com/dialogflow/es/docs/intents-matching)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
