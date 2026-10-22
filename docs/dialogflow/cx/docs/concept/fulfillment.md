---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment/
title: Fulfillments \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:43:40.313566+00:00
---

# Fulfillments  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Fulfillments Stay organized with collections  Save and categorize content based on your preferences. 

For an agent's conversational turn, the agent must respond to the end-user with an answer to a question, a query for information, or session termination. Your agent may also need to contact your service to generate dynamic responses or take actions for a turn. _Fulfillment_ is used to accomplish all of this.

A fulfillment may contain any of the following:

  * Static response messages.
  * Webhook calls for dynamic responses and/or to take actions.
  * Parameter presets to set or override parameter values.



During an agent's turn, it is possible (and sometimes desirable) to call multiple fulfillments, each of which may generate a response message. Dialogflow CX maintains these responses in a _response queue_. Once the agent's turn is over, Dialogflow CX sends the ordered responses to the end-user.

## Fulfillment use cases

Fulfillment lets you provide response messages in the following places:

  * [Page entry fulfillment](https://docs.cloud.google.com/dialogflow/cx/docs/concept/page)
  * [Routes](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#route)
  * [Event handlers](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#event)
  * [Initial prompts for forms](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter#form)
  * [Reprompt handlers for forms](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter#form-reprompt)



For each of these use cases, the console opens a fulfillment editing pane.

![Fulfillment screenshot](https://docs.cloud.google.com/static/dialogflow/cx/docs/images/fulfillment-panel.png)

## Agent responses (dialogue options)

Define agent response messages at design time when creating fulfillment. At runtime, these responses are added to the response queue.

There are several types of response messages, which are described in the following subsections. When using the console, a fulfillment panel has an initial **Agent dialogue** card, but you can click **Add dialogue response** to add more cards for other response message types.

### Static text response

Static text response messages provide text dialogue to the user. If your detect intent API calls or integration calls use speech synthesis, this text generates audio content. For these messages, supplied text uses the Speech Synthesis Markup Language (SSML).

You can define multiple text response cards and multiple text responses within each card. If you define multiple cards, they are concatenated for a single response at runtime. If you define multiple responses within a card, one of the messages in the card is selected randomly at runtime.

These text messages can contain [parameter references](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter) and inline [system functions](https://docs.cloud.google.com/dialogflow/cx/docs/reference/system-functions).

### Custom payload

Some [integrations](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration) support a custom payload response to handle rich responses. These custom payloads must be supplied in the JSON format defined in the integration documentation. For example, see the [Dialogflow CX Messenger custom payload format](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/dialogflow-messenger#fulfillment).

You can include [parameter references](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter#use) in your custom payload JSON. Wrap them in double quotes to treat them as JSON string values. For example:
    
    
    {
      "someField": "$session.params.date"
    }
    

Custom payload JSON must be limited to 24 levels of depth.

You can also send a custom payload to integrations that you develop. It won't be processed by Dialogflow CX, so you must handle it in your own business logic.

For more information, see custom payload templates.

### Live agent handoff

This response signals to the detect intent API caller that the conversation should be handed off to a human agent. Dialogflow CX uses this signal only to identify conversations handed off for measurement purposes; it does not alter the session state.

Your system or integration can use this signal to take any actions necessary to hand off the conversation. Because Dialogflow CX does not impose structure on this data, you can choose any structure that suits your system.

### Conversation success metadata

This response signals to the detect intent API caller that the conversation with the Dialogflow CX agent succeeded. Dialogflow CX uses this signal to identify conversations that succeeded for measurement purposes, and it doesn't alter the session state in any way.

Your system or integration can use this signal to take any actions that are necessary. Dialogflow CX doesn't impose any structure on this data, so you can choose any structure that suits your system.

### Play prerecorded audio

This response plays an audio file for [integrations](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration) that support this feature.

Audio file format requirements might differ for different integrations. For example, see the [requirements](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/phone-gateway#audio) for Dialogflow CX Phone Gateway.

For [partner telephony integrations](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration#telephony-partner-built-in), the URL for the audio file must be accessible by the partner. A publicly available URL, such as a [public file in Cloud Storage](https://docs.cloud.google.com/storage/docs/access-control/making-data-public), is always accessible by the partner. The partner may also provide restricted access for audio files. See the partner documentation for details.

### Output audio text

This response is similar to the text response, but it is only applicable to speech synthesis. If your agent can handle both text and voice sessions, you can use unique _text_ and _output audio text_ responses to create a different user experience for text versus voice. If output audio text is supplied for a voice session, the plain text responses are ignored.

If your agent handles both text and voice sessions and you want the same response messages, use text responses for both text and voice sessions.

Output audio text is concatenated similarly to text responses. If the output audio text responses are a mixture of text and SSML, the concatenated result is treated as SSML. You should ideally use either text or SSML consistently.

### Conditional response

This response type provides conditional responses:

The general format is:
    
    
    if [condition]
      [response]
    elif [condition]
      [response]
    elif [condition]
      [response]
    else
      [response]
    endif
    

where:

  * `[condition]` uses the same format as [route conditions](https://docs.cloud.google.com/dialogflow/cx/docs/reference/condition).
  * `[response]` is a text response.
  * `elif` and `else` blocks are optional.



For example:
    
    
    if $session.params.user-age >= 21
      Ok, you may enter.
    else
      Sorry, you cannot enter.
    endif
    

Both `[condition]` and `[response]` can use inline system functions to generate dynamic values during conversations. For more information, see [system functions](https://docs.cloud.google.com/dialogflow/cx/docs/reference/system-functions) and [route conditions](https://docs.cloud.google.com/dialogflow/cx/docs/reference/condition#func). The `[condition]` is resolved based on the session state at the beginning of the fulfillment. If the `[response]` relies on the session state, it is resolved based on the updated session state at the end of fulfillment.

For [multilingual agents](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-multilingual), `[condition]` is common for all languages, while `[response]` is language-specific. When you change `[condition]` for one language in the console, this part is updated in all of the agent's languages. Because it becomes a new condition, `[response]` is cleared for all languages other than the language you selected when updating `[condition]`.

### Telephony call transfer

Call transfers are available only for the [Dialogflow CX Phone Gateway](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/phone-gateway).

For some telephony integrations, you can specify a phone number in the US for call transfers. At runtime, when the Dialogflow CX agent triggers a fulfillment with call transfer, the call is transferred to the specified number and agent handling is suspended.

### Data store tool response

This response type configures agent responses returned from linked [data store tools](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#data_store_tools). If you configured a data store tool in this fulfillment, a data store tool response card is populated automatically.

  * **Source links:** Set the maximum number of citations to return to the user after the response. A citation is a link to the source of information in the data store, rendered as buttons. The default is 1.
  * **Inline citations:** Limit the number of inline citations returned per sentence instead of listing links after the response.
  * **Generative fallback:** Configure the agent to attempt an AI-generated response if the data store returns an empty result. If this fails, the agent uses static responses.
  * **Static responses:** Enter static text responses in the final field to send to the user word-for-word.



## Channel-specific response messages

When defining fulfillment, you can create _channel-specific response messages_ to create targeted responses for text chat, voice, SMS, or specific integrations that support channels. Any response messages that are not specific to a channel are called _default response messages_.

At runtime, Dialogflow CX selects either the default response message or a channel-specific response message when a detect intent request specifies a channel. As a best practice, you should define default response messages, even if you are using channel-specific response messages. The default response messages act as a fallback when your system fails to provide a valid channel.

A channel name is a custom field that you can set to any text. If you use the Dialogflow CX API directly for runtime calls, you can use any channel names that you like. If you use an existing integration, you must use the channel names that the integration recognizes.

### Setting channel-specific response messages at design time

To provide channel-specific response messages for fulfillment when using the console:

  * Click **Add channel** after adding default response messages to add channel-specific response messages. Click **Add channel** again to add additional channels.



To provide channel-specific response messages for fulfillment when using the API:

  * Set the `Fulfillment.messages[i].channel` field to the chosen channel for each response message. If this field is not set, the response is treated as a default response message.



### Utilizing channel-specific response messages at runtime

If you are using an existing integration that supports channels, the integration implementation performs these steps.

To receive a channel-specific response message, you must specify the channel in the detect intent request message. See the `queryParams.channel` field in the `detectIntent` method of the `Sessions` type. Go to the Session API reference

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

Dialogflow CX returns the default response message if a request defines no channel or if fulfillment finds no matching channel.

## Custom payload templates

If you use custom payloads often, use _custom payload templates_. Custom payloads are sometimes large and complex, so using templates simplifies the agent creation process.

Provide these templates in your agent settings to make them available for selection when creating fulfillment for your agent.

For example, the JSON payload for "yes" and "no" buttons can be defined as custom payload templates. When creating fulfillment that requires these buttons, select the template when creating fulfillment.

When you select a template for a fulfillment custom payload, the contents of the template are inserted into the payload. You can then edit the payload as needed.

If you change a template, changes don't propagate automatically to all fulfillment payloads where it has been referenced.

To create a custom payload template, see the [agent general settings](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-settings#settings-general).

To select a custom payload template when creating fulfillment, click **Select template** when creating a fulfillment custom payload.

## Webhook calls

When a fulfillment triggers a [webhook](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook), the agent sends a request to your service. Your webhook can perform actions, provide dynamic response messages, override parameter values, and change the current page.

The following describes webhook settings for fulfillment:

X | Item  
---|---  
Enable webhook | This enables webhook for the fulfillment.  
Webhook | Select the webhook resource.  
Tag | The text tag you provide here will get populated in the `WebhookRequest.fulfillmentInfo.tag` field of the webhook request sent to your webhook service. This can be used to control the webhook behavior in a way that is fulfillment-specific.  
Return partial response | Allows cancellation of a partial response playback. For details, see [Advanced speech settings](https://docs.cloud.google.com/dialogflow/cx/docs/concept/advanced-speech).  
  
## Parameter presets

Use fulfillment to provide presets that set or override current parameter values. These presets are applied before resolving static response messages or calling a webhook.

You can also use [system functions](https://docs.cloud.google.com/dialogflow/cx/docs/reference/system-functions) to preset a parameter to a dynamically generated value.

Some examples include:

  * Setting a parameter `now` to the current time:

Parameter | Value  
---|---  
now | $sys.func.NOW()  
  * Incrementing an existing parameter `counter` by 1:

Parameter | Value  
---|---  
counter | $sys.func.ADD($session.params.counter, 1)  
  * Setting a parameter `new-cost` to the `other-cost` parameter value, while maintaining the full composite object value:

Parameter | Value  
---|---  
new-cost | $sys.func.IDENTITY($session.params.other-cost)  



## Data store tools

For more information about this feature, see the [data store tools documentation](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store/handler).

## Advanced speech settings

These [advanced speech settings](https://docs.cloud.google.com/dialogflow/cx/docs/concept/advanced-speech) can override the [page speech settings](https://docs.cloud.google.com/dialogflow/cx/docs/concept/page#settings), [flow speech settings](https://docs.cloud.google.com/dialogflow/cx/docs/concept/flow#settings), and [agent speech settings](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-settings#settings-speech).

## Response queue

During an agent's turn, you can call multiple fulfillments, each of which may generate a response message. Dialogflow CX maintains these responses in a _response queue_.

## Partial response for streaming API

By default, Dialogflow CX only sends ordered responses to end-users after the agent's turn ends. You can also enable the **Return partial response** option in fulfillment to return queued responses as a partial response when using the streaming APIs. To learn more, see [Lifecycle of a page](https://docs.cloud.google.com/dialogflow/cx/docs/concept/page#life).

For example, if your webhook is likely to run for a long time, you can add a static response in the fulfillment and enable partial response. This causes Dialogflow CX to flush the _response queue_ and send all messages as a partial response before calling the webhook.

Partial response is not supported for the following:

  * Audio inputs in the [simulator](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console#simulator).
  * [Partner telephony integrations](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration#telephony-partner-built-in) might not support partial response. See the partner documentation to verify.



To test this feature in the simulator, enable partial response.

![Simulator partial response screenshot](https://docs.cloud.google.com/static/dialogflow/cx/docs/images/partial-response-simulator.png)

In the following example, consider that your webhook takes 5 seconds to complete and you don't enable partial response. The Dialogflow CX agent's conversational turn is not over until the webhook completes. During this 5- second turn, responses are queued while waiting for the webhook, and they are not returned to the end-user until the turn is complete. This leads to a bad user experience.

![Without partial response.](https://docs.cloud.google.com/static/dialogflow/cx/docs/images/without_partial_response.svg)

If you enable partial response in the first fulfillment, Dialogflow CX returns the first fulfillment message quickly and calls the webhook. After the webhook completes, Dialogflow CX returns the final response. This scenario improves the end-user experience because the end-user is told to expect a short wait. In addition, the webhook call executes concurrently with a response sent to the end-user.

![With partial response.](https://docs.cloud.google.com/static/dialogflow/cx/docs/images/with_partial_response.svg)

## Speech Synthesis Markup Language (SSML)

You can use Speech Synthesis Markup Language (SSML) in text or output audio text fulfillment fields. This lets you customize your audio response by providing details on pauses and audio formatting for acronyms, dates, times, abbreviations, or text that should be censored.

For syntax details, see the [Text-to-speech SSML documentation](https://docs.cloud.google.com/text-to-speech/docs/ssml).

**Note:** A fulfillment field can have no more than one `<speak></speak>` tag pair.

[ Previous arrow_back  Parameters  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter)

[ Next Webhooks  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
