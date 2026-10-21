---
url: https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Burn/
title: Burn \u00a0|\u00a0 Universal Ledger \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:53:05.325301+00:00
---

# Burn  |  Universal Ledger  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Burn/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Universal Ledger ](https://docs.cloud.google.com/universal-ledger)
  * [ Reference ](https://docs.cloud.google.com/universal-ledger/reference/rpc)



Send feedback 

#  Burn Stay organized with collections  Save and categorize content based on your preferences. 

Burns currency tokens. The sender must be a token manager and the account supplying the tokens to burn must additionally sign the transaction.

The expected flow is that the token manager will have its designated burn account which customers would transfer the tokens to before they are burnt. Alternatively, the customers could directly sign the transaction in which case it would act as an atomic "transfer-and-burn" transaction.

JSON representation  
---  
      
    
    {
      "burnAmount": {
        object ([CurrencyValue](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#CurrencyValue))
      },
      "payer": {
        object ([Entity](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Entity))
      },
      "payerId": string
    }  
  
Fields  
---  
`burnAmount` |  `object (`[CurrencyValue](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#CurrencyValue)`)` Required. The amount to burn.  
`payer  
**(deprecated)**` |  `object (`[Entity](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Entity)`)` This item is deprecated!Optional. Deprecated: Use `[payerId](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Burn#FIELDS.payer_id)` instead. The account supplying the tokens to burn. The account must have the `ROLE_PAYER` enabled on it.  
`payerId` |  `string` Optional. The ID of the account supplying the tokens to burn. The payer account must have the `ROLE_PAYER` enabled on it. One of `payer` or `payerId` must be specified.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-26 UTC."],[],[]] 
