---
url: https://docs.cloud.google.com/dialogflow/es/docs/agents-versions/
title: Versions and environments \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:45:35.691770+00:00
---

# Versions and environments  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/agents-versions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  Versions and environments Stay organized with collections  Save and categorize content based on your preferences. 

You can create multiple versions of your agent and publish them to separate environments.

When you edit an agent, you are editing the _draft agent_. At any point, you can save the draft agent as an _agent version_ , which is an immutable snapshot of your agent.

When you save the draft agent, it is published to the _default environment_. When you create agent versions, you can publish them to _custom environments_. You can create a variety of custom environments for:

  * testing
  * development
  * production
  * etc.



## Production traffic

### Always use agent versions for production traffic

A draft agent is updated every time a developer on your team makes a change. It is easy to break a draft agent unintentionally, especially if multiple people have write access to the agent. In addition, a recently edited draft agent may be inconsistent with the trained model, because training may have a delay or require manual execution.

You should always use agent versions for your production traffic. Draft agents should be tested before promoting them to production versions, and you can rollback to a previous version if any problems are discovered.

### Consider possible agent errors while changing versions

If you change an agent version in your production environment while sessions are active, it may cause agent errors for some active sessions. These errors may happen if the previous and new versions are inconsistent with each other in a way that disrupts session state. Due to this, you should plan to change versions during down-time or off-peak hours.

## Publish a version in a new environment

To publish an agent draft to a version and create a custom environment:

### Console

  1. Go to the [Dialogflow ES console](https://dialogflow.cloud.google.com).
  2. Select your agent near the top of the left sidebar menu.
  3. Click the settings _settings_ button next to the agent name.
  4. Click the **Environments** tab.
  5. Click **Publish a version**.
  6. Add an optional description and click **Next**.
  7. Select **+New Environment**.

**Note:** You can create an agent version without publishing it by selecting **Create version without publishing** from the environment menu.
  8. Enter an environment name.

  9. Choose the fulfillment method for the environment.

  10. Select Text-to-speech settings for the environment.

  11. Click **Publish**.

  12. The environment information is now listed in the **Custom environments** section.




### API

  1. Call the `create` method for the [Version type](https://docs.cloud.google.com/dialogflow/es/docs/reference/common-types#versions) to create a new agent version.
  2. Call the `create` method for the [Environment type](https://docs.cloud.google.com/dialogflow/es/docs/reference/common-types#environments) to create a new environment. Provide the agent version you just created to the `agentVersion` field.



## Revert an environment to a previous version

You can revert an environment to a previous agent version:

### Console

  1. Click an environment in the **Custom environments** section.
  2. The environment settings dialog opens.
  3. Click the option _more_vert_ button for a previously published version in the **Publishing History** section.
  4. Click **Revert to this version**.
  5. The publishing history will be updated.



### API

Call the `patch`/`update` method for the [Environment type](https://docs.cloud.google.com/dialogflow/es/docs/reference/common-types#environments) to update an environment. Provide the agent version you previously created to the `agentVersion` field.

## Load a previous version to draft

Loading a previous version to draft overwrites the draft agent in the default environment with a selected agent version.

**Caution:** Loading a previous version to draft will negate all recent changes to draft and can't be undone. You may want to save the draft to a version before taking these steps.

To load a previous version to draft:

### Console

  1. Go to the [Dialogflow ES console](https://dialogflow.cloud.google.com).
  2. Select your agent near the top of the left sidebar menu.
  3. Click the settings _settings_ button next to the agent name.
  4. Click the **Environments** tab.
  5. Click **View all versions** in the **Draft** section.
  6. Click the option _more_vert_ button for a version that you want to load to draft.
  7. Click **Load to Draft**.
  8. Click **Yes, I'm sure**.
  9. Reload any open console browser tabs, so they are refreshed with the latest agent data.



### API

Call the `patch`/`update` method for the [Environment type](https://docs.cloud.google.com/dialogflow/es/docs/reference/common-types#environments) with the following inputs:

  * Use `-` as the environment ID to specify the default environment.
  * Set `allowLoadToDraftAndDiscardChanges` to true.
  * For the `agentVersion` field, supply the agent version that will overwrite the draft agent.



## Export a version

To export a version, you need to load it to draft first, then [export the agent](https://docs.cloud.google.com/dialogflow/es/docs/agents-settings#export).

## Test your agent in an environment

You can use the API to test your agent in any of your custom environments. Call the [detect intent](https://docs.cloud.google.com/dialogflow/docs/quick/api) method, but alter the endpoint URL by inserting `environments/environment-name/users/-/` between `agent` and `sessions`.

For example, the following endpoint uses the "development" environment with an unspecified user:
    
    
    "https://dialogflow.googleapis.com/v2/projects/my-project-id/agent/environments/development/users/-/sessions/123456789:detectIntent"
    

## Environment-specific settings

Fulfillment and text-to-speech are configured by the environment, so the agent will use the environment's settings for these features.

For more information about how data is applied at various levels, see [agent application levels](https://docs.cloud.google.com/dialogflow/es/docs/data-level).

## Google Assistant

If you are using [Actions on Google release environments](https://developers.google.com/assistant/console/releases), see the versioning limitations for the [Dialogflow fulfillment library](https://docs.cloud.google.com/dialogflow/docs/fulfillment-inline-editor#library).

## Mega agent

See [how versions and environments work in mega agents](https://docs.cloud.google.com/dialogflow/es/docs/agents-mega#versions).

## Limitations

The following limitations apply:

  * Maximum number of environments per agent: 10
  * Maximum number of versions per agent: 1000



[ Previous arrow_back  Prebuilt agents  ](https://docs.cloud.google.com/dialogflow/es/docs/agents-prebuilt)

[ Next Multilingual agents  arrow_forward  ](https://docs.cloud.google.com/dialogflow/es/docs/agents-multilingual)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
