---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler/
title: State handlers \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:44:10.099674+00:00
---

# State handlers  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  State handlers Stay organized with collections  Save and categorize content based on your preferences. 

_State handlers_ , also simply called _handlers_ , are used to control the conversation by creating responses for end-users and/or by transitioning the current page. For each conversational turn, handlers are evaluated and may affect the session. Handlers have three general types of data: Term | Definition  
---|---  
Handler requirements  | These are the requirements that must be satisfied for the handler to have any effect on the session. A handler is said to be _called_ when it satisfies its requirements and affects the session in some way.  
Handler fulfillment  | If a handler is called, an optional [fulfillment](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment) is used to create responses for end-users. These responses are either defined in static agent data or retrieved dynamically from your [webhook service](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook).  
Handler transition target  | If a handler is called, an optional transition target is used to change the current page. The next page can only be a [flow start page](https://docs.cloud.google.com/dialogflow/cx/docs/concept/flow#start-page) or a page within the currently active flow.  
  
There are two types of state handlers with differing handler requirements:

Term | Definition  
---|---  
Routes  | [Routes](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#route) are called when an end-user input matches an [intent](https://docs.cloud.google.com/dialogflow/cx/docs/concept/intent) and/or some [condition](https://docs.cloud.google.com/dialogflow/cx/docs/reference/condition) on the session status is met. A route with an intent requirement is also called an _intent route_. A route with only a condition requirement is also called a _condition route_.  
Event handlers  | [Event handlers](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#event) are called when an _event_ is invoked. Some [built-in events](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#event-built-in) are triggered when unexpected end-user input is received, or when a webhook error occurs. You can also define [custom events](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#event-custom) that you invoke when something happens outside the conversation.  
  
There are three steps to processing a state handler:

Term | Definition  
---|---  
1\. Scope | A handler must be in [scope](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#scope) to have any effect on the session. The scope is determined by whether a handler is applied to a flow, a page, or a form parameter; and by whether the associated flow is active, the associated page is active, or the agent is currently attempting to fill the associated form parameter.  
2\. Evaluation | Each handler in scope is [evaluated in order](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#eval). If a handler's requirements are met, it passes evaluation.  
3\. Call | If a handler is in scope and passes evaluation, it is called. Any associated fulfillment is called, and any associated transition target is applied to the session.  
  
## Scope

In order for a handler to be evaluated, it must be in _scope_. Handler scope is an important and powerful tool that helps you control the conversation. By controlling the scope of a handler, you can control:

X | Item  
---|---  
double_arrow | When an intent can be matched  
double_arrow | When a condition should be checked  
double_arrow | When a certain event can be handled  
double_arrow | When a page transition can occur  
double_arrow | When a static fulfillment response is provided  
double_arrow | When a webhook-enabled fulfillment is called for dynamic responses  
  
The scope is determined by whether a handler is applied to a flow, a page, or a form parameter; and by whether the associated flow is active, the associated page is active, or the agent is currently attempting to fill the associated form parameter.

The detailed scoping rules are as follows:

  * Routes applied to the active flow: 
    * If the current page is the [flow start page](https://docs.cloud.google.com/dialogflow/cx/docs/concept/flow#start-page), they are in scope.
    * If the current page is not the flow start page, they are only in scope if they have an intent requirement.
  * Routes applied to the current page are in scope.
  * Event handlers applied to the active flow are in scope.
  * Event handlers applied to the current page are in scope.
  * Event handlers applied to a form parameter that the agent is currently attempting to fill are in scope.



## Routes

Routes have two requirements, and one or both must be provided. If both requirements are provided, they both must be satisfied in order to call the route:

Term | Definition  
---|---  
Intent requirement  | An [intent](https://docs.cloud.google.com/dialogflow/cx/docs/concept/intent) which must be matched to end-user input for the current conversational turn. When a route has an intent requirement, it is called an _intent route_.  
Condition requirement  | A [condition](https://docs.cloud.google.com/dialogflow/cx/docs/reference/condition) which must be met. When a route has a condition requirement, it is called a _condition route_.  
  
You can apply routes to flows (_flow-level routes_) and pages (_page-level routes_). For example, you might use routes in the following situations:

X | Item  
---|---  
double_arrow | When end-user input matches an intent, the match should trigger a [static fulfillment](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#static) response.  
double_arrow | When end-user input matches an intent, the match should trigger a [webhook-enabled fulfillment](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#webhook) for a dynamic response.  
double_arrow | When end-user input has provided the final required [form parameter](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter#form) a condition check triggers a session transition to another page.  
double_arrow | When end-user input has provided a specific [form parameter](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter#form) a condition check triggers a [static fulfillment](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#static) response.  
double_arrow | A condition check set to `true` that forces a page transition.  
  
### Intent propagation

Normally, when a route is called due to a matched intent, the intent is _consumed_. A consumed intent cannot be matched again, unless new end-user input triggers a new intent match. However, it is possible to propagate an intent match from one flow to another in the following scenario:

  * A route in `flow F1` has `intent I1` as a requirement and `flow F2` as a transition target.
  * `Flow F2` has a route that also has `intent I1` as a requirement.



In this case, when the route in `flow F1` is called, `intent I1` is matched twice for a single end-user input, and both routes are called.

Propagating intents is useful to:

X | Item  
---|---  
double_arrow | Change the current page to a specific page in another flow (transition target flow's route has a specific transition target page).  
double_arrow | Create an entry message for a flow's start page (transition target flow's route has a fulfillment).  
  
### Route groups

When building an agent, you may find that many pages have a common set of routes. To make routes reusable, you can define _route groups_. You can create these group resources reusable either within the flow or the entire agent.

For example, you may want your flow to handle end-user input like "I want to add a topping to my pizza" and "I want to change my drink size". These inputs should be handled when any one of multiple pages of the flow are active. You could define two routes with intents to handle these inputs for all relevant pages, but this is a lot of duplicated work. Instead, you can define the route group once, and add a reference to the group on all relevant pages.

#### Flow-level route groups

_Flow-level route groups_ are route group resources that are created with a flow as parent. They are reusable within the flow.

#### Agent-level route groups

_Agent-level route groups_ are route group resources that are created with an agent as parent. They are reusable within the entire agent, but disallow routes that transition to a non symbolic page as target.

### Flow-level routes

_Flow-level routes_ are routes that are applied to a flow by adding them to the flow start page. These types of handlers have the following use cases:

X | Item  
---|---  
double_arrow | Handlers with an intent or condition requirement in scope for the [flow start page](https://docs.cloud.google.com/dialogflow/cx/docs/concept/flow#start-page).  
double_arrow | Handlers with an intent requirement in scope for all pages within the flow.  
  
To create flow-level routes from the console:

  1. Open the flow start page.
  2. Click the add add button in the **Routes** heading.
  3. The route editing panel opens.
  4. Provide route fields.
  5. Click **Save**.



To reorder flow-level routes from the console:

  1. Open the flow start page.
  2. Click the **Routes** heading.
  3. The route list panel opens.
  4. Drag routes in the desired order. Alternatively, click the option more_vert menu, then select **Move To**.



To delete flow-level routes from the console:

  1. Open the flow start page.
  2. Click the **Routes** heading.
  3. The route list panel opens.
  4. Click the option more_vert menu.
  5. Select **Delete**.



### Page-level routes

_Page-level routes_ are routes that are applied to a page. These types of handlers have the following use cases:

X | Item  
---|---  
double_arrow | Handlers with an intent or condition requirement in scope when specific pages are active.  
  
To create page-level routes from the console:

  1. Open the page (not the flow start page).
  2. Click the add add button in the **Routes** heading.
  3. The route editing panel opens.
  4. Provide route fields.
  5. Click **Save**.



To reorder page-level routes from the console:

  1. Open the page (not the flow start page).
  2. Click the **Routes** heading.
  3. The route list panel opens.
  4. Drag routes in the desired order. Alternatively, click the option more_vert menu, then select **Move To**.



To delete page-level routes from the console:

  1. Open the page (not the flow start page).
  2. Click the **Routes** heading.
  3. The route list panel opens.
  4. Click the option more_vert menu.
  5. Select **Delete**.



## Event handlers

Event handlers have one requirement in order to be called:

Term | Definition  
---|---  
Event requirement  | An _event_ which must be invoked. Events are identified by their name. Some built-in events are invoked when unexpected end-user input is received, or when a webhook error occurs. You can also define custom events that you invoke when something happens outside of the conversation.  
  
You can apply event handlers to flows (_flow-level event handlers_), pages (_page-level event handlers_), and parameters (_parameter-level event handlers_). For example, you might use event handlers in the following situations:

X | Item  
---|---  
double_arrow | When end-user input does not match any intents, a _no-match_ event handler provides a specific [static fulfillment](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#static) response.  
double_arrow | A timer expires in your system, and you want to provide reminder information to the end-user with a specific [static fulfillment](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#static) response.  
  
### Flow-level event handlers

_Flow-level event handlers_ are event handlers that are applied to a flow. These types of handlers have the following use cases:

X | Item  
---|---  
double_arrow | Handlers with an event requirement in scope for the [flow start page](https://docs.cloud.google.com/dialogflow/cx/docs/concept/flow#start-page).  
double_arrow | Handlers with an event requirement in scope for all pages within the flow.  
double_arrow | Handling unexpected end-user input, shared by all pages in a flow.  
double_arrow | Handling webhook errors, shared by all pages in a flow.  
double_arrow | Handling custom events invoked by your system, shared by all pages in a flow.  
  
Every flow has event handlers for the `no-match` and `no-input` built-in events. These event handlers are automatically created when you create a flow, and they cannot be deleted.

To create flow-level event handlers from the console:

  1. Open the flow start page.
  2. Click the add add button in the **Event handlers** heading.
  3. The event handler panel opens.
  4. Provide event handler fields.
  5. Click **Save**.



To delete flow-level event handlers from the console:

  1. Open the flow start page.
  2. Click the **Event handlers** heading.
  3. The event handler list panel opens.
  4. Hover your mouse over an event handler, then click the delete delete button.



### Page-level event handlers

_Page-level event handlers_ are event handlers that are applied to a page. These types of handlers have the following use cases:

X | Item  
---|---  
double_arrow | Handlers with an event requirement in scope when specific pages are active.  
double_arrow | Handling unexpected end-user input, specific to a page.  
double_arrow | Handling webhook errors, specific to a page.  
double_arrow | Handling custom events invoked by your system, specific to a page.  
  
To create page-level event handlers from the console:

  1. Open a page (not the flow start page).
  2. If there is no **Event handlers** heading, click **Add state handler** , select **Event handlers** , then click **Apply**.
  3. Click the add add button in the **Event handlers** heading.
  4. The event handler panel opens.
  5. Provide event handler fields.
  6. Click **Save**.



To delete page-level event handlers from the console:

  1. Open a page (not the flow start page).
  2. Click the **Event handlers** heading.
  3. The event handler list panel opens.
  4. Hover your mouse over an event handler, then click the delete delete button.



### Parameter-level event handlers

_Parameter-level event handlers_ are event handlers that are applied to a form parameter. They are also known as [reprompt handlers](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter#form-reprompt). These event handlers do not allow custom events, as they are specifically intended to handle invalid end-user input during form filling.

These types of handlers have the following use cases:

X | Item  
---|---  
double_arrow | The end-user did not provide valid input when asked to fill a form parameter.  
  
To create parameter-level event handlers from the console:

  1. Open a page that contains form parameters.
  2. Click a parameter.
  3. The parameter panel opens.
  4. Scroll down to the **Reprompt event handlers** section, then click **Add event handler**.
  5. The event handler panel opens.
  6. Provide event handler fields.
  7. Click **Save**.



To delete parameter-level event handlers from the console:

  1. Open a page that contains form parameters.
  2. Click a parameter.
  3. The parameter panel opens.
  4. Scroll down to the **Reprompt event handlers** section.
  5. Hover your mouse over an event handler, then click the delete delete button.



### Built-in events

**Note:** There are important best practices for built-in error events described in the [agent design best practices guide](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-design#errors).

The following events are built-in and are invoked by Dialogflow CX. Some events are restricted to certain levels.

Event name | Flow-level | Page-level | Parameter-level | Invoked when  
---|---|---|---|---  
`sys.no-match-default` | ✔ | ✔ | ✔ | 

  * For flow or page level: end-user input does not match any intents for handlers that are in scope.
  * For parameter level: end-user input does not satisfy the form parameter.

  
`sys.no-match-[1-6]` | ✔ | ✔ | ✔ | If you provide handlers for any of these numerically ordered events, they are invoked instead of `sys.no-match-default` and in order: `sys.no-match-1`, `sys.no-match-2`, ...  
`sys.no-input-default` | ✔ | ✔ | ✔ | End-user input was not received. This can be invoked when: 

  * Dialogflow CX receives empty end-user text input.
  * Dialogflow CX receives empty end-user audio input or the input does not contain any recognized speech.
  * A [no speech timeout](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-settings#settings-speech) occurs before end-user audio input contains any recognized speech.

  
`sys.no-input-[1-6]` | ✔ | ✔ | ✔ | If you provide handlers for any of these numerically ordered events, they are invoked instead of `sys.no-input-default` and in order: `sys.no-input-1`, `sys.no-input-2`, ...  
`sys.invalid-parameter` |  |  | ✔ | Invoked when a [webhook response](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook#webhook-response) invalidates the parameter by setting `WebhookResponse.pageInfo.formInfo.parameterInfo.state` to `INVALID`.  
`sys.long-utterance` | ✔ | ✔ | ✔ | End-user input exceeds the maximum allowed length (256 characters) matched by **non-generative intents** or **parameters**. If not provided, Dialogflow CX treats long user utterance as `no-match`. For streaming audio inputs, this event is triggered only after the client closes the audio stream.  
`webhook.error` | ✔ | ✔ |  | The webhook call returned an error. This event is only invoked: 1) if there is no fine-grained webhook event handler (e.g. webhook.error.timeout) that matches the webhook error code, 2) if there is no transition target set in the original route that called the fulfillment with the failing webhook. See the evaluation order section for details.  
`webhook.error.timeout` | ✔ | ✔ |  | The webhook call timed out. A webhook event will only be invoked if there is no transition target set in the original route that called the fulfillment with the failing webhook. See the evaluation order section for details.  
`webhook.error.bad-request` | ✔ | ✔ |  | The webhook returned [400 Bad Request](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook#errors). A webhook event will only be invoked if there is no transition target set in the original route that called the fulfillment with the failing webhook. See the evaluation order section for details.  
`webhook.error.rejected` | ✔ | ✔ |  | The webhook returned [401 Unauthorized](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook#errors) or [403 Forbidden](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook#errors). A webhook event will only be invoked if there is no transition target set in the original route that called the fulfillment with the failing webhook. See the evaluation order section for details.  
`webhook.error.unavailable` | ✔ | ✔ |  | The webhook returned [503 Service Unavailable](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook#errors). A webhook event will only be invoked if there is no transition target set in the original route that called the fulfillment with the failing webhook. See the evaluation order section for details.  
`webhook.error.not-found` | ✔ | ✔ |  | The webhook call failed because the webhook URL was unreachable. A webhook event will only be invoked if there is no transition target set in the original route that called the fulfillment with the failing webhook. See the evaluation order section for details.  
`flow-cancelled` | ✔ | ✔ |  | End-user requested cancellation of flow. This event is triggered by the End Flow With Cancellation page, see the `END_FLOW_WITH_CANCELLATION` [symbolic transition target](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#symbolic).  
`flow-failed` | ✔ | ✔ |  | This flow wasn't able to complete the given task. This event is triggered by the End Flow With Failure page, see the `END_FLOW_WITH_FAILURE` [symbolic transition target](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#symbolic).  
`flow-failed-human-escalation` | ✔ | ✔ |  | End-user requested to talk to human agents. This event is triggered by the End Flow With Human Escalation page, see the `END_FLOW_WITH_HUMAN_ESCALATION` [symbolic transition target](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#symbolic).  
  
### Custom events

You can create custom events and event handlers. Custom events are used to handle things that happen outside the conversation with the end-user. For example, the end-user clicked a button, a certain amount of time has passed, available inventory has changed during the conversation, and so on.

Events are simply identified by name. You should avoid using event names that start with `sys.` or `webhook.` to avoid conflict with built-in events.

To invoke an event with the API, see the `queryInput.event` field of the `detectIntent` method for the `Session` type. Go to the Session API reference

**Select a protocol and version for the Session reference:**

Protocol | V3 | V3beta1  
---|---|---  
REST |  [Session resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.sessions) |  [Session resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.sessions)  
RPC |  [Session interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#google.cloud.dialogflow.cx.v3.Sessions) |  [Session interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3beta1#google.cloud.dialogflow.cx.v3beta1.Sessions)  
C++ |  [SessionsClient](https://googleapis.dev/cpp/google-cloud-dialogflow_cx/latest/classgoogle_1_1cloud_1_1dialogflow__cx_1_1SessionsClient.html) |  Not available   
C# |  [SessionsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SessionsClient) |  Not available   
Go |  [SessionsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3#cloud_google_com_go_dialogflow_cx_apiv3_SessionsClient) |  Not available   
Java |  [SessionsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsClient) |  [SessionsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.SessionsClient)  
Node.js |  [SessionsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3.SessionsClient.html) |  [SessionsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3beta1.SessionsClient.html)  
PHP |  Not available  |  Not available   
Python |  [SessionsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.services.sessions.SessionsClient) |  [SessionsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3beta1.services.sessions.SessionsClient)  
Ruby |  Not available  |  Not available   
  
Close

## Evaluation order

Handlers are evaluated in a specific order. The following general rules apply:

  1. Only handlers in scope are evaluated.
  2. Only handlers whose requirements are satisfied can be called.
  3. If a handler without a transition target is called, evaluation of the list of handlers continues. Due to this rule, multiple fulfillments can add multiple messages to the [response queue](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#queue).
  4. If a handler with a transition target is called, evaluation of the list of handlers ends.
  5. If a handler with fulfillment is called, and the fulfillment results in a webhook error: 
     * If the handler has a transition target defined, the webhook silently fails.
     * If an event handler is in scope for the event, it handles the event and evaluation of the list of handlers ends.
     * If no event handler is in scope for the event, the webhook silently fails.
  6. When an intent requirement is satisfied, the intent is consumed, so only the first route handler found for the intent can be called (See intent propagation for the exceptions).
  7. When a condition requirement is satisfied, the condition is not consumed, so multiple routes with the condition can be called.
  8. When an event requirement is satisfied, the event is consumed, so only the first event handler found for the event can be called.
  9. The handler call stack can affect evaluation order.



There are three phases to the evaluation:

  1. Routes that have an intent requirement are evaluated in this order: 
     1. **Page-level** : Individual routes applied to the current page, in the order supplied.
     2. **Page-level groups** : Route groups applied to the current page, in the order supplied.
     3. **Flow-level** : Routes applied to the active flow, in the order supplied.
     4. **Flow-level groups** : Route groups applied to the active flow, in the order supplied.
  2. Routes with only a condition requirement are evaluated in this order: 
     1. **Page-level** : Individual routes applied to the current page, in the order supplied.
     2. **Page-level groups** : Route groups applied to the current page, in the order supplied.
     3. **Flow-level (Only if the current page is the[flow start page](https://docs.cloud.google.com/dialogflow/cx/docs/concept/flow#start-page))**: Routes applied to the active flow, in the order supplied.
     4. **Flow-level groups (Only if the current page is the[flow start page](https://docs.cloud.google.com/dialogflow/cx/docs/concept/flow#start-page))**: Route groups applied to the active flow, in the order supplied.
  3. Event handlers are evaluated in this order: 
     1. **Parameter-level** : Event handlers applied to the current page's form parameter that the agent is currently attempting to fill (reprompt handlers), in the order supplied.
     2. **Page-level** : Event handlers applied to the current page, in the order supplied.
     3. **Flow-level** : Event handlers applied to the active flow, in the order supplied.



## Symbolic transition targets

When entering a transition target for a handler, you can enter specific flows or pages, but you can also enter symbolic transition targets:

Symbolic transition target | Description  
---|---  
`START_PAGE` | Transition to the like-named active flow's [start page](https://docs.cloud.google.com/dialogflow/cx/docs/concept/flow#start-page).  
`END_FLOW` | End the currently active flow and transition back to the page that caused a transition to the current flow. Also see Handler call stack and flow stack limit.  
`END_FLOW_WITH_CANCELLATION` | End the currently active flow and transition back to the page that caused a transition to the current flow. The calling page can handle this transition with the `flow-cancelled` [built-in event](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#event-built-in). Also see Handler call stack and flow stack limit.  
`END_FLOW_WITH_FAILURE` | End the currently active flow and transition back to the page that caused a transition to the current flow. The calling page can handle this transition with the `flow-failed` [built-in event](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#event-built-in). Also see Handler call stack and flow stack limit.  
`END_FLOW_WITH_HUMAN_ESCALATION` | End the currently active flow and transition back to the page that caused a transition to the current flow. The calling page can handle this transition with the `flow-failed-human-escalation` [built-in event](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#event-built-in). Also see Handler call stack and flow stack limit.  
`END_SESSION` | Clear current session and transition to the special page named `END_SESSION`. The next user input will restart the session at the [start page](https://docs.cloud.google.com/dialogflow/cx/docs/concept/flow#start-page) of the [Default Start Flow](https://docs.cloud.google.com/dialogflow/cx/docs/concept/flow#start).  
`PREVIOUS_PAGE` | Transition to the previous page that caused a transition to the current page. The page state from the previous page will be restored after transition.  
`CURRENT_PAGE` | Re-transition to the current page. This can be useful if you want the agent to repeat something.  
  
## Handler call stack and flow stack limit

When a session transitions from flow to flow with specific transition targets, each flow is pushed onto the flow [stack](https://en.wikipedia.org/wiki/Stack_\(abstract_data_type\)).

### Handler call stack

When a session transitions to `END_FLOW`, it returns back to the calling page that caused a transition to the completed flow. In this situation, the handler call stack is preserved. All handlers that were previously evaluated from the calling page will be skipped, and the remaining handlers will be evaluated in order.

For example:

  1. Page **P** has three handlers in this order: **H1** , **H2** , **H3**.
  2. **H1** is evaluated, but it does not cause a transition.
  3. **H2** is evaluated, and it causes a transition to flow **F**.
  4. A page in flow **F** transitions to `END_FLOW`.
  5. The session returns to Page **P** , which becomes active again with a preserved state.
  6. The handler evaluation in page **P** continues from the status it preserved, thus **H3** is evaluated.



### Flow stack limit

Maximum flow stack limit is 25. Exceeding the maximum stack limit may cause flows to be popped from the stack, leading to unexpected behavior when using the `END_FLOW` transition. To avoid these potential issues, minimize the number of flow-to-flow transitions preceding the `END_FLOW` transition.

If the flow stack is empty, the `END_FLOW` transition ends the session.

## Set conditions

To set [conditions](https://docs.cloud.google.com/dialogflow/cx/docs/reference/condition) with the console, you supply condition rules with one of three logical options:

  * Match AT LEAST ONE rule (OR)
  * Match EVERY rule (AND)
  * Customize expression



As a convenience, you can use the AND/OR options to create simple or compound conditions for parameter values.

You can use the free form **Customize expression** option for all types of conditions, including [system functions](https://docs.cloud.google.com/dialogflow/cx/docs/reference/condition#func) and [boolean constants](https://docs.cloud.google.com/dialogflow/cx/docs/reference/condition#bool-const).

For example, to set a condition that has a 10% chance of passing evaluation, select the **Customize expression** option and enter `$sys.func.rand() < 0.1` in the **Condition** field:

![Screenshot of setting a custom condition](https://docs.cloud.google.com/static/dialogflow/cx/docs/images/condition-custom.png)

[ Previous arrow_back  Pages  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/page)

[ Next Intents  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/intent)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
