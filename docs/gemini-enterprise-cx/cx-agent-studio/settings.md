---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/settings/
title: Project and agent settings \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:36:29.864218+00:00
---

# Project and agent settings  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/settings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Project and agent settings Stay organized with collections  Save and categorize content based on your preferences. 

You can control a variety settings at the project location, agent application, and agent levels.

## Project location settings

Project location settings apply to every agent application and agent within the specific project and location. To edit project location settings, navigate to the agent list, select the project and location, then click the settings tune button.

The following project and location settings are available:

  * **VPC Service Controls** : See [VPC Service Controls](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/vpc-service-controls).
  * **Allowed origins** : If you are using VPC Service Controls, you can define the HTTP(S) endpoints that are allowed when making calls external to the agent application. This allows your agents to securely interact with external services without needing to route traffic through a proxy. This applies to all types of tools and callbacks, which can make external requests. If VPC Service Controls is not enabled (default), all endpoints are allowed. If VPC Service Controls are enabled, no endpoint is allowed unless it is added to the allowed origins list.

Endpoints are provided as exact match URLs (no wild cards), including the schema and optional port. Examples:

    * `https://example.com:8443`
    * `https://api.example.com`

To manage allowed origins, you need the following Identity and Access Management permissions:

    * `ces.googleapis.com/securitysettings.get`
    * `ces.googleapis.com/securitysettings.update`

These permissions are designed to be granted to security administrators or project administrators, separate from those who edit agent data. These permissions are included in the `CES Admin` predefined role.

This setting is applied at the project and location level to enable organizations to control allowed origins for all agent applications. The setting cannot be applied per agent-application or per agent. You can also use the API to update the [SecuritySettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/SecuritySettings) `EndpointControlPolicy`.




## Agent application settings

To edit global agent application settings:

  1. Click the settings icon on the right side of the builder.



The following agent application settings are available:

  * **Basic** : 
    * **Interactions** : 
      * **Global model** : Default [model](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/agent#model-support) used unless overridden by individual agents. Note that some models may be optimized for text or voice.
      * **Language controls** : 
        * **Default language** : Start all conversations in this language.
        * **Additional languages** : If your agent application is multilingual, provide additional languages. Your agent application will automatically switch languages to match the user input
        * **Unsupported language handling** : When user input is provided in an unsupported language, the agent application will ask the user to repeat the input once. If the new input is also using an unsupported language, select the action that should take place.
    * **Behavior** : 
      * **Voice** : See [Voice and speech](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/voice).
      * **Ambient sounds** : Background sounds played by the agent.
      * **Response length** : Adjust how verbose the agent is.
      * **Allow user interruptions** : Allow the end-user to interrupt the agent.
      * **Adapt when interrupted** : When enabled, agents will try to adapt their response considering that the user may not have heard everything.
      * **Fallback behavior** : 
        * **Retries** : If AI can't generate a response, select how many times the agent should retry.
        * **Agent response** : The agent will ask end-users for permission before every retry. You can provide a default response here. A default response is used if not provided.
        * **Fallback** : Decide what happens if the agent can't continue after the last retry attempt.
    * **Agent details** : 
      * **Display name** : Display name for the agent application.
      * **Lock agent** : Prevent changes from being applied.
      * **Notes** : Human-readable description of the agent application. This is not sent to the model.
  * **Advanced** : 
    * **Speech** : See [Voice and speech](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/voice).
    * **Logging** : 
      * **Logs and data sharing** : Manage agent-wide settings for logs and agent development. 
        * **Interaction data** : Store interaction data for deeper insights and your reference. This includes simulated and live interactions, tracing data, and more. If disabled, you won't be able to see past conversations with your agent.
      * **Enable redaction** : Automatically find and remove sensitive data.
      * **Enable Cloud Logging** : Automatically stream logs to [Cloud Logging](https://docs.cloud.google.com/logging/docs).
      * **Export logs to BigQuery** : Export logs to BigQuery for custom analysis.
      * **Audio recording** : Output Cloud Storage bucket location for audio files.
    * **Tools** : 
      * **Execution mode** : Execute tool calls in parallel or sequential order.
    * **Global instruction** : Instructions for all agents in the agent application. You can use these instructions to set up a stable identity or personality across agents.

**Note:** When you configure logs export to BigQuery, the dataset needs to exist in the same location as your agent. If you enter under BigQuery Dataset the name of a dataset that does not exist in the project, CX Agent Studio will create a dataset with the given name matching the location of your agent. If a dataset with the name already exists in a different location, a new dataset with the suffice `_<agent_location>` will be used instead.

## Agent settings

To edit root or sub-agent specific settings:

  1. Click the context menu in the agent title box.
  2. Select **Edit config**.



The following root and sub-agent settings are available:

  * **Agent name** : Display name for the agent. Use snake case.
  * **Model** : The [model](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/agent#model-support) used for the agent.
  * **Description** : A description of the agent. This description is provided to other agents in the agent application.
  * **Custom code** : Provide code for [callbacks](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/callback).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
