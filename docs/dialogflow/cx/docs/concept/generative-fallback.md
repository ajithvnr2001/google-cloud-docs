---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/generative-fallback/
title: Generative fallback \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:43:19.956686+00:00
---

# Generative fallback  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/generative-fallback/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Generative fallback Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** The _Generative fallback_ feature is excluded from the [Dialogflow CX SLA](https://cloud.google.com/dialogflow/sla).

The _generative fallback_ feature uses Google's latest generative large language models (LLMs) to generate virtual agent responses when end-user input doesn't match an intent or parameter for form filling.

The feature can be configured with a _text prompt_ that instructs the LLM how to respond. You can use a predefined text prompt or add your own prompts. With the predefined prompt, the virtual agent is able to handle basic conversational situations. For example:

  * Greet and say goodbye to the user.
  * Repeat what the agent said in case the user didn't understand.
  * Hold the line when the user asks for it.
  * Summarize the conversation.



You can enable generative fallback on _no-match event handlers_ used in flows, pages, or during parameter filling. When generative fallback is enabled for a no-match event, whenever that event triggers, Dialogflow CX will attempt to produce a generated response that will be said back to the user. If the response generation is unsuccessful, the regular prescribed agent response will be issued instead.

## Limitations

The feature is available in the [languages supported by the Gemini API](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/models#gemini-models).

## Enable generative fallback

You can enable generative fallback in your agent on _no-match event handlers_ , which can be used in flow, page or parameter fulfillment.

### Enable generative fallback for an entire flow's no-match events

  1. Go to the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects).
  2. Select a project.
  3. Select an agent, then select a flow.
  4. Click the **Start Page** of the flow to expand it.
  5. Click **sys.no-match-default** under **Event handlers**.
  6. Select **Enable generative fallback** under **Agent responses**.
  7. Click **Save**.



### Enable generative fallback on specific no-match events

  1. Navigate to the target **No-match** event handler (any event starting with **No-match** , such as **No-match default** , **No-match 1** , and so on).
  2. Select **Enable generative fallback** under **Agent responses**.
  3. Click **Save**.



## Configure generative fallback

As mentioned earlier, the _generative fallback_ feature passes a request to a large language model in order to produce the generated response. The request takes the form of a _text prompt_ that is a mix of natural language and information about the current state of the agent and of the conversation. The prompt and the generated response are checked against a list of _banned phrases_. If they contain any banned phrase, or are otherwise deemed unsafe, generation will be unsuccessful, and the regular prescribed response (under _Agent says_ in the same fulfilment) will be issued instead.

The feature can be configured in multiple ways:

  1. Select a predefined prompt.
  2. Define a custom prompt.
  3. Add or remove phrases from the list of banned phrases.



When creating a prompt, in addition to a natural language description of what kind of context should be generated, the following _placeholders_ can also be used:

X | Item  
---|---  
**$conversation** | The conversation between the agent and the user, excluding the very last user utterance.  
**${conversation USER:" <user prefix>" AI:"<agent prefix>" TURNS:<turn count>}** | A parameterized version of the `$conversation` placeholder. You can customize the end-user prefix (`USER`), the agent prefix (`AI`), and the number of previous turns to include (`TURNS`). All placeholder parameter values must be specified. For example, `${conversation USER:"Human says:" AI:"Agent says:" TURNS:4}`.  
**$last-user-utterance** | The last user utterance.  
**$flow-description** | The **flow description** of the active flow.  
**$route-descriptions** | The **intent descriptions** of the active intents.  
  
Make sure to have good flow and intent descriptions.

### Choose a predefined prompt

  1. In **Agent Settings** , go to the **Generative AI** tab, and then the **Generative Fallback** sub-tab.
  2. Select one of the options in the **Template** drop-down.
  3. Click **Save**.



The feature provides two template prompts, the **Default** template (which is not visible) and the **Example** template that can serve as a guide for writing your own prompts.

### Define your own prompt

  1. In **Agent Settings** , go to the **Generative AI** tab, and then the **Generative Fallback** sub-tab.
  2. Select **\+ new template** in the **Template** drop-down.
  3. Add a **Template name**.
  4. Add a **Text prompt**.
  5. Click **Save**.



You can also start by editing the **Example** template and saving it as a new template:

  1. Select **Example** in the **Template** drop-down.
  2. Click **Edit**.
  3. Edit the **Template name**.
  4. Edit the **Text prompt**.
  5. Click **Save**.



### Modify the list of banned phrases

**Note:** Any banned phrases in this list will apply to [generators](https://docs.cloud.google.com/dialogflow/cx/docs/concept/generative/generators) and generative fallback responses.

  1. In **Agent Settings** , navigate to the **Generative AI** tab, and then the **General** sub-tab.
  2. In the **Banned phrases** section, inspect, add to, or remove phrases from the list.
  3. Click **Save**.



## Test generative fallback

You can test the _generative fallback_ feature in the simulator. Whenever a user utterance leads to no-match on a flow or a page where the no-match event was configured to produce a generative response (and the generation succeeds), the agent will output the generated response.

## Codelab

Also see the [Generative fallback codelab](https://codelabs.developers.google.com/codelabs/dialogflow-generative-fallback).

## Troubleshooting

**Note:** The steps outlined in this section are only available for **non-default prompt templates**.

If you want to debug the feature, you can inspect the resolved large language model (LLM) input prompt in Dialogflow console simulator:

  1. Click the **original response** button:

![Original response](https://docs.cloud.google.com/static/dialogflow/cx/docs/images/original-response.png)

  2. Locate the **"Generative Fallback Prompt"** field. Read these fields as plain text and check whether the LLM input makes sense. If any phrase contains `$`, examine the simulator input and clarify whether the `$` in the prompts are intentional (for example, `$` in `price is $10` would likely be intentional, while `visit $city` would likely not and could imply either misuse or a bug). If you are unsure, [contact Support](https://docs.cloud.google.com/dialogflow/docs/support/getting-support#gcp-support).

  3. If you are using a non-default prompt template but can't see the "Generative Fallback Prompt" field, [contact Support](https://docs.cloud.google.com/dialogflow/docs/support/getting-support#gcp-support).




[ Previous arrow_back  Generators  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/generators)

[ Next Overview  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
