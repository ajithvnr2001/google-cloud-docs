---
url: https://docs.cloud.google.com/dialogflow/es/docs/quick/build-agent/
title: Quickstart: Create a Dialogflow ES agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:44:15.163364+00:00
---

# Quickstart: Create a Dialogflow ES agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/quick/build-agent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a Dialogflow ES agent

Use the Dialogflow ES console to build and test an agent.

## Before you begin

Before you begin, complete the following steps:

  * Read [Dialogflow basics](https://docs.cloud.google.com/dialogflow/docs/basics).
  * Complete the [setup steps](https://docs.cloud.google.com/dialogflow/docs/quick/setup).



## Create an agent

  1. Go to the [Dialogflow ES console](https://dialogflow.cloud.google.com). 
  2. Sign in to the console if prompted. For more information, see the [Dialogflow console overview](https://docs.cloud.google.com/dialogflow/docs/console). 
  3. In the sidebar menu, expand **Loading agents**. 
  4. Click **Create new agent**. 
  5. Enter the agent name, default language, and default time zone. 
  6. Enter an existing project. To let the Dialogflow console create a project, select **Create a new Google project**. 
  7. Click **Create**. 



## Intents

[_Intents_](https://docs.cloud.google.com/dialogflow/docs/intents-overview) categorize an end-user's intention for one conversation turn. For each agent, you define many intents that together handle a complete conversation.

### Default intents

When you create an agent, Dialogflow creates two [default intents](https://docs.cloud.google.com/dialogflow/docs/intents-default) for you:

  * **Default Welcome Intent:** This intent matches when the end-user begins a conversation with your agent. It returns a response that lets the end-user know what your agent does or what they can say to begin a conversation.
  * **Default Fallback Intent:** This intent matches when the agent cannot match the end-user expression to any other intent.



To see these intents, go to the intent list for your agent:

  1. Go to the [Dialogflow ES console](https://dialogflow.cloud.google.com).
  2. Select the agent you created.
  3. Click **Intents** in the sidebar menu.



The middle of the [Dialogflow console](https://docs.cloud.google.com/dialogflow/docs/console) shows the list of intents for the agent.

![Intents list screenshot](https://docs.cloud.google.com/static/dialogflow/es/docs/images/intents-list.png)

### Test the Default Fallback Intent

![Simulator screenshot](https://docs.cloud.google.com/static/dialogflow/es/docs/images/simulator-default-fallback.png)

The Dialogflow simulator is on the right side of the console. With the simulator, you can test your agent by speaking or typing messages.

Try the agent now:

  1. Click the **Try it now** field.
  2. Type `What is your name?`.
  3. Press Enter.



The agent's response appears in the **Default Response** section. Since your input didn't match any intent, the Default Fallback Intent was matched, and you received one of the default replies.

### Create an intent

The steps in this section create an intent that answers the question "What is your name?" For each intent, you define many [training phrases](https://docs.cloud.google.com/dialogflow/docs/intents-training-phrases). A training phrase is an example of what an end-user might type or say to your agent, also known as an end-user expression. Define training phrases that help Dialogflow match expressions to an intent.

Create an intent:

  1. Click the add intent add button next to **Intents** in the sidebar menu.
  2. Enter `get-agent-name` in the **Intent name** field.
  3. In the **Training Phrases** section, click **Add training phrases**.
  4. Enter the following training phrases:

     * `What is your name?`
     * `Do you have a name?`
     * `Tell me your name`

![Training phrases screenshot](https://docs.cloud.google.com/static/dialogflow/es/docs/images/intents-training-phrases-name.png)

**Note:** In most cases, you should enter at least 10-20 (depending on complexity of intent) training phrases for reliable intent matching.
  5. In the **Responses** section, enter the following in the **Text Response** section:

     * `My name is Dialogflow!`

![Training phrases screenshot](https://docs.cloud.google.com/static/dialogflow/es/docs/images/intents-response-name.png)

  6. Click the **Save** button and wait until the **Agent Training** dialog indicates that training is complete. 




### Test your intent

![Simulator screenshot](https://docs.cloud.google.com/static/dialogflow/es/docs/images/simulator-whats-your-name.png)

In the simulator, type `What's your name?` and press Enter.

The agent responds to the expression correctly, even though the expression differs slightly from the training phrases provided.

Dialogflow uses training phrases as examples for a machine learning model to match end-user expressions to intents. The model checks the expression against every intent in the agent, assigns a score to each intent, and matches the highest scoring intent. If the highest scoring intent has a very low score, the fallback intent is matched.

## Parameters and entities

When an intent is matched at runtime, Dialogflow provides the extracted values from the end-user expression as [parameters](https://docs.cloud.google.com/dialogflow/docs/intents-actions-parameters#params). Each parameter has a type, called the [entity type](https://docs.cloud.google.com/dialogflow/docs/entities-overview), which dictates exactly how the data is extracted. Unlike raw end-user input, parameters are structured data that can easily be used to perform some logic or generate responses. 

To control how data is extracted when building an agent, annotate parts of your [training phrases](https://docs.cloud.google.com/dialogflow/docs/intents-training-phrases#annotation) and configure the associated parameters.

### Create parameters

Create intent parameters:

  1. Click the plus add button next to **Intents** in the sidebar menu.
  2. Name the intent `set-language` at the top of the intent form.
  3. Add the following training phrases: 
     * `I know English`
     * `I speak French`
     * `I know how to write in German`
  4. Click the **Save** button and wait until the **Agent Training** dialog indicates that training is complete. 

![Annotated training phrase screenshot](https://docs.cloud.google.com/static/dialogflow/es/docs/images/intents-training-phrases-languages.png)




Dialogflow automatically detects parameters in training phrases that are recognized as [system entities](https://docs.cloud.google.com/dialogflow/docs/entities-system). These are entities provided by Dialogflow for many common data types, such as location, color, and date.

**Note:** If training phrases aren't automatically annotated, [manually annotate them](https://docs.cloud.google.com/dialogflow/docs/intents-training-phrases#annotation).

After you add training phrases, Dialogflow creates a row in the **Action & parameters** table:

![Annotated training phrase screenshot](https://docs.cloud.google.com/static/dialogflow/es/docs/images/intents-parameters-language.png)

  * **Required:** Not checked; this parameter is optional.
  * **Parameter Name:** Automatically named `language` because it is recognized as a language.
  * **Entity:** Recognized as a `@sys.language` system entity.
  * **Value:** The identifier used when referencing the value of this parameter.
  * **Is List:** Not checked; this parameter is not a list.



### Use parameter data in a response

You can use the value of a parameter in your responses. For example, you can use the `$language` parameter reference in your responses when building an agent. At runtime, the agent replaces it with the language specified in the end-user expression.

Add a response that uses a parameter:

  1. Go to the **Responses** section.
  2. In the **Text Response** section, add the following: `Wow! I didn't know you knew $language.`
  3. Click the **Save** button and wait until the **Agent Training** dialog indicates that training is complete. 



### Test your parameter

![Simulator screenshot](https://docs.cloud.google.com/static/dialogflow/es/docs/images/intents-set-language-response.png)

In the simulator, type `I know Russian`. You can see that Dialogflow correctly extracts the `language` parameter with the value `Russian`, and `Russian` was correctly inserted where the parameter reference was used in the response.

### Create your own entities

In most cases, you need to gather specific data from users that is not provided by system entities. You can create [custom entities](https://docs.cloud.google.com/dialogflow/docs/entities-custom) to handle this.

Create a custom entity:

  1. Click the add entity add button next to **Entities** in the sidebar menu.
  2. Enter `language-programming` for the name of the entity.
  3. Add the following entity entries (rows):

Reference Value | Synonyms  
---|---  
JavaScript | JavaScript, js, ECMAScript  
Java | Java  
Python | Python, py  
  4. Click the **Save** button and wait until the **Agent Training** dialog indicates that training is complete. 




![Entity use screenshot](https://docs.cloud.google.com/static/dialogflow/es/docs/images/entities-language-programming.png)

Dialogflow can handle simple cases like plurality and capitalization. Add all possible synonyms for your entries. The more synonyms you add, the better your agent can identify your entities.

### Use your new entity

Add training phrases to the `set-language` intent that use the new entity:

  1. Click **Intents** in the sidebar menu.
  2. Click the `set-language` intent.
  3. Add the following training phrases: 
     * `I know javascript`
     * `I know how to code in Java`
  4. Observe that the programming languages in these training phrases are automatically annotated and added to parameters in the **Action and Parameters** section.
  5. In the **Responses** section, add the following second text response: `$language-programming is an excellent programming language`.
  6. Click the **Save** button and wait until the **Agent Training** dialog indicates that training is complete. 

**Note:** If training phrases aren't automatically annotated, [manually annotate them](https://docs.cloud.google.com/dialogflow/docs/intents-training-phrases#annotation).

### Test your new entity

![Simulator screenshot](https://docs.cloud.google.com/static/dialogflow/es/docs/images/simulator-i-know-python.png)

In the simulator, enter `I know how to code in py`. Dialogflow correctly extracts `py` for the `language-programming` parameter, identifies it as the `Python` entity, and inserts the value into the response.

## Contexts

To control the flow of the conversation, you can use [contexts](https://docs.cloud.google.com/dialogflow/docs/contexts-overview).

### Add a follow-up intent

[_Follow-up intents_](https://docs.cloud.google.com/dialogflow/docs/contexts-follow-up-intents) let you control a conversation without manually creating and managing contexts.

When you create a follow-up intent, an [output context](https://docs.cloud.google.com/dialogflow/docs/contexts-input-output#output_contexts) is added to the parent intent, and an [input context](https://docs.cloud.google.com/dialogflow/docs/contexts-input-output#input_contexts) of the same name is added to the child intent. This means the follow-up intent is matched only when the parent intent is matched in the previous conversational turn.

Add a custom follow-up intent to the `set-language` intent:

  1. Select the `set-language` intent you created in previous steps.
  2. In the **Response** section, update the text response: 
     * `Wow! I didn't know you knew $language. How long have you known $language?`
  3. Click the **Save** button and wait until the **Agent Training** dialog indicates that training is complete. 
  4. Click **Intents** in the sidebar menu.
  5. Point the cursor at the `set-language` intent and click **Add follow-up intent**.
  6. Click **Custom** in the list.
  7. Click the **Save** button and wait until the **Agent Training** dialog indicates that training is complete. 



Dialogflow automatically names the follow-up intent `set-language - custom`.

![Followup screenshot](https://docs.cloud.google.com/static/dialogflow/es/docs/images/intents-followup-set-language.png)

### Intent matching with follow-up intents

Follow-up intents are matched only after the parent intent is matched. Because the `set-language - custom` intent is matched only after the `set-language` intent, the user has just been asked the question, "How long have you known $language?" Add training phrases for likely user answers to that question:

  1. Click **Intents** in the sidebar menu.
  2. Click the `set-language - custom` intent.
  3. Add the following training phrases: 
     * `3 years`
     * `about 4 days`
     * `for 5 years`
  4. Click the **Save** button and wait until the **Agent Training** dialog indicates that training is complete. 



### Test your follow-up intent

Enter `I know French` in the simulator, and then answer the question `How long have you known French` with `about 2 weeks`.

Despite there being no response for the second expression (`about 2 weeks`), you see the expression is matched to the correct intent (`set-language - custom`), and the duration parameter is correctly parsed (`2 weeks`).

### Intents and contexts

Inspect the `set-language` intent to see that `set-language-followup` is listed as an output context prefaced by the number 2. This number is called the [lifespan](https://docs.cloud.google.com/dialogflow/docs/contexts-input-output#lifespan).

![Output context screenshot](https://docs.cloud.google.com/static/dialogflow/es/docs/images/intent-output-context.png)

After the `set-language` intent is matched, the `set-language-followup` context is active and attached to the conversation for two turns (lifespan of 2). Therefore when you respond to a question like `How long have you known $language?`, the `set-language-followup` context is active.

Inspect the `set-language - custom` intent to see that `set-language-followup` is listed as an input context, which is the same as the output context for the `set-language` intent.

Any intents with an input context that matches an active context are prioritized when Dialogflow [matches intents](https://docs.cloud.google.com/dialogflow/docs/intents-matching).

### Contexts and parameters

Contexts store parameter values, and you can access the values of parameters defined in the `set-language` intent when its output context is active. In the `set-language - custom` intent, you only asked for the duration the user has known the language, and not the referenced language itself.

To reference the language in the response:

  1. Update the `set-language - custom` intent text response to `I can't believe you've known #set-language-followup.language for $duration!`
  2. Click the **Save** button and wait until the **Agent Training** dialog indicates that training is complete. 



The `#set-language-followup.language` reference is a [parameter reference for an active context](https://docs.cloud.google.com/dialogflow/docs/intents-actions-parameters#context).

### Test the context parameter

Enter `I know French` in the simulator, and then respond to the question with `1 week`. Notice that the `language` parameter value is retrieved from the context.

## Production

Before running your agent in production, implement the [production best practices](https://docs.cloud.google.com/dialogflow/es/docs/best-practices#prod).

## What's next

Try the [Fulfillment quickstart](https://docs.cloud.google.com/dialogflow/es/docs/quick/fulfillment).

[ Previous arrow_back  Setup and cleanup  ](https://docs.cloud.google.com/dialogflow/es/docs/quick/setup)

[ Next Fulfillment  arrow_forward  ](https://docs.cloud.google.com/dialogflow/es/docs/quick/fulfillment)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
