---
url: https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/EffectiveTagDetails/
title: EffectiveTagDetails \u00a0|\u00a0 Cloud Asset Inventory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:30:06.796891+00:00
---

# EffectiveTagDetails  |  Cloud Asset Inventory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/EffectiveTagDetails/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud Asset Inventory ](https://docs.cloud.google.com/asset-inventory/docs)
  * [ Reference ](https://docs.cloud.google.com/asset-inventory/docs/asset-types)



Send feedback 

#  EffectiveTagDetails Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



The effective tags and the ancestor resources from which they were inherited.

JSON representation  
---  
      
    
    {
      "effectiveTags": [
        {
          object ([Tag](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Tag))
        }
      ],
      "attachedResource": string
    }  
  
Fields  
---  
`effectiveTags[]` |  `object (`[Tag](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Tag)`)` The effective tags inherited from the `[attachedResource](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/EffectiveTagDetails#FIELDS.attached_resource)`. Note that tags with the same key but different values may attach to resources at a different hierarchy levels. The lower hierarchy tag value will overwrite the higher hierarchy tag value of the same tag key. In this case, the tag value at the higher hierarchy level will be removed. For more information, see [tag inheritance](https://cloud.google.com/resource-manager/docs/tags/tags-overview#inheritance).  
`attachedResource` |  `string` The [full resource name](https://cloud.google.com/asset-inventory/docs/resource-name-format) of the ancestor from which `[effectiveTags](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/EffectiveTagDetails#FIELDS.effective_tags)` are inherited, according to [tag inheritance](https://cloud.google.com/resource-manager/docs/tags/tags-overview#inheritance).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-30 UTC."],[],[]] 
