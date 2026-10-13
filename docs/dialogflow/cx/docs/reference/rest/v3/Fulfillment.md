---
url: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment/
title: Fulfillment \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:23:32.632857+00:00
---

# Fulfillment  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/cx/docs/reference)



Send feedback 

#  Fulfillment Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * ResponseMessage
    * JSON representation
  * ConversationSuccess
    * JSON representation
  * OutputAudioText
    * JSON representation
  * LiveAgentHandoff
    * JSON representation
  * EndInteraction
  * PlayAudio
    * JSON representation
  * MixedAudio
    * JSON representation
  * Segment
    * JSON representation
  * TelephonyTransferCall
    * JSON representation
  * KnowledgeInfoCard
  * ToolCall
    * JSON representation
  * ResponseType
  * SetParameterAction
    * JSON representation
  * ConditionalCases
    * JSON representation
  * Case
    * JSON representation
  * CaseContent
    * JSON representation
  * GeneratorSettings
    * JSON representation



A fulfillment can do one or more of the following actions at the same time:

  * Generate rich message responses.
  * Set parameter values.
  * Call the webhook.



Fulfillments can be called at various stages in the `[Page](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.pages#Page)` or `[Form](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.pages#Page.Form)` lifecycle. For example, when a `DetectIntentRequest` drives a session to enter a new page, the page's entry fulfillment can add a static response to the `[QueryResult](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/QueryResult)` in the returning `[DetectIntentResponse](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/DetectIntentResponse)`, call the webhook (for example, to load user data from a database), or both.

