---
url: https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.types.CatalogAttribute.FacetConfig
title: Class FacetConfig (2.14.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:26:00.439437+00:00
---

# Class FacetConfig (2.14.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.types.CatalogAttribute.FacetConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class FacetConfig (2.14.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.14.0 (latest)  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.25.0  1.24.0  1.23.1  1.22.0  1.21.2  1.20.1  1.19.1  1.18.0  1.17.0  1.16.3  1.15.1  1.14.1  1.13.0  1.12.0  1.11.0  1.10.2  1.9.0  1.8.1  1.7.0  1.6.1  1.5.0  1.4.1  1.3.0  1.2.1  1.1.0  1.0.2  0.4.2  0.3.1  0.2.0  0.1.0 
    
    
    FacetConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Possible options for the facet that corresponds to the current attribute config.

## Attributes  
  
---  
**Name** | **Description**  
`facet_intervals` |  `MutableSequence[[google.cloud.retail_v2.types.Interval](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.types.Interval)]`   
If you don't set the facet SearchRequest.FacetSpec.FacetKey.intervals in the request to a numerical attribute, then we use the computed intervals with rounded bounds obtained from all its product numerical attribute values. The computed intervals might not be ideal for some attributes. Therefore, we give you the option to overwrite them with the facet_intervals field. The maximum of facet intervals per CatalogAttribute is 40. Each interval must have a lower bound or an upper bound. If both bounds are provided, then the lower bound must be smaller or equal than the upper bound.   
`ignored_facet_values` |  `MutableSequence[[google.cloud.retail_v2.types.CatalogAttribute.FacetConfig.IgnoredFacetValues](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.types.CatalogAttribute.FacetConfig.IgnoredFacetValues)]`   
Each instance represents a list of attribute values to ignore as facet values for a specific time range. The maximum number of instances per CatalogAttribute is 25.   
`merged_facet_values` |  `MutableSequence[[google.cloud.retail_v2.types.CatalogAttribute.FacetConfig.MergedFacetValue](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.types.CatalogAttribute.FacetConfig.MergedFacetValue)]`   
Each instance replaces a list of facet values by a merged facet value. If a facet value is not in any list, then it will stay the same. To avoid conflicts, only paths of length 1 are accepted. In other words, if "dark_blue" merged into "BLUE", then the latter can't merge into "blues" because this would create a path of length 2. The maximum number of instances of MergedFacetValue per CatalogAttribute is 100. This feature is available only for textual custom attributes.   
`merged_facet` |  `[google.cloud.retail_v2.types.CatalogAttribute.FacetConfig.MergedFacet](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.types.CatalogAttribute.FacetConfig.MergedFacet)`   
Use this field only if you want to merge a facet key into another facet key.   
`rerank_config` |  `[google.cloud.retail_v2.types.CatalogAttribute.FacetConfig.RerankConfig](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.types.CatalogAttribute.FacetConfig.RerankConfig)`   
Set this field only if you want to rerank based on facet values engaged by the user for the current key. This option is only possible for custom facetable textual keys.   
  
## Classes 

### IgnoredFacetValues
    
    
    IgnoredFacetValues(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Facet values to ignore on facets during the specified time range for the given SearchResponse.Facet.key attribute.

### MergedFacet
    
    
    MergedFacet(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The current facet key (i.e. attribute config) maps into the merged_facet_key. A facet key can have at most one child. The current facet key and the merged facet key need both to be textual custom attributes or both numerical custom attributes (same type).

### MergedFacetValue
    
    
    MergedFacetValue(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Replaces a set of textual facet values by the same (possibly different) merged facet value. Each facet value should appear at most once as a value per CatalogAttribute. This feature is available only for textual custom attributes.

### RerankConfig
    
    
    RerankConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Options to rerank based on facet values engaged by the user for the current key. That key needs to be a custom textual key and facetable. To use this control, you also need to pass all the facet keys engaged by the user in the request using the field [SearchRequest.FacetSpec]. In particular, if you don't pass the facet keys engaged that you want to rerank on, this control won't be effective. Moreover, to obtain better results, the facet values that you want to rerank on should be close to English (ideally made of words, underscores, and spaces).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
