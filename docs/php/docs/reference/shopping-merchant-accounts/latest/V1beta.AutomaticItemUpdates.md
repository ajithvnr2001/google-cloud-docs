---
url: https://docs.cloud.google.com/php/docs/reference/shopping-merchant-accounts/latest/V1beta.AutomaticItemUpdates
title: Google Shopping Merchant Accounts V1beta Client - Class AutomaticItemUpdates (1.4.6) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:23:43.822304+00:00
---

# Google Shopping Merchant Accounts V1beta Client - Class AutomaticItemUpdates (1.4.6)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/shopping-merchant-accounts/latest/V1beta.AutomaticItemUpdates

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Shopping Merchant Accounts V1beta Client - Class AutomaticItemUpdates (1.4.6) Stay organized with collections  Save and categorize content based on your preferences. 

1.4.6 (latest)  1.4.1  1.3.1  1.2.2  1.1.0  1.0.0  0.10.0  0.9.1  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.3  0.2.0  0.1.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Shopping Merchant Accounts V1beta Client class AutomaticItemUpdates.

Turning on [item updates](https://support.google.com/merchants/answer/3246284) allows Google to automatically update items for you. When item updates are on, Google uses the structured data markup on the website and advanced data extractors to update the price and availability of the items. When the item updates are off, items with mismatched data aren't shown.

Generated from protobuf message `google.shopping.merchant.accounts.v1beta.AutomaticItemUpdates`

## Namespace

Google \ Shopping \ Merchant \ Accounts \ V1beta

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ account_item_updates_settings` |  `[AutomaticItemUpdates\ItemUpdatesAccountLevelSettings](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-accounts/latest/V1beta.AutomaticItemUpdates.ItemUpdatesAccountLevelSettings)`   
Optional. Determines which attributes of the items should be automatically updated. If this field is not present and provided in the update mask, then the settings will be deleted. If there are no settings for subaccount, they are inherited from aggregator.  
`↳ effective_allow_price_updates` |  `bool`   
Output only. The effective value of allow_price_updates. If account_item_updates_settings is present, then this value is the same. Otherwise, it represents the inherited value of the parent account. The default value is true if no settings are present. Read-only.  
`↳ effective_allow_availability_updates` |  `bool`   
Output only. The effective value of allow_availability_updates. If account_item_updates_settings is present, then this value is the same. Otherwise, it represents the inherited value of the parent account. The default value is true if no settings are present. Read-only.  
`↳ effective_allow_strict_availability_updates` |  `bool`   
Output only. The effective value of allow_strict_availability_updates. If account_item_updates_settings is present, then this value is the same. Otherwise, it represents the inherited value of the parent account. The default value is true if no settings are present. Read-only.  
`↳ effective_allow_condition_updates` |  `bool`   
Output only. The effective value of allow_condition_updates. If account_item_updates_settings is present, then this value is the same. Otherwise, it represents the inherited value of the parent account. The default value is true if no settings are present. Read-only.  
  
### getAccountItemUpdatesSettings

Optional. Determines which attributes of the items should be automatically updated. If this field is not present and provided in the update mask, then the settings will be deleted. If there are no settings for subaccount, they are inherited from aggregator.

**Returns**  
---  
**Type** | **Description**  
`[AutomaticItemUpdates\ItemUpdatesAccountLevelSettings](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-accounts/latest/V1beta.AutomaticItemUpdates.ItemUpdatesAccountLevelSettings)|null` |   
  
### hasAccountItemUpdatesSettings

### clearAccountItemUpdatesSettings

### setAccountItemUpdatesSettings

Optional. Determines which attributes of the items should be automatically updated. If this field is not present and provided in the update mask, then the settings will be deleted. If there are no settings for subaccount, they are inherited from aggregator.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[AutomaticItemUpdates\ItemUpdatesAccountLevelSettings](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-accounts/latest/V1beta.AutomaticItemUpdates.ItemUpdatesAccountLevelSettings)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getEffectiveAllowPriceUpdates

Output only. The effective value of allow_price_updates.

If account_item_updates_settings is present, then this value is the same. Otherwise, it represents the inherited value of the parent account. The default value is true if no settings are present. Read-only.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### setEffectiveAllowPriceUpdates

Output only. The effective value of allow_price_updates.

If account_item_updates_settings is present, then this value is the same. Otherwise, it represents the inherited value of the parent account. The default value is true if no settings are present. Read-only.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getEffectiveAllowAvailabilityUpdates

Output only. The effective value of allow_availability_updates.

If account_item_updates_settings is present, then this value is the same. Otherwise, it represents the inherited value of the parent account. The default value is true if no settings are present. Read-only.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### setEffectiveAllowAvailabilityUpdates

Output only. The effective value of allow_availability_updates.

If account_item_updates_settings is present, then this value is the same. Otherwise, it represents the inherited value of the parent account. The default value is true if no settings are present. Read-only.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getEffectiveAllowStrictAvailabilityUpdates

Output only. The effective value of allow_strict_availability_updates.

If account_item_updates_settings is present, then this value is the same. Otherwise, it represents the inherited value of the parent account. The default value is true if no settings are present. Read-only.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### setEffectiveAllowStrictAvailabilityUpdates

Output only. The effective value of allow_strict_availability_updates.

If account_item_updates_settings is present, then this value is the same. Otherwise, it represents the inherited value of the parent account. The default value is true if no settings are present. Read-only.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getEffectiveAllowConditionUpdates

Output only. The effective value of allow_condition_updates.

If account_item_updates_settings is present, then this value is the same. Otherwise, it represents the inherited value of the parent account. The default value is true if no settings are present. Read-only.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### setEffectiveAllowConditionUpdates

Output only. The effective value of allow_condition_updates.

If account_item_updates_settings is present, then this value is the same. Otherwise, it represents the inherited value of the parent account. The default value is true if no settings are present. Read-only.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
