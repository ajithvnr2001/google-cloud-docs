---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/example/
title: Playbook examples \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:43:40.218658+00:00
---

# Playbook examples  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/example/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Playbook examples Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** The Generative AI App Builder still refers to playbooks as **agents**. This will be updated to **playbook** soon in the console.

Each playbook should have one or more examples. These examples are sample conversations between an end-user and the playbook, including the dialogue and actions performed by the agent. These are effectively [few-shot prompt examples](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/few-shot-examples) for the LLM.

The console provides an interface for you to enter actions.

## Multilingual agents

If you want your agent to handle multiple languages, your examples should use each of the languages.

## Example input summary and output summary

In addition to input and output parameters, playbooks support receiving an **input summary** and emitting an **output summary** for exchanging information with other playbooks. Summaries are helpful for passing abstract contextual information between playbooks, while parameters are more helpful for passing structured, well defined fields between playbooks. Parameters are the only way to exchange data between flows and playbooks.

Add relevant input summaries to examples to condition the playbook to adjust its actions based on the input summaries at runtime. Add output summaries including relevant, accurate details about the example conversation to show the playbook what details are important to summarize.

**Note:** Examples for the [default playbook](https://docs.cloud.google.com/dialogflow/vertex/docs/concept/playbooks#default) **may not** define input parameters or an input summary. The default playbook serves as an entrypoint for user conversations, so it has no way to receive input parameters.

## Example state

At a given point in the conversation, a playbook will be in one of the following states:

  * `OK`: The playbook successfully achieved its goal and control will now transfer to the parent playbook.
  * `CANCELLED`: The user decided not to proceed with the goal assigned to the playbook. The control will now transfer to the parent playbook. If the parent playbook is a CX flow, intent of the user input will be detected before the flow runs.
  * `FAILED`: The playbook cannot proceed with the goal due to some error (e.g. tool returns 500 error). The session will end with status fail. An [EndInteraction](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment#EndInteraction) message will be added to the response.
  * `ESCALATED`: The playbook decided that it cannot achieve the goal and needs to escalate the situation to a human. The session will end with status escalated. An [EndInteraction](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment#EndInteraction) message will be added to the response.
  * `PENDING`: The conversation is still continuing within the playbook.



The top-level example and its playbook invocations should be denoted with a state which corresponds to the playbook they are referencing. 

## Selection strategy

The selection strategy setting controls whether an example is included in the playbook's prompt sent to the LLM. The following options are available:

  * **Dynamically select** : The example is conditionally included, based on how relevant it is for the current conversation context. The example may be omitted if the prompt is approaching the token limit. 

  * **Always select** : The example is always included, regardless of the conversation context. The example may be omitted if the prompt is approaching the token limit.

  * **Never select** : The example is never included in the prompt. The example will have no effect on the playbook's performance. This setting is useful for temporarily excluding an example for testing.




## Add action

An example provided within a playbook consists of a series of actions. These actions may vary in their combinations, but they primarily depict the interaction between the user and the playbook, along with the actions taken in between to fulfill the user's query or requirements.

There are two ways to add actions to an example:

  * To add an action manually, click the **+** button at the bottom of the right pane or the **Add action** button when you hold the pointer over existing actions. You can use these options when you create a new example by clicking the **\+ Example** option or when you edit an existing example.
  * To generate actions automatically based on the existing playbook instructions, enter a user input in the **Enter user input** field at the bottom of the right pane. You can use this option when you create or edit an example. Alternatively, you can use this option when you test your playbook at runtime in the **Preview playbook** pane on the right. To save actions to an example from the **Preview playbook** pane, click **Save example** after selecting the playbook invocation from the invocation list on the left of the **Preview playbook** pane.



Make sure to check the automatically generated actions correctness and edit them if necessary. This is especially important for the playbooks with few or no examples.

The following types of actions are supported by the playbook:

### Playbook response

The playbook response to the user query.

### User input

The user query.

### Tool use

This is a [tool](https://docs.cloud.google.com/dialogflow/vertex/docs/concept/tools) invocation to get additional information needed to fulfill the user's query. This action should specify the following details:

  * **Tool** : Name of the tool that should be invoked.

  * **Action** : Name of the operation for the [OpenAPI tool](https://docs.cloud.google.com/dialogflow/vertex/docs/concept/tools#openapi) that should be invoked. For [data store tools](https://docs.cloud.google.com/dialogflow/vertex/docs/concept/tools#data-store) and [function tool](https://docs.cloud.google.com/dialogflow/vertex/docs/concept/tools#function), the action name is the same as the tool name.

  * **Tool input** : Inputs to be included in the tool call. These are usually derived from the previous conversation turns with the user.

For [Open API tools](https://docs.cloud.google.com/dialogflow/vertex/docs/concept/tools#openapi), `requestBody` JSON is required for `POST`, `PUT` and `PATCH` method types.

Sample [Open API tool](https://docs.cloud.google.com/dialogflow/vertex/docs/concept/tools#openapi) `requestBody` input for createPet action:
        
        {
          "id": 1,
          "name": "Luna"
        }
        

For data store tool, the sample `requestBody` where the query is required and other fields are optional.
        
        {
          "query": "Where is my nearest store?",
          "filter": "country: ANY(\"United States\")",
          "userMetadata": {
            "userCity": "San Francisco",
          },
          "fallback": "We don't have any stores in your area."
        }
        

  * **Tool output** : The response of the tool invocation. This is a valid JSON response from the tool to the given input. For [Open API tools](https://docs.cloud.google.com/dialogflow/vertex/docs/concept/tools#openapi), it can also be a string error (for example, "404 Not found").

Sample [Open API tool](https://docs.cloud.google.com/dialogflow/vertex/docs/concept/tools#openapi) output for listPets action:
        
        {
          "pets": [
            {
              "id": 1,
              "name": "Luna"
            },
            {
              "id": 2,
              "name": "Charlie"
            }]
        }
        

Sample Data store tool output:
        
        {
          "answer": "Here's the address to your nearest store ...",
          "snippets": [
            {
              "title": "San Francisco Downtown",
              "uri": "https://www.example.com/San_Francisco_Downtown",
              "text": "Address for San Francisco Downtown .."
            }
          ]
        }
        




To ensure the playbook is fail-safe, also include examples of how the playbook should respond when tool invocation fails. [Open API tool](https://docs.cloud.google.com/dialogflow/vertex/docs/concept/tools#openapi) invocation failure can be represented as an error string ("404 not found") in the tool output. For [data store tools](https://docs.cloud.google.com/dialogflow/vertex/docs/concept/tools#data-store) the `fallback` input can be used to specify how to respond if there is no summarized answer.

If you want your [data store tool](https://docs.cloud.google.com/dialogflow/vertex/docs/concept/tools#data-store) to include URI in the playbook response, add examples which contain the URI you want the playbook to respond with. If this URI is coming from the [data store tool](https://docs.cloud.google.com/dialogflow/vertex/docs/concept/tools#data-store), then the [data store tool](https://docs.cloud.google.com/dialogflow/vertex/docs/concept/tools#data-store) output should contain a URI which matches the URI in the playbook response. Note `fallback` cannot be used in this scenario because it will disable the capability of the LLM playbook to rephrase the [data store tool](https://docs.cloud.google.com/dialogflow/vertex/docs/concept/tools#data-store) answer to include URIs in playbook response.

Examples containing tool use actions can get quite verbose and contribute to increased input [token limit](https://docs.cloud.google.com/dialogflow/vertex/quotas#limit) consumption. To ensure efficient use of tokens, ensure that tool outputs are concise and contain information relevant to the playbook's goals. For [data store tools](https://docs.cloud.google.com/dialogflow/vertex/docs/concept/tools#data-store), consider removing snippets from examples as they can contribute to high input token consumption.

### Playbook invocation

This action is used when the playbook should invoke another task playbook to fulfill the user query. This action should specify the following details:

  * **Playbook** : Name of the playbook to be invoked.
  * **Playbook invocation input summary** : A summary of the relevant portions of the preceding conversation useful to the playbook being invoked.
  * **Input parameters** : [Input parameters](https://docs.cloud.google.com/dialogflow/vertex/docs/concept/parameters#input) to pass to the playbook.
  * **Playbook invocation output summary** : A summary of what the playbook should generate upon completion of its goal.
  * **Output parameters** : [Output parameters](https://docs.cloud.google.com/dialogflow/vertex/docs/concept/parameters#output) generated by the playbook upon completion of its goal.



### Playbook transition

A playbook transition action is a terminal action (should not be followed by other actions) which indicates that the [routine playbook](https://docs.cloud.google.com/dialogflow/vertex/docs/playbook#routine) has decided to exit and transition to a target routine playbook. Note that since this action indicates that the playbook exits, add the playbook's output parameters to the example's playbook output.

### Flow invocation

This action is used when the task playbook should invoke a flow. This action should specify the following details:

  * **Flow** : Name of the flow to be invoked.
  * **Flow input parameters** : Input parameters to pass to the flow.
  * **Flow return parameters** : Output parameters returned from the flow.



### Flow transition

A Flow transition action is a terminal action (should not be followed by other actions) which indicates that the [routine playbook](https://docs.cloud.google.com/dialogflow/vertex/docs/playbook#routine) has decided to exit and transition to a target flow. Note that since this action indicates that the playbook exits, add the playbook's output parameters to the example's playbook output.

[ Previous arrow_back  Playbook conditional actions  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/conditional-actions)

[ Next Playbook parameters  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/parameter)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
