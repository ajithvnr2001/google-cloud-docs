---
url: https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder/
title: Method: projects.locations.sessions.processOrder \u00a0|\u00a0 Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:38:11.267311+00:00
---

# Method: projects.locations.sessions.processOrder  |  Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Food AI ](https://docs.cloud.google.com/food-ai)
  * [ Reference ](https://docs.cloud.google.com/food-ai/apis)



Send feedback 

#  Method: projects.locations.sessions.processOrder Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
      * JSON representation
      * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * TextInput
    * JSON representation
  * AudioInput
    * JSON representation
  * EventInput
    * JSON representation
  * DriveOffEvent
    * JSON representation
  * CrewInterjectionEvent
    * JSON representation
  * OrderStateUpdateEvent
    * JSON representation
  * ClientEscalationEvent
    * JSON representation
  * CallerHangupEvent
  * PosErrorEvent
    * JSON representation
  * ClientExecutionResult
    * JSON representation
  * FinalizeOrderResponse
    * JSON representation
  * PaymentInfo
    * JSON representation
  * PaymentMethod
  * OrderPricesResponse
    * JSON representation
  * ValidateDeliveryAddressResponse
    * JSON representation
  * OrderStatusResponse
    * JSON representation
  * Blob
    * JSON representation
  * Config
    * JSON representation
  * FeatureGate
    * JSON representation
  * ClientAppInfo
    * JSON representation
  * SessionMode
  * TurnType
  * BidiProcessOrderResponse
    * JSON representation
  * AgentAudio
    * JSON representation
  * SpeechRecognition
    * JSON representation
  * InterruptionSignal
  * AgentEvent
    * JSON representation
  * RestartOrder
    * JSON representation
  * ClientExecutionRequest
    * JSON representation
  * FinalizeOrderRequest
  * SubmitOrderRequest
    * JSON representation
  * LoyaltyInfo
    * JSON representation
  * LoyaltyAmount
    * JSON representation
  * OrderPricesRequest
    * JSON representation
  * ValidateDeliveryAddressRequest
    * JSON representation
  * OrderStatusRequest
  * UpdatedOrderState
    * JSON representation
  * AgentText
    * JSON representation
  * SuggestedOptions
    * JSON representation
  * SuggestedItems
    * JSON representation
  * SuggestedItem
    * JSON representation
  * SuggestedModifiers
    * JSON representation
  * SuggestedModifier
    * JSON representation
  * SuggestedModifierGroups
    * JSON representation
  * SuggestedModGroup
    * JSON representation
  * SentimentMeasurement
    * JSON representation
  * TurnCompleted
  * EndSession
    * JSON representation
  * EndType



Performs a single turn logic to process user input and return the result.

### HTTP request

`POST https://foodorderingaiagent.googleapis.com/v1/{config.session=projects/*/locations/*/sessions/*}:processOrder`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`config.session` |  `string` Required. The session for the order. Format: `projects/{project}/locations/{location}/sessions/{session}`  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "config": {
        "session": string,
        "store": string,
        "laneId": string,
        "enableEchoCancellation": boolean,
        "daypartId": string,
        "featureGate": {
          "menuResponseEnabled": boolean,
          "updatedOrderStateEnabled": boolean,
          "enableOrderStatusRetrieval": boolean
        },
        "clientAppInfo": {
          "deviceModel": string,
          "osVersion": string,
          "sdkVersion": string
        },
        "mode": enum ([SessionMode](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#SessionMode)),
        "channelType": enum ([ChannelType](https://docs.cloud.google.com/food-ai/reference/rest/v1/ChannelType)),
        "enableListenOnlyDualChannel": boolean,
        "testSessionStartTime": string
      },
      "turnType": enum ([TurnType](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#TurnType)),
    
      // Union field input can be only one of the following:
      "textInput": {
        object ([TextInput](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#TextInput))
      },
      "audioInput": {
        object ([AudioInput](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#AudioInput))
      },
      "eventInput": {
        object ([EventInput](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#EventInput))
      },
      "clientExecutionResult": {
        object ([ClientExecutionResult](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#ClientExecutionResult))
      },
      "blobInput": {
        object ([Blob](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#Blob))
      }
      // End of list of possible types for union field input.
    }  
  
Fields  
---  
`config.store` |  `string` Required. The store the order is being placed for. Format: `projects/{project}/locations/{location}/brands/{brand}/stores/{store}`  
`config.laneId` |  `string` Optional. The id of a specifc drive through lane.  
`config.enableEchoCancellation` |  `boolean` Optional. Whether to enable echo cancellation for the session. If enabled, the client should provide the customerAudio and crewAudio in the AudioInput.  
`config.daypartId` |  `string` Optional. Daypart of the food menu, including breakfast, lunch, dinner, etc. This is used to determine the menu to use for the order.  
`config.featureGate` |  `object (`[FeatureGate](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#FeatureGate)`)` Optional. The feature gates for the session. This is used to enable or disable features for the session.  
`config.clientAppInfo` |  `object (`[ClientAppInfo](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#ClientAppInfo)`)` Optional. The information about the client application and device environment.  
`config.mode` |  `enum (`[SessionMode](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#SessionMode)`)` Optional. The mode of the session.  
`config.channelType` |  `enum (`[ChannelType](https://docs.cloud.google.com/food-ai/reference/rest/v1/ChannelType)`)` Optional. The type of channel used for agent communication.  
`config.enableListenOnlyDualChannel` |  `boolean` Optional. Whether to enable listen-only dual channel for the session. If enabled, the client should provide the customerAudio and crewAudio in the AudioInput, and CES will do EAC and summation on media processing server.  
`config.testSessionStartTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. The start time of the session, used for testing or evaluation purposes.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`turnType` |  `enum (`[TurnType](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#TurnType)`)` Optional. Explicit indicator of the request's position in the session lifecycle. Allows clients to deterministically control when initial session setup variables are injected.  
Union field `input`. The input from the client. `input` can be only one of the following:  
`textInput` |  `object (`[TextInput](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#TextInput)`)` The text input from the client.  
`audioInput` |  `object (`[AudioInput](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#AudioInput)`)` The audio input from the client.  
`eventInput` |  `object (`[EventInput](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#EventInput)`)` The event input from the client.  
`clientExecutionResult` |  `object (`[ClientExecutionResult](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#ClientExecutionResult)`)` The result of a client execution request.  
`blobInput` |  `object (`[Blob](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#Blob)`)` Generic binary data input. Mirrors <http://google3/google/cloud/ces/v1main/session_service.proto?l=720>  
  
### Response body

Response message for `[FoodOrderingService.ProcessOrder](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#google.cloud.foodorderingaiagent.v1.FoodOrderingService.ProcessOrder)`. Functionally contains fields from BidiProcessOrderResponse minus streaming-specific ones.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "responses": [
        {
          object ([BidiProcessOrderResponse](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#BidiProcessOrderResponse))
        }
      ]
    }  
  
Fields  
---  
`responses[]` |  `object (`[BidiProcessOrderResponse](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#BidiProcessOrderResponse)`)` Output only. List of agent responses to the request, returned in-order.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## TextInput

The text input from the client. Instead of audio, the client can alternatively send text input to the agent. A client must use either text or audio input, not both.

JSON representation  
---  
      
    
    {
      "text": string
    }  
  
Fields  
---  
`text` |  `string` Required. The text utterance from the client.  
  
## AudioInput

The audio input from the client. The input audio may have multiple channels for the customer, crew, etc. These should all be synchronized and in the format specified in the config. Audio headers should not be included. By default, the audio should be using 16-bit linear PCM audio encoding and 16000 Hz sample rate. Total bytes from all channels should be less than 25600 bytes.

JSON representation  
---  
      
    
    {
      "customerAudio": string,
      "crewAudio": string
    }  
  
Fields  
---  
`customerAudio` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Required. Customer audio data.A base64-encoded string.  
`crewAudio` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Optional. Crew audio data. This is an optional audio channel for the crew member in the same lane as the customer, and served as the reference audio for echo cancellation.A base64-encoded string.  
  
## EventInput

The event input from the client. This is used to trigger specific events within the agent.

JSON representation  
---  
      
    
    {
    
      // Union field event can be only one of the following:
      "driveOffEvent": {
        object ([DriveOffEvent](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#DriveOffEvent))
      },
      "crewInterjectionEvent": {
        object ([CrewInterjectionEvent](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#CrewInterjectionEvent))
      },
      "updateOrderStateEvent": {
        object ([OrderStateUpdateEvent](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#OrderStateUpdateEvent))
      },
      "clientEscalationEvent": {
        object ([ClientEscalationEvent](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#ClientEscalationEvent))
      },
      "callerHangupEvent": {
        object ([CallerHangupEvent](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#CallerHangupEvent))
      },
      "posErrorInput": {
        object ([PosErrorEvent](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#PosErrorEvent))
      }
      // End of list of possible types for union field event.
    }  
  
Fields  
---  
Union field `event`. Next ID: 10 The event to trigger. `event` can be only one of the following:  
`driveOffEvent` |  `object (`[DriveOffEvent](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#DriveOffEvent)`)` The drive off event.  
`crewInterjectionEvent` |  `object (`[CrewInterjectionEvent](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#CrewInterjectionEvent)`)` The crew interjection event.  
`updateOrderStateEvent` |  `object (`[OrderStateUpdateEvent](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#OrderStateUpdateEvent)`)` A client-side update to the order state.  
`clientEscalationEvent` |  `object (`[ClientEscalationEvent](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#ClientEscalationEvent)`)` A client-side escalation event.  
`callerHangupEvent` |  `object (`[CallerHangupEvent](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#CallerHangupEvent)`)` Optional. A caller hangup event.  
`posErrorInput` |  `object (`[PosErrorEvent](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#PosErrorEvent)`)` Optional. A POS error event.  
  
## DriveOffEvent

The drive off event. This indicates the customer drove off. Session will be closed after this event.

JSON representation  
---  
      
    
    {
      "reason": string
    }  
  
Fields  
---  
`reason` |  `string` Optional. The reason for drive off e.g. "order completed", "unexpected driveoff".  
  
## CrewInterjectionEvent

The crew interjection event. This indicates a crew member interjected in the session. Session will be closed after this event.

JSON representation  
---  
      
    
    {
      "mode": string
    }  
  
Fields  
---  
`mode` |  `string` Optional. The mode in which the crew member interjected, e.g. "headset", "pos".  
  
## OrderStateUpdateEvent

The update order state request. This event should be sent when the order is updated on the client side, e.g. when an item is added or removed via a traditional touch interface.

JSON representation  
---  
      
    
    {
      "order": {
        object ([Order](https://docs.cloud.google.com/food-ai/reference/rest/v1/Order))
      }
    }  
  
Fields  
---  
`order` |  `object (`[Order](https://docs.cloud.google.com/food-ai/reference/rest/v1/Order)`)` Required. The updated state of the Order associated with this session.  
  
## ClientEscalationEvent

Indicates the client is escalating the session to a human agent.

JSON representation  
---  
      
    
    {
      "reason": string
    }  
  
Fields  
---  
`reason` |  `string` Optional. The reason for client escalation e.g. "payment-declined", "pos-error", "integration-error" etc.  
  
## CallerHangupEvent

This type has no fields.

Indicates the customer hung up the call prematurely (e.g., AI aversion).

## PosErrorEvent

Point-of-Sale (POS) specific failures.

JSON representation  
---  
      
    
    {
      "errorMessages": [
        string
      ],
      "affectedItemUids": [
        string
      ],
      "affectedExternalIds": [
        string
      ],
      "metadata": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`errorMessages[]` |  `string` Optional. A list of human-readable descriptions of the errors. Multiple error messages can be provided if multiple issues occur simultaneously (e.g., multiple items are out of stock) or to provide a more detailed breakdown of a single complex failure. These messages may be used by the agent to inform the customer or for logging purposes.  
`affectedItemUids[]` |  `string` Optional. Unique item UIDs generated by the Food Ordering AI Agent that caused the error. Corresponds to `UpdatedOrderState.OrderItem.uid`.  
`affectedExternalIds[]` |  `string` Optional. List of external IDs (from the Menu) that caused the error. Should be equal to the actual representatives in the POS, which are usually under integration attributes in menu.proto (e.g., in `ItemIntegrationAttributes` or `ModifierIntegrationAttributes`).  
`metadata` |  `map (key: string, value: string)` Optional. Free-form metadata for debugging or brand-specific signaling. Can be used to pass brand-specific error codes or categories (e.g., {"BRAND_ERROR_CODE": "OUT_OF_STOCK"}).An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## ClientExecutionResult

The result of a client execution request.

JSON representation  
---  
      
    
    {
      "executionId": string,
    
      // Union field response can be only one of the following:
      "finalizeOrderResponse": {
        object ([FinalizeOrderResponse](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#FinalizeOrderResponse))
      },
      "orderPricesResponse": {
        object ([OrderPricesResponse](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#OrderPricesResponse))
      },
      "validateDeliveryAddressResponse": {
        object ([ValidateDeliveryAddressResponse](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#ValidateDeliveryAddressResponse))
      },
      "orderStatusResponse": {
        object ([OrderStatusResponse](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#OrderStatusResponse))
      }
      // End of list of possible types for union field response.
    }  
  
Fields  
---  
`executionId` |  `string` Required. The ID of the execution request this is a result for.  
Union field `response`. The specific result of the execution. `response` can be only one of the following:  
`finalizeOrderResponse` |  `object (`[FinalizeOrderResponse](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#FinalizeOrderResponse)`)` The result of finalizing the order.  
`orderPricesResponse` |  `object (`[OrderPricesResponse](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#OrderPricesResponse)`)` The result of getting the order prices.  
`validateDeliveryAddressResponse` |  `object (`[ValidateDeliveryAddressResponse](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#ValidateDeliveryAddressResponse)`)` The result of validating the delivery address.  
`orderStatusResponse` |  `object (`[OrderStatusResponse](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#OrderStatusResponse)`)` The result of getting the order status.  
  
## FinalizeOrderResponse

The result of finalizing the order.

JSON representation  
---  
      
    
    {
      "paymentFlowEnabled": boolean,
      "paymentInfo": {
        object ([PaymentInfo](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#PaymentInfo))
      },
      "totalAmountDue": {
        object ([Money](https://docs.cloud.google.com/food-ai/reference/rest/Shared.Types/Money))
      },
      "orderPriceInfo": {
        object ([OrderPriceInfo](https://docs.cloud.google.com/food-ai/reference/rest/v1/Order#OrderPriceInfo))
      }
    }  
  
Fields  
---  
`paymentFlowEnabled` |  `boolean` Optional. Whether to enable the payment handling flow in the agent.  
`paymentInfo` |  `object (`[PaymentInfo](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#PaymentInfo)`)` Optional. The payment information of the customer. No-op if paymentFlowEnabled is false.  
`totalAmountDue` |  `object (`[Money](https://docs.cloud.google.com/food-ai/reference/rest/Shared.Types/Money)`)` Optional. The total amount due for the order.  
`orderPriceInfo` |  `object (`[OrderPriceInfo](https://docs.cloud.google.com/food-ai/reference/rest/v1/Order#OrderPriceInfo)`)` Optional. The detailed price information of the order.  
  
## PaymentInfo

Payment information of the user.

JSON representation  
---  
      
    
    {
      "creditCardLastFourDigits": string,
      "creditCardCvv": string,
      "paymentMethod": enum ([PaymentMethod](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#PaymentMethod))
    }  
  
Fields  
---  
`creditCardLastFourDigits` |  `string` Optional. The last four digits of the credit card. This is used to verify the credit card number at the payment stage.  
`creditCardCvv` |  `string` Optional. CVV of the credit card.  
`paymentMethod` |  `enum (`[PaymentMethod](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#PaymentMethod)`)` Optional. The type of payment method used.  
  
## PaymentMethod

The type of payment method.

Enums  
---  
`PAYMENT_METHOD_UNSPECIFIED` | Unspecified payment method.  
`PAYMENT_METHOD_CREDIT_CARD` | Credit card.  
`PAYMENT_METHOD_CASH` | Cash.  
  
## OrderPricesResponse

The result of getting the order prices.

JSON representation  
---  
      
    
    {
      "success": boolean,
      "orderPriceInfo": {
        object ([OrderPriceInfo](https://docs.cloud.google.com/food-ai/reference/rest/v1/Order#OrderPriceInfo))
      }
    }  
  
Fields  
---  
`success` |  `boolean` Required. Whether the order prices were successfully retrieved.  
`orderPriceInfo` |  `object (`[OrderPriceInfo](https://docs.cloud.google.com/food-ai/reference/rest/v1/Order#OrderPriceInfo)`)` Optional. Total order price after all discounts, fees, taxes, etc  
  
## ValidateDeliveryAddressResponse

The result of validating a delivery address.

JSON representation  
---  
      
    
    {
      "success": boolean,
      "validationStatus": enum ([ValidationStatus](https://docs.cloud.google.com/food-ai/reference/rest/v1/Order#ValidationStatus))
    }  
  
Fields  
---  
`success` |  `boolean` Required. Whether or not the validation completed without error.  
`validationStatus` |  `enum (`[ValidationStatus](https://docs.cloud.google.com/food-ai/reference/rest/v1/Order#ValidationStatus)`)` Required. The validation status of the delivery address.  
  
## OrderStatusResponse

The result of getting the order status.

JSON representation  
---  
      
    
    {
      "success": boolean
    }  
  
Fields  
---  
`success` |  `boolean` Required. Whether the order status was successfully retrieved.  
  
## Blob

Represents a blob input or output in the conversation.

JSON representation  
---  
      
    
    {
      "mimeType": string,
      "data": string
    }  
  
Fields  
---  
`mimeType` |  `string` Required. The IANA standard MIME type of the source data.  
`data` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Required. Raw bytes of the blob.A base64-encoded string.  
  
## Config

The configuration for a session and food ordering properties. At the start of each connection, the client must first send a config message. This must happen before any other requests to initiate the session. If the client disconnects, they should repeat the same config message when they reconnect.

JSON representation  
---  
      
    
    {
      "session": string,
      "store": string,
      "laneId": string,
      "enableEchoCancellation": boolean,
      "daypartId": string,
      "featureGate": {
        object ([FeatureGate](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#FeatureGate))
      },
      "clientAppInfo": {
        object ([ClientAppInfo](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#ClientAppInfo))
      },
      "mode": enum ([SessionMode](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#SessionMode)),
      "channelType": enum ([ChannelType](https://docs.cloud.google.com/food-ai/reference/rest/v1/ChannelType)),
      "enableListenOnlyDualChannel": boolean,
      "testSessionStartTime": string
    }  
  
Fields  
---  
`session` |  `string` Required. The session for the order. Format: `projects/{project}/locations/{location}/sessions/{session}`  
`store` |  `string` Required. The store the order is being placed for. Format: `projects/{project}/locations/{location}/brands/{brand}/stores/{store}`  
`laneId` |  `string` Optional. The id of a specifc drive through lane.  
`enableEchoCancellation` |  `boolean` Optional. Whether to enable echo cancellation for the session. If enabled, the client should provide the customerAudio and crewAudio in the AudioInput.  
`daypartId` |  `string` Optional. Daypart of the food menu, including breakfast, lunch, dinner, etc. This is used to determine the menu to use for the order.  
`featureGate` |  `object (`[FeatureGate](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#FeatureGate)`)` Optional. The feature gates for the session. This is used to enable or disable features for the session.  
`clientAppInfo` |  `object (`[ClientAppInfo](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#ClientAppInfo)`)` Optional. The information about the client application and device environment.  
`mode` |  `enum (`[SessionMode](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#SessionMode)`)` Optional. The mode of the session.  
`channelType` |  `enum (`[ChannelType](https://docs.cloud.google.com/food-ai/reference/rest/v1/ChannelType)`)` Optional. The type of channel used for agent communication.  
`enableListenOnlyDualChannel` |  `boolean` Optional. Whether to enable listen-only dual channel for the session. If enabled, the client should provide the customerAudio and crewAudio in the AudioInput, and CES will do EAC and summation on media processing server.  
`testSessionStartTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. The start time of the session, used for testing or evaluation purposes.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## FeatureGate

The feature gates for the session. This is used to enable or disable features for the session.

JSON representation  
---  
      
    
    {
      "menuResponseEnabled": boolean,
      "updatedOrderStateEnabled": boolean,
      "enableOrderStatusRetrieval": boolean
    }  
  
Fields  
---  
`menuResponseEnabled` |  `boolean` Optional. Returns the menu data to the client in BidiProcessOrderResponse if set.  
`updatedOrderStateEnabled` |  `boolean` Optional. If set, updatedOrderState is returned instead of legacyOrderStateResponse.  
`enableOrderStatusRetrieval` |  `boolean` Optional. If set, the agent will support order status retrieval.  
  
## ClientAppInfo

Information about the client application and device environment. This is primarily used for logging, analytics, and debugging.

JSON representation  
---  
      
    
    {
      "deviceModel": string,
      "osVersion": string,
      "sdkVersion": string
    }  
  
Fields  
---  
`deviceModel` |  `string` Optional. The device model of the client (e.g., "iPhone 13", "Pixel 7", "Kiosk v2").  
`osVersion` |  `string` Optional. The operating system version of the client (e.g., "iOS 16.1", "Android 13").  
`sdkVersion` |  `string` Optional. The version of the client SDK or application software.  
  
## SessionMode

The mode of the session.

Enums  
---  
`SESSION_MODE_UNSPECIFIED` | The session mode is not specified.  
`HYBRID` | The session supports both audio and text. This is the default.  
`TEXT` | The session is text-only.  
  
## TurnType

Represents the lifecycle position of a unary request within a session.

Enums  
---  
`TURN_TYPE_UNSPECIFIED` | Unspecified turn type.  
`INITIALIZE` | Explicitly indicates this request initializes the session in unary mode. When set, initial session variables (e.g., store metadata and menus) are injected into CES.  
`SUBSEQUENT` | Explicitly indicates a subsequent conversational turn or mid-session update. When set, initial session variables are omitted to prevent input token explosion.  
  
## BidiProcessOrderResponse

The top-level message returned from `FoodOrderingService.BidiProcessOrder` method.

JSON representation  
---  
      
    
    {
    
      // Union field response can be only one of the following:
      "agentAudio": {
        object ([AgentAudio](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#AgentAudio))
      },
      "speechRecognition": {
        object ([SpeechRecognition](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#SpeechRecognition))
      },
      "legacyOrderStateResponse": {
        object
      },
      "interruptionSignal": {
        object ([InterruptionSignal](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#InterruptionSignal))
      },
      "agentEvent": {
        object ([AgentEvent](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#AgentEvent))
      },
      "clientExecutionRequest": {
        object ([ClientExecutionRequest](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#ClientExecutionRequest))
      },
      "updatedOrderState": {
        object ([UpdatedOrderState](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#UpdatedOrderState))
      },
      "agentText": {
        object ([AgentText](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#AgentText))
      },
      "suggestedOptions": {
        object ([SuggestedOptions](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#SuggestedOptions))
      },
      "sentimentMeasurement": {
        object ([SentimentMeasurement](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#SentimentMeasurement))
      },
      "turnCompleted": {
        object ([TurnCompleted](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#TurnCompleted))
      },
      "endSession": {
        object ([EndSession](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#EndSession))
      }
      // End of list of possible types for union field response.
    }  
  
Fields  
---  
Union field `response`. The response from the agent. `response` can be only one of the following:  
`agentAudio` |  `object (`[AgentAudio](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#AgentAudio)`)` The audio response from the agent.  
`speechRecognition` |  `object (`[SpeechRecognition](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#SpeechRecognition)`)` The speech recognition result from the agent.  
`legacyOrderStateResponse` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` The legacy order state response for a session.  
`interruptionSignal` |  `object (`[InterruptionSignal](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#InterruptionSignal)`)` Interruption signal detected from the audio input.  
`agentEvent` |  `object (`[AgentEvent](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#AgentEvent)`)` Event from the agent.  
`clientExecutionRequest` |  `object (`[ClientExecutionRequest](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#ClientExecutionRequest)`)` The request forward to the client to execute. This is used for client side execution, such as adding a code to the order.  
`updatedOrderState` |  `object (`[UpdatedOrderState](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#UpdatedOrderState)`)` Indicates an update to the order state. Includes the complete state of the order.  
`agentText` |  `object (`[AgentText](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#AgentText)`)` The text response from the agent.  
`suggestedOptions` |  `object (`[SuggestedOptions](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#SuggestedOptions)`)` Options to suggest to the customer.  
`sentimentMeasurement` |  `object (`[SentimentMeasurement](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#SentimentMeasurement)`)` The realtime sentiment score measured for this turn.  
`turnCompleted` |  `object (`[TurnCompleted](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#TurnCompleted)`)` Turn Completed message.  
`endSession` |  `object (`[EndSession](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#EndSession)`)` Indicates that the session is ending, and that this will be the last turn.The agent will finish sending any pending responses for the current turn, and then send a final turnCompleted message. The agent will not start any new turns. For example, a 2 turn session will look like:

  * Turn 1
  * customer input 1
  * ... agent response and order state messages
  * turnCompleted
  * Turn 2
  * customer input 2
  * ... agent response and order state messages
  * endSession
  * ... pending agent response and order state messages
  * turnCompleted

  
  
## AgentAudio

The audio response from the agent.

JSON representation  
---  
      
    
    {
      "agentAudio": string
    }  
  
Fields  
---  
`agentAudio` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` The audio data from the agent.A base64-encoded string.  
  
## SpeechRecognition

The speech recognition result from the agent.

JSON representation  
---  
      
    
    {
      "transcript": string,
      "languageCode": string,
      "isFinal": boolean
    }  
  
Fields  
---  
`transcript` |  `string` Transcribed text from the audio input in the detected language.  
`languageCode` |  `string` The language code of the transcript. The language code should be in BCP-47 format, such as "en-US".  
`isFinal` |  `boolean` Indicates whether this is the final transcript for the turn.  
  
## InterruptionSignal

This type has no fields.

Indicates the agent's audio response has been interrupted (e.g. by end user barge-in). Client should stop playback immediately.

## AgentEvent

Special event from the agent that needs client to take action.

JSON representation  
---  
      
    
    {
    
      // Union field event can be only one of the following:
      "restartOrder": {
        object ([RestartOrder](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#RestartOrder))
      }
      // End of list of possible types for union field event.
    }  
  
Fields  
---  
Union field `event`. The event from the agent. `event` can be only one of the following:  
`restartOrder` |  `object (`[RestartOrder](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#RestartOrder)`)` Customer requests to restart the order.  
  
## RestartOrder

Customer requests to start over the order.

JSON representation  
---  
      
    
    {
      "confirmationStep": boolean
    }  
  
Fields  
---  
`confirmationStep` |  `boolean` The agent is asking the customer to confirm the restarting request.  
  
## ClientExecutionRequest

A request to the for client side to execute a command.

JSON representation  
---  
      
    
    {
      "executionId": string,
    
      // Union field request can be only one of the following:
      "finalizeOrderRequest": {
        object ([FinalizeOrderRequest](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#FinalizeOrderRequest))
      },
      "submitOrderRequest": {
        object ([SubmitOrderRequest](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#SubmitOrderRequest))
      },
      "orderPricesRequest": {
        object ([OrderPricesRequest](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#OrderPricesRequest))
      },
      "validateDeliveryAddressRequest": {
        object ([ValidateDeliveryAddressRequest](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#ValidateDeliveryAddressRequest))
      },
      "orderStatusRequest": {
        object ([OrderStatusRequest](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#OrderStatusRequest))
      }
      // End of list of possible types for union field request.
    }  
  
Fields  
---  
`executionId` |  `string` Required. A unique ID for this execution request.  
Union field `request`. The specific request to be executed. `request` can be only one of the following:  
`finalizeOrderRequest` |  `object (`[FinalizeOrderRequest](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#FinalizeOrderRequest)`)` A request to finalize the order.  
`submitOrderRequest` |  `object (`[SubmitOrderRequest](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#SubmitOrderRequest)`)` A request to submit the order.  
`orderPricesRequest` |  `object (`[OrderPricesRequest](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#OrderPricesRequest)`)` A request to get the order prices.  
`validateDeliveryAddressRequest` |  `object (`[ValidateDeliveryAddressRequest](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#ValidateDeliveryAddressRequest)`)` A request to validate the delivery address.  
`orderStatusRequest` |  `object (`[OrderStatusRequest](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#OrderStatusRequest)`)` A request to get the order status.  
  
## FinalizeOrderRequest

This type has no fields.

A request to finalize the order. This is typically sent by the agent when the customer indicates they are done ordering and want to pay.

## SubmitOrderRequest

A request to submit the order, with all the required payment information collected from the customer.

JSON representation  
---  
      
    
    {
      "paymentInfo": {
        object ([PaymentInfo](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#PaymentInfo))
      },
      "loyaltyInfo": {
        object ([LoyaltyInfo](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#LoyaltyInfo))
      },
      "tipAmount": {
        object ([Money](https://docs.cloud.google.com/food-ai/reference/rest/Shared.Types/Money))
      }
    }  
  
Fields  
---  
`paymentInfo` |  `object (`[PaymentInfo](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#PaymentInfo)`)` Required. The payment information for the order.  
`loyaltyInfo` |  `object (`[LoyaltyInfo](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#LoyaltyInfo)`)` Optional. The loyalty consumed for the order.  
`tipAmount` |  `object (`[Money](https://docs.cloud.google.com/food-ai/reference/rest/Shared.Types/Money)`)` Optional. The tip amount for the order.  
  
## LoyaltyInfo

Represents a customer's loyalty information.

JSON representation  
---  
      
    
    {
      "loyaltyAmount": {
        object ([LoyaltyAmount](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#LoyaltyAmount))
      }
    }  
  
Fields  
---  
`loyaltyAmount` |  `object (`[LoyaltyAmount](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#LoyaltyAmount)`)` Required. The loyalty amount. This can be a loyalty balance or loyalty consumed.  
  
## LoyaltyAmount

Represents a customer's loyalty amount.

JSON representation  
---  
      
    
    {
      "units": string
    }  
  
Fields  
---  
`units` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Required. The loyalty points.  
  
## OrderPricesRequest

A request to get the order prices.

JSON representation  
---  
      
    
    {
      "order": {
        object ([Order](https://docs.cloud.google.com/food-ai/reference/rest/v1/Order))
      }
    }  
  
Fields  
---  
`order` |  `object (`[Order](https://docs.cloud.google.com/food-ai/reference/rest/v1/Order)`)` Optional. The order to get the prices for. If not specified, we can assume the request is for the existing order/cart in the session.  
  
## ValidateDeliveryAddressRequest

A request to validate a delivery address collected during the session.

JSON representation  
---  
      
    
    {
      "deliveryAddress": {
        object ([DeliveryAddress](https://docs.cloud.google.com/food-ai/reference/rest/v1/Order#DeliveryAddress))
      }
    }  
  
Fields  
---  
`deliveryAddress` |  `object (`[DeliveryAddress](https://docs.cloud.google.com/food-ai/reference/rest/v1/Order#DeliveryAddress)`)` Required. The delivery address to validate.  
  
## OrderStatusRequest

This type has no fields.

A request to get the order status.

## UpdatedOrderState

Event returned by the agent representing an update to the order state.

JSON representation  
---  
      
    
    {
      "order": {
        object ([Order](https://docs.cloud.google.com/food-ai/reference/rest/v1/Order))
      },
      "changed": boolean
    }  
  
Fields  
---  
`order` |  `object (`[Order](https://docs.cloud.google.com/food-ai/reference/rest/v1/Order)`)` The updated state of the Order associated with this session.  
`changed` |  `boolean` Output only. Whether the order state has updates.  
  
## AgentText

The text response from the agent.

JSON representation  
---  
      
    
    {
      "text": string
    }  
  
Fields  
---  
`text` |  `string` The text response from the agent.  
  
## SuggestedOptions

Options to suggest to the customer.

JSON representation  
---  
      
    
    {
      "suggestedModifierGroups": {
        object ([SuggestedModifierGroups](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#SuggestedModifierGroups))
      },
    
      // Union field suggested_options can be only one of the following:
      "suggestedItems": {
        object ([SuggestedItems](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#SuggestedItems))
      },
      "suggestedModifiers": {
        object ([SuggestedModifiers](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#SuggestedModifiers))
      }
      // End of list of possible types for union field suggested_options.
    }  
  
Fields  
---  
`suggestedModifierGroups` |  `object (`[SuggestedModifierGroups](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#SuggestedModifierGroups)`)` A group of suggested modifiers.  
Union field `suggested_options`. The suggested options. `suggested_options` can be only one of the following:  
`suggestedItems` |  `object (`[SuggestedItems](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#SuggestedItems)`)` A list of items to suggest to the customer.  
`suggestedModifiers` |  `object (`[SuggestedModifiers](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#SuggestedModifiers)`)` A list of modifiers to suggest to the customer.  
  
## SuggestedItems

A list of items to suggest to the customer.

JSON representation  
---  
      
    
    {
      "items": [
        {
          object ([SuggestedItem](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#SuggestedItem))
        }
      ]
    }  
  
Fields  
---  
`items[]` |  `object (`[SuggestedItem](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#SuggestedItem)`)` The items to suggest to the customer.  
  
## SuggestedItem

An item to suggest to the customer.

JSON representation  
---  
      
    
    {
      "itemId": string,
      "displayName": string,
      "image": {
        object ([Image](https://docs.cloud.google.com/food-ai/reference/rest/v1/Image))
      },
      "basePrice": {
        object ([Money](https://docs.cloud.google.com/food-ai/reference/rest/Shared.Types/Money))
      },
      "integrationAttributes": {
        object ([ItemIntegrationAttributes](https://docs.cloud.google.com/food-ai/reference/rest/v1/ItemIntegrationAttributes))
      }
    }  
  
Fields  
---  
`itemId` |  `string` ID of the item in the menu.  
`displayName` |  `string` Human-readable name for this tem to be shown on user interfaces.  
`image` |  `object (`[Image](https://docs.cloud.google.com/food-ai/reference/rest/v1/Image)`)` Image to display for this item in the UI.  
`basePrice` |  `object (`[Money](https://docs.cloud.google.com/food-ai/reference/rest/Shared.Types/Money)`)` The base price of the item. This may be affected by the selected modifiers. This is the price per unit of the item.  
`integrationAttributes` |  `object (`[ItemIntegrationAttributes](https://docs.cloud.google.com/food-ai/reference/rest/v1/ItemIntegrationAttributes)`)` Metadata associated with this entity used for downstream integrations.  
  
## SuggestedModifiers

A list of modifiers to suggest to the customer.

JSON representation  
---  
      
    
    {
      "modifiers": [
        {
          object ([SuggestedModifier](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#SuggestedModifier))
        }
      ],
      "parentUid": string
    }  
  
Fields  
---  
`modifiers[]` |  `object (`[SuggestedModifier](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#SuggestedModifier)`)` The modifiers to suggest to the customer.  
`parentUid` |  `string` The unique identifier of the parent item/modifier to apply the modifiers to.  
  
## SuggestedModifier

A modifier to suggest to the customer.

JSON representation  
---  
      
    
    {
      "modifierId": string,
      "modifierGroupId": string,
      "modifierGroupDisplayName": string,
      "displayName": string,
      "image": {
        object ([Image](https://docs.cloud.google.com/food-ai/reference/rest/v1/Image))
      },
      "priceAdjustment": {
        object ([Money](https://docs.cloud.google.com/food-ai/reference/rest/Shared.Types/Money))
      },
      "integrationAttributes": {
        object ([ModifierIntegrationAttributes](https://docs.cloud.google.com/food-ai/reference/rest/v1/ModifierIntegrationAttributes))
      },
      "alreadyIncluded": boolean
    }  
  
Fields  
---  
`modifierId` |  `string` ID of the modifier in the menu.  
`modifierGroupId` |  `string` ID of the modifier group that this modifier should be added to if the suggestion is accepted.  
`modifierGroupDisplayName` |  `string` Display name of the modifier group that this modifier belongs to.  
`displayName` |  `string` Human-readable name for this tem to be shown on user interfaces.  
`image` |  `object (`[Image](https://docs.cloud.google.com/food-ai/reference/rest/v1/Image)`)` Image to display for this item in the UI.  
`priceAdjustment` |  `object (`[Money](https://docs.cloud.google.com/food-ai/reference/rest/Shared.Types/Money)`)` The price adjustment associated with this modifier, if any. This is the price per unit of the modifier.  
`integrationAttributes` |  `object (`[ModifierIntegrationAttributes](https://docs.cloud.google.com/food-ai/reference/rest/v1/ModifierIntegrationAttributes)`)` Metadata associated with this entity used for downstream integrations.  
`alreadyIncluded` |  `boolean` Whether this modifier is already included in the order.  
  
## SuggestedModifierGroups

A list of modifier groups to suggest to the customer.

JSON representation  
---  
      
    
    {
      "modifierGroups": [
        {
          object ([SuggestedModGroup](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#SuggestedModGroup))
        }
      ]
    }  
  
Fields  
---  
`modifierGroups[]` |  `object (`[SuggestedModGroup](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#SuggestedModGroup)`)` The modifier groups to suggest to the customer.  
  
## SuggestedModGroup

A modifier group to suggest to the customer.

JSON representation  
---  
      
    
    {
      "modifierGroupId": string,
      "displayName": string,
      "modifiers": [
        {
          object ([SuggestedModifier](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#SuggestedModifier))
        }
      ],
      "maxSelectionCount": integer,
      "minSelectionCount": integer,
      "maxSelectionCountPerModifier": integer
    }  
  
Fields  
---  
`modifierGroupId` |  `string` ID of the modifier group in the menu.  
`displayName` |  `string` The display name of the modifier group.  
`modifiers[]` |  `object (`[SuggestedModifier](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#SuggestedModifier)`)` The modifiers in this group.  
`maxSelectionCount` |  `integer` The maximum number of modifiers that can be selected from this group.  
`minSelectionCount` |  `integer` The minimum number of modifiers that must be selected from this group.  
`maxSelectionCountPerModifier` |  `integer` Limits the number of times each modifier can be applied within this group.  
  
## SentimentMeasurement

The realtime sentiment score measured for this turn.

JSON representation  
---  
      
    
    {
      "score": number,
      "magnitude": number
    }  
  
Fields  
---  
`score` |  `number` Optional. Sentiment score between -1.0 (negative sentiment) and 1.0 (positive sentiment).  
`magnitude` |  `number` Optional. Magnitude of sentiment, regardless of score.  
  
## TurnCompleted

This type has no fields.

Indicates that the Food AI agent has detected the end of the current conversation turn and will provide no further output for this turn.

## EndSession

Indicates the agent has terminated the session, due to either successful completion (e.g. user says "Good bye!" ) or an agent escalation.

JSON representation  
---  
      
    
    {
      "type": enum ([EndType](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#EndType)),
      "reason": string,
      "posResponse": string,
      "agentResponse": string,
      "storeSchedule": {
        object ([Schedule](https://docs.cloud.google.com/food-ai/reference/rest/v1/Schedule))
      }
    }  
  
Fields  
---  
`type` |  `enum (`[EndType](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder#EndType)`)` The type of end session event.  
`reason` |  `string` The reason for ending the session.  
`posResponse` |  `string` Optional. The POS response from checking in the order (optional). This is an opaque string payload representing the POS transaction status.  
`agentResponse` |  `string` Optional. The final agent response message to be spoken/displayed to the user (optional).  
`storeSchedule` |  `object (`[Schedule](https://docs.cloud.google.com/food-ai/reference/rest/v1/Schedule)`)` Optional. The store schedule. This is only set when the end type is STORE_CLOSED.  
  
## EndType

Type of end session event.

Enums  
---  
`END_TYPE_UNSPECIFIED` | The end type is not specified.  
`DRIVE_OFF` | The customer drove off.  
`AGENT_ESCALATION` | The agent escalated the session to a human agent.  
`CREW_INTERJECTION` | A crew member interjected in the session.  
`ORDER_COMPLETED` | Order was successfully completed and no further action is needed.  
`PAYMENT_FLOW_SUCCESS` | The payment flow was successful and no further action is needed.  
`PAYMENT_FLOW_FAILURE` | The payment flow failed.  
`CLIENT_ESCALATION` | The client escalated the session to a human agent.  
`CALLER_HANGUP` | The customer hung up the call prematurely.  
`REQUESTED_CHECKOUT` | The customer requested to check out.  
`REQUESTED_ORDER_STATUS` | The customer asked about their order status.  
`STORE_CLOSED` | The store is closed.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-21 UTC."],[],[]] 
