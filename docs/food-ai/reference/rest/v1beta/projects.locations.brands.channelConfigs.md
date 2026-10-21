---
url: https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs
title: REST Resource: projects.locations.brands.channelConfigs \u00a0|\u00a0 Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:14:44.931510+00:00
---

# REST Resource: projects.locations.brands.channelConfigs  |  Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Food AI ](https://docs.cloud.google.com/food-ai)



Send feedback 

#  REST Resource: projects.locations.brands.channelConfigs Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ChannelConfig
    * JSON representation
    * OperationsConfig
      * JSON representation
    * UpsellStrategy
      * JSON representation
    * UpsellConfig
      * JSON representation
    * GreetingOffer
      * JSON representation
    * OfferMessage
      * JSON representation
    * MessageConfig
      * JSON representation
    * ClosingOffer
      * JSON representation
    * ClosingMessage
      * JSON representation
    * CelUpsell
      * JSON representation
    * SuggestedModifierGroup
      * JSON representation
    * Greetings
      * JSON representation
    * FeaturesConfig
      * JSON representation
    * OrderPickup
    * OrderDineIn
    * NameCollection
    * GetOrderPrices
    * EndSessionWithCheckoutRequest
    * EnableAddressCollection
    * SupportCashPayment
    * InteractionMode
    * DisambiguationStrategy
      * JSON representation
    * DisambiguationMapping
      * JSON representation
    * Type
    * TargetItem
      * JSON representation
    * TargetModifier
      * JSON representation
    * State
    * Type
    * SupplementalInstructions
      * JSON representation
    * Tone
  * Methods



## Resource: ChannelConfig

