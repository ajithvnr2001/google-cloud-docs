---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/EncryptionSpec/
title: EncryptionSpec \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T04:45:25.049858+00:00
---

# EncryptionSpec  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/EncryptionSpec/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  EncryptionSpec Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



A customer-managed encryption key specification that can be applied to all created resources (e.g. `Conversation`).

JSON representation  
---  
      
    
    {
      "name": string,
      "kmsKey": string
    }  
  
Fields  
---  
`name` |  `string` Immutable. The resource name of the encryption key specification resource. Format: projects/{project}/locations/{location}/encryptionSpec  
`kmsKey` |  `string` Required. The name of customer-managed encryption key that is used to secure a resource and its sub-resources. If empty, the resource is secured by our default encryption key. Only the key in the same location as this resource is allowed to be used for encryption. Format: `projects/{project}/locations/{location}/keyRings/{keyRing}/cryptoKeys/{key}`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
