---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/flow/
title: Flows \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:43:17.416680+00:00
---

# Flows  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/flow/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Flows Stay organized with collections  Save and categorize content based on your preferences. 

Complex dialogs often involve multiple conversation topics. For example, a pizza delivery agent may have _food order_ , _customer information_ , and _confirmation_ as distinct topics. Each topic requires multiple conversational turns for an agent to acquire the relevant information from the end-user.

_Flows_ are used to define these topics and the associated conversational paths. Every agent has one flow called the [Default Start Flow](https://docs.cloud.google.com/dialogflow/cx/docs/concept/flow#start). This single flow may be all you need for a simple agent. More complicated agents may require additional flows, and different development team members can be responsible for building and maintaining these flows. For example, the flows of a pizza delivery agent may look like the following: 

![Example multi-flow diagram.](https://docs.cloud.google.com/static/dialogflow/cx/docs/images/cx-flow.svg)

## Default start flow

The **Default Start Flow** is automatically created when you initialize an agent. It can serve as the sole flow for simple agents or as the initial entry point for more complex agents that incorporate multiple flows.

**Note:** The **Default Start Flow** cannot be deleted.

When using the API, you can reference the default start flow with the following flow ID:
    
    
    00000000-0000-0000-0000-000000000000

## Flow's start page

Every flow includes a **Start** page, represented as a node in the console graph when the flow is selected. This page becomes the active page upon flow activation.

Unlike standard pages, a start page lacks parameters and response messages. You can still send a message using one of the following methods:

  * [Intent propagation](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#intent-prop)
  * Use a simple `true` [condition](https://docs.cloud.google.com/dialogflow/cx/docs/reference/condition) in a [route](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#route) that has a fulfillment response or a transition target to a normal page with entry fulfillment
  * [Custom events](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#event-custom)



### Reference a start page in API requests

To reference a flow's start page in runtime API requests, use `START_PAGE` as a page ID.

To make design-time changes to a start page through the API, use the `get` and `patch/update` API methods for the `Flow` type.

Go to the Flow API reference

**Select a protocol and version for the Flow reference:**

Protocol | V3 | V3beta1  
---|---|---  
REST |  [Flow resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows) |  [Flow resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.flows)  
RPC |  [Flow interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#google.cloud.dialogflow.cx.v3.Flows) |  [Flow interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3beta1#google.cloud.dialogflow.cx.v3beta1.Flows)  
C++ |  [FlowsClient](https://googleapis.dev/cpp/google-cloud-dialogflow_cx/latest/classgoogle_1_1cloud_1_1dialogflow__cx_1_1FlowsClient.html) |  Not available   
C# |  [FlowsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.FlowsClient) |  Not available   
Go |  [FlowsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3#cloud_google_com_go_dialogflow_cx_apiv3_FlowsClient) |  Not available   
Java |  [FlowsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.FlowsClient) |  [FlowsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.FlowsClient)  
Node.js |  [FlowsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3.FlowsClient.html) |  [FlowsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3beta1.FlowsClient.html)  
PHP |  Not available  |  Not available   
Python |  [FlowsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.services.flows.FlowsClient) |  [FlowsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3beta1.services.flows.FlowsClient)  
Ruby |  Not available  |  Not available   
  
Close

## Create a flow

To create a flow:

###  Console 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects).
  2. Select your project.
  3. Find the agent in the list.
  4. Click the add _add_ button in the **Flows** section.
  5. Select **Create flow**.
  6. Enter a display name for your flow.
  7. Click the flow you just created.



###  API 

See the `create` method for the `Flow` type. Go to the Flow API reference

**Select a protocol and version for the Flow reference:**

Protocol | V3 | V3beta1  
---|---|---  
REST |  [Flow resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows) |  [Flow resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.flows)  
RPC |  [Flow interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#google.cloud.dialogflow.cx.v3.Flows) |  [Flow interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3beta1#google.cloud.dialogflow.cx.v3beta1.Flows)  
C++ |  [FlowsClient](https://googleapis.dev/cpp/google-cloud-dialogflow_cx/latest/classgoogle_1_1cloud_1_1dialogflow__cx_1_1FlowsClient.html) |  Not available   
C# |  [FlowsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.FlowsClient) |  Not available   
Go |  [FlowsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3#cloud_google_com_go_dialogflow_cx_apiv3_FlowsClient) |  Not available   
Java |  [FlowsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.FlowsClient) |  [FlowsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.FlowsClient)  
Node.js |  [FlowsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3.FlowsClient.html) |  [FlowsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3beta1.FlowsClient.html)  
PHP |  Not available  |  Not available   
Python |  [FlowsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.services.flows.FlowsClient) |  [FlowsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3beta1.services.flows.FlowsClient)  
Ruby |  Not available  |  Not available   
  
Close

## Flow data

To access flow's data:

###  Console 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects).
  2. Select your project.
  3. Find the agent in the list.
  4. Click the agent display name.
  5. Click the flow in the **Flows** section.
  6. The flow's pages are populated in the **Pages** section. To learn how to edit a page, see the [Pages guide](https://docs.cloud.google.com/dialogflow/cx/docs/concept/page).
  7. Click the flow in the graph.
  8. A flow edit panel appears. Use this panel to browse and edit additional flow data.
  9. Click **Save** to save any changes.



###  API 

For flows, see the `get` and `patch/update` for the `Flow` type. Go to the Flow API reference

**Select a protocol and version for the Flow reference:**

Protocol | V3 | V3beta1  
---|---|---  
REST |  [Flow resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows) |  [Flow resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.flows)  
RPC |  [Flow interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#google.cloud.dialogflow.cx.v3.Flows) |  [Flow interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3beta1#google.cloud.dialogflow.cx.v3beta1.Flows)  
C++ |  [FlowsClient](https://googleapis.dev/cpp/google-cloud-dialogflow_cx/latest/classgoogle_1_1cloud_1_1dialogflow__cx_1_1FlowsClient.html) |  Not available   
C# |  [FlowsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.FlowsClient) |  Not available   
Go |  [FlowsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3#cloud_google_com_go_dialogflow_cx_apiv3_FlowsClient) |  Not available   
Java |  [FlowsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.FlowsClient) |  [FlowsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.FlowsClient)  
Node.js |  [FlowsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3.FlowsClient.html) |  [FlowsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3beta1.FlowsClient.html)  
PHP |  Not available  |  Not available   
Python |  [FlowsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.services.flows.FlowsClient) |  [FlowsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3beta1.services.flows.FlowsClient)  
Ruby |  Not available  |  Not available   
  
Close

For pages, see the `get` and `patch/update` methods for the `Page` type. Go to the Page API reference

**Select a protocol and version for the Page reference:**

Protocol | V3 | V3beta1  
---|---|---  
REST |  [Page resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.pages) |  [Page resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.flows.pages)  
RPC |  [Page interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#google.cloud.dialogflow.cx.v3.Pages) |  [Page interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3beta1#google.cloud.dialogflow.cx.v3beta1.Pages)  
C++ |  [PagesClient](https://googleapis.dev/cpp/google-cloud-dialogflow_cx/latest/classgoogle_1_1cloud_1_1dialogflow__cx_1_1PagesClient.html) |  Not available   
C# |  [PagesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.PagesClient) |  Not available   
Go |  [PagesClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3#cloud_google_com_go_dialogflow_cx_apiv3_PagesClient) |  Not available   
Java |  [PagesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.PagesClient) |  [PagesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.PagesClient)  
Node.js |  [PagesClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3.PagesClient.html) |  [PagesClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3beta1.PagesClient.html)  
PHP |  Not available  |  Not available   
Python |  [PagesClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.services.pages.PagesClient) |  [PagesClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3beta1.services.pages.PagesClient)  
Ruby |  Not available  |  Not available   
  
Close

The following data is associated with flows:

  * **[Pages](https://docs.cloud.google.com/dialogflow/cx/docs/concept/page):** Pages that make up the flow.
  * **[Routes](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#route):** Routes available when the flow's start page is active. Intent-based routes can also be triggered while other flow pages are active. For details, see [State handler scope](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#scope) and [Flow-level routes](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#route-flow).
  * **[Event handlers](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#event):** Handlers that may be called when the flow is active. For details, see [Flow-level event handlers](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#event-flow).



To learn more about how data is applied at varying levels, see the [Data application levels](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-level).

## Flow settings

The following settings are available for flows:

  * **Display name:** A human-readable name of the flow.
  * **Description:** A description of the flow.
  * **ML settings:** Flow ML settings are also accessed and described in [Agent ML settings](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-settings#settings-ml).
  * **Language auto detection:** Language auto detection lets you specify the end-user languages in which Dialogflow CX should automatically recognize and respond. For details, see [Multilingual agents](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-multilingual#lang-detect).
  * **Flow lock:** A locked flow cannot be edited, including the following changes to its child resources:

    1. [Pages](https://docs.cloud.google.com/dialogflow/cx/docs/concept/page) cannot be created, edited, or deleted.
    2. [Versions](https://docs.cloud.google.com/dialogflow/cx/docs/concept/version) cannot be created, edited, or deleted.
    3. [Flow-level route groups](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#route-group-flow) cannot be created, edited, or deleted.
    4. [Agent-level route groups](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#route-group-agent) referenced by a locked flow or any page under a locked flow cannot be deleted, but they can still be edited.
**Note:** This setting cannot be changed if the [lock is enabled at the agent level](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent#agent-lock).
  * **Advanced speech settings:** These [advanced speech settings](https://docs.cloud.google.com/dialogflow/cx/docs/concept/advanced-speech) can optionally override the same [agent speech settings](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-settings#settings-speech).

  * **Speech adaptation settings:** Flow level speech adaptation settings. To learn more, see the [Manual speech adaptation](https://docs.cloud.google.com/dialogflow/cx/docs/concept/speech-adaptation#manual-adaptation).

  * **Input parameters:** Parameters from the task playbook that are made available to the flow.

  * **Return parameters:** Parameters that the flow returns to a task playbook.




For more information about how data is applied at varying levels, see the [Data application levels](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-level).

To access flow settings:

###  Console 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects).
  2. Select your project.
  3. Find the agent in the list.
  4. Hold the pointer over the flow in the **Flows** section.
  5. Click the options _more_vert_ button.
  6. Select **Flow settings**.
  7. Browse or edit settings.
  8. Click **Save** to save any changes.



###  API 

See the `get` and `patch/update` methods for the `Flow` type. Go to the Flow API reference

**Select a protocol and version for the Flow reference:**

Protocol | V3 | V3beta1  
---|---|---  
REST |  [Flow resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows) |  [Flow resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.flows)  
RPC |  [Flow interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#google.cloud.dialogflow.cx.v3.Flows) |  [Flow interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3beta1#google.cloud.dialogflow.cx.v3beta1.Flows)  
C++ |  [FlowsClient](https://googleapis.dev/cpp/google-cloud-dialogflow_cx/latest/classgoogle_1_1cloud_1_1dialogflow__cx_1_1FlowsClient.html) |  Not available   
C# |  [FlowsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.FlowsClient) |  Not available   
Go |  [FlowsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3#cloud_google_com_go_dialogflow_cx_apiv3_FlowsClient) |  Not available   
Java |  [FlowsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.FlowsClient) |  [FlowsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.FlowsClient)  
Node.js |  [FlowsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3.FlowsClient.html) |  [FlowsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3beta1.FlowsClient.html)  
PHP |  Not available  |  Not available   
Python |  [FlowsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.services.flows.FlowsClient) |  [FlowsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3beta1.services.flows.FlowsClient)  
Ruby |  Not available  |  Not available   
  
Close

## Delete a flow

To delete a flow:

###  Console 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects).
  2. Select your project.
  3. Find the agent in the list.
  4. Hold the pointer over the flow in the **Flows** section.
  5. Click the settings _more_vert_ button.
  6. Select **Delete**.



###  API 

See the `delete` method for the `Flow` type. Go to the Flow API reference

**Select a protocol and version for the Flow reference:**

Protocol | V3 | V3beta1  
---|---|---  
REST |  [Flow resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows) |  [Flow resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.flows)  
RPC |  [Flow interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#google.cloud.dialogflow.cx.v3.Flows) |  [Flow interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3beta1#google.cloud.dialogflow.cx.v3beta1.Flows)  
C++ |  [FlowsClient](https://googleapis.dev/cpp/google-cloud-dialogflow_cx/latest/classgoogle_1_1cloud_1_1dialogflow__cx_1_1FlowsClient.html) |  Not available   
C# |  [FlowsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.FlowsClient) |  Not available   
Go |  [FlowsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3#cloud_google_com_go_dialogflow_cx_apiv3_FlowsClient) |  Not available   
Java |  [FlowsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.FlowsClient) |  [FlowsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.FlowsClient)  
Node.js |  [FlowsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3.FlowsClient.html) |  [FlowsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3beta1.FlowsClient.html)  
PHP |  Not available  |  Not available   
Python |  [FlowsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.services.flows.FlowsClient) |  [FlowsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3beta1.services.flows.FlowsClient)  
Ruby |  Not available  |  Not available   
  
Close

## Train a flow

To train a flow:

###  Console 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects).
  2. Select your project.
  3. Find the agent in the list.
  4. Click **Agent Settings**.
  5. Open the **ML** tab.
  6. To train a single flow, click **Train** in the corresponding row.
  7. To train multiple flows, select them with checkboxs, then click **Train selected flow NLU model**.



###  API 

See the `train` method for the `Flow` type. Go to the Flow API reference

**Select a protocol and version for the Flow reference:**

Protocol | V3 | V3beta1  
---|---|---  
REST |  [Flow resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows) |  [Flow resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.flows)  
RPC |  [Flow interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#google.cloud.dialogflow.cx.v3.Flows) |  [Flow interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3beta1#google.cloud.dialogflow.cx.v3beta1.Flows)  
C++ |  [FlowsClient](https://googleapis.dev/cpp/google-cloud-dialogflow_cx/latest/classgoogle_1_1cloud_1_1dialogflow__cx_1_1FlowsClient.html) |  Not available   
C# |  [FlowsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.FlowsClient) |  Not available   
Go |  [FlowsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3#cloud_google_com_go_dialogflow_cx_apiv3_FlowsClient) |  Not available   
Java |  [FlowsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.FlowsClient) |  [FlowsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.FlowsClient)  
Node.js |  [FlowsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3.FlowsClient.html) |  [FlowsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3beta1.FlowsClient.html)  
PHP |  Not available  |  Not available   
Python |  [FlowsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.services.flows.FlowsClient) |  [FlowsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3beta1.services.flows.FlowsClient)  
Ruby |  Not available  |  Not available   
  
Close

## Export a flow

You can export a flow in two ways:

  * **Data export:** This exports your flow as raw data for import into any agent. Resources referenced by the flow (intents, entities, and webhooks) are included in the export. Select the **raw data** format when following the steps below.
  * **Diagram export ([Preview](https://cloud.google.com/products/#product-launch-stages)):** This exports your flow as a visual diagram in draw.io XML format, which can be imported into tools like [Lucidchart](https://www.lucidchart.com/pages/draw.io-import) or [diagrams.net](https://www.diagrams.net/doc/faq/import-diagram). Select the **XML** data format when following the steps below.

**Note:** **Diagram export** is not available for agents using [CMEK](https://docs.cloud.google.com/dialogflow/cx/docs/concept/cmek).



You can export a flow with the following options:

  * **Include referenced flows:** Exports the target flow and all recursively referenced flows with no maximum depth. All exported flows and their transitions are preserved during import.



To export a flow:

###  Console 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects).
  2. Select your project.
  3. Find the agent in the list.
  4. Hold the pointer over the flow in the **Flows** section.
  5. Click the options _more_vert_ button.
  6. Select **Export flow**.
  7. Follow instructions to complete.



###  API 

See the `export` method for the `Flow` type. Go to the Flow API reference

**Select a protocol and version for the Flow reference:**

Protocol | V3 | V3beta1  
---|---|---  
REST |  [Flow resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows) |  [Flow resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.flows)  
RPC |  [Flow interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#google.cloud.dialogflow.cx.v3.Flows) |  [Flow interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3beta1#google.cloud.dialogflow.cx.v3beta1.Flows)  
C++ |  [FlowsClient](https://googleapis.dev/cpp/google-cloud-dialogflow_cx/latest/classgoogle_1_1cloud_1_1dialogflow__cx_1_1FlowsClient.html) |  Not available   
C# |  [FlowsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.FlowsClient) |  Not available   
Go |  [FlowsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3#cloud_google_com_go_dialogflow_cx_apiv3_FlowsClient) |  Not available   
Java |  [FlowsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.FlowsClient) |  [FlowsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.FlowsClient)  
Node.js |  [FlowsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3.FlowsClient.html) |  [FlowsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3beta1.FlowsClient.html)  
PHP |  Not available  |  Not available   
Python |  [FlowsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.services.flows.FlowsClient) |  [FlowsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3beta1.services.flows.FlowsClient)  
Ruby |  Not available  |  Not available   
  
Close

## Import a flow

Importing a flow from a source agent into a target agent also imports its referenced global resources, such as intents, entities, and webhooks. If the target agent has resources with the same display names, Dialogflow CX displays a summary and offers three options for resolving the conflicts:

  * **Replace existing resources:** Source agent resources will overwrite target agent resources.
  * **Import as new resources:** Source agent resources will be added with a distinctive suffix in the name.
  * **Keep original resources:** Target agent resources will be unchanged.



To import a flow:

###  Console 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects).
  2. Select your project.
  3. Find the agent in the list.
  4. Click the add _add_ button in the **Flows** section.
  5. Select **Import flow**.
  6. Follow instructions to complete.



###  API 

See the `import` method for the `Flow` type. Go to the Flow API reference

**Select a protocol and version for the Flow reference:**

Protocol | V3 | V3beta1  
---|---|---  
REST |  [Flow resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows) |  [Flow resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.flows)  
RPC |  [Flow interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#google.cloud.dialogflow.cx.v3.Flows) |  [Flow interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3beta1#google.cloud.dialogflow.cx.v3beta1.Flows)  
C++ |  [FlowsClient](https://googleapis.dev/cpp/google-cloud-dialogflow_cx/latest/classgoogle_1_1cloud_1_1dialogflow__cx_1_1FlowsClient.html) |  Not available   
C# |  [FlowsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.FlowsClient) |  Not available   
Go |  [FlowsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3#cloud_google_com_go_dialogflow_cx_apiv3_FlowsClient) |  Not available   
Java |  [FlowsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.FlowsClient) |  [FlowsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.FlowsClient)  
Node.js |  [FlowsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3.FlowsClient.html) |  [FlowsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3beta1.FlowsClient.html)  
PHP |  Not available  |  Not available   
Python |  [FlowsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.services.flows.FlowsClient) |  [FlowsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3beta1.services.flows.FlowsClient)  
Ruby |  Not available  |  Not available   
  
Close

[ Previous arrow_back  Flow-based agent basics  ](https://docs.cloud.google.com/dialogflow/cx/docs/basics)

[ Next Pages  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/page)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
