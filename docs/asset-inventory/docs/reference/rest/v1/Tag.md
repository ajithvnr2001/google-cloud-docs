---
url: https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Tag/
title: Tag \u00a0|\u00a0 Cloud Asset Inventory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:30:07.955064+00:00
---

# Tag  |  Cloud Asset Inventory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Tag/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud Asset Inventory ](https://docs.cloud.google.com/asset-inventory/docs)
  * [ Reference ](https://docs.cloud.google.com/asset-inventory/docs/asset-types)



Send feedback 

#  Tag Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



The key and value for a [tag](https://cloud.google.com/resource-manager/docs/tags/tags-overview).

JSON representation  
---  
      
    
    {
      "tagKey": string,
      "tagKeyId": string,
      "tagValue": string,
      "tagValueId": string
    }  
  
Fields  
---  
`tagKey` |  `string` TagKey namespaced name, in the format of {ORG_ID}/{TAG_KEY_SHORT_NAME}.  
`tagKeyId` |  `string` TagKey ID, in the format of tagKeys/{TAG_KEY_ID}.  
`tagValue` |  `string` TagValue namespaced name, in the format of {ORG_ID}/{TAG_KEY_SHORT_NAME}/{TAG_VALUE_SHORT_NAME}.  
`tagValueId` |  `string` TagValue ID, in the format of tagValues/{TAG_VALUE_ID}.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-08 UTC."],[],[]] 
