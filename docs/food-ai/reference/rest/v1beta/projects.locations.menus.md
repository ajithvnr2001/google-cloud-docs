---
url: https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus
title: REST Resource: projects.locations.menus \u00a0|\u00a0 Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:28:06.396521+00:00
---

# REST Resource: projects.locations.menus  |  Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Food AI ](https://docs.cloud.google.com/food-ai)



Send feedback 

#  REST Resource: projects.locations.menus Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Menu
    * JSON representation
  * Item
    * JSON representation
  * Availability
    * JSON representation
  * DaypartAvailability
    * JSON representation
  * MenuScheduleAvailability
    * JSON representation
  * Status
  * FulfillmentMethodAvailability
    * JSON representation
  * ModifierGroupReference
    * JSON representation
  * DefaultModifierSelection
    * JSON representation
  * ModifierConstraints
    * JSON representation
  * Modifier
    * JSON representation
  * ModifierGroup
    * JSON representation
  * ModifierAction
    * JSON representation
  * MenuCategory
    * JSON representation
  * MenuLabel
    * JSON representation
  * MenuSchedule
    * JSON representation
  * Methods



## Resource: Menu

Defines a menu of what can be ordered from a restaurant.

JSON representation  
---  
      
    
    {
      "name": string,
      "store": string,
      "displayName": string,
      "items": [
        {
          object ([Item](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus#Item))
        }
      ],
      "modifiers": [
        {
          object ([Modifier](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus#Modifier))
        }
      ],
      "modifierGroups": [
        {
          object ([ModifierGroup](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus#ModifierGroup))
        }
      ],
      "categories": [
        {
          object ([MenuCategory](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus#MenuCategory))
        }
      ],
      "createTime": string,
      "updateTime": string,
      "labels": [
        {
          object ([MenuLabel](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus#MenuLabel))
        }
      ],
      "menuSchedules": [
        {
          object ([MenuSchedule](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus#MenuSchedule))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Identifier. The menu name. Format: projects/{project}/locations/{location}/menus/{menu}  
`store` |  `string` Optional. The resource name of the Store this Menu is associated with. Format: projects/{project}/locations/{location}/brands/{brand}/stores/{store}  
`displayName` |  `string` Optional. Optional, human-readable display name for this menu for user interfaces.  
`items[]` |  `object (`[Item](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus#Item)`)` Optional. Items in this menu.  
`modifiers[]` |  `object (`[Modifier](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus#Modifier)`)` Optional. Item modifiers in this menu.  
`modifierGroups[]` |  `object (`[ModifierGroup](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus#ModifierGroup)`)` Optional. Modifier groups in this menu.  
`categories[]` |  `object (`[MenuCategory](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus#MenuCategory)`)` Optional. Menu categories in this menu.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time this menu was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time this menu was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels[]` |  `object (`[MenuLabel](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus#MenuLabel)`)` Optional. Labels for this menu.  
`menuSchedules[]` |  `object (`[MenuSchedule](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus#MenuSchedule)`)` Optional. Menu schedules in this menu.  
  
## Item

Item represents a menu entity which is valid only as a top-level item within an order. Item may represent a single food item, drink, service, promotion, or combination meal which can be modified with various choices.

JSON representation  
---  
      
    
    {
      "id": string,
      "semanticName": string,
      "displayName": string,
      "categoryIds": [
        string
      ],
      "description": string,
      "image": {
        object ([Image](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/Image))
      },
      "availability": {
        object ([Availability](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus#Availability))
      },
      "basePrice": {
        object ([Money](https://docs.cloud.google.com/food-ai/reference/rest/Shared.Types/Money))
      },
      "integrationAttributes": {
        object ([ItemIntegrationAttributes](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/ItemIntegrationAttributes))
      },
      "modifierGroups": [
        {
          object ([ModifierGroupReference](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus#ModifierGroupReference))
        }
      ],
      "modifierConstraints": {
        object ([ModifierConstraints](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus#ModifierConstraints))
      }
    }  
  
Fields  
---  
`id` |  `string` Required. Identifier for this item, unique within the menu.  
`semanticName` |  `string` Optional. Concise, human-readable name which clearly & distinctly identifies this item. Should be unique among Items in the menu.  
`displayName` |  `string` Required. Human-readable name for this item to be used on user interfaces.  
`categoryIds[]` |  `string` Optional. Category of the item.  
`description` |  `string` Optional. Human-readable description.  
`image` |  `object (`[Image](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/Image)`)` Optional. Image to display for this item in the UI.  
`availability` |  `object (`[Availability](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus#Availability)`)` Optional. Availability of the item.  
`basePrice` |  `object (`[Money](https://docs.cloud.google.com/food-ai/reference/rest/Shared.Types/Money)`)` Optional. The base price of the item. This may be affected by the selected modifiers.  
`integrationAttributes` |  `object (`[ItemIntegrationAttributes](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/ItemIntegrationAttributes)`)` Optional. Metadata associated with this entity used for downstream integrations.  
`modifierGroups[]` |  `object (`[ModifierGroupReference](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus#ModifierGroupReference)`)` Optional. References to modifier groups which apply to this item.  
`modifierConstraints` |  `object (`[ModifierConstraints](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus#ModifierConstraints)`)` Optional. Constrains what modifiers can / must be applied to this item across referenced ModifierGroups.  
  
## Availability

Defines the availability of an item or modifier.

JSON representation  
---  
      
    
    {
      "daypartAvailability": {
        object ([DaypartAvailability](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus#DaypartAvailability))
      },
      "menuScheduleAvailability": {
        object ([MenuScheduleAvailability](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus#MenuScheduleAvailability))
      },
      "status": enum ([Status](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus#Status)),
      "fulfillmentAvailability": {
        object ([FulfillmentMethodAvailability](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus#FulfillmentMethodAvailability))
      }
    }  
  
Fields  
---  
`daypartAvailability` |  `object (`[DaypartAvailability](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus#DaypartAvailability)`)` Optional. Daypart-level availability information for this item. If omitted, daypart-based availability is ignored.  
`menuScheduleAvailability` |  `object (`[MenuScheduleAvailability](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus#MenuScheduleAvailability)`)` Optional. Menu schedule-level availability information for this item. If omitted, menu schedule-based availability is ignored.  
`status` |  `enum (`[Status](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus#Status)`)` Optional. Indicates a status leading to unavailability, or that the item is available. If omitted, the item is available by default.  
`fulfillmentAvailability` |  `object (`[FulfillmentMethodAvailability](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus#FulfillmentMethodAvailability)`)` Optional. The fulfillment methods this item is available for. If omitted, the item is available for all fulfillment methods.  
  
## DaypartAvailability

Constrains availability of this entity to specified dayparts.

JSON representation  
---  
      
    
    {
      "daypartIds": [
        string
      ]
    }  
  
Fields  
---  
`daypartIds[]` |  `string` Required. Dayparts during which this item is available.  
  
## MenuScheduleAvailability

Constrains availability of this entity to specified menu schedule.

JSON representation  
---  
      
    
    {
      "menuScheduleIds": [
        string
      ]
    }  
  
Fields  
---  
`menuScheduleIds[]` |  `string` Required. Menu schedules during which this item is available.  
  
## Status

Status of availability.

Enums  
---  
`STATUS_UNSPECIFIED` | Invalid status. menus.create will fail if any item or modifier has this status.  
`STATUS_AVAILABLE` | Indicates that the item is available for purchase.  
`STATUS_UNAVAILABLE` | Indicates that the item is unavailable for ambiguous reasons.  
`STATUS_OUT_OF_STOCK` | Indicates that the item is currently out of stock, but may become available in the near future.  
`STATUS_DISCONTINUED` | Indicates that the item is discontinued, and will remain unavailable for the foreseeable future.  
  
## FulfillmentMethodAvailability

Constrains availability of this entity to specified fulfillment methods.

JSON representation  
---  
      
    
    {
      "fulfillmentMethods": [
        enum ([FulfillmentMethod](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/FulfillmentMethod))
      ]
    }  
  
Fields  
---  
`fulfillmentMethods[]` |  `enum (`[FulfillmentMethod](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/FulfillmentMethod)`)` Required. Fulfillment methods for which this item is available.  
  
## ModifierGroupReference

A reference to a modifier group.

JSON representation  
---  
      
    
    {
      "id": string,
      "defaultModifiers": [
        {
          object ([DefaultModifierSelection](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus#DefaultModifierSelection))
        }
      ],
      "minSelectionCount": integer,
      "maxSelectionCount": integer
    }  
  
Fields  
---  
`id` |  `string` Required. The modifier group ID.  
`defaultModifiers[]` |  `object (`[DefaultModifierSelection](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus#DefaultModifierSelection)`)` Optional. The set of modifiers that are applied by default.  
`minSelectionCount` |  `integer` Optional. The minimum count of modifiers from the referenced ModifierGroup which must be selected. If this value is set on both the ModifierGroupReference and the ModifierGroup, both constraints are enforced. If not set, there is no minimum.  
`maxSelectionCount` |  `integer` Optional. The maximum count of total modifiers from the referenced group that may be selected. If this value is set on both the ModifierGroupReference and the ModifierGroup, both constraints are enforced. If not set, there is no maximum.  
  
## DefaultModifierSelection

Specifies the default selection of a modifier within a ModifierGroup.

JSON representation  
---  
      
    
    {
      "id": string,
      "quantity": integer
    }  
  
Fields  
---  
`id` |  `string` Required. The modifier ID.  
`quantity` |  `integer` Optional. The quantity of this modifier to apply. If omitted, reference is treated as having a quantity of 1.  
  
## ModifierConstraints

Constrains what modifiers can or must be applied to an entity across referenced ModifierGroups.

JSON representation  
---  
      
    
    {
      "minQuantity": integer,
      "maxQuantity": integer
    }  
  
Fields  
---  
`minQuantity` |  `integer` Optional. The minimum number of modifiers that must be applied across directly referenced ModifierGroups. If not specified, no minimum is enforced.  
`maxQuantity` |  `integer` Optional. The maximum number of modifiers that may be applied across directly referenced ModifierGroups. If not specified, no maximum is enforced.  
  
## Modifier

Defines modifying options made within for items or other modifiers, via relationships defined by ModifierGroup.

JSON representation  
---  
      
    
    {
      "id": string,
      "displayName": string,
      "description": string,
      "image": {
        object ([Image](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/Image))
      },
      "semanticName": string,
      "categoryIds": [
        string
      ],
      "availability": {
        object ([Availability](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus#Availability))
      },
      "priceAdjustment": {
        object ([Money](https://docs.cloud.google.com/food-ai/reference/rest/Shared.Types/Money))
      },
      "integrationAttributes": {
        object ([ModifierIntegrationAttributes](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/ModifierIntegrationAttributes))
      },
      "modifierGroups": [
        {
          object ([ModifierGroupReference](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus#ModifierGroupReference))
        }
      ],
      "modifierConstraints": {
        object ([ModifierConstraints](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus#ModifierConstraints))
      }
    }  
  
Fields  
---  
`id` |  `string` Required. Identifier for this modifier, unique within the menu.  
`displayName` |  `string` Required. Human-readable name for this item to be used on user interfaces.  
`description` |  `string` Optional. Human-readable description.  
`image` |  `object (`[Image](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/Image)`)` Optional. Image to display for this item in the UI.  
`semanticName` |  `string` Optional. Concise, human-readable name which clearly & distinctly identifies this modifier. Should be unique among Modifiers in ModifierGroups where this Modifier exists.  
`categoryIds[]` |  `string` Optional. Category of the modifier.  
`availability` |  `object (`[Availability](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus#Availability)`)` Optional. Availability for this modifier.  
`priceAdjustment` |  `object (`[Money](https://docs.cloud.google.com/food-ai/reference/rest/Shared.Types/Money)`)` Optional. An additive adjustment applied to the top-level item's price when this modifier is selected. Leave empty if the modifier does not affect the price.  
`integrationAttributes` |  `object (`[ModifierIntegrationAttributes](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/ModifierIntegrationAttributes)`)` Optional. Metadata associated with this entity used for downstream integrations.  
`modifierGroups[]` |  `object (`[ModifierGroupReference](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus#ModifierGroupReference)`)` Optional. References to modifier groups which apply to this modifier.  
`modifierConstraints` |  `object (`[ModifierConstraints](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus#ModifierConstraints)`)` Optional. Constrains what modifiers can / must be applied to this modifier across referenced ModifierGroups.  
  
## ModifierGroup

Defines a group of modifiers from which selections can be made.

JSON representation  
---  
      
    
    {
      "id": string,
      "displayName": string,
      "semanticName": string,
      "modifierIds": [
        string
      ],
      "modifierActions": [
        {
          object ([ModifierAction](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus#ModifierAction))
        }
      ],
      "minSelectionCount": integer,
      "maxSelectionCount": integer,
      "maxSelectionCountPerModifier": integer,
      "integrationAttributes": {
        object ([ModifierGroupIntegrationAttributes](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/ModifierGroupIntegrationAttributes))
      }
    }  
  
Fields  
---  
`id` |  `string` Required. Identifier for this modifier group, unique within its menu.  
`displayName` |  `string` Required. The modifier group name -- e.g. "Toppings (Sandwich)" or "Side for Medium Combo".  
`semanticName` |  `string` Optional. The modifier group name -- e.g. "Toppings (Sandwich)" or "Side for Combo".  
`modifierIds[]` |  `string` Required. The modifier IDs that are part of this group.  
`modifierActions[]` |  `object (`[ModifierAction](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus#ModifierAction)`)` Optional. The actions that can be taken on the modifiers in this group.  
`minSelectionCount` |  `integer` Optional. The minimum count of modifiers from the referenced group that must be selected in order for the Item to be valid. If not set, there is no minimum. For a group where exactly one selection is required, this should be 1.  
`maxSelectionCount` |  `integer` Optional. The maximum count of total modifiers from the referenced group that may be selected. If not set, there is no maximum. For a group where exactly one selection is required, this should be 1.  
`maxSelectionCountPerModifier` |  `integer` Optional. Limits the number of times each modifier can be applied within this group. If not set, the default is 1.  
`integrationAttributes` |  `object (`[ModifierGroupIntegrationAttributes](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/ModifierGroupIntegrationAttributes)`)` Optional. Metadata associated with this entity used for downstream integrations.  
  
## ModifierAction

Defines an action that can be taken on modifiers.

JSON representation  
---  
      
    
    {
      "name": string
    }  
  
Fields  
---  
`name` |  `string` Required. The modifier action name -- e.g. "NO", "SIDE", "ADD", "EXTRA".  
  
## MenuCategory

Defines a category containing items or modifiers. Categories are used to organize items in user interfaces and for semantic grouping for the agent's understanding.

JSON representation  
---  
      
    
    {
      "id": string,
      "displayName": string,
      "description": string,
      "parentId": string
    }  
  
Fields  
---  
`id` |  `string` Required. Identifier for this menu category, unique within the menu.  
`displayName` |  `string` Optional. Human-readable name for this menu category to be used on user interfaces.  
`description` |  `string` Optional. Human-readable description.  
`parentId` |  `string` Optional. The parent menu category ID. If empty, this is a top-level category.  
  
## MenuLabel

String labels for describing a menu in UIs.

JSON representation  
---  
      
    
    {
      "name": string
    }  
  
Fields  
---  
`name` |  `string` Required. Name for the label.  
  
## MenuSchedule

Defines the menu schedule for items and modifiers.

JSON representation  
---  
      
    
    {
      "id": string,
      "schedules": [
        {
          object ([Schedule](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/Schedule))
        }
      ],
      "displayName": string
    }  
  
Fields  
---  
`id` |  `string` Optional. The schedule id, for instance "BREAKFAST", "LUNCH", etc.  
`schedules[]` |  `object (`[Schedule](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/Schedule)`)` Optional. Schedule active hours.  
`displayName` |  `string` Optional. Specifies an optional display name for this schedule.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus/create)`

|  Creates a menu.  
  
### `[delete](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus/delete)`

|  Deletes the specified menu.  
  
### `[get](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus/get)`

|  Gets a menu.  
  
### `[list](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus/list)`

|  Lists menus.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-23 UTC."],[],[]] 
