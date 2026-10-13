---
url: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents
title: REST Resource: projects.agent.intents \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:32:09.194552+00:00
---

# REST Resource: projects.agent.intents  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/es/docs/reference)



Send feedback 

#  REST Resource: projects.agent.intents Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Intent
    * JSON representation
    * WebhookState
    * TrainingPhrase
      * JSON representation
    * Type
    * Part
      * JSON representation
    * Parameter
      * JSON representation
    * Message
      * JSON representation
    * Text
      * JSON representation
    * Image
      * JSON representation
    * QuickReplies
      * JSON representation
    * Card
      * JSON representation
    * Button
      * JSON representation
    * SimpleResponses
      * JSON representation
    * SimpleResponse
      * JSON representation
    * BasicCard
      * JSON representation
    * Button
      * JSON representation
    * OpenUriAction
      * JSON representation
    * Suggestions
      * JSON representation
    * Suggestion
      * JSON representation
    * LinkOutSuggestion
      * JSON representation
    * ListSelect
      * JSON representation
    * Item
      * JSON representation
    * SelectItemInfo
      * JSON representation
    * CarouselSelect
      * JSON representation
    * Item
      * JSON representation
    * BrowseCarouselCard
      * JSON representation
    * BrowseCarouselCardItem
      * JSON representation
    * OpenUrlAction
      * JSON representation
    * UrlTypeHint
    * ImageDisplayOptions
    * TableCard
      * JSON representation
    * ColumnProperties
      * JSON representation
    * HorizontalAlignment
    * TableCardRow
      * JSON representation
    * TableCardCell
      * JSON representation
    * MediaContent
      * JSON representation
    * ResponseMediaType
    * ResponseMediaObject
      * JSON representation
    * Platform
    * FollowupIntentInfo
      * JSON representation
  * Methods



## Resource: Intent

An intent categorizes an end-user's intention for one conversation turn. For each agent, you define many intents, where your combined intents can handle a complete conversation. When an end-user writes or says something, referred to as an end-user expression or end-user input, Dialogflow matches the end-user input to the best intent in your agent. Matching an intent is also known as intent classification.

