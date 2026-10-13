---
url: https://docs.cloud.google.com/php/docs/reference/shopping-merchant-accounts/latest/V1beta.Accepted
title: Google Shopping Merchant Accounts V1beta Client - Class Accepted (1.4.6) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:12:13.237608+00:00
---

# Google Shopping Merchant Accounts V1beta Client - Class Accepted (1.4.6)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/shopping-merchant-accounts/latest/V1beta.Accepted

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Shopping Merchant Accounts V1beta Client - Class Accepted (1.4.6) Stay organized with collections  Save and categorize content based on your preferences. 

1.4.6 (latest)  1.4.1  1.3.1  1.2.2  1.1.0  1.0.0  0.10.0  0.9.1  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.3  0.2.0  0.1.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Shopping Merchant Accounts V1beta Client class Accepted.

Describes the accepted terms of service.

Generated from protobuf message `google.shopping.merchant.accounts.v1beta.Accepted`

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
`↳ terms_of_service` |  `string`   
The accepted [termsOfService](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-accounts/latest/google.shopping.merchant.accounts.v1main.TermsOfService).  
`↳ accepted_by` |  `string`   
The account where the acceptance was recorded. This can be the account itself or, in the case of subaccounts, the MCA account.  
`↳ valid_until` |  `[Google\Type\Date](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Type.Date.html)`   
When set, it states that the accepted [TermsOfService](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-accounts/latest/google.shopping.merchant.accounts.v1main.TermsOfService) is only valid until the end of this date (in UTC). A new one must be accepted before then. The information of the required [TermsOfService](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-accounts/latest/google.shopping.merchant.accounts.v1main.TermsOfService) is found in the [Required](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-accounts/latest/Required) message.  
  
### getTermsOfService

The accepted [termsOfService](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-accounts/latest/google.shopping.merchant.accounts.v1main.TermsOfService).

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setTermsOfService

The accepted [termsOfService](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-accounts/latest/google.shopping.merchant.accounts.v1main.TermsOfService).

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getAcceptedBy

The account where the acceptance was recorded. This can be the account itself or, in the case of subaccounts, the MCA account.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setAcceptedBy

The account where the acceptance was recorded. This can be the account itself or, in the case of subaccounts, the MCA account.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getValidUntil

When set, it states that the accepted [TermsOfService](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-accounts/latest/google.shopping.merchant.accounts.v1main.TermsOfService) is only valid until the end of this date (in UTC). A new one must be accepted before then. The information of the required [TermsOfService](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-accounts/latest/google.shopping.merchant.accounts.v1main.TermsOfService) is found in the [Required](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-accounts/latest/Required) message.

**Returns**  
---  
**Type** | **Description**  
`[Google\Type\Date](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Type.Date.html)|null` |   
  
### hasValidUntil

### clearValidUntil

### setValidUntil

When set, it states that the accepted [TermsOfService](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-accounts/latest/google.shopping.merchant.accounts.v1main.TermsOfService) is only valid until the end of this date (in UTC). A new one must be accepted before then. The information of the required [TermsOfService](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-accounts/latest/google.shopping.merchant.accounts.v1main.TermsOfService) is found in the [Required](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-accounts/latest/Required) message.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Type\Date](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Type.Date.html)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
