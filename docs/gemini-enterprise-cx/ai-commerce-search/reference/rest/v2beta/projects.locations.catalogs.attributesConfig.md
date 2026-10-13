---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig
title: REST Resource: projects.locations.catalogs.attributesConfig \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:39:26.120439+00:00
---

# REST Resource: projects.locations.catalogs.attributesConfig  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  REST Resource: projects.locations.catalogs.attributesConfig Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: AttributesConfig
    * JSON representation
  * CatalogAttribute
    * JSON representation
  * AttributeType
  * IndexableOption
  * DynamicFacetableOption
  * SearchableOption
  * ExactSearchableOption
  * RetrievableOption
  * FacetConfig
    * JSON representation
  * IgnoredFacetValues
    * JSON representation
  * MergedFacetValue
    * JSON representation
  * MergedFacet
    * JSON representation
  * RerankConfig
    * JSON representation
  * AttributeConfigLevel
  * Methods



## Resource: AttributesConfig

Catalog level attribute config.

JSON representation  
---  
      
    
    {
      "name": string,
      "catalogAttributes": {
        string: {
          object ([CatalogAttribute](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#CatalogAttribute))
        },
        ...
      },
      "attributeConfigLevel": enum ([AttributeConfigLevel](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#AttributeConfigLevel))
    }  
  
Fields  
---  
`name` |  `string` Required. Immutable. The fully qualified resource name of the attribute config. Format: `projects/*/locations/*/catalogs/*/attributesConfig`  
`catalogAttributes` |  `map (key: string, value: object (`[CatalogAttribute](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#CatalogAttribute)`))` Enable attribute(s) config at catalog level. For example, indexable, dynamicFacetable, or searchable for each attribute.The key is catalog attribute's name. For example: `color`, `brands`, `attributes.custom_attribute`, such as `attributes.xyz`.The maximum number of catalog attributes allowed in a request is 1000.  
`attributeConfigLevel` |  `enum (`[AttributeConfigLevel](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#AttributeConfigLevel)`)` Output only. The `[AttributeConfigLevel](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#AttributeConfigLevel)` used for this catalog.  
  
## CatalogAttribute

Catalog level attribute config for an attribute. For example, if customers want to enable/disable facet for a specific attribute.

JSON representation  
---  
      
    
    {
      "key": string,
      "inUse": boolean,
      "type": enum ([AttributeType](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#AttributeType)),
      "indexableOption": enum ([IndexableOption](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#IndexableOption)),
      "dynamicFacetableOption": enum ([DynamicFacetableOption](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#DynamicFacetableOption)),
      "searchableOption": enum ([SearchableOption](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#SearchableOption)),
      "recommendationsFilteringOption": enum ([RecommendationsFilteringOption](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/RecommendationsFilteringOption)),
      "exactSearchableOption": enum ([ExactSearchableOption](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#ExactSearchableOption)),
      "retrievableOption": enum ([RetrievableOption](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#RetrievableOption)),
      "facetConfig": {
        object ([FacetConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#FacetConfig))
      }
    }  
  
Fields  
---  
`key` |  `string` Required. Attribute name. For example: `color`, `brands`, `attributes.custom_attribute`, such as `attributes.xyz`. To be indexable, the attribute name can contain only alpha-numeric characters and underscores. For example, an attribute named `attributes.abc_xyz` can be indexed, but an attribute named `attributes.abc-xyz` cannot be indexed.If the attribute key starts with `attributes.`, then the attribute is a custom attribute. Attributes such as `brands`, `patterns`, and `title` are built-in and called system attributes.  
`inUse` |  `boolean` Output only. Indicates whether this attribute has been used by any products. `True` if at least one `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products#Product)` is using this attribute in `[Product.attributes](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products#Product.FIELDS.attributes)`. Otherwise, this field is `False`.`[CatalogAttribute](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#CatalogAttribute)` can be pre-loaded by using `[CatalogService.AddCatalogAttribute](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig/addCatalogAttribute#google.cloud.retail.v2beta.CatalogService.AddCatalogAttribute)` or `[CatalogService.UpdateAttributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs/updateAttributesConfig#google.cloud.retail.v2beta.CatalogService.UpdateAttributesConfig)` APIs. This field is `False` for pre-loaded `[CatalogAttribute](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#CatalogAttribute)`s.Only pre-loaded `[catalog attributes](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#CatalogAttribute)` that are neither in use by products nor predefined can be deleted. `[Catalog attributes](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#CatalogAttribute)` that are either in use by products or are predefined attributes cannot be deleted; however, their configuration properties will reset to default values upon removal request.After catalog changes, it takes about 10 minutes for this field to update.  
`type` |  `enum (`[AttributeType](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#AttributeType)`)` Output only. The type of this attribute. This is derived from the attribute in `[Product.attributes](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products#Product.FIELDS.attributes)`.  
`indexableOption` |  `enum (`[IndexableOption](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#IndexableOption)`)` When `[AttributesConfig.attribute_config_level](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#AttributesConfig.FIELDS.attribute_config_level)` is CATALOG_LEVEL_ATTRIBUTE_CONFIG, if INDEXABLE_ENABLED attribute values are indexed so that it can be filtered, faceted, or boosted in `[SearchService.Search](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.placements/search#google.cloud.retail.v2beta.SearchService.Search)`.Must be specified when `[AttributesConfig.attribute_config_level](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#AttributesConfig.FIELDS.attribute_config_level)` is CATALOG_LEVEL_ATTRIBUTE_CONFIG, otherwise throws INVALID_FORMAT error.  
`dynamicFacetableOption` |  `enum (`[DynamicFacetableOption](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#DynamicFacetableOption)`)` If DYNAMIC_FACETABLE_ENABLED, attribute values are available for dynamic facet. Could only be DYNAMIC_FACETABLE_DISABLED if `[CatalogAttribute.indexable_option](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#CatalogAttribute.FIELDS.indexable_option)` is INDEXABLE_DISABLED. Otherwise, an INVALID_ARGUMENT error is returned.Must be specified, otherwise throws INVALID_FORMAT error.  
`searchableOption` |  `enum (`[SearchableOption](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#SearchableOption)`)` When `[AttributesConfig.attribute_config_level](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#AttributesConfig.FIELDS.attribute_config_level)` is CATALOG_LEVEL_ATTRIBUTE_CONFIG, if SEARCHABLE_ENABLED, attribute values are searchable by text queries in `[SearchService.Search](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.placements/search#google.cloud.retail.v2beta.SearchService.Search)`.If SEARCHABLE_ENABLED but attribute type is numerical, attribute values will not be searchable by text queries in `[SearchService.Search](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.placements/search#google.cloud.retail.v2beta.SearchService.Search)`, as there are no text values associated to numerical attributes.Must be specified, when `[AttributesConfig.attribute_config_level](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#AttributesConfig.FIELDS.attribute_config_level)` is CATALOG_LEVEL_ATTRIBUTE_CONFIG, otherwise throws INVALID_FORMAT error.  
`recommendationsFilteringOption` |  `enum (`[RecommendationsFilteringOption](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/RecommendationsFilteringOption)`)` When `[AttributesConfig.attribute_config_level](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#AttributesConfig.FIELDS.attribute_config_level)` is CATALOG_LEVEL_ATTRIBUTE_CONFIG, if RECOMMENDATIONS_FILTERING_ENABLED, attribute values are filterable for recommendations. This option works for categorical features only, does not work for numerical features, inventory filtering.  
`exactSearchableOption` |  `enum (`[ExactSearchableOption](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#ExactSearchableOption)`)` If EXACT_SEARCHABLE_ENABLED, attribute values will be exact searchable. This property only applies to textual custom attributes and requires indexable set to enabled to enable exact-searchable. If unset, the server behavior defaults to `[EXACT_SEARCHABLE_DISABLED](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#ExactSearchableOption.ENUM_VALUES.EXACT_SEARCHABLE_DISABLED)`.  
`retrievableOption` |  `enum (`[RetrievableOption](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#RetrievableOption)`)` If RETRIEVABLE_ENABLED, attribute values are retrievable in the search results. If unset, the server behavior defaults to `[RETRIEVABLE_DISABLED](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#RetrievableOption.ENUM_VALUES.RETRIEVABLE_DISABLED)`.  
`facetConfig` |  `object (`[FacetConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#FacetConfig)`)` Contains facet options.  
  
## AttributeType

The type of an attribute.

Enums  
---  
`UNKNOWN` | The type of the attribute is unknown.Used when type cannot be derived from attribute that is not `[inUse](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#CatalogAttribute.FIELDS.in_use)`.  
`TEXTUAL` | Textual attribute.  
`NUMERICAL` | Numerical attribute.  
  
## IndexableOption

The status of the indexable option of a catalog attribute.

Enums  
---  
`INDEXABLE_OPTION_UNSPECIFIED` | Value used when unset.  
`INDEXABLE_ENABLED` | Indexable option enabled for an attribute.  
`INDEXABLE_DISABLED` | Indexable option disabled for an attribute.  
  
## DynamicFacetableOption

The status of the dynamic facetable option of a catalog attribute.

Enums  
---  
`DYNAMIC_FACETABLE_OPTION_UNSPECIFIED` | Value used when unset.  
`DYNAMIC_FACETABLE_ENABLED` | Dynamic facetable option enabled for an attribute.  
`DYNAMIC_FACETABLE_DISABLED` | Dynamic facetable option disabled for an attribute.  
  
## SearchableOption

The status of the searchable option of a catalog attribute.

Enums  
---  
`SEARCHABLE_OPTION_UNSPECIFIED` | Value used when unset.  
`SEARCHABLE_ENABLED` | Searchable option enabled for an attribute.  
`SEARCHABLE_DISABLED` | Searchable option disabled for an attribute.  
  
## ExactSearchableOption

The status of the exact-searchable option of a catalog attribute.

Enums  
---  
`EXACT_SEARCHABLE_OPTION_UNSPECIFIED` | Value used when unset.  
`EXACT_SEARCHABLE_ENABLED` | Exact searchable option enabled for an attribute.  
`EXACT_SEARCHABLE_DISABLED` | Exact searchable option disabled for an attribute.  
  
## RetrievableOption

The status of the retrievable option of a catalog attribute.

Enums  
---  
`RETRIEVABLE_OPTION_UNSPECIFIED` | Value used when unset.  
`RETRIEVABLE_ENABLED` | Retrievable option enabled for an attribute.  
`RETRIEVABLE_DISABLED` | Retrievable option disabled for an attribute.  
  
## FacetConfig

Possible options for the facet that corresponds to the current attribute config.

JSON representation  
---  
      
    
    {
      "facetIntervals": [
        {
          object ([Interval](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/Interval))
        }
      ],
      "ignoredFacetValues": [
        {
          object ([IgnoredFacetValues](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#IgnoredFacetValues))
        }
      ],
      "mergedFacetValues": [
        {
          object ([MergedFacetValue](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#MergedFacetValue))
        }
      ],
      "mergedFacet": {
        object ([MergedFacet](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#MergedFacet))
      },
      "rerankConfig": {
        object ([RerankConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#RerankConfig))
      }
    }  
  
Fields  
---  
`facetIntervals[]` |  `object (`[Interval](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/Interval)`)` If you don't set the facet `[SearchRequest.FacetSpec.FacetKey.intervals](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/FacetSpec#FacetKey.FIELDS.intervals)` in the request to a numerical attribute, then we use the computed intervals with rounded bounds obtained from all its product numerical attribute values. The computed intervals might not be ideal for some attributes. Therefore, we give you the option to overwrite them with the facetIntervals field. The maximum of facet intervals per `[CatalogAttribute](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#CatalogAttribute)` is 40. Each interval must have a lower bound or an upper bound. If both bounds are provided, then the lower bound must be smaller or equal than the upper bound.  
`ignoredFacetValues[]` |  `object (`[IgnoredFacetValues](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#IgnoredFacetValues)`)` Each instance represents a list of attribute values to ignore as facet values for a specific time range. The maximum number of instances per `[CatalogAttribute](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#CatalogAttribute)` is 25.  
`mergedFacetValues[]` |  `object (`[MergedFacetValue](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#MergedFacetValue)`)` Each instance replaces a list of facet values by a merged facet value. If a facet value is not in any list, then it will stay the same. To avoid conflicts, only paths of length 1 are accepted. In other words, if "dark_blue" merged into "BLUE", then the latter can't merge into "blues" because this would create a path of length 2. The maximum number of instances of MergedFacetValue per `[CatalogAttribute](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#CatalogAttribute)` is 100. This feature is available only for textual custom attributes.  
`mergedFacet` |  `object (`[MergedFacet](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#MergedFacet)`)` Use this field only if you want to merge a facet key into another facet key.  
`rerankConfig` |  `object (`[RerankConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#RerankConfig)`)` Set this field only if you want to rerank based on facet values engaged by the user for the current key. This option is only possible for custom facetable textual keys.  
  
## IgnoredFacetValues

`[Facet values](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/SearchResponse#Facet.FIELDS.values)` to ignore on `[facets](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/SearchResponse#Facet)` during the specified time range for the given `[SearchResponse.Facet.key](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/SearchResponse#Facet.FIELDS.key)` attribute.

JSON representation  
---  
      
    
    {
      "values": [
        string
      ],
      "startTime": string,
      "endTime": string
    }  
  
Fields  
---  
`values[]` |  `string` List of facet values to ignore for the following time range. The facet values are the same as the attribute values. There is a limit of 10 values per instance of IgnoredFacetValues. Each value can have at most 128 characters.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Time range for the current list of facet values to ignore. If multiple time ranges are specified for an facet value for the current attribute, consider all of them. If both are empty, ignore always. If start time and end time are set, then start time must be before end time. If start time is not empty and end time is empty, then will ignore these facet values after the start time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` If start time is empty and end time is not empty, then ignore these facet values before end time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## MergedFacetValue

Replaces a set of textual facet values by the same (possibly different) merged facet value. Each facet value should appear at most once as a value per `[CatalogAttribute](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#CatalogAttribute)`. This feature is available only for textual custom attributes.

JSON representation  
---  
      
    
    {
      "values": [
        string
      ],
      "mergedValue": string
    }  
  
Fields  
---  
`values[]` |  `string` All the facet values that are replaces by the same `[mergedValue](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#MergedFacetValue.FIELDS.merged_value)` that follows. The maximum number of values per MergedFacetValue is 25. Each value can have up to 128 characters.  
`mergedValue` |  `string` All the previous values are replaced by this merged facet value. This mergedValue must be non-empty and can have up to 128 characters.  
  
## MergedFacet

The current facet key (i.e. attribute config) maps into the `[mergedFacetKey](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#MergedFacet.FIELDS.merged_facet_key)`. A facet key can have at most one child. The current facet key and the merged facet key need both to be textual custom attributes or both numerical custom attributes (same type).

JSON representation  
---  
      
    
    {
      "mergedFacetKey": string
    }  
  
Fields  
---  
`mergedFacetKey` |  `string` The merged facet key should be a valid facet key that is different than the facet key of the current catalog attribute. We refer this is merged facet key as the child of the current catalog attribute. This merged facet key can't be a parent of another facet key (i.e. no directed path of length 2). This merged facet key needs to be either a textual custom attribute or a numerical custom attribute.  
  
## RerankConfig

Options to rerank based on facet values engaged by the user for the current key. That key needs to be a custom textual key and facetable. To use this control, you also need to pass all the facet keys engaged by the user in the request using the field [SearchRequest.FacetSpec]. In particular, if you don't pass the facet keys engaged that you want to rerank on, this control won't be effective. Moreover, to obtain better results, the facet values that you want to rerank on should be close to English (ideally made of words, underscores, and spaces).

JSON representation  
---  
      
    
    {
      "rerankFacet": boolean,
      "facetValues": [
        string
      ]
    }  
  
Fields  
---  
`rerankFacet` |  `boolean` If set to true, then we also rerank the dynamic facets based on the facet values engaged by the user for the current attribute key during serving.  
`facetValues[]` |  `string` If empty, rerank on all facet values for the current key. Otherwise, will rerank on the facet values from this list only.  
  
## AttributeConfigLevel

At which level we offer configuration for attributes.

Enums  
---  
`ATTRIBUTE_CONFIG_LEVEL_UNSPECIFIED` | Value used when unset. In this case, server behavior defaults to `[CATALOG_LEVEL_ATTRIBUTE_CONFIG](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#AttributeConfigLevel.ENUM_VALUES.CATALOG_LEVEL_ATTRIBUTE_CONFIG)`.  
`PRODUCT_LEVEL_ATTRIBUTE_CONFIG` | At this level, we honor the attribute configurations set in `[Product.attributes](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products#Product.FIELDS.attributes)`.  
`CATALOG_LEVEL_ATTRIBUTE_CONFIG` | At this level, we honor the attribute configurations set in `CatalogConfig.attribute_configs`.  
  
## Methods  
  
---  
  
### `[addCatalogAttribute](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig/addCatalogAttribute)`

|  Adds the specified `[CatalogAttribute](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#CatalogAttribute)` to the `[AttributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#AttributesConfig)`.  
  
### `[batchRemoveCatalogAttributes](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig/batchRemoveCatalogAttributes)`

|  Removes all specified `[CatalogAttribute](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#CatalogAttribute)`s from the `[AttributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#AttributesConfig)`.  
  
### `[removeCatalogAttribute](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig/removeCatalogAttribute)`

|  Removes the specified `[CatalogAttribute](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#CatalogAttribute)` from the `[AttributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#AttributesConfig)`.  
  
### `[replaceCatalogAttribute](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig/replaceCatalogAttribute)`

|  Replaces the specified `[CatalogAttribute](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#CatalogAttribute)` in the `[AttributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#AttributesConfig)` by updating the catalog attribute with the same `[CatalogAttribute.key](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#CatalogAttribute.FIELDS.key)`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
