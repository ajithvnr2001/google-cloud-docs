---
url: https://docs.cloud.google.com/dialogflow/es/docs/agents-mega/
title: Mega agents \u00a0|\u00a0 Dialogflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:42:31.526137+00:00
---

# Mega agents  |  Dialogflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/agents-mega/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  Mega agents Stay organized with collections  Save and categorize content based on your preferences. 

You can combine multiple Dialogflow agents, called _sub-agents_ , into a single agent, called a _mega agent_. When you perform a detect intent request against a mega agent, all of the sub-agents are considered, and the best response from the sub-agents is returned.

There are a variety of reasons that you may want to use mega agents:

  * **Better governance** : If you have multiple teams building an agent, each team can be responsible for one sub-agent, which simplifies change conflicts across teams.
  * **More intents** : If you have agents with a large number of intents, you may approach the [intent count limit](https://docs.cloud.google.com/dialogflow/quotas). In this case, you could create multiple sub-agents and one mega agent.



## Limitations

The following limitations apply to mega agents:

  * A mega agent and its sub-agents must be created in the same [region](https://docs.cloud.google.com/dialogflow/es/docs/how/region).
  * Within one region, a mega agent and its sub-agents are all associated with different Google Cloud projects.
  * A mega agent can have at most 10 sub-agents.
  * [Small talk](https://docs.cloud.google.com/dialogflow/docs/agents-small-talk) does not work for mega agents.
  * Sub-agent intent priority has no effect on intent matching when sending requests to a mega agent.
  * The [Google Assistant integration](https://docs.cloud.google.com/dialogflow/docs/integrations/aog) cannot be used with mega agent.
  * Partner built-in telephony integrations ([AudioCodes](https://docs.cloud.google.com/dialogflow/docs/integrations/audiocodes), [Avaya](https://docs.cloud.google.com/dialogflow/docs/integrations/avaya), [SignalWire](https://docs.cloud.google.com/dialogflow/docs/integrations/signalwire), [Voximplant](https://docs.cloud.google.com/dialogflow/docs/integrations/voximplant)) are not supported.
  * The mega agent does not support [fallback intents](https://docs.cloud.google.com/dialogflow/es/docs/intents-default#fallback) used as [follow-up intents](https://docs.cloud.google.com/dialogflow/es/docs/contexts-follow-up-intents).



## Creating sub-agents

You create sub-agents [like any other agent](https://docs.cloud.google.com/dialogflow/docs/quickstart-console). Add any intents, contexts, entities, etc. as necessary to build your agents.

## Creating or updating a mega agent

You can use the Dialogflow Console to create a mega agent and link it to sub-agents.

Dialogflow takes most agent settings from the mega agent into account and logs data to the mega agent. For example:

  * [Dialogflow takes agent-wide logging, sentiment, speech-to-text and text-to-speech settings](https://docs.cloud.google.com/dialogflow/docs/agents-settings) from the mega agent.
  * Dialogflow stores [analytics](https://docs.cloud.google.com/dialogflow/docs/analytics), [conversation history](https://docs.cloud.google.com/dialogflow/docs/history) and [data for the training tool](https://docs.cloud.google.com/dialogflow/docs/training) in the mega agent.

**Warning:** Dialogflow ignores all resources in a mega agent except basic fallback intents. For example, other intents, follow-up fallback intents, contexts, and entities are all ignored.

### Web UI

### 1\. Create a mega agent

  1. Go to the [Dialogflow ES console](https://dialogflow.cloud.google.com).
  2. Click **Create Agent** in the left sidebar menu. (If you already have other agents, click the agent name, scroll to the bottom and click **Create new agent**.)
  3. Enter your agent's name, default language, default time zone and Google Cloud project.
  4. Set the **Agent Type** as **Mega Agent**.
  5. Click the **Create** button.



### 2\. Add and manage sub-agents

  1. Click **Sub Agents** in the left sidebar menu.
  2. Select a sub-agent you wish to add to the mega agent.
  3. The sub-agent **Environment** defaults to **Draft** , but you can update this as needed.
  4. If you want to use the **Knowledge Base** associated with the sub-agent, change the field from **Excluded** to **Included**.
  5. Click **Save**.



## Set up roles

Depending on how you plan to use your mega agent, you need to grant specific [roles](https://docs.cloud.google.com/dialogflow/docs/access-control#roles) in your sub-agent projects, so the mega agent has permission to make calls to the sub-agents. To set up these roles:

  1. Create the mega agent and sub-agent Google Cloud projects as you normally would, and ensure you have enabled the "Dialogflow API" for each.
  2. If you plan on [using the API](https://docs.cloud.google.com/dialogflow/docs/api-overview) to interact with your mega agent, you must grant a role on each of your sub-agent projects to the service account you use for mega agent API calls, and the role should have permission to make detect intent calls. The following [roles](https://docs.cloud.google.com/dialogflow/docs/access-control#roles) will provide this access: Project Owner, Project Editor, Dialogflow API Admin, or Dialogflow API Client. To get this service account's email address: 
     1. Visit the [IAM service account page](https://console.cloud.google.com/iam-admin/serviceaccounts).
     2. Select the project for your mega agent.
     3. Either select a service account you already created for API calls or add a new service account that has the desired role. Follow the [setup instructions](https://docs.cloud.google.com/dialogflow/docs/quick/setup#auth) to create a new service account and download a private key.
     4. Take note of the chosen service account email address. You will need this below.
  3. If you plan on using any [integrations](https://docs.cloud.google.com/dialogflow/docs/integrations) for the mega agent, the [automatically created](https://docs.cloud.google.com/dialogflow/docs/access-control#auto-service-accounts) service-project-number@gcp-sa-dialogflow.iam.gserviceaccount.com service account for the mega agent's project must have a role on that project that includes permission to make detect intent calls. The following [roles](https://docs.cloud.google.com/dialogflow/docs/access-control#roles) will provide this access: Project Owner, Project Editor, Dialogflow API Admin, or Dialogflow API Client. To get this service account's email address:

     1. Visit the [IAM main page](https://console.cloud.google.com/iam-admin/iam).
     2. Select the project for your mega agent.
     3. Enable the **Include Google-provided role grants** option on the right.
     4. Find the service account that matches the pattern:  
service-project-number@gcp-sa-dialogflow.iam.gserviceaccount.com.
     5. Take note of the chosen service account email address. You will need this below.
**Caution:** If this service account is not populated, you may need to send at least one request to your mega agent using an integration. You can use the [Dialogflow Messenger](https://docs.cloud.google.com/dialogflow/es/docs/integrations/dialogflow-messenger) integration as an easy way to do this, or you could setup your desired [integration](https://docs.cloud.google.com/dialogflow/es/docs/integrations) for the mega agent prior to configuring sub-agents. The Hangouts Chat, Dialogflow Messenger, Facebook Messenger, and Facebook Workplace integrations each automatically create this special service account.
  4. For each sub-agent project, grant roles to the mega agent service accounts you collected above:

     1. Visit the [IAM main page](https://console.cloud.google.com/iam-admin/iam).
     2. Select the project for your sub-agent.
     3. [Grant the desired roles](https://docs.cloud.google.com/iam/docs/granting-roles-to-service-accounts) to your mega agent's service account email addresses on the project.



## Detect intent

To detect intent, call the request like any other [detect intent request](https://docs.cloud.google.com/dialogflow/docs/quickstart-api#detect_intent) and use the mega agent's project ID. Dialogflow will consider all of the sub-agents, and the best response from the sub-agents is returned.

For example, consider the following sub-agents:

Sub-agent | Intent | Training Phrases  
---|---|---  
Orders | Books | "I want to buy a book"  
"Add a book to my cart"  
Hats | "I want to purchase a hat"  
"I want a hat"  
Account | Balance | "What is my balance?"  
"How much is left in my account?"  
Address | "I want to change my address"  
"I have a new address"  
  
If an end-user says "I want to buy a hat please", a detect intent request sent to the mega agent will result in a match for the `Hats` intent in the `Orders` agent.

To specify one or more sub-agents for a detect intent request, set the `subAgents` field of [`QueryParameters`](https://docs.cloud.google.com/dialogflow/docs/reference/rest/v2/QueryParameters). For example, the REST JSON for this request would look like:
    
    
    {
      "queryInput": {
        "text": {
          "text": "reserve a meeting room for six people",
          "languageCode": "en-US"
        }
      },
      "queryParams": {
        "subAgents": [
           {"project": "projects/sub-agent-1-project-id"},
           {"project": "projects/sub-agent-2-project-id"}
        ]
      }
    }
    

## Invoking events

To [invoke an event from a webhook service](https://docs.cloud.google.com/dialogflow/docs/events-custom#invoke_event_from_webhook), you can specify the sub-agent for the intent you wish to trigger. Use the following event name format:
    
    
    sub-agent-project-id.event-name

For example, if the sub-agent project ID is `123`, and the event name is `alarm` for the desired intent, use `123.alarm` for the event name.

If you do not specify a sub-agent for the event, the event will be sent back to the sub-agent that contains the previously matched intent.

**Note:** When specifying sub-agents for events, you should only use the mega agent for detect intent requests, and you should not send detect intent requests directly to sub-agents.

## Setting output context

To set output contexts from a webhook service, you can specify the sub-agent that the context belongs to. Use the following format:
    
    
    projects/mega_agent_project_id/agent/sessions/session_id/contexts/sub_agent_project_id.context_name
    

For example, if the session is `projects/mega_agent_project_id/agent/sessions/session_id`, and you want to set a context named `music_context` for a sub-agent with project ID `sub_project_1`, you can set the output context with the following name:
    
    
    projects/mega_agent_project_id/agent/sessions/session_id/contexts/sub_project_1.music_context
    

If you don't specify a sub-agent prefix for the context name, the system will consider it as a context of the mega agent.

## Context lifespan

When a context becomes active, the [context lifespan](https://docs.cloud.google.com/dialogflow/es/docs/contexts-input-output#lifespan) normally determines how many conversational turns will occur before the context becomes inactive. Essentially, the runtime lifespan of an active context is decremented for each conversational turn after it becomes active.

This behavior may be different for mega agents. During a conversation, intents from different sub-agents may be matched for each conversational turn. When an intent from a sub-agent is matched, and the intent has an output context, the lifetime of this context is only decremented for further matches of intents in the same sub-agent.

For example, an intent match occurs in sub-agent **A** , and the intent has an output context which activates a context. Any matches of intents in sub-agent **B** do not decrement the runtime lifespan for the active context that was originated in sub-agent **A**.

## Versions and Environments

[Versions and environments](https://docs.cloud.google.com/dialogflow/es/docs/agents-versions) on the mega agent level allow you to create different snapshots of the mega agent's fallback intent and set diffent webhooks and Text-to-Speech settings for different mega agent's environments.

Settings on the mega agent's **Sub Agents** console page are not included in the mega agent's versions and environments. Mega agent requests always triger sub-agents' environments specified on that page at that moment.

[ Previous arrow_back  Multilingual agents  ](https://docs.cloud.google.com/dialogflow/es/docs/agents-multilingual)

[ Next Small talk  arrow_forward  ](https://docs.cloud.google.com/dialogflow/es/docs/agents-small-talk)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
