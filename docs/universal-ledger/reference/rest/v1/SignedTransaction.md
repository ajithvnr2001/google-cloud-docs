---
url: https://docs.cloud.google.com/universal-ledger/reference/rest/v1/SignedTransaction/
title: SignedTransaction \u00a0|\u00a0 Universal Ledger \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:53:06.286269+00:00
---

# SignedTransaction  |  Universal Ledger  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/universal-ledger/reference/rest/v1/SignedTransaction/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Universal Ledger ](https://docs.cloud.google.com/universal-ledger)
  * [ Reference ](https://docs.cloud.google.com/universal-ledger/reference/rpc)



Send feedback 

#  SignedTransaction Stay organized with collections  Save and categorize content based on your preferences. 

A transaction with attached signatures. To submit a transaction, this message should be serialized and included in a `SubmitTransactionRequest`.

JSON representation  
---  
      
    
    {
      "serializedClientTransaction": string,
      "senderSignature": string,
      "senderSigningKeySlot": enum ([KeySlot](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/KeySlot)),
      "otherSignatures": [
        string
      ],
      "otherSigningKeySlots": [
        enum ([KeySlot](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/KeySlot))
      ]
    }  
  
Fields  
---  
`serializedClientTransaction` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Required. A serialized `[ClientTransaction](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction)` with the transaction details.A base64-encoded string.  
`senderSignature` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Required. The signature of the transaction sender.The signature should be computed by signing the `serializedClientTransaction` bytes with their own private key.For a transaction chain, the bytes to be signed are computed as the concatenation of: - A digest of the serialized client transaction of the entire chain. - A digest of the serialized signed transaction of each unit in the chain, in the order they appear in the chain. The digests are computed using SHA-256.A base64-encoded string.  
`senderSigningKeySlot` |  `enum (`[KeySlot](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/KeySlot)`)` Optional. The key slot of the sender used to sign the transaction. Uses the primary slot of the sender account if not specified.  
`otherSignatures[]` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Optional. The signatures of accounts listed as additional transaction signatories. The number and order of these signatures must match the `signatories` field in the `[ClientTransaction](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientTransaction)`.The bytes to be signed are the same as those for the `senderSignature`, which each signatory should sign with their own private key.The number and identity of additional signatories depends on the particular transaction kind. For a transaction chain, one signature is needed for each account appearing either as the sender or as a signatory of a unit in the chain.A base64-encoded string.  
`otherSigningKeySlots[]` |  `enum (`[KeySlot](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/KeySlot)`)` Optional. The key slots of the accounts listed as additional transaction signatories. If set, the number and order of these key slots must match the `otherSignatures` field in the `[SignedTransaction](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/SignedTransaction)`. Defaults to the primary slot of each account if not specified.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-25 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-25 UTC."],[],[]] 
