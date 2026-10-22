---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent/
title: Agents \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:56:01.084098+00:00
---

# Agents  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Agents Stay organized with collections  Save and categorize content based on your preferences. 

A _Dialogflow CX agent_ is a virtual agent that handles concurrent conversations with your end-users. It is a natural language understanding module that understands the nuances of human language. Dialogflow CX translates end-user text or audio during a conversation to structured data that your apps and services can understand. You design and build a Dialogflow CX agent to handle the types of conversations required for your system.

A Dialogflow CX agent is similar to a human call center agent. You train them both to handle expected conversation scenarios, and your training does not need to be overly explicit.

## Create an agent

**Note:** You can create multiple Dialogflow CX agents for one [Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).

To create an agent:

###  Console 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects).
  2. Create or choose a project.
  3. Click **Create agent**.
  4. Select **Auto-generate** to create a [data store agent](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store-agent) or select **Build your own** to create other kinds of agents.
  5. Complete the form for basic agent settings: 
     1. You can choose any display name.
     2. Select your preferred [location](https://docs.cloud.google.com/dialogflow/cx/docs/how/region#avail). If you want to change advanced [location settings](https://docs.cloud.google.com/dialogflow/cx/docs/how/region#location-settings), click the **Edit** button.
     3. Select your preferred time zone.
     4. Select the default language for your agent. You cannot change the default language for an agent once it is created.
  6. Click **Save**.



###  API 

If you have not already configured [location settings](https://docs.cloud.google.com/dialogflow/cx/docs/concept/region#location-settings) for your project, you must configure these settings with the console before creating agents with the API. You cannot configure location settings with the API.

To create an agent, see the `create` method for the `Agent` type. Go to the Agent API reference

**Select a protocol and version for the Agent reference:**

Protocol | V3 | V3beta1  
---|---|---  
REST |  [Agent resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents) |  [Agent resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents)  
RPC |  [Agent interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#google.cloud.dialogflow.cx.v3.Agents) |  [Agent interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3beta1#google.cloud.dialogflow.cx.v3beta1.Agents)  
C++ |  [AgentsClient](https://googleapis.dev/cpp/google-cloud-dialogflow_cx/latest/classgoogle_1_1cloud_1_1dialogflow__cx_1_1AgentsClient.html) |  Not available   
C# |  [AgentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentsClient) |  Not available   
Go |  [AgentsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3#cloud_google_com_go_dialogflow_cx_apiv3_AgentsClient) |  Not available   
Java |  [AgentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AgentsClient) |  [AgentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.AgentsClient)  
Node.js |  [AgentsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3.AgentsClient.html) |  [AgentsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3beta1.AgentsClient.html)  
PHP |  Not available  |  Not available   
Python |  [AgentsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.services.agents.AgentsClient) |  [AgentsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3beta1.services.agents.AgentsClient)  
Ruby |  Not available  |  Not available   
  
Close

## Agent data

Dialogflow CX agents serve as top-level containers for settings and data for virtual agents. The following data is associated with agents:

  * [Intents](https://docs.cloud.google.com/dialogflow/cx/docs/concept/intent)
  * [Entity types](https://docs.cloud.google.com/dialogflow/cx/docs/concept/entity)
  * [Webhooks](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook)
  * [Flows](https://docs.cloud.google.com/dialogflow/cx/docs/concept/flow)
  * [Pages](https://docs.cloud.google.com/dialogflow/cx/docs/concept/page)
  * [Route groups](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#group)



For more information about how data is applied at varying levels, see the [data application levels](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-level).

## Smart endpointing

Speech-to-Text (STT) is an API that converts audio to text using machine learning, enabling you to integrate speech recognition into your applications. Supported STT models include any long-form model (for example, `phone_call`). Only the `en-US` language is supported.

**Note:** If using a short model, this enables the cloud speech endpointing.

If smart endpointing is enabled for the agent, you can customize smart endpointing behavior for a numeric parameter by setting **Waiting timeout** to specify the additional time. Dialogflow CX will then wait for the user to provide additional input.

The waiting timeout is a grace period letting you add something to STT transcript before the speech timeout is triggered. Dialogflow CX uses heuristics to specify what timeout needs to be chosen based on the transcript. For example, it can choose very short timeout if the intent was matched successfully. If intent was not matched, it can increase timeout to let you say something else, and retry intent matching.

Other STT features include:

  * **Faster Endpointing:** Real-time analysis uses Audio Transcription Streaming to distinguish between a natural pause and the completion of an utterance while the STT stream remains open. If the user has finished speaking, Dialogflow CX terminates the stream early to deliver a faster response.
  * **Natural Conversational Feedback:** If the user pauses mid-utterance, Dialogflow CX can dynamically extend the STT timeout to prevent premature interruptions or inject natural backchanneling cues (e.g., "mm hmm," "uh huh") to confirm the virtual agent is still listening.



## Export and restore an agent

**Warning:** We will no longer export raw value credentials for OpenAPI Tools and Webhooks, starting Aug 15, 2025. You should migrate to store your credentials in Secret Manager. For instructions, see [Webhook](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook#secret-manager-auth) and [Tool](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/tool#secret-manager-auth) documentations.

You can export an agent to a file, and restore an agent with that file.

An agent export includes all agent data except the following:

  * [Flow versions](https://docs.cloud.google.com/dialogflow/cx/docs/concept/version): Only the flow versions used in the selected environment are exported to a file.
  * [Environments](https://docs.cloud.google.com/dialogflow/cx/docs/concept/version): Environments other than the selected environment are not exported to a file.



An agent restore overwrites all target agent data (including all flow versions) except the following:

  * [Environments](https://docs.cloud.google.com/dialogflow/cx/docs/concept/version): All custom environments remain unchanged in the target agent. Flow versions referenced by custom environments in the target agent will continue to exist as long as the associated environments exist. However, these stale flow versions are not listed or selectable flow versions for the agent.
  * [Vertex AI Agents Apps](https://docs.cloud.google.com/generative-ai-app-builder/docs/agent-intro): The association to a Vertex AI Agents App remains unchanged in the target agent (i.e., the value of `engine` in [GenAppBuilderSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents#GenAppBuilderSettings)). This means that data store agents can only be restored into other existing data store agents because the resulting agent also needs to have an association to a Vertex AI Agents App.
  * [Vertex AI Agents Data Stores](https://docs.cloud.google.com/generative-ai-app-builder/docs/agent-usage): All references to data stores will be overwritten in the target agent, according to the following rules:

    * If the target agent isn't associated with an App, then it's not possible to restore an agent with data store references into it. Trying to do so results in an error message. To fix that, you can either [create a new data store agent](https://docs.cloud.google.com/generative-ai-app-builder/docs/agent-usage#create_a_data_store_agent) from scratch. (Alternatively, you can turn your existing agent into a data store agent by adding a data store [state handler](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler) to it. In this case, you'll be guided through adding an associated App to your agent.)
    * If the target agent is associated with an App, then all the data store references will be updated upon restore: their Google Cloud project ID and location will be updated to match the App of the target agent. The collection ID and data store ID will remain unchanged. This means that you need to add data stores for all the IDs with matching types into the App of the target agent prior to the restore operation.

Example: If the source agent refers to a data store named `projects/123/locations/eu-west2/collections/default_collection/dataStores/myDataStore1` and the App of the target agent is named `projects/321/locations/us-east1/collections/default_collections/engines/app123`, then the resulting data store reference in the target agent becomes: `projects/321/locations/us-east1/collections/default_collection/dataStores/myDataStore1`


**Note:** In the API and in the contents of the exported data, a Vertex AI Agents App is called a GenAppBuilder Engine. For example, in an exported JSON package, you can find the name of the engine in the `agent.json` file, under the key `genAppBuilderSettings.engine`.

When exporting, you can select the export file format. If you're using source control versioning for your agent data, you should [export in the JSON format](https://docs.cloud.google.com/dialogflow/cx/docs/reference/json-export). When you restore an agent, Dialogflow CX automatically determines the file format.

To export or restore an agent:

###  Console 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects).
  2. Choose the project for the agent.
  3. Select the menu option _more_vert_ for an agent in the list.
  4. Click **Export** or **Restore** button.
  5. Follow instructions to complete.



**Note:** To restore a data store agent, make sure that the target agent was created as a [data store agent](https://docs.cloud.google.com/generative-ai-app-builder/docs/agent-usage#create_a_data_store_agent).

###  API 

See the `export` and `restore` methods for the `Agent` type. Go to the Agent API reference

**Select a protocol and version for the Agent reference:**

Protocol | V3 | V3beta1  
---|---|---  
REST |  [Agent resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents) |  [Agent resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents)  
RPC |  [Agent interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#google.cloud.dialogflow.cx.v3.Agents) |  [Agent interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3beta1#google.cloud.dialogflow.cx.v3beta1.Agents)  
C++ |  [AgentsClient](https://googleapis.dev/cpp/google-cloud-dialogflow_cx/latest/classgoogle_1_1cloud_1_1dialogflow__cx_1_1AgentsClient.html) |  Not available   
C# |  [AgentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentsClient) |  Not available   
Go |  [AgentsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3#cloud_google_com_go_dialogflow_cx_apiv3_AgentsClient) |  Not available   
Java |  [AgentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AgentsClient) |  [AgentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.AgentsClient)  
Node.js |  [AgentsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3.AgentsClient.html) |  [AgentsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3beta1.AgentsClient.html)  
PHP |  Not available  |  Not available   
Python |  [AgentsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.services.agents.AgentsClient) |  [AgentsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3beta1.services.agents.AgentsClient)  
Ruby |  Not available  |  Not available   
  
Close

If the agent size exceeds the [maximum limit](https://docs.cloud.google.com/dialogflow/quotas#size), use the Cloud Storage option for agent export and restore.

If you use GitHub, also see the [GitHub export/restore guide](https://docs.cloud.google.com/dialogflow/cx/docs/concept/github).

## Delete an agent

**Caution:** Deleting an agent **cannot** be undone. Export your agent to keep a backup if necessary.

In order to delete an agent, you need a role that provides full access or edit access. For more information, see the [Access control guide](https://docs.cloud.google.com/dialogflow/cx/docs/concept/access-control).

To delete an agent:

###  Console 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects).
  2. Choose the project for the agent.
  3. Select the menu option _more_vert_ for an agent in the list.
  4. Click the button _delete_.
  5. Confirm deletion in the dialog.



###  API 

See the `delete` method for the `Agent` type. Go to the Agent API reference

**Select a protocol and version for the Agent reference:**

Protocol | V3 | V3beta1  
---|---|---  
REST |  [Agent resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents) |  [Agent resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents)  
RPC |  [Agent interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#google.cloud.dialogflow.cx.v3.Agents) |  [Agent interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3beta1#google.cloud.dialogflow.cx.v3beta1.Agents)  
C++ |  [AgentsClient](https://googleapis.dev/cpp/google-cloud-dialogflow_cx/latest/classgoogle_1_1cloud_1_1dialogflow__cx_1_1AgentsClient.html) |  Not available   
C# |  [AgentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentsClient) |  Not available   
Go |  [AgentsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3#cloud_google_com_go_dialogflow_cx_apiv3_AgentsClient) |  Not available   
Java |  [AgentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AgentsClient) |  [AgentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.AgentsClient)  
Node.js |  [AgentsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3.AgentsClient.html) |  [AgentsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3beta1.AgentsClient.html)  
PHP |  Not available  |  Not available   
Python |  [AgentsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.services.agents.AgentsClient) |  [AgentsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3beta1.services.agents.AgentsClient)  
Ruby |  Not available  |  Not available   
  
Close

If you [delete your project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#shutting_down_projects), all Dialogflow CX agents and data associated with the project are deleted immediately.

[ Previous arrow_back  Dialogflow CX console overview  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console)

[ Next Overview  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/prebuilt)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
