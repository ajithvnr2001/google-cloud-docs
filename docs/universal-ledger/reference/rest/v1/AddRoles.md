---
url: https://docs.cloud.google.com/universal-ledger/reference/rest/v1/AddRoles/
title: AddRoles \u00a0|\u00a0 Universal Ledger \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:53:05.420492+00:00
---

# AddRoles  |  Universal Ledger  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/universal-ledger/reference/rest/v1/AddRoles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Universal Ledger ](https://docs.cloud.google.com/universal-ledger)
  * [ Reference ](https://docs.cloud.google.com/universal-ledger/reference/rpc)



Send feedback 

#  AddRoles Stay organized with collections  Save and categorize content based on your preferences. 

Adds the specified roles to the account. The sender must be the account manager of the account to modify.

JSON representation  
---  
      
    
    {
      "account": {
        object ([Entity](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Entity))
      },
      "accountId": string,
      "roles": [
        enum ([Role](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Role))
      ]
    }  
  
Fields  
---  
`account  
**(deprecated)**` |  `object (`[Entity](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Entity)`)` This item is deprecated!Optional. Deprecated: Use `[accountId](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/AddRoles#FIELDS.account_id)` instead. The ID of the account to be modified.  
`accountId` |  `string` Optional. The ID of the account to be modified. One of `account` or `accountId` must be specified. The value is limited to 60 characters.  
`roles[]` |  `enum (`[Role](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account#Role)`)` Required. The roles to be added.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-26 UTC."],[],[]] 
