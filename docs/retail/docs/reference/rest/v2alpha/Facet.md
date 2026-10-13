---
url: https://docs.cloud.google.com/retail/docs/reference/rest/v2alpha/Facet/
title: Facet \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:36:30.423779+00:00
---

# Facet  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/retail/docs/reference/rest/v2alpha/Facet/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Facet Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * FacetValue
    * JSON representation



A facet result.

JSON representation  
---  
      
    
    {
      "key": string,
      "values": [
        {
          object ([FacetValue](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/Facet#FacetValue))
        }
      ],
      "dynamicFacet": boolean
    }  
  
Fields  
---  
`key` |  `string` The key for this facet. E.g., "colorFamilies" or "price" or "attributes.attr1".  
`values[]` |  `object (`[FacetValue](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/Facet#FacetValue)`)` The facet values for this field.  
`dynamicFacet` |  `boolean` Whether the facet is dynamically generated.  
  
## FacetValue

A facet value which contains value names and their count.

JSON representation  
---  
      
    
    {
      "count": string,
      "minValue": number,
      "maxValue": number,
    
      // Union field facet_value can be only one of the following:
      "value": string,
      "interval": {
        object ([Interval](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/Interval))
      }
      // End of list of possible types for union field facet_value.
    }  
  
Fields  
---  
`count` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of items that have this facet value.  
`minValue` |  `number` The minimum value in the `[FacetValue.interval](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/Facet#FacetValue.FIELDS.interval)`. Only supported on numerical facets and returned if `[SearchRequest.FacetSpec.FacetKey.return_min_max](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/FacetSpec#FacetKey.FIELDS.return_min_max)` is true.  
`maxValue` |  `number` The maximum value in the `[FacetValue.interval](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/Facet#FacetValue.FIELDS.interval)`. Only supported on numerical facets and returned if `[SearchRequest.FacetSpec.FacetKey.return_min_max](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/FacetSpec#FacetKey.FIELDS.return_min_max)` is true.  
Union field `facet_value`. A facet value which contains values. `facet_value` can be only one of the following:  
`value` |  `string` Text value of a facet, such as "Black" for facet "colorFamilies".  
`interval` |  `object (`[Interval](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/Interval)`)` Interval value for a facet, such as [10, 20) for facet "price".  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
