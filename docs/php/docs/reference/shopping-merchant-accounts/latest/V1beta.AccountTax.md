---
url: https://docs.cloud.google.com/php/docs/reference/shopping-merchant-accounts/latest/V1beta.AccountTax
title: Google Shopping Merchant Accounts V1beta Client - Class AccountTax (1.4.6) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:09:43.175618+00:00
---

# Google Shopping Merchant Accounts V1beta Client - Class AccountTax (1.4.6)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/shopping-merchant-accounts/latest/V1beta.AccountTax

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Shopping Merchant Accounts V1beta Client - Class AccountTax (1.4.6) Stay organized with collections  Save and categorize content based on your preferences. 

1.4.6 (latest)  1.4.1  1.3.1  1.2.2  1.1.0  1.0.0  0.10.0  0.9.1  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.3  0.2.0  0.1.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Shopping Merchant Accounts V1beta Client class AccountTax.

The tax settings of a merchant account. All methods require the admin role.

Generated from protobuf message `google.shopping.merchant.accounts.v1beta.AccountTax`

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
`↳ name` |  `string`   
Identifier. The name of the tax setting. Format: "{account_tax.name=accounts/{account}}"  
`↳ account` |  `int|string`   
Output only. The ID of the account to which these account tax settings belong.  
`↳ tax_rules` |  `array<[TaxRule](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-accounts/latest/V1beta.TaxRule)>`   
Tax rules. "Define the tax rules in each region. No tax will be presented if a region has no rule."  
  
### getName

Identifier. The name of the tax setting.

Format: "{account_tax.name=accounts/{account}}"

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setName

Identifier. The name of the tax setting.

Format: "{account_tax.name=accounts/{account}}"

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getAccount

Output only. The ID of the account to which these account tax settings belong.

**Returns**  
---  
**Type** | **Description**  
`int|string` |   
  
### setAccount

Output only. The ID of the account to which these account tax settings belong.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int|string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getTaxRules

Tax rules. "Define the tax rules in each region.

No tax will be presented if a region has no rule."

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<[TaxRule](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-accounts/latest/V1beta.TaxRule)>` |   
  
### setTaxRules

Tax rules. "Define the tax rules in each region.

No tax will be presented if a region has no rule."

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array<[TaxRule](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-accounts/latest/V1beta.TaxRule)>`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
