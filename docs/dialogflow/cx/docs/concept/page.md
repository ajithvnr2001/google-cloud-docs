---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/page/
title: Pages \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:56:10.521784+00:00
---

# Pages  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/page/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Pages Stay organized with collections  Save and categorize content based on your preferences. 

A Dialogflow CX conversation (session) can be described and visualized as a [state machine](https://en.wikipedia.org/wiki/Finite-state_machine). The states of a session are represented by _pages_. 

For each [flow](https://docs.cloud.google.com/dialogflow/cx/docs/concept/flow), you define many pages, where your combined pages can handle a complete conversation on the topics the flow is designed for. At any given moment, exactly one page is the _current page_ , the current page is considered _active_ , and the flow associated with that page is considered _active_. Every flow has a special [start page](https://docs.cloud.google.com/dialogflow/cx/docs/concept/flow#start-page). When a flow initially becomes active, the start page becomes the current page. For each conversational turn, the current page will either stay the same or transition to another page.

You configure each page to collect information from the end-user that is relevant for the conversational state represented by the page. For example, you might create the pages (in blue) in the diagram below for a _Food Order_ flow of a pizza delivery agent. The _Start_ node of the diagram represents the start page of the _Food Order_ flow. When the flow is complete, it transitions to the _Confirmation_ flow.

![Example multi-flow diagram.](https://docs.cloud.google.com/static/dialogflow/cx/docs/images/cx-page.svg)

## Lifecycle of a page

Once a page becomes active, the agent follows several steps which may involve entry fulfillment, prefilling forms, state handler evaluation, form parameter prompting, sending response messages to the end-user, and either a page change or a repeat loop:

![Page lifecycle diagram.](https://docs.cloud.google.com/static/dialogflow/cx/docs/images/cx-page-lifecycle.svg)

The details of this process are as follows:

  1. If entry [fulfillment](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment) exists for the page, it is called. Any static responses provided by fulfillment are added to the [response queue](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#queue).

If [partial response](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#partial-response) is enabled, Dialogflow CX flushes the _response queue_ and sends all queued messages as a partial response to the streaming API caller.

If the fulfillment has a webhook, the webhook is called, which may append additional responses to the queue. These additional responses do not trigger an immediate flush of the _response queue_.

  2. If the page has form parameters, they may be pre-filled:

     * Any set [session parameter](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter#session) with the same name as a [form parameter](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter#form) is copied to the form parameter.
     * If a [route](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#route) triggered a transition to this page, and the route contains a matched [intent](https://docs.cloud.google.com/dialogflow/cx/docs/concept/intent), any intent parameter with the same name as a [form parameter](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter#form) is copied to the form parameter.
  3. If any state handlers are [in scope](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#scope), they are evaluated according to the [handler evaluation order rules](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#eval). This can involve routes, event handlers, or reprompt handlers invoked from the prior loop iteration. If any state handler is called, one or both of the following may happen:

     * If fulfillment exists for the handler, it is called. Any static responses provided by fulfillment are added to the [response queue](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#queue). Partial response and webhook are also executed if they are enabled.
     * If a target flow or page exists for the handler, the session transitions to the target and the page becomes inactive.
  4. If all of the following are true, a form parameter prompt is added to the response queue:

     * The page has a form.
     * There are required form parameters left to fill.
     * A [reprompt handler](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter#reprompt) was not followed in step 3.
     * Partial response and webhook are executed if they are enabled.
  5. The remaining response queue messages are sent to the end-user, and the agent waits for end-user input.

  6. If end-user input provides a prompted form parameter, fill the parameter. Continue to step 3.




## Page lifecycle navigation

The [simulator](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console#simulator) execution steps viewer allows you to switch between the steps for a specific conversation turn and brings the related agent builder elements into focus for each step. In the following example, end-user input "I would like to rent a car" triggers five execution and transition steps:

  1. The executions steps viewer brings you to conversation starting page for the first step. In this case it's the default start page. ![Page execution step 1.](https://docs.cloud.google.com/static/dialogflow/cx/docs/images/execution_step1.png)

  2. Transition route for the intent `car_rental.reservation_create` is triggered. The executions steps viewer brings this route to focus, where you can see that the transition target is the `Pickup Location` page. ![Page execution step 2.](https://docs.cloud.google.com/static/dialogflow/cx/docs/images/execution_step2.png)

  3. Agent enters page `Pickup Location`. ![Page execution step 3.](https://docs.cloud.google.com/static/dialogflow/cx/docs/images/execution_step3.png)

  4. Agent evaluates the entry fulfillment of `Pickup Location` page. The fulfillment is empty, so nothing happens. ![Page execution step 4.](https://docs.cloud.google.com/static/dialogflow/cx/docs/images/execution_step4.png)

  5. Agent tries to collect the required form parameter `pickup_location` and the initial prompt fulfillment message for this parameter is shown to the end-user. ![Page execution step 5.](https://docs.cloud.google.com/static/dialogflow/cx/docs/images/execution_step5.png)




You can also undo the last utterance and try something else to test different page transitions.

![Undo utterance.](https://docs.cloud.google.com/static/dialogflow/cx/docs/images/simulator_undo.png)

## Create a page

**Note:** A page will not appear on the console graph until transitions have been created with a target set to the page.

To create a page:

###  Console 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects).
  2. Choose your Google Cloud project.
  3. Select your agent.
  4. Select a flow for the page in the **Flows** section.
  5. Click the add _add_ button in the **Pages** section.
  6. Enter a display name for your page.
  7. Click the settings _more_vert_ button next to the page display name.
  8. Select **Edit**.
  9. Enter the fields in the page edit panel that appears.
  10. Click **Save**.



###  API 

See the `create` method for the `Page` type. Go to the Page API reference

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

## Page data

To access a page's data:

###  Console 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects).
  2. Choose the Google Cloud project for the agent.
  3. Select your agent.
  4. Click the flow in the **Flows** section.
  5. The flow's pages are populated in the **Pages** section.
  6. Click the settings _more_vert_ button next to the page display name.
  7. Select **Edit**.
  8. Enter the fields in the page edit panel that appears.
  9. Click **Save** to save any changes.



###  API 

See the `get` and `patch/update` methods for the `Page` type. Go to the Page API reference

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

The following data is associated with pages:

  * **Display name** : A human-readable name for your page.
  * **Entry fulfillment** (also known as **Entry dialogue**): This is the [fulfillment](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment) to call when the page initially becomes active.
  * **Parameters** : These are the parameter values in a page [form](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter#form) that capture structured input from the end-user.
  * **Routes** : These state handlers may be called when the page is active. For details, see [Page-level handler routes](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#route-page)
  * **Route groups** : The routes within these groups may be called when the page is active. For details, see [Route groups](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#route-group)
  * **Event handlers** : These event handlers may be called when the page is active. For details, see [Page-level event handlers](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#event-page)



## Page settings

The following settings are available for pages:

  * **Advanced speech settings** : These [advanced speech settings](https://docs.cloud.google.com/dialogflow/cx/docs/concept/advanced-speech) can optionally override the same [flow speech settings](https://docs.cloud.google.com/dialogflow/cx/docs/concept/flow#settings) and [agent speech settings](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-settings#settings-speech).

  * **Speech adaptation settings** : Page level speech adaptation settings can optionally override the same [flow speech adaptation settings](https://docs.cloud.google.com/dialogflow/cx/docs/concept/flow#settings). More detailed instructions in [manual speech adaptation](https://docs.cloud.google.com/dialogflow/cx/docs/concept/speech-adaptation#manual-adaptation).




To access page settings:

###  Console 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects).
  2. Choose your Google Cloud project.
  3. Select your agent.
  4. Hover your mouse over the page in the **Pages** section.
  5. Click the options _more_vert_ button.
  6. Select **Page settings**.
  7. Browse or edit settings.
  8. Click **Save** to save any changes.



###  API 

See the `get` and `patch/update` methods for the `Page` type. Go to the Page API reference

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

## Delete a page

To delete a page:

###  Console 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects).
  2. Choose your Google Cloud project.
  3. Select your agent.
  4. Select the flow for the page in the **Flows** section.
  5. Click the settings _more_vert_ button next to the page display name in the **Pages** section.
  6. Select **Delete**.



###  API 

See the `delete` method for the `Page` type. Go to the Page API reference

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

[ Previous arrow_back  Flows  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/flow)

[ Next State handlers  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
