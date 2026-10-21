---
url: https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.stores.discounts
title: REST Resource: projects.locations.brands.stores.discounts \u00a0|\u00a0 Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:50:57.208307+00:00
---

# REST Resource: projects.locations.brands.stores.discounts  |  Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.stores.discounts

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Food AI ](https://docs.cloud.google.com/food-ai)



Send feedback 

#  REST Resource: projects.locations.brands.stores.discounts Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Discount
    * JSON representation
  * DiscountType
  * Scope
  * ItemGroup
    * JSON representation
  * SelectItems
    * JSON representation
  * ItemMatcher
    * JSON representation
  * ModifierMatcher
    * JSON representation
  * AllOf
    * JSON representation
  * AnyOf
    * JSON representation
  * Constraint
    * JSON representation
  * DiscountIntegrationAttributes
    * JSON representation
  * Methods



## Resource: Discount

A discount that can be applied to orders at a store. Next ID: 16

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "type": enum ([DiscountType](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.stores.discounts#DiscountType)),
      "scope": enum ([Scope](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.stores.discounts#Scope)),
      "schedule": {
        object ([Schedule](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/Schedule))
      },
      "fixedAmount": {
        object ([Money](https://docs.cloud.google.com/food-ai/reference/rest/Shared.Types/Money))
      },
      "percent": number,
      "maxDiscountValue": {
        object ([Money](https://docs.cloud.google.com/food-ai/reference/rest/Shared.Types/Money))
      },
      "appliedItems": {
        object ([ItemGroup](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.stores.discounts#ItemGroup))
      },
      "requiredItems": {
        object ([ItemGroup](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.stores.discounts#ItemGroup))
      },
      "autoApply": boolean,
      "promoCode": string,
      "additionalConstraint": {
        object ([Constraint](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.stores.discounts#Constraint))
      },
      "integrationAttributes": {
        object ([DiscountIntegrationAttributes](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.stores.discounts#DiscountIntegrationAttributes))
      },
      "image": {
        object ([Image](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/Image))
      }
    }  
  
Fields  
---  
`name` |  `string` Identifier. The discount name. Format: projects/{project}/locations/{location}/brands/{brand}/stores/{store}/discounts/{discount}  
`displayName` |  `string` Required. The user-facing name of the discount (e.g., "20% Off Your Order").  
`type` |  `enum (`[DiscountType](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.stores.discounts#DiscountType)`)` Required. The type of discount being applied.  
`scope` |  `enum (`[Scope](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.stores.discounts#Scope)`)` Required. The scope at which the discount is applied.  
`schedule` |  `object (`[Schedule](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/Schedule)`)` Optional. The schedule when the discount is active.  
`fixedAmount` |  `object (`[Money](https://docs.cloud.google.com/food-ai/reference/rest/Shared.Types/Money)`)` Optional. The fixed monetary value of the discount or the fixed total price, depending on the 'type'.  
`percent` |  `number` Optional. The percentage value of the discount (0.0 to 100.0). Set when 'type' is PERCENT_OFF.  
`maxDiscountValue` |  `object (`[Money](https://docs.cloud.google.com/food-ai/reference/rest/Shared.Types/Money)`)` Optional. If the discount type is PERCENT_OFF, we can set a max discount value user can get.  
`appliedItems` |  `object (`[ItemGroup](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.stores.discounts#ItemGroup)`)` Optional. The group of items the discount is applied to. Required if 'scope' is ITEM. E.g. Bundles, mix-and-match, and the GET part of BOGO are defined here.  
`requiredItems` |  `object (`[ItemGroup](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.stores.discounts#ItemGroup)`)` Optional. The group of items that must be present in the cart to activate the discount only need to be set when discount type is BOGO. E.g. The BUY part of BOGO discount is defined here.  
`autoApply` |  `boolean` Optional. If true, the discount is automatically applied when the criteria are met.  
`promoCode` |  `string` Optional. The code required to apply the discount.  
`additionalConstraint` |  `object (`[Constraint](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.stores.discounts#Constraint)`)` Optional. Additional constraint to apply this discount.  
`integrationAttributes` |  `object (`[DiscountIntegrationAttributes](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.stores.discounts#DiscountIntegrationAttributes)`)` Optional. Metadata associated with this entity used for downstream integrations.  
`image` |  `object (`[Image](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/Image)`)` Optional. Image to display for this discount in the UI.  
  
## DiscountType

The type of a discount.

Enums  
---  
`DISCOUNT_TYPE_UNSPECIFIED` | Unspecified discount type.  
`BOGO` | Buy X, Get Y Free/Z Percent Off/For Z amount.  
`FIXED_OFF` | A fixed monetary amount discount (e.g., $5.00 off an item or order).  
`PERCENT_OFF` | A percentage discount (e.g., 20% off an item or order).  
`FIXED_TOTAL` | Sets the final price of the discounted items to a fixed total (e.g., 2 items for $10.00).  
`FREE_DELIVERY` | Waives the delivery fee for the order.  
  
## Scope

Defines the level at which the discount is applied.

Enums  
---  
`SCOPE_UNSPECIFIED` | Unspecified scope.  
`ORDER` | Applied to the entire order.  
`ITEM` | Applied to specific items.  
  
## ItemGroup

A collection of items from the menu, defined by selection criteria, used to specify required or applied items for a discount. Next ID: 6

JSON representation  
---  
      
    
    {
      "name": string,
    
      // Union field type can be only one of the following:
      "selectItems": {
        object ([SelectItems](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.stores.discounts#SelectItems))
      },
      "allOf": {
        object ([AllOf](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.stores.discounts#AllOf))
      },
      "anyOf": {
        object ([AnyOf](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.stores.discounts#AnyOf))
      }
      // End of list of possible types for union field type.
    }  
  
Fields  
---  
`name` |  `string` Optional. Name of the item group.  
Union field `type`. The type of item group. `type` can be only one of the following:  
`selectItems` |  `object (`[SelectItems](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.stores.discounts#SelectItems)`)` A list of matchers. An item is considered a match if it satisfies ANY of these ItemMatcher criteria (OR logic).  
`allOf` |  `object (`[AllOf](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.stores.discounts#AllOf)`)` Represents a logical AND of sub-groups.  
`anyOf` |  `object (`[AnyOf](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.stores.discounts#AnyOf)`)` Represents a logical OR of sub-groups.  
  
## SelectItems

Defines a requirement to select a specific quantity of items where each item matches ANY of the provided ItemCriteria.

JSON representation  
---  
      
    
    {
      "matches": [
        {
          object ([ItemMatcher](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.stores.discounts#ItemMatcher))
        }
      ],
      "minQuantity": integer,
      "maxQuantity": integer
    }  
  
Fields  
---  
`matches[]` |  `object (`[ItemMatcher](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.stores.discounts#ItemMatcher)`)` Required. Matchers for the items.  
`minQuantity` |  `integer` Optional. Minimum quantity required for a match.  
`maxQuantity` |  `integer` Optional. Maximum quantity allowed for a match.  
  
## ItemMatcher

Defines the criteria for matching a single item. All specified fields are combined using AND. Next ID: 5

JSON representation  
---  
      
    
    {
      "itemId": string,
      "modifierId": string,
      "categoryId": string,
      "modifierMatcher": {
        object ([ModifierMatcher](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.stores.discounts#ModifierMatcher))
      }
    }  
  
Fields  
---  
`itemId` |  `string` Optional. Item ID to match.  
`modifierId` |  `string` Optional. Modifier ID to match.  
`categoryId` |  `string` Optional. Category ID to match.  
`modifierMatcher` |  `object (`[ModifierMatcher](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.stores.discounts#ModifierMatcher)`)` Optional. Defines the criteria for modifiers in order to match the Item.  
  
## ModifierMatcher

Defines the criteria for matching modifiers.

JSON representation  
---  
      
    
    {
      "allowedModifierIds": [
        string
      ],
      "minModifiers": integer,
      "maxModifiers": integer
    }  
  
Fields  
---  
`allowedModifierIds[]` |  `string` Optional. Modifier id that are required in order to apply the discount.  
`minModifiers` |  `integer` Optional. The minimum number of modifiers required for a match. If required_modifier_ids is set, will only count modifiers in the list.  
`maxModifiers` |  `integer` Optional. The maximum number of modifiers allowed for a match. If required_modifier_ids is set, will only count modifiers in the list.  
  
## AllOf

Represents a logical AND of sub-groups.

JSON representation  
---  
      
    
    {
      "groups": [
        {
          object ([ItemGroup](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.stores.discounts#ItemGroup))
        }
      ]
    }  
  
Fields  
---  
`groups[]` |  `object (`[ItemGroup](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.stores.discounts#ItemGroup)`)` Required. Sub-groups components.  
  
## AnyOf

Represents a logical OR of sub-groups.

JSON representation  
---  
      
    
    {
      "groups": [
        {
          object ([ItemGroup](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.stores.discounts#ItemGroup))
        }
      ]
    }  
  
Fields  
---  
`groups[]` |  `object (`[ItemGroup](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.stores.discounts#ItemGroup)`)` Required. Sub-groups components.  
  
## Constraint

Additional constraint to apply this discount.

JSON representation  
---  
      
    
    {
      "minSpend": {
        object ([Money](https://docs.cloud.google.com/food-ai/reference/rest/Shared.Types/Money))
      },
      "maxUsesPerOrder": integer,
      "allowedChannels": [
        enum ([ChannelType](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/ChannelType))
      ],
      "requiresCustomerSignin": boolean,
      "isStackable": boolean
    }  
  
Fields  
---  
`minSpend` |  `object (`[Money](https://docs.cloud.google.com/food-ai/reference/rest/Shared.Types/Money)`)` Optional. Min spend in order to apply this discount.  
`maxUsesPerOrder` |  `integer` Optional. How many times can this discount being used per order.  
`allowedChannels[]` |  `enum (`[ChannelType](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/ChannelType)`)` Optional. Channels this discount can be applied. If not set, the discount can be applied to all channels.  
`requiresCustomerSignin` |  `boolean` Optional. For mobile orders, if we need customer to signin to get this discount.  
`isStackable` |  `boolean` Optional. If this discount can be used with other discount.  
  
## DiscountIntegrationAttributes

Metadata associated with a discount used for downstream integrations.

JSON representation  
---  
      
    
    {
      "customIntegrationAttributes": {
        object
      }
    }  
  
Fields  
---  
`customIntegrationAttributes` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. Arbitrary metadata to be associated with an entity, used to build downstream integrations, i.e. identifiers or schema information for constructing an order for submission to a third-party point of sale API.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.stores.discounts/create)`

|  Creates a discount.  
  
### `[delete](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.stores.discounts/delete)`

|  Deletes the specified discount.  
  
### `[get](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.stores.discounts/get)`

|  Gets a discount.  
  
### `[list](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.stores.discounts/list)`

|  Lists discounts.  
  
### `[patch](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.stores.discounts/patch)`

|  Updates the specified discount.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-21 UTC."],[],[]] 
