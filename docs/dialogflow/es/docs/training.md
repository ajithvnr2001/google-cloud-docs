---
url: https://docs.cloud.google.com/dialogflow/es/docs/training/
title: Training \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:45:46.798764+00:00
---

# Training  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/training/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  Training Stay organized with collections  Save and categorize content based on your preferences. 

When your agent is trained, Dialogflow uses your training data to build machine learning models specifically for your agent. This training data primarily consists of intents, intent training phrases, and entities referenced in an agent; which are effectively used as machine learning data labels. However, agent models are built using parameter prompt responses, agent settings, and many other pieces of data associated with your agent.

Whenever you change your agent, you should ensure that the agent is trained before attempting to use it. Depending on your agent settings, training may occur automatically or manually.

You can also use the Training Tool to analyze and import actual conversation data, and to improve your training data.

## Draft agent automatic training

By default, agent training for a [draft agent](https://docs.cloud.google.com/dialogflow/es/docs/agents-versions) is executed automatically every time you update and save the agent from the console. Popup dialogs will display the status of this training.

However, updating your agent with the API does not trigger automatic training.

## Draft agent manual training

You can update agent [ML settings](https://docs.cloud.google.com/dialogflow/es/docs/agents-settings#ml) to disable automatic training for a draft agent.

If your agent has more than 780 intents, or if you have disabled the automatic training setting, you must manually execute training.

To manually train an agent from the console, click the **Train** button in the ML settings.

To manually train an agent with the API, call the `train` method on the [Agent](https://docs.cloud.google.com/dialogflow/docs/reference/common-types#agents) type.

**Note:** After [restore or import](https://cloud.google.com/dialogflow/es/docs/agents-settings#export), the agent is retrained, even if the automatic training is disabled.

## Agent version automatic training

Whenever a new [agent version](https://docs.cloud.google.com/dialogflow/es/docs/agents-versions) is created, the new agent version is automatically trained.

To create a new agent version from the console, click the **Publish a version** button on the Environments tab.

To create a new agent version with the API, call the `create` method for the [Version type](https://docs.cloud.google.com/dialogflow/es/docs/reference/common-types#versions) to create a new agent version.

## Training Tool

The Training Tool is used to review end-users inputs sent to your agent and to improve your training data. Using the tool, you can:

  * Review actual end-users inputs and the intents that are matched for each conversational turn with the current agent model.
  * Add the end-user expressions from these conversations to the training phrases of the matched intents, different intents, or fallback intents.
  * Import end-user expressions you have prepared or captured from actual conversations.



The tool uses [agent history](https://docs.cloud.google.com/dialogflow/docs/history) data to load conversations, so [interaction logging](https://docs.cloud.google.com/dialogflow/docs/agents-settings#general) must be enabled to use the tool. The Training Tool only shows end-user expressions. To view both agent and end-user conversation data, see the more complete agent history.

To open the Training Tool:

  1. Go to the [Dialogflow ES console](https://dialogflow.cloud.google.com).
  2. Select your agent near the top of the left sidebar menu.
  3. Click **Training** in the left sidebar menu.



### Conversation list

When you open the tool, it shows the conversation list. This is a list of recent conversations in reverse chronological order. Each row in the list provides a summary of a conversation. The following table describes each of the UI elements:

UI Element | Description  
---|---  
Conversation | The first end-user expression in the conversation.  
Date | The date that the conversation occurred or was imported.  
_refresh_ | When a conversation is used to update training data (as described below), the status indicator for the row shows a green checkmark.  
  
### Training view

When you click a row in the conversation list, it opens the conversation in training view. The training view shows a list of conversational turns and provides controls to add this data to your training data.

**Note:** You don't have to worry about duplicate training phrases. If you add training phrases that already exist to an intent, Dialogflow will merge them into one example.

When you edit the displayed data or click a task button on the right, you create training data update tasks that get queued for saving. Once you are done creating tasks, click the **Approve** button to execute all queued tasks. Once approved, you should manually train your agent.

![Training view screenshot](https://docs.cloud.google.com/static/dialogflow/es/docs/images/training-process.png)

The following table describes each of the UI elements:

UI Element | Description  
---|---  
Date | The date that the conversation occurred or was imported.  
Requests | The number of rows for the conversation.  
No Match | The number of rows for which no intent is matched.  
User Says | The end-user expression for the row.  
Intent | The intent for this row matched with the current agent model. You can click the link to change the associated intent to a new or existing intent.  
_check_ | Queues a task to add the end-user expression for the row as a training phrase to the currently selected intent. The icon turns green when a task is queued.  
_block_ | Queues a task to add the end-user expression for the row as a training phrase to the default fallback intent. This creates a [negative example](https://docs.cloud.google.com/dialogflow/docs/intents-default#negative-examples). The icon turns orange when a task is queued.  
_delete_ | Queues a task to delete the row. The icon turns red when a task is queued.  
Approve | Executes queued tasks for all rows.  
  
### Annotations

When looking at a conversation in training view, end-user expressions show matched entities as highlighted [annotations](https://docs.cloud.google.com/dialogflow/docs/intents-training-phrases#annotation). To add or edit an annotation:

  1. Click an annotation or select the words you want to annotate.
  2. Choose an existing entity from the menu.



![Annotation screenshot](https://docs.cloud.google.com/static/dialogflow/es/docs/images/training-entity-annotations.png)

### Import conversations

You can import conversation data files you have prepared or captured to the Training Tool. Importing conversations can be used to improve an existing agent. To upload a conversation, click the **Upload** button at the top of the page. Then, you can analyze this data for adding to training data as described above.

The following describes the file content format, its limitations, and the results:

  * Each uploaded file results in a single conversation in the Training Tool.
  * Requests are not sent to the detect intent API, therefore, no contexts are activated and no intents are matched.
  * A single text file or a zip archive that can contain up to 10 text files.
  * One upload cannot exceed 3 MB.
  * The files should only contain end-user expressions delimited by newlines.
  * Ideally, files should only include data that is useful as training phrases.
  * The order of the end-user expressions is not important.



Here is an example file:
    
    
    I want information about my account.
    What is my checking account balance?
    How do I transfer money to my savings account?
    

### Limitations

  * The Training Tool is only available for the `global` [region](https://docs.cloud.google.com/dialogflow/es/docs/how/region).
  * The Training Tool does not take the [ML Classification Threshold](https://docs.cloud.google.com/dialogflow/es/docs/agents-settings#ml) setting into consideration for intent matching. You may see different intents matched at runtime and in the Training tool, even if the agent model has not changed.
  * End-user inputs containing [required](https://docs.cloud.google.com/dialogflow/es/docs/intents-actions-parameters#required) parameter values may not match to the expected intents in the Training tool, while matching correctly at runtime. This may happen in the following situations: 
    * There are no annotated training phrases in that intent.
    * The input significantly differs from the training phrases.



## Best practices

### Use the Training Tool at various stages of development

Use the Training Tool at various stages of agent development, and refine your training data at each stage:

  * Before your agent is released to production, test it with a small group of users.
  * Shortly after your agent is released to production, examine if real conversations are behaving as expected.
  * Whenever significant changes are made to your agent, check that the new changes are behaving as expected.
  * Run the tool periodically for production agents, to perform regular analysis.



### Import quality data

The following can often be useful sources of data:

  * Logs of conversations with human customer service agents.
  * Online customer support conversations (email, forums, FAQs).
  * Customer questions on social media.



You should avoid the following types of data:

  * Long-form, non-conversational end-user expressions.
  * End-user expressions that are not relevant to any of the intents in your agent.
  * Logs of things not said by end-users (for example, responses from customer service agents).



[ Previous arrow_back  Knowledge connectors  ](https://docs.cloud.google.com/dialogflow/es/docs/knowledge-connectors)

[ Next Access control  arrow_forward  ](https://docs.cloud.google.com/dialogflow/es/docs/access-control)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