JSON representation  
---  
      
    
    {
      "messages": [
        {
          object ([ResponseMessage](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment#ResponseMessage))
        }
      ],
      "webhook": string,
      "returnPartialResponses": boolean,
      "tag": string,
      "codeBlockFunction": string,
      "setParameterActions": [
        {
          object ([SetParameterAction](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment#SetParameterAction))
        }
      ],
      "conditionalCases": [
        {
          object ([ConditionalCases](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment#ConditionalCases))
        }
      ],
      "advancedSettings": {
        object ([AdvancedSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/AdvancedSettings))
      },
      "enableGenerativeFallback": boolean,
      "generators": [
        {
          object ([GeneratorSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment#GeneratorSettings))
        }
      ]
    }  
  
Fields  
---  
`messages[]` |  `object (`[ResponseMessage](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment#ResponseMessage)`)` The list of rich message responses to present to the user.  
`webhook` |  `string` The webhook to call. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/webhooks/<WebhookID>`.  
`returnPartialResponses` |  `boolean` Whether Dialogflow should return currently queued fulfillment response messages in streaming APIs. If a webhook is specified, it happens before Dialogflow invokes webhook. Warning: 1) This flag only affects streaming API. Responses are still queued and returned once in non-streaming API. 2) The flag can be enabled in any fulfillment but only the first 3 partial responses will be returned. You may only want to apply it to fulfillments that have slow webhooks.  
`tag` |  `string` The value of this field will be populated in the `[WebhookRequest](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/WebhookRequest)` `fulfillmentInfo.tag` field by Dialogflow when the associated webhook is called. The tag is typically used by the webhook service to identify which fulfillment is being called, but it could be used for other purposes. This field is required if `webhook` is specified.  
`codeBlockFunction` |  `string` Optional. The name of the code block function to execute, if this is a code block fulfillment. The code block itself is implied by the fulfillment's parent, e.g. a playbook.  
`setParameterActions[]` |  `object (`[SetParameterAction](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment#SetParameterAction)`)` Set parameter values before executing the webhook.  
`conditionalCases[]` |  `object (`[ConditionalCases](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment#ConditionalCases)`)` Conditional cases for this fulfillment.  
`advancedSettings` |  `object (`[AdvancedSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/AdvancedSettings)`)` Hierarchical advanced settings for this fulfillment. The settings exposed at the lower level overrides the settings exposed at the higher level.  
`enableGenerativeFallback` |  `boolean` If the flag is true, the agent will utilize LLM to generate a text response. If LLM generation fails, the defined `[responses](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment#FIELDS.messages)` in the fulfillment will be respected. This flag is only useful for fulfillments associated with no-match event handlers.  
`generators[]` |  `object (`[GeneratorSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment#GeneratorSettings)`)` A list of Generators to be called during this fulfillment.  
  
## ResponseMessage

Represents a response message that can be returned by a conversational agent.

Response messages are also used for output audio synthesis. The approach is as follows:

  * If at least one OutputAudioText response is present, then all OutputAudioText responses are linearly concatenated, and the result is used for output audio synthesis.
  * If the OutputAudioText responses are a mixture of text and SSML, then the concatenated result is treated as SSML; otherwise, the result is treated as either text or SSML as appropriate. The agent designer should ideally use either text or SSML consistently throughout the bot design.
  * Otherwise, all Text responses are linearly concatenated, and the result is used for output audio synthesis.



This approach allows for more sophisticated user experience scenarios, where the text displayed to the user may differ from what is heard.

JSON representation  
---  
      
    
    {
      "responseType": enum ([ResponseType](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment#ResponseType)),
      "channel": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "text": {
        object ([Text](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Text))
      },
      "payload": {
        object
      },
      "conversationSuccess": {
        object ([ConversationSuccess](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment#ConversationSuccess))
      },
      "outputAudioText": {
        object ([OutputAudioText](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment#OutputAudioText))
      },
      "liveAgentHandoff": {
        object ([LiveAgentHandoff](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment#LiveAgentHandoff))
      },
      "endInteraction": {
        object ([EndInteraction](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment#EndInteraction))
      },
      "playAudio": {
        object ([PlayAudio](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment#PlayAudio))
      },
      "mixedAudio": {
        object ([MixedAudio](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment#MixedAudio))
      },
      "telephonyTransferCall": {
        object ([TelephonyTransferCall](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment#TelephonyTransferCall))
      },
      "knowledgeInfoCard": {
        object ([KnowledgeInfoCard](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment#KnowledgeInfoCard))
      },
      "toolCall": {
        object ([ToolCall](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment#ToolCall))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`responseType` |  `enum (`[ResponseType](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment#ResponseType)`)` Response type.  
`channel` |  `string` The channel which the response is associated with. Clients can specify the channel via `[QueryParameters.channel](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/QueryParameters#FIELDS.channel)`, and only associated channel response will be returned.  
Required. The rich response message. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`text` |  `object (`[Text](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Text)`)` Returns a text response.  
`payload` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Returns a response containing a custom, platform-specific payload.  
`conversationSuccess` |  `object (`[ConversationSuccess](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment#ConversationSuccess)`)` Indicates that the conversation succeeded.  
`outputAudioText` |  `object (`[OutputAudioText](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment#OutputAudioText)`)` A text or ssml response that is preferentially used for TTS output audio synthesis, as described in the comment on the ResponseMessage message.  
`liveAgentHandoff` |  `object (`[LiveAgentHandoff](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment#LiveAgentHandoff)`)` Hands off conversation to a human agent.  
`endInteraction` |  `object (`[EndInteraction](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment#EndInteraction)`)` Output only. A signal that indicates the interaction with the Dialogflow agent has ended. This message is generated by Dialogflow only when the conversation reaches `END_SESSION` page. It is not supposed to be defined by the user.It's guaranteed that there is at most one such message in each response.  
`playAudio` |  `object (`[PlayAudio](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment#PlayAudio)`)` Signal that the client should play an audio clip hosted at a client-specific URI. Dialogflow uses this to construct `[mixedAudio](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment#ResponseMessage.FIELDS.mixed_audio)`. However, Dialogflow itself does not try to read or process the URI in any way.  
`mixedAudio` |  `object (`[MixedAudio](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment#MixedAudio)`)` Output only. An audio response message composed of both the synthesized Dialogflow agent responses and responses defined via `[playAudio](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment#ResponseMessage.FIELDS.play_audio)`. This message is generated by Dialogflow only and not supposed to be defined by the user.  
`telephonyTransferCall` |  `object (`[TelephonyTransferCall](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment#TelephonyTransferCall)`)` A signal that the client should transfer the phone call connected to this agent to a third-party endpoint.  
`knowledgeInfoCard` |  `object (`[KnowledgeInfoCard](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment#KnowledgeInfoCard)`)` Represents info card for knowledge answers, to be better rendered in Dialogflow Messenger.  
`toolCall` |  `object (`[ToolCall](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment#ToolCall)`)` Returns the definition of a tool call that should be executed by the client.  
End of mutually exclusive fields.  
  
## ConversationSuccess

Indicates that the conversation succeeded, i.e., the bot handled the issue that the customer talked to it about.

Dialogflow only uses this to determine which conversations should be counted as successful and doesn't process the metadata in this message in any way. Note that Dialogflow also considers conversations that get to the conversation end page as successful even if they don't return `[ConversationSuccess](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment#ConversationSuccess)`.

You may set this, for example: * In the `[entryFulfillment](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.pages#Page.FIELDS.entry_fulfillment)` of a `[Page](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.pages#Page)` if entering the page indicates that the conversation succeeded. * In a webhook response when you determine that you handled the customer issue.

JSON representation  
---  
      
    
    {
      "metadata": {
        object
      }
    }  
  
Fields  
---  
`metadata` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Custom metadata. Dialogflow doesn't impose any structure on this.  
  
## OutputAudioText

A text or ssml response that is preferentially used for TTS output audio synthesis, as described in the comment on the ResponseMessage message.

JSON representation  
---  
      
    
    {
      "allowPlaybackInterruption": boolean,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "text": string,
      "ssml": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`allowPlaybackInterruption` |  `boolean` Output only. Whether the playback of this message can be interrupted by the end user's speech and the client can then starts the next Dialogflow request.  
The source, which is either plain text or SSML. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`text` |  `string` The raw text to be synthesized.  
`ssml` |  `string` The SSML text to be synthesized. For more information, see [SSML](https://docs.cloud.google.com/speech/text-to-speech/docs/ssml).  
End of mutually exclusive fields.  
  
## LiveAgentHandoff

Indicates that the conversation should be handed off to a live agent.

Dialogflow only uses this to determine which conversations were handed off to a human agent for measurement purposes. What else to do with this signal is up to you and your handoff procedures.

You may set this, for example: * In the `[entryFulfillment](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.pages#Page.FIELDS.entry_fulfillment)` of a `[Page](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.pages#Page)` if entering the page indicates something went extremely wrong in the conversation. * In a webhook response when you determine that the customer issue can only be handled by a human.

JSON representation  
---  
      
    
    {
      "metadata": {
        object
      }
    }  
  
Fields  
---  
`metadata` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Custom metadata for your handoff procedure. Dialogflow doesn't impose any structure on this.  
  
## EndInteraction

This type has no fields.

Indicates that interaction with the Dialogflow agent has ended. This message is generated by Dialogflow only and not supposed to be defined by the user.

## PlayAudio

Specifies an audio clip to be played by the client as part of the response.

JSON representation  
---  
      
    
    {
      "audioUri": string,
      "allowPlaybackInterruption": boolean
    }  
  
Fields  
---  
`audioUri` |  `string` Required. URI of the audio clip. Dialogflow does not impose any validation on this value. It is specific to the client that reads it.  
`allowPlaybackInterruption` |  `boolean` Output only. Whether the playback of this message can be interrupted by the end user's speech and the client can then starts the next Dialogflow request.  
  
## MixedAudio

Represents an audio message that is composed of both segments synthesized from the Dialogflow agent prompts and ones hosted externally at the specified URIs. The external URIs are specified via `[playAudio](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment#ResponseMessage.FIELDS.play_audio)`. This message is generated by Dialogflow only and not supposed to be defined by the user.

JSON representation  
---  
      
    
    {
      "segments": [
        {
          object ([Segment](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment#Segment))
        }
      ]
    }  
  
Fields  
---  
`segments[]` |  `object (`[Segment](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment#Segment)`)` Segments this audio response is composed of.  
  
## Segment

Represents one segment of audio.

JSON representation  
---  
      
    
    {
      "allowPlaybackInterruption": boolean,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "audio": string,
      "uri": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`allowPlaybackInterruption` |  `boolean` Output only. Whether the playback of this segment can be interrupted by the end user's speech and the client should then start the next Dialogflow request.  
Content of the segment. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`audio` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Raw audio synthesized from the Dialogflow agent's response using the output config specified in the request.A base64-encoded string.  
`uri` |  `string` Client-specific URI that points to an audio clip accessible to the client. Dialogflow does not impose any validation on it.  
End of mutually exclusive fields.  
  
## TelephonyTransferCall

Represents the signal that telles the client to transfer the phone call connected to the agent to a third-party endpoint.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "phoneNumber": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
Endpoint to transfer the call to. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`phoneNumber` |  `string` Transfer the call to a phone number in [E.164 format](https://en.wikipedia.org/wiki/E.164).  
End of mutually exclusive fields.  
  
## KnowledgeInfoCard

This type has no fields.

Represents info card response. If the response contains generative knowledge prediction, Dialogflow will return a payload with Infobot Messenger compatible info card.

Otherwise, the info card response is skipped.

## ToolCall

Represents a call of a specific tool's action with the specified inputs.

JSON representation  
---  
      
    
    {
      "tool": string,
      "action": string,
      "inputParameters": {
        object
      }
    }  
  
Fields  
---  
`tool` |  `string` Required. The `[tool](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools#Tool)` associated with this call. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/tools/<ToolID>`.  
`action` |  `string` Required. The name of the tool's action associated with this call.  
`inputParameters` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. The action's input parameters.  
  
## ResponseType

Represents different response types.

Enums  
---  
`RESPONSE_TYPE_UNSPECIFIED` | Not specified.  
`ENTRY_PROMPT` | The response is from an `[entry prompt](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.pages#Page.FIELDS.entry_fulfillment)` in the page.  
`PARAMETER_PROMPT` | The response is from `[form-filling prompt](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.pages#Page.Parameter.FIELDS.fill_behavior)` in the page.  
`HANDLER_PROMPT` | The response is from a `[transition route](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/TransitionRoute)` or an [event handler][EventHandler] in the page or flow or transition route group.  
  
## SetParameterAction

Setting a parameter value.

JSON representation  
---  
      
    
    {
      "parameter": string,
      "value": value
    }  
  
Fields  
---  
`parameter` |  `string` Display name of the parameter.  
`value` |  `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)` The new value of the parameter. A null value clears the parameter.  
  
## ConditionalCases

A list of cascading if-else conditions. Cases are mutually exclusive. The first one with a matching condition is selected, all the rest ignored.

JSON representation  
---  
      
    
    {
      "cases": [
        {
          object ([Case](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment#Case))
        }
      ]
    }  
  
Fields  
---  
`cases[]` |  `object (`[Case](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment#Case)`)` A list of cascading if-else conditions.  
  
## Case

Each case has a Boolean condition. When it is evaluated to be True, the corresponding messages will be selected and evaluated recursively.

JSON representation  
---  
      
    
    {
      "condition": string,
      "caseContent": [
        {
          object ([CaseContent](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment#CaseContent))
        }
      ]
    }  
  
Fields  
---  
`condition` |  `string` The condition to activate and select this case. Empty means the condition is always true. The condition is evaluated against [form parameters][Form.parameters] or [session parameters][SessionInfo.parameters].See the [conditions reference](https://cloud.google.com/dialogflow/cx/docs/reference/condition).  
`caseContent[]` |  `object (`[CaseContent](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment#CaseContent)`)` A list of case content.  
  
## CaseContent

The list of messages or conditional cases to activate for this case.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "message": {
        object ([ResponseMessage](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment#ResponseMessage))
      },
      "additionalCases": {
        object ([ConditionalCases](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment#ConditionalCases))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
Either a message is returned or additional cases to be evaluated. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`message` |  `object (`[ResponseMessage](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment#ResponseMessage)`)` Returned message.  
`additionalCases` |  `object (`[ConditionalCases](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment#ConditionalCases)`)` Additional cases to be evaluated.  
End of mutually exclusive fields.  
  
## GeneratorSettings

Generator settings used by the LLM to generate a text response.

JSON representation  
---  
      
    
    {
      "generator": string,
      "inputParameters": {
        string: string,
        ...
      },
      "outputParameter": string
    }  
  
Fields  
---  
`generator` |  `string` Required. The generator to call. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/generators/<GeneratorID>`.  
`inputParameters` |  `map (key: string, value: string)` Map from [placeholder parameter][Generator.Parameter.id] in the `[Generator](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.generators#Generator)` to corresponding session parameters. By default, Dialogflow uses the session parameter with the same name to fill in the generator template. e.g. If there is a placeholder parameter `city` in the Generator, Dialogflow default to fill in the `$city` with `$session.params.city`. However, you may choose to fill `$city` with `$session.params.desination-city`. - Map key: [parameter ID][Genrator.Parameter.id] - Map value: session parameter nameAn object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`outputParameter` |  `string` Required. Output parameter which should contain the generator response.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-24 UTC."],[],[]] 