A channel configuration represents an operational strategy configuration. Channel configuration lifecycle: * **DRAFT** : A configuration is in a draft state when it has no associated config application rules and is not set as the default configuration for the brand. * **ACTIVE** : A configuration is in an active state when it is either associated with any config application rule or set as the brand's default. * When active, the runtime applies the channel configuration to matching stores. To ensure flexibility, the relationship between channel configuration and config application rule is one-to-many on each resource level: * On the brand level, there is a one-to-many relationship between channel configurations and config application rules. * On the store level, there is another one-to-many relationship between channel configurations and config application rules. When multiple channel configurations are applicable, the runtime determines the configuration to apply based on the following precedence order (latter overwrites former in case of conflict): 1. Brand-level default 2. Brand-level binding 3. Store-level default 4. Store-level binding

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "createTime": string,
      "updateTime": string,
      "operationsConfig": {
        object ([OperationsConfig](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig.OperationsConfig))
      },
      "state": enum ([State](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig.State)),
      "type": enum ([Type](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig.Type_1)),
      "supplementalInstructions": {
        object ([SupplementalInstructions](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig.SupplementalInstructions))
      },
      "tone": enum ([Tone](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig.Tone)),
      "configApplicationRules": [
        {
          object ([ConfigApplicationRule](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.configApplicationRules#ConfigApplicationRule))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Identifier. The channel configuration name. Format: projects/{project}/locations/{location}/brands/{brand}/channelConfigs/{channelConfig}  
`displayName` |  `string` Optional. Optional display name for this channel configuration for user interfaces. Value is limited to 63 characters.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time this channel configuration was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time this channel configuration was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`operationsConfig` |  `object (`[OperationsConfig](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig.OperationsConfig)`)` Optional. The operational strategy for the channel configuration.  
`state` |  `enum (`[State](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig.State)`)` Output only. The status of the channel configuration.  
`type` |  `enum (`[Type](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig.Type_1)`)` Required. The type of the channel configuration.  
`supplementalInstructions` |  `object (`[SupplementalInstructions](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig.SupplementalInstructions)`)` Optional. Supplemental instructions for the channel configuration.  
`tone` |  `enum (`[Tone](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig.Tone)`)` Optional. The tone of the agent.  
`configApplicationRules[]` |  `object (`[ConfigApplicationRule](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.configApplicationRules#ConfigApplicationRule)`)` Output only. The config application rules associated with this channel configuration.  
  
### OperationsConfig

Configurations for defining an operational strategy.

JSON representation  
---  
      
    
    {
      "displayName": string,
      "description": string,
      "upsellStrategy": {
        object ([UpsellStrategy](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig.UpsellStrategy))
      },
      "greetings": [
        {
          object ([Greetings](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig.Greetings))
        }
      ],
      "defaultLanguageCode": string,
      "featuresConfig": {
        object ([FeaturesConfig](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig.FeaturesConfig))
      },
      "interactionMode": enum ([InteractionMode](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig.InteractionMode)),
      "disambiguationStrategy": {
        object ([DisambiguationStrategy](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig.DisambiguationStrategy))
      }
    }  
  
Fields  
---  
`displayName` |  `string` Optional. The name of this operational strategy.  
`description` |  `string` Optional. A description of this operational strategy.  
`upsellStrategy` |  `object (`[UpsellStrategy](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig.UpsellStrategy)`)` Optional. Configuration for upsell behavior.  
`greetings[]` |  `object (`[Greetings](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig.Greetings)`)` Optional. Customized greeting messages to use (per language).  
`defaultLanguageCode` |  `string` Optional. Default language to use for serving customers.  
`featuresConfig` |  `object (`[FeaturesConfig](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig.FeaturesConfig)`)` Optional. Agent features configuration.  
`interactionMode` |  `enum (`[InteractionMode](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig.InteractionMode)`)` Optional. The interaction mode of the agent.  
`disambiguationStrategy` |  `object (`[DisambiguationStrategy](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig.DisambiguationStrategy)`)` Optional. Strategy configuration for Disambiguation Control.  
  
### UpsellStrategy

Defines the strategy for upselling.

JSON representation  
---  
      
    
    {
      "maxUpsellOffers": integer,
      "maxUpsellDeclines": integer,
      "maxItemsInCart": integer,
      "upsells": [
        {
          object ([UpsellConfig](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig.UpsellConfig))
        }
      ],
      "cateringGuidelines": string
    }  
  
Fields  
---  
`maxUpsellOffers` |  `integer` Optional. The maximum number of upsell offers to present per session.  
`maxUpsellDeclines` |  `integer` Optional. The maximum number of times a customer can decline an upsell before further upsells are skipped for the current session.  
`maxItemsInCart` |  `integer` Optional. The maximum number of items allowed in the cart before further upsells are skipped for the current session.  
`upsells[]` |  `object (`[UpsellConfig](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig.UpsellConfig)`)` Optional. The configured upsells.  
`cateringGuidelines` |  `string` Optional. Represents a set of text representing the offline-generated serving calculations and group ordering rules for this menu. Read by the conversational LLM.  
  
### UpsellConfig

Defines the configuration for an upsell instance.

JSON representation  
---  
      
    
    {
      "displayName": string,
      "priority": integer,
      "skipOnMultiQuantityUpsoldFromItem": boolean,
      "skipOnPreviousTurnUpsell": boolean,
      "disabled": boolean,
    
      // Union field upsell_type_config can be only one of the following:
      "greetingOffer": {
        object ([GreetingOffer](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig.GreetingOffer))
      },
      "closingOffer": {
        object ([ClosingOffer](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig.ClosingOffer))
      },
      "celUpsell": {
        object ([CelUpsell](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig.CelUpsell))
      }
      // End of list of possible types for union field upsell_type_config.
    }  
  
Fields  
---  
`displayName` |  `string` Optional. Name for the upsell. Is used for UI display, as well as metrics aggregation and analytics.  
`priority` |  `integer` Required. Number representing the priority ordering of the upsell configuration relative to all other UpsellConfigs within a given UpsellStrategy. Higher priority UpsellConfigs will have their upsell attempted before lower priority ones.

  * Values can be on the range [1, inf).
  * Lower values have higher priority. For example, an UpsellConfig with priority 1 in an UpsellStrategy will always be attempted first.
  * Within an UpsellStrategy, each UpsellConfig must have a uniquely-valued priority (ex: only one UpsellConfig can have a priority of 3).
  * Priority values don't necessarily have to be contiguous within an UpsellStrategy (ex: there can be UpsellConfigs with priority values: {1, 2, 5, 6, 9}). The precedence of upsell configurations is determined on a relative basis (from the previous example: 1 < 2 < 5 < 6 < 9).

  
`skipOnMultiQuantityUpsoldFromItem` |  `boolean` Optional. Whether to skip this upsell if the item to upsell from has a quantity > 1\. This configuration only applies to the relevant upsell types: - Item to combo - Combo up size - Modifier addition - Combo drink - Item up size - Combo variant - Item triggered  
`skipOnPreviousTurnUpsell` |  `boolean` Optional. Whether to skip this upsell if the prior conversational turn was an upsell.  
`disabled` |  `boolean` Optional. Indicates whether the upsell type is disabled. If true, the upsell will not be attempted. This configuration is useful for disabling an upsell type as part of a config application rule override.  
Union field `upsell_type_config`. The type-specific configuration of the upsell. `upsell_type_config` can be only one of the following:  
`greetingOffer` |  `object (`[GreetingOffer](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig.GreetingOffer)`)` Upsell specific items as part of the agent welcome message.  
`closingOffer` |  `object (`[ClosingOffer](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig.ClosingOffer)`)` Upsell specific items after a customer has completed their order.  
`celUpsell` |  `object (`[CelUpsell](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig.CelUpsell)`)` Dynamically evaluated upsell rule based on Common Expression Language (CEL).  
  
### GreetingOffer

Upsell specific items as part of the agent welcome message.

JSON representation  
---  
      
    
    {
      "messages": [
        {
          object ([OfferMessage](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig.OfferMessage))
        }
      ]
    }  
  
Fields  
---  
`messages[]` |  `object (`[OfferMessage](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig.OfferMessage)`)` Required. Greeting upsell messages to be used.  
  
### OfferMessage

Common configuration for greeting and closing offer messages.

JSON representation  
---  
      
    
    {
      "displayName": string,
      "messageFrequency": number,
      "upsoldItems": [
        string
      ],
      "messageConfigs": [
        {
          object ([MessageConfig](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig.MessageConfig))
        }
      ],
      "upsoldItemIds": [
        string
      ]
    }  
  
Fields  
---  
`displayName` |  `string` Optional. Name to use for display and analytics.  
`messageFrequency` |  `number` Optional. Fraction of the time to use this message. Ex: a messageFrequency of 0.2 means this message will be used for 20% of sessions. If all messageFrequency values are unset (0.0), each message will be used for 1/n proportion of sessions, where n is the number of OfferMessages configured for the offer type. If only some messageFrequency values are set, OfferMessages with unset messageFrequency values will not be used.  
`upsoldItems[]` |  `string` Optional. Names of the items being upsold in this message. Set this OR upsoldItemIds, but not both.  
`messageConfigs[]` |  `object (`[MessageConfig](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig.MessageConfig)`)` Required. Per-language upsell messages.  
`upsoldItemIds[]` |  `string` Optional. IDs of the items being upsold in this message. Set this OR upsoldItems, but not both.  
  
### MessageConfig

Language-specific message to use for an upsell.

JSON representation  
---  
      
    
    {
      "languageCode": string,
      "messageText": string
    }  
  
Fields  
---  
`languageCode` |  `string` Required. Code of the language to use for this message. BCP-47 language code, such as "en-US" or "fr-CA".  
`messageText` |  `string` Required. Language-specific message text.  
  
### ClosingOffer

Upsell specific items after a customer has completed their order.

JSON representation  
---  
      
    
    {
      "closingMessages": [
        {
          object ([ClosingMessage](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig.ClosingMessage))
        }
      ]
    }  
  
Fields  
---  
`closingMessages[]` |  `object (`[ClosingMessage](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig.ClosingMessage)`)` Required. Closing offer upsells to apply.  
  
### ClosingMessage

Closing upsell message configuration.

JSON representation  
---  
      
    
    {
      "offerMessage": {
        object ([OfferMessage](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig.OfferMessage))
      },
      "skipTerms": [
        string
      ]
    }  
  
Fields  
---  
`offerMessage` |  `object (`[OfferMessage](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig.OfferMessage)`)` Required. Offer message configuration.  
`skipTerms[]` |  `string` Optional. This upsell will be skipped if any of these terms are present in the name of an item already in the customer's order.  
  
### CelUpsell

Represents a pre-computed rule that defines under what contextual conditions a set of items should be proactively upsold to the user.

JSON representation  
---  
      
    
    {
      "conditionExpression": string,
      "suggestedMenuItems": [
        string
      ],
      "triggerReason": string,
      "priority": integer,
      "suggestedModifiers": [
        string
      ],
      "suggestedModifierGroups": [
        {
          object ([SuggestedModifierGroup](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig.SuggestedModifierGroup))
        }
      ],
      "maxModifierPerGroup": integer,
      "suggestionOnly": boolean
    }  
  
Fields  
---  
`conditionExpression` |  `string` Required. A CEL (Common Expression Language) string evaluated against the current session state (`Order` and `ClientSessionMetadata`). If it evaluates to True, the rule triggers. Example: `"context.weather_condition == 'HOT' && order.items.size() > 0"`  
`suggestedMenuItems[]` |  `string` Required. The semantic names of the items to suggest if this rule triggers.  
`triggerReason` |  `string` Optional. A natural language instruction provided to the conversational LLM explaining _why_ this upsell is being made, so it can formulate a natural upsell. Example: `"Suggest a cold drink because it is a hot day."`  
`priority` |  `integer` Optional. The `priority` of this rule. Higher numbers mean higher priority. If multiple rules trigger, the highest priority rule's suggestions are favored. If omitted, the `priority` defaults to `0`.  
`suggestedModifiers[]` |  `string` Optional. The semantic names of the modifiers to suggest if this rule triggers.  
`suggestedModifierGroups[]` |  `object (`[SuggestedModifierGroup](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig.SuggestedModifierGroup)`)` Optional. The modifier groups to suggest if this rule triggers.  
`maxModifierPerGroup` |  `integer` Optional. Max number of modifiers to suggest per group.  
`suggestionOnly` |  `boolean` Optional. Not real upsell, but just to show the suggested options to user.  
  
### SuggestedModifierGroup

A suggested modifier group.

JSON representation  
---  
      
    
    {
      "name": string,
      "suggestedModifiers": [
        string
      ]
    }  
  
Fields  
---  
`name` |  `string` Optional. The semantic name of the modifier group.  
`suggestedModifiers[]` |  `string` Optional. The semantic names of the modifiers to suggest within this group.  
  
### Greetings

Represents greeting messages for a specific language.

JSON representation  
---  
      
    
    {
      "languageCode": string,
      "greetingPhrases": [
        string
      ]
    }  
  
Fields  
---  
`languageCode` |  `string` Optional. The language code of the greeting phrases. BCP-47 language code, such as "en-US" or "fr-CA".  
`greetingPhrases[]` |  `string` Optional. A list of greeting phrases in the specified language.  
  
### FeaturesConfig

Configurations for agent features. Feature flag list that is used to generate agent's custom instructions and tools.

JSON representation  
---  
      
    
    {
      "orderPickup": {
        object ([OrderPickup](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig.OrderPickup))
      },
      "orderDineIn": {
        object ([OrderDineIn](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig.OrderDineIn))
      },
      "nameCollection": {
        object ([NameCollection](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig.NameCollection))
      },
      "confirmOrderInfoAtStart": boolean,
      "confirmOrderInfoOnFinalize": boolean,
      "getOrderPrices": {
        object ([GetOrderPrices](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig.GetOrderPrices))
      },
      "endSessionWithCheckoutRequest": {
        object ([EndSessionWithCheckoutRequest](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig.EndSessionWithCheckoutRequest))
      },
      "enableAddressCollection": {
        object ([EnableAddressCollection](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig.EnableAddressCollection))
      },
      "supportCashPayment": {
        object ([SupportCashPayment](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig.SupportCashPayment))
      },
      "budgetBasedOrdering": boolean
    }  
  
Fields  
---  
`orderPickup` |  `object (`[OrderPickup](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig.OrderPickup)`)` Optional. Order pickup feature configuration.  
`orderDineIn` |  `object (`[OrderDineIn](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig.OrderDineIn)`)` Optional. Order Dine-in feature configuration.  
`nameCollection` |  `object (`[NameCollection](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig.NameCollection)`)` Optional. Name collection feature configuration.  
`confirmOrderInfoAtStart  
**(deprecated)**` |  `boolean` This item is deprecated!Optional. Whether to confirm order info at the start of the session. Deprecated: replaced by confirmOrderInfoOnFinalize.  
`confirmOrderInfoOnFinalize` |  `boolean` Optional. Whether to confirm order info when finalizing the order.  
`getOrderPrices` |  `object (`[GetOrderPrices](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig.GetOrderPrices)`)` Optional. Get order prices feature configuration.  
`endSessionWithCheckoutRequest` |  `object (`[EndSessionWithCheckoutRequest](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig.EndSessionWithCheckoutRequest)`)` Optional. End session with checkout request feature configuration.  
`enableAddressCollection` |  `object (`[EnableAddressCollection](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig.EnableAddressCollection)`)` Optional. Enable delivery address collection feature configuration.  
`supportCashPayment` |  `object (`[SupportCashPayment](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig.SupportCashPayment)`)` Optional. Support cash payment feature configuration.  
`budgetBasedOrdering` |  `boolean` Optional. Whether to enable budget based ordering.  
  
### OrderPickup

This type has no fields.

Allows customer to order food via agent for pickup.

### OrderDineIn

This type has no fields.

Allows customer to order food via agent for dine in

### NameCollection

This type has no fields.

Enables agent to collect customer name during session.

### GetOrderPrices

This type has no fields.

Enables agent to get order prices from the POS.

### EndSessionWithCheckoutRequest

This type has no fields.

Enables agent to end session with checkout request.

### EnableAddressCollection

This type has no fields.

Enables agent to collect customer delivery address during session.

### SupportCashPayment

This type has no fields.

Enables agent to support cash payment.

### InteractionMode

The interaction mode of the agent.

Enums  
---  
`INTERACTION_MODE_UNSPECIFIED` | Interaction mode is unspecified.  
`ORDER_TAKING` | The agent participates in a two-way conversation to take orders.  
`LISTEN_ONLY` | The agent only listens and does not speak.  
  
### DisambiguationStrategy

Strategy configuration for Disambiguation Control.

JSON representation  
---  
      
    
    {
      "mappings": [
        {
          object ([DisambiguationMapping](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig.DisambiguationMapping))
        }
      ]
    }  
  
Fields  
---  
`mappings[]` |  `object (`[DisambiguationMapping](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig.DisambiguationMapping)`)` Optional. The configured disambiguation mappings.  
  
### DisambiguationMapping

A mapping rule to correct invalid terms or clarify ambiguous items.

JSON representation  
---  
      
    
    {
      "type": enum ([Type](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig.Type)),
      "customerTerms": [
        string
      ],
      "targets": [
        {
          object ([TargetItem](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig.TargetItem))
        }
      ],
      "customInstruction": string
    }  
  
Fields  
---  
`type` |  `enum (`[Type](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig.Type)`)` Required. The operational type of the disambiguation rule.  
`customerTerms[]` |  `string` Required. Customer utterances or shortcut strings. Each customer term is limited to 100 characters.  
`targets[]` |  `object (`[TargetItem](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig.TargetItem)`)` Required. Fully structured target menu items to suggest or clarify, including nested modifiers.  
`customInstruction` |  `string` Optional. Optional custom conditional macro instructions or phrasing hints.  
  
### Type

The operational type of the disambiguation rule.

Enums  
---  
`TYPE_UNSPECIFIED` | Unspecified rule type.  
`SINGLE_TARGET` | Used for single-target mappings (shortcuts, custom combo configurations, or valid synonyms).  
`INVALID_ITEM` | Used for invalid items, out-of-stock items, or competitor products.  
`DISAMBIGUATION` | Used for ambiguous inputs requiring clarification among multiple valid target options.  
  
### TargetItem

A structured item alternative target.

JSON representation  
---  
      
    
    {
      "itemName": string,
      "modifiers": [
        {
          object ([TargetModifier](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig.TargetModifier))
        }
      ],
      "itemId": string
    }  
  
Fields  
---  
`itemName` |  `string` Required. The item name in the menu catalog.  
`modifiers[]` |  `object (`[TargetModifier](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig.TargetModifier)`)` Optional. Structured modifiers to attach to this target.  
`itemId` |  `string` Optional. The unique ID of the item in the menu catalog (linking directly to menu.proto).  
  
### TargetModifier

A structured modifier to apply to the target item.

JSON representation  
---  
      
    
    {
      "modifierName": string,
      "modifierGroupName": string,
      "modifierId": string,
      "modifierGroupId": string
    }  
  
Fields  
---  
`modifierName` |  `string` Required. The modifier name matching the catalog entry directly.  
`modifierGroupName` |  `string` Optional. Optional modifier group name to bind the modifier.  
`modifierId` |  `string` Optional. The unique ID of the modifier in the menu catalog (linking directly to menu.proto).  
`modifierGroupId` |  `string` Optional. The unique ID of the modifier group in the menu catalog.  
  
### State

Status of the channel configuration.

Enums  
---  
`STATE_UNSPECIFIED` | Status is unspecified.  
`DRAFT` | The channel configuration is a draft and not yet ready for use.  
`ACTIVE` | The channel configuration is active and can be used.  
`PROMOTED` | The channel configuration is promoted.  
  
### Type

The type of the channel configuration.

Enums  
---  
`TYPE_UNSPECIFIED` | Type is unspecified.  
`UPSELL_STRATEGY` | The channel configuration is for upsell strategy.  
`AGENT_CUSTOMIZATION` | The channel configuration is for agent customization.  
  
### SupplementalInstructions

Configurations for supplemental instructions.

JSON representation  
---  
      
    
    {
      "freeformInstructions": string
    }  
  
Fields  
---  
`freeformInstructions` |  `string` Optional. Free-form instructions included in the prompt.  
  
### Tone

The tone of the agent.

Enums  
---  
`TONE_UNSPECIFIED` | Tone is unspecified.  
`CONCISE_AND_DIRECT` | The agent's tone is concise and direct.  
`PROFESSIONAL_AND_FORMAL` | The agent's tone is professional and formal.  
`FRIENDLY` | The agent's tone is friendly.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs/create)`

|  Creates a ChannelConfig.  
  
### `[delete](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs/delete)`

|  Deletes the specified ChannelConfig.  
  
### `[get](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs/get)`

|  Gets a ChannelConfig.  
  
### `[list](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs/list)`

|  Lists ChannelConfigs.  
  
### `[patch](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs/patch)`

|  Updates the specified ChannelConfig.  
  
### `[promote](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs/promote)`

|  Promotes the specified channel config.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-21 UTC."],[],[]] 
