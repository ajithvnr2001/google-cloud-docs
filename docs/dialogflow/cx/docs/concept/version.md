---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/version/
title: Versions and environments \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:44:02.859670+00:00
---

# Versions and environments  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/version/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Versions and environments Stay organized with collections  Save and categorize content based on your preferences. 

You can create multiple versions of your agent flows, [playbooks](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook) and tools and deploy them to separate serving environments.

When you edit a flow, playbook or tool, you are editing the _draft_. At any point, you can save the draft as a _version_. A version is an immutable snapshot of your flow, playbook or tool data and associated agent data. For flows, this includes intents, entities, webhooks, pages, route groups. For playbooks, this includes only examples.

When you save a draft, it is deployed to the _default environment_. When you create specific versions, you can deploy them to _custom environments_. You can create a variety of custom environments such as:

  * testing
  * development
  * production



In addition, you can create [environment-specific webhooks](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook#environment-specific), so that you can isolate your production environment from development and testing environments.

## Production traffic best practices

### Always use versions for production traffic

A draft is updated every time a developer on your team makes a change. It is possible to break a draft unintentionally, especially if multiple people have write access to the agent. In addition, a recently edited draft may be inconsistent with the trained model, because training may have a delay or require manual execution.

You should always use versions for your production traffic. Draft resources should be tested before promoting them to production versions, and you can rollback to a previous version if any problems are discovered.

### Always use environment-specific webhooks

When making updates to your agent, you often have interdependent updates to your webhook code. During development and testing of these changes, you want the following:

  * To test the agent updates against the webhook code updates.
  * To avoid deploying your webhook code to production until you have completed testing.



Using [environment-specific webhooks](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook#environment-specific) achieves both of these goals.

### Consider possible agent errors while changing versions

If you change a version in your production environment while sessions are active, it may cause agent errors for some active sessions. These errors may happen if the previous and new versions are inconsistent with each other in a way that disrupts session state. Due to this, you should plan to change versions during down-time or off-peak hours.

## Load a version to draft

At any time, you can load a version to draft, so it is editable and used by the default environment.

Loading a flow version to draft can update multiple resources in an agent, including agent-level resources like intents and entities. When loading a version to draft with either the console or API, you can choose whether agent-level resources will be overwritten.

Similarly, restoring a playbook version to draft will overwrite the existing playbook in draft and its examples. And restoring a tool will overwrite the existing tool in draft.

## Manage versions

To manage your versions:

###  Console 

To list the current versions for a flow:

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects).
  2. Choose your Google Cloud project.
  3. Select your agent.
  4. Click the **Shared Resources** tab.
  5. Click **Versions**.
  6. The agent flows are listed. Select one.
  7. The versions are listed for the selected flow.



To list the current versions for a playbook:

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects).
  2. Choose your Google Cloud project.
  3. Select your agent.
  4. Select the playbook
  5. Click **Version History**.
  6. Click **View version history**.
  7. The versions are listed for the selected playbook.



To list the current versions for a tool:

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects).
  2. Choose your Google Cloud project.
  3. Select your agent.
  4. Select the tool
  5. Click **Version History**.
  6. Click **View version history**.
  7. The versions are listed for the selected tool.



