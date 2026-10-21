---
url: https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ChangeAccountManager/
title: ChangeAccountManager \u00a0|\u00a0 Universal Ledger \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:47:53.400722+00:00
---

# ChangeAccountManager  |  Universal Ledger  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ChangeAccountManager/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Universal Ledger ](https://docs.cloud.google.com/universal-ledger)
  * [ Reference ](https://docs.cloud.google.com/universal-ledger/reference/rpc)



Send feedback 

#  ChangeAccountManager Stay organized with collections  Save and categorize content based on your preferences. 

Transfers the responsibility of managing a particular account to another manager. The sender must be the current account manager of the account and, to provide consent, the new manager must also sign this transaction.

JSON representation  
---  
      
    
    {
      "account": {
        object ([Entity](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Entity))
      },
      "accountId": string,
      "nextManager": {
        object ([Entity](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Entity))
      },
      "nextManagerId": string
    }  
  
Fields  
---  
`account  
**(deprecated)**` |  `object (`[Entity](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Entity)`)` This item is deprecated!Optional. Deprecated: Use `[accountId](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ChangeAccountManager#FIELDS.account_id)` instead. The ID of the account whose manager is to be changed.  
`accountId` |  `string` Optional. The ID of the account whose manager is to be changed. One of `account` or `accountId` must be specified. The value is limited to 60 characters.  
`nextManager  
**(deprecated)**` |  `object (`[Entity](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Entity)`)` This item is deprecated!Optional. Deprecated: Use `[nextManagerId](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ChangeAccountManager#FIELDS.next_manager_id)` instead. The ID of the new proposed account manager. Validation requires that the new manager has also signed this transaction.  
`nextManagerId` |  `string` Optional. The ID of the new proposed account manager. Validation requires that the new manager has also signed this transaction. One of `nextManager` or `nextManagerId` must be specified. The value is limited to 60 characters.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-26 UTC."],[],[]] 
