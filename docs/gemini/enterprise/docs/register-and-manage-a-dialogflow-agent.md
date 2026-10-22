---
url: https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-a-dialogflow-agent/
title: Register and manage Dialogflow agents \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:49:46.108904+00:00
---

# Register and manage Dialogflow agents  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-a-dialogflow-agent/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Register and manage Dialogflow agents Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to register and use Dialogflow agents with Gemini Enterprise.

## Overview

To use a Dialogflow agent with Gemini Enterprise, you must first deploy then register your agent. Registering your Dialogflow agent links your deployed agent to Gemini Enterprise so that they can communicate.

## Before you begin

Before registering your Dialogflow agent, you must ensure that these steps are completed:

  * Deploy your Dialogflow agent. To view the Dialogflow and conversational agents dashboard, see [Conversational agents](https://conversational-agents.cloud.google.com).

  * The [Gemini Enterprise Admin](https://docs.cloud.google.com/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin) role.

  * Enable the Discovery Engine API. To enable the Discovery Engine API for the Google Cloud project, in the Google Cloud console, go to the **Discovery Engine API** page.

[Go to Discovery Engine API](https://console.cloud.google.com/apis/api/discoveryengine.googleapis.com/metrics)

  * Create a Gemini Enterprise app. For more information, see [Create an app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app).




## Register a Dialogflow agent with Gemini Enterprise

You can register your Dialogflow agent with Gemini Enterprise using the Google Cloud console or the REST API. Registration makes your agent available to users within a Gemini Enterprise app.

**Agent registration quota and licensing:** Registering an agent with an app consumes one unit of your project's pooled daily agent creation quota (`discoveryengine.googleapis.com/agents_tier_enterprise_regional`). Quota is determined by the number of Gemini Enterprise Standard licenses (1 creation per user per day, pooled) or Plus licenses (10 per user per day, pooled) distributed to the project. Frontline licenses provide 0 creation quota.

If you register a backend agent across multiple Gemini Enterprise apps or engines in the same project, each registration API call (`agents.create`) counts as an agent creation against this daily quota. Automated deployment scripts or CI/CD pipelines registering an agent across many apps can encounter `HTTP 429 RESOURCE_EXHAUSTED: Agent creation quota exceeded` if the number of registration calls in a day exceeds the number of distributed Standard licenses. Ensure your project has sufficient Standard licenses distributed before executing multi-app rollouts. For more details, see [Daily creation quotas](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/quotas-and-limits#creation-quotas).

###  Console 

To register a Dialogflow agent using the Google Cloud console, follow these steps:

  1. In the Google Cloud console, go to the **Gemini Enterprise** page.

[Go to **Gemini Enterprise**](https://console.cloud.google.com/gemini-enterprise/products)

  2. Select your project.

  3. Click the name of the app that you want to register the agent with.

  4. Click **Agents > add Add Agents**. The **Choose an agent type** pane appears.

  5. On the **Custom agent via Dialogflow** card, click **Add** to register your Dialogflow agent with Gemini Enterprise. The **Configuration** pane opens.

  6. To configure your agent, follow these steps:

     1. Enter a name in the **Your agent name** field. This value appears in Gemini Enterprise as the display name of your agent.

     2. Enter a description in the **Describe your agent** field. This value is used by an LLM to determine whether to invoke your agent in response to a user query.

     3. Enter the resource path of the Dialogflow agent that you want to register with Gemini Enterprise in the **Dialogflow agent source** field.

Use this format: `projects/{project}/locations/{location}/agents/{agent}`

The **Agent availability** option, **When selected** , is set by default.

     4. Click **Create**.




###  curl 

This code sample demonstrates how you can register your agent:
    
    
      curl -X POST \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        -H "X-Goog-User-Project: PROJECT_ID" \
        "https://discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/assistants/default_assistant/agents" \
        -d '{
          "displayName": "DISPLAY_NAME",
          "description": "DESCRIPTION",
          "icon": {
            "uri": "ICON_URI"
          },
          "dialogflowAgentDefinition": {
            "dialogflowAgent": "projects/DIALOGFLOW_PROJECT_ID/locations/DIALOGFLOW_LOCATION/agents/DIALOGFLOW_AGENT_ID"
          }
        }'
    

Replace the variables with values:

  * PROJECT_ID: the ID of your Google Cloud project.
  * APP_ID: the ID of your Gemini Enterprise app.
  * DISPLAY_NAME: the user-friendly name for your agent that displays in Gemini Enterprise.
  * DESCRIPTION: a brief explanation of what your agent does that's visible to users in Gemini Enterprise. For example, _Extract key information from uploaded invoices for business travel_.
  * ICON_URI: the public URI of an icon that displays next to your Dialogflow agent's name. You can also provide a Base64-encoded image in `icon.content`.
  * DIALOGFLOW_PROJECT_ID: the Google Cloud project ID that identifies the location of your Dialogflow agent.
  * DIALOGFLOW_LOCATION: the specific geographic location where your Dialogflow agent is hosted, such as `global` or `us-central1`.
  * DIALOGFLOW_AGENT_ID: the unique identifier of your Dialogflow agent.



The successful response to this command returns all fields of the newly created Dialogflow agent resource, which includes its unique resource name in the name field. This resource name can be used for future updates or references.

## List agents connected to an app

The following code sample demonstrates how you can get the details of all the agents connected to your app:

###  REST 
    
    
    curl -X GET \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    "https://ENDPOINT_LOCATION-discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION/collections/default_collection/engines/APP_ID/assistants/default_assistant/agents"
    

Replace the variables with values:

  * ENDPOINT_LOCATION: the multi-region for your API request. Specify one of the following values: 
    * `us` for the US multi-region
    * `eu` for the EU multi-region
    * `global` for the Global location
For more information, see [Specify a multi-region for your data store](https://docs.cloud.google.com/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store). 
  * PROJECT_ID: the ID of your Google Cloud project.
  * LOCATION: the multi-region of your app: `global`, `us`, or `eu`.
  * APP_ID: the ID of your Gemini Enterprise app.



If your agent isn't prebuilt by Google, the response includes a `name` field in the first few lines. The value of this field contains the Agent ID at the end of the path. For example, in the following response, the Agent ID is `12345678901234567890`:
    
    
    {
    "name": "projects/123456/locations/global/collections/default_collection/engines/my-app/assistants/default_assistant/agents/12345678901234567890",
    ...
    }
    

## View details of a Dialogflow agent

The following code sample demonstrates how you can retrieve the details of an agent that was registered with Gemini Enterprise:

###  REST 
    
    
    curl -X GET \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    "https://ENDPOINT_LOCATION-discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION/collections/default_collection/engines/APP_ID/assistants/default_assistant/agents/AGENT_ID"
    

Replace the variables with values:

  * ENDPOINT_LOCATION: the multi-region for your API request. Specify one of the following values: 
    * `us` for the US multi-region
    * `eu` for the EU multi-region
    * `global` for the Global location
For more information, see [Specify a multi-region for your data store](https://docs.cloud.google.com/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store). 
  * PROJECT_ID: the ID of your Google Cloud project.
  * LOCATION: the multi-region of your app: `global`, `us`, or `eu`.
  * APP_ID: the ID of your Gemini Enterprise app.
  * AGENT_ID: the ID of the agent. You can find the agent ID by listing the agents connected to your app.



## Update a Dialogflow agent

All of the fields that were supplied during agent registration can be updated. The following fields are mandatory during the update process:

  * `displayName`
  * `description`
  * `reasoning_engine`



When updating a field, all fields and their values must be redefined in the update request, even if no changes are made to a particular field.

This code sample demonstrates how you can update the registration of your Dialogflow agent:

###  curl 
    
    
      curl -X PATCH \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        -H "X-Goog-User-Project: PROJECT_ID" \
      "https://discoveryengine.googleapis.com/v1alpha/AGENT_RESOURCE_NAME" \
        -d '{
          "displayName": "DISPLAY_NAME",
          "description": "DESCRIPTION",
          "icon": {
            "uri": "ICON_URI"
          },
          "dialogflowAgentDefinition": {
            "dialogflowAgent": "projects/PROJECT_ID/locations/REASONING_ENGINE_LOCATION/agents/DIALOGFLOW_AGENT_ID"
          }
        }'
    

Replace the variables with values:

  * PROJECT_ID: the ID of your Google Cloud project.
  * AGENT_RESOURCE_NAME: the resource name of the agent registration to be updated.
  * DISPLAY_NAME:tThe display name of the agent.
  * DESCRIPTION: the description of the agent that's displayed in Gemini Enterprise. The description is only for the user's benefit.
  * ICON_URI: the public URI of an icon that displays next to your Dialogflow agent's name. You can also provide a Base64-encoded image in `icon.content`.
  * REASONING_ENGINE_LOCATION: the cloud location of the reasoning engine that you're creating an agent at.
  * DIALOGFLOW_AGENT_ID: the unique identifier of your Dialogflow agent.



## Delete a Dialogflow agent

The following code sample demonstrates how you can delete an agent that is connected to your app:

###  REST 
    
    
    curl -X DELETE \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    "https://ENDPOINT_LOCATION-discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION/collections/default_collection/engines/APP_ID/assistants/default_assistant/agents/AGENT_ID"
    

Replace the variables with values:

  * ENDPOINT_LOCATION: the multi-region for your API request. Specify one of the following values: 
    * `us` for the US multi-region
    * `eu` for the EU multi-region
    * `global` for the Global location
For more information, see [Specify a multi-region for your data store](https://docs.cloud.google.com/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store). 
  * PROJECT_ID: the ID of your Google Cloud project.
  * LOCATION: the multi-region of your app: `global`, `us`, or `eu`
  * APP_ID: the ID of your Gemini Enterprise app.
  * AGENT_ID: the ID of the agent. You can find the agent ID by listing the agents connected to your app.



#### Example command and result
    
    
    curl -X DELETE \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    "https://global-discoveryengine.googleapis.com/v1alpha/projects/my-project-123/locations/global/collections/default_collection/engines/my-app/assistants/default_assistant/agents/12345678901234567890"
    
    
    * * *
    
    
    {
      "name": "projects/123456/locations/global/collections/default_collection/engines/my-app/assistants/default_assistant/agents/12345678901234567890/operations/delete-agent-12345678901234567890",
      "done": true
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