The following information is displayed for each resource:

  * **Display name** : The version display name.
  * **Version ID** : The ID for the version.
  * **NLU Type** : The [NLU type](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-settings#settings-ml) for the flow version.
  * **Creation timestamp** : The date and time that the version was created.
  * **Status** : The training status. A flow version is not ready to use until the status is marked as **Ready**.



To create a new version, click the **Create** button and provide the **Display name** and **Description** for the version.

To load a specific flow version as the draft flow:

  1. Hold the pointer over a version row.
  2. Click the option _more_vert_ button.
  3. Click the **Load to draft** option.
  4. An option is provided to overwrite agent-level data when loading.



To delete a specific flow version:

  1. Hold the pointer over a version row.
  2. Click the option _more_vert_ button.
  3. Click the **Delete version** option.



###  API 

See the methods for the `Version` type. Go to the Version API reference

**Select a protocol and version for the Version reference:**

Protocol | V3 | V3beta1  
---|---|---  
REST |  [Version resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.versions) |  [Version resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.flows.versions)  
RPC |  [Version interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#versions) |  [Version interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3beta1#versions)  
C++ |  [VersionsClient](https://googleapis.dev/cpp/google-cloud-dialogflow_cx/latest/classgoogle_1_1cloud_1_1dialogflow__cx_1_1VersionsClient.html) |  Not available   
C# |  [VersionsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.VersionsClient) |  Not available   
Go |  [VersionsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3#cloud_google_com_go_dialogflow_cx_apiv3_VersionsClient) |  Not available   
Java |  [VersionsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.VersionsClient) |  [VersionsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.VersionsClient)  
Node.js |  [VersionsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3.VersionsClient.html) |  [VersionsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3beta1.VersionsClient.html)  
PHP |  Not available  |  Not available   
Python |  [VersionsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.services.versions.VersionsClient) |  [VersionsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3beta1.services.versions.VersionsClient)  
Ruby |  Not available  |  Not available   
  
Close

**Note:** The `load` method has a `allowOverrideAgentResources` field, which can be used to control whether agent level resources are overwritten when restoring a flow as the draft flow.**Note:** When calling the `delete` method to delete a version, you must first remove all references to the version in environments data.

## Compare flow versions

**Note:** **Compare versions** is limited by 2MB response size. Use [REST API method](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.versions/compareVersions) to overcome this limitation.

Once you have created flow versions, you can use the **compare versions** tool to see a side-by-side comparison between flow versions or the draft version. This features is not available for playbooks. To compare versions:

###  Console 

  1. Hold the pointer over a version row.
  2. Click the option _more_vert_ button.
  3. Click the **Compare versions** option.
  4. Select another flow version or draft flow for comparison.
  5. A side-by-side comparison is shown.



###  API 

See the `compareVersions` method for the `Version` type. Go to the Version API reference

**Select a protocol and version for the Version reference:**

Protocol | V3 | V3beta1  
---|---|---  
REST |  [Version resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.versions) |  [Version resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.flows.versions)  
RPC |  [Version interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#versions) |  [Version interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3beta1#versions)  
C++ |  [VersionsClient](https://googleapis.dev/cpp/google-cloud-dialogflow_cx/latest/classgoogle_1_1cloud_1_1dialogflow__cx_1_1VersionsClient.html) |  Not available   
C# |  [VersionsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.VersionsClient) |  Not available   
Go |  [VersionsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3#cloud_google_com_go_dialogflow_cx_apiv3_VersionsClient) |  Not available   
Java |  [VersionsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.VersionsClient) |  [VersionsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.VersionsClient)  
Node.js |  [VersionsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3.VersionsClient.html) |  [VersionsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3beta1.VersionsClient.html)  
PHP |  Not available  |  Not available   
Python |  [VersionsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.services.versions.VersionsClient) |  [VersionsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3beta1.services.versions.VersionsClient)  
Ruby |  Not available  |  Not available   
  
Close

## Manage environments

To manage your agent environments:

###  Console 

To list the current environments for an agent:

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects).
  2. Choose your Google Cloud project.
  3. Select your agent.
  4. Click the **Shared Resources** tab.
  5. Click **Environments**.
  6. The agent environments are listed.



To create a new environment, click the **Create** button and provide information.

To select flow, playbook and tool versions and configure an environment, click an environment and provide information.

To view editing history of an environment, click the history _history_ button near the right side of an environment in the list.

To copy an environment resource name that includes the environment ID, click the copy _content_copy_ button near the right side of an environment in the list.

To delete an environment, click the delete _delete_ button near the right side of an environment in the list.

###  API 

See the methods for the `Environment` type. Go to the Environment API reference

**Select a protocol and version for the Environment reference:**

Protocol | V3 | V3beta1  
---|---|---  
REST |  [Environment resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments) |  [Environment resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.environments)  
RPC |  [Environment interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#environments) |  [Environment interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3beta1#environments)  
C++ |  [EnvironmentsClient](https://googleapis.dev/cpp/google-cloud-dialogflow_cx/latest/classgoogle_1_1cloud_1_1dialogflow__cx_1_1EnvironmentsClient.html) |  Not available   
C# |  [EnvironmentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EnvironmentsClient) |  Not available   
Go |  [EnvironmentsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3#cloud_google_com_go_dialogflow_cx_apiv3_EnvironmentsClient) |  Not available   
Java |  [EnvironmentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.EnvironmentsClient) |  [EnvironmentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.EnvironmentsClient)  
Node.js |  [EnvironmentsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3.EnvironmentsClient.html) |  [EnvironmentsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3beta1.EnvironmentsClient.html)  
PHP |  Not available  |  Not available   
Python |  [EnvironmentsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.services.environments.EnvironmentsClient) |  [EnvironmentsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3beta1.services.environments.EnvironmentsClient)  
Ruby |  Not available  |  Not available   
  
Close

**Note:** To reference a draft flow, use `0` as the flow version ID.

## Specify environment for session calls

Using either the [console simulator](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console#simulator) or the API, you can specify an environment when making runtime session calls. If an environment is not specified, the default environment is used.

###  Console 

When using the console simulator, select the **Test agent in environment** option, then select an environment.

###  API 

To specify an environment for `detectIntent`, `streamingDetectIntent`, `matchIntent`, and session entity REST calls; alter the URL by inserting `environments/environment-id` between the `agent` and `sessions` path parameters.

For example, the following URL uses the `6db409d7-57ac-41d7-83bd-89b8768e2745` environment ID:
    
    
    https://dialogflow.googleapis.com/v3/projects/my-project-id/locations/us/agents/my-agent-id/environments/6db409d7-57ac-41d7-83bd-89b8768e2745/sessions/my-session-id:detectIntent
    

## Specify flow versions for session calls

Using either the [console simulator](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console#simulator) or the API, you can specify a set of flow versions when making runtime session calls. The selected flow versions don't necessarily need to be referenced in any environment.

###  Console 

When using the console simulator, select the **Test agent with specific flow versions** option, then select flow versions.

###  API 

To specify flow versions for `detectIntent`, `streamingDetectIntent`, `matchIntent`, and session entity REST calls; provide the chosen flow versions in the `query_parameters.flow_versions` field of the request.

[ Previous arrow_back  Using multiple projects  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/multi-project)

[ Next Data application levels  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-level)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