For more information, see the [intent guide](https://cloud.google.com/dialogflow/docs/intents-overview).

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "webhookState": enum ([WebhookState](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.WebhookState)),
      "priority": integer,
      "isFallback": boolean,
      "mlDisabled": boolean,
      "liveAgentHandoff": boolean,
      "endInteraction": boolean,
      "inputContextNames": [
        string
      ],
      "events": [
        string
      ],
      "trainingPhrases": [
        {
          object ([TrainingPhrase](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.TrainingPhrase))
        }
      ],
      "action": string,
      "outputContexts": [
        {
          object ([Context](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.environments.users.sessions.contexts#Context))
        }
      ],
      "resetContexts": boolean,
      "parameters": [
        {
          object ([Parameter](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.Parameter))
        }
      ],
      "messages": [
        {
          object ([Message](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.Message))
        }
      ],
      "defaultResponsePlatforms": [
        enum ([Platform](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.Platform))
      ],
      "rootFollowupIntentName": string,
      "parentFollowupIntentName": string,
      "followupIntentInfo": [
        {
          object ([FollowupIntentInfo](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.FollowupIntentInfo))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Optional. The unique identifier of this intent. Required for `[Intents.UpdateIntent](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents/patch#google.cloud.dialogflow.v2.Intents.UpdateIntent)` and `[Intents.BatchUpdateIntents](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents/batchUpdate#google.cloud.dialogflow.v2.Intents.BatchUpdateIntents)` methods. Format: `projects/<Project ID>/agent/intents/<Intent ID>`.  
`displayName` |  `string` Required. The name of this intent.  
`webhookState` |  `enum (`[WebhookState](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.WebhookState)`)` Optional. Indicates whether webhooks are enabled for the intent.  
`priority` |  `integer` Optional. The priority of this intent. Higher numbers represent higher priorities.

  * If the supplied value is unspecified or 0, the service translates the value to 500,000, which corresponds to the `Normal` priority in the console.
  * If the supplied value is negative, the intent is ignored in runtime detect intent requests.

  
`isFallback` |  `boolean` Optional. Indicates whether this is a fallback intent.  
`mlDisabled` |  `boolean` Optional. Indicates whether Machine Learning is disabled for the intent. Note: If `mlDisabled` setting is set to true, then this intent is not taken into account during inference in `ML ONLY` match mode. Also, auto-markup in the UI is turned off.  
`liveAgentHandoff` |  `boolean` Optional. Indicates that a live agent should be brought in to handle the interaction with the user. In most cases, when you set this flag to true, you would also want to set endInteraction to true as well. Default is false.  
`endInteraction` |  `boolean` Optional. Indicates that this intent ends an interaction. Some integrations (e.g., Actions on Google or Dialogflow phone gateway) use this information to close interaction with an end user. Default is false.  
`inputContextNames[]` |  `string` Optional. The list of context names required for this intent to be triggered. Format: `projects/<Project ID>/agent/sessions/-/contexts/<Context ID>`.  
`events[]` |  `string` Optional. The collection of event names that trigger the intent. If the collection of input contexts is not empty, all of the contexts must be present in the active user session for an event to trigger this intent. Event names are limited to 150 characters.  
`trainingPhrases[]` |  `object (`[TrainingPhrase](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.TrainingPhrase)`)` Optional. The collection of examples that the agent is trained on.  
`action` |  `string` Optional. The name of the action associated with the intent. Note: The action name must not contain whitespaces.  
`outputContexts[]` |  `object (`[Context](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.environments.users.sessions.contexts#Context)`)` Optional. The collection of contexts that are activated when the intent is matched. Context messages in this collection should not set the parameters field. Setting the `lifespanCount` to 0 will reset the context when the intent is matched. Format: `projects/<Project ID>/agent/sessions/-/contexts/<Context ID>`.  
`resetContexts` |  `boolean` Optional. Indicates whether to delete all contexts in the current session when this intent is matched.  
`parameters[]` |  `object (`[Parameter](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.Parameter)`)` Optional. The collection of parameters associated with the intent.  
`messages[]` |  `object (`[Message](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.Message)`)` Optional. The collection of rich messages corresponding to the `Response` field in the Dialogflow console.  
`defaultResponsePlatforms[]` |  `enum (`[Platform](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.Platform)`)` Optional. The list of platforms for which the first responses will be copied from the messages in PLATFORM_UNSPECIFIED (i.e. default platform).  
`rootFollowupIntentName` |  `string` Output only. Read-only. The unique identifier of the root intent in the chain of followup intents. It identifies the correct followup intents chain for this intent. We populate this field only in the output.Format: `projects/<Project ID>/agent/intents/<Intent ID>`.  
`parentFollowupIntentName` |  `string` Read-only after creation. The unique identifier of the parent intent in the chain of followup intents. You can set this field when creating an intent, for example with `[intents.create](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents/create#google.cloud.dialogflow.v2.Intents.CreateIntent)` or `[intents.batchUpdate](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents/batchUpdate#google.cloud.dialogflow.v2.Intents.BatchUpdateIntents)`, in order to make this intent a followup intent.It identifies the parent followup intent. Format: `projects/<Project ID>/agent/intents/<Intent ID>`.  
`followupIntentInfo[]` |  `object (`[FollowupIntentInfo](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.FollowupIntentInfo)`)` Output only. Read-only. Information about all followup intents that have this intent as a direct or indirect parent. We populate this field only in the output.  
  
### WebhookState

Represents the different states that webhooks can be in.

Enums  
---  
`WEBHOOK_STATE_UNSPECIFIED` | Webhook is disabled in the agent and in the intent.  
`WEBHOOK_STATE_ENABLED` | Webhook is enabled in the agent and in the intent.  
`WEBHOOK_STATE_ENABLED_FOR_SLOT_FILLING` | Webhook is enabled in the agent and in the intent. Also, each slot filling prompt is forwarded to the webhook.  
  
### TrainingPhrase

Represents an example that the agent is trained on.

JSON representation  
---  
      
    
    {
      "name": string,
      "type": enum ([Type](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.Type)),
      "parts": [
        {
          object ([Part](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.Part))
        }
      ],
      "timesAddedCount": integer
    }  
  
Fields  
---  
`name` |  `string` Output only. The unique identifier of this training phrase.  
`type` |  `enum (`[Type](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.Type)`)` Required. The type of the training phrase.  
`parts[]` |  `object (`[Part](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.Part)`)` Required. The ordered list of training phrase parts. The parts are concatenated in order to form the training phrase.Note: The API does not automatically annotate training phrases like the Dialogflow Console does.Note: Do not forget to include whitespace at part boundaries, so the training phrase is well formatted when the parts are concatenated.If the training phrase does not need to be annotated with parameters, you just need a single part with only the `[Part.text](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.Part.FIELDS.text)` field set.If you want to annotate the training phrase, you must create multiple parts, where the fields of each part are populated in one of two ways:

  * `Part.text` is set to a part of the phrase that has no parameters.
  * `Part.text` is set to a part of the phrase that you want to annotate, and the `entityType`, `alias`, and `userDefined` fields are all set.

  
`timesAddedCount` |  `integer` Optional. Indicates how many times this example was added to the intent. Each time a developer adds an existing sample by editing an intent or training, this counter is increased.  
  
### Type

Represents different types of training phrases.

Enums  
---  
`TYPE_UNSPECIFIED` | Not specified. This value should never be used.  
`EXAMPLE` | Examples do not contain @-prefixed entity type names, but example parts can be annotated with entity types.  
`TEMPLATE` | Templates are not annotated with entity types, but they can contain @-prefixed entity type names as substrings. Template mode has been deprecated. Example mode is the only supported way to create new training phrases. If you have existing training phrases that you've created in template mode, those will continue to work.This item is deprecated!  
  
### Part

Represents a part of a training phrase.

JSON representation  
---  
      
    
    {
      "text": string,
      "entityType": string,
      "alias": string,
      "userDefined": boolean
    }  
  
Fields  
---  
`text` |  `string` Required. The text for this part.  
`entityType` |  `string` Optional. The entity type name prefixed with `@`. This field is required for annotated parts of the training phrase.  
`alias` |  `string` Optional. The parameter name for the value extracted from the annotated part of the example. This field is required for annotated parts of the training phrase.  
`userDefined` |  `boolean` Optional. Indicates whether the text was manually annotated. This field is set to true when the Dialogflow Console is used to manually annotate the part. When creating an annotated part with the API, you must set this to true.  
  
### Parameter

Represents intent parameters.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "value": string,
      "defaultValue": string,
      "entityTypeDisplayName": string,
      "mandatory": boolean,
      "prompts": [
        string
      ],
      "isList": boolean
    }  
  
Fields  
---  
`name` |  `string` The unique identifier of this parameter.  
`displayName` |  `string` Required. The name of the parameter.  
`value` |  `string` Optional. The definition of the parameter value. It can be:

  * a constant string,
  * a parameter value defined as `$parameter_name`,
  * an original parameter value defined as `$parameter_name.original`,
  * a parameter value from some context defined as `#context_name.parameter_name`.

  
`defaultValue` |  `string` Optional. The default value to use when the `value` yields an empty result. Default values can be extracted from contexts by using the following syntax: `#context_name.parameter_name`.  
`entityTypeDisplayName` |  `string` Optional. The name of the entity type, prefixed with `@`, that describes values of the parameter. If the parameter is required, this must be provided.  
`mandatory` |  `boolean` Optional. Indicates whether the parameter is required. That is, whether the intent cannot be completed without collecting the parameter value.  
`prompts[]` |  `string` Optional. The collection of prompts that the agent can present to the user in order to collect a value for the parameter.  
`isList` |  `boolean` Optional. Indicates whether the parameter represents a list of values.  
  
### Message

A rich response message. Corresponds to the intent `Response` field in the Dialogflow console. For more information, see [Rich response messages](https://cloud.google.com/dialogflow/docs/intents-rich-messages).

JSON representation  
---  
      
    
    {
      "platform": enum ([Platform](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.Platform)),
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "text": {
        object ([Text](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.Text))
      },
      "image": {
        object ([Image](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.Image))
      },
      "quickReplies": {
        object ([QuickReplies](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.QuickReplies))
      },
      "card": {
        object ([Card](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.Card))
      },
      "payload": {
        object
      },
      "simpleResponses": {
        object ([SimpleResponses](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.SimpleResponses))
      },
      "basicCard": {
        object ([BasicCard](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.BasicCard))
      },
      "suggestions": {
        object ([Suggestions](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.Suggestions))
      },
      "linkOutSuggestion": {
        object ([LinkOutSuggestion](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.LinkOutSuggestion))
      },
      "listSelect": {
        object ([ListSelect](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.ListSelect))
      },
      "carouselSelect": {
        object ([CarouselSelect](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.CarouselSelect))
      },
      "browseCarouselCard": {
        object ([BrowseCarouselCard](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.BrowseCarouselCard))
      },
      "tableCard": {
        object ([TableCard](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.TableCard))
      },
      "mediaContent": {
        object ([MediaContent](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.MediaContent))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`platform` |  `enum (`[Platform](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.Platform)`)` Optional. The platform that this message is intended for.  
Required. The rich response message. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`text` |  `object (`[Text](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.Text)`)` The text response.  
`image` |  `object (`[Image](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.Image)`)` The image response.  
`quickReplies` |  `object (`[QuickReplies](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.QuickReplies)`)` The quick replies response.  
`card` |  `object (`[Card](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.Card)`)` The card response.  
`payload` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` A custom platform-specific response.  
`simpleResponses` |  `object (`[SimpleResponses](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.SimpleResponses)`)` The voice and text-only responses for Actions on Google.  
`basicCard` |  `object (`[BasicCard](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.BasicCard)`)` The basic card response for Actions on Google.  
`suggestions` |  `object (`[Suggestions](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.Suggestions)`)` The suggestion chips for Actions on Google.  
`linkOutSuggestion` |  `object (`[LinkOutSuggestion](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.LinkOutSuggestion)`)` The link out suggestion chip for Actions on Google.  
`listSelect` |  `object (`[ListSelect](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.ListSelect)`)` The list card response for Actions on Google.  
`carouselSelect` |  `object (`[CarouselSelect](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.CarouselSelect)`)` The carousel card response for Actions on Google.  
`browseCarouselCard` |  `object (`[BrowseCarouselCard](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.BrowseCarouselCard)`)` Browse carousel card for Actions on Google.  
`tableCard` |  `object (`[TableCard](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.TableCard)`)` Table card for Actions on Google.  
`mediaContent` |  `object (`[MediaContent](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.MediaContent)`)` The media content card for Actions on Google.  
End of mutually exclusive fields.  
  
### Text

The text response message.

JSON representation  
---  
      
    
    {
      "text": [
        string
      ]
    }  
  
Fields  
---  
`text[]` |  `string` Optional. The collection of the agent's responses.  
  
### Image

The image response message.

JSON representation  
---  
      
    
    {
      "imageUri": string,
      "accessibilityText": string
    }  
  
Fields  
---  
`imageUri` |  `string` Optional. The public URI to an image file.  
`accessibilityText` |  `string` Optional. A text description of the image to be used for accessibility, e.g., screen readers.  
  
### QuickReplies

The quick replies response message.

JSON representation  
---  
      
    
    {
      "title": string,
      "quickReplies": [
        string
      ]
    }  
  
Fields  
---  
`title` |  `string` Optional. The title of the collection of quick replies.  
`quickReplies[]` |  `string` Optional. The collection of quick replies.  
  
### Card

The card response message.

JSON representation  
---  
      
    
    {
      "title": string,
      "subtitle": string,
      "imageUri": string,
      "buttons": [
        {
          object ([Button](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.Button))
        }
      ]
    }  
  
Fields  
---  
`title` |  `string` Optional. The title of the card.  
`subtitle` |  `string` Optional. The subtitle of the card.  
`imageUri` |  `string` Optional. The public URI to an image file for the card.  
`buttons[]` |  `object (`[Button](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.Button)`)` Optional. The collection of card buttons.  
  
### Button

Contains information about a button.

JSON representation  
---  
      
    
    {
      "text": string,
      "postback": string
    }  
  
Fields  
---  
`text` |  `string` Optional. The text to show on the button.  
`postback` |  `string` Optional. The text to send back to the Dialogflow API or a URI to open.  
  
### SimpleResponses

The collection of simple response candidates. This message in `QueryResult.fulfillment_messages` and `WebhookResponse.fulfillment_messages` should contain only one `SimpleResponse`.

JSON representation  
---  
      
    
    {
      "simpleResponses": [
        {
          object ([SimpleResponse](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.SimpleResponse))
        }
      ]
    }  
  
Fields  
---  
`simpleResponses[]` |  `object (`[SimpleResponse](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.SimpleResponse)`)` Required. The list of simple responses.  
  
### SimpleResponse

The simple response message containing speech or text.

JSON representation  
---  
      
    
    {
      "textToSpeech": string,
      "ssml": string,
      "displayText": string
    }  
  
Fields  
---  
`textToSpeech` |  `string` One of textToSpeech or ssml must be provided. The plain text of the speech output. Mutually exclusive with ssml.  
`ssml` |  `string` One of textToSpeech or ssml must be provided. Structured spoken response to the user in the SSML format. Mutually exclusive with textToSpeech.  
`displayText` |  `string` Optional. The text to display.  
  
### BasicCard

The basic card message. Useful for displaying information.

JSON representation  
---  
      
    
    {
      "title": string,
      "subtitle": string,
      "formattedText": string,
      "image": {
        object ([Image](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.Image))
      },
      "buttons": [
        {
          object ([Button](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.Button_1))
        }
      ]
    }  
  
Fields  
---  
`title` |  `string` Optional. The title of the card.  
`subtitle` |  `string` Optional. The subtitle of the card.  
`formattedText` |  `string` Required, unless image is present. The body text of the card.  
`image` |  `object (`[Image](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.Image)`)` Optional. The image for the card.  
`buttons[]` |  `object (`[Button](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.Button_1)`)` Optional. The collection of card buttons.  
  
### Button

The button object that appears at the bottom of a card.

JSON representation  
---  
      
    
    {
      "title": string,
      "openUriAction": {
        object ([OpenUriAction](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.OpenUriAction))
      }
    }  
  
Fields  
---  
`title` |  `string` Required. The title of the button.  
`openUriAction` |  `object (`[OpenUriAction](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.OpenUriAction)`)` Required. Action to take when a user taps on the button.  
  
### OpenUriAction

Opens the given URI.

JSON representation  
---  
      
    
    {
      "uri": string
    }  
  
Fields  
---  
`uri` |  `string` Required. The HTTP or HTTPS scheme URI.  
  
### Suggestions

The collection of suggestions.

JSON representation  
---  
      
    
    {
      "suggestions": [
        {
          object ([Suggestion](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.Suggestion))
        }
      ]
    }  
  
Fields  
---  
`suggestions[]` |  `object (`[Suggestion](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.Suggestion)`)` Required. The list of suggested replies.  
  
### Suggestion

The suggestion chip message that the user can tap to quickly post a reply to the conversation.

JSON representation  
---  
      
    
    {
      "title": string
    }  
  
Fields  
---  
`title` |  `string` Required. The text shown the in the suggestion chip.  
  
### LinkOutSuggestion

The suggestion chip message that allows the user to jump out to the app or website associated with this agent.

JSON representation  
---  
      
    
    {
      "destinationName": string,
      "uri": string
    }  
  
Fields  
---  
`destinationName` |  `string` Required. The name of the app or site this chip is linking to.  
`uri` |  `string` Required. The URI of the app or site to open when the user taps the suggestion chip.  
  
### ListSelect

The card for presenting a list of options to select from.

JSON representation  
---  
      
    
    {
      "title": string,
      "items": [
        {
          object ([Item](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.Item))
        }
      ],
      "subtitle": string
    }  
  
Fields  
---  
`title` |  `string` Optional. The overall title of the list.  
`items[]` |  `object (`[Item](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.Item)`)` Required. List items.  
`subtitle` |  `string` Optional. Subtitle of the list.  
  
### Item

An item in the list.

JSON representation  
---  
      
    
    {
      "info": {
        object ([SelectItemInfo](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.SelectItemInfo))
      },
      "title": string,
      "description": string,
      "image": {
        object ([Image](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.Image))
      }
    }  
  
Fields  
---  
`info` |  `object (`[SelectItemInfo](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.SelectItemInfo)`)` Required. Additional information about this option.  
`title` |  `string` Required. The title of the list item.  
`description` |  `string` Optional. The main text describing the item.  
`image` |  `object (`[Image](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.Image)`)` Optional. The image to display.  
  
### SelectItemInfo

Additional info about the select item for when it is triggered in a dialog.

JSON representation  
---  
      
    
    {
      "key": string,
      "synonyms": [
        string
      ]
    }  
  
Fields  
---  
`key` |  `string` Required. A unique key that will be sent back to the agent if this response is given.  
`synonyms[]` |  `string` Optional. A list of synonyms that can also be used to trigger this item in dialog.  
  
### CarouselSelect

The card for presenting a carousel of options to select from.

JSON representation  
---  
      
    
    {
      "items": [
        {
          object ([Item](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.Item_1))
        }
      ]
    }  
  
Fields  
---  
`items[]` |  `object (`[Item](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.Item_1)`)` Required. Carousel items.  
  
### Item

An item in the carousel.

JSON representation  
---  
      
    
    {
      "info": {
        object ([SelectItemInfo](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.SelectItemInfo))
      },
      "title": string,
      "description": string,
      "image": {
        object ([Image](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.Image))
      }
    }  
  
Fields  
---  
`info` |  `object (`[SelectItemInfo](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.SelectItemInfo)`)` Required. Additional info about the option item.  
`title` |  `string` Required. Title of the carousel item.  
`description` |  `string` Optional. The body text of the card.  
`image` |  `object (`[Image](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.Image)`)` Optional. The image to display.  
  
### BrowseCarouselCard

Browse Carousel Card for Actions on Google. <https://developers.google.com/actions/assistant/responses#browsing_carousel>

JSON representation  
---  
      
    
    {
      "items": [
        {
          object ([BrowseCarouselCardItem](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.BrowseCarouselCardItem))
        }
      ],
      "imageDisplayOptions": enum ([ImageDisplayOptions](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.ImageDisplayOptions))
    }  
  
Fields  
---  
`items[]` |  `object (`[BrowseCarouselCardItem](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.BrowseCarouselCardItem)`)` Required. List of items in the Browse Carousel Card. Minimum of two items, maximum of ten.  
`imageDisplayOptions` |  `enum (`[ImageDisplayOptions](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.ImageDisplayOptions)`)` Optional. Settings for displaying the image. Applies to every image in `[items](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.BrowseCarouselCard.FIELDS.items)`.  
  
### BrowseCarouselCardItem

Browsing carousel tile

JSON representation  
---  
      
    
    {
      "openUriAction": {
        object ([OpenUrlAction](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.OpenUrlAction))
      },
      "title": string,
      "description": string,
      "image": {
        object ([Image](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.Image))
      },
      "footer": string
    }  
  
Fields  
---  
`openUriAction` |  `object (`[OpenUrlAction](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.OpenUrlAction)`)` Required. Action to present to the user.  
`title` |  `string` Required. Title of the carousel item. Maximum of two lines of text.  
`description` |  `string` Optional. Description of the carousel item. Maximum of four lines of text.  
`image` |  `object (`[Image](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.Image)`)` Optional. Hero image for the carousel item.  
`footer` |  `string` Optional. Text that appears at the bottom of the Browse Carousel Card. Maximum of one line of text.  
  
### OpenUrlAction

Actions on Google action to open a given url.

JSON representation  
---  
      
    
    {
      "url": string,
      "urlTypeHint": enum ([UrlTypeHint](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.UrlTypeHint))
    }  
  
Fields  
---  
`url` |  `string` Required. URL  
`urlTypeHint` |  `enum (`[UrlTypeHint](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.UrlTypeHint)`)` Optional. Specifies the type of viewer that is used when opening the URL. Defaults to opening via web browser.  
  
### UrlTypeHint

Type of the URI.

Enums  
---  
`URL_TYPE_HINT_UNSPECIFIED` | Unspecified  
`AMP_ACTION` | Url would be an amp action  
`AMP_CONTENT` | URL that points directly to AMP content, or to a canonical URL which refers to AMP content via .  
  
### ImageDisplayOptions

Image display options for Actions on Google. This should be used for when the image's aspect ratio does not match the image container's aspect ratio.

Enums  
---  
`IMAGE_DISPLAY_OPTIONS_UNSPECIFIED` | Fill the gaps between the image and the image container with gray bars.  
`GRAY` | Fill the gaps between the image and the image container with gray bars.  
`WHITE` | Fill the gaps between the image and the image container with white bars.  
`CROPPED` | Image is scaled such that the image width and height match or exceed the container dimensions. This may crop the top and bottom of the image if the scaled image height is greater than the container height, or crop the left and right of the image if the scaled image width is greater than the container width. This is similar to "Zoom Mode" on a widescreen TV when playing a 4:3 video.  
`BLURRED_BACKGROUND` | Pad the gaps between image and image frame with a blurred copy of the same image.  
  
### TableCard

Table card for Actions on Google.

JSON representation  
---  
      
    
    {
      "title": string,
      "subtitle": string,
      "image": {
        object ([Image](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.Image))
      },
      "columnProperties": [
        {
          object ([ColumnProperties](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.ColumnProperties))
        }
      ],
      "rows": [
        {
          object ([TableCardRow](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.TableCardRow))
        }
      ],
      "buttons": [
        {
          object ([Button](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.Button_1))
        }
      ]
    }  
  
Fields  
---  
`title` |  `string` Required. Title of the card.  
`subtitle` |  `string` Optional. Subtitle to the title.  
`image` |  `object (`[Image](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.Image)`)` Optional. Image which should be displayed on the card.  
`columnProperties[]` |  `object (`[ColumnProperties](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.ColumnProperties)`)` Optional. Display properties for the columns in this table.  
`rows[]` |  `object (`[TableCardRow](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.TableCardRow)`)` Optional. Rows in this table of data.  
`buttons[]` |  `object (`[Button](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.Button_1)`)` Optional. List of buttons for the card.  
  
### ColumnProperties

Column properties for `[TableCard](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.TableCard)`.

JSON representation  
---  
      
    
    {
      "header": string,
      "horizontalAlignment": enum ([HorizontalAlignment](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.HorizontalAlignment))
    }  
  
Fields  
---  
`header` |  `string` Required. Column heading.  
`horizontalAlignment` |  `enum (`[HorizontalAlignment](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.HorizontalAlignment)`)` Optional. Defines text alignment for all cells in this column.  
  
### HorizontalAlignment

Text alignments within a cell.

Enums  
---  
`HORIZONTAL_ALIGNMENT_UNSPECIFIED` | Text is aligned to the leading edge of the column.  
`LEADING` | Text is aligned to the leading edge of the column.  
`CENTER` | Text is centered in the column.  
`TRAILING` | Text is aligned to the trailing edge of the column.  
  
### TableCardRow

Row of `[TableCard](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.TableCard)`.

JSON representation  
---  
      
    
    {
      "cells": [
        {
          object ([TableCardCell](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.TableCardCell))
        }
      ],
      "dividerAfter": boolean
    }  
  
Fields  
---  
`cells[]` |  `object (`[TableCardCell](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.TableCardCell)`)` Optional. List of cells that make up this row.  
`dividerAfter` |  `boolean` Optional. Whether to add a visual divider after this row.  
  
### TableCardCell

Cell of `[TableCardRow](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.TableCardRow)`.

JSON representation  
---  
      
    
    {
      "text": string
    }  
  
Fields  
---  
`text` |  `string` Required. Text in this cell.  
  
### MediaContent

The media content card for Actions on Google.

JSON representation  
---  
      
    
    {
      "mediaType": enum ([ResponseMediaType](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.ResponseMediaType)),
      "mediaObjects": [
        {
          object ([ResponseMediaObject](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.ResponseMediaObject))
        }
      ]
    }  
  
Fields  
---  
`mediaType` |  `enum (`[ResponseMediaType](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.ResponseMediaType)`)` Optional. What type of media is the content (ie "audio").  
`mediaObjects[]` |  `object (`[ResponseMediaObject](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.ResponseMediaObject)`)` Required. List of media objects.  
  
### ResponseMediaType

Format of response media type.

Enums  
---  
`RESPONSE_MEDIA_TYPE_UNSPECIFIED` | Unspecified.  
`AUDIO` | Response media type is audio.  
  
### ResponseMediaObject

Response media object for media content card.

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "contentUrl": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "largeImage": {
        object ([Image](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.Image))
      },
      "icon": {
        object ([Image](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.Image))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`name` |  `string` Required. Name of media card.  
`description` |  `string` Optional. Description of media card.  
`contentUrl` |  `string` Required. Url where the media is stored.  
Image to show with the media card. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`largeImage` |  `object (`[Image](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.Image)`)` Optional. Image to display above media content.  
`icon` |  `object (`[Image](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent.Image)`)` Optional. Icon to display above media content.  
End of mutually exclusive fields.  
  
### Platform

The rich response message integration platform. See [Integrations](https://cloud.google.com/dialogflow/docs/integrations).

Enums  
---  
`PLATFORM_UNSPECIFIED` | Default platform.  
`FACEBOOK` | Facebook.  
`SLACK` | Slack.  
`TELEGRAM` | Telegram.  
`KIK` | Kik.  
`SKYPE` | Skype.  
`LINE` | Line.  
`VIBER` | Viber.  
`ACTIONS_ON_GOOGLE` | Google Assistant See [Dialogflow webhook format](https://developers.google.com/assistant/actions/build/json/dialogflow-webhook-json)  
`GOOGLE_HANGOUTS` | Google Hangouts.  
  
### FollowupIntentInfo

Represents a single followup intent in the chain.

JSON representation  
---  
      
    
    {
      "followupIntentName": string,
      "parentFollowupIntentName": string
    }  
  
Fields  
---  
`followupIntentName` |  `string` The unique identifier of the followup intent. Format: `projects/<Project ID>/agent/intents/<Intent ID>`.  
`parentFollowupIntentName` |  `string` The unique identifier of the followup intent's parent. Format: `projects/<Project ID>/agent/intents/<Intent ID>`.  
  
## Methods  
  
---  
  
### `[batchDelete](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents/batchDelete)`

|  Deletes intents in the specified agent.  
  
### `[batchUpdate](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents/batchUpdate)`

|  Updates/Creates multiple intents in the specified agent.  
  
### `[create](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents/create)`

|  Creates an intent in the specified agent.  
  
### `[delete](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents/delete)`

|  Deletes the specified intent and its direct or indirect followup intents.  
  
### `[get](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents/get)`

|  Retrieves the specified intent.  
  
### `[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents/list)`

|  Returns the list of all intents in the specified agent.  
  
### `[patch](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents/patch)`

|  Updates the specified intent.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-24 UTC."],[],[]] 
